---
name: private-by-default
description: "Use when a feature shows, shares, stores or reuses member data, such as a leaderboard, tracked positions, followers, handles, linked accounts, emails or location; when a default decides who sees member activity; when the owner asks is this private or who can see this; or before member data goes into logs or a new store. Not for outside parties building on the company's data; use tailered-ai:open-platform-gate. Not for growth use of member data; use tailered-ai:activation-number."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Private by default

Member data a feature shows or shares starts off. In February 2010 Google Buzz exposed people's frequent Gmail contacts by default; the 2011 FTC order required a privacy program and 20 years of audits, and Google built up privacy engineering. The guard: in 2018 a Google+ bug exposed profile data of up to 500,000 users and Google+ was shut down for consumers. Review the default and the code, not only the intent.

## When to Activate

- A feature shows, shares, stores or reuses member data, or a default decides who sees it.
- The owner asks "is this private" or "who can see this".
- Member data is about to go into logs or a new store.

Do not use for:
- outside parties building on the company's data: tailered-ai:open-platform-gate;
- growth use of member data: tailered-ai:activation-number;
- hardening an agent's own tools and keys: tailered-ai:agent-security-hardening.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the feature, the member data it touches, its defaults and its stores.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `privacy-review.md`: the data map, defaults, store checks and verdict.

## Steps

Lead the reply with the data map, then the verdict line, then the detail.

### 1. Map the data

List each piece of member data the feature shows, stores, shares or reuses, and what the member gave it for.

Completion: a table of data items with their original purpose.

### 2. Set the defaults

For each item: who sees it by default. Anything shown to other members or reused for a new purpose starts off, with a clear control the member turns on and can turn off. A feature that only works with sharing on says so before the member opts in.

Completion: a default and a control for every item.

### 3. Check the store

Where each item is kept, who and what can read it, whether it lands in logs, how a member deletes it, and that no key sits in code or a file. Test with made-up members, never real ones.

Completion: five answers per store: location, readers, logs, deletion, keys.

### 4. Decide

Ship, change, with each fix listed, or stop. Name the owner of the fixes. A live change ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict word, the fixes, the owner and the release route.

## Anti-Patterns

- Sharing on by default, with an off switch buried in settings.
- Using data given for login or billing for anything else.
- Real member records in test runs or logs.
- Reviewing the plan but not the code that ships.

## Source and adaptation

Source: original Tailered AI skill, which cites the 2010 Google Buzz launch, the FTC's 2011 order, and Google's October 2018 Google+ announcement. No third-party skill text is copied.
