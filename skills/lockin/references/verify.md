# Verify: gates, claim and results

One procedure for proof, in three branches. Pick the branch by what is being claimed:

| Branch | Use when | Proof |
|---|---|---|
| access | a read, run or fetch failed and you are about to ask a human for access, a file or a value | the same read retried once another way, then the ask with the failed command quoted (command, exit code, first error line); an ask without a quoted failing command is held, not sent |
| gates | a change is finished and the project's checks have not run as a set; "run the checks", "is it ready" | the project's own build, types, lint, tests, security and diff gates, in that order, as one report |
| claim | about to say done, fixed, passing, works or ready; about to commit, hand off or repeat a helper's success | the one proving command, run fresh after the last edit, quoted with its exit code |
| results | about to report a model, backtest or analysis number (score, error, edge, ROI, calibration, significance) | a fresh rerun from raw data with a fixed seed, out-of-sample, quoted with interval and sample size |

A claim of "all gates pass" runs gates first and cites its report. The automatic stop check (`verify-claim-guard`, a Claude Code Stop hook when the owner registers it) enforces only the claim branch's core rule: no done, fixed or passing after an edit unless a check ran after that edit.

## Branch: gates

Run the project's own gates in a fixed order and write down what each one said. Kept from the source: six phases (build, types, lint, tests, security scan, diff review), stop on a failed build, a fixed report format, and re-running after big changes. The gates are the project's, not ours; this skill invents none.

### Inputs and outputs

Input: the project folder and its changed files. Output: a gate report (below) with the exact command, exit code and a short output excerpt per gate. Unrun gates are reported as NOT RUN with the reason, never as PASS.

### Steps

#### 1. Find the real runners

Many company folders are Node or Python scripts with no `package.json`. Look for a `run-suite.sh`, `Makefile`, `package.json` scripts, `pyproject.toml`, `tox.ini`, `*.test.mjs` or a README test line. Use what the folder uses. Do not assume `npm`.

Completion: each of the six gates names a real command or is marked "none exists here".

#### 2. Build

Run the build command. If it fails, stop, show the output, and fix or report before going on.

Completion: exit code recorded; a failed build stops the loop.

#### 3. Types and lint

Run the type checker and linter the project already configures (for example `tsc --noEmit`, `pyright`, `ruff check`). Report the error count; do not add new tools.

Completion: both gates have an exit code and an error count, or "none exists here".

#### 4. Tests

Run the whole suite with the folder's runner. Record total, passed, failed and coverage only if the runner prints it.

Completion: the pass and fail counts come from the runner's own output.

#### 5. Security scan

Search the changed files for secrets (keys, tokens, passwords) and leftover debug logging. Never print a secret value; give file and line only.

Completion: the scan lists each hit as file:line or says none found in the changed files.

#### 6. Diff review

Run `git diff --stat` and read each changed file for unintended edits, missing error handling and edge cases. Check that nothing live was deleted; if something was, move it aside or save a backup copy first (the owner rule).

Completion: every changed file is accounted for as intended or flagged.

#### 7. Report

```
VERIFICATION REPORT
Build / Types / Lint / Tests / Security / Diff: PASS | FAIL | NOT RUN each, with command and exit code
Overall: READY | NOT READY
Issues to fix: numbered list
```

If production is next, hand off to `tailered-ai:workflow` Release. This report does not authorize shipping.

Completion: the report names every gate and the Overall line matches the gate results.

### Anti-Patterns

- Assuming `npm run build` exists; find the real runner.
- Reporting PASS for a gate that was not run.
- Running only the fast gates and calling it verified.
- Pasting a secret into the report.
- Treating READY as permission to deploy.

## Branch: claim

No success claim without fresh evidence from this turn. Kept from the source: the iron law, the five-step gate (identify, run, read, verify, then claim), the claim-versus-proof table, the red-flag wording list and the red-green check for regression tests. A passing check proves only what it checked. Premise before inventory: open the script or record the claim rests on and quote its path:line before counting, summarizing or grading anything built on it.

