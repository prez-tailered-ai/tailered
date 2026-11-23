---
name: admit-and-rewrite
description: "Use when the way the company built something is the wrong bet and patches keep failing; when members have moved, such as from sportsbooks to prediction markets, and the product has not; when the owner says we bet wrong, start over, rewrite it or pivot; or when a rewrite is half done with no end date. Not for trying a new idea as an experiment; use tailered-ai:capped-experiment. Not for announcing a new direction to every session; use tailered-ai:direction-memo."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Admit and rewrite

Say plainly when a bet was wrong, then rewrite toward where members already are. In 2012 Zuckerberg called Facebook's HTML5 mobile app its biggest mistake, and the team rebuilt the iOS app natively and shipped it that August; mobile became the core of the business. The guard: the 2021 turn to the metaverse went where users were not yet, with years of large reported losses. A company pivot follows members who are already there.

## When to Activate

- The same part keeps breaking and each patch buys a week.
- Members have moved, such as to Partner A and Partner B, and the main product still serves the old path.
- The owner says "we bet wrong", "start over", "rewrite it" or "pivot".
- A rewrite is half done with no end date.

Do not use for:
- trying a new idea with a loss cap: tailered-ai:capped-experiment;
- telling every session the new direction: tailered-ai:direction-memo;
- trying a pipeline change on one league: tailered-ai:one-league-trial.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the current approach, what keeps failing, and where members are now, with counts.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `rewrite.md`: the admitted bet, the member evidence, the rewrite plan with dates, the stop rule, and the verdict.

## Steps

### 1. Admit the bet

Write one sentence: we bet on X, and it was wrong because Y. Add the cost so far, such as patches in the last 30 days or hours lost.

Completion: the sentence and one cost number.

### 2. Follow the members

Show where members already are: the share using the new path today, such as traders as a share of active members. If fewer than a quarter are there now, the move is a bet, not a rewrite; send it to tailered-ai:capped-experiment.

Completion: the share as a number, and rewrite or experiment.

### 3. Plan the rewrite

Freeze new features on the old path from a date. The old path keeps running until the new one passes the same checks. Set two or three milestones with dates and name one owner.

Completion: the freeze date, the milestones with dates, and the owner.

### 4. Set the stop rule and judge

Write what would stop the rewrite: a missed milestone by more than two weeks, or members not moving. Give one verdict: rewrite, patch (the bet was right; fix one named part) or stay. The owner decides. Each step ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the stop rule, the verdict with its number, and the release route named.

## Anti-Patterns

- Patching the wrong bet for another season.
- Pivoting to where members might go someday.
- Switching off the old path before the new one passes.
- A rewrite with no freeze date and no end.

## Source and adaptation

Source: original Tailered AI skill, which cites Zuckerberg's September 2012 remarks on HTML5, the August 2012 native iOS app, and the reported Reality Labs losses after the 2021 rename to Meta. No third-party skill text is copied.
