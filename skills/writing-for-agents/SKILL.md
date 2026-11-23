---
name: writing-for-agents
description: "Write or edit a document an agent consumes, a skill, an AGENTS.md or CLAUDE.md, or a file reached by a pointer, so each run takes the same path: sharp context pointers, material placed on the information hierarchy, steps that end on checkable completion criteria, leading words, positive wording and pruning. Use when creating or editing such a document. Includes /handoff-fable for saving or refreshing a Fable project packet and exact launch prompt. Not for prose written for people only."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Writing for agents

Make a document predictable for the agent that runs it: the same process every run, not the same output. The source's concepts are kept in compressed form: context pointers and their branches, the two loads (context and cognitive), the information hierarchy with progressive disclosure and co-location, completion criteria with clarity and demand, splitting by sequence, leading words, positive wording over prohibition, and pruning for single source of truth, environment caches, relevance and no-ops. The skill-specific branch (invocation choice, splitting by invocation, router skills) is read from [skill mechanics](references/skill-mechanics.md) when the document is a skill.

## Handoff branch

For `/handoff-fable`, or a request to save or refresh a Fable handoff and its exact launch prompt, follow [the handoff workflow](references/handoff-fable.md). For prompt-only requests, return the saved prompt; for ordinary document edits, continue below. This is instruction syntax within Writing for Agents, not a separate native slash-command registration.

## When to Activate

- Creating or editing a skill in this plugin or in a project.
- Modifying an `AGENTS.md`, `CLAUDE.md` or another always-loaded instruction file.
- Writing a reference document that a pointer in one of those files will reach.
- Adapting a source document into one of the above and deciding what to keep, compress or disclose.

Do not use for:
- Prose for human readers only (reports, release notes): the house reporting rules in `../../references/conventions.md`.
- Rating a finished output: agent-self-evaluation.
- Setting ownership, release or evidence policy: the conventions file itself, edited by its integration owner.

## Inputs and outputs

Required inputs:
- The document kind and where it loads: always-loaded (an instruction file, a skill description) or disclosed (reached by a pointer).
- The branches it serves: the distinct cases that make different runs take different paths.
- Representative fixtures: at least one prompt per branch and one prompt that must leave the pointer unfired.
- When adapting a source: its license, confirmed from the distribution before copying more than concepts.

When the branches or fixtures are unknown, write them down as the first output and confirm them before drafting; a pointer with unknown branches cannot be tested. When the license is unconfirmed, keep to concepts in your own wording and record the gap.

Output: the document, its pointer text, and a fixture check showing which pointer fires on which fixture and which reference file each branch reaches.

## Steps

### 1. Bind the document, its load and its branches

Name the kind, the load it spends (context load for always-loaded text, cognitive load for material a person must remember to reach), and the branches. Cognitive load is spent where human judgement matters and removed where it does not.

Completion: kind, load and the branch list are written, with one fixture per branch and one negative fixture.

### 2. Place every piece on the information hierarchy

Sort the content into steps (ordered actions) and reference (definitions, rules, facts). Put steps in-file first. Inline the reference every branch needs; disclose behind a pointer what only some branches reach. Keep a concept's definition, rules and caveats under one heading (co-location). Watch for sprawl: a document too long even with every line live; cure it by disclosing reference and splitting by branch or sequence.

Completion: each piece has a tier (in-file step, in-file reference, disclosed reference), disclosed pieces have a named file, and related material sits under one heading.

### 3. Write the pointers

A pointer states what the material is and the branches that trigger reaching it; its wording, not its target, decides when the agent reaches it. Lead with the triggering word, keep one trigger per branch, and cut identity the body already carries. When a must-have target sits behind a weak pointer, sharpen the wording first and inline only if sharpening fails. Test every pointer against the fixtures.

Completion: each fixture reaches only the reference its branch needs, the negative fixture fires nothing, and every pointer path resolves to an existing file.

### 4. End every step on a completion criterion

Give each step a bound the agent can tell done from not-done with (clarity) and that requires the full work (demand): "every modified file accounted for" over "produce a list". A vague bound invites premature completion toward the visible later steps; sharpen the bound first, and split the sequence across a real context boundary only when the rush is observed. A flat body of reference takes its own bar: "every rule applied".

Completion: every step ends on a checkable, exhaustive criterion, and any split is justified by an observed rush.

### 5. Choose leading words and positive wording

Replace spelled-out triads and gestures with one pretrained word the agent already thinks with (a tight loop, a red test), repeated as a token; coin a word only with a clear definition. State the target behavior positively; keep a prohibition only as a hard guardrail and pair it with the positive action.

Completion: restated passages are collapsed to leading words, and every prohibition is paired with its positive target.

### 6. Prune

Keep one authoritative home per meaning across the document and its projections (manifests, README lines, sibling skills): point to it rather than restate it. Treat the environment (scripts, config, directory layout, help output) as a source of truth and cache only what the agent cannot look up: the unwritten convention, the reason, the gotcha. Check every line for relevance to remove sediment. Delete whole sentences that fail the no-op test (would the agent behave differently without it?), and strengthen a leading word that is too weak to beat the default.

Completion: no meaning has two homes, no line restates a cheap lookup, and every remaining sentence changes behavior.

### 7. Read it as the agent and record the fixture check

Run each fixture through the finished document: follow the pointers, do the steps, check each criterion. Record which pointer fired, which file was reached and where a step's criterion was unclear. Fix and rerun until the record is clean.

Completion: the fixture record shows each branch reaching only its relevant material and every criterion checkable.

## Anti-Patterns

- Inlining everything so the top of the file bloats; instead disclose what only some branches need behind a sharp pointer.
- Writing a pointer with synonyms for one branch; instead keep one trigger per distinct branch.
- Ending a step on "understanding reached"; instead end it on a condition the agent can check.
- Steering by prohibition; instead state the target behavior and keep a ban only as a paired guardrail.
- Restating `package.json` scripts or policy that lives in the conventions file; instead point to the source of truth.
- Keeping stale layers because removal feels risky; instead prune line by line for relevance.

## Source and adaptation

Source: `writing-for-agents`, local agent skills distribution (mattpocock/skills), entrypoint SHA256 `551adca942227b44192edba88acd4e8db911f0121ce58ad16944ccf6a896a74a`, with `SKILL-MECHANICS.md` and `agents/openai.yaml`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- The all-reference source was restructured into the plugin's step form with completion criteria, keeping every concept (context pointers, the two loads, information hierarchy, progressive disclosure, co-location, sprawl, completion criteria, splitting, leading words, negation, pruning) in compressed wording with attribution.
- The skill-specific branch was moved to `references/skill-mechanics.md` and adapted to this plugin's fixed frontmatter keys and to host-dependent invocation mechanics.
- A fixture check was added so pointer branches are tested against representative prompts, and a single-source rule now covers projections such as manifests and README lines.
- A license-confirmation input was added before substantial copying, per the writer brief.
- `agents/openai.yaml` (display name and short description for one host) was not carried over; this plugin's hosts read the frontmatter.

## Done means

Each item names the text that must appear in the transcript before this skill counts as done (checked by `tools/change_checks.py done`).

- Branches or fixtures written before drafting: `fixture`
