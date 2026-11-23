---
name: test-then-argue
description: "Use when a change to a main product card, an alert, the model or a publishing-step rule is about to ship; when two people disagree on which version is better; when the owner says test it, measure before you believe, or what number does this move; or when a change shipped with no number. Not for capping the loss of a big bet; use tailered-ai:capped-experiment. Not for a copied feature against a rival's; use tailered-ai:copy-then-outgrow."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Test then argue

Google ran its first A/B test in 2000, on how many results a page should show (reported). The guard: designer Douglas Bowman left in 2009 after 41 shades of blue were tested for one link. Testing trivia wastes the method, and a target set after the result is not a test. The rule, written by a session and not the owner: a change to a card or a model ships with the number it must move and the test that reads it.

## When to Activate

- A card, alert, model or the publishing step rule change is about to ship.
- Two people disagree on which version is better.
- The owner says "test it" or "what does this move", or a change shipped with no number.

Do not use for:
- capping the loss of a big bet: tailered-ai:capped-experiment;
- a copied feature against the rival's: tailered-ai:copy-then-outgrow;
- putting the test in front of members: tailered-ai:labs-opt-in.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the change and any past numbers for the same measure.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `test.md`: number, target, test, read date, result and verdict.

## Steps

Lead the reply with the test table, then the verdict line, then the detail.

### 1. Name the number

One number the change must move, its value now, the target and the read date. For a model: log loss or closing-line value on held-out games. For a card: the share of members who open the price comparison.

Completion: number, now, target and date, each real or marked `proposal`.

### 2. Fix the test first

Before the change ships, write how it is read: a backtest on games the model never saw, or an A/B window. State the sample needed, such as 300 games or 400 members per side. Time-stamp `test.md`; the target does not move after.

Completion: the test and sample size written and time-stamped before any result.

### 3. Read it and decide

Compare the result to the target. Ship, change or drop. Disagreement after that is a proposal for the next test, not a veto. Name the owner who reads it.

Completion: ship, change or drop, the number that decided it, and the owner.

### 4. Name the route

A live change ships through tailered-ai:workflow and the release coordinator on the owner's word. A test members see goes through tailered-ai:labs-opt-in.

Completion: the release route is named.

## Anti-Patterns

- Setting the target after seeing the result.
- Testing link colors while the model goes untested.
- A sample too small to tell either way.
- Shipping on agreement alone.

## Source and adaptation

Source: original Tailered AI skill, which cites Wired's 2012 report on Google's A/B testing, Douglas Bowman's 2009 post, and the note's practice 3, marked [added]. No third-party skill text is copied.
