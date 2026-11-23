"""Offline consumer checks; provider output is synthetic, never live certification."""
import json
import subprocess
from pathlib import Path

import pytest
import yaml

from scripts import run, scenario_generator, spec_generator
from scripts.grader import ComplianceResult, StepResult
from scripts.parser import ComplianceSpec, Detector, ObservationEvent, Step
from scripts.report import generate_report


def spec():
    return ComplianceSpec('fixture', 'Fixture', 'synthetic', '1',
                          (Step('read', 'Read source', True, Detector('Read source')),), .8)


def test_report_preserves_failure_and_timeline():
    event = ObservationEvent('1', 'tool_complete', 'Read', 'fixture', 'a|b\nc', 'output')
    result = ComplianceResult('fixture', (StepResult('read', False, (), 'missing'),), 0, True, {'read': [0]})
    scenario = scenario_generator.Scenario('one', 1, 'supportive', 'synthetic', 'Read\nthen assess', ())
    text = generate_report(Path('fixture.md'), spec(), [('supportive', result, [event])], [scenario])
    assert '| Overall Compliance | 0% |' in text
    assert '| read | Yes | NO | missing |' in text
    assert 'a\\|b c' in text
    assert '> Read\n> then assess' in text
    assert 'Promote read' in text


def test_report_success_and_empty_denominator():
    good = ComplianceResult('fixture', (StepResult('read', True, (), None),), 1, False, {})
    assert '| Overall Compliance | 100% |' in generate_report(Path('fixture'), spec(), [('one', good, [])])
    assert '| Overall Compliance | 0% |' in generate_report(Path('fixture'), spec(), [])


@pytest.mark.parametrize('output', ['{broken', '{}', 'null'])
def test_generator_malformed_output_cannot_return_spec(tmp_path, monkeypatch, output):
    skill = tmp_path / 'SKILL.md'; skill.write_text('Synthetic instruction')
    monkeypatch.setattr(subprocess, 'run', lambda *a, **k: subprocess.CompletedProcess([], 0, output, ''))
    with pytest.raises((KeyError, TypeError, yaml.YAMLError)):
        spec_generator.generate_spec(skill, max_retries=0)


def test_spec_generator_consumes_json_and_fences(tmp_path, monkeypatch):
    skill = tmp_path / 'SKILL.md'; skill.write_text('Synthetic instruction')
    payload = {'id': 'fixture', 'name': 'Fixture', 'source_rule': 'synthetic', 'version': '1',
               'steps': [{'id': 'read', 'description': 'Read source', 'required': True,
                          'detector': {'description': 'Read source'}}],
               'scoring': {'threshold_promote_to_hook': .8}}
    monkeypatch.setattr(subprocess, 'run', lambda *a, **k: subprocess.CompletedProcess([], 0, '```yaml\n'+json.dumps(payload)+'\n```', ''))
    actual = spec_generator.generate_spec(skill, max_retries=0)
    assert actual.steps[0].id == 'read'
    assert actual.threshold_promote_to_hook == .8


@pytest.mark.parametrize('generator', [spec_generator.generate_spec, scenario_generator.generate_scenarios])
def test_failed_provider_cannot_return_success(tmp_path, monkeypatch, generator):
    skill = tmp_path / 'SKILL.md'; skill.write_text('Synthetic instruction')
    monkeypatch.setattr(subprocess, 'run', lambda *a, **k: subprocess.CompletedProcess([], 9, '', 'controlled failure'))
    with pytest.raises(RuntimeError, match='controlled failure'):
        if generator is scenario_generator.generate_scenarios:
            generator(skill, 'steps: []')
        else:
            generator(skill, max_retries=0)


def test_run_complete_consumer_and_write_failure(tmp_path, monkeypatch, caplog):
    skill = tmp_path / 'SKILL.md'; skill.write_text('Synthetic instruction')
    out = tmp_path / 'report.md'
    monkeypatch.setattr(run, '__file__', str(tmp_path / 'scripts' / 'run.py'))
    monkeypatch.setattr(run.sys, 'argv', ['run', str(skill), '--output', str(out)])
    monkeypatch.setattr(run, 'generate_spec', lambda *a, **k: spec())
    monkeypatch.setattr(run, 'generate_scenarios', lambda *a, **k: [])
    run.main()
    assert '| Scenarios | 0 |' in out.read_text()
    prior = out.read_bytes()
    original = Path.write_text
    def fail_output(path, text, *args, **kwargs):
        if path.parent == out.parent and path.suffix == ".tmp":
            raise OSError('controlled persistence failure')
        return original(path, text, *args, **kwargs)
    monkeypatch.setattr(Path, 'write_text', fail_output)
    caplog.clear()
    with pytest.raises(OSError, match='controlled persistence failure'):
        run.main()
    assert out.read_bytes() == prior
    assert 'Report saved' not in caplog.text


