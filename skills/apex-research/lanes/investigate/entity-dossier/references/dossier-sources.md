# Dossier sources and sections

## Tiers

- Primary: the entity's own filings and official pages, court records, regulator notices, audited reports.
- Secondary: established news and trade press, ratings bodies.
- Tertiary: blogs, forums, social posts, review sites, aggregators.

## Sources by subject type

| Type | Primary | Secondary | Tertiary |
|---|---|---|---|
| Company | official site (about, leadership, newsroom, careers); securities filings if listed: annual and quarterly reports, material-event notices; court and regulator records | news, trade press, funding and company databases if available | employee review sites, social posts, forums |
| Nonprofit | tax filings (annual returns and their schedules), published impact reports, state charity registries | news, charity raters | donor forums, social posts |
| Public body | official government sites, budgets, audit reports, procurement notices | news | commentary |
| Person, public role | employer pages, filings naming them, conference talks, papers, their own published site | news and interviews | social posts |

Purpose shifts priority: diligence leans on filings and financial trends; sales prep on recent launches and hires; reporting on court records, regulator actions and filings; interview prep on recent strategy and leadership changes.

Listed US companies: the filings service takes `https://data.sec.gov/submissions/CIK<10-digit id>.json` and expects a descriptive user-agent with a contact the user provides. A going-concern note in an annual report is a primary red flag.

Nonprofit metrics worth reading: program spending as a share of total (a very low overhead can mean misclassification), executive pay schedule, share of independent board members, related-party transactions, any going-concern note.

Degradation: when a source is blocked or down, record it, retry once, and continue with the next tier, noting the gap in the section it affects.

## Nine sections

1. Summary: who they are, why they matter here, the verdict, three things to know.
2. Identity facts: founded, location, size or stage, role, key affiliations; each cell sourced and tiered.
3. Hypothesis test: the hypothesis word for word; three to five supporting and three to five disconfirming points with citations; verdict paragraph.
4. Twelve-month timeline, newest first.
5. Network, five to ten entries ranked by relevance to the hypothesis.
6. Reputation, with a noise caveat.
7. Red flags, each tiered.
8. Hooks: the hook, the finding with its citation, a suggested opening line.
9. Audit: sources with tiers; searches (number, query, supporting or disconfirming, returned, cited); the three counts and tier counts; failures; optional backends used.
