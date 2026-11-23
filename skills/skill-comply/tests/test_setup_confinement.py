"""Real filesystem regressions; provider execution is outside this test scope."""
import os
import subprocess

import pytest

from scripts import runner
from scripts.scenario_generator import Scenario


def scenario(*commands: str) -> Scenario:
    return Scenario("probe", 1, "test", "confined setup", "read fixture", commands)


def test_absolute_operand_cannot_create_outside_file(tmp_path, monkeypatch):
    base = tmp_path / "base"
    monkeypatch.setattr(runner, "SANDBOX_BASE", base)
    sentinel = tmp_path / "sentinel"
    sentinel.write_bytes(b"keep")
    outside = tmp_path / "outside-created"
    blocked = False
    try:
        runner._setup_sandbox(base / "probe", scenario(f"touch {outside}"))
    except ValueError:
        blocked = True
    assert not outside.exists(), "setup escaped its admitted root"
    assert sentinel.read_bytes() == b"keep"
    assert blocked, "unsupported setup must explicitly block"


def test_unsupported_setup_blocks_instead_of_silent_success(tmp_path, monkeypatch):
    monkeypatch.setattr(runner, "SANDBOX_BASE", tmp_path / "base")
    with pytest.raises(ValueError, match="Blocked setup"):
        runner._setup_sandbox(tmp_path / "base/probe", scenario("cd anywhere"))


@pytest.mark.parametrize("command", [
    "touch ../escaped", "mkdir -p ../escaped", "touch sub/../../escaped",
    "touch ./escaped", "touch /tmp/escaped", "touch -r sentinel escaped",
    "touch $(echo escaped)", "touch escaped;touch elsewhere", "touch `echo escaped`",
    "sh -c 'touch escaped'", "bash -c 'touch escaped'", "env touch escaped",
    "python -c pass", "/usr/bin/touch escaped", "npm install", "pip install x",
    "tar -xf archive", "unzip archive", "cp source target", "mv source target",
    "chmod 777 target", "git init", "echo hi", "pushd dir", "popd", "",
    "touch", "mkdir -p", "mkdir dir",
])
def test_rejection_preserves_outside_sentinel_and_never_calls_provider(tmp_path, monkeypatch, command):
    base = tmp_path / "base"
    monkeypatch.setattr(runner, "SANDBOX_BASE", base)
    sentinel = tmp_path / "sentinel"
    sentinel.write_bytes(b"protected")
    before = sentinel.stat()
    def forbidden(*args, **kwargs):
        pytest.fail("rejected setup reached a subprocess")
    monkeypatch.setattr(runner.subprocess, "run", forbidden)
    with pytest.raises(ValueError, match="Blocked setup"):
        runner.run_scenario(scenario("mkdir -p valid", command))
    assert not base.exists()
    assert sentinel.read_bytes() == b"protected"
    assert sentinel.stat().st_mtime_ns == before.st_mtime_ns
    assert set(tmp_path.iterdir()) == {sentinel}


@pytest.mark.parametrize("command", ["touch escape/created", "mkdir -p escape/created", "touch escape"])
def test_symlink_inserted_before_operations_cannot_escape(tmp_path, monkeypatch, command):
    base = tmp_path / "base"
    monkeypatch.setattr(runner, "SANDBOX_BASE", base)
    outside = tmp_path / "outside"
    outside.mkdir()
    sentinel = outside / "sentinel"
    sentinel.write_bytes(b"protected")
    real_open = os.open
    def insert_link(path, flags, *args, **kwargs):
        fd = real_open(path, flags, *args, **kwargs)
        if path == "probe":
            (base / "probe/escape").symlink_to(outside, target_is_directory=True)
        return fd
    monkeypatch.setattr(runner.os, "open", insert_link)
    with pytest.raises(OSError):
        runner._setup_sandbox(base / "probe", scenario(command))
    assert sentinel.read_bytes() == b"protected"
    assert list(outside.iterdir()) == [sentinel]
    assert (base / "probe/escape").is_symlink()


def test_valid_setup_reaches_real_runner_with_actual_files(tmp_path, monkeypatch):
    base = tmp_path / "base"
    monkeypatch.setattr(runner, "SANDBOX_BASE", base)
    def provider(args, **kwargs):
        assert args[:2] == ["claude", "-p"]
        root = kwargs["cwd"]
        assert (root / "src/module.py").read_bytes() == b""
        assert (root / "tests").is_dir()
        assert (root / "space name").read_bytes() == b""
        return subprocess.CompletedProcess(args, 0, '', '')
    monkeypatch.setattr(runner.subprocess, "run", provider)
    result = runner.run_scenario(scenario("mkdir -p src tests src", 'touch src/module.py "space name"'))
    assert result.sandbox_dir == base / "probe"
    assert result.observations == ()


def test_existing_attempt_is_preserved_without_replay(tmp_path, monkeypatch):
    base = tmp_path / "base"
    root = base / "probe"
    root.mkdir(parents=True)
    sentinel = root / "failed-evidence"
    sentinel.write_bytes(b"keep prior attempt")
    monkeypatch.setattr(runner, "SANDBOX_BASE", base)
    with pytest.raises(FileExistsError):
        runner._setup_sandbox(root, scenario("touch new"))
    assert sentinel.read_bytes() == b"keep prior attempt"
    assert list(root.iterdir()) == [sentinel]


def test_wrong_root_is_rejected_without_changes(tmp_path, monkeypatch):
    monkeypatch.setattr(runner, "SANDBOX_BASE", tmp_path / "base")
    with pytest.raises(ValueError, match="unexpected scenario root"):
        runner._setup_sandbox(tmp_path / "elsewhere", scenario("touch file"))
    assert list(tmp_path.iterdir()) == []


def test_blocked_setup_never_replaces_cli_report(tmp_path, monkeypatch):
    from scripts import run
    from scripts.parser import ComplianceSpec
    source = tmp_path / "skill.md"
    source.write_text("fixture")
    report = tmp_path / "report.md"
    report.write_bytes(b"prior verified evidence")
    monkeypatch.setattr(run, "__file__", str(tmp_path / "scripts/run.py"))
    monkeypatch.setattr(run.sys, "argv", ["run", str(source), "--output", str(report)])
    monkeypatch.setattr(run, "generate_spec", lambda *a, **k: ComplianceSpec("x", "x", "x", "1", (), .8))
    monkeypatch.setattr(run, "generate_scenarios", lambda *a, **k: [scenario("npm install")])
    with pytest.raises(ValueError, match="Blocked setup"):
        run.main()
    assert report.read_bytes() == b"prior verified evidence"
    assert not list(tmp_path.glob("report.md.*.tmp"))
