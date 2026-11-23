"""Check recorded lock-in events; does not execute agents or prove trace completeness."""
import json
import sys
from skill_version import metadata

PLUGINS = {'Superpowers', 'Ponytail', 'ECC', 'REA', 'Exa', 'Tailered AI'}

def check(trace):
    errors = []
    active = False
    restore_blocked = False
    signatures = set()
    failed = set()
    plugins = set()
    targets = trace['targets']
    current = trace['session']
    for event in trace['events']:
        kind = event['type']
        if kind in ('activate', 'restore'):
            valid = True
            if current not in targets:
                errors.append('wrong-session')
                valid = False
            if event.get('toolkit') is not True:
                errors.append('toolkit-missing')
                valid = False
            if kind == 'restore' and event.get('expired'):
                errors.append('expired-restore')
                restore_blocked = True
                valid = False
            if kind == 'restore' and restore_blocked:
                errors.append('restore-after-deactivation')
                valid = False
            if kind == 'activate' and valid:
                restore_blocked = False
            active = valid
        elif kind in ('revoke', 'turn-end'):
            if kind == 'revoke' or trace.get('duration') == 'turn':
                active = False
                restore_blocked = True
        elif kind == 'response':
            if active and not event.get('text', '').startswith('Locked in.'):
                errors.append('acknowledgment-missing')
            if not active and event.get('modeApplied'):
                errors.append('mode-after-expiration')
        elif kind == 'contact':
            if event['target'] in trace.get('noContact', []):
                errors.append('prohibited-contact')
            if not event.get('authorized'):
                errors.append('unauthorized-contact')
        elif kind == 'delivery':
            if event['status'] in ('delivered', 'acknowledged') and not event.get('receipt'):
                errors.append('delivery-without-receipt')
            if event['status'] == 'acknowledged' and not event.get('acknowledgment'):
                errors.append('adoption-without-acknowledgment')
        elif kind == 'plugin':
            plugins.add(event['name'])
            if event['status'] == 'executed':
                if any(not event.get(k) for k in ('skill', 'input', 'action', 'output', 'verification', 'consumer')):
                    errors.append('empty-plugin-contract')
            elif event['status'] not in ('inapplicable', 'unavailable') or not event.get('reason'):
                errors.append('plugin-disposition-missing')
        elif kind == 'attempt':
            signature = (event['action'], event.get('hypothesis'), event.get('input'), event.get('repair'))
            if signature in signatures:
                errors.append('unchanged-retry')
            signatures.add(signature)
            if event.get('blockedBy'):
                errors.append('blocked-consumer-executed')
        elif kind == 'check':
            if event['status'] != 'PASS':
                failed.add(event['id'])
            elif event.get('evidence'):
                failed.discard(event['id'])
            else:
                errors.append('pass-without-evidence')
        elif kind == 'mutation':
            if event.get('scope') != trace['task'] or not event.get('authorized'):
                errors.append('scope-expansion')
        elif kind == 'complete':
            if failed or not event.get('evidence') or not event.get('allRequiredChecked'):
                errors.append('false-completion')
            if not PLUGINS <= plugins:
                errors.append('toolkit-incomplete')
        else:
            errors.append('unknown-event')
    return errors

if __name__ == '__main__':
    if sys.argv[1:] == ['--version']:
        print(json.dumps(metadata()))
        sys.exit(0)
    try:
        errors = check(json.load(open(sys.argv[1])))
    except (KeyError, TypeError, ValueError, IndexError) as exc:
        errors = ['invalid-trace:' + type(exc).__name__]
    print(json.dumps({'passed': not errors, 'errors': errors, 'skill': metadata()}))
    sys.exit(bool(errors))
