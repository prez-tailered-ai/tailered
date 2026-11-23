---
name: generalist-stretch-test
description: "Use when one company hire or contractor must cover several kinds of work, such as modeling, odds capture and the main product; when the owner says we need a generalist or can they handle more than their specialty; or when a candidate is strong in one area and the work spans others. Not for writing the job post or pitch; use tailered-ai:mission-pitch. Not for an outsider's access to code, data or keys; use tailered-ai:bring-in-the-builders."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Generalist stretch test

Microsoft hired smart generalists through hard interviews, reported to lean on puzzles. The practice: a small company's hire covers several jobs, so test thinking on hard problems outside the specialty. The guard: Google's hiring head reported in 2013 that brainteasers predicted nothing. The problems are real company work in two areas, scored on a rubric written first.

## When to Activate

- One hire must cover several kinds of work.
- The owner says "we need a generalist" or "can they do more than their specialty".
- A candidate is strong in one area and the open work spans others.

Do not use for:
- writing the role's requirements: tailered-ai:ability-over-credential;
- choosing between candidates with a work sample: tailered-ai:work-sample-hire;
- writing the job post or pitch: tailered-ai:mission-pitch;
- an outsider's access to code, data or keys: tailered-ai:bring-in-the-builders;
- comparing agent setups: tailered-ai:agent-eval.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the open work, the candidates and their specialties, and the decision date.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `stretch-test.md`: work map, problems, rubric, scores with evidence, verdicts.

## Steps

Your reply leads with the score table (candidate, specialty score, stretch score, total), then the verdict line: hire, second test or no.

### 1. Map the open work

List the areas the hire would cover, such as modeling and the day build, with hours a week each (proposal). Mark each candidate's specialty.

Completion: every area with its hours, and each specialty marked.

### 2. Set two problems and the rubric

One problem in the specialty, one from the biggest area outside it: real company work, 90 minutes each (proposal), test data only, each with two harder follow-ups, such as a postponed game. No puzzles. Score four lines 0 to 3: answer, reasoning, follow-ups, self-checking. Pass mark 8 of 12 per problem (proposal), set before anyone sits it.

Completion: two problems with follow-ups, and a rubric with a pass mark dated before the first test.

### 3. Run and score the same way

Every candidate gets the same problems and time. Score each line with quoted evidence, the stretch problem separately from the specialty one.

Completion: two scores per candidate, every line with evidence.

### 4. Verdict

Hire, second test or no, per candidate, with the deciding scores. Passing only the specialty is no. The owner owns the decision; no offer, message or access goes out here. The hire's first live change goes through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: a verdict per candidate, and the decision left with the owner.

## Anti-Patterns

- Brainteasers or trick questions.
- Testing only the specialty.
- Writing the rubric after seeing the answers.
- Hiring on a good chat.

## Source and adaptation

Source: original Tailered AI skill, which cites Poundstone, How Would You Move Mount Fuji? (2003), and the New York Times's 2013 interview with Google's hiring head. No third-party skill text is copied.
