---
name: long-term-letter
description: "Use when a choice trades this season's results against the company's position years out, such as dropping a league, a cheaper data source or a model shortcut; when the owner says long term, worth it in three years, or asks for a letter like Bezos' 1997 letter; or when no written long-term commitments exist. Not for setting a price; use tailered-ai:price-forces-cost."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Long-term letter

Write down a few long-term commitments once, then judge choices against them. Bezos' first shareholder letter, in 1997, said Amazon would choose long-term leadership over short-term profit, and every later letter carried it. It also took until 2003 for a first full-year profit, $35.3 million. The owner's guard: a small company cannot carry that. So every commitment here has a floor.

## When to Activate

- A choice helps this season and may hurt later, or the reverse.
- The owner says "long term", "is this worth it in three years" or "write our letter".
- No written long-term commitments exist in the project.

Do not use for:
- setting a price: tailered-ai:price-forces-cost;
- capping one experiment: tailered-ai:capped-experiment.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the decision, and the letter at `docs/long-term-letter.md` in the project if one exists. Runway in months and monthly cash, from the owner; mark it unknown if not given.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: the letter (new or updated, approved by the owner) and `decision.md` with the table and recommendation.

## Steps

### 1. Find the letter

Read `docs/long-term-letter.md`. If none exists, write one in step 2 before judging anything, and say so.

Completion: a letter exists or is drafted.

### 2. Write or update the letter

One page. Three to five commitments, each with a measure, for example beating a public benchmark over a season, or member renewal. Say what the company gives up short-term for them and what it will not trade: member trust, estimates never advice, an honest record. Add the floor: each long bet names a checkpoint date and a cash or time limit, and a missed checkpoint shrinks or ends it. The letter changes only on the owner's word.

Completion: one page, a measure on every commitment, the floor present, and the owner's approval noted or asked for.

### 3. Judge the choice

For each commitment, does the choice help, hurt or not touch it over three years? Then the floor: what the choice costs in cash or time against the runway.

Completion: a table of commitments by effect, plus one runway line with the cost in hours or dollars, estimated and marked if not known.

### 4. Recommend

Keep, change or stop, naming the commitment that decided it. When a choice helps the long term but breaks the floor, the floor wins; propose the smaller version that fits.

Completion: the word keep, change or stop, with its deciding line; never "it depends".

## Anti-Patterns

- Commitments that are slogans with no measure.
- "Long term" as cover for a bet with no checkpoint.
- Rewriting the letter to fit the decision at hand.
- Planning on years of losses, as Amazon could and the company cannot.

## Source and adaptation

