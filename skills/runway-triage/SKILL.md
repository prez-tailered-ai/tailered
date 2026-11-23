---
name: runway-triage
description: "Use when cash or runway is short; when two efforts both need money and there is only enough for one; when the owner says we're near the end, all in, or asks what keeps us alive; or before a decision that spends the last months of cash. Not for capping one experiment; use tailered-ai:capped-experiment. Not for finding idle spend; use tailered-ai:find-it-inside. Not for a trade-off years out; use tailered-ai:long-term-letter."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Runway triage

In 2008 Musk put his remaining money into SpaceX and Tesla when both were near failure. Falcon 1 reached orbit on its fourth flight, and both companies had new money by the end of the year. The guard: he reportedly ended that year with almost no personal cash and borrowed for living costs. This skill plans the company's cash. Putting in personal money is the owner's own decision; the skill never recommends it and gives no personal investment advice.

## When to Activate

- Cash or runway is short.
- Two efforts both need money and there is enough for one.
- The owner says "we're near the end", "all in" or "what keeps us alive".
- A decision would spend the last months of cash.

Do not use for:
- capping one experiment's loss: tailered-ai:capped-experiment;
- finding idle or duplicate spend: tailered-ai:find-it-inside;
- a trade-off whose payoff is years out: tailered-ai:long-term-letter.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: cash on hand, monthly spend, money expected and how certain it is, and the efforts competing for cash.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `triage.md`: months of runway, the uncounted money, the one proof point, the keep, pause or stop list with savings, and the trigger dates.

## Steps

### 1. Count the months

Months of runway = cash on hand divided by monthly spend. Count only money that has arrived. Money promised but not signed goes on a separate list and is not counted.

Completion: months of runway from cash in hand, and the list of uncounted money.

### 2. Name the one proof point

Name the single result, with a number and a date, that would make the company fundable or self-paying: paying members, a graded public record, a signed partner. Name its owner.

Completion: one proof point with a number, a date and an owner.

### 3. Keep, pause or stop each effort

Mark each effort keep (it moves the proof point), pause (it can wait without loss) or stop. Do not split cash evenly so that nothing gets enough. Show the monthly saving from each pause or stop and the new runway.

Completion: every effort marked, with savings and the new months of runway.

### 4. Set the triggers

Write a check date for the proof point and a cash floor, for example three months of spend, at which the owner decides on deeper cuts, outside money or winding down. Personal money is not an input or an option on this sheet. Nothing is cancelled, spent or sent from here. A live change goes through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: a check date, a floor in months, and the decision left with the owner.

## Anti-Patterns

- Counting money that has not arrived.
- Splitting cash evenly so nothing gets enough.
- Treating the founder's own savings as the plan.
- Keeping the cash floor from the owner.

## Source and adaptation

Source: original Tailered AI skill, which cites SpaceX's 2008 Falcon 1 launch record, the NASA resupply contract of December 2008, reported accounts of Tesla's December 2008 financing, and Ashlee Vance's Elon Musk (2015). No third-party skill text is copied.
