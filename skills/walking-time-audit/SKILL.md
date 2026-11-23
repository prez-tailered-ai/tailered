---
name: walking-time-audit
description: "Measure how much of a Claude Code session's or job's time goes to walking (reading, searching, waiting, re-reading files already read) versus doing the work, from its transcript or step times, and propose one fix per top cost that brings the input to the work. Use when asked where a session's time or tokens went, why a job takes so long, what we keep re-reading, or to find wasted motion. Not for timing a pipeline's stages or making code faster; use tailered-ai:lockin. Not for rating a session's quality; use tailered-ai:agent-self-evaluation."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Walking time audit

Find the walking. A Ford foreman with a stop-watch found assemblers spent four hours of a nine-hour day walking, then put in a slide and split the job. Sessions walk too: they re-read files, search for what a record already says, and wait. This skill puts a number on that. It reports on the process and never ranks a person or a session.

## When to Activate

- "Where did this session's time go?", "why does this take so long?", "what do we keep re-reading?"
- Before automating a step, to see what the step is really made of.

Do not use for:
- profiling code or a pipeline's stages: tailered-ai:lockin;
- rating work quality: tailered-ai:agent-self-evaluation;
- the health of a capture job: tailered-ai:ai-model-capture-health.

## Inputs and outputs

Where to work: `<skill>` below means this skill's own folder. Create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and run every command from it. Never write into the skill folder or into system temp, which can be cleared. Tables go in your reply.

Inputs: one or more session ids or transcript files, under `~/.claude/projects/<project>/<session id>.jsonl`; or, for a job with no transcript, a step list with seconds. With no input, use the three longest transcripts of the last seven days and say so. A forked or resumed session's history can sit in a later session's file, so if its own file is missing or short, find it with `grep -l <session id> ~/.claude/projects/<project>/*.jsonl` and pass `--session <session id>` with that one file. Forks copy history, so pass one file, not every match; the script counts a copied record once.

Output: `walking.json` and a report: share of tool time per class, the most repeated reads, and the top three walking costs, each with one proposed slide. A slide is a change that brings the input to the work, as a slide on the bench brought the part to the assembler.

## Steps

### 1. Measure

For a transcript: `python3 -I "<skill>/scripts/walking_time.py" [--session <id>] <session.jsonl> [more.jsonl] > walking.json`

For a job: `python3 -I "<skill>/scripts/walking_time.py" --steps steps.json`, with `[{"name": "read rows", "class": "gather", "seconds": 40}]`.

Each tool call's time runs from its call to its result. Classes: `gather` (reads, searches, listing and read-only shell commands), `wait` (monitors, sleeps, background agents), `work` (edits, writes, other commands). Repeated reads count the Read tool and absolute paths of files that exist, named by read-only shell commands; relative paths and Grep or Glob targets are not counted. It also totals `tokens`, and lists `unfinished_calls` that never returned; a long one can be a stall, so name it. It covers the main thread only. The output also gives `elapsed_seconds`, `tool_clock_seconds` (parallel calls counted once), `before_typed_prompts_seconds` and `unaccounted_seconds`, so report the whole clock, not only tool time. Shares add up each call's own time. A call cut off when a session ended goes to `unfinished_calls`, and one moved to the background is listed in `moved_to_background` with only the time until it moved. An answer box left open can also hold the gap when a session ended, so check any large `human_seconds` before calling it the owner's time. A background agent or workflow returns at launch, so its time does not show as `wait`: check `unaccounted_seconds` and the notifications. The time between a result and the next call is `model_seconds`. Time the owner takes to answer a question is `human_seconds`. Both stay out of the shares, so a person's pause never counts as the session walking.

The script prints tool names, file paths and each command's first word, never command text or file contents, because transcripts can hold secrets. A transcript with no tool calls is an error.

Completion: the script exits 0 for each transcript, or you report which session has no records anywhere and stop.

### 2. Check the classes

The classes are a rule of thumb. Find the five slowest calls in the transcript by their `id` and `at`, and confirm each class, because a slow `cat` of a huge file and a long build look alike in a summary. Correct any wrong one in your report with its reason.

Completion: the five slowest calls are each confirmed or corrected.

### 3. Name the top three

Rank by seconds and by repeated reads. For each cost, write the number, what caused it and one slide: an index, a one-command fetch, a note in the queue record, a pinned path. Say what the slide would save, and label that an estimate.

Completion: three costs each have a number, a cause and one slide; if fewer exist, or a cost sits in helper agents this script cannot read, say so.

### 4. Report and stop

Lead with the walking share. Name the sample and its limits: one session's share is not a rule for all sessions. Building a slide is separate work.

Completion: the report names the sample, the shares, tokens, any stall and the slides, and names no person as slow.

## Anti-Patterns

- Treating all reading as waste; reading is how work starts. The target is repeated and avoidable walking.
- Reporting a percentage with no sample size.
- Ranking sessions or people against each other.
- Printing command text from a transcript; it can contain tokens.
- Calling a slide's saving measured before anyone has built it.

## Source and adaptation

