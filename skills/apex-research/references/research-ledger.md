# Research ledger

One append-only JSONL file per research run, written where the lane skill says (the user's chosen path or the working directory, never the repository root). Every lane skill under `lanes/` appends to it; the router (`../SKILL.md`) names the lane and skill in the report's first line.

Common fields on every entry: `id`, `type`, `run_id`, `skill`, `created_at` (UTC ISO 8601), `label` (Fresh, Retained, Reported or Proposed; see `../../../references/conventions.md`, Evidence labels).

| `type` | Written when | Required fields |
|---|---|---|
| `protocol` | before searching | `question`, `output_wanted`, `stop_rule`, `limits` (cases, attempts, elapsed, spend, owner of a failure) |
| `search` | each search or fetch pass | `backend`, `query`, `window`, `result_count`, `status` |
| `source` | each unique source | `source_id` (URL, DOI or registry id), `title`, `retrieved_at`, `read_status`, `independence_group`, `sha256` for local files |
| `passage` | each excerpt used | `source_id`, `locator`, `quote` (verbatim where permitted), `claim_id`, `stance` (supports, contradicts, neutral) |
| `disposition` | each claim judged | `claim_id`, `verdict` (supported, contradicted, unsupported, held), `passage_ids`, `reason` |
| `report` | once, at the finish | `path`, `sha256`, `claim_kind` per statement (observed, inferred, proposed), `next_action` |

A null stays null. A disposition cites at least one `passage` or says why none exists. A ledger from a Retained run is read, never rewritten.
