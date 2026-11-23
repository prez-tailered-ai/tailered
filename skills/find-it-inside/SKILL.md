---
name: find-it-inside
description: "Before a new spend or a fundraising ask, list money locked inside the company: idle jobs, duplicate storage, unused subscriptions, money tied up by slow jobs and data members might pay for, each with dollars, a check and how to undo it. Use when asked where we can find money, how to cut the bill, how much runway we can free up, what we could sell, or before asking for funding or a bigger budget. Not for hitting a target on one job; use tailered-ai:price-forces-cost. Not for one capture job's cost; use tailered-ai:ai-model-capture-health."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Find it inside

Look inside before asking outside. By Ford's account, facing debts in 1921, he went from $20 million to $87.3 million in about three months: selling stock on hand, speeding up transit and selling by-products, and he said it showed a business can find resources within itself. This skill does that search. It lists and recommends. It retires, sells and cancels nothing.

## When to Activate

- A new paid tool, bigger budget or funding ask is on the table.
- The owner asks where the money is going or how to free some up.

Do not use for:
- fitting one job under a named number: tailered-ai:price-forces-cost;
- one capture job's cost: tailered-ai:ai-model-capture-health;
- cleaning a full disk: handle that directly.

## Inputs and outputs

Where to work: `<skill>` below means this skill's own folder. Create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and run every command from it. Never write into the skill folder or into system temp, which can be cleared. Tables go in your reply.

Inputs: the ask this is meant to offset, if any, and its amount. With none, report the total found.

Output: `release.json` and `result.json` in the task folder, and a table: source, kind, dollars per month or one-time, the check behind it, how to undo it and the action the owner would approve.

## Steps

### 1. Search every kind

Check each kind and record what you found, including nothing:
- `idle`: scheduled jobs, schedulers, servers and volumes with no use in 30 days by their own logs;
- `duplicate`: the same data in two places, old release folders on hosts;
- `subscription`: paid tools and seats nobody used in 30 days, from bills the owner shares (never open a secret or a key);
- `speed`: money tied up by slowness, such as compute held by a job that waits;
- `byproduct`: what we already hold that members might pay for, such as minute price history in Cloud Storage.

Start from the project's `artifacts/` notes and any billing export the owner shared. Use read-only commands only; anything beyond that needs the owner. Mark a finding `proven` if the evidence shows it, or `lead` if it needs a closer look.

Completion: `searched` has all five kinds, each starting `found`, `none found` or `unavailable`, with the reason.

### 2. Price each finding from a real number

A bill or meter is `basis: measured`. A saved note or a short reading is `basis: estimate`, and the totals keep the two apart. For a range, use the low end and put the range in `check`. With no number at all, set `dollars` to `null`, since an unpriced finding belongs on the list but not in a total. A by-product's revenue is a proposal: price it as `null` until there is a real offer or test.

Completion: every row has dollars with its basis and check, or `null`.

### 3. Write the undo

The owner's never-delete rule applies: copy to cold storage before anything live is retired, and give the storage URL of the copy in `copied_to` on any row with `retires: true`. Every row says how to bring it back, or "nothing changes" for a row that only asks for a bill or a check. A row with no undo is flagged one-way, and it needs its own owner yes and a day's wait under the workspace rule in the shared workspace rules when it deletes live work.

Completion: `python3 -I "<skill>/scripts/release_table.py" release.json > result.json` exits 0.

Shape: `{"ask": 500, "searched": {"idle": "found", "duplicate": "none found", "subscription": "unavailable: no bills shared", "speed": "none found", "byproduct": "found"}, "rows": [{"source": "old-job", "kind": "idle", "status": "proven", "dollars": 12, "basis": "measured", "period": "month", "check": "billing export", "undo": "re-enable scheduler", "action": "pause trigger"}]}`.

### 4. Report and stop

Lead with the measured monthly total, and whether it covers the ask. Keep measured and estimated, monthly and one-time, and priced and unpriced apart. List the five `searched` marks.

Completion: the owner has the table and has decided nothing yet; no job, file or subscription changed.

## Anti-Patterns

- Counting a guess in the total.
- Retiring something while auditing.
- Adding one-time and monthly money together.
- Cutting what members rely on and calling it waste; say what would break.
- Treating by-products as revenue before anyone has offered to pay.

## Source and adaptation

Source: original Tailered AI skill, which cites My Life and Work (1922), chapter XII. No third-party skill text is copied. Self-test: `python3 -I "<skill>/scripts/release_table.py" --selftest`.
