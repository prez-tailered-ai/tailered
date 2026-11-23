---
name: pause-publish-fix
description: "Use when a wrong line, projection or price reached members through the main product or the publishing step and the cause is in the pipeline; when the owner says stop publishing, pause the main product or fix trust first; or when the same fault comes back. Not for correcting the cards and telling members; use tailered-ai:same-day-correction. Not for finding which layer caused it; use tailered-ai:full-stack-trace."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Pause publishing, fix the pipeline

Gates's Trustworthy Computing memo of January 2002 put security ahead of features; Windows feature work was reported to stop for a security push. The owner's practice: after a wrong line, pause publishing and fix the pipeline before new features. The guard: the Blaster worm still hit Windows in 2003, so the restart needs a check that would have caught the fault.

## When to Activate

- A wrong line reached members and the cause is in the pipeline.
- The owner says "stop publishing", "pause the main product" or "fix trust first".
- The same wrong-line fault comes back.

Do not use for:
- correcting the cards and telling members: tailered-ai:same-day-correction;
- finding which layer caused it: tailered-ai:full-stack-trace;
- the routine check after every run: tailered-ai:refly-the-pipeline.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the wrong line, where and when it was published, and today's leagues on the main product.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `pause-and-fix.md`: pause request, held features, fix, new check, restart request.

## Steps

Your reply leads with the pause table (league, publishing now, pause or keep, reason), then the verdict line: pause, keep or restart.

### 1. Ask for the pause

Propose pausing only the leagues the fault can reach. The pause is a live change: request it through tailered-ai:workflow and the release coordinator on the owner's word. Never stop anything from here. Name the owner who runs it.

Completion: a pause request with leagues, owner and time, at the release coordinator.

### 2. Hold new features

Mark every open feature change to this pipeline held until the restart.

Completion: the held list, or "no open features".

### 3. Fix the pipeline, not the line

Find the stage that made the line (tailered-ai:full-stack-trace if unclear) and fix it in a copy. Add a check that would have stopped it, such as a range or stale-price check, failing on the bad run and passing on the fixed one. Card corrections go to tailered-ai:same-day-correction.

Completion: the fault stage, the fix, and the new check's fail and pass.

### 4. Ask for the restart

Restart only when the check passes on a full rerun of every paused league. Request it through tailered-ai:workflow and the release coordinator on the owner's word, then release the held features. Verdict: restart or keep paused, with the deciding number, such as 0 of 412 lines failing.

Completion: the rerun result, the restart request and the verdict.

## Anti-Patterns

- Hand-editing the wrong line and carrying on.
- Pausing or restarting without the owner's word.
- Shipping a feature during the pause.
- Restarting with no new check.

## Source and adaptation

Source: original Tailered AI skill, which cites Gates's Trustworthy Computing memo of 15 January 2002, reported accounts of the 2002 Windows security push, the August 2003 Blaster worm. No third-party skill text is copied.
