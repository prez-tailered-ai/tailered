---
name: skill-creator
description: Create a new Tailered skill or improve one, test it against fixture prompts with and without the skill, benchmark the result, and tune its description so it triggers on the right requests. Use when asked to write, edit, evaluate, benchmark or optimize a skill. Not for deciding which existing skill fits a task; use find-skills. Not for auditing installed skills for drift or overlap; use skill-stocktake or skill-comply.
license: Apache-2.0
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Skill creator

Make a skill, prove it works, then ship it through `tailered-ai:workflow`. Kept from the source: capture intent, interview, draft, test prompts run with the skill and against a baseline, graded assertions, the benchmark and review viewer, improve-and-rerun, optional blind comparison, and the description optimization loop with a 60/40 train and held-out split. New skills live in `skills/<name>/` and follow the house format in `skills/agentic-os/SKILL.md`. Reading this skill installs nothing.

## When to Activate

- The user says "make a skill", "turn this into a skill", "improve this skill", "test this skill" or "why doesn't this skill trigger".
- A repeated workflow or a promoted lesson (`continuous-learning`) needs to become a skill.
- A skill's description misfires and needs measured tuning.

Do not use for:
- picking an existing skill for a task: `find-skills`;
- finding skills that drifted, overlap or stopped firing: `skill-stocktake` or `skill-comply`;
- wording rules for agent instructions in general: `writing-for-agents`;
- the release itself (activation, ledger): `tailered-ai:workflow`;
- one-off prompts that will not repeat: write the prompt, not a skill.

## Inputs and outputs

Inputs: what the skill should do, the phrases and situations that should trigger it, the expected output, and the nearest sibling skills it must route to. Missing answers are asked once; do not invent triggers.

Output: a folder `skills/<name>/` with `SKILL.md` (under 130 lines), optional `scripts/`, `references/`, `assets/`; an `evals/evals.json`; a benchmark and review from a workspace outside the skills folder (`mktemp -d`); the checker outputs; and a workflow Release record. Schemas for the JSON files are in `references/schemas.md`.

## Steps

### 1. Capture intent and interview

Pull answers from the conversation first (steps taken, corrections, formats). Ask what the skill enables, when it triggers, the output format, and whether it has verifiable outputs worth test cases. Find the closest existing skill in `skills/` and name it; if one covers the job, improve it instead.

Completion: four written answers plus the nearest sibling and why the new skill is not a duplicate.

### 2. Draft SKILL.md in the house format

Follow `skills/agentic-os/SKILL.md` section by section: frontmatter (`name`, `description` with what, when and "Not for ...; use <skill>", `license`), title, kept-concepts paragraph, the When to Activate section with "Do not use for:" routes, Inputs and outputs, Steps each ending in a checkable `Completion:`, Anti-Patterns, and Source and adaptation. Put every "when to use" in the description. Explain why each rule exists in plain English. Move bulk into `references/` and `scripts/` and point to them by relative path.

Completion: the repository skill checks exit 0.

### 3. Write test prompts and a baseline

Write 2 to 3 realistic prompts per branch of the skill plus one negative that must not trigger it. Save them in `evals/evals.json` (prompts first, assertions later). Bound the run before it starts: number of prompts, one attempt each, and who owns a failure.

Completion: every branch has a prompt, there is one negative, and `evals/evals.json` parses.

### 4. Run with the skill and the baseline

For each prompt, run one agent with the skill and one baseline (no skill for a new skill; a snapshot of the old folder for an edit: `cp -RL <skill> <workspace>/skill-snapshot/`). Start both together, save outputs under `<workspace>/iteration-N/<eval-name>/{with_skill,without_skill}/outputs/`, and save each run's tokens and duration to `timing.json` as it finishes.

Completion: every prompt has both outputs and a `timing.json`; an output that is missing is named, not skipped.

### 5. Grade, aggregate and review

