---
name: continuous-learning
description: Turn what a session just taught into small, scored lessons (trigger, action, confidence 0.3 to 0.9, evidence, scope), review them, and promote a proven one into a skill edit only through the workflow Prove phase. Use when asked to remember a lesson, record an instinct, review or decay what was learned, or promote a lesson into a skill. Not for running a task loop; use continuous-agent-loop. Not for grading one answer; use agent-self-evaluation.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Continuous learning

Learn from sessions as atomic, scored lessons kept in one file, and change a skill only when a lesson has earned it. Kept from the source: the atomic instinct (one trigger, one action), confidence from 0.3 (tentative) to 0.9 (near certain), evidence on every entry, project or global scope, promotion of repeated high-confidence lessons, and confidence that falls when evidence contradicts it. This skill installs no observer hook and runs no background model; it reads and writes plain files only.

## When to Activate

- The user says "remember this", "record a lesson", "instinct", "what have we learned" or "promote this lesson".
- A correction, a failed check or a repeated workaround should be kept so the next session starts better.
- The daily learning proposals need review.

Do not use for:
- one attempt-check-adjust loop on a single task: `continuous-agent-loop`;
- scoring one answer against a rubric: `agent-self-evaluation`;
- finding skills that no longer fire or conflict: `skill-comply` or `skill-stocktake`;
- writing or rewriting a whole skill: `skill-creator`;
- the release itself: `tailered-ai:workflow`.

## Inputs and outputs

Inputs: what happened (the correction, failure or repeated step), where the proof is (a file path, command output, ledger line), and the scope. The existing store is `${XDG_DATA_HOME:-~/.local/share}/tailered-workflow/`: `lessons.jsonl` (written by `check-release.mjs`, rotates at 1 MiB to `lessons.1.jsonl`), `variants.jsonl`, and this skill's `instincts.jsonl`. These are separate logs with different record shapes; `lessons.mjs status` reports all three. Automation: only the daily learning task runs unattended; capturing an instinct is a manual `lessons.mjs add`. If a file is missing, report it and continue with the others.

Output: appended lesson lines, a ranked status, and, when promoted, a skill edit that passed workflow Prove.

## Steps

### 1. Capture one atomic lesson

Write it as: trigger ("when ..."), action (one thing to do), confidence, evidence, scope (`project` by default, `global` only when it held in two or more projects). One trigger and one action per lesson; split anything longer. Start at 0.3 to 0.5 for a single observation, 0.6 to 0.7 for a repeat, 0.8 to 0.9 only with a check that decided it. Run `node scripts/lessons.mjs add --trigger="..." --action="..." --confidence=0.5 --evidence="..." [--scope=global]`.

Completion: the command prints `added`, and `status` lists the line. A confidence outside 0.3 to 0.9 is refused with exit 1; do not work around it.

### 2. Check the store

Run `node scripts/lessons.mjs status`. It shows the count, the top five by confidence (newest line wins per trigger and action) and the size of each file.

Completion: the output names every file and its size, and any file near 1 MiB is noted (it rotates once on the next write).

### 3. Review before trusting

Read the top lessons and the latest daily learning proposals. Mark each one: keep, raise, decay or drop. A lesson written against an old skill text is stale: compare the `skillSha` in `lessons.jsonl` with the current SKILL.md hash.

Completion: every reviewed lesson has a recorded verdict and the reason.

### 4. Decay when contradicted

When new evidence contradicts a lesson, append a new line with the same trigger and action and a lower confidence (drop 0.2 per contradiction). Never edit or delete old lines; the newest line is current. Below 0.3 the lesson is dropped from use but stays in the file.

Completion: `status` shows the lower value for that trigger and the evidence line names the contradiction.

### 5. Promote through workflow Prove

A lesson may change a skill only at 0.8 or higher, with evidence from two or more separate sessions or runs. Make the smallest skill edit, then follow `tailered-ai:workflow` Prove: fixture prompts and `node scripts/bench.mjs` must still pass. The edit is local until the workflow Release phase and the owner's word.

Completion: the bench output shows it still passes and the edit is a named file diff; otherwise the lesson stays a lesson.

### 6. Report

State how many lessons were added, decayed, promoted or left, what each check proved, and who acts next.

Completion: the report names the store path, the counts and the next owner.

## Anti-Patterns

- An observer hook or background model "to learn automatically"; capture is a deliberate step.
- Confidence of 0.9 from one story; high needs a deciding check.
- Several actions in one lesson.
- Editing or deleting old lines instead of appending a lower-confidence one.
- Promoting a lesson into a skill without workflow Prove.
- A project lesson saved as global, which carries it into places it does not fit.
- Secrets, tokens or personal data in a lesson's evidence.

## Source and adaptation

Source: `continuous-learning-v2` from the ECC bundle 2.2.1. SHA256 of the source entrypoint: `ddad12451a0d582c6ef1b197b7be193bef613cbc74eba4117fcb74fc7a4ecd00`. License: MIT (see NOTICE.md at the plugin root).

- Dropped the observer hooks, `observe.sh`, the background Haiku observer and the Python `instinct-cli.py`; the store is JSON lines written by one Node standard-library script (`scripts/lessons.mjs`) with `status`, `add` and `--self-test`.
- Used the existing Tailered store (`lessons.jsonl`, `variants.jsonl`, the daily learning task) instead of a new homunculus directory.
- Kept the 0.3 to 0.9 confidence range and added a refusal outside it, rotation at 1 MiB, and decay by appended lines.
- Replaced "evolve into skills, commands or agents" with promotion only through `tailered-ai:workflow` Prove and Release.
- Removed import, export and automatic project detection; scope is stated by the writer.
