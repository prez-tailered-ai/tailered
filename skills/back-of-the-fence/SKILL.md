---
name: back-of-the-fence
description: "Use when a company change looks finished on the surface but its unseen parts were never opened: error paths, stale, empty and started-game states, logs, file and column names, time zones; when the owner says back of the fence, finish the inside or craft; or before a model or main product change is called done. Not for removing dead code; use tailered-ai:refactor-clean. Not for green checks that may hide a real problem; use tailered-ai:day-one-check."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Back of the fence

Finish the parts members rarely see as well as the parts they do. Jobs learned from his father to finish the back of a fence; the Mac team's signatures were molded inside the case, and he cared how the circuit board looked (Isaacson, 2011). The guard: NeXT's perfectionism cost years, and NeXT was reported to sell about 50,000 computers. So the inside work gets a time box, and only harm to a member blocks a release.

## When to Activate

- A change looks done but its unseen parts were not opened.
- The owner says "back of the fence", "finish the inside" or "craft".
- Before a model or main product change is called done.

Do not use for:
- removing dead code: tailered-ai:refactor-clean;
- green checks that may hide a problem: tailered-ai:day-one-check.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the change, the files it touched, and its release date.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank. When you cannot open the page, file or data a step asks for, still fill every row: name the exact page, file or command to check and the value you expect there, marked `proposal`. Every row of every table gets a verdict word and an owner.

Output: `inside.md`: each unseen part with its grade and evidence, the fixes, the logged flaws with owners, and the verdict.

## Steps

Lead the reply with the findings table: each state or part checked, the page or file it was seen in, sound, flaw or harm, and for each flaw an owner and a fix date.

Lead the reply with the parts table, then the verdict line, then detail.

### 1. List the unseen parts

For the change, list: the error path, the stale-price state, the no-market state, the started-game state, the logs it writes, file and column names, time zones on stored times, and the record it leaves. Give each its file or route.

Completion: a list of parts, each with a path or route.

### 2. Open and grade each one

Open it and grade it: sound, flaw (untidy but harmless) or harm (can mislead a member, such as a stale price shown as fresh or a started game shown as pregame). Cite what you saw: a file line or a rendered state.

Completion: every part has a grade and its evidence.

### 3. Fix inside a time box

Set the box (proposal: 90 minutes for the change). Every harm is fixed before release, with no time limit. Flaws are fixed inside the box, or logged with an owner and a date.

Completion: no harm left open, and every flaw fixed or logged with owner and date.

### 4. Give the verdict

Ship (no harm left) or hold (a harm is open). Name the owner. The release goes through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict word, the owner, and the release route named.

## Anti-Patterns

- Calling it done from the main screen alone.
- Polishing flaws past the time box while a harm waits.
- Shipping with a stale state that looks fresh.
- A logged flaw with no owner or date.

## Source and adaptation

Source: original Tailered AI skill, which cites Isaacson's Steve Jobs (2011) on the fence, the Mac case and the circuit board, and reported NeXT sales. No third-party skill text is copied.
