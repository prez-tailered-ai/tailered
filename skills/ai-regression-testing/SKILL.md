---
name: ai-regression-testing
description: Turn a defect found in agent-written code into an executed reproducer, a matching corrected case and a path-parity check across sandbox, mock and real code paths, using the repository's actual test runner. Use after a bug is found and fixed in agent-modified code, or when the same model wrote and reviewed a change. Not for a general testing standard; that is ai-first-engineering.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# AI regression testing

Prevent the re-introduction of defects in code that an agent wrote and then reviewed with the same assumptions. The source's useful structure is kept: tests are written for bugs that were found, not for code that works; the reproducer runs before the fix and the same case runs after it; every code path that produces a contract (sandbox or mock, real, feature-flag branches) is checked for the same shape; and a bug check runs mechanical checks before any model review. The framework, runner and mode switch are resolved from the repository.

## When to Activate

- A defect was found in agent-modified routes, handlers, queries or state logic, and a fix is planned or done.
- A change has a sandbox, mock or feature-flag path beside the real path.
- The same model wrote and reviewed a change and nothing mechanical has run on it.

Do not use for:
- Setting the repository's testing standard or review gates: ai-first-engineering.
- Comparing agents on fixed tasks: agent-eval.
- Rating the quality of a written output: agent-self-evaluation.
- Running the existing suite with nothing changed: the repository's own test command.

## Inputs and outputs

Required inputs:
- The defect: what was observed, where (route, function, query, component), and the retained evidence (failing output, report, trace).
- The test runner and the mode switch, resolved from the repository (lockfile, config, scripts, environment handling).
- The contract the code must satisfy: the fields, states or results the caller depends on.

When the runner cannot be resolved, report that and stop before writing a test; a test with no runner proves nothing. When no defect exists yet, say so: this skill writes bug-driven tests and adds none for untouched code.

Output: a named reproducer that failed for the defect's reason, the same case passing after the fix, a parity check for every path that produces the contract, and a report with measured counts (cases run, passed, failed) and the paths each result proves.

## Steps

### 1. Resolve the runner and the mode switch

Read the lockfile, test configuration and scripts to find the test command, the test file location and how a sandbox or mock mode is enabled (environment variable, config flag, injected client). Record the exact command.

Completion: the test command, test directory and the mode switch are written down from inspected files, or their absence is reported.

### 2. Bind the defect to its contract

State the contract the defect violated: the field that was missing, the state that leaked, the rollback that did not happen. Name the code paths that produce that contract. Read [the regression patterns](references/regression-patterns.md) to classify the defect.

Completion: the defect has a one-line contract statement, a pattern classification and the list of producing paths.

### 3. Write the reproducer and run it red

Write one test named after the defect that asserts the contract. Run it before the fix. It must fail for the defect's reason. A failure caused by a missing dependency, an import error, a syntax error or a wrong fixture is a harness accident: fix the harness and run again; it does not count as the target going red.

Completion: the reproducer's failing output cites the contract assertion, and the output is retained.

### 4. Apply the fix and run the same case green

Apply the fix on every producing path. Run the same test; it passes. Run the surrounding suite with the resolved command to catch collateral breakage.

Completion: the named test passes, the suite result is recorded with counts, and no new failure is unexplained.

### 5. Check path parity

For each producing path, assert the same contract shape. Label what each result proves: a sandbox or mock path proves that path only. The real path needs a real-path check (integration test, staging call, retained production evidence) or its contract status stays open. Mocked evidence never certifies production (see `../../references/conventions.md`, Evidence labels).

Completion: every producing path has a parity assertion or an open item, and each result carries its proof label.

### 6. Order the bug check

When a broader check is requested, run it in this order: the resolved test command; the build or type check; behavior review using the pattern list in `references/regression-patterns.md`; one regression test per fix found. A mechanical failure is reported first and blocks the review step until explained.

Completion: each stage has a result, and every fix found has a named regression test or an open item.

### 7. Report what is proved

Lead with the defect, the test name and the before and after results. Report measured counts only. State which paths are covered and which contract remains open. Fresh and Retained evidence are labelled per the conventions.

Completion: a reader can tell what the fix proves, on which paths, and what still prevents a full-path claim.

## Anti-Patterns

- Trusting a same-model review in place of a test; instead run the reproducer and cite its output.
- Writing tests for code that never had a bug to raise a coverage figure; instead write the test where the bug was found.
- Fixing the real path and leaving the sandbox or mock path with a different shape; instead assert parity on every producing path.
- Selecting every column or field to make a missing one appear; instead name the needed field explicitly in the query and assert it in the test.
- Counting a missing dependency or a syntax accident as the target going red; instead fix the harness and rerun.
- Claiming the regression cannot recur; instead state that the named case is now executed on the resolved runner.

## Source and adaptation

Source: `ai-regression-testing`, ECC 2.2.3 installed local bundle, entrypoint SHA256 `83f2f5c4083af5762dd658f742d4a390eb3a6f969d835f69e8f47efba296c127`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- The Next.js, Vitest and Supabase setup, helper and command examples were removed; the runner, test location and mode switch are resolved from the repository.
- The "use SELECT *" fix for a missing column was removed; the pattern now names the missing field explicitly in the query and asserts it, because a blanket projection masks the contract and widens data exposure.
- The claim that a tested regression "cannot happen again" and the observed-frequency figures were removed; results are reported as measured counts and named executed cases.
- Harness accidents (missing dependency, syntax error, wrong fixture) are distinguished from the target going red.
- Sandbox and real-path contracts are distinguished with proof labels; mock evidence proves the mocked path only.
- The custom `/bug-check` command definition became an ordered procedure in step 6; no command is installed.
- The four regression patterns were rewritten framework-neutrally in `references/regression-patterns.md`.
