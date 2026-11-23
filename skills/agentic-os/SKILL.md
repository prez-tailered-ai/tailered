---
name: agentic-os
description: Map a persistent multi-agent working setup onto the actual hosts, kernel instructions, specialist agents, commands, scheduled work and file state, each bound to an existing capability and the shared queue. Use when asked for an agentic OS, personal OS, persistent agent or multi-agent setup that survives restarts. Not for one bounded task loop; use continuous-agent-loop.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Agentic OS

Treat the host as a persistent working environment rather than a chat session. Kept from the source: five layers (kernel, agents, commands, scripts, state), a small declarative kernel whose routing lives in markdown tables, a memory scope per agent, append-only logs, decision records, add-never-rename schema evolution and end-of-session reflection. Each layer is bound to a capability the host already has; reading this skill activates no kernel identity, queue, scheduler, dispatch or memory store.

## When to Activate

- The user says "agentic OS", "personal OS", "persistent agent", "agent coordinator" or "multi-agent setup".
- A long-running project needs its identity, decisions and next action to survive a session restart.
- Work must be routed to specialist agents by declared rules inside one workspace.

Do not use for:
- one bounded attempt-check-adjust cycle on a single task: `continuous-agent-loop`;
- several agents producing one deliverable in parallel: `team-agent-orchestration`;
- enabling scheduling, dispatch, memory or computer control as capabilities: `autonomous-agent-harness`;
- a running service's lifecycle and rollout: `enterprise-agent-ops`;
- a recap of what a session did: `checklist-session`.

## Inputs and outputs

Required inputs: the workspace root and its instruction files (`AGENTS.md`, `CLAUDE.md`, the plugin skill list the host reports), the session's coordination record, and the recurring workflows the user wants routed. When one is missing, report the gap and stop at the layer that depends on it; do not guess a path or a workflow.

Output: a layer map (table) binding every layer to an existing host path or marking it "separately scoped capability" with its owner, plus one restart-continuity demonstration recorded with evidence labels from `../../references/conventions.md`.

## Steps

### 1. Inventory the layers the host already has

Resolve the real host first. In Claude Code the kernel is the loaded `CLAUDE.md` chain and commands are plugin skills or `.claude/commands/`; in Codex the kernel is `AGENTS.md` and commands are plugin skills. The workspace `AGENTS.md` and `CLAUDE.md` are the kernel; the shared queue record is the only task store. Record each layer's capability state (available, configured, loaded) as defined in the conventions.

Completion: a five-row table (kernel, agents, commands, scripts, state) names an existing path for each row or marks it absent.

### 2. Keep the kernel small and declarative

Write routing as a markdown table: agent, role, trigger phrase, the file that defines it. Routing in code is not used. The kernel file already belongs to the integration owner, so kernel changes are proposals in your coordination record until that owner applies them. The kernel declares no new identity; the session identity is the one recorded under the workspace rule.

Completion: the routing table is complete and the kernel change is either applied by its owner or recorded as Proposed.

### 3. Define each specialist agent with a memory scope

For each agent record identity, memory scope (the existing files it reads and the one place it appends), tool surface and constraints. An agent is "available" only when the host lists it; a markdown file nobody loads is Proposed.

Completion: every agent has identity, memory scope, tool surface, constraints and a discovery state.

### 4. Map commands to what the host discovers

Keep imperative command names. Verify a helper exists in the host before routing to it: list the host's commands or skills and match by name. The source's standard set (daily sync, research, decision log) is a candidate list, not an inventory.

Completion: each routed command has a verified host path or is marked Proposed.

### 5. Bind state to existing records

Status, owner and next action live only in the coordination record. Decisions and narrative logs are markdown in an allowed location; structured state is JSON. Logs are append-only. Evolve schemas by adding fields and marking old ones deprecated. Spend is logged only when the host reports it; otherwise mark it unavailable.

Completion: each kind of state names one existing location and no second board, queue or memory store exists.

### 6. Treat scheduled automation as a separately scoped capability

The source's LaunchAgent, systemd timer and process-manager examples are not setup instructions here. Record scheduling as a capability with its own target, owner, permission, budget, cleanup and acceptance, and hand the declaration to `autonomous-agent-harness`. Nothing is installed or started by this skill.

Completion: scheduling is recorded as Proposed with an owner, or as NOT APPLICABLE with the reason.

### 7. Demonstrate restart continuity

Start a fresh session and read only the kernel, the coordination record and the decision records. Reproduce identity, current decisions and the open next action; compare them to the record. A fact found only in an old log is Retained and is promoted to current only when the record or a decision confirms it. Append a reflection when the user asks or at closeout, not every turn.

Completion: the fresh read matches the record on identity, decisions and next action, with every stale fact labeled Retained.

## In the workflow

Supplies the Bind record of `tailered-ai:workflow`. Treat disk as a budget with owners: no test run when free disk is low, each run's temp folder named `tailered-<task>.*` and swept by its own runner, and another session's folders removed only on the owner's word after a backup copy.

## Anti-Patterns

- One agent that does everything; split by domain and route in the kernel table.
- A session that starts stateless; read the record and decisions first.
- A second task board or memory store beside the queue; keep status in the coordination record.
- Routing written as code; keep it in the markdown table.
- Credentials in the kernel or agent files; reference the secret by name and load it in the host.
- Installing a scheduler because the source describes one; declare the capability and its owner.
- Promoting an old log line to a current fact; confirm against the record first.

## Source and adaptation

Source: `agentic-os` from the ECC bundle 2.2.3 (installed local bundle). SHA256 of the source entrypoint: `e1d1207353652456ac84a821e5522def1d108677318630af4fd7ac16735b5c04`. License: MIT (see NOTICE.md at the plugin root).

- Mapped kernel, agents, commands, scripts and state to the actual hosts (Claude Code and Codex plugin skills, the workspace `AGENTS.md` and `CLAUDE.md`) because the source assumed a single Claude-only project layout.
- Made the shared queue record the only task store and removed the `data/` project database so no second board exists.
- Turned the LaunchAgent, systemd and pm2 scheduling examples into a separately scoped capability with its own owner and acceptance, since a skill starts no scheduler.
- Removed new kernel identity; the session identity is the queue record's own.
- Replaced "verify the standard command set" with verifying each helper exists in the host, and made reflection on-request rather than every session.
- Added capability states, evidence labels and the restart-continuity demonstration from the conventions.
