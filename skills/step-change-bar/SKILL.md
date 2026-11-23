---
name: step-change-bar
description: "Use when a goal or model target is a small gain, such as 10 percent better on one league; when the owner says 10x, moonshot, think bigger or set the bar; or when a plan stops at one game, market or league. Not for setting the deadline; use tailered-ai:two-date-plan. Not for capping the cost of a bet; use tailered-ai:capped-experiment."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Step-change bar

Page was reported as pushing 10x goals because they force a new approach, where 10 percent invites tuning the old one (Wired, 2013). A session reading, marked [added] in the source note and not the owner's own words: set the bar at a step change, every game, every market, every day, not a 10 percent gain on one league. The guard: Google Glass went public unfinished and its consumer program ended in 2015 (reported). A big bar still needs a first step that ships.

## When to Activate

- A goal or model target is a small gain on one league or one market.
- The owner says 10x, moonshot, think bigger or set the bar.
- A plan stops at one game, market or league.

Do not use for:
- setting the dates: tailered-ai:two-date-plan;
- capping what a bet may cost: tailered-ai:capped-experiment.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the current goal, today's coverage (games a day, markets per game, leagues) and the day-build steps.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `bar.md`: both goals, what breaks, the first step and the verdict.

## Steps

Lead the reply with the two goals side by side, then the verdict line, detail after.

### 1. Write both goals

Write the incremental goal (such as cut NHL totals error 10 percent) and the step-change goal: every game, every market (spread, total, moneyline and the matching prediction-market contracts), every day, in all four leagues. Put today's baseline beside each, such as 40 of 120 games a day (proposal).

Completion: two goals, each with a number and today's baseline.

### 2. Find what breaks at the step change

Name what in today's approach cannot reach the bar: a hand step, a per-league script, a one-league source, a review by eye. Tuning cannot pass these.

Completion: each breaking part named with the number it caps, such as 40 games a day.

### 3. Cut a first step that ships

Choose the first slice toward the bar that can be checked within two weeks (proposal), with its check number and a named owner.

Completion: first step, check number, date and owner.

### 4. Verdict and route

Write step change, keep incremental (no known approach reaches it; say why) or stop. The owner sets the bar; until then it is a proposal. Dates go to tailered-ai:two-date-plan, the cap to tailered-ai:capped-experiment, live changes through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: a verdict word, the owner named as the decider, and the routes named.

## Anti-Patterns

- A 10x goal with no first step that ships.
- Calling 10 percent on one league a step change.
- Claiming 10x in public before it is measured.
- Quoting the session reading as the owner's words.

## Source and adaptation

Source: original Tailered AI skill, which cites Wired (2013), reported Glass accounts and session reading [added] (3) of. No third-party skill text is copied.
