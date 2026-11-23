#!/usr/bin/env node
// Tailered continuous learning store. Node stdlib only.
//   lessons.mjs status
//   lessons.mjs add --trigger=... --action=... --confidence=0.3-0.9 --evidence=... [--scope=project|global]
//   lessons.mjs --self-test
// Writes $XDG_DATA_HOME/tailered-workflow/instincts.jsonl (default ~/.local/share). Past 1 MiB it rotates to instincts.1.jsonl; an older instincts.1.jsonl is first kept as instincts.<time>.jsonl, never overwritten.
import fs from 'node:fs'; import os from 'node:os'; import path from 'node:path';
const MAX = 1 << 20;
const dirFor = env => path.join(env.XDG_DATA_HOME ?? path.join(env.HOME ?? os.homedir(), '.local/share'), 'tailered-workflow');
const size = f => fs.statSync(f, {throwIfNoEntry: false})?.size ?? 0;
const parse = argv => Object.fromEntries(argv.filter(s => s.startsWith('--')).map(s => s.slice(2).split(/=(.*)/s).slice(0, 2)));

function add(dir, a) {
  const c = Number(a.confidence);
  if (!(c >= 0.3 && c <= 0.9)) throw new Error('confidence must be a number from 0.3 to 0.9');
  for (const k of ['trigger', 'action', 'evidence']) if (!a[k]) throw new Error(`missing --${k}=`);
  const scope = a.scope ?? 'project';
  if (!['project', 'global'].includes(scope)) throw new Error('scope must be project or global');
  fs.mkdirSync(dir, {recursive: true});
  const log = path.join(dir, 'instincts.jsonl');
  if (size(log) > MAX) { const one = path.join(dir, 'instincts.1.jsonl'); if (fs.existsSync(one)) fs.renameSync(one, path.join(dir, `instincts.${Date.now()}.jsonl`)); fs.renameSync(log, one); }
  fs.appendFileSync(log, JSON.stringify({at: new Date().toISOString(), trigger: a.trigger, action: a.action, confidence: c, evidence: a.evidence, scope}) + '\n');
}

function status(dir) {
  const lines = [];
  let n = 0, rows = [];
  for (const f of ['instincts.1.jsonl', 'instincts.jsonl']) {
    const p = path.join(dir, f); lines.push(`${f}: ${size(p)} bytes`);
    for (const l of (fs.existsSync(p) ? fs.readFileSync(p, 'utf8') : '').split('\n').filter(Boolean)) { try { rows.push(JSON.parse(l)); n++; } catch { /* skip a damaged line */ } }
  }
  for (const f of ['lessons.jsonl', 'lessons.1.jsonl', 'variants.jsonl']) lines.push(`${f}: ${size(path.join(dir, f))} bytes`);
  rows = [...new Map(rows.map(r => [r.trigger + '\0' + r.action, r])).values()];   // newest line per trigger+action is current (decay appends a lower one)
  n = rows.length;
  rows.sort((x, y) => y.confidence - x.confidence);
  return [`instincts: ${n}`, ...rows.slice(0, 5).map(r => `  ${r.confidence} [${r.scope}] when ${r.trigger} -> ${r.action}`), ...lines].join('\n');
}

function selfTest() {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'tailered-lessons-')); let bad = 0;
  const t = (name, ok) => { console.log(`${ok ? 'PASS' : 'FAIL'} ${name}`); if (!ok) bad++; };
  try {
    const dir = dirFor({XDG_DATA_HOME: tmp}); const base = {trigger: 'a', action: 'b', evidence: 'c'};
    add(dir, {...base, confidence: '0.5'});
    t('add appends one line', fs.readFileSync(path.join(dir, 'instincts.jsonl'), 'utf8').trim().split('\n').length === 1);
    for (const c of ['0.2', '0.95', 'abc', undefined]) { let threw = false; try { add(dir, {...base, confidence: c}); } catch { threw = true; } t(`refuses confidence ${c}`, threw); }
    t('refused adds wrote nothing', fs.readFileSync(path.join(dir, 'instincts.jsonl'), 'utf8').trim().split('\n').length === 1);
    fs.writeFileSync(path.join(dir, 'instincts.jsonl'), 'x'.repeat(MAX + 1));
    add(dir, {...base, confidence: '0.9'});
    t('rotates past 1 MiB', size(path.join(dir, 'instincts.1.jsonl')) === MAX + 1 && size(path.join(dir, 'instincts.jsonl')) < 1000);
    add(dir, {...base, confidence: '0.4'});   // same trigger+action, lower: decay
    t('newest line per trigger wins', /^instincts: 1\n {2}0\.4 /.test(status(dir)));
  } catch (e) { t(`self-test crashed: ${e.message}`, false); } finally { fs.rmSync(tmp, {recursive: true, force: true}); }
  t('temp dir removed', !fs.existsSync(tmp));
  return bad ? 1 : 0;
}

const [cmd, ...rest] = process.argv.slice(2);
try {
  if (cmd === '--self-test') process.exit(selfTest());
  else if (cmd === 'status') console.log(status(dirFor(process.env)));
  else if (cmd === 'add') { add(dirFor(process.env), parse(rest)); console.log('added'); }
  else { console.error('usage: lessons.mjs status | add --trigger= --action= --confidence=0.3-0.9 --evidence= [--scope=project|global] | --self-test'); process.exit(2); }
} catch (e) { console.error(`error: ${e.message}`); process.exit(1); }
