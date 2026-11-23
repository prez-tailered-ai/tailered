---
name: pipe-before-demand
description: "Use when a new sport, league, market type or price source is coming and each one so far needed its own build; when the owner says build the tool before demand or one general pipe, or asks how many days a new sport would take; or before someone copies a league's pipeline step to make a new one. Not for merging per-league scripts that already exist; use tailered-ai:one-chassis-audit. Not for trying a step on one league; use tailered-ai:one-league-trial."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Pipe before demand

Build the general tool before the demand arrives. NVIDIA launched CUDA in 2006, years before AlexNet trained on its GPUs in 2012. The owner's version: one general pipe that can take a new sport or market in days. The guard: the company cannot carry years of platform cost, so it builds only for the next two named arrivals, under a cap, and every record keeps its source.

## When to Activate

- A new sport, market type or price source is planned, and the last one took weeks of one-off code.
- The owner says "build the tool before demand" or "one general pipe", or asks how many days a new sport would take.
- Someone is about to copy one league's pipeline step to make another.

Do not use for:
- merging per-league scripts that already exist: tailered-ai:one-chassis-audit;
- trying the new pipe on one league: tailered-ai:one-league-trial;
- whether to enter a market at all: tailered-ai:capped-experiment.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: today's pipeline steps, the sports or markets in view, and how long the last addition took.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `pipe-plan.md`: the step table, days today and target, the build list, the cap and the verdict.

## Steps

### 1. Count the days today

For each step from capture to the main product card, write what a new sport or market needs: code, config or nothing. Add up the days the last addition took, from its record or a marked proposal.

Completion: a step table with code, config or nothing on every step, and a total in days.

### 2. Name the next two arrivals

Name the next two sports or markets and the pipe's owner, a person or session. No named arrival, no build.

Completion: two named arrivals and one named owner.

### 3. Turn code into config

For each step marked code, write what would make it config: a league table, one market adapter shape. Every record keeps where it came from (feed, capture time); a pipe that drops the source is lossy, not general. Target: five days or fewer for a new sport unless the owner names another.

Completion: a build list, a target in days, and the source field named in each record shape.

### 4. Cap it and decide

Cap the build in hours with tailered-ai:capped-experiment. Verdict: build, change (a smaller list) or stop (one-off work is cheaper). The first run goes through tailered-ai:one-league-trial; anything live ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict word, the cap in hours, and the release route named.

## Anti-Patterns

- A platform for sports nobody has named.
- Copying a league's script "just this once" again.
- A record shape with no source field.
- Calling it general before a second sport ran through it.

## Source and adaptation

Source: original Tailered AI skill, which cites NVIDIA's 2006 CUDA launch, the 2012 AlexNet paper. No third-party skill text is copied.
