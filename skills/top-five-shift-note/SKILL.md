---
name: top-five-shift-note
description: "Use when a session, agent or person ends a shift, hands off or stops for the day; when the owner asks for top five, a five-line note, an end-of-shift note or what everyone did today; or when the owner is reading long reports or transcripts to learn where things stand. Not for a full checklist of what a session proved; use tailered-ai:checklist-session. Not for the written case for a decision; use tailered-ai:memo-not-slides."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Top-five shift note

End every shift with five lines. Jensen Huang is reported to keep about 60 direct reports and to ask everyone for a short "top five things" email, which he reads to see the company without layers of status meetings. The owner's version: every person and agent ends its shift with a five-line note. The guard: a flat company works only when the notes are short, true and read; a note that hides a slip, or a number with no source, is worse than none.

## When to Activate

- A session, agent or person ends a shift, hands off, or stops for the day.
- The owner says "top five", "five-line note" or "end of shift", or asks what everyone did.
- The owner is reading long reports or transcripts to learn where things stand.

Do not use for:
- a full checklist of what a session proved: tailered-ai:checklist-session;
- the written case for a decision: tailered-ai:memo-not-slides.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: what this shift did, its evidence (files, command results, record ids), what is blocked, and the reader (the owner unless someone else is named).

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `top-five.md`: the reader, then five lines of under 25 words each, each with its source.

## Steps

### 1. Pick the five

Choose what matters to the reader, not the biggest efforts. Fixed order: 1 finished, 2 in progress with its next step, 3 blocked and who must act, 4 a risk or a slip, 5 the one thing the reader must decide. A line with nothing says "none"; never pad it.

Completion: five lines in that order, each under 25 words.

### 2. Source every claim

Each line names its evidence: a file path, a command result or a record id. A number carries where it came from. A claim with no evidence says "unverified". Never drop a bad result to keep the note clean.

Completion: every line has a source or the word unverified.

### 3. Name owners and dates

Lines 2, 3 and 5 name an owner and a date. A slip on line 4 gives the old date, the new date and the reason.

Completion: an owner and a date on lines 2, 3 and 5.

### 4. File it

Write `top-five.md` in the task folder. If this session has its own queue record, copy the lines there; never write another session's record. Send nothing. Live work still goes through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the file exists with the reader named at the top, and its path is in the reply.

## Anti-Patterns

- Six lines, or five paragraphs.
- Listing effort ("read 40 files") instead of results.
- Leaving out the blocked line because it looks bad.
- Writing in another session's record.

## Source and adaptation

Source: original Tailered AI skill, which cites reported accounts of Huang's direct reports and top-five emails (Huang interviews; The Nvidia Way, 2024). No third-party skill text is copied.
