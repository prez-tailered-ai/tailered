# Search plans and report sections

## Plans by purpose

| Purpose | Queries | Ranking | Relevant date | Report stresses |
|---|---|---|---|---|
| Novelty | three narrow queries on the invention's own terms; two broad concept queries with synonyms on two sites; one class-restricted query | claim-language overlap with the description | priority date, against the expected filing date | closest art and how the claims differ |
| Freedom to operate | broad queries limited to active (not expired, not abandoned) patents in the chosen jurisdictions; claim text of each active hit | risk per active claim | grant date and status | flags per jurisdiction, claim-by-claim risk |
| Landscape | broad queries on the technology space; dominant classes; filer tally in those classes; ten-year filing trend for the top five filers | filing volume and trend | publication date | filer map, growth areas |
| Acquisition diligence | the target, its subsidiaries and named inventors as assignee and inventor searches; recorded assignment chain; family grouping | portfolio coverage | grant and assignment dates | portfolio table, ownership checks |
| Litigation prior art | the target patent number (validate the format first), its priority date, art before that date in the same classes, searches on adjacent claim language | how directly a hit anticipates the target's claims | the target's priority date as the cut-off | ranked knock-out candidates |

## Classification follow-up

Patents describe one idea in many vocabularies: older terms, another field's words, or deliberately unusual wording to widen claims. Examiner-assigned classes bridge that. The cooperative classification is shared by the major offices; the international classification is the fallback in some. Both are hierarchical (section, class, subclass, group).

Pattern: run the keyword queries; read the classes of the top five hits; find the one to three dominant classes; run one query with the same keywords plus the class filter (one per class if several dominate); merge, group families, rank. Example: a modern "AI diagnosis" keyword search plus the medical-informatics diagnosis class also surfaces decades-old expert-system and decision-support patents.

Missing class-adjacent art means a false "novel", false confidence to ship, or a weak invalidity case.

## Report sections

1. Summary and verdict: purpose banner, one-line verdict, three or four key findings, legal disclaimer.
2. Closest art: five to ten ranked hits, each with linked number and title, assignee, priority and filing dates, claim 1 text, score and reason.
3. Landscape: top ten filers, ten-year trend, class distribution (full for landscape and diligence, short otherwise).
4. Citation signals: foundational patents (heavily cited) and recent citation activity if the optional index ran; otherwise "manual review recommended".
5. Geography: filings by jurisdiction for the top ten (freedom to operate, landscape, diligence only).
6. Freedom-to-operate flags: patent, jurisdiction, relevant claims, risk (high, medium, low), mitigation note.
7. Strategy: novelty, ways to differentiate the claims; freedom to operate, design-around ideas and jurisdiction choices; landscape, filers to watch; diligence, portfolio red flags; litigation, ranked knock-out candidates. Each with the counsel-review line.
8. Audit: searches (number, query, site, results, status), counts, rate or tier limits met, failed steps, attorney reminder.

## Failure handling

Generic description: one push, then proceed with a caveat. Rate limited: wait, retry once, switch site. Claims unreadable: abstract only, flagged. Family grouping incomplete: say so and suggest manual checking. Under three hits: report as niche or a real gap.
