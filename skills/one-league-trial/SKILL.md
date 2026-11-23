---
name: one-league-trial
description: "Try a new main product day-build step or pipeline change on one league in a copied release folder, at three or more settings, and record time and correctness against the live method before any wider use; ends in expand or stop. Use when the owner says test it small first, try it on one sport, one league first, before every sport, or when a new day-build, draft or publish step needs a trial. Not for a full suite run of a finished candidate or the release; use tailered-ai:workflow."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# One-league trial

Try the rough version on one part first. Ford tested the moving line on one part, the magneto, and tried three line speeds before settling on 44 inches a minute. His chassis test was a rope and a windlass. A trial here costs little because it runs on a copy and reaches no member.

## When to Activate

- A new day-build step, adapter rule, draft pipeline or publish script is proposed.
- The owner says "test it small first", "one sport first" or "try it on NHL".
- The owner pastes trial results and asks whether to roll out: go straight to step 4 and mark every run `"source": "reported"`.

Do not use for:
- proving a finished candidate before release: tailered-ai:workflow;
- writing the regression test for a fixed bug: tailered-ai:ai-regression-testing;
- deciding between models or prompts: tailered-ai:agent-eval.

## Inputs and outputs

Where to work: `<skill>` below means this skill's own folder. Create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and run every command from it. Never write into the skill folder or into system temp, which can be cleared. Tables go in your reply.

Inputs: the change, the league, and the setting to vary (batch size, window, concurrency, retry count). If no league is named, pick the one with the fewest games today and say so.

Output: `trial.json` and `result.json` in the task folder, and one table: live method plus each setting, with seconds, checks passed and any new failure.

## Steps

### 1. Make a real copy

Copy the live release folder with `cp -RL`; read the live one from `systemctl show` of the unit through the read-only host path. Never symlink a release folder. Check it before any edit: `python3 -I "<skill>/scripts/trial_table.py" --check-copy <dir> --against <live release folder>`. That confirms no links, no missing file and no changed size; it does not prove the copy behaves like live.

Completion: `--check-copy` prints `ok`.

### 2. Narrow it to one league

If the day build has no league flag, narrow its league table to the one league in the copy only, or feed fixtures for that league. Write the exact edit into the trial notes so it is not mistaken for part of the change.

Completion: a run of the copy touches only that league, shown by its receipt or output.

### 3. Run the baseline, then three settings

Run the unchanged copy first, then the change at three settings, one too low and one too high if you can find them. Use the same inputs each time. Run at most two heavy simulations at once and keep memory free. Record seconds, checks and each failed check by name; write `unnamed-1` if only a count is known. Rerun the winner and the baseline once and record it as `second_seconds`, because one timing can be luck; a slower repeat counts against the winner. For the day build, its own test suite is the correctness check: compare failure sets, since some failures are already known on the live line. If the suite caches results, refresh the cache after each edit, or a changed copy can print a cached PASS.

Completion: the baseline and at least three settings each have seconds, checks and a failure list.

### 4. Judge it

`python3 -I "<skill>/scripts/trial_table.py" trial.json > result.json`

Shape (`settings` needs at least three of these): `{"league": "NHL", "margin_pct": 5, "baseline": {"seconds": 40, "checks_passed": 9, "checks_total": 9, "failures": [], "source": "ran", "second_seconds": 41}, "settings": [{"name": "60", "seconds": 30, "checks_passed": 9, "checks_total": 9, "failures": [], "source": "ran", "second_seconds": 31}]}`.

EXPAND needs a setting at least `margin_pct` faster that loses no check and adds no failure. Anything else is STOP, unless the owner wants the change for another reason. EXPAND alone is not permission to move on: `ready_for_next_league` is true only when the winner and baseline were each run twice here, with named failures. Report it with `needs_repeat`, `unverified_numbers` and `failures_known_by_count_only` beside the verdict.

Completion: the script exits 0 with EXPAND and a winner, or STOP. For INCOMPLETE, supply what it lists.

### 5. Report and stop

Give the table, the verdict and, if `ready_for_next_league`, the next league: the one with the fewest games today, at least one, not yet in this task folder's earlier trials, unless the owner names one. Otherwise, the next step is the repeat or the real run. A trial proves one league at these inputs and nothing wider. Reaching production goes through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the owner has the table, and nothing in this run wrote to a live folder.

## Anti-Patterns

- Symlinking a release folder to save disk; copy it.
- One setting and a verdict; Ford's first speed was wrong and so was his second.
- Comparing to a remembered time; run the baseline in the same session on the same inputs.
- Hiding the league-narrowing edit inside the change.
- Calling EXPAND ready to ship; it earns the next league, not a release.

## Source and adaptation

Source: original Tailered AI skill, which cites My Life and Work (1922), chapter V. No third-party skill text is copied. Self-test: `python3 -I "<skill>/scripts/trial_table.py" --selftest`.
