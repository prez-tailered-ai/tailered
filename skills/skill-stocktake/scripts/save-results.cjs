'use strict';
const fs = require('node:fs');
const path = require('node:path');
const { randomUUID } = require('node:crypto');
const object = v => v !== null && typeof v === 'object' && !Array.isArray(v);
const timestamp = v => typeof v === 'string' && /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/.test(v) && Number.isFinite(Date.parse(v));
function validate(cache) {
  if (!object(cache) || !object(cache.skills)) throw Error('cache requires a skills object');
  if ('mode' in cache && !['full', 'quick'].includes(cache.mode)) throw Error('invalid mode');
  if ('evaluated_at' in cache && !timestamp(cache.evaluated_at)) throw Error('invalid evaluated_at');
  for (const [key, e] of Object.entries(cache.skills)) {
    if (!key || !object(e) || typeof e.path !== 'string' || !e.path.trim() ||
        typeof e.reason !== 'string' || !e.reason.trim() || typeof e.verdict !== 'string' ||
        !/^(Keep|Improve|Update|Retire|Merge into .+)$/.test(e.verdict) ||
        (e.mtime != null && !timestamp(e.mtime))) throw Error(`invalid skill entry: ${key}`);
  }
  if ('batch_progress' in cache) {
    const p = cache.batch_progress;
    if (!object(p) || !Number.isSafeInteger(p.total) || !Number.isSafeInteger(p.evaluated) ||
        p.evaluated < 0 || p.total < p.evaluated || !['in_progress', 'completed'].includes(p.status) ||
        (p.status === 'completed' && p.total !== p.evaluated)) throw Error('invalid batch_progress');
  }
}
let stage;
let guard;
let owner;
let phase = 'before-replacement';
function fail(error) {
  process.stderr.write(JSON.stringify({ status: 'failed', phase, staging: stage || null,
    guard: guard || null, error: error.message,
    next: 'Retain guard/staging; reconcile destination and ownership before any subsequent write.' }) + '\n');
  process.exitCode = 1;
}
try {
  const [requested, mode, ...extra] = process.argv.slice(2);
  if (!requested || extra.length || (mode !== undefined && mode !== '--replace')) throw Error('Usage: save-results.sh RESULTS_JSON [--replace]');
  const incoming = JSON.parse(fs.readFileSync(0, 'utf8'));
  validate(incoming);
  const destination = path.join(fs.realpathSync(path.dirname(path.resolve(requested))), path.basename(requested));
  guard = `${destination}.owner`;
  const ownership = fs.openSync(guard, 'wx', 0o600);
  owner = JSON.stringify({ token: randomUUID(), pid: process.pid, destination });
  let identity;
  try {
    fs.writeFileSync(ownership, owner);
    fs.fsyncSync(ownership);
    identity = fs.fstatSync(ownership);
  } finally { fs.closeSync(ownership); }
  // Guard coordinates cooperating callers; directory owners can still alter filesystem names.
  let result = incoming;
  if (mode !== '--replace') {
    let existing;
    try { existing = JSON.parse(fs.readFileSync(destination, 'utf8')); }
    catch (error) { if (error.code !== 'ENOENT') throw error; }
    if (existing !== undefined) {
      validate(existing);
      result = { ...existing, skills: { ...existing.skills, ...incoming.skills } };
      for (const key of ['mode', 'batch_progress']) if (key in incoming) result[key] = incoming[key];
    }
  }
  result = { ...result, evaluated_at: new Date().toISOString().replace(/\.\d{3}Z$/, 'Z') };
  validate(result);
  const bytes = JSON.stringify(result, null, 2) + '\n';
  stage = `${destination}.${randomUUID()}.staging`;
  const fd = fs.openSync(stage, 'wx', 0o600);
  try {
    fs.writeFileSync(fd, bytes);
    const staged = fs.readFileSync(stage, 'utf8');
    validate(JSON.parse(staged));
    if (staged !== bytes) throw Error('staged bytes differ');
    fs.fsyncSync(fd);
  } finally { fs.closeSync(fd); }
  phase = 'replacement-outcome-uncertain';
  fs.renameSync(stage, destination);
  phase = 'replaced-durability-unconfirmed';
  const parent = fs.openSync(path.dirname(path.resolve(destination)), 'r');
  try { fs.fsyncSync(parent); } finally { fs.closeSync(parent); }
  phase = 'persisted';
  process.stdout.write(JSON.stringify({ status: 'persisted', destination }) + '\n', error => {
    if (error) { fail(error); return; }
    try {
      const current = fs.lstatSync(guard);
      if (!current.isFile() || current.dev !== identity.dev || current.ino !== identity.ino ||
          fs.readFileSync(guard, 'utf8') !== owner) throw Error('ownership changed; guard retained');
      fs.unlinkSync(guard);
    } catch (failure) { fail(failure); }
  });
} catch (error) {
  fail(error);
}
