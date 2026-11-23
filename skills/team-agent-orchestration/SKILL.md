---
name: team-agent-orchestration
description: Coordinate several agents on one deliverable through the existing shared queue, work items with one owner, disjoint files, dependency-ready acceptance, an inspected disposition for every received output and one integration owner. Use for multi-agent fan-out, squad or agent Kanban coordination, or merging agent output into one product. Not for one agent's bounded loop; use continuous-agent-loop.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Team Agent Orchestration

Manage agents like a team with narrow contracts. Kept from the source: owner, scope, state, evidence and merge gate per work item; the seven-step flow from shaping to extraction; the control view requirements; and the failure modes (agent soup, invisible work, board theater, overlapping writes, no product artifact). The board is the existing shared queue; the source's Kanban columns are translated onto its statuses rather than kept as a second board.

## When to Activate

- A task spans several agents, harnesses, branches or worktrees.
- The user mentions team orchestration, agent Kanban, squad, conductor, control pane or multi-agent work.
- Agent fan-out is producing output that is not becoming one mergeable product.

Do not use for:
- one agent iterating on one task: `continuous-agent-loop`;
- the persistent layer map of a workspace: `agentic-os`;
- scheduled or dispatched runs outside the session: `autonomous-agent-harness`;
- a session recap of what was done: `checklist-session`.

## Inputs and outputs

Required inputs: the deliverable and its acceptance, the orchestrating session's coordination record, the list of agents actually available in the host, and the file tree the work touches. When the acceptance or the file list is missing, report the gap before assigning anything; an assignment without disjoint files is not made.

Output: work items in the coordination record (one owner, status, files, acceptance, merge gate), a disposition entry for every received output, and an integration report with merged and pending items, evidence, blockers with owner and next action, and reusable candidates.

## Steps

### 1. Shape the work items

Convert the ambition into items with title, acceptance, merge gate, dependencies and the files each may write. Dependency-ready means every input an item needs is named and either exists or is another item.

Completion: every item has acceptance, merge gate, dependencies and a file list.

### 2. Translate the board onto the queue

Record each item in the coordination record under the workspace rules with the queue status instead of a Kanban column:

| Source column | Queue status | Exit condition |
| --- | --- | --- |
| Backlog | `idea` | acceptance written |
| Ready | `open` | owner and files assigned |
| Running | `claimed`, then `in_progress` | handoff artifact and changed files exist |
| Review | `handed_over` (to the integration owner) | gates pass, diff inspected |
| Blocked | `blocked` | blocker has owner and next action |
| Merged | `complete` | integrated by the integration owner |
| Archived | `abandoned` | reason recorded |

The card fields map to the record's `id`, `title`, `status`, `needs`, `files` or `branch`, `claimedAt` and `takenFrom` or `with`; acceptance and merge gate go in the item's description.

Completion: every item is in the record with a queue status and no second board exists.

### 3. Assign boundaries

One owner per item. File lists are disjoint; an overlap requires the owner's hand-over through the record's `asks` before any write. The orchestrating session holds its own authority only; an assigned agent inherits none of it and may not release, approve or widen scope. One integration owner holds the shared manifests and the merge.

Completion: no two items share a file, and the integration owner is named.

### 4. Run agents against evidence

Each agent writes its handoff note and evidence (test output, diff, logs, screenshots) at its agreed path. Set each agent's limits (attempts, elapsed time, spend, effects) per `../../references/conventions.md` before it starts. Track liveness from the record's heartbeat, which is computed, never typed.

Completion: each running item has a handoff path and a limit set, and its status is `in_progress`.

### 5. Give every received output a disposition

Inspect each handoff: label its evidence Fresh, Retained, Reported or Proposed; decide accepted, returned with a named defect, or declined; and record the consuming action (merged into the integration branch, folded into another item, or dropped with the reason). An output with no consuming action is invisible work.

Completion: every handoff has an inspected disposition and a consuming action in the record.

### 6. Review and integrate in sequence

The integration owner runs tests first, then diff review, then security and risk checks, then product polish, and resolves conflicts alone. A passing gate makes an item mergeable into the integration branch; release of the product stays with the release coordinator and the owner's exact word.

Completion: merged items are `complete`; pending items have a named failing gate or blocker.

### 7. Extract what repeats

When an item pattern recurs, propose it as a shared skill candidate in the report; promotion is the integration owner's decision.

Completion: the report lists candidates with the item ids that justify them, or states none.

## In the workflow

Parallel Build and Prove work in `tailered-ai:workflow`: give each agent disjoint files and its own temp folder, merge results in a fixed order (the day-build runner's `JOBS` pattern), and run reviewers and council voices as separate fresh subagents whose verdicts are saved as files. Review passes: `tailered-ai:lockin` (review, audit).

## Anti-Patterns

- Many agents with no owner or merge gate; shape items before fan-out.
- Useful output that exists only in a transcript; require the handoff path.
- A board whose items have no acceptance; write acceptance at `idea`.
- Parallel writes to the same file; assign disjoint files or request hand-over.
- An agent acting on the orchestrator's authority; each session's record holds only its own.
- Assuming an orchestrator process is live; read the computed liveness in the record.

## Source and adaptation

Source: `team-agent-orchestration` from the ECC bundle 2.2.3 (installed local bundle). SHA256 of the source entrypoint: `a64dbdf4b6df857c044d6b38cf23324fcd7d2c139ba1cfcd39535e8c928c49a3`. License: MIT (see NOTICE.md at the plugin root).

- Translated the seven Kanban columns onto the existing queue statuses (idea, open, claimed, in_progress, blocked, handed_over, complete, abandoned) and the card schema onto the record's fields, so no second board is created.
- Named one integration owner and required disjoint file lists with hand-over through the record's `asks`.
- Added an inspected disposition and consuming action for every received output.
- Stated that no agent inherits the orchestrator's authority and that release stays with the release coordinator.
- Replaced the external control pane with the queue board's computed liveness and removed pull-request and desktop-orchestrator assumptions.
