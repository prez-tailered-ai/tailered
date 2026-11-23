---
name: replace-the-best-seller
description: "Use when a challenger model, version or method may beat the live company model; when a backtest or shadow run says the challenger wins; when the owner says replace it, switch the model or the challenger won; or when a winning challenger has waited days for a switch. Not for choosing which challengers to try; use tailered-ai:ai-model-research. Not for the season's model calendar; use tailered-ai:yearly-model-clock. Not for copying a rival's feature; use tailered-ai:copy-then-outgrow."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Replace the best seller

Jobs replaced Apple's own best sellers before rivals could: the iPod nano replaced the best-selling iPod mini in September 2005. The owner: when a challenger beats the live model on a fair test, switch that day. The guard: a test picked after the results is a switch on noise, so the test is frozen first. "That day" means the switch request is ready that day; it ships on the owner's exact word.

## When to Activate

- A challenger may beat the live model.
- A backtest or shadow run says the challenger wins.
- The owner says "replace it", "switch the model" or "the challenger won", or a winner has waited days.

Do not use for:
- choosing challengers: tailered-ai:ai-model-research;
- the season's model calendar: tailered-ai:yearly-model-clock;
- copying a rival's feature: tailered-ai:copy-then-outgrow.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: both models, the test results, and the test rules with their date.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank. When you cannot open the page, file or data a step asks for, still fill every row: name the exact page, file or command to check and the value you expect there, marked `proposal`. Every row of every table gets a verdict word and an owner.

Output: `switch.md`: fairness answers, verdict, switch request with rollback, look-back date.

## Steps

Lead the reply with one line: switch, keep or rerun, then both models' numbers on the same test (log loss, Brier and closing-line value for live and challenger, as proposals if unseen), the owner, and for rerun the date.

Lead the reply with the fairness table and both models' numbers, then the verdict line, then detail.

### 1. Check the test was fair

Answer four questions. Were the metric and win margin written before results? Were both models scored on the same held-out games? Did each use only data known before each start? Is the gap bigger than noise? Proposal rules: log loss and closing-line value, the last 300 games per league, and a 90% bootstrap interval on the gap that excludes zero.

Completion: four yes or no answers and the date the rules were frozen.

### 2. Call it

Switch (all four yes and the challenger ahead), keep (the live model ahead or level), or rerun (any no, with the rerun named). Name the owner.

Completion: the verdict word, the two models' numbers, and the owner.

### 3. Write the switch request that day

On a switch, write the request the same day: the leagues and cells that change, the rollback (the old model kept, one step back), and the check after the switch. Carry it through tailered-ai:workflow; it ships through the release coordinator on the owner's exact word. This skill does not repoint the live model.

Completion: the request dated the same day as the verdict, with rollback and release route.

### 4. Watch the first slate

After it goes live, compare the first slate's published numbers with the challenger's test output. Set a look-back date.

Completion: the first-slate check result, a look-back date and its owner.

## Anti-Patterns

- Choosing the metric after seeing the results.
- Waiting a season while a fair winner sits idle.
- Switching with no rollback.
- Calling the switch live before the owner's word.

## Source and adaptation

Source: original Tailered AI skill, which cites the iPod nano's replacement of the iPod mini (2005), the iPhone's effect on iPod sales. No third-party skill text is copied.
