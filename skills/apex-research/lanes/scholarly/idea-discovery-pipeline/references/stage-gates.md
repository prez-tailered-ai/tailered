# Stage gates

A gate checks evidence that already exists. It creates none, and it never counts a heading, a "done" note or a self-score as evidence. Each stage records one `report` entry in the research ledger naming its report section and the section's SHA-256 when it passes.

| Stage | Report section | Gate passes when | Ledger entries |
|---|---|---|---|
| 0 context | Context | protocol entry exists with budget and pilot rule | `protocol` |
| 1 survey | Literature landscape | section non-empty; lane report present; at least one lane contributed | `search`, `source`, `report` |
| 2 ideas | Ranked ideas | every idea has feasibility, cost and quick-novelty notes; do-not-repeat list applied; pilots run only under the pilot rule, with results or "plan only" | one `disposition` per idea (`claim_kind: recommendation`, `held`), `report` |
| 3 novelty | Novelty verification | every carried idea has a verdict, a named paper for any ABANDON, and the reviewer identity | `disposition` per idea, `report` |
| 4 review | Critical review | reviewer identity recorded; a clear proceed or abandon stance; negative results were in the brief | `passage` with the stance, `report` |
| 5 refine | Refined proposal | problem anchor, one-sentence method, claims to test, minimum evidence, first three runs | `report` |
| 6 final | Gate result | stages 0 to 5 all passed | `report` with PASS or BLOCKED |

## Rules

- A reviewer-bearing stage (3 or 4) passes only with a returned verdict and the reviewer identity actually used. `unavailable` blocks it.
- Positive verdicts: PROCEED and PROCEED WITH CAUTION at stage 3; any bottom line not arguing to abandon at stage 4.
- A negative verdict eliminates that idea, recorded under Eliminated ideas with the reason and, for failed ideas, a `lesson` entry with the research reason. It does not reopen stage 2.
- A failed gate stops the pass. The report names the stage and the missing evidence as `BLOCKED: <stage> evidence missing`. Starting again is a new invocation the user chooses.
- PASS at stage 6 is evidence that the pass completed. It is not approval to run experiments or spend compute; that needs the owner's word.
