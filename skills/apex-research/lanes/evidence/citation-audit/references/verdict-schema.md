# Citation audit verdict file

The verdict file is written on every run, including NOT APPLICABLE and BLOCKED runs. It is evidence, not approval.

## Fields

| Field | Meaning |
|---|---|
| `audit` | `citation-audit` |
| `verdict` | PASS, WARN, FAIL, NOT APPLICABLE, BLOCKED or ERROR |
| `reason_code` | short code, e.g. `all_keep`, `metadata_drift`, `wrong_context`, `not_found`, `no_citations`, `bib_unreadable`, `lookup_failed` |
| `summary` | one plain sentence |
| `input_hashes` | map of each file read (path relative to the manuscript folder, absolute if outside) to `sha256:<hex>` |
| `reviewer` | the configured identifier actually used, or `unavailable` |
| `reviewer_context` | `fresh` |
| `generated_at` | UTC ISO-8601 |
| `ledger` | path of the research ledger file the dispositions were appended to |
| `details.total_cited` | number of distinct cited keys audited (not the bibliography size) |
| `details.per_entry[]` | `{key, verdict, axis_failures: [EXISTENCE, METADATA, CONTEXT], uses: [{file, line, context: supports|weak|wrong, note}], resolved_id}` |
| `details.uncited[]` | only with `uncited` on: `{key, suggestion: prune|check, note}`; `check` only with local evidence such as a to-do comment naming the key |
| `details.uncited_status` | only with `uncited` on: `ok` or `unavailable` (the list could not be built; never blocking) |
| `freeze` | true when the bibliography was frozen |
| `details.freeze_actions[]` | only under freeze: `{key, base_verdict, action: keep|drift_noted|soften_sentence|drop_in_text_citation, occurrences: [{file, line, current, proposed, reason}]}` |

## Decision table

| State | Verdict |
|---|---|
| No bibliography or no citations | NOT APPLICABLE |
| Bibliography named but unreadable | BLOCKED |
| Every entry KEEP | PASS |
| Only FIX verdicts | WARN |
| Any REPLACE or REMOVE | FAIL |
| Lookups or the reviewer failed | ERROR |

Uncited entries and freeze mode never change the verdict. A FAIL under freeze is still a FAIL; freeze only changes what the proposals touch.

## Ledger mapping

- Each use: one `passage` entry, `stance` from the context answer (supports, contradicts for wrong, context for weak), `claim_id` naming the citing sentence.
- Each use: one `disposition`. KEEP and FIX uses are `supported` (FIX notes the metadata fault), a wrong-context use is `contradicted`, a weak use is `mixed`, a REMOVE entry's uses are `unsupported`, and an unresolved lookup is `held`.
