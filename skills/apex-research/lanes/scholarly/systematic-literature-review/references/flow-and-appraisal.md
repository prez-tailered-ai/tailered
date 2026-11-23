# Flow counts and appraisal

Detail for steps 3 to 5 of systematic-literature-review.

## Flow table

Record each row in the `report` entry. Every row after the first must be derivable from the rows above it; if it is not, the gap is named in the review's limitations.

| Row | Meaning | Check |
|---|---|---|
| identified | records returned, per source class | sum of `search` entry counts |
| removed before screening | duplicates, plus any automation or other removals with reasons | identified minus this equals screened |
| screened | records at title and abstract | |
| excluded at screening | by exclusion code | screened minus this equals sought |
| reports sought | full texts requested | |
| not retrieved | sought but unavailable, with reason | sought minus this equals assessed |
| assessed | full texts read for eligibility | |
| excluded at full text | by exclusion code, counted per code | assessed minus this equals included reports |
| included reports | | |
| included studies | from the study-to-report map | may be fewer than included reports |

Updated reviews add a row for studies carried over from the earlier version.

## Study-to-report map

One line per study: a study id, the trial registration or cohort identifier if any, and each report's `source_id` with the outcomes it supplies. When two reports give the same outcome, record which one is used and why (later follow-up, full report over abstract, peer-reviewed over preprint).

## Appraisal tools by design

Name the tool in the protocol; record its judgement per study with the reason.

| Design | Tool family |
|---|---|
| randomised trials | a risk-of-bias tool for randomised trials, domain by domain |
| non-randomised interventions | a risk-of-bias tool for non-randomised studies |
| diagnostic accuracy | a diagnostic-accuracy quality tool |
| systematic reviews being cited | a review-quality checklist |
| technical or benchmark papers | dataset leakage, baseline fairness, seeds and variance reported, code and data availability |

Certainty across a body of evidence uses the four certainty grades (see citation-audit), never a study count.

## Citation identity check

For each cited identifier, record: resolved (yes, no, inconclusive); title, first author and year match (yes or the mismatch); correction or retraction notice found (yes, none found in the sources checked); preprint (yes or no, and the published version if one exists). A throttled or failed lookup is inconclusive, not evidence of fabrication. "None found" is scoped to the sources checked.
