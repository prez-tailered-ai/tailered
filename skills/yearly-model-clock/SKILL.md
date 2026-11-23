---
name: yearly-model-clock
description: "Use when planning model versions for a coming season; when the owner asks for a release calendar, a yearly clock or when the next model ships; or when a model version date is at risk or has passed. Not for carrying one release through its checks; use tailered-ai:workflow. Not for choosing what to change in the model; use tailered-ai:ai-model-research."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Yearly model clock

Ship model versions on a fixed clock. At Computex in June 2024 NVIDIA set a one-year rhythm and named its next architectures in public. Blackwell then slipped: delays were reported in August 2024, and NVIDIA said it had changed the chip's mask to improve yield. The owner's version: a public calendar for model versions before each season, and say out loud when a date slips. Every date on it carries its source.

## When to Activate

- A season is coming (college football in August, NBA and NHL in October, college basketball in November) with no version calendar.
- The owner asks for a release calendar or a yearly clock, or when the next model ships.
- A version date is at risk or has passed.

Do not use for:
- a single delivery date with a stretch date and an honest estimate: tailered-ai:two-date-plan;
- carrying one release through its checks: tailered-ai:workflow;
- choosing what to change in the model: tailered-ai:ai-model-research.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the leagues and their season starts, the versions planned, what each needs (data, backtest, review), and past release dates.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `model-calendar.md`: one row per version (league, version, what changes, date, owner, source of the date, status, verdict) and a slip note for any moved row.

## Steps

Lead the reply with the result: the calendar table with every row marked on track, at risk or moved, and any slip said plainly with its new date. Detail follows.

### 1. Fix the clock

One version per league per season, dated before its first game; mid-season fixes are patches. Base each date on how long the last release took; a date with no basis is a marked proposal.

Completion: a row per league with a date, a named owner and the source of the date.

### 2. Check each date is reachable

List what must be true by when: data captured, backtest done, review passed. If the work cannot fit, move the date or cut scope now.

Completion: each row marked on track, at risk or moved, with a one-line reason.

### 3. Say the slip out loud

When a date is at risk or passed, write the slip note that day: old date, new date, the reason in one plain sentence, and what members use meanwhile. It is a draft for the owner, never folded quietly into the next version.

Completion: a slip note for every at-risk or moved row, or the words "no slips".

### 4. Route the calendar

The calendar and slip notes are public content: the owner approves the words, and they go live only through tailered-ai:workflow and the release coordinator on the owner's word. Nothing is posted from here. Give each row a verdict: keep, change or stop.

Completion: a verdict word on every row and the release route named.

## Anti-Patterns

- Dates set to please, with no past release behind them.
- Moving a date in the file without a slip note.
- A version shipped mid-season that changes numbers members relied on.
- A public date with no owner.

## Source and adaptation

Source: original Tailered AI skill, which cites NVIDIA's one-year rhythm at Computex 2024, its August 2024 statement on the Blackwell mask change, reported coverage of the delay. No third-party skill text is copied.
