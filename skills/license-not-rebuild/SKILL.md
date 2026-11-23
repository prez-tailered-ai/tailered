---
name: license-not-rebuild
description: "Use when an outside tool, data feed, model or service is winning at something the company was about to build; when the owner says buy the thing that could beat us, partner with them, license it or why rebuild it; or when a build plan copies a product that already exists and could be licensed. Not for reading a deal's terms; use tailered-ai:growth-cap-check. Not for a supplier that has failed us; use tailered-ai:stoppage-to-ownership."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# License, not rebuild

When an outside tool or feed is already winning, bring it in by partnership or license instead of rebuilding it. Zuckerberg bought Instagram in 2012 for about $1 billion and WhatsApp in 2014 for $19 billion, before either could beat Facebook. The company cannot buy companies, so the owner's version is to partner or license. The guards: the FTC sued in 2020 calling the pattern buy or bury, so the aim is to use the tool, not to remove a rival; and no partner gets member data for any purpose beyond the deal, without the member's consent.

## When to Activate

- A tool, feed, model or service does well what the company planned to build.
- The owner says "buy the thing that could beat us", "partner", "license it" or "why rebuild".
- A build plan repeats a product that could be licensed.

Do not use for:
- reading a deal's terms: tailered-ai:growth-cap-check;
- a supplier that has stopped us: tailered-ai:stoppage-to-ownership;
- finding the money for it: tailered-ai:find-it-inside;
- reusing an existing agent skill: tailered-ai:skill-scout.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the outside tool, what the company would build instead, its price if known, and the build estimate in hours.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result.

Output: `license-call.md`: the threat test, the cost table, the data check, the verdict and the owner's open decision.

## Steps

### 1. Test the threat

Say what the tool does that members would leave the company for, or that would take the company months to match. Give evidence: its users, its accuracy, or members asking for it. If it does not threaten the company or save months, stop here.

Completion: one sentence on the threat with its evidence, or the word ignore.

### 2. Compare partner, license and build

For each, give cost for one year in dollars, hours, time until members see it, and the exit if it ends. Build cost counts upkeep, not just the first version. Mark guesses `proposal`.

Completion: a three-row table with all four columns filled.

### 3. Check the data

List what the company's data the deal would send out and what comes in. Member data goes only where the deal needs it, for that purpose only, with consent where it is personal. The partner may not reuse it for ads or marketing.

Completion: a data table with each item, its purpose and its limit.

### 4. Give the verdict

One word: partner, license, build or ignore, with the number that decided it. Name the owner who would run the integration. Send the terms to tailered-ai:growth-cap-check before the owner signs. This skill contacts, signs and pays for nothing; any live change ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: the verdict, its number, the owner, and the next step left with the owner.

## Anti-Patterns

- Rebuilding a tool that already wins because building feels like progress.
- Licensing to keep a rival away from others.
- Counting only the first build, not the upkeep.
- Letting a partner reuse member data.

## Source and adaptation

Source: original Tailered AI skill, which cites the Instagram (2012) and WhatsApp (2014) deals, the FTC's 2020 antitrust suit. No third-party skill text is copied.
