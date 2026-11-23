---
name: hand-deliver-first
description: "Use when a new model version, main product feature or market is nearly ready and no member has used it; when the owner asks who should try it first, or wants beta testers or early members; or when a feature is being finished on guesses about how members will use it. Not for writing the press release before anything is built; use tailered-ai:press-release-first. Not for checking paid access after a sale; use tailered-ai:after-sale-check."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Hand-deliver first

Put the first unit in a real user's hands. In August 2016 Huang delivered the first DGX-1 to OpenAI himself, and NVIDIA has long built next to the customers who push its products hardest. The owner's version for the company: give an early build to a few named members, watch what they do, and change it from that. The guard: a few early users are not the market, and loud traders can pull the product toward themselves. So their feedback is weighed against the whole audience, about 70% prediction-market traders and 30% sportsbook bettors, and nothing is sent to them without the owner.

## When to Activate

- A model version, main product feature or market is nearly ready and no member has used it.
- The owner asks who should try it first, or wants beta testers or early members.
- A feature is being finished on guesses about member use.

Do not use for:
- writing the press release before a build: tailered-ai:press-release-first;
- checking paid access after a sale: tailered-ai:after-sale-check.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the early build, who could try it, and how long the trial runs.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `early-members.md`: the members and why, the draft invitation, what each did, and the verdict. Member names stay in this file and are not posted.

## Steps

### 1. Pick three to five members

Name them, or describe them by role when names are unknown. Mix the audience: most from prediction markets, at least one sportsbook bettor. Write why each one.

Completion: three to five members, each with a reason and an audience type.

### 2. Draft the hand-off

Write what they get, what we ask of them, how long (one week unless the owner says otherwise) and what they must know: these are estimates, never advice, and this is an early version. This is a draft; the owner sends it.

Completion: a draft invitation, with the owner named as the sender.

### 3. Record what they do

For each member, write what they used, what they asked and what broke, with the source (their words and the date). Write "no response" when there is none. Never fill a row from a guess.

Completion: a row per member with a source, or the words no response.

### 4. Decide

Verdict: keep, change (each change with an owner) or stop. Mark each change with how many members asked and their audience type; one trader's ask is not a mandate. Anything live ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict word, an owner per change, and the release route named.

## Anti-Patterns

- Picking only the members who already like the product.
- Sending the invitation without the owner.
- Turning one member's wish into a feature for everyone.
- Writing feedback nobody gave.

## Source and adaptation

Source: original Tailered AI skill, which cites Huang's delivery of the first DGX-1 to OpenAI in August 2016. No third-party skill text is copied.
