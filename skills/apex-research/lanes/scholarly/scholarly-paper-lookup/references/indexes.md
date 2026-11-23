# Scholarly index routing and hazards

Each index is an optional backend. Its capability state is unverified until a call in this session returns a well-formed answer. Endpoints were documented upstream as of 2026-09-30; check them before relying on them.

## Routing

| Intent | Primary | Also consider |
|---|---|---|
| biomedical topic | PubMed | Europe PMC, OpenAlex, Semantic Scholar |
| biomedical full text, or keyword inside full text | Europe PMC | PMC, CORE |
| biology or health preprints by topic | Europe PMC with `SRC:"PPR"` | OpenAlex |
| biology or health preprints by date or DOI | bioRxiv, medRxiv | Europe PMC |
| physics, maths, CS preprints | arXiv | OpenAlex, Semantic Scholar |
| any field, broad | OpenAlex | Crossref, Semantic Scholar |
| one paper by DOI | Crossref | Unpaywall, Semantic Scholar |
| open-access copy | Unpaywall | CORE, PMC |
| citation graph or author works | Semantic Scholar | OpenAlex, OpenCitations |
| PMID, PMCID, DOI conversion | PMC ID Converter | Crossref, Europe PMC |
| retraction or correction | Crossref update metadata (`update-type:retraction`, read `update-to`) | publisher notice, PubMed publication type |
| entities in a biomedical paper | PubTator3 | Europe PMC annotations |
| deposited data, software, posters | Zenodo | Figshare, BioStudies |
| institution id from an affiliation | ROR | OpenAlex |
| is a journal open access | DOAJ | OpenAlex `is_in_doaj` |

## Identifier formats

DOI `10.xxxx/...`; PMID integer; PMCID `PMC` plus digits; arXiv `YYMM.NNNNN` or legacy `archive/NNNNNNN`; OpenAlex `W` plus digits; Europe PMC ids are `{source}/{id}` pairs, so carry the source; ORCID `0000-0000-0000-0000`; ROR `https://ror.org/` plus nine characters; Zenodo concept and version records differ. A constructed arXiv DOI under `10.48550` resolves but is not a portable key in every index; cross-reference by arXiv id.

## Quiet failures

| Index | Looks like success | Actually |
|---|---|---|
| PMC full text | well-formed article, HTTP 200 | no body element: publisher bars redistribution, metadata only |
| arXiv | one result, HTTP 200 | entry titled `Error` for a bad parameter; unknown field prefixes silently become `all:`; throttling answers in plain text |
| Europe PMC | HTTP 200 | `errCode` in the body |
| bioRxiv, medRxiv | cursor paging works | cursor is an absolute offset; a wrong step skips records; no keyword search at all |
| Figshare | HTTP 200 on GET search | the query is ignored; search is a POST |
| OpenCitations | count 0 | unknown DOI; the prefix is required |
| Unpaywall | HTTP 422 | placeholder email rejected; a real contact is required |
| OpenAlex | abstract present | stored as an inverted index; rebuild by position, keep duplicates |
| any | empty result | not indexed here, not "does not exist" |

## Rate limits to respect

NCBI about 3 per second without a key; arXiv one call per 3 seconds; Crossref list queries about 1 per second, more with a `mailto`; others are generous but still serialised per host. Optional user-supplied keys by environment name: `NCBI_API_KEY`, `S2_API_KEY`, `CORE_API_KEY` (needed for CORE full text), `OPENALEX_API_KEY`. Absent key: proceed at the lower limit and say which key would help.
