---
name: day-one-check
description: "Use when dashboards are green, the suite passes or a record says PASS but the real result is unclear; when a process has grown many steps; when the owner asks are we in good shape or is this too much process; or once a month. Not for running release checks; use tailered-ai:workflow."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Day one check

Check that the signals still stand for the result. Bezos' 2016 letter calls stasis Day 2 and names its defenses: obsess over customers, resist proxies, embrace outside trends, decide fast. The proxy trap is a metric or a process becoming the goal while nobody checks the result it stood for. The guard: "Day 1" has also been used to justify a harsh pace (New York Times, 2015). This check is about proxies, not pace.

## When to Activate

- Dashboards are green, the suite passes or a record says PASS, and the real result is unclear.
- A process has grown many steps.
- The owner asks "are we in good shape" or "is this too much process"; or once a month.

Do not use for:
- running release checks: tailered-ai:workflow;
- reviewing a change for bugs: tailered-ai:lockin.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the signals, metrics or process steps in question.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `proxies.md`: a table of each proxy, the result it stands for, the direct check and what it showed.

## Steps

### 1. List the proxies

For each green signal, metric or step, write the real result it stands for: a member sees today's games correctly, the model beat the close, a release reached members.

Completion: the table's first two columns.

### 2. Check the result directly

For at least the top two, look at the result itself: open what a member sees on today's main product, or recompute one number from raw data. Record the command or observation. When you cannot reach it, write the exact page or command to check, and the result that would mean agree or disagree.

Completion: two direct checks with what they showed.

### 3. Compare

Mark each row agree or disagree; a disagreement is the finding. For process steps, name the failure each one exists to catch and when it last caught one, or write `never`; keep every step that caught something real.

Completion: every row is marked.

### 4. Recommend

Fix the proxy that disagrees, and propose cutting or merging steps that never catch anything. The owner's release word and the release coordinator stay.

Completion: a recommendation; no step is cut without the owner.

## Anti-Patterns

- Taking green as the answer.
- Measuring the process instead of the result.
- Cutting a gate the owner set.
- Using "Day 1" as a slogan for speed.

## Source and adaptation

Source: original Tailered AI skill, which cites Amazon's 2016 shareholder letter and the New York Times (2015). No third-party skill text is copied.
