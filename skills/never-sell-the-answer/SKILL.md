---
name: never-sell-the-answer
description: "Use when a sportsbook, prediction market, affiliate or partner offers to pay for a spot on the main product, a card, an alert or a member note; when a paid link, promo code or sponsored book row goes near the model's numbers; when the owner says sponsored, paid placement or affiliate; or when anyone asks to move a projection or the price order for money. Not for choosing which paid offer gets the spot; use tailered-ai:useful-times-bid."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Never sell the answer

The core result is never for sale. Brin and Page's 1998 search paper warned that an ad-funded engine bends toward its advertisers, and Google's 2004 IPO letter promised no payment for ranking and labeled ads. The guard is Google's own lapse: the EU fined it 2.42 billion euros in 2017 for placing its own shopping service above rivals. The owner's rule: a paid book spot stays labeled and apart from the core result.

## When to Activate

- Someone offers to pay for a spot, link, promo code or book row near the model's numbers.
- The owner says "sponsored", "paid placement", "affiliate" or "ad".
- Anyone asks to change a projection, an edge or the price order for money.

Do not use for:
- choosing which paid offer gets the spot: tailered-ai:useful-times-bid;
- a partner's demand that crosses a written principle: tailered-ai:name-the-red-line.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the screen or note, its paid items, the payers and amounts.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `paid-spots.md`: the paid items, their checks, the verdict and the owner.

## Steps

Lead the reply with the check table, then the verdict line, then the detail.

### 1. List every paid item

Name each thing that earns the company money: a sponsored book row, an affiliate link, a promo code, a partner tile. Give the payer and the amount per month.

Completion: a table with item, payer and amount, each real or marked `proposal`.

### 2. Run the three checks

Labeled: a visible "Paid" tag naming the payer. Apart: its own box or row, never inside the projection line, the edge or the best-price column. Clean: no effect on any model number or on the price order, which ranks on fee-adjusted price only.

Completion: pass or fail on all three for every item.

### 3. Give the verdict

Keep when all three pass. Change, with the exact fix, when a label or spacing fails. Stop when money would touch a projection, an edge or the price order, at any amount. The owner owns the deal; name the session that owns the screen.

Completion: keep, change or stop per item, with the owner named.

### 4. Name the route

Draft replies for the owner; send nothing. A live change ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the release route is named and nothing was sent.

## Anti-Patterns

- A tag so faint that members miss it.
- A sponsor's book sorted first in the best-price column.
- "Featured" or "Partner" used in place of "Paid".
- A small model tweak for a big check.

## Source and adaptation

Source: original Tailered AI skill, which cites Brin and Page's 1998 paper, Google's 2004 IPO letter, the EU's 2017 Google Shopping decision. No third-party skill text is copied.
