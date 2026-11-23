---
name: agentic-engineering
description: "Plan and run engineering work that agents carry out end to end: completion criteria first, units with an outcome, owner, receipt and stop condition, capability and regression evals before and after, and model and cost recorded as measured, configured or unavailable. Use when planning or executing agent-run implementation. Not for comparing agents on fixed tasks; that is agent-eval."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Agentic engineering

Run engineering work where agents perform most of the implementation and the session enforces quality and risk controls. The source's useful structure is kept: the four operating principles (completion criteria first, decomposition, routing by complexity, measurement by evals), the eval-first loop (define, baseline, implement, re-run and compare), unit decomposition, session strategy, the review focus for generated code and per-task cost discipline. Routing uses the models the running host has configured, and every unit is bounded per `../../references/conventions.md`.

## When to Activate

- Asked to plan or execute a feature, refactor or fix that agents will implement end to end.
- A piece of work is too large to verify in one pass and needs decomposition with per-unit acceptance.
- Model usage or cost for a task needs to be recorded or compared between units.

Do not use for:
- Setting the team-wide process, review gates or testing standard: ai-first-engineering.
- Head-to-head measurement of agents or models on fixed tasks: agent-eval.
- Writing a regression test for a defect already found: ai-regression-testing.
- Assigning units across several sessions with an integration owner: team-agent-orchestration.

## Inputs and outputs

Required inputs:
- The request and its acceptance (product acceptance, existing tests, checks that must pass).
- The target repository with its resolved framework and test runner (lockfile, config, scripts).
- The session's existing authorization and owner from the coordination record (see `../../references/conventions.md`, Ownership and authority).
- The host's configured model identifiers, or `unavailable` when the host does not expose them.

When an input is missing, record the gap in the plan and stop at the unit that depends on it. Never invent acceptance, authorization or a model identifier.

Output: a unit plan where every unit lists outcome, owner, receipt location, stop condition and dominant risk; eval results before and after with deltas; and a per-unit cost record whose fields are each labelled measured, configured or unavailable.

## Steps

### 1. Define completion before execution

Write the completion criteria for the whole request from its acceptance. Name the capability eval (what must newly work) and the regression eval (what must keep working), each as a runnable command or a named manual check against the resolved runner.

Completion: both evals are named with the command or check that produces their result, and the criteria are checkable without further interpretation.

### 2. Decompose into verifiable units

Split the work into units sized by verifiability rather than by a clock: each unit is independently verifiable, carries one dominant risk and exposes a clear done condition. For each unit record outcome, owner, receipt (the file, test output or record field that proves completion), stop condition and the finite bounds from `../../references/conventions.md`, Bounded execution (attempts, elapsed time, spend, effects). Mark units as independent or dependent on a named earlier unit.

Completion: every unit has outcome, owner, receipt, stop condition, dominant risk and bounds, and the dependency order is explicit.

### 3. Route each unit to a configured model

Choose from the models the host has configured, matching heavier reasoning units (architecture, root-cause analysis, multi-file invariants) to the stronger configured option and narrow edits or transforms to the lighter one. Record the configured identifier actually used, or `unavailable`. Escalate only after a lighter option fails with a recorded reasoning gap in its receipt.

Completion: each unit records a configured model identifier or `unavailable`, and every escalation cites the failed receipt.

### 4. Run the baseline and capture failure signatures

Run the capability and regression evals before any change. Keep the exact failing output per case as the failure signature.

Completion: baseline results are stored with counts of cases run, passed and failed, and each failure has its signature retained.

### 5. Execute independent eligible units within existing authorization

Start units whose dependencies are met and whose effects sit inside the session's existing authorization. A unit that needs wider authority, another owner's path or a release step waits with its blocker named; the plan proceeds on the remaining eligible units. Stop a unit at its stop condition or at a repeated same-cause failure. Session strategy: continue the session for closely coupled units, start fresh after a major phase transition, and compact after a milestone rather than during active debugging.

Completion: every started unit has reached its receipt or a recorded stop, and every waiting unit names its blocker.

### 6. Re-run the evals and compare deltas

Run both evals again. Report per-case deltas against the baseline: newly passing, newly failing, unchanged. A newly failing regression case blocks the unit that caused it.

Completion: the delta table exists with counts, and any newly failing case has an owning unit.

### 7. Review generated code for behavior and record cost

Review the changes for invariants and edge cases, error boundaries, security and auth assumptions, hidden coupling and rollout risk; style stays with the repository's formatter and linter. Record per unit: model identifier, token count (measured from host output or `unavailable`), retries, wall-clock time and the result. The review finding and eval result go to the owner; release follows `../../references/conventions.md`.

Completion: the review covers each changed unit, and the cost record has every field labelled measured, configured or unavailable.

## Anti-Patterns

- Starting implementation before the evals exist; instead write the capability and regression evals first and run the baseline.
- Sizing units by a fixed number of minutes; instead size by independent verifiability and one dominant risk.
- Naming a model tier or vendor model in the plan; instead record the host's configured identifier or `unavailable`.
- Estimating tokens or cost without a measurement; instead label the field `unavailable`.
- Widening authorization because a unit is blocked; instead name the blocker and continue with eligible units.
- Treating a passing eval as release; instead hand the result to the owner and follow release authority in conventions.

## Source and adaptation

Source: `agentic-engineering`, ECC 2.2.3 installed local bundle, entrypoint SHA256 `41c32c20ec97469341f5d83d8beb15f03d1b6f1c40fb1bdf534c50cd9a38cb6f`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- The hardcoded three-tier model routing by vendor model name became routing across the host's configured models with the identifier recorded or `unavailable`, per the plugin conventions.
- The unconditional 15-minute unit rule became sizing by independent verifiability with one dominant risk, and finite bounds per unit from the conventions.
- Each unit now carries an outcome, owner, receipt and stop condition, and independent units proceed within existing authorization while blocked units name their blocker.
- Cost discipline fields are labelled measured, configured or unavailable instead of being tracked as estimates.
- The eval-first loop, session strategy and review focus are kept; style review is delegated to the repository's own tooling.
