---
name: think-week-read
description: "Use when proposals, briefs, session reports, member feedback or ideas have piled up unread; when the owner says think week, read everything or what have I missed; or before a season plan when nobody has read the backlog. Not for new outside research; use tailered-ai:apex-research. Not for research on the sports models; use tailered-ai:ai-model-research. Not for asking everyone for warnings by a deadline; use tailered-ai:call-for-warnings."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Think-week read

Twice a year Gates reportedly took a Think Week, reading papers sent in by staff and writing comments back. The practice: read the whole pile in one block, then decide on each item. The guard: a week away is a big-company luxury, and reading with no verdict wastes it. The company caps the block at one day, and every item gets a verdict.

## When to Activate

- Proposals, briefs, session reports, member feedback or ideas have piled up unread.
- The owner says "think week", "read everything" or "what have I missed".
- A season plan is due and nobody has read the backlog.

Do not use for:
- new outside research: tailered-ai:apex-research;
- research on the sports models: tailered-ai:ai-model-research;
- asking for warnings by a deadline: tailered-ai:call-for-warnings;
- an end-of-shift note: tailered-ai:top-five-shift-note.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the folders or records to read and the date range.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `reading-verdicts.md`: every item with its source, a one-line summary, its verdict and owner, and the top three ideas.

## Steps

Your reply leads with the verdict table (item, one line, verdict, owner), then the line naming the top three ideas.

### 1. Gather the whole pile

List every item in range: plans, artifacts folders, research briefs, session records (read only), member feedback. Count them. Past 40 items (proposal), read the 40 newest and list the rest.

Completion: an item count and the reading list.

### 2. Read in one block

Read each item in full, in one block of at most one day. Write a plain one-line summary of each. Do not stop to act mid-read.

Completion: a summary line for every item read.

### 3. Give each a verdict

Each item gets act, park or drop. Act needs a named owner and a date; park, the signal that would revive it; drop, one reason. Merge items that say the same thing.

Completion: every item has a verdict, and every act an owner and a date.

### 4. Pick the top three and route them

Name the three ideas that matter most this season, with the number each would move. Send each to its skill: a model or day-build change to tailered-ai:memo-not-slides, a trial to tailered-ai:capped-experiment. Nothing goes live from here; a live change takes tailered-ai:workflow and the release coordinator on the owner's word.

Completion: three ideas, each with a number, an owner and its next skill.

## Anti-Patterns

- Reading only the items that agree with the plan.
- Acting on the first good idea before the pile is done.
- A verdict of "interesting" with no owner.
- Writing in another session's record instead of only reading it.

## Source and adaptation

Source: original Tailered AI skill, which cites the Wall Street Journal's 2005 report on Gates's Think Weeks. No third-party skill text is copied.
