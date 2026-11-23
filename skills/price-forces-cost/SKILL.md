---
name: price-forces-cost
description: "Work backward from a number the owner names (a member price, a per-run cap such as a per-run test cap, a monthly line): split it across the job's measured steps, give every step a budget, and name what each cut gives up, or the exact step that cannot reach it. Use when asked to hit a target price or cost, what a price would take, how to get a job under a cap, or to make a price work. Not for judging a running capture job's cost; use tailered-ai:ai-model-capture-health."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Price forces cost

Name the number first, then make the job fit it. Ford's policy put the price cut first and worked to make that price, because a cost calculation says what a cost is and nobody knows what it ought to be. This skill recommends; it changes no price, plan or job.

## When to Activate

- The owner names a target: "get backtests under $2", "what would a $20 tier take", "make this job cost half".
- A plan is about to set a price from today's costs, and the owner wants the target tested first.

Do not use for:
- whether a running capture job is healthy or within its line: tailered-ai:ai-model-capture-health;
- making a slow step faster with no money or unit target: tailered-ai:lockin;
- changing a price or a payment: that is the owner's decision, then tailered-ai:workflow.

## Inputs and outputs

Where to work: `<skill>` below means this skill's own folder. Create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and run every command from it. Never write into the skill folder or into system temp, which can be cleared. Tables go in your reply.

Inputs: the target and its unit (dollars per run, per member per month), and the job it applies to. Ask once if the target is missing; never choose it for the owner.

Output: `budget.json` and `result.json` in the task folder, and one table: step, cost, budget, cut, what the cut gives up. Show the script's exact figures, or round so the lines add up to the total shown.

## Steps

### 1. Pin the target

Write the target, its unit, and who named it, in the owner's words. Say whether it is a real cost or a cap. A cap can be a refusal limit on an estimate: the backtest's `COST_CAP_USD` is checked against an estimate doubled by a safety factor, so a $1 cap and a $1 run are different targets. Read how a cap is enforced before splitting it.

Completion: the target, unit, `target_kind` (cost or cap, with how it is enforced) and source sentence are written down.

### 2. Measure each step

List the job's steps and read each cost from a real bill, meter or job log in the same unit, with `source: "measured: <where>"`. A figure the owner gives counts as `source: "stated: the owner"`: use it, and the result lists it as unmeasured. A step with neither stays `null`, because an unknown cost is the one a plan quietly gets wrong. Set `floor` to the cost below which the step cannot go, with `floor_reason`, starting `measured:` if a bill or log proves it; others come back in `unmeasured_floors`. A step with no floor is treated as able to reach zero and is listed under `no_floor_given`. Carry on with that, and ask about it as part of the one decision in step 5.

Completion: every step has a cost and source, or `null`, and every floor has its reason.

### 3. Write what each cut gives up

Ford's price discipline cost him flexibility, and the Model T's end showed the bill. For each step that must shrink, say what is lost in accuracy, freshness, coverage or the ability to change later.

Completion: every step above its budget has a `gives_up` line; the script reports INCOMPLETE otherwise.

### 4. Run the budget

`python3 -I "<skill>/scripts/budget.py" budget.json > result.json`

Input shape: `{"target": 2.0, "unit": "usd/run", "target_kind": "cost", "steps": [{"name": "sim", "cost": 1.8, "floor": 0.5, "floor_reason": "bill for the smallest run", "source": "measured: billing export", "gives_up": "fewer runs per game"}]}`.

Results: MEETS (already under), REACHABLE (a budget per step), UNREACHABLE (floors alone exceed the target; `blocking` names the steps), INCOMPLETE (exit 2: missing readings or `gives_up`).

Completion: `result.json` has MEETS, REACHABLE or UNREACHABLE. For INCOMPLETE, go back to step 2 or 3, or report exactly what is missing.

### 5. Report and stop

Lead with the verdict and the largest cut. Name every unmeasured step and floor, and every step with no floor. Give the owner one decision: accept what the cuts give up, change the target, or stop. Reaching the target in a plan is a proposal until a run measures it.

Completion: the owner has the table and one decision, and nothing has been changed.

## Anti-Patterns

- Starting from today's cost and adding a margin; start from the target.
- Spreading cuts evenly with no readings; budgets follow measured costs and floors.
- Calling a floor fixed without a reason; Ford treated no cost as fixed, so a floor needs its evidence.
- Presenting a budget built on stated numbers as if measured.
- Reporting savings with no `gives_up`; a cut with no stated loss is unexamined.
- Treating REACHABLE as done; it means the arithmetic allows it, not that a run achieved it.

## Source and adaptation

