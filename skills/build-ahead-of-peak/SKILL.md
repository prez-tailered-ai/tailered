---
name: build-ahead-of-peak
description: "Use when a busy stretch is coming, such as NFL Sundays, March Madness, opening night or a new league; when the owner asks will it hold up, do we have enough servers, how much capacity, or should we build our own infrastructure; or when the day build, odds capture or main product slowed down under load. Not for a supplier that stopped us; use tailered-ai:stoppage-to-ownership. Not for cutting a bill; use tailered-ai:frugal-first. Not for merging league pipelines; use tailered-ai:one-chassis-audit."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Build ahead of peak

Build the base layer before the busiest day needs it, and only as much as that day needs. Facebook built its own data center in Prineville, Oregon and shared its hardware designs through the Open Compute Project in 2011, then open-sourced React in 2013. The guard: spending ahead of demand can run far past it. Reality Labs lost about $13.7 billion in 2022, and 2023 brought the "year of efficiency" and about 21,000 layoffs. So capacity is sized to the next real peak, with a cap.

## When to Activate

- A busy stretch is coming: NFL Sundays, March Madness, opening night, a new league.
- The owner asks "will it hold up", "do we have enough servers" or "should we build our own".
- The day build, odds capture or main product slowed under load.

Do not use for:
- a supplier that stopped us: tailered-ai:stoppage-to-ownership;
- cutting a bill or a new subscription: tailered-ai:frugal-first;
- merging per-league pipelines: tailered-ai:one-chassis-audit.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the coming peak and its date, today's run times and load for each layer, and this month's hosting bill.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `peak-plan.md`: the peak in numbers, the headroom table, the choice per layer with its monthly cost, and the verdict.

## Steps

### 1. Put the peak in numbers

Name the busiest day ahead and count it: games, markets per game, price captures per minute, main product visits per hour. Set it beside a normal day.

Completion: the peak date and four counts beside today's.

### 2. Find the headroom

For each layer (day build, odds capture, storage, model run, main product serving), give today's load, its limit and its load at the peak. Mark any layer above 70% of its limit at peak. Hosting is the current host or the cloud provider only.

Completion: a table of five layers with load, limit and peak load, and the layers above 70% marked.

### 3. Choose per layer

For each marked layer pick rent more (a bigger the current host or the cloud provider machine), build (the company's own job or tool), or wait. Size to the peak times 1.5, not to a dream. Give the monthly cost. Note any tool that is not the company's edge and could be shared openly later; sharing it is the owner's call.

Completion: a choice and a monthly dollar figure for each marked layer.

### 4. Cap and route

Set the total monthly cap and the date to scale back after the peak. Give one verdict: build, rent or wait, with the number that decided it. Name the owner. The owner approves the spend; every change ships through tailered-ai:workflow and the release coordinator on the owner's word. This skill buys and deploys nothing.

Completion: the cap, the scale-back date, the verdict, the owner and the release route named.

## Anti-Patterns

- Building for ten times the peak because it might come.
- Waiting until the peak day to find the limit.
- Keeping peak servers after the peak.
- Moving hosting to another provider.

## Source and adaptation

Source: original Tailered AI skill, which cites Facebook's Prineville data center and the Open Compute Project (2011), React (2013), and Meta's reported 2022 Reality Labs loss and 2023 layoffs. No third-party skill text is copied.
