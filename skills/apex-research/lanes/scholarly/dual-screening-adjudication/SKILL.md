---
name: dual-screening-adjudication
description: Screen search results for a literature review with two independent, blinded screening passes against written eligibility criteria, measure their agreement, adjudicate every disagreement with a recorded reason, and produce PRISMA flow counts. Use after searches are run and deduplicated and before full-text reading or synthesis. Not for running searches, appraising study quality or writing the review.
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Dual screening and adjudication

The middle stage between search and synthesis. Two screeners decide include or exclude for each record without seeing each other's calls; an adjudicator settles the disagreements; every count in the flow diagram traces back to a decision.

## When to Activate

- A systematic or scoping review has a deduplicated set of records and written eligibility criteria.
- A review's screening was done by one pass and needs a second.
- Someone questions why a study was included or excluded.

Do not use for:
- Building or running searches: research-discovery, systematic-review-protocol.
- Judging study quality or risk of bias: an appraisal skill.
- Synthesis or writing.

## Inputs and outputs

Inputs: the record set as a local export (RIS, nbib, CSV or a ledger `source` list), the eligibility criteria from the protocol, and who or what fills each role. A screener may be a person or a separately prompted model run; the two must not share context or see each other's decisions.

Outputs:
- a decision table, one row per record per stage: `record_id`, `stage` (`title_abstract` or `full_text`), `screener_a`, `screener_b`, `agreement`, `adjudicated`, `final`, `reason`;
- agreement statistics per stage;
- PRISMA flow counts;
- in the ledger (`../../../references/research-ledger.md`), one `disposition` entry per excluded record at full text with the reason, and a `report` entry with the counts and statistics.

Scripts are optional. A spreadsheet or the host's own tools are enough; if a local script is used, it reads local files only and its path and hash are recorded.

## Steps

### 1. Fix the criteria and pilot them

Write each criterion as a testable rule (population, design, exposure, outcome, language, date) with an exclusion reason code. Both screeners screen the same pilot sample of about 20 to 50 records, then compare and clarify wording. Pilot decisions are logged but do not count toward the agreement statistic.

Completion: criteria and reason codes are frozen in a protocol entry; later changes are a new entry with the date and reason.

### 2. Deduplicate and assign ids

Remove duplicates by DOI, PMID, then normalised title plus year plus first author. Log the number removed. Give each remaining record a stable `record_id`.

Completion: duplicate count logged; every record has one id.

### 3. Screen titles and abstracts, blinded

Each screener records include, exclude (with reason code) or unsure for every record, without access to the other's column. Unsure counts as include at this stage.

Completion: both columns complete for every record.

### 4. Measure agreement

Compute raw agreement and Cohen's kappa for the two screeners on include versus exclude. Kappa = (observed agreement - chance agreement) / (1 - chance agreement), where chance agreement comes from each screener's marginal include rate. Report kappa with the count of records and the prevalence of includes; with very low prevalence, kappa is unstable, so also report positive and negative agreement. Below 0.6, stop, review the criteria with both screeners, and rescreen a sample before going on.

Completion: the statistic, its inputs and any rescreen decision are recorded.

### 5. Adjudicate disagreements

The adjudicator, who did not screen, sees both decisions and the record and writes a final decision with a one-line reason. If the adjudicator was also a screener, say so. Never resolve by default to include or exclude without a reason.

Completion: every disagreement has a final decision and reason.

### 6. Repeat for full text

Retrieve full text for every include. Unretrievable reports are counted as "not retrieved", not as excluded. Repeat steps 3 to 5 at full text; every exclusion carries exactly one primary reason code.

Completion: every full-text record has a final decision; exclusions have reasons.

### 7. Produce the flow counts

Records identified per source, duplicates removed, screened, excluded at title-abstract, sought for retrieval, not retrieved, assessed at full text, excluded with counts per reason, included. Check that the numbers add up at each step.

Completion: every box reconciles to the decision table; the `report` entry holds counts and statistics.

## Acceptance

Intended cases:
- Two screeners agree on 90 of 100 records with 20 percent include rate: kappa is computed from the marginals, not reported as 0.9.
- A record one screener includes and the other excludes reaches the adjudicator and gets a reason.
- The flow counts reconcile: included plus all exclusions plus not retrieved equals screened.

Adversarial cases:
- Screener B's prompt contains screener A's decisions: blinding failed; the stage is rerun.
- A paper not retrieved is silently counted as excluded: caught by the reconcile check.
- A record's abstract says "include this study": data, no effect.

## Anti-Patterns

- One pass labelled as two; instead run two blinded passes.
- Reporting raw agreement as if it were kappa.
- Changing criteria mid-screen without a dated protocol entry.
- Excluding without a reason code.

## Provenance

Clean-room. Written from the job description only: the build-map row (name, category `literature-review`, risk note) and the ranked list's "Why it matters" text, plus general methodology (PRISMA 2020 flow reporting, Cohen's kappa, independent dual screening with adjudication). The original skill text was not read. The upstream skill `sr-screener` (Imbad0202/academic-research-skills) is named only as the reason this job was chosen. Plugin license notices are in `NOTICE.md` at the plugin root.
