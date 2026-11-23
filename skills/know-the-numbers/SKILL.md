---
name: know-the-numbers
description: "Use when the owner or an owner must explain how the model, the day build or a pipeline works; before an investor, partner or member call; when a decision turns on a technical figure nobody has checked; or when the owner says I should know this, chief engineer, or drill me. Not for naming who owns an initiative; use tailered-ai:single-threaded-owner. Not for whether green metrics are real; use tailered-ai:day-one-check."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Know the numbers

Musk is SpaceX's chief engineer, and his biographers describe him knowing parts, costs and limits in detail. The guard: Tesla dropped radar in 2021 over some engineers' concerns, as the New York Times reported. Holding the detail is not the same as overruling the people with the data. The aim: the owner and each owner can state the load-bearing numbers and say where each comes from.

## When to Activate

- The owner or an owner must explain how the model, the day build or a pipeline works.
- An investor, partner or member call is coming.
- A decision turns on a technical figure nobody has checked.
- The owner says "I should know this", "chief engineer" or "drill me".

Do not use for:
- naming who owns an initiative: tailered-ai:single-threaded-owner;
- whether green metrics hide a real problem: tailered-ai:day-one-check.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the system (model, day build, main product or price capture), who is drilled, and the decision or meeting ahead.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `numbers.md`: ten load-bearing numbers, each with its source, owner, the answer given, and match or miss, plus the verdict.

## Steps

### 1. Pick the ten numbers

Choose the figures a decision would turn on. For the model: accuracy against the closing line per league, sample size, last retrain date. For the day build: run time, failure rate, cost per run. For the main product: games covered, and the sportsbook and prediction-market prices shown, such as two partner markets.

Completion: ten numbers, each tied to a decision.

### 2. Find each source

For each number, find the file, query or log that gives today's real value, and that source's owner. A number with no source is marked `unsourced` and stays out of any member, investor or public statement.

Completion: each number has a source path and an owner, or is marked `unsourced`.

### 3. Drill

Ask the owner, or the owner, each number without notes. Compare with the source. Within 10% is a match; outside it, or "I don't know", is a miss.

Completion: match or miss on all ten.

### 4. Close the misses and hear the data

For each miss, write the real value and one line that explains it. Where the owner's view and the owner's data disagree, write both and the test that would settle it; the owner decides with both in front of him. Verdict: ready when no number the meeting turns on is a miss, otherwise not ready. Nothing is sent from here.

Completion: ready or not ready, every miss corrected, and every disagreement written down.

## Anti-Patterns

- Memorizing numbers that have no source.
- Quoting a number from memory to members or investors.
- Overruling the data with confidence.
- Drilling fifty numbers instead of the ten that matter.

## Source and adaptation

