---
name: pass-the-saving
description: "Use when someone proposes a sale, promo code, discount, free week or launch price for membership; when a cost the company pays falls and the owner asks what to do with the saving; or when the owner says everyday low price or no sales. Not for working back from a price the owner named to job costs; use tailered-ai:price-forces-cost. Not for what a membership is worth; use tailered-ai:price-on-value."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Pass the saving

Pass a real saving through as a steady price instead of running sales. Walton's rule was to buy cheaper, price lower and sell more, every day, in place of weekly sales that trained shoppers to wait. At the company a promo code or a free week is the sale; a lower steady price, or the saving spent on the product, is the everyday price. The guard: Walmart's low prices were reported as pushing hard on supplier margins. A saving counts only if it comes from the company's own costs, not from a squeezed supplier or a thinner product.

## When to Activate

- Someone proposes a sale, promo code, discount, free week or launch price.
- A cost the company pays falls, such as a cheaper feed or host.
- The owner says "everyday low price", "no sales" or asks what to do with a saving.

Do not use for:
- working back from a price the owner named: tailered-ai:price-forces-cost;
- what a membership is worth: tailered-ai:price-on-value;
- approving a new spend: tailered-ai:frugal-first.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the promo proposed or the cost that fell, today's member price and member count.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `saving.md`: the saving in dollars, the real-or-not check, the three-way comparison and the verdict.

## Steps

Lead the reply with the comparison table, then the verdict line, detail after.

### 1. Name the saving or the promo

State what changed in dollars per month: a cost that fell, or the revenue a promo would give up.

Completion: one monthly dollar figure with its source, or marked `proposal`.

### 2. Check the saving is real

The saving must come from the company's own cost going down. It is not real if it comes from cutting accuracy, price freshness or a supplier's fair margin.

Completion: the word real or not real, with one line saying why.

### 3. Compare sale, steady price and product

Compare three paths for the next six months: a promo (a discount for some weeks, then back up), a lower steady price for every member, or the same price with the saving spent on the product. Show the monthly revenue effect of each at today's member count.

Completion: a three-row table with the monthly dollar effect of each path.

### 4. Give the verdict

Choose pass through (the new steady price), keep (spend it on the product) or stop the promo. The owner decides. A price change goes live only through tailered-ai:workflow and the release coordinator on the owner's word; nothing changes in billing here.

Completion: one verdict, the number behind it and the release route.

## Anti-Patterns

- A launch discount that becomes the real price.
- Calling a cut in freshness or accuracy a saving.
- Pricing up first so a sale looks generous.
- Changing price in billing before the owner's word.

## Source and adaptation

Source: original Tailered AI skill, which cites Walton and Huey, Sam Walton: Made in America (1992), and Fast Company's reported 2003 account of supplier pressure. No third-party skill text is copied.
