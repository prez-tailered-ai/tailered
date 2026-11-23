---
name: swap-any-part
description: "Use when a job runs on a vendor-only service, managed product or premium plan; when choosing parts for the day build, odds capture or the publishing step; when the owner asks are we locked in or can we switch, or says commodity. Not for whether to spend at all; use tailered-ai:frugal-first. Not for what a vendor should charge; use tailered-ai:raw-cost-floor. Not for make or buy; use tailered-ai:insource-the-markup."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Swap any part

Build from standard parts more than one seller offers. Google's first servers were cheap boards on corkboard (1999), and its engineers argued in 2003 that many commodity PCs beat fewer high-end servers on price for performance (Barroso, Dean and Hölzle). The guard: those racks were hand-built and parts failed often. A part is cheap only when the hours to run it are counted, and only while another seller could replace it.

## When to Activate

- A job runs on a vendor-only service, managed product or premium plan.
- Choosing parts for a core job, or the owner asks "are we locked in".

Do not use for:
- whether to spend at all: tailered-ai:frugal-first;
- what a vendor should charge: tailered-ai:raw-cost-floor;
- make or buy: tailered-ai:insource-the-markup.

For what happens when one box dies, use the Page set's assume-the-box-dies, built at the same time.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the job, its parts, their sellers, costs and run hours.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `parts.md`: parts, sellers, full cost, switch hours and verdict.

## Steps

Lead the reply with the parts table, then the verdict line, then the detail.

### 1. List the parts

Every part: box, storage, database, job runner, data feed, model runtime, with seller and monthly cost.

Completion: a table of part, seller and cost, each real or marked `proposal`.

### 2. Price the hours

Add the staff or session hours each part takes per month, at a rate such as $60 an hour. The full cost is the bill plus the hours.

Completion: hours and full monthly cost per part.

### 3. Test the swap

Do two or more sellers offer it in a standard form, such as a Linux box, Postgres or files in a bucket? How many hours would a move take, and can the data leave in a standard format? Name a standard swap, with full cost, for each one-seller part.

Completion: standard or one-seller, the switch hours, and a named swap for each one-seller part.

### 4. Decide

Keep, change or stop each part. Change when a swap costs less in full, or when data cannot leave. Name the owner. Try any move on a scratch copy only; a live change ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: a verdict word per part, the owner and the release route.

## Anti-Patterns

- Calling a part cheap without counting the hours.
- A managed service whose data cannot leave.
- Premium hardware where two standard boxes do.
- Moving a live job to test a swap.

## Source and adaptation

Source: original Tailered AI skill, which cites Google's 1999 corkboard servers at the Computer History Museum and Barroso, Dean and Hölzle, "Web Search for a Planet" (IEEE Micro, 2003). No third-party skill text is copied.
