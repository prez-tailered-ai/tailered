---
name: capped-experiment
description: "Use when a new league, market type, product line, data source or model family is tried as an experiment; when the owner says let's try it or calls something a big bet; or when an experiment is losing and nobody set a limit. Not for comparing prompts or models on an eval set; use tailered-ai:agent-eval. Not for trying a pipeline step on one league; use tailered-ai:one-league-trial."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Capped experiment

Run experiments big enough to matter, with the loss capped before they start. Bezos called Amazon the best place in the world to fail (2015 letter): a few large winners such as AWS pay for many failures. One failure was the Fire Phone, a $170 million charge. The owner's guard: a small company cannot absorb that. So the cap and the kill date come first.

## When to Activate

- A new league, market type, product line, data source or model family is tried.
- The owner says "let's try", "big bet" or "experiment".
- An experiment is losing money or time and nobody set a limit.

Do not use for:
- comparing prompts or models on an eval set: tailered-ai:agent-eval;
- trying a pipeline step on one league: tailered-ai:one-league-trial;
- choosing what to change in the model: tailered-ai:ai-model-research.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the idea, the runway in months and monthly cash from the owner, and the team time it would take.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `bet.md`: hypothesis, success number, loss cap in money and hours, kill date, and the write-up at the end.

## Steps

### 1. State the hypothesis

One sentence: if we do X, then Y moves by Z by a date. When the owner has given no numbers, propose concrete ones and mark them as proposals; a blank is not a hypothesis.

Completion: one sentence with a number and a date.

### 2. Cap it before it starts

Set the most money and hours it may use, and the kill date. Size the cap as a loss the company could take in full without cutting the core product; when the runway is unknown, propose a dollar and hour figure, mark it a proposal, and say what runway it assumes. The owner approves it.

Completion: the cap in dollars and hours, the kill date, and the owner's approval.

### 3. Check at the cap or the date

Continue only when the success number is on track. Money already spent is not a reason to continue. If an experiment is already running with no cap, set one from today and say so.

Completion: the word continue or stop, with the number that decided it. With no number yet, the answer is stop until the cap and success number are set.

### 4. Write it up

Record what was learned, what it cost and what to try next, in the task folder. Write up a failure the same way as a win.

Completion: the write-up exists.

## Anti-Patterns

- Starting with no cap, or moving the kill date.
- Continuing because of what was already spent.
- Experiments so small they cannot show a result either way.
- Hiding a failure.

## Source and adaptation

