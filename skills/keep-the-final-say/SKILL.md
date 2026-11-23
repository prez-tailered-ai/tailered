---
name: keep-the-final-say
description: "Use when an investor, buyer, partner, sportsbook or loud group of members pushes the company to hand over a decision or change course for a short-term number: a board seat, a veto, an offer to buy, a demand to publish picks; when the owner asks who should decide this, should we give them a say, or should we sell. Not for judging a choice against long-term commitments; use tailered-ai:long-term-letter. Not for caps in contract terms; use tailered-ai:growth-cap-check."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Keep the final say

Keep the decisions that define the company with the owner, so short-term pressure cannot move them. Zuckerberg turned down a reported $1 billion offer from Yahoo in 2006, and dual-class shares since the 2012 IPO have kept his majority vote. The guard: that control left no check inside the company, and in 2019 the FTC had to impose an independent board privacy committee from outside. So keeping the final say comes with a written check the owner holds himself to.

## When to Activate

- An investor, buyer or partner asks for a seat, a veto, approval rights or an exclusive.
- Someone offers to buy the company or a part of it.
- Pressure to change a defining rule for a quick number, such as publishing picks instead of projections.
- The owner asks "who should decide this" or "should we give them a say".

Do not use for:
- judging one choice against long-term commitments: tailered-ai:long-term-letter;
- finding caps in contract terms: tailered-ai:growth-cap-check;
- naming the owner of an initiative: tailered-ai:single-threaded-owner.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: who is pushing, what they ask for, what they offer, and the decision rights the owner holds today.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `final-say.md`: the decision-rights table, the pressure test, the owner's written check, and the verdict.

## Steps

### 1. List the decision rights

Write the decisions that define the company and who holds each today: estimates never advice, model rules, the publishing step rules, member data use, price, leagues covered, release word. Mark which one the request touches.

Completion: a table of five or more rights with the holder, and the touched right marked.

### 2. Test the pressure

State what is offered in a number (dollars, members, months of runway) and what the company gives up. Say how the touched right would be used by the other side in a bad season. Check the written long-term commitments with tailered-ai:long-term-letter.

Completion: the gain as a number, the loss in one sentence, and the bad-season case.

### 3. Write the check on the owner

Control needs a limit too. Write the rules the owner will not override alone: member data collected for one purpose is never used for another, such as marketing, without consent, and the responsible-gambling line. Name who reviews a change to them, such as an outside advisor, marked `proposal` if unnamed.

Completion: two or more written rules and a named reviewer.

### 4. Give the verdict

One word: hold (keep the right), trade (give something smaller, named) or give (hand it over, with why). The owner decides and answers the other side. This skill sends no reply and signs nothing.

Completion: the verdict, the number behind it, and the decision left with the owner.

## Anti-Patterns

- Trading a defining right for one season's money.
- Treating every request as a threat to control.
- Control with no written check on the founder.
- Answering the investor from this skill.

## Source and adaptation

