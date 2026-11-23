# Per-database search syntax

Detail for step 3 of prisma-literature-review. Each database is an optional backend whose capability state is unverified until a call in this session returns a well-formed answer. Syntax changes; check the database's own help page before a final run and record the date checked. Calls and shape checks follow scholarly-paper-lookup.

## Rendering one logical string

Logical form: `(A1 OR A2 OR A3*) AND (B1 OR "B2 phrase") AND (C1 OR C2)`, plus date, language and type limits.

| Database | Field restriction | Controlled terms | Truncation | Boolean | Date limit | Known losses |
|---|---|---|---|---|---|---|
| biomedical bibliographic index (PubMed) | `[tiab]`, `[ti]`, `[au]`, `[pt]`, `[la]` | `[mh]` explodes to narrower headings; `[mh:noexp]` does not; `[majr]` for major topic | `term*`, needs a stem of four letters or more | AND, OR, NOT in capitals; brackets group | `2015:2024[dp]` | a quoted or tagged term turns off automatic term mapping, so add the heading yourself |
| full-text biomedical index (Europe PMC) | `TITLE:`, `ABSTRACT:`, `AUTH:` | subject heading fields exist; check names in help | `term*` | AND, OR, NOT | `PUB_YEAR:[2015 TO 2024]` | full-text matches inflate counts; restrict to title and abstract for parity; `SRC:"PPR"` limits to preprints |
| physics, maths, CS preprints (arXiv) | `ti:`, `abs:`, `au:`, `cat:`, `all:` | category codes only | do not rely on wildcards; spell out variants | AND, OR, ANDNOT | `submittedDate:[YYYYMMDDHHMM TO YYYYMMDDHHMM]` | an unknown prefix silently searches all fields |
| biology and health preprint servers (bioRxiv, medRxiv) | none | none | none | none | browse by date interval | no keyword search; browse the window and filter locally, or use the full-text index's preprint source |
| broad cross-discipline index (OpenAlex) | `filter=title_and_abstract.search:` | topic and concept tags, not a thesaurus | not supported; spell out | AND, OR, NOT in capitals inside the search value | `filter=publication_year:2015-2024` | tags are machine-assigned; do not treat them as headings |
| scholarly graph (Semantic Scholar) | none in relevance search | fields of study only | bulk search supports `*` | relevance search has none; bulk search uses `+`, `\|`, `-`, quotes | `year=2015-2024` | relevance search returns a ranked sample, not a total |
| DOI registry (Crossref) | `query.bibliographic=` | none | none | none | `filter=from-pub-date:2015,until-pub-date:2024` | ranked matching; use for identity, not as a review database |
| trial and study registries | condition and intervention fields | registry vocabularies | varies | varies | registration or start date | records are studies, not reports; link them in the study-to-report map |

## Recording a translation

For each database, the amendment entry holds: the rendered string, the date checked against the help page, every feature that did not carry over and what replaced it, and the hit count from the pilot. If a block had to be run separately, list each run and how the sets were combined locally.

## Pilot precision

Precision = relevant hits in the sample divided by sample size. Below about 1 in 20, narrow by field restriction first. Above about 1 in 2 on a large result set, the string may be too narrow; check the known-eligible set before trusting it.
