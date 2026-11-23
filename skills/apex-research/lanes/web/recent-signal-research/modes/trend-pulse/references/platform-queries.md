# Platform queries, voices and briefing layout

Endpoints are short technical strings that drift. Treat each as unverified until it returns results this run; record `schema drift` if the shape changes.

## Discussion forum (public JSON search)

- Search: `reddit.com/search.json` with `q=<topic>`, `t=<hour|day|week|month|year|all>` (nearest bucket covering the window), first `sort=top`, then `sort=new`.
- Comments: append `.json?limit=<n>` to a post URL for its leading comments.
- Rate limit: per address. On HTTP 429 or a zero remaining-requests header, wait a few seconds and retry once; then try a community-restricted search (`r/<community>/search.json` with `restrict_sr=1`) or `raw_json=1`.
- Voice: end users and hobbyists; good for sentiment, problems, openings. Community norms, vote-driven amplification and brigading distort contested topics.

## Technical news forum (public search API)

- Base `hn.algolia.com/api/v1/search` with `query=<topic>`, `tags=story` then `tags=comment`, and `numericFilters=created_at_i><unix start>`.
- Voice: builders, founders, investors; good for technical credibility and scaling realism. Skews technical and contrarian, under-represents consumer views; say so in the briefing.

## Open web

Host search with a date filter, three query types: established publications (a short list of reputable outlets as site filters), recent reviews (`"<topic>" review <year>`), candid opinion (`"<topic>" problems OR complaints OR "worth it"`). Fetch before citing. Voice: editorial and produced; good for trend, comparison, breadth; publication agendas, news cycles and paywalls bias it.

## Short-post network (optional)

Routes in order: a user-supplied export (filter to the window, deduplicate by post id, keep handles, record file name and hash only); an already-connected tool; configured browser automation; else skip with the reason. Voice: real-time, personality-driven, shallow; algorithmic amplification favours inflammatory posts. It adds breaking reaction, not primary signal.

## Pattern heuristics

- Consensus: the same factual claim, not the same words, on three or more platforms. Cite one source per platform.
- Dispute: platforms or threads taking opposite positions on one question. Cite both sides and say which voice holds which view.
- Pain points: repeated complaint shapes ("tried X and Y broke", "the worst part of X").
- Excitement: repeated enthusiasm shapes ("just shipped", "this is huge").
- Emerging: present in newest results, absent from top results.
- Gaps: an angle you would expect that no source raises.

Weight each signal by the platform's voice and bias; a dispute between a consumer forum and a builder forum is often a difference of audience, not of fact.

## Briefing layout

```
# <Topic>: pulse, last <N> days
Generated <date> | angle <angle> | window <start> to <end>
TL;DR: two or three sentences
Discussion forum: top posts (title, community, score, comments, one-line summary, link); what people say
Technical news forum: notable stories (title, points, comments, summary, link); what people say, with the voice note
Web: key sources (title, publication, takeaway, link); what is said
Short-post network: findings with handles, or "skipped: <reason>"
Cross-platform patterns: consensus, disputes, pain points, excitement, emerging, gaps
Since last pulse: new, gone, changed (only when a prior briefing exists)
Takeaways: three to five bullets
Content angles: two or three, only if the data supports them
Audit: queries sent per platform, sources received, sources cited, background excluded, stopped early yes or no
```
