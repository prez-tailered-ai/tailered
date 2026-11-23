---
name: outcome-per-dollar
description: "Use when the company gives something away or funds a cause, such as a donation, a free tier, a free tool or a responsible-gambling program; when the owner asks did it work or how do we measure giving; or when a giving report counts dollars or sign-ups, not results. Not for member sign-up and retention numbers; use tailered-ai:activation-number. Not for checking whether green metrics are real; use tailered-ai:day-one-check."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Outcome per dollar

The Gates Foundation judges giving by outcomes, such as child deaths prevented, in its annual letters and Goalkeepers reports. The practice: judge every gift by what changed per dollar, not by dollars given. The guard: Gates's 2009 annual letter said the small-schools push had not raised college readiness as hoped. Measure early and change course.

## When to Activate

- the company gives something away or funds a cause: a donation, a free tier, a free tool, a responsible-gambling program or a grant.
- The owner asks "did it work" or "how do we measure giving".
- A giving report counts dollars or sign-ups, not results.

Do not use for:
- member sign-up and retention numbers: tailered-ai:activation-number;
- checking whether green metrics are real: tailered-ai:day-one-check;
- setting member prices: tailered-ai:price-on-value.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the program, its spend in dollars and hours, and its goal.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `outcome.md`: outcome, baseline, cost per outcome, check, verdict.

## Steps

Your reply leads with the outcome table (program, dollars and hours, outcome, cost per outcome, baseline), then the verdict line: keep, change or stop.

### 1. Name the outcome

Name the one result the program is for, as a number that changes. For a donation, use the charity's own reported result, such as meals served; for a free tier, free users who become members within 60 days. Dollars, posts and sign-ups alone are not outcomes.

Completion: one outcome number with its definition and source.

### 2. Set the baseline and the cost

Record the number before the program, or a comparison group, and the total cost in dollars and hours. Divide to get cost per outcome. Mark estimates as proposals.

Completion: a baseline, a total cost and a cost per outcome.

### 3. Check early

Set the first check at 30 days (proposal) with a target. Name the owner who measures it and, for a partner's result, the report it comes from.

Completion: a check date, a target and an owner.

### 4. Verdict and route

Keep, change or stop, with the deciding number. A miss at the check means change or stop; money already spent is no reason to go on. The owner decides any money; nothing is paid, donated or posted from here. A public post waits for the measured number and goes through tailered-ai:story-not-ads; a live page change goes through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict, the number, the owner and the route.

## Anti-Patterns

- Reporting dollars given as the result.
- No baseline.
- Waiting a year for the first check.
- Posting a result before it is measured.

## Source and adaptation

Source: original Tailered AI skill, which cites Gates Foundation annual letters, the Goalkeepers report (from 2017), and Gates's 2009 annual letter. No third-party skill text is copied.
