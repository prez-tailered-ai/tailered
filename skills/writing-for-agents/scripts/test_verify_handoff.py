"""Bounded negative controls for the portable handoff checker."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('checker', Path(__file__).with_name('verify_handoff.py'))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PacketTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in checker.REQUIRED:
            (self.root / name).write_text('{}' if name.endswith('.json') else 'Fixture document.\n')
        self.evidence = self.root / 'receipt.txt'
        self.evidence.write_text('owned fixture evidence')
        self.record = {'path': str(self.evidence), 'sha256': checker.digest(self.evidence)}
        self.manifest([self.record])
        (self.root / 'START-HERE.md').write_text('[Launch](LAUNCH-PROMPT.md)')
        (self.root / 'LAUNCH-PROMPT.md').write_text(f'lock-in ultra; Ponytail; SKILLS-AND-HOSTS.md; {self.root / "START-HERE.md"}')

    def manifest(self, records):
        (self.root / 'evidence-manifest.json').write_text(json.dumps({'files': records}))

    def assert_error(self, error):
        result = checker.verify(self.root)
        self.assertEqual(result['status'], 'FAIL')
        self.assertIn(error, [row['error'] for row in result['errors']])

    def test_valid_packet_is_read_only(self):
        before = {f.name: f.read_bytes() for f in self.root.iterdir()}
        self.assertEqual(checker.verify(self.root)['status'], 'PASS')
        self.assertEqual(before, {f.name: f.read_bytes() for f in self.root.iterdir()})

    def test_stale_evidence(self):
        self.evidence.write_text('changed')
        self.assert_error('hash-mismatch')

    def test_missing_evidence(self):
        self.evidence.unlink()
        self.assert_error('missing-file')

    def test_duplicate_evidence(self):
        self.manifest([self.record, self.record])
        self.assert_error('duplicate-path')

    def test_empty_evidence(self):
        self.manifest([])
        with self.assertRaises(ValueError):
            checker.verify(self.root)

    def test_broken_pointer(self):
        (self.root / 'EXECUTION.md').write_text('[Missing](absent.md)')
        self.assert_error('broken-link')

    def test_wrong_launch_destination(self):
        (self.root / 'LAUNCH-PROMPT.md').write_text('lock-in ultra; Ponytail; SKILLS-AND-HOSTS.md; /wrong/START-HERE.md')
        self.assert_error('missing-route')

    def test_lockin_or_ponytail_route(self):
        for word, ok in (('lockin', True), ('Ponytail', True), ('nothing', False)):
            (self.root / 'LAUNCH-PROMPT.md').write_text(f'lock-in ultra; {word}; SKILLS-AND-HOSTS.md; {self.root / "START-HERE.md"}')
            self.assertEqual(checker.verify(self.root)['status'] == 'PASS', ok, word)

    def test_lockin_lock_or_lock_in_route(self):
        for words, ok in (('lockin lock ultra', True), ('lock-in ultra', True), ('lock ultra', False)):
            (self.root / 'LAUNCH-PROMPT.md').write_text(f'{words}; lockin; SKILLS-AND-HOSTS.md; {self.root / "START-HERE.md"}')
            self.assertEqual(checker.verify(self.root)['status'] == 'PASS', ok, words)

    def test_missing_required_document(self):
        (self.root / 'PROJECT-SPEC.md').unlink()
        self.assert_error('missing-or-empty')


if __name__ == '__main__':
    unittest.main()
