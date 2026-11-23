---
name: license-dont-sell
description: "Use when a sportsbook, prediction market, media site or app wants the company's projections, a model, odds data or the odds readers; when the owner says license it, rent it out or own what you rent out; or when a draft deal would sell, assign or make exclusive anything the company built. Not for an outsider building on the company's data; use tailered-ai:open-platform-gate. Not for a deal's caps; use tailered-ai:growth-cap-check."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# License, don't sell

In 1980 Microsoft licensed DOS to IBM but kept the right to license it to other PC makers, so the same work sold many times. The owner's practice: own the models, the data and the odds readers, and rent them out in many places. The guard: per-processor licenses charged makers even for PCs without DOS, until a 1994 consent decree ended them. No license may keep a buyer from rivals.

## When to Activate

- A buyer asks for the company's projections, a model, odds data or the odds readers.
- The owner says "license it", "rent it out" or "own what you rent out".
- A draft deal sells, assigns or makes exclusive the company's work.

Do not use for:
- whether an outside party may build on the company's data: tailered-ai:open-platform-gate;
- reading a deal's caps: tailered-ai:growth-cap-check;
- bringing an outside tool in: tailered-ai:license-not-rebuild.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the buyer, what they want, and any draft terms.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `license-plan.md`: assets and owners, terms and fee, next buyers, verdict.

## Steps

Your reply leads with the asset table (asset, owner, rights kept, rights licensed), then the verdict line: license, change or stop.

### 1. List what the company owns

Name each asset touched: model code, projections, captured odds data, odds readers. Note any outside data in them whose terms forbid resale.

Completion: a row per asset with its owner, and each outside-data limit.

### 2. Rent, never sell

Keep ownership: non-exclusive, 12 months (proposal) with renewal, no transfer of code or raw captures, and the company keeps every improvement. Fee in dollars per month or per use. Mark any sale, assignment or exclusive clause stop.

Completion: terms with a dollar fee, and every sale, assignment or exclusive clause marked.

### 3. Name the next buyers

Name at least two more likely buyers for the same work. If none, call it a one-off and price it so.

Completion: two named buyers, or a one-off price.

### 4. Check the rival guard

Strike any term that charges or bars a buyer for using rivals, or ties products together to block a competitor.

Completion: each struck term listed, or "none found".

### 5. Verdict and route

Verdict: license, change or stop, and who negotiates. The owner signs; nothing is signed or sent here. Live access goes through tailered-ai:open-platform-gate, then tailered-ai:workflow and the release coordinator on the owner's word.

Completion: verdict, owner and route.

## Anti-Patterns

- Selling the model for one large cheque.
- Exclusivity to land the first buyer.
- Reselling outside data without the right.
- Terms that punish a buyer for using rivals.

## Source and adaptation

Source: original Tailered AI skill, which cites Manes and Andrews, Gates (1993), the 1994 US Justice Department consent decree with Microsoft. No third-party skill text is copied.
