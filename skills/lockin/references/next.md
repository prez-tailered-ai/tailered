# Next: ten ranked actions, then execute the top N

`/locktfin`, "what's next" and the -plan/-execute flags route here through `tailered-ai:lockin` (the separate locktfin skill was folded in on 2026-11-02).

Turn a scope into **ten ranked actions**, each shipped with the prompt that executes it, then execute the top N. The plan is locked before execution starts, and finished means finished.

## Grammar

```
/locktfin  (or lockin next)   plan only, ten items
-plan                         same
-execute                      plan, then execute the top item
-plan -execute --5            plan, then execute the top 5
--10                          plan, then execute all ten
--asap                        skip the confirmation between items; still gated
/locktfin-execute-10          ask for a directing prompt, then plan and execute ten
```

Every two-way ask the plan sends (a question with a default and one alternative) carries a `defaultSuffices` line (whether the default suffices, and why) and a `goal` line (the outcome the answer serves); an ask without both is a wish, and is rewritten before it is sent.

`--asap` removes the pause between items. It does **not** remove a gate. Nothing merges, deploys or force-pushes under any flag. Execution runs under lock mode (`lock.md`); where the two disagree, the stricter rule wins: lock's no-contact and release coordinator rules plus "merge and deploy are not yours". Example: the owner approved a release earlier and lock would reuse that approval, but next says merge and deploy are not yours, so next prepares the release and hands it to the owner.

## execute-10 asks first

Before planning, ask the operator for a directing prompt covering four things, in one question, without guessing:

- **Concepts:** the domain and the vocabulary the plan should use.
- **Intention:** what "better" means here, so ranking has a criterion.
- **Execution:** what may be touched, what may not, and who merges.
- **Frameworks:** which disciplines apply (test-first, adversarial review, lockin build minimalism, an existing gate).

Without those four, ranking is guesswork dressed as a plan.

## The ten items

Rank by **(value × confidence) ÷ blast radius**, not by how interesting the work is. Unblockers outrank features. A one-line change that unblocks four others outranks a large change that unblocks nothing. Open `shortcut:` debt (lockin debt) is a ranking input: a deferral at its ceiling is an unblocker candidate.

Each item carries exactly this:

```
N. <imperative title>
   Why now:      what is blocked or bleeding until this is done
   Scope:        the files or systems it touches, and what it must not touch
   Risk:         what breaks if it goes wrong, and how it is reversed
   Verification: the command that proves it, and the output that counts as pass
   Prompt:       a paste-ready instruction that executes this item alone
```

The Prompt field is the deliverable. An item without a prompt someone else could run is a wish.

## Definition of done

An item is done when **all** hold:

1. Its stated verification command ran, and its real output is quoted, not summarized.
2. The repo is still accounted for: `tailered-ai:lockin` audit of the touched folder finds no new Must fix item.
3. The full suite is green with zero failures, zero skipped tests, zero todo tests (a skipped test is not a pass; this is separate from the one-line skipped-checks note in the reply).
4. The work tree is clean, and `git diff --check` exits 0.
5. Any close-or-rebuild decision it carries is a decision table with one row per branch (close, rebuild) and one column each for the evidence read, its path, and what it decides; a table with an empty cell is a guess, and the item stays open.

## The audit loop

Next is the ranking stage of a five-stage loop:

```
1  audit     verify and validate the next scope (lockin audit)
2  next      rank the next 5, and the 5 after that
3  execute   grade both, then fix every D and F (lockin build under lock)
4  audit     re-audit after execution: did the fix hold?
5  next      rank takeaways 1-5, then the next 5
```

Stage 4 is the one that gets dropped, and it catches the fix that broke something else. Audit passes count toward `tailered-ai:workflow`'s 3-round stop rule: at the cap the loop ends **stopped, not finished**, with the open items reported to the owner. Each pass must cost less than the one before; record what made it cheaper.

## Always end with the three options

Every next output closes with this, in shape, before the plain restatement:

```
What next?
  A. Next immediate action  — Scope {N}: {Big Idea}
  B. Top 5 next best steps  — Scope {N}: {Big Idea} + Scope {N+1}: {Next Big Idea}
  C. Top 10 next best steps — Scope {N}: {Big Idea} + Scope {N+1}: {Next Big Idea}
```

The Big Idea is the outcome, never the activity. `{N+1}`'s Big Idea must be a real consequence of finishing `{N}`.

## Rules that hold under every flag

- **A gate that has never gone red is not a gate.** Break the thing it guards, watch it fail, restore, and record that you did.
- **Report the real number.** 4/5 is not done.
- **Never delete on a single signal.** Removal needs an owner's decision.
- **Merge and deploy are not yours.** Prepare them; hand them over.
- **Re-rank after every item.**

## Anti-patterns

| Smell | Why it fails |
|---|---|
| Ten items that are one item split ten ways | Padding. Rank fewer, real ones. |
| Verification is "review the output" | Not falsifiable. Name a command and its pass condition. |
| Executing all ten because `--10` was passed | The flag is a ceiling, not a quota. Stop when the next item stops earning its place. |
| Marking done on a green test you never saw fail | You proved nothing. Break it first. |
| Deferring the unblocker because it is boring | Blast radius beats novelty. The unblocker is item 1. |
