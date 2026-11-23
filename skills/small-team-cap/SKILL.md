---
name: small-team-cap
description: "Use when a company project is about to add sessions, agents, contractors or helpers; when the owner asks how many people or sessions a project needs, or says keep the team small or only top people; when a project has more workers than anyone can name a job for; or before any agreement with an outside party that touches hiring, recruiting or staff. Not for naming the one owner; use tailered-ai:single-threaded-owner. Not for dispatching helpers on a task; use tailered-ai:team-agent-orchestration."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Small team cap

Jobs kept the Macintosh team small, reportedly near 100 people, and flew a pirate flag over its building in 1983 (Isaacson, 2011). The owner's not-to-copy: Apple, Google, Intel and Adobe settled a class action over secret agreements not to recruit each other's staff for $415 million (2015). The guard: no secret agreement with any outside party. Every agreement is written, visible to the owner, and never limits whom anyone may hire or recruit.

## When to Activate

- A project is about to add sessions, agents, contractors or helpers.
- The owner asks how many a project needs, or says "keep it small".
- Before any outside agreement that touches hiring, recruiting or staff.

Do not use for:
- naming the one owner: tailered-ai:single-threaded-owner;
- dispatching helpers: tailered-ai:team-agent-orchestration;
- bringing in an outsider for their skill: tailered-ai:bring-in-the-builders.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the project, everyone working on it, and every agreement with an outside party about people.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank. When you cannot open the page, file or data a step asks for, still fill every row: name the exact page, file or command to check and the value you expect there, marked `proposal`. Every row of every table gets a verdict word and an owner.

Output: `team.md`: the roster with keep or cut, the cap, and the agreement table.

## Steps

Lead the reply with the roster table: every session, agent and contractor you can name, from the shared queue or the owner's words or as a marked proposal, each with the one job only it does and keep or cut; then the cap number.

Lead the reply with the roster table, then the verdict line, then detail.

### 1. Count the team

List every session, agent, contractor and person on the project, what each does, and the one thing only they do.

Completion: a table with name, job and unique part for every member.

### 2. Set the cap

The cap is the smallest number where every member has a job no one else does (proposal: five for one company project). A member with no unique job is cut or merged into another.

Completion: the cap number, and keep or cut on every row.

### 3. Check every agreement

For each outside agreement touching people (contractors, partners, data vendors), answer three questions. Is it written? Can the owner see it? Is it free of any term on whom anyone may hire, recruit or pay? Any no stops the agreement and goes to the owner. This skill drafts and sends nothing to outside parties.

Completion: every agreement with three answers, and each no named for the owner.

### 4. Hold the cap

Adding past the cap is the owner's call, with the unique job named first. Save the roster where the owner can read it.

Completion: the roster saved, and any request past the cap left with the owner.

## Anti-Patterns

- Adding a helper with no job only it does.
- A handshake deal with a partner about staff.
- Any no-hire or no-recruit term, written or not.
- Growing past the cap without the owner.

## Source and adaptation

