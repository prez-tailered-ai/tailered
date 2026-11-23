# Outcome workflow and host execution

Read this when activation accompanies substantive work. Explanation-only requests do not activate an execution pipeline. Use this file and `capabilities.json` (this folder) as the canonical workflow contract; do not duplicate it into host instructions.

## 1. Match capabilities and phases

Identify the user's outcomes and select explicit profiles: ui, research, engineering, instructions, undecided, audit, evaluation. Combine only relevant profiles; explain selects none. Profiles are starting points, not a keyword classifier or permission grant. Add task-specific requirements omitted by a profile before work starts; record why each is needed. Resolve alternatives against the actual host and user preferences.

Run `python3 <skill-root>/scripts/workflow.py route --profile ui --profile research` (example). Use `--phase verification` for a reviewer while retaining the whole-task requirements in the output. The resolver checks installed files, including configured G-Stack source paths; absence from a displayed catalog is not absence on disk. Multiple paths are candidates to inspect, not instructions to run every copy. Pick the installed host-compatible skill and record its exact path/hash. Confirm connector/runtime readiness with a harmless relevant operation; file presence is not readiness. Never install or enable telemetry merely to discover a capability.

Completion: each required outcome has a responsible capability, phase, inspected skill path, availability and allowed effect. Missing required capability blocks that outcome, not unrelated work. Keep applicability, availability, execution and verification separate. A role-level NOT_APPLICABLE cannot discharge a task-level requirement.

## 2. Assign contributions before execution

Research produces evidence and decision implications. Design owns interaction, visual craft and rendered inspection before freeze. Implementation consumes accepted decisions and preserves existing contracts. Verification exercises actual callers and negative paths. Review assesses the exact candidate independently only when independent execution is authorized. Evaluation compares fixed tasks; it does not replace correctness checks.

For UI, use the company's design skills (design-craft, design-shape) and the requested browser; browser-source or screenshot review alone is not a full live workflow. For ambiguous behavior resolve the decision first; once resolved, proceed. lockin build controls scope. lockin verify (gates) verifies applicable checks. REA investigates suspicious test credibility, not every ordinary test. The company writing-for-agents authors agent instructions and fixture routes. Inspect skill requirements before claiming full execution; mark adaptations partial with exact omissions.

Completion: each phase has inputs, an output, a consuming phase, acceptance criteria and an owner. This creates responsibilities, not automatic subagents. Under no-delegation rules one agent executes natively. Freeze only after required execution phases; a frozen reviewer cannot retroactively substitute for them.

## 3. Validate executable completion contracts

Use the existing task evidence record, not a new registry. For substantive execution, attach a `lock-in-workflow/1` record using the schema below. Run `workflow.py validate /absolute/path/to/run.json` before the consuming completion claim. A nonzero exit holds that claim. The helper is a read-only local validator, not an installed host hook, universal interceptor or authentication service. Actual executor/host integration must call it and honor its result; if unavailable, report verification NOT_RUN.

Required root fields: schema, session, targets, task, candidate, state (`active`), expired (false), allowed_effects, required (nonempty step IDs), steps, claim (`local`, `host`, `production`). A file receipt is exactly `{ "path": "/absolute/file", "sha256": "actual hash" }`. Candidate binds the chosen artifact or a JSON manifest of the complete candidate. A directory manifest must be stored outside its root, named with a `.json` extension, and contain exactly `schema` (`lock-in-manifest/1`), `root` (absolute source directory), and `files` (nonempty map of normalized relative paths to SHA256 digests). Include every file recursively. Validation and resumption compare all current members and hashes, rejecting added, deleted, modified, symlinked or escaping members. Legacy bare hash maps lack a bound root and are rejected; regenerate them from inspected source rather than trusting old PASS receipts. Ordinary artifact receipts remain supported; the executor must choose a complete directory manifest for multi-file candidates. This is an invocation-time snapshot, not an atomic filesystem lock or protection against a dishonest executor; rerun immediately before consuming the result and hold execution if the source changes.

Each step: id, capability, action, consumer, effect, depends_on (IDs), status (PASS/FAIL/NOT_RUN/NOT_APPLICABLE), candidate_sha256, evidence_mode, inputs/outputs/checks (nonempty file-receipt arrays for PASS). Applicable modes: local-execution, host-execution, browser-execution, retained, tabletop. Set requires_mode when acceptance demands actual host/browser execution. Record host for those modes. NOT_APPLICABLE requires a reason and cannot satisfy a required step. Required failures, cycles, absent/modified files and stale candidate bindings fail validation. Production additionally requires file receipts for approval, coordination, live_acceptance and rollback; inspect their actual identity/scope/freshness under the release policy. Hash existence alone does not prove authority.

