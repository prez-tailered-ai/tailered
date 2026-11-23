---
name: press-release-first
description: "Use when a new main product feature, card, alert, league or other member-facing change is proposed and nothing is built yet; when the owner says work backwards, start from the customer, start from a bettor's real question, or write the press release first; or when a build is about to start from an idea instead of a member's ask. Not for shaping the brief of a page already chosen; use tailered-ai:design-shape."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Press release first

Write the launch-day press release and its FAQ before building, while changing what gets built is still cheap. Amazon calls this working backwards. Its guard is the Fire Phone: reported as built around features its founder wanted, it ended in a $170 million charge in 2014. So the release here must start from a real member's question, never from ours.

## When to Activate

- A new feature, card, alert, league, market type or member-facing change is proposed and no code exists yet.
- The owner says "work backwards", "start from the customer", "a bettor's real question" or "write the press release".
- A build is about to start and nobody can quote the member who asked for it.

Do not use for:
- shaping the brief of a page already chosen: tailered-ai:design-shape;
- deciding what to change in the model: tailered-ai:ai-model-research;
- carrying a chosen change to release: tailered-ai:workflow.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the idea, and any member words about it (support mail, Discord, chat, a request the owner heard).

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `prfaq.md`: a press release under 250 words, an FAQ of five to eight questions, and a verdict line: build, change or do not build.

## Steps

### 1. Find the real question

Look for a member's own words asking for this, and quote one with its source and date. If none exists, write `No member has asked for this yet.` That line is a finding, not a gap to fill with a guess.

Completion: one quoted ask with source and date, or that line.

### 2. Write the press release

Date it launch day. In order: a headline in the member's words; one paragraph on who it is for and what they can now do; the problem they have today; how it works, in two sentences; a member quote only if one exists from step 1, otherwise `[member quote needed]`; how to start. No internal words such as day build or adapter. Estimates, never advice: it never promises winners.

Completion: under 250 words, and no quote that a real member did not say.

### 3. Write the FAQ

Five to eight questions. Member side: cost, accuracy, what happens when data is late, how it differs from the book's own app. Inside: cost to build and run, what we stop doing to make room, the number that shows it worked after 30 days, what could go wrong. Mark at least two as the questions a skeptic would ask first.

Completion: five to eight answered questions, two marked hard.

### 4. Decide

Build only when the release names a real member question and the 30-day number. A release its own member would shrug at is a do not build. For build, name the one thing it must do on day one.

Completion: the verdict line with its reason. A build goes next to tailered-ai:design-shape for the brief, and ships through tailered-ai:workflow and the release coordinator on the owner's word.

## Anti-Patterns

- Writing the release after the build to justify it.
- Inventing a member quote, or putting our wish in a member's mouth.
- A list of features with no member question behind them.
- Treating the draft as marketing copy to publish; it is an internal decision document.

## Source and adaptation

Source: original Tailered AI skill, which cites Bryar and Carr, Working Backwards (2021), on the PR/FAQ; Fast Company (2015) and Amazon's Q3 2014 results on the Fire Phone. No third-party skill text is copied.
