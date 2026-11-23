---
name: agent-introspection-debugging
description: "Debug a failing agent run in four phases: capture, diagnosis, contained recovery, report. Keeps the original failure and last successful action before any retry, tests one hypothesis with one discriminating check, and stops on an unchanged repeated failure. Use when a run loops, stalls or drifts. Not for locating a corrupting layer across the stack, which agent-architecture-audit covers."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Agent introspection debugging

Turn a failing agent run into a reproducible diagnosis and the smallest safe recovery, instead of a blind retry. Kept from the source: the four-phase loop (failure capture, root-cause diagnosis, contained recovery, introspection report), the failure-pattern table, the diagnosis questions and the recovery order (restate the objective, verify world state, shrink scope, run one discriminating check, only then retry).

## When to Activate

- A tool-call or loop limit is hit, or the same command repeats without progress.
- Context growth or prompt drift is degrading output quality.
- The filesystem, branch, process or service state differs from what the run assumed.
- A tool failure looks recoverable with a smaller corrective action.

Do not use for:
- Finding which layer of a whole agent stack corrupts answers: agent-architecture-audit.
- Verifying a code change after recovery: the repository's own test runner and review process.
- Decision ambiguity that is not a technical failure: ask the owner.

## Inputs and outputs

Required inputs; when one is missing, record it as unavailable in the capture and continue with what exists, never reconstruct it from memory:
- The error (type, message, stack trace when available) and the last meaningful tool-call sequence.
- The goal in progress and the last successful action.
- The environment assumptions the run made: working directory, branch, service state, expected files.
- The limits for recovery (Bounded execution in `../../references/conventions.md`) and the owner of a failure that exceeds them.

Output: a debug report with the failure pattern, the hypothesis and its discriminating check, the recovery action, and the evidence that the situation is now better, still blocked or stopped. It ends with the useful result and one next action when work remains.

## Steps

### 1. Capture the failure before touching anything

Write the capture first: session or task, goal in progress, the original error verbatim, the last successful step, the last failed tool or command, the repeated pattern seen, and the environment assumptions to verify. Retain the original failure and the last successful action unchanged; later retries append to the capture and never overwrite it.

Completion: the capture block exists with the original error and the last successful action recorded before any retry.

### 2. Diagnose against known patterns

Match the failure to one pattern in [references/failure-patterns.md](references/failure-patterns.md) (loop limit, context overflow, connection refused or timeout, rate limit, missing file or stale diff, tests still failing after a fix). Answer the diagnosis questions: logic, state, environment or policy failure; whether the agent lost the real objective; deterministic or transient; the smallest reversible action that would validate the diagnosis. Choose one hypothesis and one discriminating observation whose result would change or reject it.

Completion: one named pattern, one hypothesis, and one discriminating check with its expected result written down before it runs.

### 3. Recover with the smallest contained action

Run the discriminating check. If the result rejects the hypothesis, return to Step 2 with the new observation. If it supports the hypothesis, take the smallest action that changes the diagnosis surface: stop repeated retries, trim low-signal context to the active goal, blockers and evidence, re-check real filesystem, branch and process state, narrow to one command, file or test, or escalate to the owner when the failure is high-risk or externally blocked. Record the diagnosis chosen, the action taken, why it is safe, and the evidence that would prove it worked. Count attempts against the recorded limits; when the same failure returns unchanged after the action, stop and report BLOCKED with the capture intact. Claim an action (reset, configuration change, restart) only when it was performed through a real tool in the current environment.

Completion: one bounded action was taken with its evidence, or the step stopped on an unchanged repeated failure with the reason.

### 4. Report the result

Report: session or task, failure, root cause as established or as the surviving hypothesis, recovery action, result (success, partial, blocked or stopped), token and time burn observed, follow-up needed, and a preventive change worth encoding later when one is evident. Put each qualification beside the claim it changes and finish when the useful answer is complete (Reporting in `../../references/conventions.md`).

Completion: a reader can tell what failed, what was checked, what changed and what remains, without re-reading the run.

## Anti-Patterns

- Retrying the same action with slightly different wording; capture, classify, run one check, then change the plan only if the check supports it.
- Overwriting the original error with the latest one; keep the original failure and the last successful action, append new observations.
- Claiming "reset agent state" or "updated harness config" without doing it through a real tool; name only actions actually taken.
- Continuing after the same failure returns unchanged; stop, report BLOCKED, hand the capture to the owner.
- Ending with "I fixed it" alone or with a fixed footer; end with the evidence and one next action when work remains.

## Source and adaptation

- Source: agent-introspection-debugging, ECC 2.2.3 installed local bundle.
- SHA256: `0cdbfe3c822ff50d21df8cd0e20c72407a6f5658089edc0e96e79a03927cb956`
- License: MIT (see NOTICE.md at the plugin root)
- Adaptations:
  - The four phases became four steps with completion conditions; the capture retains the original failure and last successful action before any retry.
  - Diagnosis narrows to one hypothesis with one discriminating check whose expected result is written before it runs.
  - Recovery is bounded by the shared limits and stops on an unchanged repeated failure; unsupported auto-healing claims are excluded.
  - The mandatory output footer was replaced by a report that ends with the useful result and one next action.
  - Pattern table moved to `references/failure-patterns.md`; external skill handoffs removed.
