---
name: raw-cost-floor
description: "Use when a vendor quote, data feed, API, hosting bill, model run or main product feature is priced at what the market charges; when the owner says first principles about a price or cost, asks what it should really cost or what the raw inputs are; or before accepting a price because everyone pays it. Not for splitting a target price the owner named across steps; use tailered-ai:price-forces-cost."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Raw cost floor

Price a thing by its raw inputs, not by what the market charges. In a 2012 interview Musk said a rocket's raw materials came to about 2% of its usual price, and SpaceX was built in that gap. The guard: the floor is not the cost. Falcon 1 failed three times before it reached orbit, and a floor leaves out what that learning costs.

## When to Activate

- A vendor quote, data feed, API, hosting or model-run bill is taken at the going rate.
- The owner says "first principles" about a price or cost, "what should this really cost" or "what are the raw inputs".
- A main product feature or day-build step is costed by comparing it with what others charge.

Do not use for:
- splitting a target price the owner named across the job's steps: tailered-ai:price-forces-cost;
- deciding whether to build the piece in-house: tailered-ai:insource-the-markup;
- reviewing a new subscription or tool before buying it: tailered-ai:frugal-first.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the thing being priced, its current price or quote, and its usage (calls, rows, GPU hours, storage, people hours).

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `floor.md`: the raw input table with unit prices and their sources, the floor, the markup ratio, the learning allowance, and the verdict with its owner.

## Steps

### 1. List the raw inputs

Break the item into what it is made of: compute hours, storage, API calls, data rows, people hours. Give each a unit, a quantity and a unit price with its source, such as a cloud provider price list or a provider's published rate. Where usage is unknown, propose a quantity from the day build's last run and mark it `proposal`.

Completion: every input has a unit, a quantity, a unit price and a source.

### 2. Compute the floor and the ratio

Add the inputs to get the floor, per month or per run. Divide the current price by the floor. A ratio near 1 means the price is fair. A ratio of 3 or more means most of the price is markup.

Completion: the floor in dollars and the ratio, both written.

### 3. Add the learning allowance

The floor leaves out failure. Add the hours it would take the company to reach the floor: building it, failed runs, on-call and upkeep. Price those hours at a stated rate. Compare the price with the floor plus the allowance, never the floor alone.

Completion: floor plus allowance in dollars, with the hours shown.

### 4. Give the verdict and the owner

Pick one word: keep (the price is close to floor plus allowance), negotiate (take the ratio to the vendor) or rebuild (send it to tailered-ai:insource-the-markup). Name who acts and by what date. Nothing is cancelled, bought or switched here. Any live change goes through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: keep, negotiate or rebuild, a named owner and a date.

## Anti-Patterns

- Accepting a price because competitors pay it.
- Calling the floor the cost and leaving out failure and upkeep.
- Unit prices with no source.
- Switching a vendor from this sheet without the owner.

## Source and adaptation

Source: original Tailered AI skill, which cites Musk's 2012 Wired interview and SpaceX's Falcon 1 launch record. No third-party skill text is copied.
