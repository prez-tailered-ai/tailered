---
name: market-sizing
description: Size a market as total, serviceable and obtainable figures computed both from a published total downward and from customer counts and prices upward, report the gap between the two instead of averaging it away, plan a survey sample that holds for each reported segment with the finite-population correction, and score candidate segments on five usefulness criteria with size and reachability as hard gates. Every number carries its method, assumptions and confidence. Use when someone asks how big a market is, how many survey responses they need, or which segments are real. Not for live campaign measurement, pricing, positioning or competitor comparison.
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Market sizing

Method and assumptions are the deliverable. A market size is never one unsourced number, a survey is never powered only in total, and a demographic slice is not a segment until it is big enough and reachable.

## When to Activate

- "How big is this market?" for a board, an investor memo or a go or no-go decision.
- A survey is about to be fielded and needs a sample size.
- A list of candidate segments needs sorting into real markets and slices.

Do not use for:
- Comparing competitors' products: competitor-teardown.
- A research-backed decision memo on a market: decision-market-research.
- A full market report layout: market-report-scaffold.
- Campaign attribution, pricing or positioning: out of scope.

## Inputs and outputs

Inputs: the decision the numbers inform and who makes it; the precision it needs (order of magnitude, about 20 percent, about 5 percent); the market profile (business software, consumer, large enterprise, marketplace, hardware, services); sizing inputs with sources; for a survey, population, confidence, margin of error, expected proportion and segments to report; candidate segments with evidence.

Outputs: a brief following `references/sizing-methods.md` (brief layout), in chat or as a local Markdown file. Where inputs come from research, their `source` and `passage` entries are in the research ledger (`../../../references/research-ledger.md`) and each input cites them. All arithmetic is shown so a reader can redo it.

## Steps

### 1. Fix the decision

Ask, one at a time: what decision this drives and at what precision; whether both sizing methods will be run (the answer should be yes). Settle these before any numbers.

Completion: decision, decider, precision and profile are written in the brief.

### 2. Size from the top

Start from a published total for the category, with its source and date. Apply a serviceable fraction (geography, segment, product scope) and a reachable share for the planning window. Each fraction is an assumption with a source or the label `unverified planning assumption`.

Completion: total, serviceable and obtainable from the top, with every factor sourced or labelled.

### 3. Size from the bottom

Count potential customers (with source) times annual price, then the serviceable fraction and a realistic adoption rate. This forces named counts and prices.

Completion: the same three figures from the bottom, every factor sourced or labelled.

### 4. Reconcile

Report both, and the gap as a fraction of the larger. If the gap exceeds the decision's tolerance, say triangulation failed and name the assumption most likely to explain it; do not average. Round to the precision the decision needs.

Completion: both figures, the gap, a pass or fail against tolerance, and rounded headline numbers.

### 5. Plan the survey (if primary data)

Compute the sample per `references/sizing-methods.md`: base size from confidence, expected proportion (0.5 when unknown) and margin; correct for a finite population; then compute the floor for each segment to be reported, and size the survey to the segment floors. Name coverage, non-response and wording risks, and check every question for leading or two-in-one wording.

Completion: overall size, per-segment floors and the risk list.

### 6. Score segments

Score each candidate on measurable, substantial, accessible, differentiable and actionable. Substantial and accessible are gates: failing either means drop. Verdict per segment: target, watch or drop, with the reason. Prefer needs-based segments with a measurable proxy you can target.

Completion: every segment has scores, gate results and a verdict.

### 7. Assemble

Fill the brief: objective, sizing, survey plan, segments, any competitive context from public, ethically obtained sources, the assumptions register and an overall confidence (high, moderate, low) with its reason.

Completion: every number in the brief has method, assumptions and confidence beside it.

## Acceptance

Intended cases:
- A software market sized at about 1.5 billion from the top and 0.9 billion from the bottom: a 40 percent gap fails a 20 percent tolerance and the brief says which fraction to check.
- Three segments reported at plus or minus 8 percent each: the survey is sized to about 150 per segment, not to an overall figure.
- "Solo founders who might want analytics" fails the substantial gate and is dropped.

Adversarial cases:
- The user wants "just one TAM number for the deck": both methods are still shown, with a rounded headline.
- An input says "1 percent of a 40 billion market": flagged as the percent-of-a-big-number fallacy until a bottom-up check exists.
- A segment list double counts overlapping groups: flagged and the overlap removed before summing.

## Anti-Patterns

- One number with no method; instead show both directions.
- Four significant figures on order-of-magnitude inputs; instead round to the decision.
- Powering only the total; instead fund each segment floor.
- Averaging a failed triangulation; instead report the gap.

## Source and adaptation

Source: `market-research`, alirezarezvani/claude-skills at commit `19392f7a08264ed00486a251f5b2098321771f94`, entrypoint `research-ops/skills/market-research/SKILL.md` SHA256 `0e4037294f8e6bea1cb53de035eaa97bd2d74349d06f9b61d85f4420d7c084c9`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- The three calculators are not copied; their formulas and gates are written out in `references/sizing-methods.md` and the arithmetic is shown in the brief.
- The onboarding questionnaire and its saved config files in the home or project folder are dropped; defaults are asked per run.
- The opt-in automatic optimisation loop is removed (Bounded execution: no recursive or repeated rounds).
- Neighbouring upstream skills are replaced by the company siblings; named analyst firms and investors are left as general method references.
- Kept: both-direction sizing with triangulation, Fermi decomposition, fallacies, sample sizing with the finite-population correction and segment floors, total survey error, the five segment criteria with two gates, the forcing questions and the brief layout.
