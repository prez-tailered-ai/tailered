---
name: lockin
description: "the owner's working mode in one skill, picked by verb: lock (focused execution mode; /lock-in, \"lock in\"), next (rank ten actions with paste-ready prompts, then execute the top N; /locktfin, \"what's next\"), verify (proof before any claim: gates, claim or results branch; /verify), write (plans, skills and agent docs; /write), build (default; the smallest change that fully solves the task, scope levels lite, full, ultra), review (one change), audit (a whole repo or folder), debt (ledger of shortcut: comments) and help. Use on any coding task and when the user says \"ponytail\", \"be lazy\", \"yagni\", \"simplest solution\", \"do less\", \"review this\", \"code review\", \"is this over-engineered\", \"audit this codebase\", \"find bloat\", \"what can I delete\", \"what did we defer\" or \"list the shortcuts\"."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Lockin

One skill for the owner's working mode: lock in on a task, rank what comes next, and build and judge code like a lazy senior developer (the best code is the code never written, yet the whole problem gets solved). It merges lock-in, locktfin and six earlier ponytail skills; the detail sits in `references/`. Reading it changes no files and installs nothing.

## When to Activate

| Verb | Use when the user | Read |
|---|---|---|
| lock | says "/lock-in", "$lock-in", "lock in", "/lock-in ultra", "/lock-in off" | `references/lock.md` |
| next | says "what's next", "/locktfin", "rank next actions", or passes -plan, -execute, --asap, --5, --10 | `references/next.md` |
| verify | says "/verify", "run the checks", "is it ready", or is about to claim done, fixed, passing, or to report a model or backtest number | `references/verify.md` |
| write | says "/write", "write a plan", "write a skill", "edit this skill", or is about to write an implementation plan, a skill or an agent instruction file | `references/write.md` |
| build (default) | writes, fixes, refactors or picks a dependency; says "ponytail", "be lazy", "yagni", "simplest solution", "do less" | `references/build.md` |
| review | says "review this", "code review", "review my PR", "is this over-engineered" | `references/review.md` |
| audit | says "audit this codebase", "find bloat", "what can I delete" | `references/review.md` (repo scope) |
| debt | says "what did we defer", "list the shortcuts", "ponytail debt" | `references/debt.md` |
| help | asks how to use it | this table; "stop ponytail" or "normal mode" turns build mode off |

In `tailered-ai:workflow`: lock and next run in Bind (task, scope, authority, ranked plan); build is the Build phase; review and audit are Prove review passes and count toward its 3-round stop rule; debt is a Prove read, not a round; verify is the Prove exit (gates) and guards every Release and Verify claim (claim, results).

Do not use for:
- performing dead-code removal: `tailered-ai:refactor-clean`; behavior-neutral restructures: `tailered-ai:orch-refine-code`;
- non-coding requests (prose, translation, summaries).

## Inputs and outputs

Input: the verb (from the table; none named means build) and its target: the task for build, the change for review (named diff, else uncommitted changes, else the last commit), the folder or repo for audit, the repo and optional marker word for debt. The build level lives in the conversation and stays until the user names another level or says "stop ponytail" or "normal mode"; no hook or file tracks it; default full.

Output per verb: build, the change plus one or two closing lines naming what was skipped and any risk; review and audit, the report in `references/review.md`; debt, the ledger in `references/debt.md`; help, this table. Only build edits code.

## Steps

### 1. Pick the verb and level

Match the request to the table. For build, set the scope level: lite (build what was asked, name the smaller option in one line), full (all of `references/build.md`), ultra (also question the request and push back before building).

Completion: the reply states the verb, and for build the level, once.

### 2. Build

Follow `references/build.md`: list the scope, climb the six-rung ladder, finish every caller and test, leave a check for new logic, close honestly.

Completion: the closing lines name skipped work and risk (or say there is none), and every changed function's callers were searched.

### 3. Review or audit

Follow `references/review.md` with scope one change (review) or the named repo or folder (audit). Change no code.

Completion: the report has its opening line, numbered four-part findings (or the clean line) and the `Verdict:` line.

### 4. Debt

Follow `references/debt.md`. Change no code; write a file only if asked.

Completion: the ledger ends with `<N> markers, <M> with no trigger.` or `No shortcut debt. Clean ledger.`

### 5. Lock

