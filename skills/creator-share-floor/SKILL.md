---
name: creator-share-floor
description: "Work out what losing a model creator costs the company in subscribers and rework, the lowest revenue share that makes staying the creator's better deal, and the departure rate that would change the answer; for the owner to decide. Use when asked what to pay creators, what revenue share a named creator or other creators should get, how to keep creators on the creator marketplace, or what a creator leaving would cost. Not for member pricing; use tailered-ai:price-forces-cost."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Creator share floor

Pay to stop the churn, and count it as a cost cut. Ford's turnover reached 370 percent and he was hiring about 53,000 people a year to keep 14,000. After the $5 day he hired 6,508 in 1915 and called the wage one of his finest cost cuts. This skill runs that arithmetic for creators. It recommends; the owner decides the share, and nothing here contacts a creator or changes a payment.

## When to Activate

- The owner asks what share to offer, or what a creator's departure would cost.
- A creator marketplace or subscription plan needs a creator rate.

Do not use for:
- what members pay: tailered-ai:price-forces-cost;
- drafting or sending a message to a creator: that needs the owner's word, and this skill sends nothing.

## Inputs and outputs

Where to work: `<skill>` below means this skill's own folder. Create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and run every command from it. Never write into the skill folder or into system temp, which can be cleared. Tables go in your reply.

Inputs: subscribers and gross price per subscriber, running cost per subscriber, the current or proposed share, the creator's realistic best alternative per month, the share of subscribers lost if the creator leaves, the months that loss lasts, and the rework cost of a departure.

Output: `share.json` and `result.json` in the task folder, and one recommendation: the share floor, what it costs per month, what a departure costs, and the monthly departure chance at which paying it breaks even. If the verdict flips under step 3, give the range and one question in place of one figure.

## Steps

### 1. Fill the inputs, each with its source

Read real numbers from subscription records if you can find them; search the creator marketplace records and the shared queue records for up to a minute each, and say what you searched. Otherwise mark the value `"source": "assumption"` with `why`. A figure the owner gives as fact is `"source": "stated: the owner"`; one the owner says to assume is an assumption, with the owner's word as `why`. Check first whether creators have published models; early runs rest on assumptions, and the result must say so.

Shape: `{"subs": {"value": 100, "source": "assumption", "why": "..."}, "gross_per_sub": {...}, "cost_per_sub": {...}, "current_share": {...}, "alternative_monthly": {...}, "lost_sub_fraction": {...}, "loss_months": {...}, "rework_cost": {...}}`.

Completion: all eight fields have a value and a source.

### 2. Calculate

`python3 -I "<skill>/scripts/share_floor.py" share.json > result.json`

The floor is the share that matches the creator's alternative. `HOLD` means today's share already covers it. `NOT_VIABLE` means it exceeds what the subscription can pay after running costs. `RAISE_NEVER_PAYS` means the raise costs more each month than a whole departure would, so it cannot pay back on these numbers. A departure is valued at what the company keeps at today's share, and ignores any share saved on subscribers who stay.

Completion: the script exits 0 with one of `RAISE`, `HOLD`, `NOT_VIABLE` or `RAISE_NEVER_PAYS`, and every assumption is listed with why.

### 3. Test the assumptions

Pick the two inputs with the weakest sources, starting with `alternative_monthly`. Rerun each halved and doubled, with `--set field=value` on the same command. Report whether the verdict changes. A verdict that flips within that range is a question for the owner, not a recommendation.

Completion: the report shows the verdict under each changed input.

### 4. Keep terms on the work

Ford tied his bonus to home inspections, drinking and family conduct. Workers resented it, and the department that enforced it was largely dissolved by 1921. Any condition in the recommendation must concern the model and its results: publishing, grading and support. Remove any condition on a creator's private life or outside work unless it directly concerns the company's models.

Completion: every proposed condition names the work it concerns.

### 5. Report and stop

Lead with the floor and what it costs. For `RAISE`, give `break_even_monthly_departure` in plain words: the raise can only pay for itself if the creator is at least this likely to leave in a month without it. That is the best case, since it assumes the raise removes all risk of leaving, and a floor only matches the alternative. For other verdicts, say which number would change the verdict. The owner decides.

Completion: the owner has one share figure or a range with one question, the assumptions behind it, and the number that would change it, and nothing was sent or changed.

## Anti-Patterns

- Quoting a market rate as if it were this creator's alternative.
- Presenting assumption-based figures as measured.
- Counting a departure's cost as one month's revenue; the subscribers stay lost for `loss_months`.
- Adding conduct conditions to pay; terms cover the work only.

## Source and adaptation

