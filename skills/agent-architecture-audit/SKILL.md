---
name: agent-architecture-audit
description: Diagnose an agent or LLM feature whose failing layer is unknown by auditing the twelve-layer agent stack along the actual failure path, for wrapper regression, memory contamination, tool discipline failure, hidden repair loops and rendering mutation, and produce severity-ranked findings with evidence and code-first fixes. Not for a single failing run, which agent-introspection-debugging covers.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Agent architecture audit

Find which layer of an agent system corrupts the answer, show the mechanism with a source or trace reference, and order the fixes code-first. Kept from the source: the twelve-layer stack, the five common failure patterns, the four-phase workflow (scope, evidence, failure mapping, fix strategy), the severity model and the quick diagnostic questions.

## When to Activate

- An agent or LLM feature misbehaves and the failing layer is unknown.
- Behavior degraded after a prompt layer, tool definition or memory system was added.
- The same model behaves correctly in a direct call and incorrectly inside the wrapper.
- A hidden repair, retry or summarization pass is suspected of mutating responses.
- Before an agent stack goes to release review, when its owner asks for the audit.

Do not use for:
- A single failing run that needs capture and contained recovery: agent-introspection-debugging.
- Boundary validation and side-effect containment: agent-security-hardening.
- Comparing runs or models: agent-eval.
- Ordinary code review; the repository's own review process.

## Inputs and outputs

Required inputs; when one is missing, report the gap and scope the audit to what is available, without inferring the missing part:
- Target system, its entry points and the configured model identifiers, taken from the environment (Hosts and names in `../../references/conventions.md`).
- The reported symptom and the time window.
- Access to the source (agent loop, tool router, memory admission, prompt assembly), configuration (prompt templates, tool schemas, provider settings), logs or traces, and memory files.
- The owner of the runtime, who decides which fixes can be enforced in code.

Output: severity-ranked findings, the architecture diagnosis (which layer corrupted what and why), and an ordered fix plan, in that order, in the shape given in [references/report-schema.md](references/report-schema.md).

## Steps

### 1. Scope the audit to the failure path

Record target, entry points, configured model stack, symptom and time window. From the twelve layers, choose the ones on the path the symptom actually crosses; mark the rest NOT APPLICABLE with the reason before any evidence is read.

| # | Layer | What goes wrong |
|---|-------|-----------------|
| 1 | System prompt | Conflicting instructions, instruction bloat |
| 2 | Session history | Stale context injected from earlier turns |
| 3 | Long-term memory | Pollution across sessions, old topics in new conversations |
| 4 | Distillation | Compressed artifacts re-entering as pseudo-facts |
| 5 | Active recall | Redundant re-summary layers wasting context |
| 6 | Tool selection | Wrong tool routing, required tool skipped |
| 7 | Tool execution | Claimed call never executed |
| 8 | Tool interpretation | Tool output misread or ignored |
| 9 | Answer shaping | Format corruption in the final response |
| 10 | Platform rendering | Transport-layer mutation of a valid answer |
| 11 | Hidden repair loops | Silent fallback or retry running a second model pass |
| 12 | Persistence | Expired state or cached artifacts reused as live evidence |

Completion: a scope block naming the audited layers and the reason each excluded layer is off the path.

### 2. Collect evidence from the audited layers

Read the source, configuration, logs and memory files for the chosen layers. Search for tool requirements stated only in prompt text, tool calls executed without validation, model calls outside the main loop, memory admission that lets agent assertions outrank user corrections, fallback or re-prompt paths, and output rewriting before delivery. Use the repository's own search tool; record each hit with its file and line or log and row. The patterns to recognize are in [references/failure-patterns.md](references/failure-patterns.md).

Completion: every evidence item has a location reference and is labelled Fresh or Retained per `../../references/conventions.md`.

### 3. Map each finding to its mechanism

For each finding record the symptom, the mechanism by which the wrapper causes it, the source layer, the root cause, the evidence references, and a severity. State in words what the evidence shows and what remains uncertain, naming the observation that would settle it; the report carries no numeric confidence. A clean current state does not erase a dirty historical incident found in logs.

Completion: each finding has evidence references and a separate evidence/uncertainty statement; findings without evidence are listed as hypotheses, not findings.

### 4. Order the fixes code-first

Default order: gate tool requirements in code where the owned runtime can enforce them; make hidden repair agents explicit with contracts or remove them; reduce context duplicated across prompt, history, memory and distillation; tighten memory admission so user corrections outrank agent assertions; tighten distillation triggers; make rendering pass-through; convert internal flow to typed envelopes. A rule that exists only in prompt text is recorded as advisory; a code gate is required only where the owned runtime can enforce it, and otherwise the gap is named for the runtime owner.

Completion: an ordered fix plan where each item names its goal, why now, expected effect, and whether it is runtime-enforced or advisory.

### 5. Report by severity

Lead with the most severe finding. Severity model: critical, the agent can confidently produce wrong operational behavior, fix before the next release; high, correctness or stability frequently degrades, fix in the current cycle; medium, correctness usually survives but output is fragile or wasteful, plan for the next cycle; low, cosmetic or maintainability, backlog. The report is a diagnosis for the owner; release decisions stay with release authority in `../../references/conventions.md`.

Completion: findings ranked by severity, then the diagnosis, then the fix plan, with no leading summary or compliment.

## Anti-Patterns

- Blaming the model first; falsify wrapper-layer regression before any model claim.
- Blaming memory without the contamination path; show where the old content entered.
- Calling a prompt-text "must use tool" rule enforcement; name it advisory and gate it in code where the runtime allows.
- Attaching a confidence number; state the evidence and the uncertainty in words.
- Auditing all twelve layers by default; scope to the failure path and justify exclusions.

## Source and adaptation

- Source: agent-architecture-audit, ECC 2.2.3 installed local bundle (origin oh-my-agent-check).
- SHA256: `64f57e232c3533877403703bc95b3c75df9de23f657899a306f13c703009ff57`
- License: MIT (see NOTICE.md at the plugin root)
- Adaptations:
  - The twelve-layer table, failure patterns and severity model are kept; audited layers are scoped to the actual failure path with justified exclusions, replacing the mandatory full audit and the "15 minutes of debugging" trigger.
  - The numeric confidence field was dropped in favor of an evidence/uncertainty statement per finding; the JSON report shape moved to `references/report-schema.md`.
  - Code gates are required only where the owned runtime can enforce them; prompt-only rules are labelled advisory.
  - Tool-specific search commands were replaced with the repository's own search tool and a pattern reference.
  - Model stack is resolved from the environment; external skill handoffs removed.
