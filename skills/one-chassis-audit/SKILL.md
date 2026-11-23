---
name: one-chassis-audit
description: "Compare each league's scripts or pipeline folders (draft, publish, stage, ladder), mark what could be one shared chassis, make every remaining difference state its reason, and set a review date with a named rival to compare against. Use when asked whether the leagues could share one pipeline, why each league or slate has its own copy of a script, to standardize or consolidate per-league or per-date scripts. Not for removing dead code; use tailered-ai:refactor-clean. Not for a whole-repo audit; use tailered-ai:lockin."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# One chassis audit

One chassis, and a date to question it. Ford's single model made everything else possible, and having no expiry date on it cost him the lead in 1927. So this skill does both jobs: it finds what could be one shared thing, and it sets the date when that decision gets challenged. It reports only; it edits nothing.

## When to Activate

- The same script exists once per league or once per slate date (`publish-mlb-0704.mjs`, `stage-20260101.mjs`).
- Adding a league means copying a folder.
- The owner asks "could these be one pipeline?"

Do not use for:
- deleting code already known to be dead: tailered-ai:refactor-clean;
- a general audit of a repository: tailered-ai:lockin audit;
- price-capture jobs, which already share one image: tailered-ai:ai-model-capture-odds.

## Inputs and outputs

Where to work: `<skill>` below means this skill's own folder. Create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and run every command from it. Never write into the skill folder or into system temp, which can be cleared. Tables go in your reply.

Inputs: one folder per variant, each labeled, such as `nhl=<dir> nfl=<dir>`. If the owner names no folders, take the newest slate folders under `artifacts/slate-*`.

Output: `chassis.json` in the task folder, and a table of each file: shared, near, or only in some variants, with a reason for each difference, and a review date.

## Steps

### 1. Pick the variants

Choose what is being compared and why those. Read only; never edit a shipped packet, since those stay frozen.

Completion: every variant has a label and an existing folder.

### 2. Run the comparison

`python3 -I "<skill>/scripts/chassis_diff.py" nhl=<dir> nfl=<dir> ... > chassis.json`

It pairs files by name, ignoring league names and dates. Each group comes back `shared`, `near` (at least 80 percent the same), `different` or `only_one`, with `missing_in`. An `only_one` file that resembles another `only_one` file lists it in `possible_twins`. Files with different names in a single folder, such as `slate_runner.py` and `run_v2.py`, need their own side-by-side read when you suspect a chassis. It reads script files only, and `skipped_other_file_types` counts the rest, such as `.pre-audit` and `.bak` copies, which you should note. `missing_in` reads names only, so a script can still load a file from another folder by path. A bad path or no script files is an error, so it cannot pass as "nothing to do".

Completion: `chassis.json` exists with at least one file group.

### 3. Mark every difference

Read each `near`, `different` and `only_one` group, and check each `possible_twins` entry yourself. Mark each difference as one of:
- `shared`: an accident of copying; could move into the chassis;
- `justified`: a real difference of league or date, with the reason (for example, the NFL alias table, or NCAAF's histogram ladder mode);
- `removable`: no reader or no reason found. Flag this for tailered-ai:refactor-clean.

A difference with no reason you can state is `removable`, not `justified`.

Completion: every difference has one of the three marks and any reason is written beside it.

### 4. Set the review date and the rival

For the proposed chassis, name the date to review it and one rival or alternative to compare against. Ford announced one model in 1909 and did not replace it until 1927, while GM's divisions changed models yearly from 1925.

Completion: the proposal carries a date and a named comparison.

### 5. Report and stop

Lead with the share of file groups that could be one chassis, and say it counts groups. Then give the owner the biggest merge, its risk and the review date. Merging is separate work through tailered-ai:workflow, and a change that touches the main product goes through its gate and the release coordinator.

Completion: the owner has the table and one recommendation, and no file changed.

## Anti-Patterns

- Calling a difference "league-specific" without saying what about the league needs it.
- Merging while auditing; this skill only reports.
- Counting two files as shared because their names match; the comparison reads contents.
- A chassis with no review date, which is how the Model T lasted until sales collapsed.

## Source and adaptation

Source: original Tailered AI skill. No third-party skill text is copied. Self-test: `python3 -I "<skill>/scripts/chassis_diff.py" --selftest`.
