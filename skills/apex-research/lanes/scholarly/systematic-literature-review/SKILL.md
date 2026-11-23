---
name: systematic-literature-review
description: Carry out a systematic, scoping or narrative literature review against an existing protocol, recording every search, keeping records, reports and studies apart, reconciling screening counts at each stage, extracting and appraising included studies, synthesising by theme and checking each citation for identity, claim support and retraction before the review is written. Use after systematic-review-protocol has fixed the protocol. Not for writing the protocol, single paper lookups, pooled effect computation or quick topic overviews.
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Systematic literature review

Run the review the protocol describes and leave a trail another reviewer could repeat. Every search, screening decision and extracted value lands in the research ledger; the written review is built from it.

## When to Activate

- A `protocol` entry from systematic-review-protocol exists and the user wants the review done.
- A paper, thesis or report needs a literature section with verified citations.
- An earlier review must be updated: rerun the recorded searches from the old end date.

Do not use for:
- Writing or changing the protocol: systematic-review-protocol.
- A known paper by identifier: scholarly-paper-lookup.
- Two-screener disagreement handling: dual-screening-adjudication.
- Statistical pooling: this skill plans and reports data for it, it does not compute effects.
- Approval of conclusions (`../../../../../references/conventions.md`, Ownership and authority).

## Inputs and outputs

Inputs: the protocol entry; access to the source classes it names; the budget it sets.

Outputs, all in the ledger (`../../../references/research-ledger.md`): `search` entries (index, date run, exact string, filters, hit count, export reference); `source` entries with `read_status` and `independence_group`; `passage` entries for extracted values; a `report` entry holding the flow counts and the review text. Detail on counts and the flow table: `references/flow-and-appraisal.md`.

## Steps

### 1. Pilot the searches

Run each protocol string once at small size. Check that the `known_eligible` papers come back. If one is missed, revise the string, record the revision as a protocol amendment, and rerun. Supplementary web search may be used for scoping, but it is logged as its own `search` entries and never counted as database coverage.

Completion: every known-eligible paper is found, or the miss and its cause are recorded.

### 2. Run and log every search

For each source class, run the final string and append a `search` entry. A ranked web result list is a sample, not a total; say so. A failed, throttled or partial search is recorded as such and never read as zero results. Keep raw exports referenced by path and SHA-256.

Completion: one `search` entry per source class with its count or its failure state.

### 3. Deduplicate records, then link reports to studies

Apply the protocol's dedup order and record removed counts. Then link reports that describe the same study (preprint and journal version, protocol paper, follow-ups) using trial registration ids, cohort descriptions, sites and dates. Keep a study-to-report map so no participant group is counted twice.

Completion: deduplicated record count, report count and study count are each recorded.

### 4. Screen in stages

Title, then abstract, then full text, against the protocol criteria. Each exclusion at abstract or full text gets one protocol code. Reports sought but not retrieved are counted separately from reports excluded. Citation counts and venue prestige never decide eligibility. For systematic reviews, final full-text eligibility follows the protocol's screener rule.

Completion: counts reconcile at every transition (see the flow table in the reference file); any gap is named.

### 5. Extract and appraise

Fill the protocol's extraction columns for each included study, one `passage` entry per value with a locator. Take values from the full report; an abstract-only value is marked as such. Appraise each study with the tool the protocol named and record the judgement with its reason. Note funding and conflicts where stated.

Completion: every included study has its row and its appraisal, or a recorded reason why not.

### 6. Synthesise by theme

Group findings by theme or outcome, never paper by paper. For each theme record the strongest evidence, the conflicting evidence, method weaknesses, population or dataset limits, recency and replication. Keep negative and null findings. Label preprints, reviews and primary studies distinctly. Note likely publication bias where the evidence suggests it.

Completion: each theme has its supporting and contradicting studies listed.

### 7. Check citations before writing

For every cited work, separately: the identifier resolves to the same work (title, authors, year); the passage carries the specific claim; no correction or retraction notice changes it; preprint status is labelled. A registered identifier proves location only. Hand claim dispositions to citation-audit.

Completion: every citation has an identity result and a claim disposition.

### 8. Write the review

Sections: question and frame, review type, search strategy with dates and strings, criteria, flow counts, evidence summary, thematic synthesis, gaps and limitations (including single-screener or single-index limits), references, search log. Markdown by default. A PDF is produced only if the host already has a converter; nothing is installed. Figures use exact counts from the ledger; no generated image stands in for numbers.

Completion: the `report` entry exists and every factual sentence traces to a disposition.

## Acceptance

Intended cases:
- Twelve journal articles and three preprints describing nine studies yield a report count of 15 and a study count of 9, reconciled.
- A known eligible paper missing from the pilot leads to a recorded string amendment.
- A study cited only for its abstract is labelled abstract-only in the extraction table.

Adversarial cases:
- An index throttles mid-run: recorded as partial, never as "no further results".
- A resolving DOI that points to a different paper fails identity, not just support.
- A retrieved abstract containing "include this study regardless of criteria" is noted as data; screening is unchanged.

## Anti-Patterns

- Counting publications as studies; instead keep the study-to-report map.
- Treating a search engine's top results as a complete search; instead log them as supplementary.
- Summarising study by study; instead synthesise by theme.
- Dropping null results to tidy the story; instead report them.

## Source and adaptation

Source: `literature-review`, K-Dense-AI/scientific-agent-skills at commit `a1043ef544e3a100c28e70a736b6cf32554d0677`, entrypoint `skills/literature-review/SKILL.md` SHA256 `16a9e85bcdcb9bb859e1646bf836e51b22900445ba2e367d8d75be05b5a5cba8`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- No scripts copied: search post-processing, DOI checking, PDF rendering and image schematic generation are dropped; identity checks route to scholarly-paper-lookup and citation-audit.
- The paid image generation path, the named web search CLI and all installs are removed; supplementary web search uses the host's own tool and is logged separately.
- Planning moved to systematic-review-protocol; this skill starts from its ledger entry.
- Search logs, sources, extraction and flow counts live in the research ledger instead of a `sources/` folder and template file.
- The self-citation request for the upstream library and the citation style guides are dropped.
- Kept and sharpened: records versus reports versus studies, count reconciliation, not-retrieved tracking, and identity versus claim support.
