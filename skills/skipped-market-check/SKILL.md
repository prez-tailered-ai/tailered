---
name: skipped-market-check
description: "Use when choosing which league, conference, market type or prediction-market venue to cover next; when the owner asks where the big sites are not looking, what nobody covers well, or about small conferences or thin markets; or before a niche market is added. Not for capping the trial's loss; use tailered-ai:capped-experiment. Not for whether a market's prices can reach the main product in time; use tailered-ai:day-drive-map."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Skipped market check

Go where the big chains are not. Walton opened stores in towns of a few thousand people that Kmart and others passed over, and won them before anyone noticed. At the company the small towns are leagues, conferences, market types and venues the big betting sites cover thinly. Two guards. A market can be small for a reason: too few games, too thin to trade, no close to grade against. And Walmart's arrival was reported (Iowa State studies, 1990s) to hurt small-town shops; in a thin prediction market, a published projection can move the price members are trying to get.

## When to Activate

- Choosing the next league, conference, market type or venue to cover.
- The owner asks where the big sites are not looking or what nobody covers well.
- Before a niche market is added to the main product.

Do not use for:
- capping the trial's loss: tailered-ai:capped-experiment;
- whether its prices can reach the main product in time: tailered-ai:day-drive-map;
- reading what rivals launched this week: tailered-ai:weekly-rival-read.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the candidate markets, what rivals cover, member asks, and what the pipeline and model already handle.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `skipped-markets.md`: candidates, size, cost to serve and the verdict per candidate.

## Steps

Lead the reply with the candidate table and the one go, or none, then detail.

### 1. List the skipped markets

Name three to six candidates (proposal: mid-major NCAAM conferences, Group of Five NCAAF, NHL totals on prediction markets). For each, say who covers it now and how well.

Completion: each candidate has who covers it, from a public page or a rival read.

### 2. Size the town

For each, record games per season, prices offered and volume where shown, and member asks. Answer small for a reason: too few games, too thin to trade, or no closing line to grade.

Completion: each row has games, a liquidity figure, member asks and a yes or no on small for a reason.

### 3. Price the trip

Estimate the days to add it and the monthly cost, reusing the current pipeline and model where they fit. Note whether our published number could move a thin market.

Completion: days, monthly dollars and a thin-market note per candidate.

### 4. Pick one or none

Mark each go, wait or skip; at most one go. A go gets a cap from tailered-ai:capped-experiment and an owner. Live changes ship through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: verdicts on every row, one go or none, its owner, and the route.

## Anti-Patterns

- Calling a market skipped without checking who covers it.
- Entering a market too thin to grade against a close.
- Adding three niches at once.
- Ignoring that our number can move a thin price.

## Source and adaptation

Source: original Tailered AI skill, which cites Walton and Huey, Sam Walton: Made in America (1992), and reported Iowa State studies by Kenneth Stone. No third-party skill text is copied.
