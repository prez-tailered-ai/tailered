---
name: map-the-votes
description: "Use when the company is about to sign anything that grants shares, options, a SAFE, a note, profit share or votes; when a raise or partner or creator equity is discussed; or when the owner asks how much control he keeps, or says dual class or founder control. Not for pressure to hand over a decision; use tailered-ai:keep-the-final-say. Not for caps in contract terms; use tailered-ai:growth-cap-check."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Map the votes

Page and Brin kept control of Google through its share structure: the 2004 IPO gave their Class B shares ten votes each, and the 2014 split added Class C shares with no votes, so they could keep making long bets. The guard: control without answerability. Governance critics opposed the structure, and in 2018 a Senate committee was reported to have left an empty chair when Google sent neither Page nor Pichai. This skill does the arithmetic; it is not legal or financial advice, and a lawyer reads the terms.

## When to Activate

- the company is about to sign anything that grants shares, a SAFE, a note or votes.
- A raise or partner or creator equity is discussed.
- The owner asks how much control he keeps.

Do not use for:
- pressure to hand over a decision: tailered-ai:keep-the-final-say;
- caps in contract terms: tailered-ai:growth-cap-check.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: today's cap table, the proposed instrument and terms, and the rounds expected after it.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `vote-map.md`: votes by round, side rights, the control line and the verdict.

## Steps

Lead the reply with the votes-by-round table, then the verdict line, detail after.

### 1. Table today

List each holder, shares by class, votes, percent owned and percent of votes; where unknown, propose (such as the owner 100 percent of 10,000,000 shares).

Completion: a table whose percentages sum to 100.

### 2. Add this deal and two more rounds

Convert the SAFE or note at the proposed price, then add two later rounds, such as $2 million at $10 million and $8 million at $40 million (proposal). Show votes after each. List side rights that carry control without votes: board seats, vetoes, protective provisions.

Completion: percent of votes after each of three rounds, and every side right listed.

### 3. Find the control line

The owner's line, proposal: a majority of votes and of the board. Name the round and term that break it. Write what the owner will still report and to whom, so control stays answerable.

Completion: the round and term where control breaks, or "holds through round three", and the reporting written.

### 4. Verdict

Write sign (as is), change (name the term to change, such as non-voting shares or no veto) or stop. A lawyer reads the terms first; the owner signs. Nothing here signs, sends or files.

Completion: a verdict word, the term to change where it applies, and the owner named as the signer.

## Anti-Patterns

- Reading this round only.
- Missing control hidden in side rights.
- Treating control as freedom from reporting.
- Signing before a lawyer reads the terms.

## Source and adaptation

