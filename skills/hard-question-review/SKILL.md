---
name: hard-question-review
description: "Use when a technical plan or spec for the model, the day build, the odds readers or the publishing step asks for build time; when the owner says review this plan, poke holes or grill the design; or when a session will build from a plan nobody questioned. Not for the owner learning the figures to explain them; use tailered-ai:know-the-numbers. Not for writing the case for a change; use tailered-ai:memo-not-slides."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Hard-question review

Gates wrote Altair BASIC with Paul Allen in 1975 and kept reading the details as CEO; his product reviews were reported to probe plans line by line. The practice: question a technical plan hard before it gets build time. The guard: those reviews were also reported as harsh on people. Question the plan, never the person, in one sitting, so the review is no bottleneck.

## When to Activate

- A plan for the model, the day build, the odds readers or the publishing step asks for build time.
- The owner says "review this plan", "poke holes" or "grill the design".
- A session is about to build from a plan nobody has questioned.

Do not use for:
- The owner learning the figures to explain them: tailered-ai:know-the-numbers;
- writing the case for a change: tailered-ai:memo-not-slides;
- reviewing one finished diff: tailered-ai:lockin.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the plan, its author, and the decision date.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `review.md`: the plan's key numbers, the questions with evidence, the open risks, and the verdict.

## Steps

Your reply leads with the question table (question, plan line, evidence, answered or open), then the verdict line: build, change or stop.

### 1. Read it to the detail

Read the plan and the files it changes. List its key numbers: games per day, run time, cost, accuracy target, leagues. A missing number becomes a marked proposal.

Completion: the plan's numbers listed, each sourced or marked proposal.

### 2. Ask the hard questions

Write three to ten questions on what would break: a postponed game, a market with no price, ten times the games, testing, numbers already published. Each names its plan line. None is about the author.

Completion: three to ten questions, each tied to a plan line.

### 3. Answer from evidence

Answer each from code, data or a quick check, never the author's confidence. Mark each answered or open. Cap the sitting at 90 minutes (proposal); open questions return to the author with a date.

Completion: every question answered with evidence, or open with a date.

### 4. Verdict and route

Verdict: build, change or stop, with the owner who builds and the date. Build means work in a copy. Anything that goes live goes through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict, the owner, the date and the route.

## Anti-Patterns

- Questions about the person instead of the plan.
- Accepting "it should be fine" as an answer.
- A review with no end time.
- Approving a plan whose only test is "we will watch it".

## Source and adaptation

Source: original Tailered AI skill, which cites Altair BASIC (1975), Joel Spolsky's 2006 account of a BillG review, and reported accounts of Gates's review style. No third-party skill text is copied.
