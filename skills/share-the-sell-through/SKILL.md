---
name: share-the-sell-through
description: "Use when a model creator, data feed or other supplier would serve the company better if it saw how its product does here; when the owner says share the data with them or help them restock, or asks what to tell a creator or feed about their numbers; or before any usage data leaves the company. Not for deepening a supplier at renewal; use tailered-ai:partner-for-decades. Not for a supplier that stopped us; use tailered-ai:stoppage-to-ownership."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Share the sell-through

Show suppliers how their goods sell so they can restock for you. Walmart's reported partnership with Procter and Gamble from 1987, and its Retail Link system about 1991, gave suppliers store sales data so they could refill shelves themselves. At the company the suppliers are model creators and data feeds. A creator who sees which leagues members read can improve; a feed that sees the gaps we measured can fix them. The guard: Walmart's data was reported (Fast Company, 2003) as leverage to press suppliers on price. Here data goes out to help, never to squeeze, and never carries member personal data.

## When to Activate

- A creator or feed would do better if it saw its numbers at the company.
- The owner says "share the data with them" or "help them restock".
- Before any usage data leaves the company.

Do not use for:
- deepening a supplier at renewal: tailered-ai:partner-for-decades;
- a supplier that stopped us: tailered-ai:stoppage-to-ownership;
- a creator's revenue share: tailered-ai:creator-share-floor.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the supplier, the numbers we hold about its product, and any past report.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `sell-through-<supplier>.md`: the numbers, the privacy check, the one-page report draft and the cadence.

## Steps

Lead the reply with the numbers table for the supplier, then the verdict line (share, change or hold), detail after.

### 1. Pick what they can act on

Name the supplier and three to five numbers it could act on. A creator: subscribers, month-on-month retention, leagues read, graded record. A feed: gaps and stale minutes we measured, by league.

Completion: supplier named and each number given with its source.

### 2. Strip it to aggregates

No member names, emails, IDs or stake sizes, and nothing about another supplier. No figure from fewer than 10 members (proposal).

Completion: each number marked aggregate, and the minimum group size stated.

### 3. Draft the report and one ask

One page: the numbers, one ask (fix this gap, add this market) and what the company will do in return. Tie no price demand to the data.

Completion: a draft with one ask and no price demand in it.

### 4. Hand it to the owner

The owner approves and sends. Set the cadence (proposal: monthly) and an owner who prepares it. This skill sends nothing.

Completion: the draft saved, the owner named as sender, cadence and owner set, verdict share, change or hold.

## Anti-Patterns

- Sending member-level data.
- Using the numbers to push a supplier's price down.
- One supplier seeing another's numbers.
- A report with numbers and no ask.

## Source and adaptation

