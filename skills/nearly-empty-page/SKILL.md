---
name: nearly-empty-page
description: "Use when a main product card, page or member email has grown crowded; when someone asks to add a badge, banner, widget, field or default to a member surface; or when the owner says keep it simple or too busy. Not for planning a new page from scratch; use tailered-ai:design-shape. Not for cutting steps from a process; use tailered-ai:delete-the-step."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Nearly empty page

Google's homepage was for years a logo, a box and two buttons, and additions were reported as having to earn their place. Each surface did one job. The guard is the owner's not-to-copy: in 2010 Google Buzz arrived in Gmail with a default that could show a user's contacts publicly, and the FTC order required privacy audits every two years for 20 years. So nothing on a member surface shows or shares member data or contacts without asking.

## When to Activate

- A main product card, page or member email has grown crowded.
- Someone asks to add a badge, banner, widget, field or default.
- The owner says keep it simple or too busy.

Do not use for:
- planning a new page: tailered-ai:design-shape;
- cutting steps from a process: tailered-ai:delete-the-step.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the surface, the proposed addition and its owner.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `surface.md`: the one job, each element's verdict, the count before and after, and the defaults check.

## Steps

Lead the reply with the element table and the count before and after, then the verdict line, detail after.

### 1. Name the one job

Write the surface's job in one sentence. main product card: show the model's number beside the book and prediction-market prices for one game.

Completion: one sentence naming one job.

### 2. Count every element

List each visible element and whether it serves the job. Keep what the company design rules require: control labels, actionable errors, and source and timing next to their numbers. Mark each keep, change (move into a disclosure, such as Book vs model) or stop. An addition must replace an element: the count does not rise.

Completion: an element table with a verdict each, and a count after that is no higher than before.

### 3. Check the defaults

List every element that shows, shares or uses member data: follows, saves, contacts, books, profile image. Each is off until the member turns it on; no member sees another's data by default.

Completion: each data-touching element listed with its default, and none on without asking.

### 4. Owner and route

Name the owner; proposal: the main product session. The change follows the company design rules in the shared workspace AGENTS.md and ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: a named owner and the release route.

## Anti-Patterns

- Adding an explainer badge or footer to fix a crowded card.
- Removing source, timing or error text to look clean.
- Turning on a sharing default because it seems useful.
- Counting once and letting the page grow back.

## Source and adaptation

Source: original Tailered AI skill, which cites reported accounts of Google's homepage, the 2011 FTC Buzz settlement. No third-party skill text is copied.
