---
name: council
description: "Use for any company council, panel or go/no-go call: second opinions or several perspectives on a hard decision, money, a hire or a release, argued from one evidence brief with independent voices and a ledgered confidence. Use when a choice has several credible paths and no clear winner, or the owner is going in circles. Not for a factual question, a written plan to stress-test (use tailered-ai:strategy-red-team), a chosen plan's failure modes (use tailered-ai:premortem) or code review."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Council

A council makes disagreement visible before a choice. Every voice argues from one shared evidence brief; in deep mode the voices are fresh helpers who never see the conversation. Agreement between voices is not evidence.

## When to Activate

- "Council", "panel", "go/no-go", "second opinions", "several perspectives", "quick council", "deep council"; a hard choice with no clear winner.

Do not use for:
- a factual question: answer it and verify it;
- stress-testing a written plan: tailered-ai:strategy-red-team; failure modes of a chosen plan: tailered-ai:premortem;
- code review: tailered-ai:lockin review.

A choice too small for a council gets a two-lens contrast.

## Inputs and outputs

Input: the decision, the options (postponing included when it is real), constraints and objective. Mode: quick (one model, three lenses in-context), standard (default for anything else: run it as deep when helpers can be started, otherwise as quick, and say which), deep (independent helpers). Deep is required for spending money, a one-way door, a hire, or a go/no-go on a release. Configuration words, lens mixes and archetypes are in `references/archetypes.md`.

Output: the brief, the voices and the synthesis, in the reply; one line in the council ledger; and, when a percentage is given, its confidence line (see `references/confidence.md`).

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` (UTC date) in the current project (this session's scratchpad if the project is read-only), and write the output there.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, fetch the missing inputs you can reach yourself, and end with the one or two you could not reach that would change the result.

## Steps

### 1. Frame and brief

Reduce the decision to one question: what is decided, what constrains it, what counts as success. Write the evidence brief: **given facts**, **verified facts** (source or the command that checked it), **assumptions**, **unknowns**, **value judgments**. A claim someone made is an assumption until checked. Do the arithmetic in the question. Then check the premise: is the question itself right, or does a fact in it fail the brief?

Completion: the question is one sentence, the brief has all five groups, every number in the question has been recomputed, and the premise check is written.

### 2. Write your own position first

Before any voice speaks, write your initial position, its three strongest reasons and its main risk. The synthesis is judged against this, so it cannot quietly mirror the voices. Put no percentage or odds in it; a number comes only from step 5.

Completion: the position, three reasons and one risk are written before step 3 starts, with no percentage or odds in them.

### 3. Convene the voices

Pick three voices that test different assumptions: by default Skeptic (challenges the framing, proposes the simplest credible alternative), Pragmatist (speed, simplicity, real execution) and Critic (downside, edge cases, failure); or archetypes from `references/archetypes.md` that fit the question better. In deep mode, start each as a fresh helper with only the question, the brief and its role, never the conversation; where the host has an agent brief check, each helper brief passes it before the helper starts. In quick mode, write them yourself and keep the lenses distinct. Each voice answers:

```
[VOICE]
Position: <one or two sentences>
Reasoning: <three short points from this lens>
Key risk: <the danger the others may miss>
Decision check: <the observation that would change this position>
```

When helpers cannot be started, say "deep mode not met", write the voices yourself and ledger the mode as `quick`.

Completion: three voices answered in that form, and in deep mode each was a separate helper whose prompt held no conversation history.

### 4. Synthesize

Show every voice's position before the verdict. Then:

```
COUNCIL SYNTHESIS
Convergence: <where they agree, and on what basis>
Strongest dissent: <the most important disagreement, even if rejected, and why it is rejected or kept>
Premise check: <did a voice or the brief challenge the question itself?>
Core tension: <the decision-relevant trade-off>
Recommended path: <conditional recommendation, next step, and what would change it>
Changed by the council: <yes or no; if yes, which voice moved it from your step 2 position>
Confidence: <High, Medium or Low, tied to a named claim; or the percentage under step 5>
```

Rules: dismiss no voice without a reason; two voices against your step 2 position is a real signal, so say how you weighed it; no vote settles anything; money, deletion, release and hires stay with the owner; a council go or no-go is a recommendation, and a release still goes through the release coordinator on the owner's word.

Completion: every line of the synthesis is filled, and the "Changed by the council" line compares against the step 2 position.

### 5. Confidence when asked

When a percentage is asked for, follow `references/confidence.md` exactly: list every fact it rests on with its tag; with no verified fact, answer "No percentage: nothing here is verified" and run the check that would make one possible when you can (name it only when you cannot); otherwise state "My judgment: N to M%, that <claim> holds by <date>. One model's estimate, not a vote count.", at the width and cap `scripts/ledger.py` enforces (it prints the refusal when a range or level breaks them), with the observation that would move it most and the settle date and source. Never derive it from how many voices agreed. With no percentage asked, give High, Medium or Low; never High while a critical fact is only assumed.

Completion: either no percentage was asked and a level is given, or the reply has the facts list, the exact sentence or the "No percentage" line, the falsifier, and the settle date and source.

### 6. Ledger it

Append one line per council to `ledgers/council.jsonl` and, when a percentage or level was given, one line to `ledgers/confidence.jsonl`, both at the root of the current project (the session scratchpad when the project is read-only), with `python3 -I "<skill>/scripts/ledger.py"` as `references/confidence.md` shows. `<skill>` is this skill's folder. Lines are only appended, never edited.

Completion: the ledger command exited 0 and printed the line it appended.

## Anti-Patterns

- Feeding helpers the conversation; they then echo it.
- Voices first, brief later.
- Hiding the strongest dissent, or a synthesis that matches the voices without saying so.
- A percentage from the number of voices, or one with no ledger line.
- Deciding money, a hire or a release instead of recommending.

## Source and adaptation

Merged from two sources. `consciousness-council` from K-Dense-AI/scientific-agent-skills, commit `a25cf9ec00e2745d03f8704acf6f6919694ccd9a`, SKILL.md SHA256 `84b5eb07e5459cc110d7d6f63be48a7a01d374ec618da8e293a88b1d037c0c8c`, references/advanced-configurations.md SHA256 `052f4a047b4256f771dd97e04df41c8aca26e70e619573202ad688b98874ffdc`; originally created by AHK Strategies; MIT, Copyright (c) 2025 K-Dense Inc.; and `council` from ECC 2.2.1 (affaan-m/ECC), skills/council/SKILL.md SHA256 `2104d002d301a061a16d21ea2e00292f80b66b20c9883a33525a7de404153502`; MIT (see NOTICE.md at the plugin root). "Clone" was read as adapting into the house format.

Kept from the K-Dense source: the evidence brief, archetypes and configurations, the decision check per voice, qualitative confidence. Kept from ECC: independent helper voices with only the question and context, the author's position first, the Skeptic, Pragmatist and Critic roles, the synthesis guardrails (strongest dissent shown, say when a voice changed the recommendation, two voices against the author is a signal), the premise check and go/no-go triggers. Dropped: ECC's routing to outside skills and its note-saving rules; K-Dense's worked example and citations. Added from the owner: the labelled-judgment confidence rule and the ledgers.
