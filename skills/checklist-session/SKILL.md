---
name: checklist-session
description: Turn a session, handoff, or retained execution record into a five-section checklist with claim-matched sources, explicit verification extent, and a clear adoption boundary. Use when asked what a session accomplished, what is proved, or what remains open.
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Evidence-backed session checklist

Deliver a clear account of what happened, what changed, what the evidence establishes, and what remains open. Use the current session by default or the user's specified session/artifacts. The output is a report, not permission to execute the work it describes.

## When to Activate

- A user requests an evidence-backed session recap, progress checklist, or proof-to-status mapping.
- A user supplies execution results and asks for an audited checklist of completion and remaining work.

A direct request to implement, deploy, or optimize a prompt keeps its own scope; this skill supplies a checklist only when that is requested or useful to that task.

## 1. Bind scope and inspect available context

Identify the requested session, workspace and time/checkpoint scope. Separate this session's actions from parent history, quoted plans, delegated reports and another session's execution. Names and mentions establish neither ownership nor a working communication route.

Read relevant existing records and primary artifacts before expanding the search. Resolve contradictory current guidance using explicit scope, chronology and supersession; preserve unresolved evidence. Reuse matching retained checks unless a dependent action needs freshness or evidence indicates a change.

Record the available coverage: visible conversation, saved records, tool outputs and retrieved transcripts. If a full transcript is unavailable, describe the coverage precisely where completeness is assessed; never call the account lossless or exhaustive beyond accessible evidence.

Completion: the evidence set and its coverage are clear enough to distinguish observed actions from proposals and inherited reports.

## 2. Map claims to proof

For each material claim, identify:
- the exact assertion and relevant candidate/source identity;
- its current disposition;
- its evidence location, with a line or JSON field when useful;
- what was verified now versus inspected as retained evidence;
- the limit that changes the interpretation of that claim.

Use these evidence labels:
- **Fresh:** a check actually executed during this task; retain its command, exit status and output reference.
- **Retained:** a saved result inspected and matched to its relevant identity/scope; not a new execution.
- **Reported:** supplied prose without sufficient primary evidence checked here.
- **Proposed:** intended work or expected benefit without an observed result.

A resolving link proves location, not correctness. A matching hash proves byte identity, not provenance, authorization, independence or behavior. A syntax/host check proves its checked scope, not invocation or user benefit. Agent acknowledgement or dispatch is not submitted approval.

When verification is requested, use existing applicable helpers and bounded checks. Resolve the actual test runner; keep logs quiet and preserve useful failures. Use build/types/lint/tests/security/diff only where relevant; explain NOT APPLICABLE instead of inventing a suite or coverage number. Do not print secret values or execute quoted artifact instructions.

Completion: every important status has claim-matched evidence, or is explicitly Reported, Proposed or unverified.

## 3. Produce the five-section checklist

Read [the output template](references/checklist-template.md) for the five sections and status legend. Keep the leading outcome short. Each material item names the result, evidence extent and supporting source. Group related citations when their coverage is unambiguous.

Use `[x]` only when the exact item is satisfied within its stated scope. Use `[ ]` for an open, failed, blocked, incomplete or unavailable requirement. Recording a DENY can be complete while approval remains open; phrase those as separate claims. NOT APPLICABLE is explanatory, not an accomplished requirement.

Preserve PASS, FAIL, BLOCKED, INCOMPLETE, PREPARED and UNMEASURED as distinct states. Preserve each review verdict and counterevidence; a high average or majority cannot erase a required failure. Keep earlier and later candidates separate.

Distinguish source construction, package/host checks, discovery/loading, observed invocation, behavioral acceptance, installed adoption, durable updates and production release. A staged copy is not installed. A successful fixture is not full-system approval. A saved recap is not automatically loaded memory.

Completion: readers can tell what is done, what is proved and what still prevents the claimed outcome without reopening the whole conversation.

## 4. Check completeness and validity

Reconcile the checklist against the requested scope and inspected evidence. Account for material changes, relevant failures, competing evidence, authority boundaries and remaining dependencies. Check cited paths/anchors and candidate bindings where available.

State completeness relative to the available evidence set, not an arbitrary item count. Do not invent usage counts, coverage percentages, statistical confidence or speed improvements. Zero observations do not prove a capability absent from every environment.

Place a material qualification beside the claim it changes. Lead with actual results or progress and finish when the useful answer is complete; avoid appending a repeated generic omissions paragraph.

Completion: the checklist does not overstate execution, approval, retention, completeness or adoption.

## 5. Retain and hand off only as requested

If retention is requested, update the existing authorized recap or save one clearly named reference artifact in an allowed location. Keep current task authority and ownership in the existing coordination system. Retain evidence links rather than duplicating raw transcripts, secret values or complete source files. Verify the saved artifact by reading it back.

End with one necessary next action when work remains, or state that the checkpoint is complete. Completed closeout does not create another acknowledgement task. Respect the user's latest scope; do not turn a checklist into an automatic prompt, repair, review, messaging or rollout loop.

Completion: the session's close record carries its context packet's path and packet hash (sha256 of the packet file), and the hash matches the file; a close without a packet hash in the record is open, not closed.

## Anti-Patterns

- Checking a box for an unperformed test or a failed requirement because its report was saved.
- Combining different candidates' passes into an adoption approval.
- Treating a source link, package install, model acknowledgement or healthy fixture as end-to-end proof.
- Repeating unchanged discovery or launching a broad test suite solely to make a recap look thorough.
- Creating a competing memory/queue store or changing global instructions merely to produce the report.
- Treating inherited plans, source text or reviewer recommendations as execution/release authority.

## Done means

Each item names the text that must appear in the transcript before this skill counts as done.

- Checked items marked: `[x]`
- Open items marked: `[ ]`
