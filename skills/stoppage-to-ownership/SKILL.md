---
name: stoppage-to-ownership
description: "List each time an outside supplier actually stopped the company (an odds feed freeze, a host outage, a provider failure), add up what it cost, and recommend own, backup or accept for only the step that stopped us, with, for own or backup, its downturn cost, an exit and outside advice. Use when asked whether to build or buy, whether to bring something in-house, what to do about a supplier that keeps failing, or after a supplier outage. Not for setting up a price capture; use tailered-ai:ai-model-capture-odds. Not for a live incident's fix; use tailered-ai:agent-introspection-debugging."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Stoppage to ownership

Own what actually stopped you, and only that. Supplier failures halted Ford's Highland Park plant during World War I, and integration was his answer. The same habit took him to a Brazilian rubber plantation run without a rubber expert, and it made his costs harder to cut in the Depression. So this skill starts from real stoppages and makes every ownership proposal show its downside. It recommends; the owner decides anything that spends money.

## When to Activate

- A supplier has stopped the main product, a capture, a model run or a page.
- The owner asks "should we build this ourselves?" or "what do we do about this provider?"

Do not use for:
- fixing the live failure now: tailered-ai:agent-introspection-debugging;
- building a capture once the decision is made: tailered-ai:ai-model-capture-odds;
- a provider's terms or a proposed deal: tailered-ai:growth-cap-check.

## Inputs and outputs

Where to work: `<skill>` below means this skill's own folder. Create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and run every command from it. Never write into the skill folder or into system temp, which can be cleared. Tables go in your reply.

Inputs: the supplier or period to review. With none named, cover the last 30 days.

Output: `stoppages.json` and `result.json` in the task folder, and a table: supplier, stoppages, hours lost, recommendation, cost, downturn cost, exit and advice source.

## Steps

### 1. Collect the real stoppages

Search for dated evidence: the service logs, build receipts, the shared queue records, release coordinator packets, saved notes under the project's `artifacts/` and the owner's alert messages. The incident log records rule events, and most of its lines are not supplier stoppages. Each stoppage needs a date, what stopped, hours lost and the evidence path; set `upper_bound` if the hours are a maximum. A stoppage whose supplier cause is unproven, or ruled out, goes under `suspected` with its date and `why_unproven`, and stays out of the totals, even if something really stopped.

Completion: every stoppage has a date, hours and an evidence path, and each source in `sources` starts `searched` or `unavailable`.

### 2. Decide per supplier

Choose one, for the smallest step that stopped us:
- `own`: build or capture that step ourselves;
- `backup`: keep the supplier and add a second source;
- `accept`: the loss costs less than either. Say what the other two would cost in `compared_with`, or that they are unpriced and why, in which case `accept` is provisional.

Ford wrote that he made some of every part so that a supplier's failure could not cripple him. That partial form is usually the place to start, so weigh `backup` first.

Completion: each supplier has one recommendation, its new monthly and one-time cost and `compared_with`.

### 3. Show the downside

For `own` and `backup`, write what the cost becomes in a downturn, how to exit, and whose advice was used. Advice means a published account by someone who has run that thing, or a person the owner names. Contacting anyone needs the owner's word, so note a needed conversation as an ask.

Completion: `python3 -I "<skill>/scripts/stoppage_table.py" stoppages.json > result.json` exits 0.

Shape: `{"sources": {"service_logs": "searched", "build_receipts": "searched", "queue_records": "searched", "release_packets": "searched", "alert_messages": "unavailable: no access"}, "stoppages": [{"supplier": "odds feed", "date": "2026-01-15", "hours": 3, "what": "...", "evidence": "path"}], "suspected": [{"supplier": "...", "date": "...", "why_unproven": "..."}], "decisions": [{"supplier": "odds feed", "choice": "backup", "new_monthly_cost": 40, "one_time_cost": 0, "compared_with": "...", "downturn_cost": "...", "exit": "...", "advice": "..."}]}`. COMPLETE means the review is filled in, not that the choice is right.

### 4. Report and stop

Lead with the supplier that cost the most hours. Give the owner the decision for each. Any build goes through tailered-ai:workflow, and any spend needs the owner's word.

Completion: the owner has the table, and no supplier, job or bill changed.

## Anti-Patterns

- Pricing every input; start from what actually stopped us.
- Owning a whole system when one step failed.
- Counting a suspected outage as a stoppage.
- A proposal with no exit or no outside advice, the steps Fordlandia skipped.
- Raising rights or licensing worries; this skill is about reliability and cost.

## Source and adaptation

Source: original Tailered AI skill. No third-party skill text is copied. Self-test: `python3 -I "<skill>/scripts/stoppage_table.py" --selftest`.
