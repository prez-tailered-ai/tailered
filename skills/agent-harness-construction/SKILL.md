---
name: agent-harness-construction
description: Design or revise an agent's action space, tool contracts, observation shape and error recovery, mapped to the tools the host already has. Use when defining or changing a tool set, an action schema, or how tool output is read back and acted on. Not for diagnosing a run that is already failing, which agent-introspection-debugging covers.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Agent harness construction

Produce a harness specification that makes an agent's actions narrow, its observations typed and its errors recoverable, using the tools the running host already provides. Kept from the source: the four quality constraints (action space, observation, recovery, context budget), the granularity rules, the four observation fields, the error-recovery contract and the architecture-pattern guidance.

## When to Activate

- An agent's tool set or action schema is being defined or revised.
- Tool output is opaque, tools overlap, or retries do not converge on completion.
- A high-risk action (deploy, migration, permission change) is being added and needs its own narrow tool.

Do not use for:
- A run that is failing now and needs a diagnosis: agent-introspection-debugging.
- Finding which layer of a running stack corrupts answers: agent-architecture-audit.
- Validating inputs at action boundaries and proving side-effect containment: agent-security-hardening.
- Comparing completion rates across runs or models: agent-eval.

## Inputs and outputs

Required inputs; when one is missing, report the gap and stop at the step that needs it, never guess a tool name or invent a runtime:
- The host and its actual tools: the tool list the host exposes, tool servers configured in the repository, and repository scripts.
- The task family the agent performs and the owner of the harness (see Ownership in `../../references/conventions.md`).
- Existing action or tool definitions, by path, when any exist.
- The acceptance that judges a completed task.

Output: a harness specification (action table, observation contract, error contract, one failure walkthrough, context budget, architecture choice) written where the owner names, plus changed tool definitions in the framework's own format. The skill creates no runtime, scheduler, worker pool or queue.

## Steps

### 1. Bind the host, tools and task family

List every tool the agent may use and record its capability state (available, configured, loaded or invoked, per `../../references/conventions.md`). Name the harness owner and state the task family in one sentence.

Completion: a list of real tools with states, one owner, one task-family sentence.

### 2. Shape the action space

Apply the four rules: stable explicit names, schema-first narrow inputs, deterministic output shapes, no catch-all tool unless isolation is impossible. Assign granularity: micro-tools for high-risk operations, medium tools for edit/read/search loops, macro-tools only where round-trip overhead dominates. Map each action to one existing host tool or repository command; an action with no host tool is recorded as a gap with its separate owner, not created by instruction.

Completion: every action has a name, input schema, granularity class and either a mapped host tool or a recorded gap.

### 3. Write the observation and error contracts

Use the templates in [references/contracts.md](references/contracts.md). Every result carries `status`, `summary`, `next_actions` and `artifacts`, and is validated against its schema before the agent reads it. A result that fails validation, is truncated, or is empty when content was expected becomes a typed error naming the tool, the boundary and the reason; it never becomes a success with empty content. Every error path carries a root-cause hint, a safe retry instruction and an explicit stop condition.

Completion: input, result and error contracts exist for every action, and the malformed-observation case is written with its typed error.

### 4. Walk one representative failure

Pick the failure most likely in this task family (for example truncated output from a search tool). Write the sequence: observation, classified error, recovery action, then the stop condition. Bound the recovery with the limits in Bounded execution of `../../references/conventions.md`: attempts, elapsed time, spend and effects, plus who owns the failure once the bound is reached.

Completion: a written walkthrough with a finite attempt count, a named stop condition and a named failure owner.

### 5. Budget the context

Keep the invariant system prompt minimal; move long guidance into skills loaded on demand; point to files instead of inlining documents; compact at phase boundaries rather than at arbitrary token thresholds.

Completion: a two-column list of what stays in the invariant prompt and what loads on demand.

### 6. Choose the architecture pattern and name the measures

Choose ReAct for exploratory tasks with an uncertain path, function-calling for structured deterministic flows, or the hybrid (ReAct planning with typed tool execution) by default, and give the reason. Name the measures to track: completion rate, retries per task, pass@1 and pass@3, cost per successful task. Label each measured only when runs exist, configured when a target is set, otherwise unavailable; the specification carries no invented numbers.

Completion: one architecture choice with its reason, and each measure labelled measured, configured or unavailable.

## Anti-Patterns

- Several tools with overlapping semantics; give each responsibility one tool.
- Opaque output; return status, summary, next actions and artifacts.
- Error output with no next step; pair every error with a recovery hint and a stop condition.
- Malformed or empty observation read as success; return a typed error.
- Creating a runtime, worker pool or queue by instruction; map to host tools and record gaps for their owner.
- Reporting completion rates or costs no run produced; mark them unavailable.

## Source and adaptation

- Source: agent-harness-construction, ECC 2.2.3 installed local bundle.
- SHA256: `e7fb390a6663b46ea5d3c2876753a5ce32ba3bad1889686b21a42894caa1742d`
- License: MIT (see NOTICE.md at the plugin root)
- Adaptations:
  - Added required inputs, a bound-to-host step and a mapped-or-gap rule so actions resolve to existing tools instead of describing a runtime.
  - Made the observation contract a validation gate: malformed or empty output becomes a typed error, never empty success.
  - Added one representative failure walkthrough with bounded recovery and a real stop condition, tied to the shared bounded-execution limits.
  - Benchmark measures are labelled measured, configured or unavailable; no numbers are supplied by the skill.
  - Observation and error templates moved to `references/contracts.md`.
