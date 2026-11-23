---
name: frugal-first
description: "Use when a new subscription, data feed, API, tool, compute or hire is proposed, when a bill jumps, or when the owner asks to cut costs. Not for setting a price; use tailered-ai:price-forces-cost."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Frugal first

Before spending, get the result with what you have. Frugality is one of Amazon's leadership principles: do more with less, because limits force invention; its early desks were doors on legs. The guard: frugality that reached people's safety backfired, with warehouse injury rates reported above the industry's (Reveal, 2020). So nothing that protects members, data or review is ever on the cut list.

## When to Activate

- A new subscription, feed, API, tool, compute or hire is proposed.
- A bill jumps.
- The owner asks to cut costs.

Do not use for:
- setting a price: tailered-ai:price-forces-cost.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the proposed spend, or the current spend from bills and usage pages.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `spend.md`: a spend table, the frugal path for each line, the protected list and a ranked recommendation.

## Steps

### 1. List the spend

Each line with its monthly cost and what it delivers, starting with every line you can name from the stack: hosting, odds and data feeds, model and agent usage, an AI gateway and DNS, tools. Mark unknown costs as unknown, and rank by likely size until the bill is in.

Completion: the table.

### 2. Find the frugal path

For each new or large line, say what the company already has that does most of it, and the cheapest test of whether the spend changes a result, such as a one-week trial measured against the close.

Completion: an existing alternative and a cheapest test for each line.

### 3. Protect what must stay

Backups, security, reviewers, member-facing correctness, and the owner's release gates are never cut.

Completion: the protected list is stated.

### 4. Recommend

Rank by savings. Buying and cancelling are the owner's to do.

Completion: a ranked list; nothing bought or cancelled.

## Anti-Patterns

- Buying the premium option first and testing later.
- Cutting a backup or a review to save money.
- A saving that costs more hours than it saves.
- Trimming small items while a large line grows.

## Source and adaptation

Source: original Tailered AI skill, which cites Amazon's Leadership Principles and Reveal (2020). No third-party skill text is copied.
