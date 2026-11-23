---
name: useful-times-bid
description: "Use when more than one sportsbook, prediction market, affiliate or partner wants the same paid spot on the main product, a card, an alert or a member note; when the owner asks who should get the slot or says pay for useful, not loud; or when the top bidder is about to win by default. Not for keeping a paid spot labeled and apart; use tailered-ai:never-sell-the-answer. Not for what members pay; use tailered-ai:price-on-value."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Useful times bid

Rank paid spots by what members use times what the payer bids, not by the bid alone. Google's 2002 AdWords auction weighed each bid by how often people clicked the ad, and Quality Score followed in 2005. The guard: clicks are not usefulness. A loud bonus offer draws the most clicks and can do a bettor the least good. The owner's rule: pay for useful, not loud; weigh what readers use with what anyone pays.

## When to Activate

- Two or more payers want the same paid spot.
- The owner asks who gets the slot or says "useful, not loud".
- The top bidder is about to win with no use check.

Do not use for:
- keeping the paid spot labeled and apart from the core result: tailered-ai:never-sell-the-answer;
- setting what members pay: tailered-ai:price-on-value.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the spot, the candidates and bids, and member data on books and markets used.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `slot-ranking.md`: each candidate's bid, use score and product, both orders, the floor and the verdict.

## Steps

Lead the reply with the ranking table, then the verdict line, then the detail.

### 1. List the candidates and bids

Give each candidate's bid per month and who it serves: about 70% of members trade prediction markets, 30% use sportsbooks.

Completion: a table of candidate, bid and audience served.

### 2. Score use, not clicks

Score use from 0 to 1 from what members do: the share who hold an account there, and how often its price is best on the main product for their leagues. A click counts only if the account is still used after 30 days. A sign-up bonus adds nothing.

Completion: a use score per candidate with its source or marked `proposal`.

### 3. Rank both ways

Show the order by bid alone and by use times bid. Set a use floor, such as 0.2; below it a candidate gets no spot at any bid.

Completion: both orders shown, the floor stated, and the winner by use times bid.

### 4. Give the verdict

Award, hold or decline. The owner decides; name who rechecks the scores in 30 days. The spot still passes tailered-ai:never-sell-the-answer. Draft replies for the owner and send nothing; a live change ships through tailered-ai:workflow and the release coordinator on the owner's word.

Completion: award, hold or decline, the owner, the review date and the release route.

## Anti-Patterns

- Highest bid wins with no use score.
- Counting clicks or sign-ups as usefulness.
- Ranking by a bonus size members cannot keep.
- Letting the score touch the core result or price order.

## Source and adaptation

Source: original Tailered AI skill, which cites Google's 2002 AdWords auction, its 2005 Quality Score. No third-party skill text is copied.
