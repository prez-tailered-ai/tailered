---
name: direction-memo
description: "Use when the owner wants to change what every session and person works on, such as a new focus for the season, a new audience or a new rule for the whole company; when the owner says write the memo to everyone, set the direction or here is where we are going; or when sessions are pulling in different directions. Not for the case for one change; use tailered-ai:memo-not-slides. Not for long-term commitments behind one choice; use tailered-ai:long-term-letter."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Direction memo

Set company direction in one long written memo that says what changes, what stops and by when. Zuckerberg used long public memos for this: the 2012 IPO letter, "Building Global Community" in 2017, and the 2019 privacy-focused vision. The guard: the 2019 memo set encryption by default for messaging, and Messenger's default arrived in December 2023, about four and a half years later. A direction with no dated commitments drifts, so every commitment here has an owner and a date.

## When to Activate

- The owner wants to change what everyone works on: a season focus, a new audience, a company-wide rule.
- The owner says "write the memo to everyone", "set the direction" or "here is where we are going".
- Sessions are pulling in different directions on the same goal.

Do not use for:
- the case for one change to the model or day build: tailered-ai:memo-not-slides;
- long-term commitments behind one choice: tailered-ai:long-term-letter;
- planning one rewrite: tailered-ai:admit-and-rewrite.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the owner's new direction in his words, the open work in the shared queue, and the date it starts.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `direction-memo.md`: the memo (two to four pages), the stop list, the commitments table, and the check date.

## Steps

### 1. Say where and why now

Write the direction in one sentence, then why now with numbers, such as the share of members who trade prediction markets. Write it as prose, for members of the team who were not in the room.

Completion: the one-sentence direction and two or more numbers behind it.

### 2. Write the stop list

List the work that stops or slows because of this memo, from the open tasks in the shared queue. A direction that stops nothing changes nothing.

Completion: three or more named tasks marked stop or slow.

### 3. Date every commitment

Turn the direction into commitments. Each has one owner, a number to reach and a date within a season. Long goals get a first milestone inside 90 days.

Completion: a table of commitments, each with an owner, a number and a date.

### 4. Set the check and hand over

Set a check date to compare work against the memo, with keep, change or drop for each commitment. The owner reads, edits and shares the memo; sessions copy it into their own records. This skill writes only in its task folder, writes no other session's record and posts nothing.

Completion: the check date, and the memo left with the owner to share.

## Anti-Patterns

- A vision with no dates.
- A memo that stops nothing.
- Commitments with two owners or none.
- Writing into other sessions' queue records.

## Source and adaptation

