# Registry contracts

Documented upstream as of 2026-09-30. Each is an optional backend; check current documentation and response headers before relying on a limit.

| Registry | Request | Response and limits |
|---|---|---|
| DOI agency, primary | `GET https://api.crossref.org/works/{url-encoded DOI}`, no key | one `message` object; author, title and container can be incomplete; take the published date, not `created`, `deposited` or `indexed`; about 5 single-record requests per second |
| DOI agency, data and software | `GET https://api.datacite.org/dois/{url-encoded DOI}`, no key | `data.id` and `data.attributes`, a different schema from the primary agency |
| DOI content negotiation | `GET https://doi.org/{DOI}` with `Accept: application/x-bibtex`, follow redirects | one formatted record; reject a response that is not that format |
| DOI resolver check | same URL, do not follow redirects | redirect with `Location`: registered; 404: missing; anything else: inconclusive |
| PubMed search | `esearch.fcgi` under `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`, with `db=pubmed`, `term`, `retmode=json`, `tool`, optional `email`, `api_key` | `esearchresult.count`, `idlist`; only the first 10,000 hits are reachable |
| PubMed records | `.../efetch.fcgi` with `db=pubmed`, comma-separated `id`, `retmode=xml` | `PubmedArticle` records; batch up to 200 ids and confirm every requested id came back |
| PMC id converter | host `pmc.ncbi.nlm.nih.gov`, path `/tools/idconv/api/v1/articles/`; parameters `ids` and `format=json` | `records[]`; maps PMID, PMCID and DOI only for articles held in PMC |
| arXiv | `GET https://export.arxiv.org/api/query` with `id_list`, `max_results=1` | Atom entry with optional DOI and journal reference; one request per three seconds; a DOI alone does not prove journal publication |
| Broad scholarly index (title lookup for gaps) | `GET https://api.openalex.org/works` with `search`, optional `filter`; optional bearer key | `results[]`, `meta.next_cursor`; start `cursor=*`, `per_page` at most 100 |

NCBI services allow 3 requests per second without a key and 10 with one, shared across processes on the same address.

## Required fields by entry type

- article: author, title, journal, year; plus volume, pages or article number, DOI when assigned.
- inproceedings: author, title, booktitle, year.
- book: author or editor, title, publisher, year.
- incollection: author, title, booktitle, publisher, year.
- thesis: author, title, school, year.
- techreport: author, title, institution, year.
- misc or online: author or organisation, title, year, URL with access date.
