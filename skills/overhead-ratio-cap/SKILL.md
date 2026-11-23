---
name: overhead-ratio-cap
description: "Use when behind-the-scenes costs grow, such as dev tools, agent tokens, dashboards, test environments, travel or admin; when the owner asks what overhead costs as a share of spend or revenue, says keep the offices plain, or asks why the back office costs more than the product; or once a quarter. Not for approving one new spend; use tailered-ai:frugal-first. Not for finding idle jobs or money before a raise; use tailered-ai:find-it-inside."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Overhead ratio cap

Keep the back office plain so the money goes where members see it. Walton kept Bentonville's offices bare, shared hotel rooms on buying trips and drove an old pickup truck. At the company that is a cap on overhead: what the company spends on itself as a share of all spend. The guard: Walmart's thrift was reported as reaching associate pay. Here the cap never touches the pay of people doing the work, their gain share, or member-facing accuracy and freshness.

## When to Activate

- Behind-the-scenes costs grow: dev tools, agent tokens, dashboards, test environments, travel, admin.
- The owner asks what overhead costs as a share, or says "keep the offices plain".
- Once a quarter.

Do not use for:
- approving one new spend: tailered-ai:frugal-first;
- finding idle jobs or money before a raise: tailered-ai:find-it-inside;
- what a cost should really be: tailered-ai:raw-cost-floor.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: last month's bills by line, revenue if any, and the owner's cap if set.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `overhead.md`: the split, the ratio against the cap, and keep, change or stop per overhead line.

## Steps

Lead the reply with the ratio against the cap, then the verdict line, then the line table.

### 1. Split the bill

Sort every monthly cost into member-facing (odds and market feeds, main product hosting, model runs that publish) or overhead (internal tools, agent sessions, dashboards, test environments, travel, admin).

Completion: two dollar totals, with a source for each line.

### 2. Compute the ratio

Divide overhead by all spend. The owner sets the cap (proposal: 30%).

Completion: the ratio and the cap, each as a percentage.

### 3. Cut overhead, never pay or accuracy

If the ratio is over the cap, give each overhead line its plainer version and the monthly saving. Pay, gain shares, safety and member-facing accuracy and freshness are off the list.

Completion: every overhead line marked keep, change or stop, with dollars saved, and none of the protected lines touched.

### 4. Hand it to the owners

The owner approves the list. Each change has a named owner who makes it; this skill cancels nothing. A change to anything live ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: total monthly saving, the new ratio and an owner per change.

## Anti-Patterns

- Cutting pay or a gain share to meet the cap.
- Cutting price freshness and calling it overhead.
- Counting a tool as member-facing because a member might see it someday.
- Cancelling a plan before its owner agrees.

## Source and adaptation

Source: original Tailered AI skill, which cites Walton and Huey, Sam Walton: Made in America (1992), and widely reported accounts of associate pay. No third-party skill text is copied.
