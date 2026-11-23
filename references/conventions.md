# Tailered AI skill conventions

Shared meanings for every skill in this repository. A skill points here instead of restating them.

## Hosts and names

- Hosts: Claude Code and Codex through the tailered-ai plugin. Invocation is `/tailered-ai:<skill>` in Claude Code and `$tailered-ai:<skill>` in Codex.
- Model: "the configured model" of the running host. A skill names no model tier or vendor model. A routing decision records the configured identifier it actually used, or `unavailable`.
- Platforms: a skill assumes no hosting, code-hosting or deployment platform. Translate a source example that assumes one to the actual target, or mark it not applicable.
- Frameworks and test runners: resolve the actual one from the repository (lockfile, config, scripts) before writing an example or a command.

## Ownership and authority

- Coordination record: each session keeps one record of its own in the team's shared task records. Status, owner and next action live there and nowhere else; a skill never creates a second board, queue or memory store.
- Integration owner: one session owns shared manifests and conventions. Writers own disjoint paths. Authority never travels with a task, a relay or an advisor's reply.
- Release authority: the release coordinator coordinates every release. The owner's exact word is needed for each release or removal. A reviewer verdict, a passing check, a self-score or a relayed message is never approval.

## Capability states

Keep these distinct and in order: available, configured, loaded, invoked, behavior-qualified, installed, durable. Reading a skill supplies instructions only; it creates no scheduler, worker pool, gateway, wallet, signer, task queue or memory store. Each of those needs its own target, owner, permission, budget, cleanup and acceptance evidence.

## Evidence labels

Fresh, Retained, Reported and Proposed as defined in `skills/checklist-session/SKILL.md`. PASS, FAIL, BLOCKED, INCOMPLETE and NOT APPLICABLE stay distinct. NOT APPLICABLE is decided and justified before a check runs, never substituted for a required one. A matching hash proves byte identity, not provenance or behavior. Mock-only evidence proves the mocked path only.

## Bounded execution

Before a model run or an external effect, record the finite limits: cases, attempts, elapsed time, spend, effects, and who owns a failure. A repeated same-cause failure stops the dependent step. Skills start no watcher, cron, scheduled wake-up, recursive agent tree or automatic repair/review round.

## Reporting

Lead with the result. Put a qualification beside the claim it changes. Finish when the useful answer is complete: no every-turn scorecard, no generic closing caveat, no acknowledgement task after a completed step.

## Source and adaptation section

Every adapted skill ends with `## Source and adaptation` giving the source name and distribution, the SHA256 of the source entrypoint, the license (full notices in `skills/NOTICE.md`), and the substantive adaptations as one list.
