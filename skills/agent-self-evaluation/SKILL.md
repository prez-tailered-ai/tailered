---
name: agent-self-evaluation
description: Rate a delivered output on five axes, accuracy, completeness, clarity, actionability and conciseness, with claim-matched evidence for every score including a maximum, and list improvements inside the requested scope. Use when asked to rate or review your own output, or at a gate such as a handoff or a release candidate. Not an every-turn scorecard and not a substitute for independent acceptance.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Agent self-evaluation

Reflect on a delivered output against a structured five-axis rubric so omissions and overconfidence surface before the user finds them. The source's useful structure is kept: the five axes with the question each answers and what it catches, the 1 to 5 scale, the evidence rule, the four-step workflow (collect, score each axis independently, report, propose improvements) and the self-check "would the user agree?". The evaluation runs on request or at a relevant gate, its scores stay separate from independent acceptance, and a failed hard gate stands whatever the average says.

## When to Activate

- The user asks "how good was that?", "rate yourself" or for a review of your own output.
- A gate in the current work calls for it: before a handoff, a release candidate, a closeout record or a delivery the user named as significant.
- A debugging or multi-file task ended and the user asked for a quality assessment of the result.

Do not use for:
- Every turn, a session end or a hook trigger: the evaluation is requested or gated, never automatic.
- Independent acceptance, review verdicts or release decisions: the checklist-session skill and the release authority in `../../references/conventions.md`.
- Comparing agents or setups on fixed tasks: agent-eval.
- Deciding whether a hard check passed: the check's own output.

## Inputs and outputs

Required inputs:
- The original request, read back from the conversation or record.
- The delivered output being rated.
- The tool outputs that bear on correctness: test results, exit codes, lint output, diffs.
- The status of any hard gate that applies (a required check, an acceptance criterion), as PASS, FAIL, BLOCKED, INCOMPLETE or NOT APPLICABLE.
- Any user corrections received during the task.

When tool output for a correctness claim is missing, the accuracy score is capped as in [the evaluation criteria](references/evaluation-criteria.md) and the gap is named; never infer a pass. When the request is ambiguous, state the interpretation chosen and the score under the alternative.

Output: a scorecard with one score and its evidence per axis, the hard-gate status beside any average, one to three improvements ranked by impact and bounded to the requested scope, and the self-check line.

## Steps

### 1. Collect the raw material

Gather the request, the delivered output, the tool outputs and the user corrections. Record the hard-gate status from the check's own output.

Completion: each of the five inputs is present or its absence is written down, and the hard-gate status is recorded with its source.

### 2. Score each axis independently

Work through the axes in order, fresh each time, without averaging first:

| Axis | Question | What it catches |
|---|---|---|
| Accuracy | Are the facts, claims and outputs correct? | Wrong names, wrong syntax, claims that tool output disproves |
| Completeness | Did it cover what the user asked? | Missed requirements, skipped subtasks, unhandled error paths |
| Clarity | Can the reader follow it? | Undefined terms, missing context, no structure |
| Actionability | Can the user act on it now? | Vague next steps, missing verification path |
| Conciseness | Did it use the words needed and no more? | Repetition, filler, restating the question |

Scale: 5 no reasonable improvement; 4 minor nits only; 3 meets the request with one notable weakness; 2 a clear gap affecting usability or correctness; 1 misses the request or contains significant errors. Use [the scoring anchors](references/evaluation-criteria.md) when a boundary is unclear.

Evidence rule: every score cites the specific evidence that supports it. A 5 cites what was verified (the test output, the grep, the matched requirement) and not "all good". A score below 5 names the exact gap. Tool output is ground truth; a claim the output contradicts caps accuracy at 2.

Completion: five scores, each with a cited evidence line, and no score produced by working back from a desired average.

### 3. Produce the scorecard

Write a one-line summary, the five scores with evidence, and, when an average is useful, the simple average beside the hard-gate status. A hard gate marked FAIL, BLOCKED or INCOMPLETE is reported first and is never offset by the average. Add the self-check: "Would the user agree with this assessment?" with a one-line justification.

Completion: the scorecard shows the hard-gate status beside any average, and the self-check line is present.

### 4. Propose improvements within scope

For each axis at 3 or below, name the highest-impact gap, tie it to its user impact, and say what fixed looks like. Keep improvements inside what the user requested; an unrequested extension is not a gap. Apply an improvement only when the current request already covers it (a broken link in the deliverable being written); otherwise list it for the user's decision. Listing improvements starts no new repair or review round.

Completion: one to three ranked improvements, each inside the requested scope, each marked applied-within-request or proposed.

## In the workflow

Runs at the Verify exit of `tailered-ai:workflow`, after `tailered-ai:lockin` verify has re-run the claims fresh (claim branch; model and backtest numbers: results branch). Each scored gap becomes a lesson through `tailered-ai:continuous-learning`.

## Anti-Patterns

- Scoring every axis 5 with "all good"; instead cite the verification that supports each 5.
- Penalizing completeness for work the user did not ask for; instead evaluate against the request as made.
- Using the evaluation to re-argue a settled design decision; instead rate the delivered output.
- Scoring from preference; instead cite a concrete correctness, readability or testability concern.
- Letting a high average cover a failed required check; instead report the failed gate first and keep it failed.
- Running the evaluation on every turn or from a hook; instead run it on request or at the named gate.
- Starting a repair loop from the improvement list; instead hand the list to the user.

## Source and adaptation

Source: `agent-self-evaluation`, ECC 2.2.3 installed local bundle, entrypoint SHA256 `96bb21eb37760f596789f84ec0a5dad4ef92fc2255e35cd7b88dc4234062b8c1`; resources `references/evaluation-criteria.md`, `references/hook-integration.md`, `templates/evaluation-report.md`, `examples/high-score-example.md`, `examples/low-score-example.md`, `scripts/evaluate.py`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- Activation thresholds (3+ files, 50+ lines, 3+ attempts) and the Stop-hook trigger were replaced by activation on request or at a relevant gate; `references/hook-integration.md` was not carried over.
- The evidence rule now applies to every score including 5, per the plugin's acceptance.
- The average is reported beside the hard-gate status and never overrides a failed gate; the source's score-band post-evaluation actions ("redo", "don't deliver") were removed because they started an automatic repair round.
- Improvements are bounded to the requested scope and are listed, not executed as a new round.
- `scripts/evaluate.py` was inspected and not adopted: it scores by keyword heuristics on the output's wording (phrases such as "tests pass"), which rewards claims rather than evidence.
- `references/evaluation-criteria.md` was trimmed to the scoring anchors and edge cases, with vendor, repository and deployment examples removed; the bar-chart report template and the two examples were not carried over.
