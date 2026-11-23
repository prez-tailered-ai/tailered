import json
from pathlib import Path
import subprocess
import sys
import unittest
from datetime import datetime
from skill_version import metadata

ROOT = Path(__file__).resolve().parents[1]


class Version(unittest.TestCase):
    def test_cli_metadata(self):
        expected = metadata()
        self.assertRegex(expected['version'], r'^\d+\.\d+\.\d+$')
        self.assertIsNotNone(datetime.fromisoformat(expected['last_updated'].replace('Z', '+00:00')).tzinfo)
        for script in ('workflow.py', 'check_trace.py'):
            result = subprocess.run([sys.executable, str(ROOT / 'scripts' / script), '--version'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout), expected)
        for script, args, code in [('workflow.py', ['route', '--profile', 'explain'], 0), ('workflow.py', ['route', '--profile', 'unknown'], 1), ('check_trace.py', [], 1)]:
            result = subprocess.run([sys.executable, str(ROOT / 'scripts' / script), *args], capture_output=True, text=True)
            self.assertEqual(result.returncode, code, result.stderr)
            self.assertEqual(json.loads(result.stdout)['skill'], expected)
        self.assertEqual(metadata(), expected)

