---
name: lease-register
description: "Use when the company relies on a data feed, odds or prediction-market source, host, domain or account held on terms the other side can end; when the owner says check the leases, what could be taken from us, or asks when something renews; before building on a new feed or host; or monthly. Not for a supplier that already stopped us; use tailered-ai:stoppage-to-ownership. Not for caps in a deal; use tailered-ai:growth-cap-check. Not for deepening a supplier; use tailered-ai:partner-for-decades."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Lease register

Know every lease before it ends. Walton's first store, in Newport, Arkansas, sat on a 1945 lease with no renewal clause; in 1950 the landlord took it. Later Walmart owned its systems, down to a private satellite network finished in 1987. The owner's guard: watch every data feed, host and domain held on terms the other side can end. This skill keeps one register of them, each with a renewal date and a fallback.

## When to Activate

- The owner says "check the leases", "what could be taken from us" or asks when something renews.
- Before building on a new feed, host, domain or provider.
- Once a month, or when a supplier changes its terms.

Do not use for:
- a supplier that already stopped us: tailered-ai:stoppage-to-ownership;
- caps hidden in a deal: tailered-ai:growth-cap-check;
- deepening a supplier at renewal: tailered-ai:partner-for-decades.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the last register if one exists, and what the company runs on: odds feeds, prediction-market data (Partner A, Partner B and others), hosting, DNS, an AI gateway, domains, model providers and payment accounts.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `lease-register.md`: one row per lease with owner, end terms, renewal date, fallback, switch days, rating and verdict.

## Steps

Lead the reply with the register table sorted by renewal date, then the verdict line, detail after.

### 1. List every lease

Write one row for each feed, host, domain, account and provider. Name the person who holds the account, not a shared login.

Completion: every item the company runs on has a row with a named holder.

### 2. Read the end terms

From the written terms, note whether the other side can end or reprice it, the notice in days, the renewal date and whether it auto-renews. Read terms only; sign in to nothing.

Completion: each row has can-end yes or no, notice days and a renewal date, sourced or marked `proposal`.

### 3. Name the fallback

Ask the Newport question: if they ended it tomorrow, what stops? For each lease that can be ended, name the fallback (a second source, our own copy, an export) and the days to switch.

Completion: each row has a fallback, switch days and a rating of covered, thin or none.

### 4. Give a verdict

Mark each row keep, add fallback, own or renegotiate, with an owner. List renewal dates in date order for owners to diary; this skill sets no timers. Any host, DNS or feed switch ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: a verdict and owner on every row, the dated list, the route named, and nothing cancelled, signed or moved.

## Anti-Patterns

- Leaving a domain or account in a former helper's name.
- Assuming a free tier or API will stay free.
- Writing "we can switch" with no days and no tested fallback.
- Logging in to read terms instead of reading the published terms.

## Source and adaptation

Source: original Tailered AI skill, which cites Walton and Huey, Sam Walton: Made in America (1992), Walmart's corporate history of its 1987 satellite network. No third-party skill text is copied.
