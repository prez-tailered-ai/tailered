# Search lanes and depth budgets

## Keyless lane (default)

Two public indexes, reached with the host fetch tool. Endpoint shapes are short technical strings and may drift; a call that returns an unexpected shape is recorded as `schema drift` and the lane falls back to the other index.

Biomedical index (E-utilities), about three requests per second at most without a key:
- Base: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`.
- Search: `esearch.fcgi` with `db=pubmed`, `term=<query>`, `retmode=json`, `retmax=20`, `sort=relevance` -> `esearchresult.idlist`, `esearchresult.count`.
- Details: `.../esummary.fcgi?db=pubmed&id=<ids>&retmode=json` -> `title`, `authors[].name`, `pubdate`, `fulljournalname`, the `doi` entry in `articleids[]`.
- Date limits: `&datetype=pdat&mindate=<year>` or `&maxdate=<year>`.
- Link: `https://pubmed.ncbi.nlm.nih.gov/<PMID>/`. This index returns no citation counts.

Open scholarly graph (all disciplines), add `&mailto=<address>` only if the user supplies one:
- Search: `https://api.openalex.org/works?search=<query>&per-page=20` -> `display_name`, `publication_year`, `cited_by_count`, `doi`, `id`, `authorships[].author.display_name`, `primary_location.source.display_name`.
- Date limits: `&filter=from_publication_date:YYYY-MM-DD` or `to_publication_date:YYYY-MM-DD`. Reviews only: `&filter=type:review`.
- Citation counts for ranking come from here.

## Optional lane

A connected evidence-synthesis search tool, if present, runs the same queries in addition. Its state stays unverified until it returns results this run. Merge by DOI, then normalised title.

## Etiquette

One query at a time across all lanes, roughly one per second. On error: wait about three seconds, retry once, record the outcome. Three failures in a row: stop and hand over what exists. Zero results are recorded as such, with the note that the term may be niche or the gap real.

## Depth budgets

Roughly twenty results per query per source; deduplication usually removes a third to a half.

| Depth | Searches | Allocation |
|---|---|---|
| Quick | 5 | one per sub-area; no review, date-limited or follow-up searches (note this in the audit) |
| Standard (default) | 10 | 5 sub-area; 2 review-article searches for the top two sub-areas; 2 date-limited for the most important sub-area (an older cut-off and a recent one); 1 follow-up on the most cited paper, its key terms after its publication year |
| Deep | 20 | 5 sub-area; 5 review-article; 4 date-limited (top two sub-areas, old and new each); 3 follow-ups on the three most cited; 3 kept for threads that emerge |

Fixed tiers keep run time predictable and stop "a few more searches" drift. The date-limited pair shows how terminology changed.
