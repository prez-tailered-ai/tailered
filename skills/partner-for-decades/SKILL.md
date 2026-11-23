---
name: partner-for-decades
description: "Use when a supplier the company cannot easily replace (an odds feed, a prediction-market data source, cloud hosting, a model provider) is up for renewal or yearly review; when the owner asks how to deepen a partnership, whether to stay with a supplier for the long term, or what we depend on one supplier for. Not for a supplier that already stopped us; use tailered-ai:stoppage-to-ownership. Not for reading a deal's terms for caps; use tailered-ai:growth-cap-check."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Partner for decades

Keep the suppliers that matter for the long run, and give them reasons to keep you. TSMC has made NVIDIA's chips since the late 1990s, and Huang and TSMC founder Morris Chang built a partnership that has lasted decades. The guard: one partner is one point of failure. In 2023 and 2024 limits on TSMC's advanced packaging capacity reportedly held back NVIDIA's supply. A long partnership needs a named fallback.

## When to Activate

- A key supplier is up for renewal or its yearly review.
- The owner asks how to deepen a partnership, or whether to stay with a supplier long term.
- The owner asks what we depend on one supplier for.

Do not use for:
- a supplier that already stopped us: tailered-ai:stoppage-to-ownership;
- reading a deal's terms for caps: tailered-ai:growth-cap-check;
- a new tool or subscription: tailered-ai:frugal-first.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the key suppliers, what each provides, monthly spend, how long we have used them, and any record of outages.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `partners.md`: one row per supplier with what we depend on, both sides' gains, the fallback, the 12-month plan and the verdict.

## Steps

### 1. List what we depend on

For each key supplier, write what it gives us, monthly spend, how long we have used it, and who owns the relationship.

Completion: a table with a named owner on every row.

### 2. Score both sides

Write what we give the supplier (steady volume, feedback, a reference) and what it gives us. Propose one shared plan for the next 12 months, such as a data field we need or a price for a longer term.

Completion: a two-sided list and a 12-month plan for each supplier.

### 3. Name the fallback

For each supplier, name the second source and the days it would take to switch. Mark each tested or untested.

Completion: a fallback and a number of days per supplier, each marked tested or untested.

### 4. Decide

Verdict per supplier: deepen, keep or loosen. Anything that signs, spends or sends a message goes to the owner; nothing is sent from here. A change to hosting or a live feed ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: a verdict word per supplier, the owner named for any spend or message, and the release route.

## Anti-Patterns

- Treating a key supplier only as a cost to cut.
- A long partner with no fallback.
- A fallback nobody has tested, written as if it were tested.
- Signing a longer term without the owner.

## Source and adaptation

Source: original Tailered AI skill, which cites NVIDIA's partnership with TSMC since the late 1990s and reported TSMC packaging limits in 2023 and 2024. No third-party skill text is copied.
