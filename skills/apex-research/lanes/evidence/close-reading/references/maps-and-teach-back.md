# Knowledge maps and teach-back

## Map mode

A map keeps the reasoning, not just the headings.

Node types: THESIS, CLAIM, REASON, EVIDENCE, DATA (with unit, population, period, baseline), EXAMPLE (does not prove generality), CONCEPT (a term the argument depends on), ASSUMPTION, COUNTERARGUMENT, LIMITATION, QUESTION.

Edge labels, always one of: supports, explains, defines, illustrates, depends on, qualifies, contradicts, raises. Position on the page is never a relationship.

Evidence and data nodes carry: location in the source, the claim they attach to, one of the four labels, and any caveat.

Text layout:

```text
THESIS: <central claim>
  supports -> CLAIM: <claim>
    explains -> REASON: <bridge>
    supports -> EVIDENCE: <evidence> (<location>)
    qualifies -> LIMITATION: <boundary>
  depends on -> ASSUMPTION: <premise>
  contradicts -> COUNTERARGUMENT: <alternative>
```

If the user wants a mind-map file format, render the same tree in that format and escape any source text placed in attributes.

Before delivering: every major claim reaches the thesis; every evidence node attaches to a claim; examples are labelled; contradictions and limits stay visible; no conclusion exists only because of layout.

## Teach-back mode

The goal is to expose and fix gaps by recall, not to produce simple wording.

1. Name one target idea, mechanism or chapter claim.
2. Read for structure: claim, terms, mechanism, evidence.
3. Close the text and the notes.
4. The reader explains it from memory in plain words, keeping the causal and logical links.
5. Mark every vague phrase, skipped step, undefined term or leaning on jargon.
6. Find the first link that is not justified.
7. Reread only what repairs that link.
8. Rewrite with the mechanism, a concrete example or a boundary condition.
9. Transfer: apply it to a new case and predict the outcome.
10. Boundary: describe a case where it should not apply.
11. Write short recall prompts for later review.

Gap types: definition (the term is explained only by itself), mechanism (steps without the why), evidence (the claim is remembered, its support is not), boundary (cannot say when it fails), transfer (can repeat, cannot use).

Output sections: target; explanation from memory; gaps found; repaired explanation; transfer test; boundary test; three recall prompts (mechanism, evidence, limitation).

Rules: simplifying must not drop an essential condition; every analogy says where it breaks; reopening the text before the attempt spoils the test; recognising is not recalling; prompts ask for relationships and mechanisms, not vocabulary.
