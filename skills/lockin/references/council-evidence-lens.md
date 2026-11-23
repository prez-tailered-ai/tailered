# Council: evidence lens first

When a report is read by a council or by more than one reviewer, one voice takes the evidence lens before any other voice ranks a finding. The evidence lens grades the report's own machinery: the parsers that read its inputs, the recounts behind each number, the joins that match one table to another, and every count with no named source. A finding ranked on top of a broken count is a wrong finding; grading the machinery first keeps the council from ranking noise.

Use this file when the review verb runs with two or more reviewers, or when a prompt says "council" or "evidence lens". One reviewer reading alone follows `review.md` as written.

## Steps

### 1. Name the lens holder

Before any voice speaks to the report's findings, the council record names one voice as the evidence lens for this read. The holder reads the report's method, data and counting sections first and the findings last.

Completion: the council record carries one line `evidence lens: <voice>` and that voice has not yet written a finding.

### 2. Grade the report's defects

The holder lists each defect in the report's own machinery, one line each: a parser that misreads a row, a recount that does not reproduce a stated number, a join that drops or doubles rows, a count with no source named. Each line carries the concrete case (this input, this wrong number) and a grade: `blocks` (the findings built on it cannot stand), `weakens` (a finding's size is off, its direction holds) or `cosmetic`.

Completion: every number the report leans on is either reproduced or listed as a defect with its grade, and each line has a concrete case.

### 3. Rank findings only after the grade

The other voices rank findings. A finding that rests on a `blocks` defect is set aside with the defect's line quoted, not ranked. A finding on a `weakens` defect carries that line beside its rank.

Completion: no ranked finding rests on a `blocks` defect, and each `weakens` defect appears beside the finding it touches.

### 4. Record the lens finding

The council record names the lens holder's finding in its own line, above the ranked findings: `evidence lens finding: <the gravest defect, its grade, its case>` or `evidence lens finding: machinery reproduced, no defect`.

Completion: the record's lens finding line exists, sits above the ranking, and quotes a grade from step 2.

## Anti-patterns

- Ranking findings first and grading the counts after; instead grade the machinery, then rank.
- Giving the lens to the voice that wrote the report; instead a voice that did not write it holds the lens.
- A defect line with no concrete case; instead name the input and the wrong number.
