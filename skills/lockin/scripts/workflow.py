"""Read-only routing and receipt validation. Never dispatches tools or grants authority."""
import argparse
from skill_version import metadata
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def catalog():
    return json.loads((ROOT / 'references/capabilities.json').read_text())

def route(profiles, phase=None, home=None):
    home = Path(home or Path.home())
    data = catalog()
    unknown = set(profiles) - set(data['profiles'])
    if unknown:
        raise ValueError('unknown profiles: ' + ', '.join(sorted(unknown)))
    if phase and phase not in data['phases']:
        raise ValueError('unknown phase')
    selected = set().union(*(set(data['profiles'][p]) for p in profiles))
    result = []
    for key in sorted(selected):
        c = data['capabilities'][key]
        paths = sorted({str(p.resolve()) for pattern in c['paths'] for p in home.glob(pattern) if p.is_file()})
        result.append(dict(id=key, phase=c['phase'], contribution=c['contribution'],
            task_required=True, role_applicable=phase is None or phase == c['phase'],
            availability='file-present' if paths else 'unavailable', paths=paths,
            execution='not-started', verification='not-run', runtime='unverified'))
    return result

def file_receipt(receipt):
    if not isinstance(receipt, dict) or set(receipt) != {'path', 'sha256'}:
        return False
    try:
        return Path(receipt['path']).is_absolute() and digest(receipt['path']) == receipt['sha256']
    except (OSError, TypeError, ValueError):
        return False

def candidate_receipt(receipt):
    """Check the manifest and its complete recursive file set at invocation time."""
    if not file_receipt(receipt):
        return False
    path = Path(receipt['path'])
    if path.suffix.lower() != '.json':
        return True
    try:
        data = json.loads(path.read_text())
        if not isinstance(data, dict):
            return True
        if data.get('schema') != 'lock-in-manifest/1':
            # Legacy hash maps lack a bound root and must be regenerated, not trusted.
            return not (not data or all(isinstance(v, str) and len(v) == 64
                                       for v in data.values()))
        if set(data) != {'schema', 'root', 'files'}:
            return False
        root = Path(data['root'])
        files = data['files']
        if not root.is_absolute() or not root.is_dir() or not isinstance(files, dict) or not files:
            return False
        root = root.resolve()
        for name, expected in files.items():
            rel = Path(name)
            if rel.is_absolute() or '..' in rel.parts or rel.as_posix() != name:
                return False
            if not isinstance(expected, str) or len(expected) != 64:
                return False
        actual = {}
        for member in root.rglob('*'):
            if member.is_symlink():
                return False
            if member.is_file():
                actual[member.relative_to(root).as_posix()] = digest(member)
            elif not member.is_dir():
                return False
        return actual == files
    except (OSError, TypeError, ValueError):
        return False


