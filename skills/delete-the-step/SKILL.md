---
name: delete-the-step
description: "Use when the day build, the publishing step or another repeated process has grown steps nobody questions; when the owner says delete the step, simplify, the five steps, or asks who owns a step; or before automating, scripting or scheduling a manual step. Not for timing where a session's minutes went; use tailered-ai:walking-time-audit. Not for checking whether green metrics hide a real problem; use tailered-ai:day-one-check."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Delete the step

Musk's five steps run in order: question each requirement, delete what you can, simplify, speed up, and automate last. Isaacson (2023) reports his rule that if you do not add back at least a tenth of what you deleted, you did not delete enough. The guard: in 2018 Musk said excessive automation at Tesla was a mistake; the line was automated before it was simplified. The owner's practice: put a name on every step of the day build, delete the ones nobody can explain, and only then automate.

## When to Activate

- The day build, the publishing step or another repeated process has grown steps nobody questions.
- The owner says "delete the step", "simplify", "the five steps" or "who owns this step".
- Someone proposes a script, timer or automation for a manual step.

Do not use for:
- timing where a session's minutes went: tailered-ai:walking-time-audit;
- checking whether green metrics hide a real problem: tailered-ai:day-one-check;
- a failure that keeps coming back: tailered-ai:mechanism-not-intention.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the process and its step list (runbook, script, record or the last run's log).

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `steps.md`: every step with its owner, time, the harm if removed and its verdict, plus the delete list, the automate list and the check-back date.

## Steps

### 1. Put a name on every step

List every step in order: what it does, how long it takes and how often it runs. Put a person's or session's name on each: the one who asked for it and can say why. A step with no name is marked `unowned`.

Completion: every step has a name or `unowned`, and a time.

### 2. Question each requirement

Ask each owner: what breaks for members or for the model if this step is gone? The answer must name a concrete harm, such as a wrong number on a card. "We always do it", or no answer, makes the step delete. Every `unowned` step is delete.

Completion: each step marked keep, with its harm, or delete.

### 3. Delete, then simplify

Propose removing every delete step. Then simplify the keeps: merge them, cut inputs, drop repeated checks. Set a check-back date two weeks out. If fewer than one in ten deletions came back by then, say the cut may not have gone far enough. Deletions are tried in a copy; the owner approves removing anything from the live day build.

Completion: a delete list, a simplify list and a check-back date.

### 4. Speed up, then automate last

Work only on steps that survived. Speed up the slow ones first. Automate a step only when it is kept, simplified, and has run by hand the same way at least three times. Each change goes live through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: an automate list in which every step passed steps 2 and 3, and the release route named.

## Anti-Patterns

- Automating a step before asking why it exists.
- Keeping a step because its owner is senior.
- Deleting from the live day build without the owner.
- Adding a new step to watch the old ones.

## Source and adaptation

Source: original Tailered AI skill, which cites Musk's 2021 Starbase tour, Walter Isaacson's Elon Musk (2023), Musk's 2018 post on automation at Tesla. No third-party skill text is copied.
