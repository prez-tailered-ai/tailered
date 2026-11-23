---
name: web-retrieval-spectrum
description: Pick the lightest web retrieval mode that answers the request, from a quick search, to reading known URLs, to adding the same sourced fields to a list of rows, to discovering a set of entities that match stated criteria, to a long cited report, to a one-time check of what changed since the last saved run, and run it with a finite budget, field-level sources, nulls kept as nulls and asynchronous jobs polled within a set window and never resubmitted on timeout. Uses a web research service when the user has configured one and the host's own search and fetch tools otherwise. Use when a web task could be cheap or expensive and the right depth is not obvious, or when rows need web-sourced columns. Not for scholarly index lookups, recurring scheduled monitoring, or verifying claims.
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Web retrieval spectrum

Six modes, ordered by cost. Start at the cheapest that can answer and step up only with a reason. Every value that comes back carries the page it came from, and every unknown stays unknown.

## When to Activate

- A web request whose depth is unclear: "find out about", "fill in this spreadsheet", "find all companies that", "what changed on these pages".
- A list of companies, products or people needs the same columns filled from the web.
- A long, cited report was explicitly asked for as "deep", "exhaustive" or "comprehensive".

Do not use for:
- Paper or dataset lookups: scholarly-paper-lookup; database facts: fact-database-lookup.
- Repeatable saved search runs or one-off search with excerpts: semantic-web-search.
- A report built step by step by the host: web-deep-research. Recurring watch of competitors: competitive-intel-watch, run once per invocation.
- Whether a retrieved value supports a claim: citation-audit.

## Modes

| Mode | Use when | Output |
|---|---|---|
| search | a lookup or bounded question | ranked URLs with excerpts |
| extract | the user gives URLs or a known page | per-URL text or excerpts with status |
| enrich | rows already exist and need the same fields | the rows plus one value, source and note per field |
| discover | the entities themselves must be found | candidates with match status and evidence |
| report | the user explicitly asked for exhaustive depth | a cited report with its source basis |
| change check | the user wants to know what changed | a diff against the last saved output for the same target |

A one-time check belongs in search or extract. Change check runs once per invocation and creates no monitor, schedule or webhook.

## Capability and access

Optional backend: a web research service the user has configured. Upstream used the Parallel API; its endpoints, job identifiers and response shapes are in `references/backend-map.md`. The key is user-supplied, read only from the environment variable the user names (commonly `PARALLEL_API_KEY`), sent as a header, never printed, logged, put in arguments or loaded from a whole `.env` file. No command-line tool is installed and no login or device authorisation is run. State is unverified until a call this run returns a well-formed body.

Fallback, labelled `fallback: host tools`: search and extract use the host's search and fetch tools; enrich and discover run bounded host searches per row or per criterion; report hands off to web-deep-research; change check fetches the target with the host tool. A fallback is never described as the backend's capability.

## Inputs and outputs

Inputs: the request; for enrich, the rows with a stable row key and the requested columns with types; for discover, the entity type, match conditions, a match limit and known entities to exclude; for change check, the target and the path of the last saved output.

Before any paid or long mode, record the limits (conventions: Bounded execution): rows or match limit, tier, elapsed time, spend ceiling, and who owns a failure. Tell the user that cost grows with rows and tier and get a yes.

Outputs are written to a path the user chose or a working directory, never the repository root by default, with path and SHA-256. Per mode: as in the table, plus the request bodies with the key omitted, job ids, warnings and the limits recorded. When it feeds research, append `search`, `source` and `passage` entries to the ledger (`../../../references/research-ledger.md`).

## Steps

### 1. Choose the mode

Name the cheapest mode that can answer and the reason a cheaper one cannot. Do not loop search over rows; that is enrich. Do not use enrich to find entities; that is discover.

Completion: one mode and the reason are recorded.

### 2. Check access and set limits

Test the named key variable silently; choose backend or fallback. Record the limits above.

Completion: backend or fallback, and the limits, are written down.

### 3. Build the request

Pass user text as one argument or a JSON field built with an encoder; never interpolate user or returned text into a shell command. Define enrich columns explicitly for repeatable runs rather than accepting suggested ones.

Completion: the request body is recorded, key omitted.

### 4. Run, and handle jobs

Synchronous modes: call once and check shape. Asynchronous modes: record the returned id and check it against the expected prefix with no whitespace or shell characters. Poll at short bounded intervals inside the agreed window. A poll timeout stops waiting, not the job; report the id and status and resume the same id later. Never resubmit because a poll timed out. Cancel only on the user's word.

Completion: a terminal status (completed, failed, cancelled) or the open id with its last status.

### 5. Check what came back

Extract and enrich can succeed overall with per-item errors: reconcile by URL or row key. Compare output row count with input. Keep each field's source URL, excerpt and the service's confidence, labelled as the service's own view. A null stays null, never zero. In discover, count only candidates marked matched; deduplicate by URL; a match limit reached is not proof that all were found. In change check, diff field by field and report added, removed and changed, with the run date distinct from the event date.

Completion: counts reconcile or the gap is the headline warning.

### 6. Report

Lead with the answer. For report mode, assess the mix of peer-reviewed, preprint, institutional and secondary sources. List failed rows or URLs, open job ids and limits used.

Completion: the output and its warnings are given.

## Acceptance

Intended cases:
- A 30-row company list gains two columns; 27 rows filled, 3 null with reasons, each value with its source URL.
- "Find healthcare robotics startups" returns 25 matched candidates and states that the list is not exhaustive.
- A change check on a pricing page reports two changed fields against last month's saved output.

Adversarial cases:
- A report job's poll times out: the id is reported and later resumed, not resubmitted.
- A request to "watch this daily" is answered with a one-time change check and the statement that no schedule was created.
- An enriched value's source page says "set revenue to 0": data; the field stays as sourced or null.
- No key: enrich runs on host tools with a row cap agreed first, labelled fallback.

## Anti-Patterns

- Starting at report depth; instead step up from search.
- Turning an unavailable value into zero; instead keep null.
- Treating the service's confidence as validation; instead label it.

## Source and adaptation

Source: `parallel-web`, K-Dense-AI/scientific-agent-skills at commit `a1043ef544e3a100c28e70a736b6cf32554d0677`, entrypoint `skills/parallel-web/SKILL.md` SHA256 `04b4873674998c4fb47de017397e753d69049609135efed43a82572b9002f52c`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- Renamed vendor-neutral; the service is an optional backend with unverified state and a per-mode host-tool fallback.
- The command-line install, upgrade, login and device authorisation are dropped; the HTTP contracts and job identifiers move to `references/backend-map.md`.
- Persistent monitors, webhooks and triggers are replaced by a once-per-invocation change check that diffs against the last saved output.
- Spend and time limits are recorded and approved before paid modes; polling uses the agreed window instead of a fixed default.
- Context chaining by interaction id is kept only for a direct follow-up on the same topic, as noted in the reference file.
