---
name: day-drive-map
description: "Use when adding a league, market type or prediction market to the main product; when main product prices or projections arrive late or stale for some leagues; when the owner asks how far a new market is from what we already run, or where a capture job or server should live. Not for building one general pipeline for every sport; use tailered-ai:pipe-before-demand. Not for trying a step on one league; use tailered-ai:one-league-trial."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Day drive map

Grow only within reach of a hub. Walton built a distribution center, then filled the ring of towns within about a day's drive of it with stores, then built the next center. At the company a hub is a host and capture job that feeds part of the main product; a surface is one league, market and venue on the main product. Every surface must sit within its refresh window of a hub. The guard: every store in a ring depended on one center, so each hub here is checked for how much goes dark if it stops.

## When to Activate

- A league, market type or prediction market is about to be added to the main product.
- Prices or projections arrive late or stale for some leagues.
- The owner asks how far a new market is from what we run, or where a job should live.

Do not use for:
- one general pipeline for every sport: tailered-ai:pipe-before-demand;
- trying a step on one league: tailered-ai:one-league-trial;
- choosing which skipped market to enter: tailered-ai:skipped-market-check.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the hosts and capture jobs in use, the main product surfaces, measured price ages if any, and the surface proposed.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `day-drive-map.md`: hubs, surfaces, measured age against window, hub load and the verdict.

## Steps

Lead the reply with the surface table and the verdict for the proposed surface, detail after.

### 1. Map hubs and surfaces

List each hub (host, capture job, data source) and each surface it serves.

Completion: a table of every surface with its hub.

### 2. Measure the drive

For each surface, record the age of a price or projection when a member sees it, against its window (proposal: 10 minutes for pregame prices; projections ready two hours before the first game).

Completion: each surface has a measured or proposed age, its window and inside or outside.

### 3. Check each hub

Count the surfaces on each hub and name what goes dark if it stops. Check whether the hub's host or feed is held on terms the other side can end with tailered-ai:lease-register.

Completion: per hub, the surface count, what goes dark and the lease check done.

### 4. Decide the new surface

Choose add (inside an existing hub's reach), wait (until a hub is closer or larger) or new hub (the owner decides, capped with tailered-ai:capped-experiment). Any live change ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict, the age or count that decided it, an owner and the route.

## Anti-Patterns

- Adding a market no hub can refresh in time.
- One hub carrying every league with no second path.
- Guessing price age instead of measuring it.
- Moving a job to a new host outside the release route.

## Source and adaptation

Source: original Tailered AI skill, which cites Walton and Huey, Sam Walton: Made in America (1992), on distribution centers and store rings. No third-party skill text is copied.