def test_missing_skill_exits_failure(tmp_path, monkeypatch):
    monkeypatch.setattr(run.sys, 'argv', ['run', str(tmp_path / 'missing')])
    with pytest.raises(SystemExit) as failure:
        run.main()
    assert failure.value.code == 1


@pytest.mark.parametrize("dry", [False, True])
def test_real_orchestration_with_synthetic_provider_boundary(tmp_path, monkeypatch, dry):
    from scripts import runner
    skill = tmp_path / "SKILL.md"
    skill.write_text("Synthetic instruction")
    out = tmp_path / "report.md"
    monkeypatch.setattr(run, "__file__", str(tmp_path / "scripts" / "run.py"))
    monkeypatch.setattr(runner, "SANDBOX_BASE", tmp_path / "sandbox")
    monkeypatch.setattr(run.sys, "argv", ["run", str(skill), "--output", str(out)] + (["--dry-run"] if dry else []))
    payload = {"id": "fixture", "name": "Fixture", "source_rule": "synthetic", "version": "1",
               "steps": [{"id": "read", "description": "Read", "required": True,
                          "detector": {"description": "Read"}}],
               "scoring": {"threshold_promote_to_hook": .8}}
    scenarios = {"scenarios": [{"id": "fixture", "level": 1, "level_name": "supportive",
                               "description": "synthetic", "prompt": "Read source", "setup_commands": []}]}
    responses = iter([json.dumps(payload), json.dumps(scenarios), ""])
    attempts = []
    def external(args, **kwargs):
        if args[0] == "git":
            return subprocess.CompletedProcess(args, 0, "", "")
        assert args[0] == "claude"
        attempts.append(args)
        return subprocess.CompletedProcess(args, 0, next(responses), "")
    monkeypatch.setattr(subprocess, "run", external)
    run.main()
    if dry:
        assert not out.exists()
        assert len(attempts) == 2  # dry-run still attempts paid generation
    else:
        text = out.read_text()
        assert "| Scenarios | 1 |" in text
        assert "| Overall Compliance | 0% |" in text
        assert "no matching event" in text


def test_report_escapes_untrusted_tool_markup():
    event = ObservationEvent('1', 'tool_complete', '<img src=x onerror=alert(1)>|fake', 'fixture', '<script>bad</script>', 'ok')
    result = ComplianceResult('fixture', (), 0, True, {})
    text = generate_report(Path('fixture'), spec(), [('one', result, [event])])
    assert '<img' not in text
    assert '<script>' not in text
    assert '&lt;img' in text
    assert '\\|fake' in text


def test_partial_persistence_failure_preserves_previous_report(tmp_path, monkeypatch):
    skill = tmp_path / 'SKILL.md'; skill.write_text('Synthetic instruction')
    out = tmp_path / 'report.md'; out.write_text('previous evidence')
    monkeypatch.setattr(run, '__file__', str(tmp_path / 'scripts' / 'run.py'))
    monkeypatch.setattr(run.sys, 'argv', ['run', str(skill), '--output', str(out)])
    monkeypatch.setattr(run, 'generate_spec', lambda *a, **k: spec())
    monkeypatch.setattr(run, 'generate_scenarios', lambda *a, **k: [])
    original = Path.write_text
    def partial_failure(path, text, *args, **kwargs):
        original(path, 'partial', *args, **kwargs)
        raise OSError('controlled interrupted persistence')
    monkeypatch.setattr(Path, 'write_text', partial_failure)
    with pytest.raises(OSError, match='controlled interrupted persistence'):
        run.main()
    assert out.read_text() == 'previous evidence'
    assert any(p.read_text() == 'partial' for p in tmp_path.glob('report.md.*.tmp'))


def test_replace_failure_retains_old_report_and_complete_staging(tmp_path, monkeypatch):
    skill = tmp_path / 'SKILL.md'
    skill.write_text('Synthetic instruction')
    out = tmp_path / 'report.md'
    out.write_text('previous evidence')
    monkeypatch.setattr(run, '__file__', str(tmp_path / 'scripts' / 'run.py'))
    monkeypatch.setattr(run.sys, 'argv', ['run', str(skill), '--output', str(out)])
    monkeypatch.setattr(run, 'generate_spec', lambda *a, **k: spec())
    monkeypatch.setattr(run, 'generate_scenarios', lambda *a, **k: [])
    def refused(*args):
        raise OSError('controlled replace failure')
    monkeypatch.setattr(run.os, 'replace', refused)
    with pytest.raises(OSError, match='controlled replace failure'):
        run.main()
    assert out.read_text() == 'previous evidence'
    staged = list(tmp_path.glob('report.md.*.tmp'))
    assert len(staged) == 1
    assert '| Scenarios | 0 |' in staged[0].read_text()
