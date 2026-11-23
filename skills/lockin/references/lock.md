# Lock: the owner's focused execution mode

`/lock-in`, `$lock-in` and "lock in" route here through `tailered-ai:lockin` (the separate lock-in skill was folded in on 2026-11-02).

**Quickstart.** (1) Open every reply with "Locked in."; at activation say "Locked in. Tool-kit active." and state discipline level, targets and duration. (2) Activation grants no production permission; no-contact (including release coordinator) holds. (3) Do the task with lockin build at the requested discipline. (4) Verify with fresh evidence; PASS, FAIL and NOT RUN stay distinct. (5) `/lock-in off` ends it.

**Load order.** Read this file. Read `workflow.md` (its section 5 is the toolkit) only when the task is substantive (code, release, multi-step); a question or a one-line change needs neither.

Also: Reuse matching authorization; do not repeatedly ask for approvals already supplied. Preserve access controls, locks, rollback, unrelated work and failed evidence. Honor explicit no-contact restrictions, including release coordinator. Follow higher-priority instructions and keep release authority separate from this operating mode: activation alone is not blanket production permission.

## Invocation and scope

Scope is single-session (the current or one named session) or multiple-session (only the listed sessions). Instruction syntax, not a shell command or a guaranteed native slash-command parser:

- `/lock-in` (or `lockin lock`): full, current session, until revoked.
- `/lock-in lite|full|ultra`: selected level, current session.
- `/lock-in ultra --session <thread-id-or-codex-URL>`: one explicit target.
- `/lock-in full --sessions <id-or-URL>,<id-or-URL>`: only the listed targets.
- Add `--turn` to end at this response; otherwise persist in the addressed session until revoked.
- `/lock-in off`: deactivate the current session. With explicit targets, deactivate only those targets after delivery is authorized.

Normalize codex://threads/<id> to its thread ID. Never infer "all sessions" or discover unrelated chats to broaden a list. If conflicting levels or malformed scope make the target unclear, explain the exact ambiguity and continue only independent work.

At activation, state the resolved level, targets and duration briefly. Retain the instruction in session continuity when a continuity record is already used. Do not create a daemon, global configuration, recurring automation or new task merely to sustain the mode.

For another session, prepare a self-contained invocation naming `tailered-ai:lockin` lock and this file's absolute path. Send it only when the owner explicitly authorizes messaging that session. A named test target alone is not a delivery receipt. Record prepared, delivered and acknowledged separately. Never claim the remote agent adopted the mode without its acknowledgment. Without a messaging channel, give the owner the invocation to paste.

## Continuity and progress

Store activation in your existing session continuity record, never another session's record. If no writable record is available, include the same fields in the next continuity handoff instead of creating a parallel registry:

```json
{"lockIn":{"active":true,"level":"full","targets":["actual-thread-id"],"duration":"until-revoked","toolkit":true,"task":"current authorized outcome","authorization":"pointer to the actual owner instruction","noContact":["release coordinator"],"next":"next unfinished acceptance criterion","delivery":{},"budget":{"usd":0,"holdAt":"stage end"},"lastNotice":"stage, spend so far"}}
```

The record carries `budget` (the dollar line and the stage end at which it is checked) and `lastNotice` (the last stage end at which spend was reported against the budget); at a stage end with spend at or over the budget the run holds and reports before the next stage. Restore only when the current thread ID is in targets and duration has not expired. Reconcile later revocation or changed instructions before acting. `--turn` expires when that turn ends. Preserve an independently activated toolkit on revocation. Cross-session delivery entries use prepared, delivered (with receipt), then acknowledged (with response); a file or target name alone proves neither delivery nor adoption.

Prefer execution once decisions are settled. The owner's applicable release authorization and no-contact instruction remain in force until revoked; do not re-request the same approval. Missing credentials, unresolved task facts and higher-priority restrictions are concrete dependencies, not reasons to manufacture consent or claim completion. Planning and brainstorming are bounded tools for unresolved decisions, not substitutes for shipping.

After each meaningful result, select the next executable acceptance criterion. Before retrying, record the changed hypothesis, input or repair and the expected discriminating result. Do not repeat an identical failed action unchanged. A blocked dependency holds its consumers; continue independent eligible work. Keep expected and observed failures and accepted fixes in the existing task evidence. Stop when all requested acceptance criteria are verified, or report precisely what prevents the remainder.

