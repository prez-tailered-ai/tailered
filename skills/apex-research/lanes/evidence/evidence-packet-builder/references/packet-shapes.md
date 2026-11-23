# Packet shapes

Every file is rebuilt from research-ledger entries. Each row carries the ledger `entry_id`s it came from. Empty means not stated by the source; nothing is inferred to fill it.

## references.json: one record per unique reference

`reference_id` (`ref-001` ...), `source_id` (DOI, PMID, arXiv id or canonical URL), `title`, `authors`, `year`, `venue`, `url`, `doi`, `pmid`, `publication_type`, `study_design`, `population_or_system`, `sample_size`, `methods`, `intervention_or_exposure`, `comparator`, `outcomes`, `key_findings`, `quantitative_findings` (with uncertainty), `limitations`, `preprint`, `retracted`, `corrected`, `read_status`, `retrieval` (`excerpt`, `search_only`, `failed`), `evidence_label` with its rationale, `sections` (introduction, methods, discussion), `excerpt_entry_ids`.

`evidence_label` is a transparent heuristic for prioritising reading (`high`, `moderate`, `contextual`, `low`, `exclude`). It is not an appraisal; evidence-quality-review does that.

The bibliography file is generated from these records; run citation-registry-check on it before use.

## evidence-matrix.json

One row per reference: design, population, exposure, comparator, outcomes, main numbers, limitations, label.

## claim-source-map.json

One row per proposed claim: `claim_id`, claim text, `claim_kind`, `reference_ids`, up to two `passage` entry ids, `status` (`single_source`, `multi_source`, `conflicting`, `unsupported`). Independence is judged later by citation-audit, not here.

## synthesis.json

`consensus_candidates`, `conflicts`, `methods_patterns` (designs by count), `gaps`. Each item names reference ids.

## section-briefs.json

`introduction` (background, importance, open gap), `methods_rationale` (precedent for measures, protocols, models, analyses, never invented details of the user's study), `discussion` (agreeing and conflicting work, mechanisms, limits, future work). Each brief lists reference ids and candidate findings. There is no results brief.

## coverage.json

`target`, `unique_references`, `retrieved_references`, `shortfall`, `label_mix`, `retrieval_mix`, `years`, `scholarly_sources`, `preprints`, `retracted_or_withdrawn`, `unresolved_urls`, `limitations`.

## search-log.json

Per pass: objective, queries, filters, mode, time, result count, backend or fallback, warnings, and the ledger `search` entry id.
