---
name: autonomous-agent-harness
description: Scope an autonomous agent setup as four separate capabilities, memory, scheduler, dispatch and computer control, each with its own target, owner, permission, budget and recovery, inside an explicit consent boundary. Use when asked to run something continuously, on a schedule, keep monitoring, or remember across sessions. Not for designing workspace layers and routing; use agentic-os.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Autonomous Agent Harness

Combine the host's session tools with separately configured memory, scheduling, dispatch and computer-control integrations. Kept from the source: the consent boundary, the four-component architecture plus a task list, dry-run plans before anything recurring, and the constraints on session scope, permissions, usage limits and bounded memory. This is a declaration pattern; reading it enables no persistent task, computer access, private-data ingestion or remote message.

## When to Activate

- The user asks for an agent that runs continuously, on a schedule, or "keeps monitoring" something.
- The user wants context remembered across sessions or a recurring workflow triggered without them present.
- A capability request names scheduling, dispatch, memory or computer control.

Do not use for:
- the layer map and routing of a persistent workspace: `agentic-os`;
- one bounded loop inside the current session: `continuous-agent-loop`;
- a running service's lifecycle, observability and rollout: `enterprise-agent-ops`;
- a one-off browser action the host already provides: the host's browser tool.

## Inputs and outputs

Required inputs: the user's consent statement (which capability, which target workspace, which actions), the session's coordination record, and the host's reported tool and permission surface. When consent is absent, record the request as Proposed and stop; when the host surface is unknown, list what the host reports before declaring anything.

Output: one capability declaration per requested capability using [the declaration template](references/capability-declaration.md), and a state ledger in which declared, scheduled, dispatched and completed are separate observed entries with evidence labels from `../../references/conventions.md`.

## Steps

### 1. Record the consent boundary

Write what the user approved: capability, target workspace, allowed actions, forbidden actions, and whether private communications or personal data are in scope. Credentials, workspace exports and account-specific automations stay out of reusable artifacts.

Completion: the consent record names capability, target, allowed and forbidden actions, and is quoted from the user's words.

### 2. Declare each capability separately

For memory, scheduler, dispatch and computer control fill the template: target, owner, permission, budget (runs, elapsed time, spend, effects), recovery, cleanup and offline or isolated acceptance. A capability without an owner or a budget is unavailable, not pending.

Completion: every requested capability has all template fields, or is marked unavailable with the missing field named.

### 3. Bind memory to the host's existing store

Use the host's own memory location and the coordination record. The source's structured memory server is a separately owned dependency: name it, its owner and its acceptance, and install nothing. Keep memory concise; archive instead of growing files without bound.

Completion: memory names one existing location per kind (preferences, project context, task status) and no new store is created.

### 4. Declare scheduling without starting it

A session-scoped recurring prompt ends with the session; independent runs need an external scheduler on a target someone owns. Record interval, workspace, allowed actions and the authentication and permissions the runner uses. The skill starts no cron, watcher or scheduled wake-up; the owner enables it under its own acceptance.

Completion: the scheduler entry has interval, target, owner, permission, budget and recovery, and its state is `declared`.

### 5. Declare dispatch as a one-shot invocation

Dispatch means an authenticated runner invokes the host's programmatic mode in a workspace it owns with a prompt and a bounded budget. Record the trigger source, the workspace and who reads the result. A dispatched run is not completed until its output is inspected.

Completion: each dispatch entry names trigger, workspace, budget, reader and the expected output artifact.

### 6. Declare computer control in an isolated environment

Computer control needs a separately configured, isolated environment with explicit permission grants; naming a package supplies none of that. Verify one harmless action there before any workflow depends on it.

Completion: the entry names the environment, its owner, the granted permissions and the harmless verification result, or is marked unavailable.

### 7. Keep the task list in the coordination record

Persistent tasks live in the session's queue record under the workspace rules. Each task has an owner, a stop condition and a next action; a memory file holding a parallel task list is not created.

Completion: every persistent task appears in the coordination record and nowhere else.

### 8. Observe states and verify each run

Record `declared`, `scheduled`, `dispatched` and `completed` as separate entries with Fresh or Retained evidence; a schedule entry proves scheduling, not completion. Each run states its limits and failure owner; a repeated same-cause failure stops the dependent capability until its owner acts.

Completion: the state ledger shows which state each capability actually reached and what evidence proves it.

## Anti-Patterns

- Treating adoption of this skill as consent; record the user's explicit approval per capability first.
- One declaration covering memory, scheduler, dispatch and computer control; declare four.
- Registering a memory server or scheduler because the source showed the configuration; name the dependency and its owner.
- Calling a cron entry "done"; completion is an inspected result.
- A second task list in memory files; the coordination record holds tasks.
- Forwarding private messages or calendar data into reusable artifacts; keep them in the approved target only.

## Source and adaptation

Source: `autonomous-agent-harness` from the ECC bundle 2.2.3 (installed local bundle). SHA256 of the source entrypoint: `74afde3fa6e8423bdbf43f53b24c7b4a8b441648a1ad8f23953dc6eba3378409`. License: MIT (see NOTICE.md at the plugin root).

- Preserved the consent boundary and made memory, scheduler, dispatch and computer control four separate declarations, each with target, owner, permission, budget, recovery and cleanup.
- Made declared, scheduled, dispatched and completed separate observed states because the source treated a schedule entry as operation.
- Removed the "Replacing Hermes" framing, the memory-server npm registration, the GitHub webhook and pull-request workflows and the CI-runner examples, which assumed platforms not in use.
- Replaced the memory-file task queue with the shared coordination record.
- Kept the source's constraints on session scope, permission grants, usage limits and bounded memory as step completions.
