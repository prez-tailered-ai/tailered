---
name: speed-of-light-check
description: "Use when asked how fast a job could possibly run; when a day build, odds capture, backtest or publish step's run time is judged only against last month; when the owner says speed of light, asks for the time floor or how far we are from the best possible; or before setting a time target. Not for cutting a job to hit a price the owner named; use tailered-ai:price-forces-cost. Not for where a session's own time went; use tailered-ai:walking-time-audit."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Speed-of-light check

Measure against the limit, not against last time. Huang is reported to judge work against the speed of light: the limit physics allows, not last quarter's result. For the company the limit is time, set by when inputs arrive and what the work truly needs: the day build cannot finish before the last odds capture lands, and a backtest cannot run faster than its compute allows. The guard: a limit computed wrong makes good work look bad, and a limit used as a deadline becomes pressure. So the math and its sources are shown, and the limit is a measure, not an order.

## When to Activate

- A job's run time is judged only against its own past.
- The owner says "speed of light", "what is the floor" or "best possible".
- A time target is about to be set.

Do not use for:
- what a run should cost, rather than how long it should take: tailered-ai:raw-cost-floor;
- cutting a job to hit a price the owner named: tailered-ai:price-forces-cost;
- where a session's own time went: tailered-ai:walking-time-audit;
- a whole-repo speed or bloat review: tailered-ai:lockin.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the job, its stages with measured times, and when each input arrives.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `speed-of-light.md`: the measure, the limit with each term and its source, the gap by stage, and the verdict.

## Steps

Lead the reply with the result: a table of stage, actual, limit and gap, largest gap first, plus the gap for the whole run in the units asked about; then the verdict line: keep, change or stop, with an owner and a target number. When timings or sizes are unknown, propose a figure per stage, mark it `proposal` with its basis, and compute anyway.

### 1. Name the measure

Pick one time measure, such as minutes from the last odds capture to the publishing step done, or seconds per slate capture. Write today's value and where it was measured.

Completion: one measure, its current value and its source.

### 2. Compute the limit

List only what cannot be removed: input arrival times, data size over bandwidth, compute at full use, and the release checks (gates are not waste). Add them up.

Completion: the limit as a number, with every term and its source.

### 3. Measure the gap

For each stage write actual, limit and gap. Sort by gap, largest first.

Completion: a stage table sorted by gap.

### 4. Decide

Verdict: keep (within twice the limit, a proposal unless the owner sets another ratio), change (name the stage, an owner and a target number) or stop (work on a gap that cannot close). A change is tried with tailered-ai:one-league-trial and ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict word, the owner, the target number and the release route.

## Anti-Patterns

- Calling a job fast because it beat last month.
- Counting release checks as waste.
- A limit with no math shown.
- Using the limit as a deadline for people.

## Source and adaptation

Source: original Tailered AI skill, which cites reported accounts of Huang's speed-of-light practice (The Nvidia Way, 2024; Huang interviews). No third-party skill text is copied.
