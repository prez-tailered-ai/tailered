# Evaluation criteria: scoring anchors

Read when a score sits on a boundary (4 or 3, 2 or 1). Every anchor assumes the evidence rule: the score cites what was verified or the exact gap.

## Accuracy

| Score | Anchor |
|---|---|
| 5 | Every claim verified against tool output, documentation or the codebase; no errors. |
| 4 | One minor inaccuracy that does not affect correctness (a wrong default value, a misnamed option). |
| 3 | One significant factual error, or three or more minor ones (a library that is not the project's). |
| 2 | Several significant errors; the output would fail if followed. Also any claim that retained tool output contradicts. |
| 1 | Fundamentally incorrect: syntax errors, a nonexistent endpoint, a signature the code disproves. |

## Completeness

| Score | Anchor |
|---|---|
| 5 | All explicit and implicit requirements covered; edge cases and error paths handled. |
| 4 | All explicit requirements covered; one implicit requirement missed. |
| 3 | One explicit requirement missed, or two or more implicit gaps. |
| 2 | Several explicit requirements missed; a partial solution. |
| 1 | Misses the core request; delivers something adjacent. |

## Clarity

| Score | Anchor |
|---|---|
| 5 | Structured for scanning; terms defined or avoided; no ambiguity. |
| 4 | Generally clear; one section could be better organized or one term is undefined. |
| 3 | Understandable after re-reading; several organizational issues or undefined terms. |
| 2 | Confusing in places; the reader would need follow-up questions. |
| 1 | Unintelligible or self-contradictory. |

## Actionability

| Score | Anchor |
|---|---|
| 5 | One action required and the verification path is cited (the command and its result). |
| 4 | One action required; the verification path is implied, not cited. |
| 3 | Several actions required, or one action with an unclear next step (which file, which path). |
| 2 | The user must assemble how to use the output: missing run instructions, missing test, missing file. |
| 1 | Cannot be acted on without significant rework or clarification. |

## Conciseness

| Score | Anchor |
|---|---|
| 5 | Every sentence earns its place; no repetition. |
| 4 | Minor redundancy; one passage could be tightened. |
| 3 | Noticeable redundancy; a fifth or more could go without loss. |
| 2 | Significantly bloated; restates the question, includes irrelevant background. |
| 1 | More filler than substance. |

## Edge cases

- Ambiguous request: do not penalize completeness for not reading minds. State the interpretation chosen and the score under the alternative.
- Simple task: a three-line fix done correctly can score 5 on every axis. Invent no gaps.
- Error caught and fixed before delivery: accuracy is judged on what was delivered; note the self-correction as evidence of verification.
- Tool output contradicts a claim: accuracy is at most 2. Tool output is ground truth.
- Hard gate failed: report it first; the axis scores and any average describe the output's quality and do not change the gate.
