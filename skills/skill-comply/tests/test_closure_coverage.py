"""Characterize previously uncovered outcomes without changing the denominator."""
import json
import runpy
import subprocess
from pathlib import Path

import pytest

from scripts import (
    classifier,
    grader,
    parser,
    report,
    runner,
    scenario_generator,
    spec_generator,
)


def event(timestamp='1'):
    return parser.ObservationEvent(timestamp, 'tool_complete', 'Read', 'fixture', '', '')


def spec():
    return parser.ComplianceSpec('x', 'x', 'fixture', '1', (), .8)


def test_classifier_nonzero_is_error(monkeypatch):
    monkeypatch.setattr(subprocess, 'run', lambda *a, **k: subprocess.CompletedProcess([], 7, '', 'fixture failure'))
    with pytest.raises(RuntimeError, match='fixture failure'):
        classifier.classify_events(spec(), [event()])


@pytest.mark.parametrize('resolved,message', [({}, 'not yet detected'), ({'prior': [event('2')]}, 'must occur after')])
def test_order_requires_prior_event(resolved, message):
    step = parser.Step('later', 'later', True, parser.Detector('later', after_step='prior'))
    assert message in grader._check_temporal_order(step, event(), resolved, {}, set())


@pytest.mark.parametrize('body,message', [('{broken', 'Invalid JSON'), ('{}', 'Missing required field')])
def test_trace_rejects_invalid_records(tmp_path, body, message):
    p = tmp_path / 'trace'; p.write_text(body)
    with pytest.raises(ValueError, match=message):
        parser.parse_trace(p)


def test_spec_missing_file_and_scoring(tmp_path):
    p = tmp_path / 'spec'
    with pytest.raises(FileNotFoundError):
        parser.parse_spec(p)
    p.write_text('steps: []')
    with pytest.raises(KeyError, match='scoring'):
        parser.parse_spec(p)


def test_optional_step_does_not_recommend_hook():
    optional = parser.Step('optional', 'optional', False, parser.Detector('optional'))
    value = parser.ComplianceSpec('x', 'x', 'fixture', '1', (optional,), .8)
    assert 'Promote optional' not in report.generate_report(Path('fixture'), value, [])


def test_cli_entry_rejects_absent_skill(tmp_path, monkeypatch):
    monkeypatch.setattr('sys.argv', ['run', str(tmp_path / 'absent')])
    with pytest.raises(SystemExit) as result:
        runpy.run_path(str(Path(__file__).parents[1] / 'scripts/run.py'), run_name='__main__')
    assert result.value.code == 1


def test_unknown_execution_model_has_no_sandbox(tmp_path, monkeypatch):
    monkeypatch.setattr(runner, 'SANDBOX_BASE', tmp_path / 'sandbox')
    scenario = scenario_generator.Scenario('fixture', 1, 'test', '', '', ())
    with pytest.raises(ValueError, match='Unknown model'):
        runner.run_scenario(scenario, model='not-a-model')
    assert not (tmp_path / 'sandbox').exists()


def test_setup_has_no_executable_dependency(tmp_path, monkeypatch):
    base = tmp_path / 'sandbox'; monkeypatch.setattr(runner, 'SANDBOX_BASE', base)
    def external(*args, **kwargs):
        raise AssertionError('setup must not execute a command')
    monkeypatch.setattr(subprocess, 'run', external)
    runner._setup_sandbox(base / 'one', scenario_generator.Scenario('one', 1, 'test', '', '', ('touch file',)))
    assert (base / 'one/file').read_bytes() == b''


def test_redaction_root_home_and_scalar(monkeypatch):
    monkeypatch.setattr(Path, 'home', lambda: Path('/'))
    assert runner._redact_home_path('/tmp/fixture') == '/tmp/fixture'
    assert runner._redact_home_paths(7) == 7


def test_stream_noise_and_unfinished_tool_retained():
    line = {'type': 'assistant', 'message': {'content': [{'type': 'tool_use', 'id': 'a', 'name': 'Read', 'input': {'path': 'fixture'}}]}}
    events = runner._parse_stream_json('not json\n'+json.dumps(line))
    assert len(events) == 1
    assert events[0].tool == 'Read'
    assert events[0].output == ''
    assert events[0].session == 'unknown'


def test_empty_scenario_output_rejected(tmp_path, monkeypatch):
    p = tmp_path / 'skill';p.write_text('fixture')
    monkeypatch.setattr(subprocess, 'run', lambda *a, **k: subprocess.CompletedProcess([], 0, ' ', ''))
    with pytest.raises(RuntimeError, match='empty output'):
        scenario_generator.generate_scenarios(p, 'steps: []')


def test_spec_retry_and_negative_retry_limit(tmp_path, monkeypatch):
    p = tmp_path / 'skill';p.write_text('fixture')
    payload = {'id': 'x', 'name': 'fixture', 'source_rule': 'fixture', 'version': '1', 'steps': [], 'scoring': {'threshold_promote_to_hook': .8}}
    outputs = iter(['{}', json.dumps(payload)])
    monkeypatch.setattr(subprocess, 'run', lambda *a, **k: subprocess.CompletedProcess([], 0, next(outputs), ''))
    assert spec_generator.generate_spec(p, max_retries=1).id == 'x'
    with pytest.raises(RuntimeError, match='unreachable'):
        spec_generator.generate_spec(p, max_retries=-1)


def test_absent_before_event_does_not_invent_ordering_failure():
    step = parser.Step('early', 'early', True, parser.Detector('early', before_step='later'))
    assert grader._check_temporal_order(step, event('1'), {}, {}, set()) is None


def test_stream_text_and_orphan_results_do_not_invent_observations():
    messages = [
        {'type': 'assistant', 'message': {'content': [{'type': 'text', 'text': 'hello'}]}},
        {'type': 'user', 'message': {'content': 'plain text'}},
        {'type': 'user', 'message': {'content': [{'type': 'tool_result', 'tool_use_id': 'absent', 'content': 'orphan'}]}},
    ]
    assert runner._parse_stream_json('\n'.join(json.dumps(m) for m in messages)) == []
