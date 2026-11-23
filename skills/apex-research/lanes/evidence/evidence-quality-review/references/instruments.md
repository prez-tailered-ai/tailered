# Instruments, biases and pitfalls

Versions as documented upstream on 2026-10-01. Use the current official document for a formal assessment and record version, date, result assessed, signalling answers and reasons.

## Which instrument answers which question

| Question | Design | Instrument | Unit |
|---|---|---|---|
| Is this result biased? | randomised trial (individual, cluster, crossover variants) | RoB 2 | one result: outcome, time point, comparison, estimate, assignment or adherence effect |
| | non-randomised intervention study | ROBINS-I 2016, or ROBINS-I V2 (November 2025, still a draft) | one result; never mix the two versions |
| | diagnostic accuracy | QUADAS-3 (tool v1.2, 2026) | one accuracy estimate |
| | cohort or case-control | Newcastle-Ottawa forms | study; no universal star thresholds |
| | various | CASP checklist for the design | study |
| | physiotherapy trials | PEDro scale | study; not equivalent to RoB 2 |
| How trustworthy is this review? | systematic review of interventions | AMSTAR 2 | review; critical domains decide, not a sum |
| How sure are we across studies? | body of evidence | GRADE | one outcome and comparison |
| Was it reported? | trial results; protocols | CONSORT 2025; SPIRIT 2025 | report |
| | observational | STROBE | report |
| | systematic review | PRISMA 2020 | report |
| | diagnostic accuracy | STARD 2015, STARD-AI extension | report |
| | interviews, focus groups | COREQ | report |
| | case reports | CARE | report |

Reporting checklists do not certify conduct or quality. A recommendation needs a separate evidence-to-decision step with context; certainty alone does not set its direction or strength.

## GRADE in brief

Start high for randomised evidence and low for observational evidence, unless the chosen approach for non-randomised studies says otherwise. Rate down for risk of bias, inconsistency, indirectness, imprecision and publication bias; rate up for large effect, dose-response, or plausible confounding that would reduce the effect. Grades: high, moderate, low, very low. Judge certainty relative to a stated threshold or range, give absolute effects where possible, and do not count one problem twice.

## Biases to check

Selection (sampling, allocation, healthy-user, survivorship, collider), confounding (by indication, time-varying), measurement (recall, observer, misclassification, detection), performance and attrition, reporting and publication (selective outcomes, spin, small-study effects; funnel asymmetry has other explanations and needs about ten studies), and analyst choices (flexible analysis, subgroup fishing, stopping rules).

## Statistical pitfalls

- A p-value is not the probability a hypothesis is true and says nothing about importance.
- Non-significance is not evidence of no effect; check whether the interval excludes important effects.
- Multiplicity without a stated family and correction.
- Pseudo-replication: repeated measures or subsamples treated as independent units.
- Observed or post-hoc power; overlapping intervals used as a test.
- Correlation read as causation; regression to the mean; ecological inference.
- Relative effects without baseline risk; change-from-baseline misuse.
- Causal claims without a defined estimand and defended exchangeability, positivity and consistency.
- Meta-analysis pooling incompatible designs or ignoring heterogeneity.
