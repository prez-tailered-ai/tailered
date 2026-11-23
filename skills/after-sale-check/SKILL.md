---
name: after-sale-check
description: "Check, signed in and read-only, that everything a paying member or subscriber bought still works after the sale: subscribed models delivering, records graded, access correct, each creator's listing kept up; every paid path gets a result, and each fail or unmeasured path gets a fix and an owner. Use when asked whether paying members are getting what they paid for, to check subscribers, supporters or the creator marketplace listings after a sale, or after a release that touches paid access. Not for the payment form itself or the shell after a release; use tailered-ai:tailered-labs-browser."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# After-sale check

The sale is the start of the job. Ford wrote that a maker is not through with a customer when the sale is complete. He required every agent to hold enough parts to keep each Ford running, and his sales chief added field agents to check dealers' service. This skill is that field agent. It reads pages and records, and it pays for nothing, changes nothing and contacts no member.

## When to Activate

- The owner asks whether paying members are getting what they paid for.
- A release touched sign-in, subscriptions, the creator marketplace or paid access.
- A creator's listing has subscribers.

Do not use for:
- the shell check after a release: tailered-ai:tailered-labs-browser;
- finding what a member complained about: read support@ directly, then come back with the path;
- changing a payment or refund: the owner's decision.

## Inputs and outputs

Where to work: `<skill>` below means this skill's own folder. Create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and run every command from it. Never write into the skill folder or into system temp, which can be cleared. Tables go in your reply.

Inputs: the paid paths to check. With none named, list them all from the live pages.

Output: `paths.json` and `result.json` in the task folder, and a table: each paid path, what was promised, what was seen, pass or fail, and the fix and owner for each fail.

## Steps

### 1. List what was sold

Read the signed-in pages with tailered-ai:tailered-labs-browser (owner profile, read-only). Start at the pricing page and the creator marketplace, then follow every other subscription or paid control you find. For each path, write what the page promises, in its own words. If no browser is available, list paths from the live release's saved source and records, say so, and leave those rows `unmeasured`; mark `not_on_sale` only when the source shows no control to buy it, and name that source as evidence.

Completion: every paid control found has a row with its promise, and the pages or files searched are named.

### 2. Check what it delivers

For each path, confirm the promise against the real result: a subscribed model has fresh projections, its Record and Graded counts move as games finish, and existing records show access opening and closing with the subscription. Read the existing records and pages only; stop before any pay button, Subscribe, Approve, Publish or Remove. The completed-payment state and receipts cannot be read this way, since receipts live with the payment provider and agents never read its key, so those rows stay `unmeasured` with the owner as owner, who can read the payment provider records or run an owner-only test purchase on the pricing page. Whether access truly closes at cancellation stays `unmeasured` unless the owner provides a test account. Keep other members' data out of the report.

A path the owner profile cannot reach stays `unmeasured`, which counts as a fail. A test account covers it only if the owner provides one.

Completion: every row has a result, with evidence (a screenshot or file path, and the time), or for `unmeasured`, what stopped the check.

### 3. Do the field-agent pass on each listing

For each creator listing with subscribers, check that projections are live, the record is current, and subscribers get their picks. Ford's field agents checked dealers' service, and this is the same job. If no creator has a published model yet, add one row with result `none_yet`.

Completion: each listing has its own row, or the report says none exists.

### 4. Name a fix for each fail

A fail or `unmeasured` row needs the ready fix and its owner: the step that restores service, or that makes the check possible. Ford's parts rule meant a breakdown never waited on the factory.

Completion: `python3 -I "<skill>/scripts/paid_paths.py" paths.json > result.json` exits 0.

Shape: `{"paths": [{"path": "/pricing", "promise": "...", "result": "pass", "evidence": "shot.png", "at": "2026-11-05T06:00:00Z", "fix": "", "owner": ""}]}`. Results: `pass`, `fail`, `unmeasured`, `not_on_sale`, `none_yet`. No paid path found is an error, because a check that saw nothing proves nothing. Exit 0 says the table is filled in, not that members are fine: read `failed` and `unmeasured`.

### 5. Report and stop

Lead with the counts of fails and of unmeasured paths, and the one that affects the most paying members; if you have no member counts, say so and lead with the one closest to money already taken. Fixes follow "Fix what you find" and production changes go through the release coordinator. A pass covers the time checked, and only the paths checked.

Completion: the owner has the table, and no payment, setting or message was made.

## Anti-Patterns

- Clicking pay or Subscribe to test; read only, and use the owner's own owner-only test when the owner runs it.
- Treating an unreachable path as passed.
- Reporting a fail with no fix or owner.
- Copying a member's data into the report.
- Writing findings onto a product page; they stay in the task record.

## Source and adaptation

Source: original Tailered AI skill, which cites My Life and Work (1922), chapters II and III. No third-party skill text is copied. Self-test: `python3 -I "<skill>/scripts/paid_paths.py" --selftest`.
