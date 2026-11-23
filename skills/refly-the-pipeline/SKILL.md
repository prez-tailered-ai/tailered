---
name: refly-the-pipeline
description: "Use when a day-build or the publishing step run of the shared pipeline that serves every league has finished; when the owner says use the same part twice, fly it again or run it again; when a run broke and someone proposes a per-league patch or copy; or before the next run of a pipeline that failed. Not for deciding which league scripts could share one pipeline; use tailered-ai:one-chassis-audit. Not for trying a new step on one league; use tailered-ai:one-league-trial."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Refly the pipeline

Use the same part twice. SpaceX landed a Falcon 9 booster in December 2015 and flew a landed booster again in March 2017: one part, inspected after each flight, then flown again. The owner's practice: one tested pipeline runs every league, is checked after each run, and runs again. The guard: Starship's first full flight in 2023 broke its own launch pad. Break things in a copy, never on members' main product.

## When to Activate

- A day-build or the publishing step run has just finished.
- The owner says "use the same part twice", "fly it again" or "run it again".
- A run broke and someone wants a per-league patch or a second copy of the pipeline.
- The next run is due on a pipeline that last failed.

Do not use for:
- deciding which league scripts could share one pipeline: tailered-ai:one-chassis-audit;
- trying a new step on one league: tailered-ai:one-league-trial.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the run (date and output folder or run ID), the leagues it served (NBA, NHL, college football, college basketball), and the pipeline's own tests.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `postflight.md`: one row per league with each check's result, each fault with its cause, owner and shared fix, the rerun result, and the verdict.

## Steps

### 1. Check every league after the run

For each league the run served, record games expected against games published, projections with no number, cards missing a sportsbook or prediction-market price, run time against the last five runs, and the pipeline's own tests. A league with no check result is a fail, not a pass.

Completion: a row per league with pass or fail on each check, and the numbers.

### 2. Name each fault and its owner

For each fail, write what broke, the first bad step and the named owner of that step. Say whether the fault is in the shared pipeline or in one league's input data.

Completion: every fail has a cause, a step and a named owner.

### 3. Fix the shared part once

Fix the fault in the shared pipeline so every league gets the fix. A per-league patch or a copied pipeline needs a written reason and goes to tailered-ai:one-chassis-audit. Add the check that would have caught it, with tailered-ai:ai-regression-testing.

Completion: one shared fix and one new check, or a written reason for a league-only fix.

### 4. Run it again in a copy

Rerun the fixed pipeline in a copied release folder for every league, not only the one that broke, and repeat step 1.

Completion: a new row per league; every league passes.

### 5. Refly or ground

Refly when every league passes: the pipeline is cleared for its next run. Ground when any league fails: the fix does not go live until it passes. Name who calls the next run. A fixed pipeline goes live through tailered-ai:workflow and the release coordinator on the owner's word. Nothing ships from here.

Completion: refly or ground, the owner, and the release route named.

## Anti-Patterns

- Patching one league and forking the pipeline.
- Calling a league fine because no check ran.
- Rerunning only the league that broke.
- Testing a fix on members' main product.

## Source and adaptation

Source: original Tailered AI skill, which cites SpaceX's Falcon 9 landing and reflight record, reported accounts of Starship's first full flight. No third-party skill text is copied.
