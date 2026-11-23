---
name: orch-refine-code
description: Restructure code without changing what it does: confirm tests are green, change in small steps with the tests rerun after each, then get one independent review of the diff. Use to extract modules, rename, reduce nesting or split large files. Not for removing dead code or duplicates; use tailered-ai:refactor-clean. Not for behavior changes; use tailered-ai:workflow.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Orchestrated Refine Code

Better structure, same behavior. Kept from the source: tests green before, small steps with tests rerun after each, characterization tests when coverage is thin, a plan the user approves first, one review, and a diff that is behavior-neutral. The existing tests are the safety net; no new behavior is written.

## When to Activate

- The user wants structure improved and behavior must stay identical: extract a module, rename for clarity, reduce nesting, split a long file.

Do not use for:
- removing unused code or merging duplicates: `tailered-ai:refactor-clean`;
- any change in behavior, a new feature or a bug fix: `tailered-ai:workflow`;
- a quality review with no edits: `tailered-ai:lockin` review;
- shipping the result: `tailered-ai:workflow` (Release).

## Inputs and outputs

Input: what to restructure and where. Output: a behavior-neutral diff, before and after test results, one review result and a commit message starting `refactor:` (committing only on the user's go-ahead).

## Steps

### 1. Confirm a green baseline

Find the real test runner for this folder (a `run-suite.sh`, `*.test.mjs`, `pytest`); many Tailered folders have no `package.json`. Run it. If tests are thin around the target, add characterization tests that pin current behavior first, and run them green.

Completion: a recorded green run that covers the code being moved.

### 2. Plan and get approval

Write a short list of small steps (what moves where, what is renamed) and the size: trivial, small, standard (2-5 files) or large. Anything touching auth, user input, file paths, external calls or secrets is at least standard. Show the plan and wait for the user's approval before editing.

Completion: the user approved the plan in chat.

### 3. Restructure in small steps

Make one step, rerun the tests, and continue only when green. Keep public names, outputs, file formats and error messages unchanged. Move code aside rather than deleting live work (make a backup copy or keep a dated copy first).

Completion: the suite is green after the last step, with a run after every step logged.

### 4. Check that behavior is the same

Read the diff for any change in outputs, defaults, ordering or error handling. Run any real entry point the code serves (a script on sample input) and compare to the before result.

Completion: the diff contains no behavior change, or each one found is reverted.

### 5. One independent review

Ask a separate read-only reviewer subagent to review the diff for behavior changes, broken callers and quality. Resolve all critical and high findings, then rerun the tests.

Completion: no open critical or high finding and a fresh green run after the fixes.

### 6. Commit on request

Show the diff summary and a `refactor:` message. Commit only when the user says to. Production steps go through `tailered-ai:workflow` Release.

Completion: the user confirmed, or the work stops here with the commit unmade.

## Anti-Patterns

- Starting with red or no tests.
- One big rewrite with a single test run at the end.
- Slipping in a fix or a new option.
- Changing public names or output formats.
- Skipping the review because the change "is only moving code".
- Mixing dead-code removal into the pass.

## Source and adaptation

Source: `orch-refine-code` from the ECC bundle 2.2.1 (installed local copy, `skills/orch-refine-code/SKILL.md`), with its command wrapper and only the size, review and two-gate parts of its pipeline skill. SHA256 of the source entrypoint: `5f0f468ffa4e220bd8f76684b3df6a14b67b34333e1ae52e0de49ed2c16fa17b`. License: MIT (see NOTICE.md at the plugin root).

- Inlined the size tiers, the plan gate, the review step and the commit gate; dropped the research, scaffold and agent-map phases.
- Replaced named agents and slash commands with plain steps and "a separate read-only reviewer subagent".
- Sent dead-code sweeps to `tailered-ai:refactor-clean`.
- Added the find-the-real-runner rule, the move-aside rule and the Release hand-off.
