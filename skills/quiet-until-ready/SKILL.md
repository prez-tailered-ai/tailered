---
name: quiet-until-ready
description: "Use when deciding what to say, and to whom, about unfinished company work such as a new model, league or feature; when the owner says keep it quiet, surprise, stealth or announce it; when a teaser, leak or early post is proposed; or when someone suggests not telling members or the owner about a change. Not for writing the launch post itself; use tailered-ai:teach-every-launch. Not for telling members about a wrong number; use tailered-ai:same-day-correction."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Quiet until ready

Jobs kept products secret until a stage reveal, often with "one more thing". The guard: in early 2009 Apple's statements about his health were reported as incomplete, and the SEC reportedly looked at the disclosures. At the company, secrecy faces outsiders before a launch only. The owner is told everything, and members are told now about anything that touches the numbers they rely on.

## When to Activate

- Someone asks what to say, and to whom, about unfinished work.
- The owner says "keep it quiet", "surprise", "stealth" or "announce it".
- A teaser, leak or early post is proposed, or someone suggests not telling members or the owner.

Do not use for:
- writing the launch post: tailered-ai:teach-every-launch;
- telling members about a wrong number: tailered-ai:same-day-correction.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the work, its facts, its planned launch date, and who has asked.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank. When you cannot open the page, file or data a step asks for, still fill every row: name the exact page, file or command to check and the value you expect there, marked `proposal`. Every row of every table gets a verdict word and an owner.

Output: `hold.md`: the told-now list, the held list with reasons, the harm check, and the reveal plan.

## Steps

Lead the reply with the two lists, then the verdict line, then detail.

### 1. Sort every fact

Put each fact in told now or held until launch. Told now, always: everything to the owner; to members, errors, outages, changes to published numbers, a model switch that changes what they see, and any new use of their data. Held from outsiders only: unfinished features, launch dates, and test results not yet shipped.

Completion: every fact in one list with a reason, and nothing withheld from the owner.

### 2. Check the hold harms no one

For each held fact, ask: does it change what a member reads on the main product today, or what they paid for? A yes moves it to told now.

Completion: a yes or no for every held fact, with yeses moved.

### 3. Plan the reveal

Set the date, what is shown, and the owner. Reveal only what has shipped through tailered-ai:workflow and the release coordinator on the owner's word. Write the post with tailered-ai:teach-every-launch; the owner approves it. This skill posts nothing.

Completion: reveal date, owner and release route named, with the owner as approver.

### 4. Keep the hold visible

Save both lists in the task folder where the owner can read them, and name who may see the held list. Verdict: hold (keep quiet until the date), tell (move to told now) or reveal (shipped; go).

Completion: the file saved, the reader list named, and the verdict word.

## Anti-Patterns

- Keeping anything from the owner.
- Quietly changing members' numbers before the reveal.
- Teasing a feature that has not shipped.
- A hold with no reveal date.

## Source and adaptation

Source: original Tailered AI skill, which cites Apple's launch secrecy and stage reveals, and reported 2009 accounts of Apple's health statements and an SEC inquiry. No third-party skill text is copied.
