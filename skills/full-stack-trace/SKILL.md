---
name: full-stack-trace
description: "Use when a number on the main product looks wrong and nobody knows which layer caused it; when a fix is about to patch the card or the publish step instead of the layer where the error starts; when the owner asks where a number came from or who owns each layer; or before a change that crosses capture, model, day build and main product. Not for deciding to bring a supplier in-house; use tailered-ai:stoppage-to-ownership. Not for recovering a failing agent run; use tailered-ai:agent-introspection-debugging."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Full-stack trace

Know every layer under the number. NVIDIA sells the whole stack, chips, systems, networking, CUDA and its libraries, designed to work together. The company's stack is odds capture, the model, the day build, the publishing step and the main product card. This skill traces one number down every layer, names each owner, and puts the fix where the error starts. The guard: NVIDIA's bundle drew reported antitrust scrutiny, and owning the stack here means knowing every layer and its source, not building every layer. A number that loses its source on the way up is a defect, even when it is right.

## When to Activate

- A main product number looks wrong or stale.
- A fix is about to patch the card or the publish step.
- The owner asks where a number came from or who owns a layer.
- A change will cross two or more layers.

Do not use for:
- fixing a wrong card for members and saying what changed: tailered-ai:same-day-correction;
- deciding to bring a supplier in-house: tailered-ai:stoppage-to-ownership;
- recovering a failing agent run: tailered-ai:agent-introspection-debugging.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the number and read access to each layer's records.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `stack-trace.md`: one row per layer with value, source, owner and status, the first wrong layer, and the verdict.

## Steps

Lead the reply with the result: the first wrong layer and its evidence, the owner of that layer, and the verdict word keep, change or stop. Fix at the lowest wrong layer, never by patching the card. Detail follows.

### 1. Pin the number

Write the game id, the market, the value on the main product and the time it was seen. Read only; change nothing while tracing.

Completion: one number with game id, market, value and time.

### 2. Walk it down

From the main product card down to the raw capture, write for each layer the value it holds, where it got it (file, feed, capture time) and its owner, a person or session. Write "missing" where a layer cannot say its source.

Completion: a row per layer with value, source and owner, or the word missing.

### 3. Find the first wrong layer

Name the lowest layer where the value or its source is wrong or missing. The fix belongs there. List any patch above it that hides the error.

Completion: one layer named, with its evidence, or "all layers agree" with the evidence.

### 4. Decide and route

Verdict: keep (all layers agree), change (fix the named layer, owner, and remove the patches above it) or stop (halt a planned downstream patch). A fix is tried with tailered-ai:one-league-trial and ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict word, the owner, and the release route named.

## Anti-Patterns

- Fixing the card because that is where the error shows.
- A layer that holds a value with no source.
- Tracing from memory.
- Building a layer in-house because this skill found a bug in it.

## Source and adaptation

Source: original Tailered AI skill, which cites NVIDIA's product stack, its 2020 Mellanox purchase, reported antitrust scrutiny (2023 to 2024). No third-party skill text is copied.
