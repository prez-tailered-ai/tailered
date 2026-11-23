# Backend map

The optional web research backend as documented upstream on 2026-09-30, base `https://api.parallel.ai`, key in the `x-api-key` header. Unverified until a call this run returns a well-formed body; check the current schema first. Persistent monitor endpoints exist upstream but this skill does not call them.

| Mode | Request | Response to check |
|---|---|---|
| search | `POST /v1/search` with non-empty `search_queries`, optional `objective`, `mode`; limits and source policy under `advanced_settings` | `results[]` with `url`, `excerpts`, optional `title`, `publish_date`; `search_id`; no cursor |
| extract | `POST /v1/extract` with `urls` (at most 20 per request), optional objective; full content under `advanced_settings` | `results[]` and per-URL `errors[]` with `url` and `error_type`; partial failure can still return success |
| report | `POST /v1/tasks/runs` with `input`, `processor`, optional `task_spec.output_schema`, optional `previous_interaction_id`; then `GET /v1/tasks/runs/{run_id}` and `.../result` | 202 with `run_id` (prefix `trun_`), `interaction_id`, `status`; result has `output.content` and `output.basis` |
| enrich | create a group (`POST /v1/tasks/groups`); add rows to it (`POST .../{taskgroup_id}/runs`, body fields `inputs` and `default_task_spec`); status `GET /v1/tasks/groups/{taskgroup_id}`; rows from `.../runs?include_input=true&include_output=true` | group id prefix `tgrp_`; `status_counts`, `is_active`; rows arrive as an event stream with input, output and basis |
| discover | `POST /v1beta/findall/ingest` with `objective` (schema preview, still a billed call), then start the run (`POST /v1beta/findall/runs`; body carries the objective, the entity type, the conditions to match, a generator tier, a limit and known entities to exclude); status and result under `/v1beta/findall/runs/{findall_id}` | id prefix `findall_`; `candidates[]` with `match_status`; only `matched` counts; result is a snapshot with no cursor |

Processor and generator tiers trade depth for latency and cost; name the tier explicitly so a rerun matches.

Interaction ids allow a direct follow-up to reuse earlier context. A task-group id is not an interaction id. Never reuse one across unrelated topics or users.

Accepted is not done: a 202 or a launch response means work was queued, not that results exist.
