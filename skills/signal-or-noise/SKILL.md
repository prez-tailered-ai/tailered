---
name: signal-or-noise
description: "Use when a hit rate, edge, record, backtest or member number looks good or bad and someone wants to act on it; before a model result is believed, posted or used to change the model; when the owner asks is this real, is it luck, or how many games do we need. Not for explaining how the model works; use tailered-ai:know-the-numbers. Not for green dashboards that may be proxies; use tailered-ai:day-one-check."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Signal or noise

Brin's Stanford work was data mining, finding which patterns in large data are real and which are chance (Brin, Motwani and Silverstein, 1997). The guard is Google Flu Trends, which overshot real flu levels badly in 2012-13 (Lazer and others, Science, 2014): a pattern that fit the data but was never checked against the outcome.

## When to Activate

- A hit rate, edge, record or backtest looks good or bad and someone wants to act.
- Before a model result is believed, posted or used to change the model.
- The owner asks "is this real", "is it luck" or "how many games do we need".

Do not use for:
- explaining how the model works: tailered-ai:know-the-numbers;
- whether green dashboards are proxies: tailered-ai:day-one-check;
- designing a public test: tailered-ai:prove-it-in-public.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the claim, its sample, the prices and how the window was chosen.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `signal-check.md`: the claim, the baseline, the interval, the trap checks and the verdict.

## Steps

Lead the reply with the check table (claim, sample, baseline, interval), then the verdict line, then the detail.

### 1. Write the claim exactly

State the number, the sample and the window: "projected NHL totals beat the market side 58% of 120 games, 1 Oct to 4 Nov".

Completion: one sentence with number, sample size and dates.

### 2. Set the baseline and the interval

Name what it must beat: break-even at the price (52.4% at -110; the fee-adjusted price on Partner A or Partner B), or the closing line. Give a 95% interval: about plus or minus 2 times the square root of p(1-p)/n. Say how many games would put the low end above the baseline.

Completion: baseline, interval and games needed, as numbers.

### 3. Check the traps

Yes or no: was the window picked after looking? Were many leagues or versions tried and one shown? Did any input leak from after game start, such as closing lines? Was it checked against real results?

Completion: four yes or no answers.

### 4. Give the verdict

Signal, noise or not yet, with the games needed for not yet. Name the owner who rechecks it and when. Draft any post for the owner and post nothing; a model change ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict word, the owner, the recheck date and nothing posted.

## Anti-Patterns

- Calling 60% over 40 games an edge.
- Showing the best league of five.
- Comparing to 50% when the price needs 52.4%.
- Trusting a fit never checked against outcomes.

## Source and adaptation

Source: original Tailered AI skill, which cites Brin, Motwani and Silverstein (SIGMOD 1997) and Lazer and others on Google Flu Trends (Science, 2014). No third-party skill text is copied.