Use `scripts/test_workflow.py` only as schema examples; synthetic data must stay labeled synthetic. Raw output must corroborate normalized receipts. No self-written PASS or invented transcript can establish execution.

Completion: required steps pass for the actual candidate, dependencies passed, effects are authorized and each claim is supported at its requested evidence level. Do not treat supplied allowed_effects as independent authorization.

## 4. Resume and recover with scoped state

Keep state in the session's existing continuity record. Store accepted decisions, current candidate receipt, completed step receipts, unresolved findings and the next eligible action. Never write another session's record. No daemon, cron, global hook or new registry is created by activation.

Run `workflow.py resume run.json --session ACTUAL_ID --candidate candidate-receipt.json` to obtain a read-only invalidation proposal. Wrong session, revocation, expiration or an invalid candidate is rejected. Candidate changes invalidate stale steps and dependent steps; reconcile remaining prerequisites before executing. Atomically update only your own existing record with the proposal after verifying the current authorization. Reuse valid evidence, preserve failures and record the changed retry hypothesis. A blocked dependency holds its consumers; eligible independent work continues. Automatic continuation is limited to the active authorized host execution; scheduled/background execution requires its own requested host mechanism.

Completion: resumption preserves decisions and authority, invalidates changed evidence and identifies the next eligible action without replaying one-use effects.

## 5. Toolkit (loaded with every lock activation)

Automatically loaded at every lock-in level. For substantive tasks, apply sections 1-4 above; `capabilities.json` (this folder) supplies discoverable path candidates and profile membership. This prose owns contribution semantics; the JSON owns resolver data, not permission or runtime readiness. Each Tailered AI skill below requires a task-specific disposition: executed, inapplicable, or unavailable. Optional outside tools (a brainstorming or plan-writing skill, a CI-test audit, a web search) are probed through `capabilities.json` at run time and recorded the same way; none is a dependency. Mandatory routing does not justify irrelevant calls. Read each selected skill; preserve its applicability boundaries. If an installed path changes, discover its replacement; report absence rather than pretending execution.

| Skill | Trigger | Input | Execute | Output | Verify | Next consumer |
|---|---|---|---|---|---|---|
| `tailered-ai:workflow` | Any change that will be tested, reviewed or released | request + the owner's words | Bind, Build, Prove, Release, Verify | phase exits met | each exit's command or file | release or report |
| `tailered-ai:lockin` build | Implementation | task + affected callers | reuse existing code; reject needless additions | smallest complete change | scope and protections preserved | candidate |
| `tailered-ai:lockin` review / audit | Review of a change or repo | candidate + callers | six finding kinds, concrete cases | numbered findings + Verdict | each finding re-read | fixes |
| lockin verify (gates) | Candidate verification | candidate + project commands | run the project's own gates in order | results with exit statuses | failures retained; missing checks not passed | delivery claims |
| lockin verify (claim) | Any done, fixed or passing claim | the claim | rerun the proving command fresh | quoted output and exit code | output read this turn | report |
| `tailered-ai:writing-for-agents` | Agent-consumed instructions | branches + fixtures | sharpen pointers and completion criteria | executable instructions | each fixture follows intended branch | executor |
| `tailered-ai:apex-research` | Named external factual gap | question + acceptance constraints | retrieve primary sources | supported conclusion | source directly supports claim | named decision |
| `tailered-ai:agent-eval` | Comparing equivalent work | baseline + candidate on identical tasks | scored comparison | metrics | same inputs, recorded runs | decision |

For every executed contribution record the actual skill path, input pointer, action/result pointer, verification and consuming task in the existing evidence record. A plugin name alone is not an execution receipt. For inapplicable/unavailable entries give a specific reason and effect on completion. If a mandatory task capability is missing, hold dependent claims and continue independent work.


No independent consensus without actual independent reviews. Existing no-delegation and no-contact restrictions remain. Read-only research is not authorization to install capabilities or deploy. No toolkit activation changes model reasoning settings.

### Design and browser responsibilities

For UI tasks, the company's design skills (design-craft, design-shape) own the relevant design workflow and rendered inspection before freeze. Browser QA (an optional tool from `capabilities.json`) contributes actual interaction evidence on the user-selected browser. Inspect the configured installation when catalog visibility is incomplete; do not equate file presence with runtime readiness. Preserve host/no-telemetry constraints and do not run bundled browser tooling that conflicts with the user's chosen browser. A reviewer may use an adjunct, but the whole task still owes its required design/browser contribution.

Record `task_required`, `role_applicable`, availability, execution and verification separately. Every task-required contribution needs an executed/verified consumer path or an explicit unmet requirement. An individual reviewer may mark its own role inapplicable; that never changes task coverage.
