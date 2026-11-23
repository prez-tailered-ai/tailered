---
name: memo-not-slides
description: "Use before any change to the model, the day build or the publishing-step rules; when the owner asks for slides, a deck or to make the case for an internal decision; or when a decision is being argued in chat with no written case. Not for agent instruction files; use tailered-ai:writing-for-agents."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Memo, not slides

Write the case as a one-page memo in full sentences, read before anyone discusses it. Amazon stopped slide presentations in senior meetings in 2004; meetings open with a narrative memo read in silence (2017 letter), because sentences force the "because" that bullets hide. Its cost is time: Bezos said great memos take a week or more. The owner's version is one page.

## When to Activate

- A change to the model, the day build or the publishing-step rules is proposed.
- The owner asks for slides, a deck or "make the case" for an internal decision.
- A decision is being argued back and forth with nothing written.

Do not use for:
- agent instruction files or skills: tailered-ai:writing-for-agents;
- design documents for a build: tailered-ai:design-document;
- investor or public decks; this skill is for internal decisions.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the proposed change and its evidence.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `memo.md`: one page, about 500 words, in paragraphs, with a small table only where numbers need one.

## Steps

### 1. Gather the facts

Say which trigger applies and why it needs a memo: a change to the model, the day build or the publishing-step rules. Then list each number with its source, a file path or command and its date. A number without a source is marked unknown.

Completion: every fact has a source or the word unknown.

### 2. Write the memo

Six parts, in this order, as paragraphs: the question and the decision needed by when; where things stand today; the options, at least two and including doing nothing, each with its cost; the recommendation and why; what evidence would change it; who decides.

Completion: all six parts, under 550 words by `wc -w`, prose rather than bullets.

### 3. Read it as a skeptic

Mark every claim without a source and every vague word such as "significant" or "much better", then fix or cut them.

Completion: no unsourced number remains.

### 4. Hand it over

The owner reads it before the discussion. Record the decision and its date at the bottom. Slides, if still wanted, come after and add nothing the memo lacks.

Completion: the decision is recorded, or the memo is with the owner.

## Anti-Patterns

- Bullets that state conclusions with no "because".
- Six pages for a small change; the owner's limit is one.
- Writing the memo after the decision.
- Slides first, memo never.

## Source and adaptation

