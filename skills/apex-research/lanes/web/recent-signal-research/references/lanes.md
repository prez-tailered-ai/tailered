# Lanes and query traps

Detail for steps 2 to 5 of recent-signal-research.

## Lane types

| Lane | What it adds | Weight signal | Typical access |
|---|---|---|---|
| community forums | detailed complaints, workarounds, top comments | votes, reply count | public JSON or search endpoints, host fetch |
| link aggregators | technical reaction, early adopter takes | points, comments | public search endpoints, no key |
| short posts | fast reaction, first-party voice of people and companies | likes, reposts, replies to the subject | user-configured connector only |
| video | demos, reviews, transcripts, viewer comments | views, likes, comment likes | host search; transcripts only if a tool is present |
| news and blogs | what was announced, dates | none; lower weight | host web search |
| code hosting | what actually shipped: releases, issue volume, star counts | live counts | public read endpoints |
| prediction markets | priced expectations | odds and their movement | public read endpoints, no key |
| reviews | buyer experience for products and companies | rating counts | host web search |

A lane's state is unverified until it returns in-window results this run.

## Query traps

| Trap | Sign | Action |
|---|---|---|
| demographic shopping | "gift for a 40 year old", age plus gender | ask for hobbies, relationship and budget; if declined, drop the age and scope to gift communities |
| colliding number | a number that matches jerseys, anniversaries or titles | drop the number from search unless it is part of the name (a version number, a place) |
| tutorial phrasing | "how to use X", "what is Y" | rephrase into discussion vocabulary: setups, tips, problems, workflows |
| single generic noun | "coffee", "headphones" | ask which facet; each facet is a different community |
| non-English topic | non-Latin script present | prefer web search with regional coverage; skip English-only community lanes and say coverage is limited |

## Entity resolution checklist

- Person: their own accounts, code host username, communities they post in.
- Product or project: official site, repository, the community that discusses it, close category peers if the user wants comparison.
- Company: domain, review pages, official accounts.
- Record what was resolved and what was looked for but not found. "No account found" is a result, not a gap to fill by guessing.

## Strength labels

- strong: carried by three or more independent lanes, or by high engagement in two.
- moderate: two lanes, or one lane with high engagement and first-party confirmation.
- single-lane: one lane only; say so beside the claim.
- thin: low engagement everywhere; mention only with that label.

These labels describe signal strength, not truth. A factual claim that matters still goes through citation-audit.
