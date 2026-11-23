---
name: mechanism-not-intention
description: "Use when the same failure has happened twice or more and the proposed fix is to be careful, remember, double-check or add a reminder; or when the owner says this keeps happening. Not for writing the test that pins one fixed bug; use tailered-ai:ai-regression-testing."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Mechanism, not intention

Replace a promise to be careful with something that acts on its own. Bezos' rule, as Bryar and Carr record it: good intentions do not work, mechanisms do. A mechanism has three parts: a tool, its adoption, and inspection. The guard is the opposite failure: mechanisms pile up into process nobody questions, which his 2016 letter calls process as proxy. So each mechanism names the failure it stops, and it goes when it stops catching it.

## When to Activate

- The same failure has happened at least twice.
- The proposed fix is "be careful", "remember to", "double-check" or a reminder note.
- The owner says "this keeps happening".

Do not use for:
- the regression test for one fixed bug: tailered-ai:ai-regression-testing;
- finding the cause of a failure; find it first, then use this skill.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the repeated failure, with the date of each occurrence.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `mechanism.md`: the failure log, the three parts, and the drop rule.

## Steps

### 1. Log the failure

List each occurrence with its date, what happened and what it cost. One occurrence calls for a fix, not a mechanism: say so and stop.

Completion: at least two dated occurrences, or the stop line.

### 2. Design the smallest mechanism

Tool: a check, block, default or template that acts without anyone remembering, such as a guard in the script or a test that fails. Prefer making the wrong thing impossible over warning about it. Adoption: where it runs on every relevant action, named by file or step, and one owner: when no person is known, the owner of the script or step it lives in, such as the day-build owner, marked `proposal`. Inspection: how anyone sees it working, such as a count of catches in a log.

Completion: all three parts filled, with one named owner.

### 3. Add the drop rule

Name the failure it stops and a review date, 60 days out unless the owner sets another. At review, a mechanism that caught nothing is dropped or kept with a written reason.

Completion: the drop rule with its date.

### 4. Hand it over

Building it goes through tailered-ai:lockin. Anything live ships through tailered-ai:workflow and the release coordinator on the owner's word. This skill changes nothing live.

Completion: the next step is named, and nothing live changed.

## Anti-Patterns

- A reminder, a checklist line or "be careful" as the fix.
- A mechanism with no owner, or no way to see it work.
- Stacking a new mechanism on top of one that already covers the failure.
- A mechanism for a one-time event.

## Source and adaptation

Source: original Tailered AI skill, which cites Bryar and Carr, Working Backwards (2021), and Amazon's 2016 shareholder letter. No third-party skill text is copied.
