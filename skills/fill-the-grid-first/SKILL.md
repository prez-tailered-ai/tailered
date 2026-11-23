---
name: fill-the-grid-first
description: "Use when a new league, sport, bet type, prop or market is proposed while the company's current grid is not done; when the owner says cut the list, focus, say no, or the grid; when someone asks to add NFL, MLB, soccer or player props; or when work spreads past the grid. Not for running an approved bet with a loss cap; use tailered-ai:capped-experiment. Not for trying a pipeline step on one league; use tailered-ai:one-league-trial."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Fill the grid first

Back at Apple in 1997, Jobs cut the product line to a two-by-two grid: consumer and pro by desktop and portable. The owner's rule for the company: a grid of leagues by bet types, and anything outside it is a no until every cell is full. The guard: a no can stay wrong too long. In 2007 iPhone apps were to be web apps only; the App Store opened in July 2008. So every no keeps its reason and what reopens it.

## When to Activate

- A new league, bet type, prop or market is proposed.
- The owner says "cut the list", "focus", "say no" or "the grid".
- Work spreads past the grid.

Do not use for:
- running an approved bet with a loss cap: tailered-ai:capped-experiment;
- trying a pipeline step on one league: tailered-ai:one-league-trial.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the request, the owner's grid, what each cell publishes.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank. When you cannot open the page, file or data a step asks for, still fill every row: name the exact page, file or command to check and the value you expect there, marked `proposal`. Every row of every table gets a verdict word and an owner.

Output: `grid.md`: the grid, each cell full or open, the ruling, and the no list.

## Steps

Lead the reply with the grid table, then the verdict line, then detail.

### 1. Draw the grid

Rows are leagues, columns are bet types. Without the owner's grid, propose the four main product leagues (NBA, NHL, NCAAF, NCAAM) by spread or puck line, total and moneyline, marked `proposal`.

Completion: a table with every cell named.

### 2. Mark each cell full or open

Full means published on every slate for a window and passing a check. Proposal: 14 days, graded against the closing line, no open defect. Each open cell gets what is missing and an owner.

Completion: every cell says full or open, with the evidence or the missing piece and its owner.

### 3. Rule on the request

Inside the grid: yes, and work on an open cell goes first. Outside the grid while any cell is open: no until full. Log each no: the ask, who asked, the reason and the reopen trigger.

Completion: the verdict word (yes or no until full) and, for a no, its line in the no list.

### 4. Point the work

Name the open cell closest to full as next, with owner and date. Changing the grid is the owner's call. Live work carries through tailered-ai:workflow and ships through the release coordinator on the owner's word.

Completion: the next cell, owner and date, and the release route named.

## Anti-Patterns

- Yes to a new league while a cell is open.
- Full with no window or check.
- A no with no reopen trigger.
- Changing the grid without the owner.

## Source and adaptation

Source: original Tailered AI skill, which cites Isaacson's Steve Jobs (2011) on the 1997 product grid, the App Store's July 2008 opening. No third-party skill text is copied.