def validate(run):
    """Validate declared evidence; does not attest its truth or complete event capture."""
    errors = []
    if run.get('schema') != 'lock-in-workflow/1':
        return ['invalid-schema']
    if not run.get('session') or not run.get('task') or not run.get('candidate'):
        errors.append('identity-missing')
    if run.get('session') not in run.get('targets', []):
        errors.append('wrong-session')
    if run.get('state') != 'active' or run.get('expired') is not False:
        errors.append('inactive-or-expired')
    if not candidate_receipt(run.get('candidate')):
        errors.append('candidate-missing-or-stale')
    allowed = run.get('allowed_effects', [])
    if not isinstance(allowed, list):
        return errors + ['invalid-effects']
    steps = run.get('steps', [])
    if not isinstance(steps, list):
        return errors + ['invalid-steps']
    ids = [s.get('id') for s in steps if isinstance(s, dict)]
    if len(ids) != len(steps) or len(ids) != len(set(ids)) or not all(ids):
        return errors + ['invalid-step-identities']
    by_id = {s['id']: s for s in steps}
    required = set(run.get('required', []))
    if not required or not required <= set(ids):
        errors.append('required-coverage-missing')
    visits, stack = set(), set()
    def visit(key):
        if key in stack:
            errors.append('dependency-cycle'); return
        if key in visits:
            return
        stack.add(key)
        for dep in by_id[key].get('depends_on', []):
            if dep not in by_id:
                errors.append('dependency-missing')
            else:
                visit(dep)
        stack.remove(key); visits.add(key)
    for key in ids:
        visit(key)
    for s in steps:
        sid = s['id']
        if s.get('status') not in ['PASS', 'FAIL', 'NOT_RUN', 'NOT_APPLICABLE']:
            errors.append('invalid-status:' + sid)
        if s.get('effect') not in allowed:
            errors.append('unauthorized-effect:' + sid)
        if sid in required and s.get('status') != 'PASS':
            errors.append('required-not-passed:' + sid)
        if s.get('status') == 'NOT_APPLICABLE' and not s.get('reason'):
            errors.append('missing-disposition-reason:' + sid)
        if s.get('status') != 'PASS':
            continue
        if any(by_id.get(d, {}).get('status') != 'PASS' for d in s.get('depends_on', [])):
            errors.append('blocked-consumer:' + sid)
        if s.get('candidate_sha256') != run.get('candidate', {}).get('sha256'):
            errors.append('stale-step:' + sid)
        if not all(s.get(k) for k in ['capability', 'action', 'consumer', 'inputs', 'outputs', 'checks']):
            errors.append('incomplete-contract:' + sid)
        for k in ['inputs', 'outputs', 'checks']:
            refs = s.get(k, [])
            if not isinstance(refs, list) or not all(file_receipt(r) for r in refs):
                errors.append('invalid-receipt:' + sid + ':' + k)
        mode = s.get('evidence_mode')
        if mode not in ['local-execution', 'host-execution', 'browser-execution', 'retained', 'tabletop']:
            errors.append('invalid-evidence-mode:' + sid)
        needs = s.get('requires_mode')
        if needs and mode != needs:
            errors.append('insufficient-evidence-mode:' + sid)
        if mode in ['host-execution', 'browser-execution'] and not s.get('host'):
            errors.append('host-missing:' + sid)
    if run.get('claim') not in ['local', 'host', 'production']:
        errors.append('invalid-claim')
    if run.get('claim') == 'host' and not any(s.get('evidence_mode') == 'host-execution' and s.get('status') == 'PASS' for s in steps):
        errors.append('host-execution-missing')
    if run.get('claim') == 'production':
        for k in ['approval', 'coordination', 'live_acceptance', 'rollback']:
            if not file_receipt(run.get(k)):
                errors.append('production-' + k + '-missing')
    return sorted(set(errors))

def resume(run, session, candidate):
    """Propose invalidation only; caller atomically updates its own existing record."""
    if run.get('session') != session or session not in run.get('targets', []):
        raise ValueError('wrong session')
    if run.get('state') != 'active' or run.get('expired') is not False:
        raise ValueError('revoked or expired')
    if not candidate_receipt(candidate):
        raise ValueError('invalid candidate')
    invalid = {s['id'] for s in run['steps'] if s.get('candidate_sha256') != candidate['sha256']}
    while True:
        more = {s['id'] for s in run['steps'] if invalid.intersection(s.get('depends_on', []))}
        if more <= invalid:
            break
        invalid |= more
    return {'session': session, 'invalidate': sorted(invalid),
        'next': [s['id'] for s in run['steps'] if (s['id'] in invalid or s.get('status') != 'PASS')
                 and all(d not in invalid and next((x.get('status') for x in run['steps'] if x['id']==d), None)=='PASS' for d in s.get('depends_on', []))], 'writes': False}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--version', action='version', version=json.dumps(metadata()))
    sub=p.add_subparsers(dest='command',required=True)
    r=sub.add_parser('route');r.add_argument('--profile',action='append',required=True);r.add_argument('--phase')
    v=sub.add_parser('validate');v.add_argument('run')
    r=sub.add_parser('resume');r.add_argument('run');r.add_argument('--session',required=True);r.add_argument('--candidate',required=True)
    args=p.parse_args()
    read=lambda f:json.loads(Path(f).read_text())
    try:
        if args.command=='route': result={'capabilities':route(args.profile,args.phase)}
        elif args.command=='validate':
            errors=validate(read(args.run));result={'passed':not errors,'errors':errors}
        else: result=resume(read(args.run),args.session,read(args.candidate))
        print(json.dumps({**result, 'skill': metadata()},indent=2));return 1 if result.get('passed') is False else 0
    except (ValueError,TypeError,KeyError,OSError,AttributeError) as e:
        print(json.dumps({'passed':False,'error':str(e),'skill':metadata()}));return 1

if __name__=='__main__':raise SystemExit(main())
