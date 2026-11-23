---
name: strategy-red-team
description: "Use when asked to red-team, stress-test or pressure-test a plan, PRD, roadmap, launch, pricing or strategy, even one already chosen; to poke holes in it or ask what kills it; or to get it ready for an exec or investor review. Not for imagining a chosen plan's failure, use tailered-ai:premortem; not for weighing options with no plan yet, use tailered-ai:council; not for reviewing code, use tailered-ai:lockin review."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Strategy red-team

Most plans have only survived polite feedback. This skill is a sharp, fair adversary: it attacks the claims the plan cannot live without, today, and hands back the cheapest way to find out whether each is true. The goal is a sharper decision, not a longer risk list. A few real kill-assumptions with tests beat twenty generic risks.

A red-team attacks the logic now. A premortem (tailered-ai:premortem) imagines the chosen plan has failed and works back to why. The words decide: "red-team it" gets a red-team even on a chosen plan, and "premortem it" gets a premortem.

## When to Activate

- "Red-team this", "stress-test this plan", "poke holes in it", "what kills this?"
- A plan, PRD, pricing, launch or roadmap is about to go to a decision maker.
- A goal has numbers (revenue, conversion, dates) that nobody has multiplied out.

Do not use for:
- reviewing code or a diff: tailered-ai:lockin review;
- a hard choice between options with no plan yet: tailered-ai:council;
- a constraint everyone treats as fixed: tailered-ai:first-principles.

## Inputs and outputs

Input: the plan (text or a file) and, if given, the decision it feeds and the deadline. With no plan, search the named file, thread or project for it first and ask only when none exists; never red-team a summary of a summary.

Output: one report in the shape in step 6, in the reply and saved in the task folder. Nothing else is edited.

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, fetch the missing inputs you can reach yourself, and end with the one or two you could not reach that would change the result.

## Steps

### 1. Extract every claim

List what the plan asserts as true: about the user, the market, the constraint, the mechanism, the money and the timeline. Mark each **load-bearing** (if false, the plan dies) or cosmetic. Do the arithmetic the plan implies: multiply every rate by its base and compare the result with the goal. A base the plan does not give is written `not given` and listed under what could not be assessed, never assumed. A goal the plan's own numbers cannot reach is the first kill-assumption.

Completion: every claim is listed with its mark, and every number in the plan has been multiplied through to the goal, with the result written.

### 2. Steelman, then attack

For each load-bearing claim, first write the strongest reason it might be true. Attack that version, never a weaker one. Write the attack as "Fails if ___": concrete and falsifiable ("fails if monthly churn stays above 8% after the second month"), never "execution risk".

Completion: each load-bearing claim has a steelman line and a "Fails if" line.

### 3. Refute yourself

Default to "the risk is real" unless the plan already cites evidence against it. When a claim is well reasoned, say so plainly and move it to what holds up. Invent no weakness the plan does not have; a red-team that manufactures doubt is as useless as one that rubber-stamps.

Completion: each claim is kept as a kill-assumption or moved to "what holds up" with the reason.

### 4. Rank

Score each kill-assumption 1 to 5 on impact if wrong, likelihood it is wrong and cheapness to test, and rank by the product. Keep at most five. When fewer survive step 3, keep fewer and say how many survived; never pad the list.

Completion: the kept kill-assumptions are in ranked order, each shows its three scores and their product, and the count is at most five.

### 5. Give each one something to do

For every kept kill-assumption write four lines: **Fails if**, **Evidence to get this week** (the specific query, data pull or conversation; run the read-only ones you can now and report the result; one that spends money, deploys, writes to production or contacts a person is named, not run: spending and contacting a person wait for the owner's word, and a deploy or production write goes through the release coordinator on the owner's word; a test a limit stops is reported as "not run, because <limit>" and stays the first test), **Kill criterion** (the threshold at which you stop or change course; one you set yourself is marked `proposal`) and **Cheapest test** (the smallest experiment that moves the belief). A second model's opinion is added only when asked; mark where it disagrees.

Completion: every kill-assumption has all four lines, each specific to this plan.

### 6. Report

```
#### Red-team: <plan in one line>

#### Top kill-assumptions (ranked by impact x likelihood x cheapness to test)
1. Claim: ...  Steelman: ...  Scores (judgments, not measurements): impact 5, likelihood 4, cheapness 5 = 100 (example only)
   Fails if: ...  Evidence to get this week: ...  Kill criterion: ...  Cheapest test: ...

#### What holds up
<each well-reasoned claim and why>

#### What I could not assess
<what the plan did not give enough to judge>
```

End on what to do first, not on what to fear; the one or two inputs that would change the result follow that line.

Completion: the report has all three sections, and the first line after it names the one test to run first, already run when it is read-only and the agent can run it (the limit in step 5).

## Anti-Patterns

- A generic risk list ("competition", "execution") with nothing specific to this plan.
- Attacking a strawman instead of the steelman.
- Leaving a goal unmultiplied: rates quoted without their base.
- Padding the list to look thorough; the cheapest high-impact test is the whole point.
- Inventing doubt about a claim that the plan already supports.

## Source and adaptation

Source: `strategy-red-team` from phuryn/pm-skills, commit `2a12295a7717569baa7be181b4cfebe3ca38a6bb`, SKILL.md SHA256 `3758fcf6f2f2653721c9d58586f7816e17d47d4723b54a5d3457a6641d2663fc`. License: MIT, Copyright (c) 2026 Pawel Huryn (see NOTICE.md at the plugin root). "Clone" was read as adapting into the house format, not copying byte for byte.

Changes: restructured into the house step form with completion criteria; added the step 1 arithmetic pass, shown 1-5 scores per item, a ceiling of five with no floor, routing to the plugin's premortem, council, first-principles and review skills, and "Do not use for"; the `$ARGUMENTS` placeholder, the cross-model step's model list and the further-reading links were dropped.
