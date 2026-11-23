---
name: agent-eval
description: Compare coding agents or agent setups on reproducible YAML-defined tasks with pinned source identity, at least one deterministic judge, a finite run budget, and honest reporting of pass counts, time and cost or its absence. Use when choosing between agents or measuring the effect of an agent setup change. Not for rating one delivered output; that is agent-self-evaluation.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Agent eval

Replace impressions about which coding agent or setup works better with matched, reproducible task runs. The source's useful structure is kept: declarative YAML task definitions (name, description, repository, files, prompt, judges, pinned commit), one isolated checkout per run, the four metrics (pass rate, cost when available, time, consistency across repeated runs), the define-run-compare workflow, and the judge types with at least one deterministic judge per task. The external `agent-eval` command-line tool and any worktree tooling are separate dependencies whose presence is verified, never assumed.

## When to Activate

- Choosing between coding agents, or between two configurations of one agent, for a real codebase.
- An agent's model or tooling changed and the effect on pass rate, time or cost needs measurement.
- A team decision about agent adoption needs data from matched runs.

Do not use for:
- Rating the quality of one delivered output: agent-self-evaluation.
- Regression tests for a defect in application code: ai-regression-testing.
- Planning and running the engineering work itself: agentic-engineering.
- Reviewing an agent's runtime architecture: agent-architecture-audit.

## Inputs and outputs

Required inputs:
- The comparison question and its decision owner.
- The candidates: each agent or setup with its tool identity, version and the configured model identifier it will use, or `unavailable` where the host does not expose it.
- The target repository with the commit to pin and the test runner resolved from it (lockfile, config, scripts).
- The finite run budget: tasks, candidates, runs per candidate, time cap per run, spend cap, and who owns a failure (see `../../references/conventions.md`, Bounded execution).
- The runner and isolation dependencies: whether the `agent-eval` tool and the checkout isolation it relies on are present and inspected.

When a candidate's identity, the pinned commit or the budget is missing, report the gap and stop before any run. When the external tool is absent, report it as a separate dependency and stop; this skill installs nothing.

Output: versioned task files, one result record per run (judge results, time, cost or `unavailable`, retained judge output), and a comparison table in counts with the sample size beside every figure.

## Steps

### 1. Bind the question, candidates and budget

Write the comparison question, the decision owner, each candidate's tool identity, version and configured model identifier or `unavailable`, and the finite budget. Record the pinned commit hash of the target repository.

Completion: every candidate has an identity line, the commit hash is recorded, and the budget has all five limits and a failure owner.

### 2. Define tasks as versioned fixtures

Write three to five tasks that represent real work on the target, one YAML file each, kept under version control as test fixtures:

```yaml
name: add-retry-logic
description: Add exponential backoff retry to the HTTP client
repo: ./my-project
commit: "<pinned commit hash>"
files:
  - src/http_client.py
prompt: |
  Add retry logic with exponential backoff to all HTTP requests.
  Max 3 retries. Initial delay 1s, max delay 30s.
judge:
  - type: command
    command: <resolved test runner command for tests/test_http_client>
  - type: grep
    pattern: "exponential_backoff|retry"
    files: src/http_client.py
```

Every task carries at least one deterministic judge (a test command or a build command on the resolved runner). A pattern judge may accompany it. A model-based judge, when used, is listed separately and its result is reported in its own column, never merged into the deterministic pass count.

Completion: each task file has a pinned commit, named files, a prompt and at least one deterministic judge, and the files are committed as fixtures.

### 3. Verify the runner and isolation dependencies

Confirm the `agent-eval` tool is present, inspect its version and source, and confirm how it isolates each run (a fresh checkout from the pinned commit, separate from the base repository) and who cleans up those checkouts. State its capability state per `../../references/conventions.md`, Capability states.

Completion: the tool and the isolation mechanism are recorded as available or installed with evidence, and the cleanup owner is named; otherwise the run is reported as blocked on a separate dependency.

### 4. Run within the budget

Run each task for each candidate the planned number of times. Per run record: pass or fail per judge, wall-clock time, cost as measured from the tool's output or `unavailable`, and the retained judge output. Stop at the time cap, the spend cap, or a repeated same-cause failure of the harness.

Completion: the planned run count is reached or the stop reason is recorded, and every completed run has a result record.

### 5. Compare in counts

Produce the comparison table with pass count over run count per candidate and task, consistency as passes across repeats (for example 2/3), median and range of time, and cost as a measured figure or `unavailable`. Place the sample size beside every figure. With a handful of runs, state that the sample does not separate the candidates when the counts differ by one or two runs; a superiority claim needs more runs within a new budget.

Completion: the table has no figure without its denominator, no cost figure that was not measured, and no superiority statement unsupported by the counts.

### 6. Hand the result to the decision owner

Deliver the table, task files, result records and the open items (unavailable costs, blocked runs). The result is evidence for the owner's decision; it is not adoption, installation or release (see `../../references/conventions.md`, Ownership and authority).

Completion: the owner has the artifacts and the open items, and the record states that no adoption step was taken.

## Anti-Patterns

- Running without a pinned commit; instead record the commit hash in every task file.
- Using only a model-based judge; instead keep at least one deterministic judge per task and report the model-based result separately.
- Presenting the external tool as installed; instead verify it and record its capability state.
- Reporting a percentage alone; instead report the count over the run count.
- Filling a missing cost figure with an estimate; instead write `unavailable`.
- Declaring a winner from three runs; instead state that the sample does not separate the candidates.

## Source and adaptation

Source: `agent-eval`, ECC 2.2.3 installed local bundle, entrypoint SHA256 `57fa683e356b6f5612bc6d7dc101ae39c126e6edf9a48f4ec53afea3e80d7e5d`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- The `agent-eval` command-line tool and its git worktree isolation are treated as separate, unverified dependencies with their own capability state and cleanup owner; the installation section and the repository link were replaced by a verification step.
- Candidate identities carry the configured model identifier or `unavailable`; vendor agent names from the source examples were removed.
- The `pytest` judge example became a command judge on the resolved test runner.
- A finite run budget with a failure owner was added, per the plugin conventions on bounded execution.
- The sample table with percentages and dollar figures was replaced by counts with denominators and `unavailable` for unmeasured cost, and a rule against superiority claims from tiny samples.
- Model-based judging is reported in its own column, separate from deterministic pass counts.
