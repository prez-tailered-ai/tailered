# Request fields, run file and filter rules

Detail for steps 2 to 4 of semantic-web-search. Field names follow the upstream HTTP API and connected tool as documented on 2026-09-30; they drift, so confirm against the exposed tool list or the service's docs before relying on one.

## HTTP backend endpoints

`POST /search`, `POST /findSimilar`, `POST /contents` on the service base URL; JSON bodies; key in the `x-api-key` header from the named environment variable. Contents accepts 1 to 100 URLs per call upstream. No offset or cursor pagination is documented.

## Search and similar body

| Field | Values |
|---|---|
| `query` (search) or `url` (similar) | required |
| `numResults` | default 10; 1 to 100 |
| `type` | `auto` unless asked; also `neural`, `fast`, `instant` |
| `category` | `research paper` or `publication`, `news`, `company`, `personal site`, `financial report`, `people` |
| `includeDomains`, `excludeDomains` | domain lists |
| `includeText`, `excludeText` | a required or excluded phrase |
| `startPublishedDate`, `endPublishedDate` | ISO 8601 |
| country | two-letter ISO code |
| `contents` | `highlights` (default), `text` with `maxCharacters`, `summary`, or none (metadata only) |

Company and people categories reject date and exclude-domain filters; drop them and warn. Highlights do not imply text; ask for each content kind explicitly.

## Contents body

`urls` (batched), the same `contents` options, and an optional freshness bound: `0` fresh only, `-1` cache only, else a maximum age in hours (up to 720 upstream). Omitting it uses the service's cache policy. Each URL returns a status with `id` (the requested URL), `status` (`success` or `error`) and `source` (`cached` or `crawled`) where given.

## Connected tool shapes

- Web search: `query`, a result count (default around 8), a search mode (`auto`), a live-crawl preference (live crawl when the index is stale), optional `category`.
- Code context: `query` and a content budget in tokens, roughly 1,000 to 50,000. Use 1,000 to 2,000 for a focused snippet, 5,000 or more for broad context.

## Run specification and results file (`run` mode)

Specification, saved before the call:
- `run_id`: short lowercase hyphenated name from the topic.
- `mode`: `search` or `extract`.
- search: `query`, `passes` (`scholarly`, `general` or `both`), `result_count`, `content` (`none`, `highlights`, `text`), optional date bounds, domain lists and `category`.
- extract: `urls`, `content`, optional freshness bound.

Results file `<run_id>.json`: the specification, the access path, `accessed_at`, `results[]` with `url`, `title`, `published_date`, `author`, `highlights`, `text` (each may be absent), for extraction `statuses[]`, and `warnings[]` for unapplied filters, partial batches and fallbacks. Record its path and SHA-256.

## Scholarly pass

Publication category plus an allowlist such as arxiv.org, biorxiv.org, medrxiv.org, pubmed.ncbi.nlm.nih.gov and major journal domains. Source priority for technical questions: peer-reviewed articles and proceedings over blogs and news; preprints when no reviewed version exists; institutional and government sources over commercial ones; primary research over summaries. Verify publication type and review status per source; the category is a bias, not a guarantee. If no scholarly sources come back, report coverage and filters, not "this topic is unstudied".

## Fallback mapping

Host search has no category bias or meaning-based ranking. Domain allowlists become `site:` queries where the host search supports them, else the filter is reported as not applied. Extraction falls back to the host fetch tool one URL at a time, with the same per-URL status recorded.
