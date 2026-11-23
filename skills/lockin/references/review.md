# Review and audit

Review like the senior developer who will be paged when it breaks. Order of importance: correct, safe, holds under load, tested, fast, lean. Both change no code.

- **Review** covers one change: what the user names; if nothing, the uncommitted changes, else the last commit. Line count of the change: `git diff --shortstat`.
- **Audit** covers a named folder, package or repo (nothing named: the whole repo). Lean totals: `git ls-files` and line counts.

## 1. Understand first

Review: read the diff, then the callers of every changed function, what it calls, the tests and the README. When a signature, return value or behavior changes, grep every caller.

Audit: map first. Read the README, deploy and build config, dependency list, entry points (main, routes, handlers, jobs, CLI) and tests. Trace the main flows end to end, and read in full the paths for user input, money, auth, data writes, background jobs and shared state. On a big repo go deep where a mistake costs most and say what you did not read.

Both: trace where data comes in, is stored and goes out. Find the expected load (README, deploy config): one person running a script, or many users and processes. Say which load you assumed.

## 2. Look for six kinds of finding

1. **Bug:** wrong result, crash, missed edge case (empty, zero, last item, rounding, time zones), a broken caller, callers that disagree, one rule applied two ways.
2. **Risk:** security holes (injection, weak randomness, secrets, unchecked user input) and data loss (swallowed errors, bad write order, no transaction).
3. **Scale:** fine for one user, wrong for many: check-then-write races, repeated work per process, unbounded growth, a query per item, O(n^2), per-process state that must be shared.
4. **Missing test:** risky logic with no test that fails when it breaks. One good test, not coverage.
5. **Speed:** big slowdowns are problems; small wins are suggestions.
6. **Lean:** delete (dead code, unused options and flags), reuse (name the path), stdlib or native, yagni (one-implementation interface, pass-through wrapper), merge near-copies, split mixed jobs by job and never by line count.

## 3. Check before you report

Council: when two or more reviewers read one report, one voice takes the evidence lens first and grades the report's own counts before any finding is ranked; steps in `council-evidence-lens.md`.

Every finding needs a concrete case: this input leads to this wrong result. Re-read the lines: the caller exists, the value can be empty. Before calling code unused, grep the whole tree: tests, fixtures, config, string and dynamic references. A `shortcut:` comment naming its limit is a decision, not a finding, unless the expected load already crosses it. Propose the smallest fix, preferring ones that delete code. No style taste, no "consider", no vague worries.

## 4. Write the report

Very simple English, short sentences, each technical term explained once.

- Open with `What this change does:` (review) or `What this repo does:` plus the assumed load (audit), in two or three sentences.
- Ranked groups: **Must fix** (bug, security, data loss, breaks at the expected load), **Should fix** (untested risk, real slowness, duplication, mixed jobs, needless code), **Nice to have**. Skip empty groups.
- Number findings across groups so the user can say "fix 2 and 5". Audit: at most 20, and say how many smaller ones were left out.
- Each finding has four parts: **What this is**, **Problem**, **Fix**, **If we skip it**.

End:
- Review: `Verdict: Ship.` or `Verdict: fix 1 and 3 first.`; `Lean: -<N> lines possible.` when lean findings exist; one `Not checked:` line. Nothing found: `Looks good. Ship.` plus one line on what was checked.
- Audit: `Verdict:` (healthy, or what to fix first); `Lean: -<N> lines, -<M> dependencies possible.` when lean findings exist; `Not checked:`. Nothing found: `Healthy. Nothing to fix.` plus one line on what was checked.

## Anti-patterns

- Auditing file by file instead of by risk.
- More than 20 audit findings with no note of the rest.
- Fixing code during the review.