## Discipline levels

Lock's lite, full and ultra are **discipline** levels. They are separate from build's **scope** levels: `lock ultra` does not set `build ultra`, and it never starts `next -execute` by itself. All levels retain security, validation, accessibility, requested scope and honest verification; they change workflow discipline, not model settings or privileges.

| Level | Execution | Completion evidence |
|---|---|---|
| lite | Direct implementation; reuse existing helpers; minimal narration. | Targeted checks for changed behavior and explicit remaining gaps. |
| full | Trace affected callers and complete the entire authorized slice; repair substantiated failures. | Applicable regressions plus intended-caller verification, exact changed scope and rollback when releasing. |
| ultra | Full, plus challenge the highest-risk failure assumptions and eliminate redundant work. Use existing failure fixtures and negative controls; stop repeating unchanged experiments. | Verify each relevant negative control fails for its intended reason, recovery works, and release claims match deployed behavior. Report unresolved risks rather than expanding scope. |

Do not add arbitrary reviewer counts, mandatory documents or new infrastructure. Apply task-specific requirements when the user explicitly requested them. Budget retries proportionately; on a repeated blocker, retain evidence, explain the concrete dependency and continue eligible independent work. Never manufacture completion to satisfy urgency.

## Agents and toolkit

When delegation is separately permitted, put the resolved level, scope, task, acceptance criteria and no-contact restrictions in every delegation, and require concrete results and evidence back. This mode does not authorize spawning agents. If agents are prohibited, execute natively.

Every lock activation automatically activates the toolkit; no separate invocation is required. Read [the toolkit mapping](workflow.md) (section 5) on activation. The toolkit inherits the exact level, session targets and duration. Include this automatic activation in authorized delegations and cross-session handoffs. `/lock-in off` ends its inherited toolkit activation; preserve any separately requested toolkit scope. At activation acknowledge "Locked in. Tool-kit active." This means the mapping is loaded, not that all tools have already run.

## Outcome routing and execution

For substantive work, follow [the outcome workflow](workflow.md): (1) resolve capabilities by task and phase, (2) assign complete contributions, (3) validate candidate-bound receipts before completion claims, (4) resume from scoped state with invalidation, and (5) apply the toolkit; comparing equivalent work goes to `tailered-ai:agent-eval`. Use `scripts/workflow.py` through the actual host shell. These are local execution controls, not a claim of universal host enforcement. Do not let reviewer-only scope erase an overall task requirement. Capability routes resolve to Tailered AI skills where one exists; the remaining routes in `capabilities.json` are optional tools probed at run time and reported `unavailable` when absent.

## Completion

Verify claims with fresh evidence appropriate to the task. For software, use actual project commands and real caller behavior; for prose, inspect requirements and references. Keep PASS, FAIL, NOT RUN and NOT APPLICABLE distinct. Report the delivered result and evidence succinctly. Skipped checks and material risks: one line, only when they change the owner's next decision (the owner rule, newer than lock-in 1.0.0's "always name skipped checks"). Do not imply an independent review occurred when only self-review ran.

For installation and behavior checks, use `evals/lockin.json` (skill root). Run `scripts/check_trace.py` on actual observed events when available. Synthetic fixtures qualify the checker only; they do not prove agent obedience, cross-session adoption or compaction persistence. Compare baseline and candidate on identical tasks before claiming performance gains.

## Scripts

Python 3 standard library is sufficient.

| Script | Purpose | Arguments |
|---|---|---|
| `scripts/workflow.py` | Resolve capabilities; validate receipts; propose resumption | `route`, `validate`, `resume`; use `--help` |
| `scripts/check_trace.py` | Check recorded activation and execution events | Absolute trace JSON path |
| `scripts/test_*.py` | Exercise helper contracts and negative cases | `python3 -I -m unittest discover -s scripts -p 'test_*.py'` from the skill root |

These scripts validate supplied records, not the truth or completeness of captured events. No automatic host hook or daemon is installed. Missing Python or a required skill: hold the affected claim and report the prerequisite. Invalid or stale receipts: preserve the failure, repair the producer, then rerun affected consumers. Never invent a host API or grading result.
