---
name: research-knowledge-graph
description: Keep a project's papers, ideas, experiments, claims and gaps connected across research questions by linking existing research ledger entries with typed edges in one plain append-only file, then answer queries from a size-capped digest and lint the graph for orphans, contradictions, dangling links and stale claims. Use when a project spans many reading and testing sessions and earlier findings, especially failed ideas, must shape later ones. Not for a one-off search, task tracking, or long-term memory of conversations.
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Research knowledge graph

Compile what a project has learned once and keep it current, instead of re-deriving it each session. The evidence already lives in the research ledger; this skill adds only the relationships between entries, as plain lines in one file. No service, database, watcher or helper script sits behind it.

## When to Activate

- "Add this paper to the project map", "what do we know about", "which ideas failed and why".
- After multi-source-literature-retrieval, novelty-check or an experiment verdict, to link what was found.
- Before generating new ideas, to read failed ideas and open gaps first.

Do not use for:
- Task status, owners or next actions: the session's queue record (see `../../../../../references/conventions.md`).
- Finding papers: multi-source-literature-retrieval and the retrieval primitives.
- Grading a claim: citation-audit.

## Inputs and outputs

Inputs: one subcommand (`init`, `link`, `capture check`, `query`, `lint`, `stats`), the project's ledger files, and for `link` the relationships to record. Outputs: appended edge lines, or a digest, lint list or counts shown to the user. Ledger files are read, never rewritten.

## Data shape

Nodes are ledger entries (`../../../references/research-ledger.md`); this skill writes no second store for them.

| Node | Ledger form | Node id |
|---|---|---|
| paper | `source` entry, `source_id` DOI or preprint id | `paper:<source_id>` |
| experiment | `source` entry for a result file, `source_id` local path with SHA-256 | `exp:<entry_id>` |
| claim | `claim_id` with its latest `disposition` | `claim:<claim_id>` |
| idea | `claim_id` with `claim_kind: recommendation`; `held` until tested | `idea:<claim_id>` |
| gap | `claim_id` with `claim_kind: question` | `gap:<claim_id>` |
| failed-idea lesson | `lesson` entry naming the idea and the research reason | on the idea |

Edges live in `research-graph/edges.jsonl` at the project root, one JSON object per line, append-only, hash-chained like the ledger:

```json
{"edge_id":"e12","at":"2026-10-18T09:00:00Z","actor":"writing","from":"idea:q3-c4","to":"paper:10.1000/xyz","type":"inspired_by","evidence":"q3/q3-p17","prev_hash":"<sha256 of previous line>"}
```

Edge types: `extends`, `contradicts`, `supersedes` (paper to paper); `inspired_by` (idea to paper); `addresses_gap` (paper or idea to gap); `tested_by` (idea or claim to experiment); `supports`, `invalidates` (experiment to claim or idea). `evidence` names the ledger entry (`<question_id>/<entry_id>`) that justifies the edge. Removing an edge is a new line `{"type":"retract","retracts":"e12",...}`. Page-style views, if wanted, are generated from these files and never edited by hand.

## Steps

Each invocation runs one subcommand and stops.

### init

Create `research-graph/` with an empty `edges.jsonl`. Record the ledger files it will read.

Completion: the folder and empty file exist.

### link

For each relationship found in this session, check both node entries exist in a ledger, then append an edge with its evidence entry. An edge to a missing node is refused, not written. A claim's grade stays in its disposition; `supports` and `invalidates` edges carry experimental support separately and never overwrite it.

Completion: each new edge is appended with a valid chain hash, or refused with the reason.

### capture check

Before a lesson, idea or claim is recorded as durable, screen it. Environment failures, transient errors and "tool X cannot do Y" statements are operational noise; rewrite them as the fix or missing configuration, or drop them. A failed idea's research reason (what was tried, the metric, why it failed) is the opposite: always keep it.

Completion: the item is kept, rewritten or dropped, with the reason.

### query

Build a digest capped at about 8,000 characters, from short fields only (titles, one-line theses, dispositions, lesson text), never full bodies: open gaps first, failed ideas always, then paper clusters by shared tags, the most connected papers, live chains from limitation to opportunity, unresolved questions. When over budget, cut low-ranked papers, then cluster detail, then chains; never cut failed ideas or top gaps.

Completion: the digest is returned with its character count.

### lint

Report, without fixing: orphan nodes (no edges); claims with both `supports` and `invalidates`; dangling edges (node no longer in any ledger); ideas `held` and untested for more than 14 days; papers sharing two or more tags with no edge; a broken hash chain in either file.

Completion: a lint list with counts per check.

### stats

Counts of papers, ideas by outcome, experiments, claims by disposition, edges by type, open gaps, last edge time.

Completion: the counts are shown.

## Acceptance

Intended cases:
- After a retrieval run, five papers are linked to two gaps with evidence entries, chain intact.
- A query digest is under 8,000 characters and lists both failed ideas.
- Lint finds a claim with both a supporting and an invalidating experiment.

Adversarial cases:
- A link to a paper never recorded in a ledger: refused, nothing appended.
- A lesson reading "the reviewer is broken, never use it": rewritten as the configuration fault or dropped.
- A hand-edited line in `edges.jsonl`: lint reports the broken chain at that line.
- Enough new material accumulates to suggest re-ideation: the skill suggests it; it does not start it.

## Source and adaptation

Source: `research-wiki`, wanshuiyin/Auto-claude-code-research-in-sleep at commit `15c0b799e6cd5fbc4da381a5786dd0bc2cdf15ee`, entrypoint `skills/research-wiki/SKILL.md` SHA256 `3bd314f83f2db97fcfafb74495f1ca23bebad37a69d355bc61aaea8cbb519552`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- The page-per-entity wiki and its two helper scripts become ledger entries plus one plain hash-chained JSONL edges file; no script is copied and no service runs.
- Nodes map onto existing ledger kinds and claim kinds instead of new entity folders; the timeline log is the ledger and edge chain themselves.
- Cross-skill ingest hooks become a `link` step the user or a sibling skill invokes; nothing triggers automatically.
- The optional second-model server is dropped; no reviewer call is needed here.
- Kept: the edge vocabulary, edges as the single source of relationships, the capture screen, the budgeted digest that always keeps failed ideas, lint checks and suggest-only re-ideation.
