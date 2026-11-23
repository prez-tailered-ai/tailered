---
name: single-threaded-owner
description: "Use when several sessions or people are each doing part of one initiative, when nobody can say who owns something, when an initiative stalls between owners, or when the owner asks who should own it. Not for dispatching helpers on one task; use tailered-ai:team-agent-orchestration."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Single-threaded owner

Give each initiative one owner whose only job it is. Amazon moved from two-pizza teams to single-threaded leaders: one person fully on one initiative, with the team to deliver it (Bryar and Carr). Split attention kills initiatives quietly. The guard: an owner can wall the work off, so the owner publishes what others can rely on.

## When to Activate

- Two or more sessions or people are each doing part of one initiative.
- Nobody can say who owns it, or it stalls between owners.
- The owner asks "who should own this".

Do not use for:
- sending helpers to work one task in parallel: tailered-ai:team-agent-orchestration.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the initiative, and who touches it now, from the shared queue records.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: an owner record: initiative, owner, what each other party stops, the outcome the owner answers for, and the interface.

## Steps

### 1. Map who touches it

List each session or person working on it and what they do.

Completion: the list, with sources.

### 2. Pick one owner

Choose the one with the most context and the capacity to make it their only thread, and name them. When you cannot see who that is, name the role or session that fits, such as the session that built the loader, marked `proposal`; never leave the owner unnamed. If two qualify, the owner decides.

Completion: exactly one name, with the owner's word where it was contested.

### 3. Clear the rest

For each other party, say what they stop or hand over, with the files. The owner drops other threads or names who takes them.

Completion: every other party has a stop or a handover.

### 4. Set the outcome and the interface

Name the measurable result the owner answers for and its date, and what others can rely on: an output file, a schedule, a weekly note. The owner records it in its own queue record; a session writes only its own record.

Completion: the owner's record carries the outcome and the interface.

## Anti-Patterns

- Co-owners, or a committee.
- An owner with three other jobs.
- Naming an owner without stopping the others.
- Writing another session's queue record.

## Source and adaptation

