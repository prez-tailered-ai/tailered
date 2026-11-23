"""Faults around the real CLI report writer, with synthetic generation only."""
import os
import stat

import pytest

from scripts import run
from scripts.parser import ComplianceSpec


@pytest.fixture
def report_target(tmp_path, monkeypatch):
    source = tmp_path / 'skill.md'; source.write_text('fixture')
    target = tmp_path / 'report.md'; target.write_text('previous evidence')
    monkeypatch.setattr(run, '__file__', str(tmp_path / 'scripts/run.py'))
    monkeypatch.setattr(run.sys, 'argv', ['run', str(source), '--output', str(target)])
    monkeypatch.setattr(run, 'generate_spec', lambda *a, **k: ComplianceSpec('x', 'x', 'x', '1', (), .8))
    monkeypatch.setattr(run, 'generate_scenarios', lambda *a, **k: [])
    return target


def test_file_sync_failure_preserves_old_and_staging(report_target, monkeypatch, caplog):
    def fail(fd):
        raise OSError('file sync fault')
    monkeypatch.setattr(run.os, 'fsync', fail)
    with pytest.raises(OSError, match='file sync fault'):
        run.main()
    assert report_target.read_text() == 'previous evidence'
    assert len(list(report_target.parent.glob('report.md.*.tmp'))) == 1
    assert 'Report saved' not in caplog.text


def test_metadata_sync_failure_has_new_bytes_but_no_success(report_target, monkeypatch, caplog):
    real_sync = os.fsync
    def fail_directory(fd):
        if stat.S_ISDIR(os.fstat(fd).st_mode):
            raise OSError('metadata sync fault')
        real_sync(fd)
    monkeypatch.setattr(run.os, 'fsync', fail_directory)
    with pytest.raises(OSError, match='metadata sync fault'):
        run.main()
    assert '| Scenarios | 0 |' in report_target.read_text()
    assert 'Report saved' not in caplog.text


def test_success_order_sync_replace_metadata_ack(report_target, monkeypatch):
    observed = []
    sync, replace, info = os.fsync, os.replace, run.logger.info
    def track_sync(fd):
        observed.append('directory' if stat.S_ISDIR(os.fstat(fd).st_mode) else 'file')
        sync(fd)
    def track_replace(a, b):
        observed.append('replace'); replace(a, b)
    def track_info(message, *args, **kwargs):
        if 'Report saved' in message:
            observed.append('ack')
        info(message, *args, **kwargs)
    monkeypatch.setattr(os, 'fsync', track_sync)
    monkeypatch.setattr(os, 'replace', track_replace)
    monkeypatch.setattr(run.logger, 'info', track_info)
    run.main()
    assert observed == ['file', 'replace', 'directory', 'ack']
    assert '| Scenarios | 0 |' in report_target.read_text()


def test_receipt_failure_requires_readback_before_retry(report_target, monkeypatch):
    info = run.logger.info
    def lost_receipt(message, *args, **kwargs):
        if 'Report saved' in message:
            raise OSError('receipt unavailable')
        info(message, *args, **kwargs)
    monkeypatch.setattr(run.logger, 'info', lost_receipt)
    with pytest.raises(OSError, match='receipt unavailable'):
        run.main()
    assert '| Scenarios | 0 |' in report_target.read_text()
    assert not list(report_target.parent.glob('report.md.*.tmp'))


def test_full_sync_failure_preserves_previous(report_target, monkeypatch):
    import fcntl
    def fail(fd, operation):
        raise OSError('full sync fault')
    monkeypatch.setattr(fcntl, 'fcntl', fail)
    with pytest.raises(OSError, match='full sync fault'):
        run.main()
    assert report_target.read_text() == 'previous evidence'
    assert len(list(report_target.parent.glob('report.md.*.tmp'))) == 1


def test_non_darwin_policy_uses_fsync_without_macos_operation(report_target, monkeypatch):
    import fcntl
    from types import SimpleNamespace
    def unavailable(*args):
        raise AssertionError('non-Darwin policy called F_FULLFSYNC')
    monkeypatch.setattr(run, 'sys', SimpleNamespace(platform='linux', argv=run.sys.argv))
    monkeypatch.setattr(fcntl, 'fcntl', unavailable)
    run.main()
    assert '| Scenarios | 0 |' in report_target.read_text()
