---
name: move-fast-stable
description: "Use when the owner wants to ship every day, asks how fast we can ship or how long a broken main product may stay broken, says move fast or keep it steady, when the day build broke after a change, or when no fix-time promise is written down. Not for carrying one change to release; use tailered-ai:workflow. Not for deciding one change is reversible; use tailered-ai:two-way-door-call."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Move fast, stable

Ship small changes every day, on a day build that must not break. Facebook's early motto was to move fast and break things; in 2014 it became move fast with stable infrastructure. The owner's version: ship daily, keep the day build steady, and write down how fast a break gets fixed. The guard: a routine change can still take everything down, as Meta's six-hour outage in October 2021 showed, so the promise is a rollback time, not a hope.

## When to Activate

- The owner says "ship daily", "move fast", "keep it steady" or asks how long a broken main product may stay broken.
- The day build broke after a change and nobody knew how fast it had to be fixed.
- Changes are piling up for one big release.

Do not use for:
- carrying one change through release: tailered-ai:workflow;
- sorting one decision as reversible or not: tailered-ai:two-way-door-call;
- pinning one fixed bug with a test: tailered-ai:ai-regression-testing;
- diagnosing a live break: tailered-ai:agent-introspection-debugging.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the changes waiting to ship, the day build's last 30 runs, and past breaks with how long each lasted.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `ship-rule.md`: the stable core, the daily ship rule, the fix-time promise with an owner, and the verdict.

## Steps

### 1. Name the stable core

List what must not break: the day build finishing, the publishing step, the member main product loading with today's numbers beside market prices. Each item gets a check a command or file decides. Everything else may move daily.

Completion: a list of three to six core items, each with its check.

### 2. Write the daily ship rule

Each daily change is small, sits behind the core checks, and has a rollback tested before it ships. Set a size limit in files or lines. A change that touches the core waits for a slower path.

Completion: the size limit as a number, and the rule in two or three sentences.

### 3. Write the fix-time promise

For a core break: detect within N minutes, roll back within N minutes, fix or explain to the owner within N hours. Name the owner who rolls back, by session or person. Base the numbers on the past breaks; with none, propose numbers and mark them `proposal`.

Completion: three numbers, a named owner, and the past break they were measured against.

### 4. Judge and route

Compare the last 30 runs with the promise. Give one verdict: keep (promise met), change (missed; slow the ship rate or tighten the checks), or stop daily shipping until the core holds. Each daily change still ships through tailered-ai:workflow and the release coordinator on the owner's word. This skill ships nothing.

Completion: the verdict with the run count that decided it, and the release route named.

## Anti-Patterns

- Shipping daily with no written fix time.
- Calling a break fixed when it was only noticed.
- Big changes split into small ones that cannot ship alone.
- Skipping the release word because the change is small.

## Source and adaptation

Source: original Tailered AI skill, which cites Facebook's 2012 IPO letter, the 2014 F8 motto change, Meta's October 2021 outage post. No third-party skill text is copied.
