---
name: labs-opt-in
description: "Use when an unfinished feature, card, alert, model view or league should be tried by some members first; when the owner says Labs, beta, early access or let a few members try it; or when a test is in front of members with no label, opt-in or end date. Not for starting a feature from a member's ask; use tailered-ai:press-release-first. Not for capping a big bet's money or hours; use tailered-ai:capped-experiment."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Labs opt-in

Ship early only to members who choose it. Google Labs (from 2002) and Gmail Labs (2008) put rough features behind a clear label that each user turned on; Google closed Labs in 2011. The guard is Glass, the owner's not-to-copy: sold to the public at $1,500 in 2013 before its job was proven, withdrawn from consumers in January 2015. A Labs test is labeled, opt-in and capped, and its job is clear first.

## When to Activate

- An unfinished feature, card, alert or model view should reach some members first.
- The owner says "Labs", "beta" or "early access".
- A test is in front of members with no label, opt-in or end date.

Do not use for:
- starting a feature from a member's ask: tailered-ai:press-release-first;
- capping the money or hours of a big bet: tailered-ai:capped-experiment;
- a big idea whose job is not clear: tailered-ai:job-before-moonshot;
- a public accuracy test: tailered-ai:prove-it-in-public.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the feature, its job sentence, and how many members could try it.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `labs-plan.md`: job, label, opt-in, cap, number, end date and exit verdict.

## Steps

Lead the reply with the Labs card, then the verdict line, then the detail.

### 1. Check the job

One sentence: who it is for and what it does for them. If it cannot be written, stop and use tailered-ai:job-before-moonshot.

Completion: the job sentence, or a stop.

### 2. Label it and make it opt-in

A visible "Labs" tag on every screen it touches, a line on what may break, a switch the member turns on, and an off switch that works at once. Members who did not opt in see nothing. No price; Labs is never sold.

Completion: label text, opt-in, off switch and "no price" written.

### 3. Cap it

The most members, such as 50; an end date, such as 4 weeks out; the one number it is read by, set with tailered-ai:test-then-argue; and the cost cap.

Completion: member cap, end date, number with target, and cost cap, each real or marked `proposal`.

### 4. Exit on the date

At the end date: graduate, change, or close. Draft the note to opted-in members for the owner; send nothing. Name the owner. Turning Labs on, and any graduation, ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict word, the owner, the draft note and the release route.

## Anti-Patterns

- A Labs feature on by default.
- A Labs feature behind the paywall or priced.
- No end date, so Labs becomes permanent.
- More Labs tests than anyone reads.

## Source and adaptation

Source: original Tailered AI skill, which cites Google Labs and Gmail Labs' public record. No third-party skill text is copied.
