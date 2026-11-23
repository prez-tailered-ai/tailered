---
name: line-up-every-party
description: "Use when a company product needs several outside parties to say yes before it can work, such as Partner A, Partner B, a sportsbook, an odds feed or a data owner; when the owner says get them all on board, do a deal with the markets or negotiate the whole thing; or when a launch waits on more than one outside yes. Not for reading one deal's terms for caps; use tailered-ai:growth-cap-check. Not for renewing one long-term supplier; use tailered-ai:partner-for-decades. Not for licensing one tool; use tailered-ai:license-not-rebuild."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Line up every party

Jobs brought the five major record labels into the iTunes Music Store at 99 cents a song (April 2003), and launched the iPhone with one carrier, Cingular, later AT&T (2007). The guard: in 2013 a US court found Apple had conspired with five publishers to raise e-book prices; Apple paid $450 million (2014 settlement). At the company each deal is with one party, written and visible to the owner; none coordinates prices or hiring, and no party learns another's terms.

## When to Activate

- A product needs more than one outside party to say yes.
- The owner says "get them all on board" or "do a deal with the markets".
- A launch waits on several outside yeses.

Do not use for:
- reading one deal's terms: tailered-ai:growth-cap-check;
- renewing one supplier: tailered-ai:partner-for-decades;
- licensing one tool: tailered-ai:license-not-rebuild.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the product, the parties it needs, and what the company can offer each.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank. When you cannot open the page, file or data a step asks for, still fill every row: name the exact page, file or command to check and the value you expect there, marked `proposal`. Every row of every table gets a verdict word and an owner.

Output: `parties.md`: the party map, ask order, fallback, and one checked draft per party.

## Steps

Lead the reply with the party map, then the verdict line, then detail.

### 1. Map who must say yes

For each party: what the company needs from it, what it gets, and what it does if it says no.

Completion: a table with need, gain and no-option for every party.

### 2. Order the asks

Name the yes that unlocks the others and ask that party first. Name a smaller fallback product that needs fewer parties, such as one market's prices only.

Completion: the ask order, the first party, and the fallback.

### 3. Draft one deal per party

Draft terms, price, length and exit for each party, separately. Check each draft: written, between the company and that party only, no term on prices with any other party, no no-hire or no-recruit term, no side letter, visible to the owner. A failed check is cut from the draft.

Completion: every draft with its checks passed, or the failing term named and cut.

### 4. Hand it to the owner

The owner decides each ask and who sends it. Run tailered-ai:growth-cap-check on any term offered back. This skill sends, signs and agrees to nothing. Give the plan a verdict: go (first yes is likely), change (use the fallback) or stop.

Completion: the verdict word, the owner named as the decider, and nothing sent.

## Anti-Patterns

- Telling one party what another agreed.
- A spoken side deal outside the written terms.
- Any term that sets prices across parties.
- Waiting on every party when a fallback could ship.

## Source and adaptation

