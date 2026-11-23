---
name: refactor-clean
description: Find and remove dead code and duplicates one item at a time, with the tests green before and after each removal. Use for unused functions, files, exports, dependencies or near-identical copies. Not for restructuring live code with no deletions; use tailered-ai:orch-refine-code. Not for a plain gate report; use tailered-ai:lockin verify.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Refactor Clean

Remove what nothing uses, safely. Kept from the source: detect, sort by risk (safe, caution, danger), remove one item at a time with a test run before and after, check for dynamic use before removing caution items, then merge near-duplicates and report. Do not refactor while cleaning.

## When to Activate

- The user asks to remove dead code, unused files, exports or dependencies, or to merge duplicate helpers.
- A folder has grown copies of the same script or helper.

Do not use for:
- improving structure with the same code kept (extract, rename, reduce nesting): `tailered-ai:orch-refine-code`;
- running the project's gates as a report: `tailered-ai:lockin` verify;
- cleaning during a release or deploy: stop and use `tailered-ai:workflow` first.

## Inputs and outputs

Input: the folder or module to clean. Output: a short cleanup report (removed, kept, skipped with reasons, lines saved) and the final test result.

## Steps

### 1. Establish a green baseline

Find the folder's real test runner (`run-suite.sh`, `*.test.mjs`, `pytest`, a package script). Many Tailered folders have no `package.json`; do not assume `npm`. Run the whole suite. If it is red or absent, stop: add or fix tests first, or report that cleanup is unsafe.

Completion: a recorded green run, or a stop with the reason.

### 2. Detect candidates

Use the tools the project already has or are cheap to run (knip, depcheck, ts-prune, vulture, deadcode). With none, search for definitions with no references. Include dynamic use: string names, `import()`, `require()`, config files, cron or systemd units, shell scripts and routes.

Completion: a candidate list with the evidence for each.

### 3. Sort by risk

- SAFE: unused internal helpers and test helpers.
- CAUTION: components, routes, middleware, anything exported or referenced by name.
- DANGER: config, entry points, types, anything a running service, schedule or other session may use.

Completion: every candidate has a tier. DANGER items are left alone and reported.

### 4. Remove one item at a time

Never delete live work. Before removal, move the file aside to a dated folder outside the repo (`~/.local/share/tailered-removed/<date>/`, never inside the working tree, so it cannot be committed or shipped) or make a backup copy (the owner rule); take single functions out with a small edit. Then rerun the suite. If it fails, restore the item and mark it skipped.

Completion: each removal has a green run after it, or is restored.

### 5. Merge duplicates

Only after removals. Pick the most complete, best-tested copy, point callers at it, move the others aside, rerun the suite.

Completion: callers all use the kept copy and the suite is green.

### 6. Report

List removed, skipped (with why), moved-aside location and the final suite result.

Completion: the report's final line quotes a fresh suite run after the last change.

## Anti-Patterns

- Removing without a green baseline.
- Batching many removals into one test run.
- Cleaning while a feature or release is in flight.
- Restructuring code in the same pass.
- Removing something a live service may load by name.
- Reporting "no regressions" without a fresh run.

## Source and adaptation

Source: `refactor-clean` command from the ECC bundle 2.2.1 (installed local copy, `commands/refactor-clean.md`) plus its cleanup agent description in the same bundle. SHA256 of the source entrypoint: `be911e404a89e79cc878e20ba28b0feeacc2350db8710624622d88a453bf13db`. License: MIT (see NOTICE.md at the plugin root).

- Merged the command and the agent into one skill and dropped the agent as a dependency.
- Replaced the git revert and outright removal with move-aside or a backup copy, per the never-delete-live-work rule.
- Added the find-the-real-runner rule for folders without `package.json`.
- Added the dynamic-use check for services, schedules and shell scripts, and the release stop.
- Routed structure-only changes to `tailered-ai:orch-refine-code`.
