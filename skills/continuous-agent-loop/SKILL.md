---
name: continuous-agent-loop
description: Run a bounded foreground agent loop with explicit attempts, elapsed time, spend and effect limits, quality gates and recovery rules. Use when one task needs repeated attempt, check and adjust cycles that self-check and stop on repeated same-cause failure or a missing required gate. Not for coordinating several agents on one deliverable; use team-agent-orchestration.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Continuous Agent Loop

Run one task through repeated attempt, gate and adjust cycles inside the current session. Kept from the source: the loop selection flow, the combined stack (decomposition, quality gates, eval loop, session persistence), the four failure modes and the four recovery moves. The default loop is bounded and foreground; every limit is written before the first attempt and the loop ends when the acceptance holds or a limit is reached.

## When to Activate

- A task will take several attempts against a checkable acceptance (tests, lint, an eval, a reproducer).
- The user asks to "keep going until it passes", "iterate on this", or "self-check and retry".
- A loop has stalled and needs a recovery decision.

Do not use for:
- several agents working one deliverable in parallel: `team-agent-orchestration`;
- recurring runs outside the session: `autonomous-agent-harness`;
- a single attempt with no gate: the host's ordinary edit and test tools;
- release or merge of the result: The release coordinator, per `../../references/conventions.md`.

## Inputs and outputs

Required inputs: the task goal, a checkable acceptance, the resolved gate commands (actual test runner, linter or eval from the repository's lockfile, config and scripts) and the finite limits. When the acceptance or a required gate is missing, report the gap and run no attempt; a loop without a gate is guessing.

Output: a loop contract written before the first attempt, an iteration log with the cause class of each failure, and a final report stating the result, the measured iteration count, which limit or acceptance ended the loop, and the one next action.

## Steps

### 1. Write the loop contract

Record goal, acceptance, scope (files allowed to change), and the limits: maximum attempts, maximum elapsed time, spend cap, and allowed effects (local edits only, or named side effects). Name who owns a failure that reaches a limit.

Completion: the contract lists all four limits with numbers and the failure owner.

### 2. Select the loop shape

Default to one sequential bounded foreground loop. The source routes strict PR control, RFC decomposition and exploratory parallel generation to helper commands; those helpers are not part of this plugin. Verify a helper exists in the host before routing to it: list the host's commands or skills and match by name. When none matches, stay sequential and note the request as Proposed.

Completion: the shape is recorded as sequential, or as a named helper with its verified host path.

### 3. Resolve the gates

Map the combined stack to what exists: decomposition into units with their own acceptance; quality gates from the repository's actual commands; an eval only when a runner is present; persistence through the coordination record. A required gate that cannot run marks the loop BLOCKED before any attempt.

Completion: each gate names its command and exit expectation, or the loop is BLOCKED with the missing gate named.

### 4. Run one iteration

Make one change, run the gates, record the result with a cause class (same cause as the previous failure, new cause, or passed). Keep logs quiet and keep the useful failure output.

Completion: the iteration entry has the change, the gate results and a cause class.

### 5. Decide to continue or stop

Continue only when the acceptance is not yet met, no limit is reached and the latest failure has a new cause. Stop on a repeated same-cause failure, a reached limit, or a gate that became unavailable; label the stop PASS, FAIL, BLOCKED or INCOMPLETE.

Completion: the decision and its reason are written in the log before the next attempt or the exit.

### 6. Recover a stalled loop

Freeze the loop, inspect the last two iterations by hand, reduce scope to the failing unit, and replay that unit with explicit acceptance. A replay is a new contract with its own limits, not a continuation of the spent ones.

Completion: the replay contract exists or the loop is handed to the failure owner.

### 7. Report and hand over

Lead with the result and the measured counts: attempts used of the maximum, elapsed time, spend when the host reports it (otherwise unavailable), effects produced. Merge, publish or release stays with the release coordinator and the owner's exact word; the loop produces a candidate.

Completion: the report names result, counts, the ending condition and one next action.

## In the workflow

Runs inside Build and Prove of `tailered-ai:workflow`: each iteration ends on that phase's exit, review rounds count toward its 3-round stop rule, a speed or behavior variant is promoted only when the workflow bench and suite stay green, and each iteration's outcome is logged with `tailered-ai:continuous-learning`.

## Anti-Patterns

- An unbounded "run until green" loop; write the limits first.
- Retrying after a repeated same-cause failure; stop and reduce scope.
- Routing to a helper command the host does not list; verify it exists or stay sequential.
- Counting a skipped or unavailable gate as a pass; mark the loop BLOCKED.
- Letting the loop merge or release its own output; hand the candidate over.
- Escalating spend or attempts mid-loop to finish; the replay gets its own contract.

## Source and adaptation

Source: `continuous-agent-loop` from the ECC bundle 2.2.3 (installed local bundle). SHA256 of the source entrypoint: `f228cd383a9063b3a0116c5aea02565e859992f63fae5e799adf9c9e44e2454d`. License: MIT (see NOTICE.md at the plugin root).

- Made a bounded foreground loop with explicit attempt, elapsed-time, spend and effect limits the default, replacing the source's unbounded sequential default and the exploratory parallel path.
- Removed the helper commands the source routes to (harness audit, quality gate, RFC pipeline, REPL persistence, PR and DAG loops), which are not in this plugin; the skill now verifies a helper exists in the host before routing.
- Added a loop contract, cause classification and a stop rule for repeated same-cause failure and unavailable gates.
- Bound persistence to the coordination record and release to the release coordinator.
