---
name: latency-budget
description: "Use when the main product card or a page feels slow, a day build ran long or no run time is written down; when the owner says fast is a feature, latency or time budget; or when a change may add load or build time. Not for a job's physical floor; use tailered-ai:speed-of-light-check. Not for how long a broken main product may stay broken; use tailered-ai:move-fast-stable."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Latency budget

Google's published "Ten things" list puts fast ahead of slow, and Google reported half a second of delay cut searches by about a fifth. A session reading, marked [added] in the source note and not the owner's own words: give the main product card and the day build a time budget in seconds, measured every run, and treat a miss as a defect. The guard: speed bought by serving stale prices or skipping a check is also a miss.

## When to Activate

- The main product card feels slow, the day build ran long, or no run time is written down.
- The owner says fast is a feature, latency or time budget.
- A change may add load or build time.

Do not use for:
- a job's physical floor: tailered-ai:speed-of-light-check;
- how long a broken main product may stay broken: tailered-ai:move-fast-stable.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the surface or job, recent run times and the timing logs.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `budget.md`: budgets in seconds, measured runs, verdicts and misses filed as defects.

## Steps

Lead the reply with the budget-versus-measured table, then the verdict line, detail after.

### 1. Set the budget in seconds

One budget per surface and job, at the 95th percentile. Proposals: main product card first render 1.5 seconds on a phone; day build 1,200 seconds, split by stage. Add a freshness bound so speed cannot come from old data; proposal: prices under 300 seconds old at render. The owner approves.

Completion: a budget in seconds and a freshness bound for each surface and job.

### 2. Measure every run

Take the last 20 runs (proposal) and write the median and 95th percentile per stage. If a stage has no timing, name the timing to add and its owner; adding it follows tailered-ai:workflow.

Completion: median and 95th percentile per stage, or the timing to add and its owner.

### 3. File misses as defects

Each run over budget or over the freshness bound is a defect: date, stage, seconds over, owner. Write keep (met), fix (missed) or change (the budget is wrong, with evidence; the owner decides) per budget.

Completion: a verdict word per budget, and every miss filed.

### 4. Route the fix

Fix the slowest stage first. A change that adds time states its added seconds before approval. Changes ship through tailered-ai:workflow and the release coordinator on the owner's word; this skill ships nothing.

Completion: the release route, and each pending change's added seconds.

## Anti-Patterns

- A budget measured once, or never.
- Averages that hide the slow tail.
- Meeting the budget with stale prices or a skipped check.
- Raising the budget quietly after a miss.

## Source and adaptation

Source: original Tailered AI skill, which cites Google's "Ten things we know to be true", reported 2006 latency tests and session reading [added] (2). No third-party skill text is copied.
