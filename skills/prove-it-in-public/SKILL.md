---
name: prove-it-in-public
description: "Design one public test a skeptic would accept before a launch or funding ask: freeze the rules and entries with a hash and a timestamp before games start, grade every entry, and prepare both the win post and the loss post for the owner. Use when asked to prove a model or claim publicly, run a public contest or challenge, build credibility before a launch, or show a track record people can trust. Not for choosing or fixing a model; use tailered-ai:ai-model-research. Not for one pick's image; use tailered-ai:graphic."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Prove it in public

Say what you will do, then do it where people can see. Ford's first company had failed and his backers doubted him, so in 1901 he raced the country's best-known driver, and new investors followed. He also won partly because the rival's car broke down, and one win is not a record. So this skill fixes the terms first and publishes the result either way. It drafts; the owner posts.

## When to Activate

- A launch, partner talk or funding ask needs proof a skeptic would accept.
- The owner asks for a public challenge or a track record people can check.

Do not use for:
- improving a model: tailered-ai:ai-model-research;
- an image for one pick: tailered-ai:graphic;
- publishing projections to the main product: the publishing step, on the owner's word.

## Inputs and outputs

Where to work: `<skill>` below means this skill's own folder. Create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and run every command from it. Never write into the skill folder or into system temp, which can be cleared. Tables go in your reply.

Inputs: the claim to test, the leagues and the period. Use the company's own numbers, measured against a named benchmark such as the closing line. Never adopt outside picks as ours.

Output: frozen files with their manifests, `rules.canonical.json`, `results.json`, `graded.json`, `final.json`, and two drafts, `post-win.md` and `post-loss.md`. A setup run stops after step 2 plus the drafts, and resumes when games finish.

## Steps

### 1. Write rules a skeptic would accept

State the claim, the metric, the benchmark, the minimum number of entries, the end date, and what counts as winning, as `win_if` in words and `win_pct` as a number. Size it first with `python3 -I "<skill>/scripts/freeze.py" power <entries> <win_pct> <true_rate>`, since a good model can easily fail a small test: 100 games needing 62 wins passes a true 55 percent model only about one time in ten. Ask what an honest critic would attack, such as picking the easy games, dropping losses or changing the metric, and close it: every selected game counts.

For one slate, put rules and entries in one file. For a test over weeks, numbers set weeks ahead would miss injury news, so freeze a plan first with a `selection` rule and no entries, then freeze each night's slate before its first start, with `plan_sha256` set to the plan's hash. When the benchmark is the close, freeze the model's own `number` and let `side` name the method, such as `"model vs close"`, because the side is only known at the close.

Plan: `{"claim": "...", "metric": "...", "benchmark": "closing line", "min_entries": 300, "ends": "2026-12-31", "win_if": "...", "win_pct": 0.55, "selection": "every NBA game the main product carries", "expected_slates": 30}`. Slate: `{"plan_sha256": "...", "entries": [{"id": "401892640", "start": "2026-11-07T00:00:00Z", "side": "...", "number": -3.5}]}`. For a practice run with made-up ids, add `"rehearsal": true`, and the manifest says not to post it.

Completion: all fields are filled, `min_entries` fits the schedule, the size check is shown, and the attacks you considered are listed.

### 2. Freeze before the first game

`python3 -I "<skill>/scripts/freeze.py" freeze rules.json > manifest.json` (for a slate, `freeze slate.json --plan plan.json`, which checks its plan hash and dates while they can still be fixed), then `python3 -I "<skill>/scripts/freeze.py" canon rules.json > rules.canonical.json`. For a slate, name both files after it, such as `slate-1107.manifest.json`, so nothing is overwritten. A plan has no first start, so its deadline is the first selected game's start: take that from the schedule and give it to the owner.

It refuses any entry already started or with no side or number, because a test with known results or an empty prediction proves nothing. A local hash proves only that the file has not changed; it does not prove when it was made. To a skeptic, what counts is the hash posted publicly before the first start, so that post is the owner's to make. Publish `rules.canonical.json` too: anyone can check it with `shasum -a 256`.

Completion: `manifest.json` exists, and the owner has the hash to post before the first start, or a note that the deadline passed and a new freeze is needed.

### 3. Grade every entry

As games finish, use only real graded results. For each frozen file, run `python3 -I "<skill>/scripts/freeze.py" verify <file> <manifest>` and `python3 -I "<skill>/scripts/freeze.py" grade <file> <manifest> results.json > graded.json`. Results use `[{"id": "...", "outcome": "win", "evidence": "close -3.5, final 101-98"}]`, with `win`, `loss`, `push` or `void`. Publish the closes and scores with the results, so anyone can recompute each outcome; the script takes the label as given. A void needs a stated reason, and grading fails on a missing or repeated result. At the end, run `python3 -I "<skill>/scripts/freeze.py" tally <plan> [--missed "<reason>"] <file> <manifest> <results> [more triples] > final.json`, which recomputes from the frozen files and decides WIN, LOSS or TOO_FEW from `win_pct`, counting wins and losses only. It refuses a slate frozen against another plan or a repeated game. A slate you could not freeze in time stays reported through `--missed`: the verdict stands, and `may_say_record` turns false. It cannot see games the selection rule named that no slate holds, so check the schedule and report any.

Completion: `verify` prints `ok` for every file, and `final.json` has a verdict.

### 4. Prepare both posts before you know the result

Draft `post-win.md` and `post-loss.md` when you freeze, in the same plain tone, with blanks for the numbers. Fill the result numbers only from `final.json`; hashes and dates come from the manifests. The word "record" needs `may_say_record: true`, meaning the minimum entries were reached.

Completion: at setup, both drafts exist with blanks. After grading, no result number is missing from `final.json`.

### 5. Hand over and stop

The owner decides whether to post. A loss gets posted as agreed, which is what makes a future win believable.

Completion: at setup, the owner has the hash, the canonical file, the deadline and both drafts. At the end, the owner has `final.json` and the matching filled draft. Nothing was posted.

## Anti-Patterns

- Starting after the first game, or adding entries once results are in.
- Dropping a loss as a void without a stated reason.
- Calling a few wins a record.
- Calling a local timestamp public proof.
- Writing only the win post.
- Posting anything without the owner's word.

## Source and adaptation

