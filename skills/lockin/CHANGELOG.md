# Lock-in change history

## 1.4.0 — 2026-11-02T21:34:07Z (verify and write)

- verify verb: references/verify.md folds verification-loop (gates), verification-before-completion (claim) and verifying-results-before-claiming (results); the three skills are retired. An automatic Stop check (12 tests), registered only on the owner's yes.
- write verb: references/write.md folds superpowers writing-plans and writing-skills (references in references/write/); agent docs route to tailered-ai:writing-for-agents.

## 1.3.0 — 2026-11-02T20:59:58Z (pointers folded)

- Removed the /lock-in and /locktfin pointer skills and their host links; lockin's lock and next verbs carry their triggers.
- The agent instructions file links to references/lock.md. The handoff verifier accepts "lockin lock ultra" or "lock-in ultra". The pointer version test was removed.

## 1.2.0 — 2026-11-02T20:56:04Z (council cuts)

- Dropped the gain verb (benchmark figures from an unshipped file) and the help step (help is the verb table).
- Merged tool-kit.md into workflow.md section 5; replaced outside skill names in workflow.md with the company ones.
- Folded docs/fixtures.md and docs/qualification.md into evals/lockin.json (18 cases) and removed docs/.
- Removed the nvidia route, workflow.md's measurement section and workflow.py's compare command (and its test); comparisons go to tailered-ai:agent-eval.
- Removed repeats: lock.md's opening paragraph (the quickstart covers it) and build.md's anti-patterns.

## 1.1.1 — 2026-11-02 (council fixes)

- QA docs moved to docs/; script paths relative to the skill root; NVIDIA links, a stale test thread ID, the login example and huge-audit/cali-execute hooks removed; lock quickstart and load order; scope, discipline and depth named; evals cover every verb.

### Merge notes moved from SKILL.md

- Six skills became one, routed by verb; review and audit share one reference because they differ only in scope.
- The source's level hook, flag files, status band, config and update commands do not ship; the level lives in the conversation.
- Gain's figures are carried as published numbers because the source's benchmark file is not shipped.
- Named "lockin" by the owner.
- Step 2 (2026-11-02) folded in two owner-original skills: lock-in 1.0.0 (SHA256 `222bfb7ea2f0e176ca40c7ec1f31a364b66c082916ea61e73bc00af2b09d0e9e`) as `lock` with its references, scripts, evals, version.json and CHANGELOG.md, and locktfin (SHA256 `980069086a609c8f5e3700cd0722295bb8bbbc74c0775218f1298476c5907368`) as `next`. Both old paths are now pointers. locktfin's huge-audit and cali-execute steps became lockin audit, with the originals optional when installed.

## 1.1.0 — 2026-11-02T20:25:48Z

- Folded into tailered-ai:lockin as the `lock` verb with locktfin as `next`; the old lock-in skill is now a pointer. Capability routes for implementation, verification, evaluation, architecture, research and instructions resolve to Tailered AI skills.

## 1.0.0 — 2026-10-22T11:47:45Z

First numbered local revision; earlier revisions were unversioned.

Added:
- One authoritative version and UTC last-updated timestamp in `version.json`.
- Version metadata in both helpers' JSON results, including handled failures.
- `--version` on both command-line helpers.
- Regression checks for version output and shared host aliases.

Inherited from the prior revision:
- Capability routing, contribution contracts, receipt validation, scoped recovery, and equivalent-work comparison.
- Recursive manifest drift checks and activation lifecycle protection.
- One canonical skill shared by Codex and Claude aliases.

This entry records local changes, not production adoption or a new NVIDIA grade.

## Maintenance

For each skill change, update `version.json` with its version and actual UTC update time, then append a dated entry here describing additions, changes, fixes, and verification. Use patch increments for compatible fixes, minor increments for compatible features, and major increments for breaking behavior. Do not change the timestamp on execution. Preserve historical receipts; a changed skill needs fresh candidate-bound evidence.
