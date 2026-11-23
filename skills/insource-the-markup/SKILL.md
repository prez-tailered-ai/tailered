---
name: insource-the-markup
description: "Use when a supplier, vendor or tool charges many times what it would cost the company to build the same piece; when the owner asks should we build it ourselves, make or buy, or why we pay so much for this; or after tailered-ai:raw-cost-floor returns rebuild. Not for a supplier that has stopped or failed us; use tailered-ai:stoppage-to-ownership. Not for finding idle spend; use tailered-ai:find-it-inside."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Insource the markup

Build in-house the piece a supplier overcharges for. SpaceX built its own engines, avionics and many smaller parts when supplier quotes ran many times its own estimate, as Ashlee Vance's 2015 biography reports. The guard: an in-house part is owned forever. Its upkeep and its delays fall on the builder, as Tesla's slow 2018 Model 3 ramp showed.

## When to Activate

- A supplier's price is many times what the same piece would cost to build.
- The owner asks "should we build it ourselves", "make or buy" or "why do we pay so much for this".
- tailered-ai:raw-cost-floor returned rebuild.

Do not use for:
- a supplier that has stopped or failed us: tailered-ai:stoppage-to-ownership;
- finding idle or duplicate spend: tailered-ai:find-it-inside;
- costing the piece from its raw inputs first: tailered-ai:raw-cost-floor.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the supplier, the piece it supplies, its yearly price, and the floor from tailered-ai:raw-cost-floor if one exists.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `make-or-buy.md`: the piece, the yearly buy cost, the build cost, yearly upkeep and hosting, the payback months, the verdict, the lifetime owner and the exit.

## Steps

### 1. Name the exact piece

Take only the overpriced piece, not the whole supplier. Write what it does in one sentence, its yearly price, and what depends on it: which leagues, which main product cards, which day-build steps.

Completion: one piece, one yearly price and one dependency list.

### 2. Cost the build and the upkeep

Estimate the hours to build it and the hours per month to keep it working: fixes, on-call, data-format changes. Add hosting. Price hours at a stated rate. Unknown figures get a proposal, marked `proposal`.

Completion: build cost, yearly upkeep and yearly hosting, in dollars.

### 3. Compare over two years

Compare two years of the supplier's price with the build cost plus two years of upkeep and hosting. Payback months = build cost divided by the monthly saving. If upkeep plus hosting is at or above the supplier's price, the payback is "never".

Completion: the two-year totals and the payback in months, or "never".

### 4. Give the verdict, owner and exit

Build when payback is under 12 months and the hours exist this quarter. Negotiate when the markup is large but the hours do not exist. Buy otherwise. For build, name the owner of the part for its whole life and the exit: how to switch back to the supplier. Try it in a copy with tailered-ai:one-league-trial first. Going live goes through tailered-ai:workflow and the release coordinator on the owner's word. Nothing is cancelled or bought here.

Completion: build, negotiate or buy, a lifetime owner and a written exit step.

## Anti-Patterns

- Building because the supplier is annoying, not because the numbers say so.
- Leaving upkeep and on-call out of the build cost.
- Replacing the whole supplier when one piece is overpriced.
- Cancelling the supplier before the in-house part has passed a trial.

## Source and adaptation

Source: original Tailered AI skill, which cites Ashlee Vance's Elon Musk (2015) and Tesla's 2018 Model 3 ramp. No third-party skill text is copied.
