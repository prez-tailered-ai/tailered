// Proves the 25 NVIDIA specialists are byte-identical to what was imported: every line of references/signed-sha256.txt
// (sha256, path under skills/nvidia, original path) must match the file now. Byte identity only; it does not verify the sigstore signatures.
// Usage: node check-signed.mjs [--self-test]
import fs from 'node:fs'; import path from 'node:path'; import os from 'node:os'; import {createHash} from 'node:crypto'; import {fileURLToPath} from 'node:url';
const ROOT = fileURLToPath(new URL('..', import.meta.url));
export function check(root, list = path.join(root, 'references/signed-sha256.txt')) {
  const bad = [], rows = fs.readFileSync(list, 'utf8').trim().split('\n');
  for (const row of rows) {
    const [sha, rel] = row.split('  '), f = path.join(root, rel);
    if (!fs.existsSync(f)) bad.push(`missing ${rel}`);
    else if (createHash('sha256').update(fs.readFileSync(f)).digest('hex') !== sha) bad.push(`changed ${rel}`);
  }
  // an added file inside a specialist folder is also drift: list every file under the specialists and compare
  const listed = new Set(rows.map(r => r.split('  ')[1]));
  for (const area of fs.readdirSync(root, {withFileTypes: true}).filter(d => d.isDirectory() && !['references', 'scripts'].includes(d.name)))
    for (const f of fs.readdirSync(path.join(root, area.name), {recursive: true}).map(String))
      if (fs.statSync(path.join(root, area.name, f)).isFile() && !listed.has(`${area.name}/${f}`)) bad.push(`added ${area.name}/${f}`);
  return {rows: rows.length, bad};
}
if (process.argv.includes('--self-test')) {   // a changed byte and a missing file must both be caught
  const T = fs.mkdtempSync(path.join(os.tmpdir(), 'tailered-nvidia-signed-')); fs.mkdirSync(path.join(T, 'references'));
  fs.writeFileSync(path.join(T, 'a.md'), 'x'); fs.writeFileSync(path.join(T, 'b.md'), 'y');
  const sha = s => createHash('sha256').update(s).digest('hex');
  fs.mkdirSync(path.join(T, 'area')); fs.writeFileSync(path.join(T, 'area/a.md'), 'x'); fs.writeFileSync(path.join(T, 'area/b.md'), 'y');
  fs.writeFileSync(path.join(T, 'references/signed-sha256.txt'), `${sha('x')}  area/a.md  o/a.md\n${sha('y')}  area/b.md  o/b.md\n`);
  const clean = check(T).bad.length === 0; fs.writeFileSync(path.join(T, 'area/a.md'), 'z'); fs.rmSync(path.join(T, 'area/b.md')); fs.writeFileSync(path.join(T, 'area/new.md'), 'n');
  const r = check(T), ok = clean && r.bad.includes('changed area/a.md') && r.bad.includes('missing area/b.md') && r.bad.includes('added area/new.md');
  fs.rmSync(T, {recursive: true}); console.log(ok ? 'self-test PASS (clean ok, changed, missing and added caught)' : 'self-test FAIL'); process.exit(ok ? 0 : 1);
}
const {rows, bad} = check(ROOT); for (const b of bad) console.log('FAIL ' + b);
console.log(bad.length ? `${bad.length} of ${rows} files differ` : `PASS ${rows}/${rows} files byte-identical`); process.exit(bad.length ? 1 : 0);
