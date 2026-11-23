---
name: assume-the-box-dies
description: "Use when the day build, odds capture or main product runs on one machine, disk or process; when a server or disk failed or nearly failed; when cheaper machines are proposed; or when the owner asks what if the box dies, or says failover or redundancy. Not for what hosting should cost; use tailered-ai:raw-cost-floor. Not for tracing a wrong number through layers; use tailered-ai:full-stack-trace."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Assume the box dies

Google ran on commodity machines in its own data centers, and its software expected failure: the Google File System paper (2003) treats a dying disk or machine as the normal case and keeps copies so work goes on. Cheap hardware saves money only when the software survives the failure. The guard: a cheap box with no copy turns one failure into a main product outage. The company hosting is the current host or the cloud provider.

## When to Activate

- The day build, odds capture or main product depends on one machine, disk or process.
- A server or disk failed or nearly failed, or cheaper machines are proposed.
- The owner asks what if the box dies, or says failover or redundancy.

Do not use for:
- what hosting should cost: tailered-ai:raw-cost-floor;
- cutting a new spend: tailered-ai:frugal-first;
- tracing a wrong main product number: tailered-ai:full-stack-trace.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: where the job runs (machines, disks, databases, schedules, DNS), backups and recent failures.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `failure-map.md`: each part, its copies, impact, recovery minutes, cover, cost, owner and verdict.

## Steps

Lead the reply with the failure-map table, then the verdict line, detail after.

### 1. Map the single points

List every part the main product and day build need, and how many working copies each has. Two copies on the same disk, account or region count as one.

Completion: a parts table with copy counts.

### 2. Kill each one on paper

For each single-copy part, write what members see if it dies at 6 pm on a game day, and minutes to recover. Losing the main product over 30 minutes (proposal) fails.

Completion: impact, recovery minutes and pass or fail per part.

### 3. Choose the cheapest cover

For each failing part choose a copy, retry, automatic restart, second region or re-run from captured data; prefer software cover to costlier hardware. Write the monthly cost and a named owner. A backup counts only after a restore test, run in a copied folder, never on production.

Completion: cover, monthly cost and owner per failing part, and a restore test planned in a copy.

### 4. Verdict and route

Write keep (covered), change (add the cover) or stop (drop the part) per part. Any change to live machines, schedules or the day build ships through tailered-ai:workflow and the release coordinator on the owner's word. This skill does not reboot, fail over, move or delete anything.

Completion: a verdict word per part and the release route named.

## Anti-Patterns

- Paying for premium hardware instead of a copy.
- "We have backups" with no restore test.
- Testing failure on production.
- Counting a copy that shares a disk, account or region.

## Source and adaptation

Source: original Tailered AI skill, which cites the Google File System paper (2003) and Barroso and Holzle (2009). No third-party skill text is copied.