Follow `references/lock.md`: resolve level, targets and duration; open every reply with "Locked in." and acknowledge "Locked in. Tool-kit active." on activation. Activation alone grants no production permission; no-contact restrictions, including release coordinator, hold. Lock's lite, full and ultra set execution discipline and are separate from build's scope levels; `lock ultra` never starts `next -execute` by itself.

Completion: the reply states level, targets and duration, and the continuity record (or handoff) holds the lockIn fields.

### 6. Next

Follow `references/next.md`: ten ranked items, each with Why now, Scope, Risk, Verification and a paste-ready Prompt; execute only the top N asked for, under lock, where the stricter rule wins and merge and deploy are not yours. The re-audit loop counts toward the workflow's 3 review rounds; at the cap it ends "stopped, not finished" with the open items listed.

Completion: every item has its five fields, and the reply ends with the A/B/C "What next?" block before the plain restatement.

### 7. Verify

Follow `references/verify.md`: pick gates, claim or results from its table and run that branch's steps; a claim that all gates pass runs gates first. Quote the command, exit code and counts.

Completion: every claim in the reply carries the command and result from this turn, or the real status replaces the claim.

### 8. Write

Follow `references/write.md`: plan (implementation plans in `docs/superpowers/plans/`), skill (the house format, tested before it ships) or agent-doc (routes to `tailered-ai:writing-for-agents`).

Completion: the plan, skill or document exists, and its branch's self-review or checks are recorded.

## Load order and output contract

Read this file, then only the reference for the chosen verb. Level words name three separate things: build's **scope** level, lock's **discipline** level, and review versus audit **depth**.

Output: one opener ("Locked in." while lock is active) and one footer: next's A/B/C block when next ran, then the plain restatement. Skipped checks and material risks take one line, only when they change the owner's next decision.

## Anti-Patterns

- Lazy about the change itself: a broken caller or test left behind.
- A finding with no concrete case, or a review that skips the callers.
- Calling code dead without a tree-wide grep.
- Editing code during review, audit, debt or help.
- Treating the level as saved on disk; it lives in the conversation.
- Reading `lock ultra` as `build ultra`, or as permission to execute ranked items.
- Stacking several footers; there is one.

## Source and adaptation

Merged from six Tailered AI skills that adapted the ponytail plugin 5.3.2 (MIT, Copyright (c) 2026 DietrichGebert). SHA256 of each source entrypoint: ponytail `9badd22a32e19cb884e46dfa8d3aae82bb81dfa5484105b8b4f0262df823a509`; ponytail-review `33fe4ebe22a460924e5d4a261e223df22e409cc94ab76182bee9fb91a3ef022e`; ponytail-audit `2b3223a02c386d1263e1b08343cb8eb3a53e444cdafb1d79e26c8ec2a8fcad28`; ponytail-debt `b5ec2762f6ba8c4af9ea7173aa6c9f91b88655a25e43f9de0264f6ce8722b25f`; ponytail-gain `231034a896d6762e4b5c8468287083422c56b499119976ec9f76821f7d083090`; ponytail-help `86ab0ce0af70cbeeeef499d5c884873b393f87f86401dcc45553662ce2c1eff9`. License: MIT (see NOTICE.md at the plugin root).

- verify (2026-11-02) folds three Tailered AI skills: verification-loop (ECC 2.2.1, MIT, source SHA256 `f0d56107f79e607d4de6c5543b8edfb1b58ab9ae4019b39831689cd91116543e`), verification-before-completion (superpowers 7.0.1, MIT, `2befe7fc55bcadaa3d97dd9e8efeb633d2561c0ebe74c5a8b17c4d9e7e4520b3`) and verifying-results-before-claiming (science-superpowers, concepts only, `90fbeb6dce4a1213778c3ced639ba6aab5a5a801bc4ee2a53c98d7058c4decad`).
- write (2026-11-02) folds superpowers 7.0.1 writing-plans (MIT, source SHA256 `a6c67c1900064347c2a329990dd3c555657c51c3ec53b259a08aa01a2c26139a`) and writing-skills (MIT, `8cb3ac68c6d8c4bb46886b998b09af7989643cab8bd0e46ee86dd62e64546bbe`), and routes agent docs to tailered-ai:writing-for-agents.
- History of the merges: `CHANGELOG.md`.

## Done means

Each item names the text that must appear in the transcript before this skill counts as done (checked by `tools/change_checks.py done`).

- Opener stated while lock is active: `Locked in.`
- Plain restatement after the footer: `---`