Write objectively checkable assertions while runs finish. Grade each run with `agents/grader.md` into `grading.json` (fields `text`, `passed`, `evidence`). From this skill's folder run `python3 -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>`, read `agents/analyzer.md` for patterns the averages hide, then show the human `python3 eval-viewer/generate_review.py <workspace>/iteration-N --skill-name <name> --benchmark <workspace>/iteration-N/benchmark.json` (add `--static <file>` with no display, and `--previous-workspace` from iteration 2). Stop the viewer when done. For "is the new version better?" use `agents/comparator.md` for a blind A/B.

Completion: `benchmark.json` exists with pass rates and timings, the negative prompt did not trigger the skill, and the human's `feedback.json` is read.

### 6. Improve and repeat

Generalize from the feedback rather than patching one prompt, drop lines that waste time in the transcripts, and move repeated helper code the runs all wrote into `scripts/`. Rerun into `iteration-N+1`. Stop when the feedback is empty, the human is satisfied, or two rounds show no gain; three rounds is the cap.

Completion: the last benchmark is not worse than the one before, and each accepted finding has a fix or a recorded reason.

### 7. Tune the description (optional)

Write 20 realistic queries (8 to 10 should trigger, 8 to 10 near-misses) and review them with `assets/eval_review.html`. Run `python3 -m scripts.run_loop --eval-set <file> --skill-path <skill> --model <configured model id> --max-iterations 5 --verbose`. It needs the `claude` command line tool, runs each query 3 times and spends model calls; state that cap to the user first. Apply `best_description` only if the held-out score improves.

Completion: before and after scores are reported and the frontmatter holds the winning description, or the description is unchanged with the scores.

### 8. Ship through the workflow

Run `python3 -m scripts.quick_validate <skill>` for the structure check. Then use `tailered-ai:workflow`: Prove (the fixture prompts per branch plus the negative; the bench of any skill you changed still passes) and Release (the ledger line; the owner's word before installing into the shared suite). Never copy to a live location by hand.

Completion: the Prove evidence names the exact folder hash, and the ledger line exists or the release is named as awaiting the owner.

## Eval safety

`scripts/run_eval.py` writes a temporary command into the nearest `.claude/commands/` above the current folder. Run it only from a scratch project made with `mktemp -d -t tailered-skill-eval`, never from a Tailered repo, and after a killed run delete that scratch folder.

## Anti-Patterns

- Writing the skill and testing it only in your own head; run the baseline.
- A description that says what the skill does but not when, or one that matches every nearby request.
- Test prompts so plain that no skill would be needed; make them realistic and specific.
- Putting the "when to use" rules in the body, where the router never sees them.
- Leaving the eval workspace inside the skills folder.
- Reading a pass as proof for branches it never exercised.
- Skills that reach into another plugin or an external service; name tailered-ai siblings only.

## Source and adaptation

Source: `skill-creator` from Anthropic's skills. SHA256 of the source entrypoint: `42765c880e446a83c85f7852fc77b43ecd46c76ca219d68051799ac7425e6943`. License: Apache-2.0 (`LICENSE.txt` in this folder; notices in NOTICE.md at the plugin root).

- Copied the whole folder (18 files) with `cp -RL`: scripts, agents, references, eval viewer and assets are unchanged and called by relative path.
- Rewrote SKILL.md into the house format and cut it from 485 to under 130 lines; removed the Claude.ai-only and Cowork sections and the `present_files` or `SendUserFile` packaging step, which cannot be verified here.
- Added the Tailered checks, the workflow Prove and Release path, a required negative prompt, a bounded round cap and a spend note for the description loop.
- Grep of the copied files found no `anthropic-skills`, `ecc:` or `superpowers:` names. `scripts/run_eval.py` writes and then removes a temporary command file in the project's `.claude/commands/` and runs `claude -p`, so the description loop needs Claude Code and runs from a project root; kept as is and noted here. `package_skill.py` and `quick_validate.py` mention claude.ai upload rules (flat folder, name and description limits); kept as they only validate structure, and the Tailered package is not built with `package_skill.py`.
