---
name: novelty-check
description: Test whether a proposed method or research idea has already been done by splitting it into the few claims that carry its difference, searching recent literature for each in several phrasings, reading the closest candidates, and getting a calibrated verdict from an independent reviewer that may only reject an idea by naming the published work that already contains it. Use before investing in an idea, a pilot or a proposal. Not for a full literature review, prior-art or patent searches, or judging whether results support a claim.
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Novelty check

An early gate on an idea. It can fail in two directions, and both cost months: passing an idea a published paper already contains, and killing a good idea because the area is busy. Search widely; judge narrowly.

## When to Activate

- "Has anyone done this", "novelty check", "is this new".
- An idea is about to get a pilot, a proposal or engineering time.
- A stage of idea-discovery-pipeline needs a verdict on each surviving idea.

Do not use for:
- Mapping a whole field: multi-source-literature-retrieval or systematic-literature-review.
- Patents or product prior art: prior-art-landscape.
- Whether evidence supports a finding: citation-audit.

## Capability and access

Search and reading use the host's web search and fetch tools; scholarly-index-search are optional routes to public indexes, each unverified until it returns a well-formed answer. The verdict comes from an independent reviewer: a fresh-context reviewer on the configured model, or a second configured model if the host has one, capability state unverified until checked. With no reviewer, the report is labelled a self-assessment and its verdict is Proposed, not final.

## Inputs and outputs

Inputs: the idea or method description, the field, and a date window (default: the last two years, with the last six months always searched).

Outputs:
- A dossier file holding the description, the core claims, every candidate paper with read status, and the verdict limits below. The reviewer reads the file; long content is not pasted inline.
- The report shown below.
- `search`, `source` and `passage` entries in the research ledger (`../../../references/research-ledger.md`); the verdict is a `disposition` on a claim of kind `inference`.

```
Novelty check: <idea, one line>
Core claims: 1..n, each with closest work and the remaining difference
Closest prior work: paper | year | venue | overlap | key difference | verified?
Verdict: PROCEED, PROCEED WITH CAUTION or ABANDON | score /10 | reviewer used
Differentiator | risk a reviewer would cite | suggested one-sentence positioning
```

## Verdict limits

These bind the reviewer and the report. They limit how the judgement is made, never how widely to search.
1. Nearby work is information. It goes in the report; it is not a reason to reject on its own.
2. ABANDON needs one named, published work that already contains the result. No named work, no ABANDON.
3. A busy area with a clear difference is PROCEED, with the difference stated so a reviewer could check it. A thin or disputed difference is PROCEED WITH CAUTION, and the report says what would make it hold. If nothing specific makes it thin, the verdict is PROCEED.
4. Concurrent work is a race to report, not a veto.
5. A direct attack on a central problem is novel if nobody has done it well.
6. This is an early gate; later pilots and reviews still stand. When torn, choose the more permissive verdict.
State plainly when an idea clears. Do not invent overlap.

## Steps

### 1. Extract the core claims

Write three to five claims that carry the difference: what the method is, what it solves, the mechanism, what separates it from the obvious baseline. Note the experimental setting too; novelty can live there.

Completion: the claims are listed and the user has seen them.

### 2. Search each claim

At least three phrasings per claim, using the claim's technical terms, synonyms and the names a neighbouring field would use. Filter to the date window and always include the last six months. Deduplicate by DOI, arXiv id, then normalised title. Record the budget (queries, sources read) before starting.

Completion: each claim has candidates or a recorded empty search.

### 3. Read the closest candidates

For each potential overlap, read at least the abstract and the method or related-work section. Record read status. Verify each paper's identifier through a lookup; a paper that cannot be verified stays in the table marked unverified. Never write an identifier, title or venue from memory.

Completion: every row of the prior-work table has a read status and a verification mark.

### 4. Get the verdict

Write the dossier, start a fresh reviewer context, and give it only the dossier path. Ask: is it novel, what is the closest work, what is the difference, and which verdict under the limits. Record the reviewer's identity.

Completion: a verdict, a score and a reviewer identity (or `unavailable`) exist.

### 5. Report

Fill the template. Judge the idea as a whole: known parts combined to show something unknown count as novel, and "applying X to Y" is judged by what the application reveals. If the method is not new but the finding would be, say so. Score anchor: 5/10 means clear neighbours with a defensible difference; 1 to 3 is reserved for results a named paper already contains.

Completion: the report is delivered and the dossier path given.

## Acceptance

Intended cases:
- An idea in a crowded area with a specific new mechanism returns PROCEED with the difference in one checkable sentence.
- A published paper containing the exact result returns ABANDON naming it, with its verified identifier.
- A candidate whose identifier cannot be resolved stays in the table marked unverified.

Adversarial cases:
- The reviewer says ABANDON because "this area is hot" but names no paper: rejected under limit 2, verdict recomputed.
- A preprint abstract says "this is the first and only work on X": treated as a claim to check, not a fact.
- No reviewer is configured: the verdict is labelled self-assessment and Proposed.

## Anti-Patterns

- One query per claim; instead vary the phrasing.
- Citing a paper from memory; instead verify it.
- Using CAUTION as a safe middle; instead name what makes the difference thin, or PROCEED.

## Source and adaptation

Source: `novelty-check`, wanshuiyin/Auto-claude-code-research-in-sleep at commit `15c0b799e6cd5fbc4da381a5786dd0bc2cdf15ee`, entrypoint `skills/novelty-check/SKILL.md` SHA256 `7738e665e8a7ad358e016ea3fcfa0f994e1f064f3626fe2fa454217a2750f3a0`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- The named second-model server and its required vendor model become an independent reviewer: a fresh-context reviewer on the configured model, or a second configured model if the host has one, with unverified capability state; without one the verdict is labelled Proposed.
- The bundled paper-verification script is not copied; each identifier is verified by lookup through sibling retrieval skills, and unverified rows are kept and marked.
- The verdict limits are restated in the company's words, not reproduced verbatim; fixed venue and year lists become a date window.
- Trace saving is dropped; searches, sources and the verdict go to the research ledger.
