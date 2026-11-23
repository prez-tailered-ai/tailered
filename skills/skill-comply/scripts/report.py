"""Generate Markdown compliance reports."""

from __future__ import annotations

from datetime import UTC, datetime
from html import escape
from pathlib import Path

from scripts.grader import ComplianceResult
from scripts.parser import ComplianceSpec, ObservationEvent
from scripts.scenario_generator import Scenario


def _text(value: str) -> str:
    """Keep provider text literal inside Markdown headings, tables and quotes."""
    value = escape(value).replace("\\", "\\\\")
    for char in "`*_{}[]()#+-.!|":
        value = value.replace(char, "\\" + char)
    return value.replace("\r", " ").replace("\n", " ")


def generate_report(
    skill_path: Path,
    spec: ComplianceSpec,
    results: list[tuple[str, ComplianceResult, list[ObservationEvent]]],
    scenarios: list[Scenario] | None = None,
) -> str:
    """Generate a Markdown compliance report.

    Args:
        skill_path: Path to the skill file that was tested.
        spec: The compliance spec used for grading.
        results: List of (scenario_level_name, ComplianceResult, observations) tuples.
        scenarios: Original scenario definitions with prompts.
    """
    now = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    overall = _overall_compliance(results)
    threshold = spec.threshold_promote_to_hook

    lines: list[str] = []
    lines.append(f"# skill-comply Report: {_text(skill_path.name)}")
    lines.append(f"Generated: {now}")
    lines.append("")

    # Summary
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Skill | {_text(str(skill_path))} |")
    lines.append(f"| Spec | {_text(spec.id)} |")
    lines.append(f"| Scenarios | {len(results)} |")
    lines.append(f"| Overall Compliance | {overall:.0%} |")
    lines.append(f"| Threshold | {threshold:.0%} |")

    promote_steps = _steps_to_promote(spec, results, threshold)
    if promote_steps:
        step_names = ", ".join(promote_steps)
        lines.append(f"| Recommendation | **Promote {_text(step_names)} to hooks** |")
    else:
        lines.append("| Recommendation | All steps above threshold — no hook promotion needed |")
    lines.append("")

    # Expected Behavioral Sequence
    lines.append("## Expected Behavioral Sequence")
    lines.append("")
    lines.append("| # | Step | Required | Description |")
    lines.append("|---|------|----------|-------------|")
    for i, step in enumerate(spec.steps, 1):
        req = "Yes" if step.required else "No"
        lines.append(f"| {i} | {_text(step.id)} | {req} | {_text(step.detector.description)} |")
    lines.append("")

    # Scenario Results
    lines.append("## Scenario Results")
    lines.append("")
    lines.append("| Scenario | Compliance | Failed Steps |")
    lines.append("|----------|-----------|----------------|")
    for level_name, result, _obs in results:
        failed = [s.step_id for s in result.steps if not s.detected
                  and any(sp.id == s.step_id and sp.required for sp in spec.steps)]
        failed_str = ", ".join(failed) if failed else "—"
        lines.append(f"| {_text(level_name)} | {result.compliance_rate:.0%} | {_text(failed_str)} |")
    lines.append("")

    # Scenario Prompts
    if scenarios:
        lines.append("## Scenario Prompts")
        lines.append("")
        for s in scenarios:
            lines.append(f"### {_text(s.level_name)} (Level {s.level})")
            lines.append("")
            for prompt_line in s.prompt.splitlines():
                lines.append(f"> {_text(prompt_line)}")
            lines.append("")

    # Hook Promotion Recommendations (optional/advanced)
    if promote_steps:
        lines.append("## Advanced: Hook Promotion Recommendations (optional)")
        lines.append("")
        for step_id in promote_steps:
            rate = _step_compliance_rate(step_id, results)
            step = next(s for s in spec.steps if s.id == step_id)
            lines.append(
                f"- **{_text(step_id)}** (compliance {rate:.0%}): {_text(step.description)}"
            )
        lines.append("")

    # Per-scenario details with timeline
    lines.append("## Detail")
    lines.append("")
    for level_name, result, observations in results:
        lines.append(f"### {_text(level_name)} (Compliance: {result.compliance_rate:.0%})")
        lines.append("")
        lines.append("| Step | Required | Detected | Reason |")
        lines.append("|------|----------|----------|--------|")
        for sr in result.steps:
            req = "Yes" if any(
                sp.id == sr.step_id and sp.required for sp in spec.steps
            ) else "No"
            det = "YES" if sr.detected else "NO"
            reason = sr.failure_reason or "—"
            lines.append(f"| {_text(sr.step_id)} | {req} | {det} | {_text(reason)} |")
        lines.append("")

        # Timeline: show what the agent actually did
        if observations:
            # Build reverse index: event_index → step_id
            index_to_step: dict[int, str] = {}
            for step_id, indices in result.classification.items():
                for idx in indices:
                    index_to_step[idx] = step_id

            lines.append(f"**Tool Call Timeline ({len(observations)} calls)**")
            lines.append("")
            lines.append("| # | Tool | Input | Output | Classified As |")
            lines.append("|---|------|-------|--------|------|")
            for i, obs in enumerate(observations):
                step_label = index_to_step.get(i, "—")
                input_summary = _text(obs.input[:100])
                output_summary = _text(obs.output[:50])
                lines.append(
                    f"| {i} | {_text(obs.tool)} | {input_summary} | {output_summary} | {_text(step_label)} |"
                )
            lines.append("")

    return "\n".join(lines)


def _overall_compliance(results: list[tuple[str, ComplianceResult, list[ObservationEvent]]]) -> float:
    if not results:
        return 0.0
    return sum(r.compliance_rate for _, r, _obs in results) / len(results)


def _step_compliance_rate(
    step_id: str,
    results: list[tuple[str, ComplianceResult, list[ObservationEvent]]],
) -> float:
    detected = sum(
        1 for _, r, _obs in results
        for s in r.steps if s.step_id == step_id and s.detected
    )
    return detected / len(results) if results else 0.0


def _steps_to_promote(
    spec: ComplianceSpec,
    results: list[tuple[str, ComplianceResult, list[ObservationEvent]]],
    threshold: float,
) -> list[str]:
    promote = []
    for step in spec.steps:
        if not step.required:
            continue
        rate = _step_compliance_rate(step.id, results)
        if rate < threshold:
            promote.append(step.id)
    return promote
