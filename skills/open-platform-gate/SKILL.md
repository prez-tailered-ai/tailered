---
name: open-platform-gate
description: "Use when someone outside the company wants to build on its data: an API, a data export, an embed or widget, a developer, an affiliate site or a partner app showing the company's projections; when the owner says open it up, let others build on it, or platform; or before any outside party gets an access key. Not for bringing an outside tool into the company; use tailered-ai:license-not-rebuild. Not for reading the partner's contract; use tailered-ai:growth-cap-check."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Open platform gate

Let others build on the company's projections, through a gate that decides what goes out. Facebook opened its platform to outside apps in 2007 and its Graph API in 2010, and apps grew on its network. The guard: through that opening, one app reached data on up to 87 million people, mostly friends of users who installed it, the Cambridge Analytica case. Outside builders get public projections; member data never goes out, and no member's data is shared because someone else agreed.

## When to Activate

- Someone asks for an API, export, embed, widget or partner feed of the company's data.
- The owner says "open it up", "platform" or "let others build on it".
- Before any outside party gets an access key.

Do not use for:
- bringing an outside tool into the company: tailered-ai:license-not-rebuild;
- reading the partner's contract: tailered-ai:growth-cap-check;
- checking a projection claim in public: tailered-ai:prove-it-in-public.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: who wants access, what they want to build, and the fields, leagues and refresh rate they ask for.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `gate.md`: the field table with each field's class, the limits, the owner, and the verdict.

## Steps

### 1. Sort every field

List each field they would get. Mark each public (published projections, game times, public market prices), internal (model inputs, weights, unpublished numbers) or member (anything about a member: email, phone, follows, usage, payment). Only public fields may go out.

Completion: a table with every field and its class.

### 2. Close member data

Remove every member field. Also remove anything that reveals a member indirectly, such as counts for small groups or who follows what. Member data collected for one purpose is never used for another, such as a partner's marketing, without that member's own consent; one member's consent never covers another member.

Completion: zero member fields left, and the removed fields listed.

### 3. Set the limits

Write: requests per day, delay behind the main product (such as 15 minutes), a label that the numbers are estimates, never advice, logging of every call, a switch to cut access, and a review date. Name the owner who holds the switch. Mark guessed numbers `proposal`.

Completion: six limits written with numbers and a named owner.

### 4. Give the verdict

One word: open (as listed), limit (fewer fields or slower) or close (no access). Issuing a key and any live change go through tailered-ai:workflow and the release coordinator on the owner's word. This skill creates no keys and sends no data.

Completion: the verdict, the field count going out, and the release route named.

## Anti-Patterns

- Giving out member data because the partner asked nicely.
- Sharing friend or follower data on one member's consent.
- Access with no switch and no log.
- Letting a partner present projections as picks.

## Source and adaptation

Source: original Tailered AI skill, which cites Facebook Platform (2007), the Graph API (2010), Facebook's 2018 Cambridge Analytica estimate. No third-party skill text is copied.
