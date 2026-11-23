# Harness contracts

Templates for Step 3. Express them in the framework's own schema format once the framework is resolved from the repository.

## Action input

- `name`: stable, explicit, unique within the tool set.
- `inputs`: schema-first, narrow; each field typed, required fields listed, no free-form catch-all field.
- `risk`: micro (high-risk, one effect), medium (read/edit/search), macro (bundled, justified by round-trip cost).
- `mapped_to`: the host tool or repository command that executes it, or `gap` with the gap's owner.

## Observation (result)

Validated against this shape before the agent reads it.

- `status`: `success` | `warning` | `error`
- `summary`: one line stating the result.
- `next_actions`: list of actionable follow-ups; may be empty on `success`.
- `artifacts`: file paths or identifiers produced; may be empty.
- `payload`: the typed content; when `status` is `success` and content was expected, `payload` is present and non-empty.

Validation rule: a result that is missing fields, fails its type, is truncated, or has `status: success` with an expected-but-empty `payload` is rewritten as an error observation below. It is never passed on as a success.

## Error observation

- `status`: `error`
- `tool`: the producing tool.
- `boundary`: where it failed (input validation, execution, output validation).
- `reason`: validation or execution reason, without echoing sensitive content.
- `root_cause_hint`: the most likely cause.
- `safe_retry`: the one retry that is safe, or `none`.
- `stop_condition`: what ends retrying (attempt count, elapsed time, spend, or an observation that does not change), and who owns the failure then.