### Inputs and outputs

Input: the claim you are about to make. Output: the claim stated with its evidence (command, exit code, counts), or the real status if the evidence does not support it.

### Steps

#### 1. Name the proving command

Write the claim, then the one command that would prove it. In folders with no `package.json`, find the real runner (a `run-suite.sh`, a `*.test.mjs`, a script the README names). Do not assume `npm test`.

Completion: the claim and its command are written down together.

#### 2. Run it fresh and whole

Run the full command now, in this turn. An earlier run, a partial run or a "should pass" does not count.

Completion: the command ran after the last edit, and its exit code is recorded.

#### 3. Read the output

Read the output itself: failures, errors, counts, warnings. Match the claim to the proof: tests passing needs zero failures; build passing needs exit 0, not a clean linter; a fixed bug needs the original symptom rerun and gone; a new regression test needs red then green (revert the fix, see it fail, restore, see it pass).

Completion: the output supports the claim, or you have written down the real status instead.

#### 4. Check delegated work

If an agent or tool said it succeeded, check the actual diff or file and rerun the proof yourself.

Completion: the changed files were inspected, not just the report.

#### 5. Claim with evidence

State the claim with the command and the result, for example "34 of 34 tests pass (run-suite.sh, exit 0)". If a requirement list exists, check each line; passing tests do not prove every requirement.

Completion: the final message includes the command and the observed result, and no wording goes beyond them.

### Anti-Patterns

- "Should work now", "probably", "seems to".
- Cheering ("Done!") before the run.
- Calling the build good because the linter passed.
- Repeating a subagent's success report.
- Committing or opening a PR first and checking later.
- Leaving a failed check out of the message.

## Branch: results

A number is a claim. Do not report it until you have produced it fresh and read it. Kept as concepts: evidence before claims, fresh reproduction from raw data with a fixed seed, reading effect size with its interval rather than a bare p-value, out-of-sample metrics for model quality, and not trusting a helper's "done".

### Inputs and outputs

Input: the claimed result, the script or notebook that produces it, and the raw data. Output: the result stated with its fresh number, interval or sample size and the exact command, or the real result if it differs.

### Steps

#### 1. Name the claim and its source

Write the claim and the one script that produces it. Find the real runner for that folder; many are plain scripts or a `run-suite.sh`, not an npm project.

Completion: claim, script, raw data path and seed are written down.

#### 2. Rerun from raw, fixed seed

Run it now from the unmodified raw data. Backtests and models must use data available at the time (no future games). Do not edit the raw data; if cleaning is needed, write a copy and never delete live work (move aside or save a backup copy first).

Completion: the run happened after the last code or data change, and the output file or log is saved.

#### 3. Read the actual output

Read the numbers: estimate, interval, sample size, row counts in and out, and diagnostics. A script that ran without error is not a correct result. A non-significant result is "no detectable effect, interval X to Y", not "no effect".

Completion: the numbers you will quote were copied from this run's output.

#### 4. Check the basis

Confirm the metric is out-of-sample (held-out games or a walk-forward split), not training fit. Compare with the market baseline or closing line where the claim is about edge. Confirm the reproduction matches the earlier number to the reported precision.

Completion: the split type, baseline and match-to-earlier-run are each stated.

#### 5. Check delegated work

If a subagent or script said it finished, open the saved output and rerun the key number yourself.

Completion: the artifact was read, not just the report.

#### 6. Claim with the evidence

State the result with its number, interval, sample size and command. If it does not hold, say what the fresh run shows. Odds or lines quoted for a game must come from the book or odds tool this run, not from memory.

Completion: every figure in the message traces to this run's output.

### Anti-Patterns

- "It was significant last time."
- Reporting training accuracy as model quality.
- "p was above .05, so there is no effect."
- Saying "reproduces" without rerunning from raw.
- Quoting a number from before the latest code change.
- Repeating a helper's success report.
