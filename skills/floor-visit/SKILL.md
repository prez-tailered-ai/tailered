---
name: floor-visit
description: "Use when the owner has not looked at the work where it happens lately; when the owner says go see it, walk the floor, or asks what the people running the day build, the publishing step or member support think is in their way; or when reports say fine but nobody has asked the doer. Not for giving a new feature to its first members; use tailered-ai:hand-deliver-first. Not for where a session's time went; use tailered-ai:walking-time-audit."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Floor visit

Go where the work happens and listen to the people doing it. Walton flew his own plane from store to store, walked the aisles and asked clerks what was selling and what was in their way. At the company the floor is the day build as it runs, the main product as a member sees it, and the sessions and people doing the work. The guard: a visit that changes nothing teaches people not to speak, and a visitor who fixes the shelf himself takes the work from its owner.

## When to Activate

- The owner has not looked at the live work in a week or more.
- The owner says "go see it", "walk the floor" or asks what is in people's way.
- Reports say fine but nobody has asked the session or person doing the work.

Do not use for:
- putting a new feature in front of its first members: tailered-ai:hand-deliver-first;
- where a session's time or tokens went: tailered-ai:walking-time-audit;
- whether green metrics are real: tailered-ai:day-one-check.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the place to visit, the visitor, and who does the work there.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `visit.md`: the place, what was seen, what the doers said, and the one fix.

## Steps

Lead the reply with the one fix and its owner, then the verdict line, then what was seen and heard.

### 1. Pick the floor

Choose one place (proposal: today's day build run and the NBA main product on a phone). Name the visitor, the owner or the owner, and the date.

Completion: place, visitor and date are written.

### 2. Look before you ask

Watch the work as it is: read the run log, open the main product as a member, read the queue record. Read only. Never write another session's record or take over its work.

Completion: three first-hand observations, each with where it was seen, such as a stale price or a slow step.

### 3. Ask the doer

Ask each person or session doing the work two questions: what is in your way, and what have you seen elsewhere that we should copy? Ask a session through its owner or the queue, not by editing its record. Write the answers in their own words.

Completion: answers from at least one named doer, attributed.

### 4. Bring back one fix

Pick one fix. Its owner is the work's owner, not the visitor. Mark the other answers fix, watch or drop. Draft a short note telling the doer what happened to their answer; do not send it. A live change ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: one fix with an owner and date, every answer marked, and the note drafted.

## Anti-Patterns

- A visit that ends with no fix.
- The visitor doing the fix instead of the owner.
- Reading summaries instead of the work itself.
- Asking only questions with a yes answer.

## Source and adaptation

Source: original Tailered AI skill, which cites Walton and Huey, Sam Walton: Made in America (1992). No third-party skill text is copied.
