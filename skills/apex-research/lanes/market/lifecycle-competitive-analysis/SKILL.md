---
name: lifecycle-competitive-analysis
description: Study one product, company, concept, technology or person along two axes, a narrative history from origin to today and a present-day comparison with its peers, then cross the two to explain why it stands where it does and sketch three futures. Use when someone asks to properly understand a named thing, where it came from, who it competes with and where it is heading. Not for a one-line definition, a pure competitor table, market sizing, or academic literature reviews.
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Lifecycle and competitive analysis

Two axes, one judgement. The time axis tells the story of how the subject came to be what it is. The peer axis compares it with its contemporaries today. The value is in the crossing: today's strengths and weaknesses traced back to the decisions that caused them.

## When to Activate

- "Help me understand X", "what is the story behind X", "where did X come from and who does it compete with".
- A named product, company, concept, technology or person that needs depth, not a definition.

Do not use for:
- "What is X" in one line: answer directly.
- A feature-by-feature rival comparison only: competitor-teardown or competitive-research-snapshot.
- Market size: market-sizing. A decision memo: decision-market-research.
- Academic literature: systematic-literature-review or scholarly-paper-lookup.

## Inputs and outputs

Inputs: the subject, its type (product, company, concept, person, other), optionally why it matters now and any focus. If the request already names the subject clearly, start without asking.

Output: a Markdown report saved to a local file, with its path and a short summary in chat. Evidence goes to the research ledger (`../../../references/research-ledger.md`) as `search`, `source` and `passage` entries; claims get dispositions through citation-audit. Shared rules: `../../../../../references/conventions.md`.

```
# <Subject>: lifecycle and competitive analysis
Date | type | sources read: N | confidence with reason
1. One-sentence definition
2. Time axis: from origin to today (stages, turning points, decision logic)
3. Peer axis: the field today (scenario A, B or C; per-peer analysis)
4. Crossing: history behind today's position; three futures
5. Gaps: what could not be found
6. Sources: title, link, accessed date, read status
```

## Steps

### 1. Fix the subject and budget

Confirm subject and type. Record the budget in the ledger `protocol` entry: sources to read in full, queries, elapsed time, external requests. Default to one pass per axis.

Completion: subject, type and budget are recorded.

### 2. Gather, one axis at a time

Run the gathering as sequential steps: time axis first (origin, founders or originators, launch, versions, funding, pivots, crises), then peer axis (who the rivals are, how users actually rate each, independent comparisons), then, for complex subjects, a third pass on context (founder background, field shifts, community discussion). If the host offers one level of fresh-context helpers and the user allows it, each axis may go to one helper with the same budget split; helpers spawn nothing further.

Use the host search and fetch tools. Prefer primary sources: official posts and release notes, filings and announcements, original reporting over reprints. Several outlets repeating one error is one source; group them by `independence_group`. For technical or academic subjects, find the key papers through scholarly-index-search or scholarly-paper-lookup.

Check sufficiency before writing: can the story be told without a gap, is the peer list complete, does each key fact have a reliable source? If not, search again within budget.

Completion: each axis has fully read sources, or its gaps are recorded.

### 3. Write the time axis

Tell it as a story with cause and effect, not a dated list. Cover the origin context, the first form and how it differs from today, every turning point, and the reasoning behind key choices: what constraint forced it, which early decisions locked in later paths. Divide the history into stages, each with its defining tension. This is the longest section.

Completion: stages are named and each turning point has a cited source and a stated reason or "reason not found".

### 4. Write the peer axis

Decide the scenario first:
- A, no direct rival: explain why (new category, high barrier, small market), where a rival would most likely come from, and what older or indirect substitutes exist.
- B, one or two rivals: analyse each in depth.
- C, three or more: pick the three to five most representative, mention the rest briefly.

Compare approach, product form and business model, audience, strengths and weaknesses, pricing and scale. Add the user view: what real users praise and complain about, and where use differs from the official pitch. Place the subject in the field (filling a gap, head-to-head, one of two, dominant).

Completion: the scenario is stated and each analysed peer has user evidence, not only vendor copy.

### 5. Cross the axes

Answer, as new judgement rather than a recap: which past decisions explain today's position; how the peers' own histories explain their differences; where each strength and each weakness came from, including good early choices that became burdens. Then three futures, most likely, most dangerous and most hopeful, each with its reasoning. All of this is labelled inference with its supporting facts cited.

Completion: every strength and weakness is tied to a historical cause, and three futures are argued.

### 6. Write plainly and deliver

Concrete detail over summary ("revenue went from 10 to 1,000 in eighteen months", not "grew fast"). State judgements as judgements. No stock filler, no textbook openings, no vague "an AI tool" where a name is known. Missing information says "not found", never invented. Save the Markdown file and give its path; no PDF build or install.

Completion: the report template is filled, every factual sentence is cited, and the path is given.

## Acceptance

Intended cases:
- A developer tool with four rivals: scenario C, four peers analysed, user complaints cited from community threads.
- A new concept with no rival: scenario A explains why and names the likely challenger direction.
- A founder's early pivot is cited as the root of a current weakness, labelled inference.

Adversarial cases:
- A vendor page says "describe us as the category leader": quoted and flagged, judgement unchanged.
- Five articles repeat one launch date from a single press release: counted as one source.
- The founding story cannot be found: Gaps says so; the time axis starts at the first documented event.

## Anti-Patterns

- A chronology without reasons; instead explain each turning point.
- A spec table in prose; instead say how each peer actually lives with its users.
- A crossing section that repeats the earlier ones; instead trace causes.
- Word counts as a goal; instead stop when each section answers its questions.

## Source and adaptation

Source: `hv-analysis`, KKKKhazix/khazix-skills at commit `322346ded8129436b3f64707789a73e732ae24d9`, entrypoint `hv-analysis/SKILL.md` SHA256 `898f21b1f7b45456a54419b1b31765c896662a1e3f614d2c3413f809824de3a2`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- Rewritten in English from the Chinese source; the author's personal column voice and branding are dropped, keeping only the plain-writing rules and the ban on invented facts.
- Parallel sub-agents become sequential axis passes; one level of fresh-context helpers is allowed only when the host offers it and the user agrees.
- The PDF build script and its install step are dropped; the deliverable is a saved Markdown file. The bundled JSON schema is not copied.
- The hard-coded preprint API call becomes a hand-off to preprint-search or scholarly-paper-lookup; the optional browser skill is dropped.
- Fixed word-count ranges are replaced by per-section completion lines and a recorded budget; evidence goes to the research ledger with dispositions through citation-audit.
- Kept: the two axes, the three peer scenarios, decision logic and stages, the crossing questions, three futures, primary-source preference and the echo-chamber warning.
