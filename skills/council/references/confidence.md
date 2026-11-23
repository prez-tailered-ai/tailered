# Confidence when asked

The owner's rule. Read by step 5 and step 6 of the council skill.

## Earn the number
Before any percentage, list every fact it rests on, each tagged `verified` (with its source or the command that checked it), `given` or `assumed`. With no `verified` fact, the answer is "No percentage: nothing here is verified", then run the check that would make one possible when you can; name it only when you cannot.

## State it exactly
"My judgment: N to M%, that <named claim> holds by <date>. One model's estimate, not a vote count."
- The range is 10 points wide (20 while the ledger's report shows `widen_by` 10) unless the sources narrow it.
- Cap it at 70% while any critical fact is `assumed`, and say which fact.

## Make it falsifiable
Name the one observation that would move it most, which direction, and roughly how far. Name the date and the source by which the claim will be settled.

## Ledger it
Append one line to `ledgers/confidence.jsonl`: time (`date -u`), claim, range, the facts used with their tags, the settle-by date, the settle source and the session id. A percentage with no ledger line was never given. Lines are added, never edited. With no percentage asked, give High, Medium or Low as before; the ledger line is still written, with `level` instead of `range`.

```
python3 -I "<skill>/scripts/ledger.py" confidence --root <project> --claim "<claim>" --low N --high M \
  --fact "verified:<fact> (<source>)" --fact "assumed:<fact>" --critical-assumed "<fact or none>" \
  --settle-by YYYY-MM-DD --settle-source "<where the outcome will be read>" --session <session id>
python3 -I "<skill>/scripts/ledger.py" confidence --root <project> --claim "<claim>" --level Medium ... (no percentage asked)
python3 -I "<skill>/scripts/ledger.py" council --root <project> --question "<q>" --mode quick|standard|deep \
  --position "<voice>: <position>" ... --recommendation "<path>" --session <session id>
```
The script refuses a range of any width other than 10 points plus the report's `widen_by` without `--narrowed-by "<source>"`, a high end above 70 or a High level while `--critical-assumed` names a fact, a second settle of one claim, a percentage with no `verified:` fact, and a missing settle date or source.

## Score it
On the settle date, record what happened: `ledger.py settle --root <project> --id <line id> --outcome 1|0` (or `--unsettleable`). The Brier score is (p - outcome)^2 with p the range midpoint. An unsettleable claim counts against the council.

## Correct the model with its own record
`ledger.py report --root <project>` prints the count, mean Brier score and how often outcomes fell inside the stated ranges. Once 20 or more claims are settled, every new percentage shows that track record. When outcomes land inside the ranges less than 60% of the time, the next answers widen their ranges (the script prints the widening to use) until coverage recovers.

## Nothing borrowed
The number never comes from how many voices agreed, from the user's tone, or from earlier unscored estimates.
