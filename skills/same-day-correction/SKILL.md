---
name: same-day-correction
description: "Use when a published projection, main product card, market price or the publishing step output is found wrong; when the owner says push a fix, correct every card, or tell members what changed; or when a fix shipped with no note to members. Not for diagnosing a live incident's cause; use tailered-ai:agent-introspection-debugging. Not for the release steps themselves; use tailered-ai:workflow."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Same-day correction

Fix it by sending software, then say so. Tesla fixes cars over the air: in 2023 two recalls, of about 363,000 and about 2 million cars, were fixed by software updates. The owner's practice: push a correction to every card the same day and post what changed. The guard: a software fix is still a release, and a regulator later questioned whether one of those fixes was enough. Do not say fixed before it is, and never post a number before it is real.

## When to Activate

- A published projection, main product card, market price or the publishing step output is wrong.
- The owner says "push a fix", "correct every card" or "tell members what changed".
- A fix shipped with no note to members.

Do not use for:
- diagnosing a live incident's cause: tailered-ai:agent-introspection-debugging;
- the release steps themselves: tailered-ai:workflow;
- the routine check after every run: tailered-ai:refly-the-pipeline.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: what was wrong, where it was seen, and when it was published.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `correction.md`: every affected card with its wrong and right number, the fix and its owner, the release time, the live check, and the member note draft.

## Steps

### 1. Find every affected card

Search the published output for every card the fault touched, across every league and date, not only the one reported. List each card with its wrong and right number.

Completion: a count of affected cards and a table of wrong against right numbers.

### 2. Fix once, at the source

Fix the cause in the shared pipeline, so corrected numbers come from a rerun, not from hand edits on cards. Run the post-run check from tailered-ai:refly-the-pipeline in a copy. Name the owner.

Completion: the fix, a passing rerun for every affected card, and the owner.

### 3. Ship it today through the route

The correction goes live through tailered-ai:workflow and the release coordinator on the owner's word, on the day the fault was found. If it cannot ship today, say so and give the time it will.

Completion: the release requested with a target time today, or the stated reason and time it waits.

### 4. Check live, then draft what changed

After it ships, open each corrected card on the live main product and confirm the new number. Then draft a short member note: what was wrong, which cards, the corrected numbers, when it was fixed, and what now stops it happening again. Only numbers seen on the live corrected cards go in the note. Verdict: post or hold. The owner approves and posts it; nothing is posted from here.

Completion: every corrected card confirmed live, a draft whose every number matches them, and post or hold left with the owner.

## Anti-Patterns

- Correcting only the card someone reported.
- Hand-editing cards instead of fixing the source.
- Fixing quietly with no note to members.
- Saying fixed before the live cards show it.

## Source and adaptation

Source: original Tailered AI skill, which cites NHTSA's 2023 Tesla recall notices, reported accounts of NHTSA's later query. No third-party skill text is copied.
