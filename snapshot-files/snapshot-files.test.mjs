import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { mkdirSync, mkdtempSync, symlinkSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";

import { snapshotFiles } from "./snapshot-files.mjs";

/* ---------------------------------------- the walker must not block on a non-regular file */

// The O_NOFOLLOW restructure moved the open BEFORE the type check -- fstat and
// the isFile() guard both run after it -- where the lstat-based code it replaced returned on
// anything that was not a regular file before opening anything.
//
// O_NOFOLLOW refuses symlinks and says nothing about FIFOs. POSIX: open(fifo, O_RDONLY) blocks
// until a writer opens the other end. Measured: a regular file opens in 0ms, the same FIFO with
// O_NONBLOCK opens in 1ms, and without it the call never returned (killed at 12s). One FIFO
// anywhere under the snapshot root hangs the process forever, and a snapshot that never finishes
// is worse than one that refuses.

test("a FIFO in the tree is skipped rather than blocking forever", { timeout: 15000 }, () => {
  const base = mkdtempSync(join(tmpdir(), "snap-fifo-"));
  writeFileSync(join(base, "a.txt"), "one\n");
  execFileSync("mkfifo", [join(base, "pipe")]);
  writeFileSync(join(base, "z.txt"), "two\n");

  const files = snapshotFiles(["."], base);
  const names = files.map((f) => f.path).sort();
  assert.deepEqual(names, ["a.txt", "z.txt"], `FIFO was not skipped cleanly: ${JSON.stringify(names)}`);
});

test("a symlink is still refused, not merely skipped", () => {
  // The refusal is the reason the open carries O_NOFOLLOW at all; adding O_NONBLOCK must not
  // weaken it into a silent skip.
  const base = mkdtempSync(join(tmpdir(), "snap-link-"));
  writeFileSync(join(base, "a.txt"), "one\n");
  symlinkSync("/etc/passwd", join(base, "link"));
  assert.throws(() => snapshotFiles(["."], base), /refuses symbolic link/);
});

test("ordinary files still snapshot with their digests", () => {
  const base = mkdtempSync(join(tmpdir(), "snap-ok-"));
  writeFileSync(join(base, "a.txt"), "one\n");
  mkdirSync(join(base, "sub"));
  writeFileSync(join(base, "sub", "b.txt"), "two\n");

  const files = snapshotFiles(["."], base);
  assert.deepEqual(files.map((f) => f.path), ["a.txt", "sub/b.txt"]);
  assert.ok(files.every((f) => /^[0-9a-f]{64}$/.test(f.sha256)));
  assert.equal(files[0].byte_length, 4);
});

// O_NONBLOCK stopped the FIFO from hanging, but it only makes the open non-blocking -- it does
// not make it succeed. A unix socket refuses open() outright: measured on macOS, snapshotting a
// directory containing one aborts the WHOLE walk with
//     Unknown system error -102: ... open '/tmp/sock-XXXX/s.sock'
// so a.txt and z.txt are never recorded and the operator gets a bare errno naming nothing they
// can act on. Same root cause as the FIFO -- opening a thing that is not a regular file -- half
// fixed. The type is already in the directory entry, so the walker should never reach for it.
test("a unix socket in the tree is skipped rather than aborting the snapshot", { timeout: 15000 }, async () => {
  const net = await import("node:net");
  const base = mkdtempSync(join(tmpdir(), "snap-sock-"));
  writeFileSync(join(base, "a.txt"), "one\n");
  writeFileSync(join(base, "z.txt"), "two\n");
  const server = net.createServer();
  await new Promise((resolve) => server.listen(join(base, "s.sock"), resolve));
  try {
    const names = snapshotFiles(["."], base).map((f) => f.path).sort();
    assert.deepEqual(names, ["a.txt", "z.txt"], `socket was not skipped cleanly: ${JSON.stringify(names)}`);
  } finally {
    server.close();
  }
});

test("order is by code point, a file listed twice is recorded once, and ./ exclusions apply", () => {
  const base = mkdtempSync(join(tmpdir(), "snap-order-"));
  for (const name of ["_x", "a", "B", "Z"]) writeFileSync(join(base, name), name);
  mkdirSync(join(base, "real"));
  writeFileSync(join(base, "real", "f.txt"), "f");
  mkdirSync(join(base, "skip"));
  writeFileSync(join(base, "skip", "g.txt"), "g");
  const files = snapshotFiles([".", "real", "real/f.txt"], base, ["./skip"]);
  assert.deepEqual(files.map((f) => f.path), ["B", "Z", "_x", "a", "real/f.txt"]);
});
