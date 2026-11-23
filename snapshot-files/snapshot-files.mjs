
import { closeSync, constants, fstatSync, openSync, readFileSync, readdirSync } from "node:fs";
import { join, relative, resolve } from "node:path";

import { sha256Bytes } from "./hash.mjs";

export function snapshotFiles(paths, base, excludedPrefixes = []) {
  const files = [];
  const excluded = excludedPrefixes.map((path) => path.split("\\").join("/").replace(/^(\.\/)+/, "").replace(/\/$/, ""));
  const taken = new Set();
  // Plain code-point order, so two machines with different locales produce the same list.
  const byCodePoint = (a, b) => (a < b ? -1 : a > b ? 1 : 0);
  function visit(path) {
    const relativePath = relative(base, path).split("\\").join("/");
    if (excluded.some((prefix) => relativePath === prefix || relativePath.startsWith(`${prefix}/`))) return;
    // ONE path resolution, and the kernel performs the symlink refusal during it.
    // lstat-then-open resolved the path twice, so the thing checked and the thing opened
    // were not guaranteed to be the same inode. O_NOFOLLOW
    // fails with ELOOP on a symlink at open time, which is the same refusal enforced with
    // no window instead of a look followed by a hope. The file read below uses this handle;
    // a directory is listed by its path.
    let handle;
    try {
      // O_NONBLOCK is what stops a FIFO, socket or device node from hanging this walker. The open
      // happens BEFORE the type check -- that is the point, it is what makes the resolution single
      // and the symlink refusal kernel-enforced -- but O_NOFOLLOW only refuses symlinks. POSIX has
      // open(fifo, O_RDONLY) block until a writer appears, and measured here it never returned
      // (killed at 12s) while the same FIFO with O_NONBLOCK opened in 1ms. One FIFO under the
      // snapshot root would hang the process forever, and a snapshot that never finishes is worse
      // than one that refuses. On a regular file the flag is a no-op.
      handle = openSync(path, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
    } catch (error) {
      if (error?.code === "ELOOP") {
        throw new Error(`source snapshot refuses symbolic link: ${path}`);
      }
      throw error;
    }
    let bytes;
    try {
      const stat = fstatSync(handle);
      if (stat.isDirectory()) {
        closeSync(handle);
        handle = null;
        // Filter on the dirent type rather than opening and recovering: O_NONBLOCK stops a
        // FIFO hanging but a socket refuses open() outright (macOS: "Unknown system error
        // -102"), which aborted the entire walk. Symlinks stay in so the explicit ELOOP
        // refusal still fires -- dropping them here would downgrade a stated refusal to a
        // silent skip, which is the opposite of what that check is for.
        const entries = readdirSync(path, { withFileTypes: true })
          .filter((entry) => entry.isFile() || entry.isDirectory() || entry.isSymbolicLink())
          .sort((a, b) => byCodePoint(a.name, b.name));
        for (const entry of entries) visit(join(path, entry.name));
        return;
      }
      if (!stat.isFile()) return;
      bytes = readFileSync(handle);
    } finally {
      if (handle !== null) closeSync(handle);
    }
    // The same file reached through two listed paths is recorded once.
    if (taken.has(relativePath)) return;
    taken.add(relativePath);
    files.push({
      path: relativePath,
      byte_length: bytes.length,
      sha256: sha256Bytes(bytes),
    });
  }
  for (const path of paths) visit(resolve(base, path));
  return files.sort((a, b) => byCodePoint(a.path, b.path));
}
