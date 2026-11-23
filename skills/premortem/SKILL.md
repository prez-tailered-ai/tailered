---
name: premortem
description: "Use when asked for a premortem or pre-mortem, or to premortem something, \"what could go wrong\", \"why would this fail\", or \"assume it failed\"; before building a chosen plan or design; or once a favorite option has been picked. Not for a bug review of a diff, use tailered-ai:lockin review; not for attacking a strategy's assumptions now, use tailered-ai:strategy-red-team; not for deciding release, which goes through the release coordinator."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Premortem

"It is three months from now and this failed badly. Why?" Gary Klein's question frees people to name risks that a forward-looking review smooths over. Its weakness is false alarms: a risk flagged by pattern alone, without reading the code around it, wastes the fix budget on things already handled. This skill keeps the question and adds a verification pass, so every tiger it reports carries the evidence that no mitigation exists.

## When to Activate

- "Premortem this", "what could go wrong", "why would this fail", "assume it failed".
- A plan has been chosen and building is about to start (deep).
- A plan change or a merge-ready change needs its failure modes named (quick).

Do not use for:
- a bug review of a diff with findings to fix: tailered-ai:lockin review;
- attacking a strategy's load-bearing claims now: tailered-ai:strategy-red-team;
- deciding release: production goes through the release coordinator with the owner's word.

## Inputs and outputs

Input: the target (a plan file, a diff, files or a design) and the depth. Quick fits a plan, a PR or a localized change; deep fits a whole implementation before it starts. With no depth named, pick from that rule and say which.

Output: the premortem record in the format in `references/checklists.md`, plus a short summary and one decision question for the owner. This skill changes no code. After the owner decides, it writes only two things: the plan's mitigation section, when mitigations are chosen, and the task record (the premortem record file in the task folder; with no plan file, the mitigation section goes there too).

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, fetch the missing inputs you can reach yourself, and end with the one or two you could not reach that would change the result.

## Steps

### 1. Frame the failure

Read the whole target. Write one line: "It is three months from now and <target> failed. Why?" Name the depth.

Completion: the target was read in full (for a change inside a larger file: the changed lines and every path they touch), and the frame line and depth are written.

### 2. Gather suspected risks

Run the quick or deep checklist in `references/checklists.md` against the target and write every suspected risk, with no filtering yet. Include the unspoken ones: no tests, no owner, a date nobody believes, "we'll watch the logs". Include input the code does not expect: a missing parameter, malformed input, an empty body.

Completion: every checklist item for the chosen depth was asked, and each suspicion has a line.

### 3. Verify each suspicion

For each one, read the code or plan around it from a numbered listing (`nl -ba`), and cite those line numbers: at least 20 lines either side, the fallback or else branch, the try/catch, the caller, and whether the item is even in scope or only in tests or dev code. Run a small check when one can settle it. Then classify it:
- **Tiger**: real, unmitigated, will hurt. Record its location, severity and `mitigation_checked`, the specific mitigations you looked for and did not find.
- **Paper tiger**: looks threatening but is handled. Record where the mitigation is, by file and line.
- **Elephant**: a risk nobody wants to say out loud, often about process, ownership or dates.
- **False alarm**: verified, and nothing there; say why.
- **Unverified**: the target cannot settle it (it depends on a host, a proxy or data you cannot see). Record the check that would settle it and who can run it; it is neither a tiger nor a false alarm.

Input from an unauthenticated caller that can kill the process or corrupt data is a high tiger. A suspicion with any verification check unanswered is not a tiger. A handled case can still hide a smaller real risk (a silent fallback with no log); record that under low risks.

Completion: every suspicion is classified; every tiger has a location, a severity and a filled `mitigation_checked`; every paper tiger names its mitigation's location; every unverified item names its settling check.

### 4. Hand the decision back

Summarize the counts and the high tigers and high elephants first. Ask the owner one question with the host's question tool: accept the risks, add mitigations to the plan (recommended when a high tiger or high elephant exists), research mitigations, or discuss one risk. High tigers and high elephants block until mitigated or explicitly accepted; medium ones inform. An accepted risk is the owner's call on the plan only; it never stands in for release approval.

Completion: the owner has the summary and the question, and no code was changed.

### 5. Record the outcome

When mitigations are chosen, append a "Risk mitigations (premortem)" section to the plan: each tiger and each high elephant, its mitigation and the phase it lands in; each accepted risk with the reason; the date, depth and counts. Rerun a quick premortem on the mitigated plan; when it finds any high tiger or high elephant, new or remaining, go back to step 4 with it. When the owner accepts the risks instead, record the acceptance and the reason in the task record; no rerun is needed. When the owner asks to research mitigations, give 2 to 4 options per high tiger or high elephant, each with its location or source, then return to step 4. When the owner asks to discuss one risk, discuss it, then return to step 4.

Completion: the plan or the task record shows each tiger's and each high elephant's disposition, and either a rerun found no high tiger or high elephant, new or remaining, the acceptance is recorded with its reason, or the owner's next choice at step 4 is recorded.

## Anti-Patterns

- Flagging a tiger from pattern alone, without reading the lines around it.
- A tiger with no location or no `mitigation_checked`.
- Filing something you could not check as a false alarm; it is unverified.
- Dropping a paper tiger silently; listing it with its mitigation shows the reader it was checked.
- Fixing the code during the premortem; the owner decides first.

## Source and adaptation

Source: `premortem` from parcadei/continuous-claude-v3, commit `d07ff4b06b62f43771bc0c927d0211b734d6149e`, SKILL.md SHA256 `ee0f02aad10415ab9b875e1992fc7be0f3678e9d7add4364848e6874cec9cc42`. License: MIT, Copyright (c) 2026 Cosimo Streppone (see NOTICE.md at the plugin root). Method after Gary Klein, "Performing a Project Premortem", Harvard Business Review, 2007; tiger, paper tiger and elephant categories as the source credits them to Shreyas Doshi. "Clone" was read as adapting into the house format.

Changes: 451 lines compressed to the house step form; the checklists, verification checklist and record format moved to `references/checklists.md`; the source's pseudo-code calls to named helper agents and its integration points with that repo's own plan commands were dropped; release was routed to the release coordinator; added the unverified class, a low-risk slot, unexpected-input suspicions, a loop back to step 4 when a rerun finds any high tiger, and the accept-only path.
