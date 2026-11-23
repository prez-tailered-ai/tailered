---
name: rank-by-record
description: "Use when projections are ordered for the main product, a digest or a shortlist; when the owner asks which picks to trust, or says rank by record, PageRank or votes; or when a list is sorted by model confidence or edge size. Not for a public test of the model; use tailered-ai:prove-it-in-public. Not for changing the model; use tailered-ai:ai-model-research."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Rank by record

PageRank (Brin and Page, 1998) ranked pages by the links others gave them, each link a vote. The owner's practice: rank picks by their checked record, not by how sure the model sounds. The guard: link farms gamed PageRank; a record is gamed by choosing the window, league or sample. Member activity counts only in totals; member data or contacts are never exposed or shared without asking (Google Buzz).

## When to Activate

- Projections are ordered for the main product, a digest or a shortlist.
- The owner asks which picks to trust, or says rank by record, PageRank or votes.
- A list is sorted by model confidence or edge size alone.

Do not use for:
- a frozen public test of the model: tailered-ai:prove-it-in-public;
- what to change in the model: tailered-ai:ai-model-research.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: today's list, and graded past projections with the price at publish and the closing price.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `ranking.md`: each item's record cell, sample size, score, rank and verdict.

## Steps

Lead the reply with the ranked table, then the verdict line, detail after.

### 1. Build the record cells

Group graded projections into cells, such as NBA totals with a 2 to 4 point edge. Per cell write count, hit rate, average closing-line value (did the market move toward the model?) and calibration. Fix the window first; proposal: the last 180 days.

Completion: a cell table with all four figures, and the window stated first.

### 2. Score each item by its cell

Score each item by its cell, not its confidence. Closing-line value weighs most: the closing market is the strongest vote others cast. A cell under 100 games (proposal) is shrunk toward zero and marked thin.

Completion: every item has a cell, a score and a thin mark where it applies.

### 3. Check for gaming

Was the window picked after the fact, a losing league dropped, the sample too small? Flag items whose rank moves when the window shifts 30 days. Member follows or saves count only as totals.

Completion: three written answers, and no member name, contact or per-member action in the output.

### 4. Verdict, owner and route

Write keep, change (rank lower) or stop (hold off) per item. Name the daily owner; proposal: the day-build session. Members see estimates, never advice. A live order change goes through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: a verdict word per item, a named owner and the release route.

## Anti-Patterns

- Sorting by confidence or edge size and calling it a ranking.
- Choosing the window after seeing which looks best.
- Putting a thin cell on top.
- Showing which members followed or saved a game.

## Source and adaptation

Source: original Tailered AI skill, which cites Brin and Page (1998). No third-party skill text is copied.
