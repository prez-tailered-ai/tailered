---
name: saturday-close-review
description: "Use when last week's results need reviewing; when the owner asks how the model did last week, how we did against the close, for closing line value or CLV, or for the Saturday numbers; or when no fixed weekly review is on the calendar. Not for choosing what to change in the model; use tailered-ai:ai-model-research. Not for whether green metrics hide a problem; use tailered-ai:day-one-check."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Saturday close review

Look at last week's numbers early, every week, in one fixed slot. Walton held a Saturday morning meeting where managers went through the week's numbers store by store before anyone told a story. At the company the number is the close: did the market move toward each published projection by game time? The guard: his meetings were reported as long and early, so this one is capped at 30 minutes and puts the table before the talk.

## When to Activate

- The owner asks how the model did last week, or against the closing line.
- The owner says CLV, closing line value or "the Saturday numbers".
- No fixed weekly review exists, or one was skipped because the week went badly.

Do not use for:
- choosing what to change in the model: tailered-ai:ai-model-research;
- whether green dashboards hide a problem: tailered-ai:day-one-check;
- explaining how the model works: tailered-ai:know-the-numbers.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: last week's published projections per league, the closing sportsbook lines and prediction-market closing prices for the same games, and last week's review if one exists.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `review.md`: the slot and owner, the per-league table, a keep, watch or change mark per league, and one action per change.

## Steps

Lead the reply with the per-league table, then one verdict line per league, detail after.

### 1. Fix the slot and the owner

One weekly slot, the same every week (proposal: Saturday 09:00 Pacific, 30 minutes), and one named owner who runs it. The review happens on bad weeks too.

Completion: slot, length and owner are written in `review.md`.

### 2. Pull the week against the close

The owner says picks; the company publishes projections, so grade each projection's side. For every projection published Monday to Sunday, record the number when published, the closing line or closing price, and whether the close moved toward the model. Use the stored closing archive; start no new capture.

Completion: one row per league with games graded, the share that beat the close, the average gap in points or probability, and the data source named.

### 3. Read the numbers before the story

Compare each league with last week and the four-week average. Flag a league below 50% beat-the-close two weeks running (proposal), or with fewer than 20 graded games as too small to judge.

Completion: each league is marked keep, watch or change, with the number that decided it.

### 4. One action per change

Each change gets one action, one owner and a date. Model questions go to tailered-ai:ai-model-research. Anything that goes live ships through tailered-ai:workflow and the release coordinator on the owner's word. The review itself changes nothing.

Completion: every change row has an action, owner, date and route, and nothing was published or edited.

## Anti-Patterns

- Moving or skipping the slot after a losing week.
- Grading by win rate alone and ignoring the close.
- Letting talk run past 30 minutes before the table is read.
- Leaving a change with no owner or date.

## Source and adaptation

Source: original Tailered AI skill, which cites Walton and Huey, Sam Walton: Made in America (1992), reported accounts of the Saturday meeting. No third-party skill text is copied.
