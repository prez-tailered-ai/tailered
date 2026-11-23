---
name: agent-sort
description: Classify the skill, command, rule and hook surface actually installed for one project into DAILY and LIBRARY with repository evidence, mapped to the local tailered-ai plugin route and the session's existing coordination record. Use when a project loads more than it uses or needs a repeatable load decision. Not for writing or adapting a skill, which writing-for-agents covers.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Agent sort

Sort the installed agent surface of one project into two buckets backed by evidence from the actual codebase: DAILY loads every session, LIBRARY stays accessible without loading by default. Kept from the source: the repository as the single source of truth, the two-bucket model, the evidence table, the six review passes (agents, skills, commands, rules, hooks and scripts, extras), the load plan and the verification report.

## When to Activate

- A project loads a full bundle of skills, rules or hooks and only a subset matches its stack.
- A repository has drifted into the wrong language rules or hook set.
- A team wants a repeatable, evidence-backed load decision instead of hand-curation.

Do not use for:
- Writing or adapting a skill body: writing-for-agents.
- Auditing whether a loaded skill behaves correctly: agent-architecture-audit.
- Removing installed surfaces from a shared host; that is a separate change by the surface's owner, recorded in the coordination record.

## Inputs and outputs

Required inputs; when one is missing, report the gap and leave the affected rows unclassified:
- The project path and its repository evidence (lockfiles, framework configs, CI and hook configs, build and test scripts, dependency manifests, stack docs).
- The installed surface, enumerated from where the host actually loads it: the tailered-ai plugin skills, other plugin directories, project and user skill, command, rule and hook directories. A skill, hook or script that a document merely mentions is not part of the surface.
- The session's coordination record (Ownership in `../../references/conventions.md`), which holds the decision and its next action; no second board.

Output, in this order: STACK summary, DAILY inventory with evidence, LIBRARY inventory with evidence, LOAD PLAN, VERIFICATION. Each inventory row is `path | type | bucket | repository evidence | justification`.

## Steps

### 1. Read the repository stack

Establish languages, frameworks, package manager, test stack, lint and format stack, runtime surface and operator integrations present, from files in the repository, not from preference. Translate any platform assumption in a candidate surface to the actual target per Hosts and names in `../../references/conventions.md`.

Completion: a STACK summary where every line cites a repository file.

### 2. Enumerate the installed surface

List every candidate with its path and type, grouped for the six passes: agents, skills, commands, rules, hooks and scripts, extras (contexts, examples, tool-server configs, templates, guidance docs). Record each candidate's capability state (available, configured, loaded) as observed in the host. Run the passes sequentially, or in parallel where the host offers bounded subagents, with the limits in Bounded execution of `../../references/conventions.md`.

Completion: every candidate has a path, a type, a pass and an observed state; nothing listed comes from a mention alone.

### 3. Build the evidence table

For every candidate record the path, type, proposed bucket, repository evidence and a short justification, for example:

```text
skills/frontend-patterns | skill | DAILY   | component files and framework config present | core stack
rules/python/*           | rules | LIBRARY | no Python source, no Python manifest         | keep accessible
```

Completion: every DAILY row cites concrete repository evidence; every LIBRARY row states why it is not daily.

### 4. Decide DAILY versus LIBRARY

DAILY when the repository clearly uses the matching stack, the component helps every session, and the repository already depends on the corresponding runtime or workflow. LIBRARY when the component is off-stack, is needed only occasionally, or adds context without immediate relevance. LIBRARY means accessible, not deleted or unavailable.

Completion: every row is in exactly one bucket and the two inventories are written.

### 5. Write the load plan on the existing route

DAILY skills stay loaded through the route the host already uses: the tailered-ai plugin (`/tailered-ai:<skill>` in Claude Code, `$tailered-ai:<skill>` in Codex) or the project's own skill directory. DAILY rules are limited to matching language sets; DAILY hooks and scripts are limited to ones the repository can run. LIBRARY surfaces stay reachable by explicit invocation on the same route or by search. When the project wants a router, it is a short index of triggers and locations, never a copy of skill bodies. Any installation, removal or hook change is listed as a proposed action for its owner, with no change applied by this skill; nothing is installed because a source mentions it.

Completion: a LOAD PLAN listing keep, propose-install, propose-remove and route-via-library per row, each proposal naming its owner.

### 6. Verify and record

Check that every DAILY file exists where the host loads it, that off-stack language rules are not active, that incompatible hooks are not active, and that the result matches the STACK summary. Report DAILY count, LIBRARY count, proposed removals and open questions, and write the decision and next action to the session's coordination record.

Completion: a VERIFICATION section with each check marked PASS, FAIL or BLOCKED, and the coordination record updated.

## Anti-Patterns

- Classifying from what "feels useful"; cite a repository file for every DAILY row.
- Reading LIBRARY as removal; keep the surface reachable and route to it.
- Installing a hook, rule, command or script because a source document names it; list it as a proposal for its owner.
- Creating a second install system, board or router that duplicates skill bodies; use the existing plugin route and the coordination record.
- Counting a staged or mentioned surface as loaded; record the observed capability state.

## Source and adaptation

- Source: agent-sort, ECC 2.2.3 installed local bundle.
- SHA256: `5847fc20cf0fd0d00c0c2dbacca03472c5a43af429978cf874dd41ecc144dc53`
- License: MIT (see NOTICE.md at the plugin root)
- Adaptations:
  - The classified surface is what is actually installed in the host for the project, enumerated from load locations; mentions in documents are excluded.
  - The install plan became a load plan on the existing tailered-ai plugin route; installations and removals are proposals for their owner, applied by no step here.
  - The decision is recorded in the session's existing coordination record instead of a new artifact set; handoffs to external skills were removed.
  - Example search commands that assumed a specific tool and stack were replaced by repository-file evidence.
