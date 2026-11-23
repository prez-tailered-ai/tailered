# Field matrix, recipes and prefixes

Detail for the matrix route of scholarly-paper-lookup (steps 2, 3 and 7). Every index is an optional backend whose capability state is unverified until a call in this session returns a well-formed answer. Endpoints and batch sizes change; check the index's help page and record the date. Routing for single needs, identifier formats, quiet failures and rate limits: `indexes.md`.

## Field by index

P = primary, F = fallback. Pick one P per field; use F only for a gap.

| Field | DOI registry (Crossref) | broad index (OpenAlex) | scholarly graph (Semantic Scholar) | biomedical index (PubMed) | full-text archive (PMC, Europe PMC) | open-access resolver (Unpaywall) | repository aggregator (CORE) | preprint servers (arXiv, bioRxiv, medRxiv) |
|---|---|---|---|---|---|---|---|---|
| title, authors, venue, year | P | F | F | P for biomedical | | | | P for preprints |
| abstract | | F (inverted index) | P | P for biomedical | | | | P for preprints |
| open-access copy | | F (`best_oa_location`) | F (`openAccessPdf`) | | F | P | F | P for preprints |
| full text | | | | | P for biomedical, if body present | | P with a user key | P (PDF) |
| citation count | F (`is-referenced-by-count`) | P | P | | | | | |
| citing works | | F | P | | F (Europe PMC) | | | |
| retraction or correction | P (update metadata) | F (`is_retracted`) | | F (publication type) | | | | |
| funder | P | F | | | | | | |
| author ids (ORCID) | F | P | F | | | | | |
| preprint to published link | F (relation metadata) | F | F | | | | | P for biology and health (`published` field) |

## Recipes for composite requests

| Request | Plan |
|---|---|
| everything about a paper | registry for metadata, retraction and funder; graph for abstract and citations; resolver for open-access copy |
| comprehensive topic search | biomedical index, Europe PMC, broad index and graph; deduplicate by DOI, then by the agreement check |
| find and read | biomedical index or broad index to find; resolver for a copy; archive or aggregator for text |
| preprint keyword search | Europe PMC with `SRC:"PPR"`; take the `10.1101/` DOIs to the preprint server for its published-link field |
| preprint and its published version | preprint server's published-link lookup; registry to confirm the journal record; agreement check on both |
| author overview | broad index by ORCID for works; graph for citation counts; never by name alone when the name is common |
| mixed identifier list | converter first for PMID, PMCID and DOI; graph batch with prefixes for arXiv ids; broad index for the rest |

## Prefixes and converters

- Scholarly graph accepts `DOI:`, `PMID:`, `PMCID:` and `ARXIV:` prefixes on the paper path, and a POST batch endpoint taking a list of prefixed ids.
- Broad index accepts `doi:` and `pmid:` on the works path, and `|` for OR inside a filter value, such as `filter=doi:a|b|c`.
- The biomedical archive's ID converter takes up to 200 comma-separated PMIDs, PMCIDs or DOIs per call and returns all three where known.
- Preprint servers' published-link lookup accepts either the preprint DOI or the journal DOI; `NA` means no link recorded, not "never published".
- arXiv ids carry a version (`2103.15348v3`); record it, and query by the base id unless a version was asked for. Cross-reference arXiv papers by arXiv id, not a constructed `10.48550` DOI.

## Agreement check

Normalise case, punctuation, accents and whitespace in titles. Compare first author surname and publication year; a one-year difference between preprint and journal record is expected and recorded, not a conflict. Anything else that differs is a conflict.
