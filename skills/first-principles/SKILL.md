---
name: first-principles
description: "Use when a limit or practice that is not a price is defended only by precedent or authority (\"everyone does it this way\", \"that's how it works\", \"can't be done\"), when the owner says first principles about a limit, practice or design, or when a new requirement must join an existing design, codebase or document. Not for a vendor quote or what something should cost, use tailered-ai:raw-cost-floor; not for a verified hard limit, an ordinary feature (use tailered-ai:lockin build), an incident, or a whole plan (use tailered-ai:strategy-red-team)."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# First principles

Two branches, one habit: refuse to inherit a constraint or a structure without checking why it exists. **Rebuild** strips claimed constraints down to what is independently supported and builds again from that. **Redesign** integrates a new requirement as if it had been a founding assumption, instead of bolting it on.

## When to Activate

| Branch | Use when |
|---|---|
| rebuild | a limit is treated as fixed on the strength of precedent or authority (a price goes to `tailered-ai:raw-cost-floor`); convention keeps failing or yields only small variants; greenfield work where industry defaults may smuggle false requirements |
| redesign | a new requirement must join an existing design, document or codebase, especially one whose stated rationale it contradicts |

Do not use for:
- a vendor quote or what something should cost: `tailered-ai:raw-cost-floor`;
- a constraint that is verified physics, hard regulation or measured capacity: accept it and optimize within it;
- an ordinary feature that fits the current design: tailered-ai:lockin build;
- a case where a proven standard library, protocol or pattern already fits: use it;
- an incident in progress: act on the likeliest cause first, and rebuild after;
- attacking a whole plan: tailered-ai:strategy-red-team.

## Inputs and outputs

Input: the problem and its claimed constraints (rebuild), or the existing design and the new requirement (redesign). For redesign, the affected files or sections; read them all before step 5.

Output (rebuild): six named parts, `claimed_constraints`, `primitives`, `discarded_assumptions`, `rebuild`, `binding_residuals` and `kill_test`. Output (redesign): the from-scratch design, the propagation list and the delivery order. Both in the reply; redesign edits files only when the user asked for the change to be made.

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, fetch the missing inputs you can reach yourself, and end with the one or two you could not reach that would change the result.

## Steps

### 1. Pick the branch

Match the request to the table. A request can need both: rebuild a constraint first, then redesign around the result.

Completion: the reply names the branch once.

### 2. Rebuild: state and tag every constraint

List every limit treated as fixed: cost, scale, stack, process, "must use X". Split a claim that mixes two reasons into one row per reason, then tag each with exactly one of five tags:
- `physics/math`: follows from physics, arithmetic or complexity bounds;
- `regulation/contract`: a law, licence, signed term or published terms of use;
- `measured fact`: a measurement taken or read in this run, with its source;
- `owner requirement`: something the owner has decided they need (a deadline, a quality bar, a scope);
- `convention/authority`: price, precedent, habit, a vendor's or an expert's say-so.

The first four bind. An `owner requirement` binds until the owner changes it; you may question it, with the observation that would justify changing it, but never discard it yourself. `convention/authority` binds only when evidence upgrades it. Write the result as a table:

| Constraint | Tag | Support |
|---|---|---|
| "we have to use Kubernetes" (team habit) | convention/authority | how earlier projects were run |

Completion: every claimed constraint is a table row with exactly one of the five tags, and every `measured fact` row names its measurement.

### 3. Rebuild: decompose to primitives

Write the true requirements: required inputs, volumes and rates, bounds from conservation or complexity, owner requirements, and real non-negotiables. Each primitive cites its support: a measurement, a derivation, or the owner's stated requirement. For each discarded convention, write the observation that would falsify discarding it.

Completion: every primitive cites support that is not precedent alone, and every discarded assumption has its falsifier.

### 4. Rebuild: build again and stop

Build the simplest solution that satisfies the binding constraints and ignores the artificial ones; prefer commodity inputs and fewer moving parts. Keep the binding residuals in view, and do not wish a real contract or law away. Name the single cheapest test that would falsify the rebuild, and what it costs in hours or dollars, or `not measured`. Stop after one pass unless new evidence arrives.

Completion: the reply shows all six output parts under their names, the rebuild uses only primitives, and one kill test is named with its cost or `not measured`.

### 5. Redesign: design it from scratch

Read every affected file or section. Ask: if this requirement had been there from the start, what would we have built? Write that design in a few lines. Name every existing statement it makes false, rationale sections first: a rationale such as "one warehouse, so stock is a single number" stops being true the moment the requirement adds a second one.

Completion: the from-scratch design is written, and every contradicted statement is listed with its location.

### 6. Redesign: propagate and deliver in increments

List every place the change must reach: types, storage, interfaces, docs, examples, tests and rationale. Then order the work so each increment ships on its own and leaves the design coherent. When the user asks for a smaller bolt-on, give it, and state what it leaves open against the from-scratch design.

Completion: the propagation list covers every kind of place named above that exists in this design, each increment has its own check, and any bolt-on names its gaps.

## Anti-Patterns

- Accepting a vendor's or the industry's price as physics.
- Tagging the owner's own requirement as convention and then discarding it.
- A primitive whose only support is "that is how others do it".
- Wishing away a real contract, licence or law.
- Rebuilding for novelty when a standard solution already fits the verified constraints.
- Bolting a requirement on and leaving the old rationale standing.

## Source and adaptation

Rebuild branch source: `thinking-first-principles` from tjboudreaux/cc-thinking-skills, commit `7b8fece345dfaa11773be7152ccd194589cb5437`, SKILL.md SHA256 `a3fd307e169b420a9eebce847849a6778435fe83cf8e1d130d59e98453e617cb`. License: MIT, Copyright (c) 2025 TJ Boudreaux (see NOTICE.md at the plugin root).

Redesign branch source: `principle-redesign-from-first-principles` from cursor/plugins, commit `2776ddd2355d6d6c8747d3964600f28daf62f049`, path `harness/pstack/claude-code/skills/`, SKILL.md SHA256 `170e0a658783e43fee8ec5a8c2422a4abb8f69cef621dd1819a95910b8207034`. License: MIT, Copyright (c) 2026 Lauren Tan, from `pstack/LICENSE` and `harness/pstack/claude-code/LICENSE` at that commit (SHA256 `bc957ca6bee02792566a1a028d105e02e247c6e77cf057061674273da77b200e`; see NOTICE.md). The branch is written in Tailered AI's own wording.

Changes: the two sources merged into one skill with two branches; restructured into the house step form with completion criteria; the four-tag set gained `owner requirement`, and `convention/analogy/authority` was shortened to `convention/authority`; added the falsifier per discarded assumption, the cost of the kill test, the contradicted-rationale check and the bolt-on gap rule; the sources' `disable-model-invocation` key was dropped for this plugin's fixed frontmatter, and the triggers were narrowed to business and technical constraints.
