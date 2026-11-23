---
name: ai-first-engineering
description: "Scope an engineering process for one codebase where agents write most of the code: planning standard, eval coverage, behavior-focused review, agent-friendly architecture and a raised testing bar, bound to the real target, its owner and release gates. Use when setting review gates, ownership or testing rules for agent-written code. Not for rating one output; that is agent-self-evaluation."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# AI-first engineering

Produce a scoped engineering process for a codebase where agents generate a large share of the implementation. The source's useful structure is kept: three process shifts (planning over typing speed, eval coverage over anecdote, review of behavior over syntax), four architecture requirements, the five review focus areas, the raised testing standard for generated code, and the capability signals for assigning work. Each of these is bound to one real target with one existing owner and the release gates that apply, instead of being stated as universal ceremony.

## When to Activate

- Asked to set process, review gates, ownership rules or a testing standard for a repository or service where agents produce much of the code.
- A target accepts agent-written changes and its acceptance, owner or release gates are undefined or scattered across files.
- Review time goes to style while behavior regressions, data integrity or recovery pass unchecked.

Do not use for:
- Decomposing and running one piece of engineering work: agentic-engineering.
- Writing the regression test for a defect that was found: ai-regression-testing.
- Rating a delivered output on quality axes: agent-self-evaluation.
- Reformatting or linting code: the repository's own formatter and linter.

## Inputs and outputs

Required inputs:
- The target: a repository, package or service path.
- Its owner, read from the coordination record (see `../../references/conventions.md`, Ownership and authority).
- The acceptance that applies: product acceptance, existing test commands, existing checks.
- The release gates that apply to this target.

When an input is missing, write it as an open gap in the output with who can supply it. Never fill it with an assumed owner, an assumed gate or a generic standard.

Output: one process document, or a section added to the target's existing engineering document, with the target, owner, planning standard, eval coverage map, review focus mapped to named checks, architecture requirements located in the actual code, and the testing standard bound to the resolved test runner. Every review item points to a named check or is marked `no check` and listed as open.

## Steps

### 1. Bind the target, owner and gates

Read the coordination record for the owner. Resolve the framework, formatter, linter and test runner from the repository (lockfile, config, scripts). List the release gates that apply, pointing at `../../references/conventions.md` for release authority rather than restating it.

Completion: the document header names the target path, owner, acceptance, gates and resolved tools, each with the file or record field it came from, and every missing item is marked open.

### 2. Apply the three process shifts to this target

- Planning quality over typing speed: every planned change carries acceptance criteria before any code is generated; name where those criteria live for this target.
- Eval coverage over anecdotal confidence: list the evals and tests that exist for the domains agents touch, labelled measured (a command ran) or configured (declared, not run here) or unavailable.
- Review of behavior over syntax: style is enforced by the resolved formatter and linter; reviewers read behavior.

Completion: each shift has one concrete rule for this target that names the tool, file or check it relies on, or is marked configured or unavailable.

### 3. Locate the architecture requirements in the code

For each requirement (explicit boundaries, stable contracts, typed interfaces, deterministic tests) name where it holds in the target and where behavior is instead spread across hidden conventions.

Completion: every requirement has at least one located example or a located gap, and each gap has an owner or is marked open.

### 4. Map the review focus to checks

Build one table with five rows: behavior regressions, security assumptions, data integrity, failure handling and recovery, rollout safety. Each row names the existing check (command, test file, migration check, rollback procedure) or `manual review item` or `no check`. Generated-code regressions, data integrity and recovery need a named check or an open item; a description of intent is not a check.

Completion: all five rows are filled from inspected files or commands, and every `no check` row appears in the open items.

### 5. Set the testing standard for generated code

State the standard for this target: regression coverage for touched domains, explicit edge-case assertions, integration checks at interface boundaries. Bind it to the resolved runner command and the test location. Bug-driven cases follow ai-regression-testing. Report counts that were measured; where coverage was not measured, write `unmeasured`.

Completion: the standard names the runner command and the test location, and contains no invented coverage figure.

### 6. Record capability signals for assigning work

List the observable signals the source names for strong AI-first engineering (clean decomposition of ambiguous work, measurable acceptance criteria, high-signal prompts and evals, risk controls held under delivery pressure) as evidence to look for when assigning a unit of work to a session or a person, with where that evidence would appear (a plan with acceptance criteria, an eval file, a recorded stop condition).

Completion: each signal names its observable evidence location.

### 7. Keep verdicts separate from release

State in the document that a reviewer verdict, a passing check or a self-score is an input to release coordination and never approval, per `../../references/conventions.md`. Hand the finished document to the owner named in step 1.

Completion: the document carries the release-authority pointer, and the owner has the document and the open items list.

## In the workflow

In `tailered-ai:workflow`, a rule or speedup counts only once it lives in a script with a self-test. Gates run through `tailered-ai:lockin` verify; dead code goes through `tailered-ai:refactor-clean`; behavior-neutral restructures through `tailered-ai:orch-refine-code`; lean defaults from `tailered-ai:lockin`.

## Anti-Patterns

- Copying a universal process into every repository; instead scope each rule to this target's actual tools and checks.
- Spending reviewer attention on style; instead run the resolved formatter and linter and review behavior.
- Writing "regression coverage required" with no mapped test; instead name the test or mark the row open.
- Treating a passing review as a release decision; instead point to the release authority in conventions.
- Reporting a coverage percentage nobody measured; instead report measured counts or `unmeasured`.

## Source and adaptation

Source: `ai-first-engineering`, ECC 2.2.3 installed local bundle, entrypoint SHA256 `114913bdcb6127392df56d96f7f1312f36c74d69c278dece6d377b9bd92123a5`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- The source's universal operating model became a process scoped to one target with its owner, acceptance and release gates read from the coordination record and the repository, so the output is actionable rather than ceremony.
- Review focus areas are mapped to named checks; generated-code regressions, data integrity and recovery each need a check or an open item, because an intent without a check was indistinguishable from coverage.
- Style review is delegated to the repository's resolved formatter and linter, keeping syntax automation separate from behavior review.
- "Hiring and evaluation signals" became capability signals for assigning work, with observable evidence locations, since this plugin does not run hiring.
- Reviewer verdicts and passing checks are stated as inputs to release coordination, never approval, per the plugin conventions.
- Coverage is reported as measured counts or `unmeasured`; the source's implied coverage expectations carried no measurement.
