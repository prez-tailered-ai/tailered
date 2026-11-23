---
name: price-on-value
description: "Use when setting or changing what members pay; when a plan or tier is priced at cost plus a margin; when the owner asks what a membership is worth, says price on value, or asks whether we charge too little or too much; or before a pricing page states what members get. Not for working back from a price the owner already named to job costs; use tailered-ai:price-forces-cost. Not for creator revenue shares; use tailered-ai:creator-share-floor."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Price on value

Charge for what the member gets, not for what the parts cost. NVIDIA prices on what its products do for the buyer. In October 2022 it withdrew the RTX 4080 12GB after buyers said its name and price overstated what it delivered. The company's guard: a projections product cannot price on promised winnings. Value is stated as what a member gets, such as time saved, prices compared across books and markets, and a graded record, and every value number carries its source.

## When to Activate

- A price or tier is being set or changed.
- A plan is priced as cost plus a margin.
- The owner asks what a membership is worth, or whether we charge too little or too much.
- A pricing page is about to say what members get.

Do not use for:
- working back from a named price to job costs: tailered-ai:price-forces-cost;
- creator revenue shares: tailered-ai:creator-share-floor;
- cutting the bill: tailered-ai:frugal-first.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: what each plan includes, today's price, cost per member, and any member words on what they value.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `value-price.md`: the value table, the floor, ceiling and proposed price, and the verdict.

## Steps

Lead the reply with the result: floor, ceiling and proposed price, each in dollars, using marked proposals where data is missing; then the verdict word and that the owner decides. Detail follows.

### 1. List what a member gets

For each thing a member gets, write its measured value and the source: minutes saved per slate, books and markets compared, the graded record and its sample size. No profit, return or win-rate promise.

Completion: a table of deliverable, value and source, with no profit claim.

### 2. Price the alternative

Write what a member would pay to get the same thing another way: other tools, or their own time at an hourly rate (a proposal unless known).

Completion: an alternative price in dollars, with a source or marked proposal.

### 3. Set the range

The floor is cost per member (from tailered-ai:price-forces-cost or the known bill). The ceiling is the alternative. Propose a price between them, with the reason.

Completion: floor, ceiling and proposed price in dollars.

### 4. Check the words and decide

Read the pricing words: every number has a source, nothing promises winnings, and the product is called estimates, never advice. Verdict: keep, change or stop. A price change is live: the owner decides, and it ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict word, the price, the owner named as decider, and the release route.

## Anti-Patterns

- Cost plus a margin with no look at value.
- A value claim with no source.
- Promising profit to justify the price.
- A name or tier that suggests more than it delivers.

## Source and adaptation

Source: original Tailered AI skill, which cites widely reported NVIDIA pricing and the October 2022 withdrawal of the RTX 4080 12GB. No third-party skill text is copied.
