#!/usr/bin/env python3
"""Read-only packet identity and routing check. Prints JSON; writes nothing."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

REQUIRED = ('START-HERE.md', 'PROJECT-SPEC.md', 'RESEARCH-AND-DECISIONS.md',
            'EXECUTION.md', 'CHECKPOINT.md', 'SKILLS-AND-HOSTS.md',
            'sources.json', 'evidence-manifest.json', 'LAUNCH-PROMPT.md')


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def verify(packet):
    errors = []
    for name in REQUIRED:
        file = packet / name
        if not file.is_file() or not file.stat().st_size:
            errors.append({'file': name, 'error': 'missing-or-empty'})
    if errors:
        return {'status': 'FAIL', 'errors': errors}
    json.loads((packet / 'sources.json').read_text())
    records = json.loads((packet / 'evidence-manifest.json').read_text())['files']
    if not isinstance(records, list) or not records:
        raise ValueError('evidence-manifest.files must be a nonempty list')
    seen = set()
    for record in records:
        path = Path(record['path'])
        reason = None
        if not path.is_absolute():
            reason = 'not-absolute'
        elif str(path.resolve()) in seen:
            reason = 'duplicate-path'
        elif not path.is_file():
            reason = 'missing-file'
        elif digest(path) != record['sha256']:
            reason = 'hash-mismatch'
        if reason:
            errors.append({'file': str(path), 'error': reason})
        seen.add(str(path.resolve()))
    links = 0
    # Historical backups retain their original relative-link context.
    for name in REQUIRED:
        if not name.endswith('.md'):
            continue
        for raw in re.findall(r'\[[^\]]+\]\((<[^>]+>|[^)\n]+)\)', (packet / name).read_text()):
            target = raw.strip('<>')
            if urlparse(target).scheme or target.startswith('#'):
                continue
            target = re.sub(r':\d+$', '', unquote(target.split('#', 1)[0]))
            links += 1
            if not (packet / target).exists():
                errors.append({'file': name, 'error': 'broken-link', 'target': target})
    launch = (packet / 'LAUNCH-PROMPT.md').read_text()
    start = (packet / 'START-HERE.md').read_text()
    for token in (str(packet / 'START-HERE.md'), ('lockin lock ultra', 'lock-in ultra'), ('lockin', 'Ponytail'), 'SKILLS-AND-HOSTS.md'):
        options = token if isinstance(token, tuple) else (token,)  # lockin replaced Ponytail and lock-in; older packets keep the old names
        if not any(o.lower() in launch.lower() for o in options):
            errors.append({'file': 'LAUNCH-PROMPT.md', 'error': 'missing-route', 'token': ' or '.join(options)})
    if 'LAUNCH-PROMPT.md' not in start:
        errors.append({'file': 'START-HERE.md', 'error': 'missing-launch-pointer'})
    return {'status': 'FAIL' if errors else 'PASS', 'packet': str(packet),
            'scope': 'File identity, local link existence and launch routing; not behavioral qualification.',
            'evidence_files': len(records), 'local_links': links, 'errors': errors}


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError('usage: verify_handoff.py ABSOLUTE_PACKET_DIRECTORY')
        packet = Path(sys.argv[1])
        if not packet.is_absolute():
            raise ValueError('packet path must be absolute')
        result = verify(packet.resolve())
    except (OSError, ValueError, KeyError, TypeError) as error:
        result = {'status': 'FAIL', 'errors': [{'error': str(error)}]}
    print(json.dumps(result, indent=2))
    return 0 if result['status'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
