---
name: two-date-plan
description: "Use when setting a deadline for a launch, a new league, a model change or a main product feature; when the owner sets a date the team calls impossible, or says ship it by Friday or ten times faster; or before any date is told to members, creators or the public. Not for deciding whether the change is reversible; use tailered-ai:two-way-door-call. Not for the release itself; use tailered-ai:workflow."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Two-date plan

Musk sets dates nobody believes and often closes most of the gap; he has said himself that he is optimistic on timing. The guard: self-driving dates told to the public were missed year after year. So keep two dates: a stretch date inside the team, and a public date only once it is real. The owner's rule from "funding secured" holds for dates too: never tell members a date or a number before it is real.

## When to Activate

- A deadline is being set for a launch, new league, model change or main product feature.
- The owner sets a date the team calls impossible, or says "by Friday" or "ten times faster".
- Someone wants to tell members, creators or the public when something will ship.

Do not use for:
- deciding whether the change is reversible: tailered-ai:two-way-door-call;
- carrying the change through release: tailered-ai:workflow;
- removing steps to close the gap: tailered-ai:delete-the-step.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the work, the owner's date if he set one, and the team's own estimate.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `dates.md`: the stretch date, the honest estimate, the gap and its closers, the public date or "none yet", and the weekly verdicts.

## Steps

### 1. Set the stretch date and owner

Take the owner's date. If he gave none, propose one at about half the team's estimate and mark it `proposal`. Name the one owner of the work.

Completion: a stretch date and a named owner.

### 2. Write the honest estimate and the gap

Estimate the finish date on today's plan. The gap is the days between it and the stretch date. List what would close it: cut scope, delete steps with tailered-ai:delete-the-step, run parts in parallel. Give each closer the days it saves.

Completion: an estimate, the gap in days, and at least three closers with days saved.

### 3. Hold the public date

The stretch date stays inside the team. It never goes in a main product note, a member message, a creator promise or a post. A public date exists only when the work passes in a copy, or when the estimate has held for two weeks with a margin. Until then the public date is "none yet".

Completion: a public date with its evidence, or "none yet" with the reason.

### 4. Check each week and cut

Each week compare progress with both dates. If the stretch date will be missed, say so that day and cut scope. Never move the public date in silence. Anything that goes live goes through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: on track, cut or reset, with the days remaining.

## Anti-Patterns

- Telling members the stretch date.
- Hiding a miss until the day it lands.
- Padding the stretch date so it is easy.
- Moving the public date without saying why.

## Source and adaptation

Source: original Tailered AI skill, which cites Musk's own remarks on his timing, reported self-driving timelines from 2016 on. No third-party skill text is copied.
