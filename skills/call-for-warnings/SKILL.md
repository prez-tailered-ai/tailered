---
name: call-for-warnings
description: "Use when a decision on the model, the day build, the publishing step, pricing or a new market should hear objections first; when the owner says listen early, any warnings or write it down once; or when warnings sit scattered across chats, sessions and agents. Not for the owner setting a new direction for everyone; use tailered-ai:direction-memo. Not for the written case for one change; use tailered-ai:memo-not-slides."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Call for warnings

In May 1995 Gates's Internet Tidal Wave memo ranked the Internet above every other priority. Staff warnings, such as J Allard's 1994 memo, were reported to have come first, and sat unread. The owner's practice: a reply deadline for warnings from anyone or any agent, then one plain note everyone reads. The guard: silence by the deadline is no reply, never agreement.

## When to Activate

- A decision on the model, the day build, the publishing step, pricing or a market is coming.
- The owner says "listen early", "any warnings" or "write it down once".
- Warnings sit scattered with no single record.

Do not use for:
- The owner setting a new direction for everyone: tailered-ai:direction-memo;
- the written case for one change: tailered-ai:memo-not-slides;
- reading a backlog with no decision pending: tailered-ai:think-week-read.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the decision, its date, and who should be asked.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `warnings-note.md`: the call, every warning with source and answer, and the note.

## Steps

Your reply leads with the warning table (who, warning or no reply, answer), then the verdict line: go, change or hold.

### 1. Write the call

Write the decision in one sentence, its date, what counts as a warning (any risk or odd number), and the reply deadline, 24 hours before (proposal). List who is asked: the owner, each active session in the shared queue records, each agent on the work, anyone named.

Completion: the call with a dated deadline and a named list of who is asked.

### 2. Hand it over to go out

Nothing is sent from here. The owner sends it, or it goes in this session's own queue record, never another's.

Completion: the call with the owner or in this session's own record, timed.

### 3. Collect until the deadline

Record each warning with source and time, and no reply for anyone silent. Late ones go in, marked late. Answer each: acted (what changed), declined (one reason) or open (owner and date).

Completion: each one asked has a warning or no reply; each warning an answer.

### 4. Write it down once

One plain note, at most a page: the decision, warnings and answers, what changed, owner and date. It replaces the scattered threads. Verdict: go, change or hold. The owner decides and shares it; anything live takes tailered-ai:workflow and the release coordinator on the owner's word.

Completion: one note under a page, with a verdict, an owner and the route.

## Anti-Patterns

- Deciding before the deadline.
- Treating no reply as agreement.
- Dropping a warning because an agent sent it.
- Several notes for one decision.

## Source and adaptation

Source: original Tailered AI skill, which cites Gates's Internet Tidal Wave memo of 26 May 1995, reported accounts of J Allard's 1994 memo. No third-party skill text is copied.
