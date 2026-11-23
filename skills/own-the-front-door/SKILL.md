---
name: own-the-front-door
description: "Use when the company's projections, prices or help reach members through places the company does not run, such as Discord, X, a partner site, a reseller or a screenshot channel; when the owner asks where members first meet the product, or says own the experience or our own store; or when members sign up or get help somewhere the company does not control. Not for giving outsiders data or an access key; use tailered-ai:open-platform-gate. Not for planning posts or attention; use tailered-ai:story-not-ads."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Own the front door

Jobs opened Apple's own stores in May 2001 (Tysons Corner, Virginia, and Glendale, California) so buyers met the product, and got help at the Genius Bar, the way Apple meant. The guard: a channel costs real money, and Gateway closed its own stores in 2004. The company owns a web main product, not shops. Spend only where members already are, and the door never hides other books' prices.

## When to Activate

- the company's numbers or help reach members through places it does not run.
- The owner asks where members first meet the product, or says "own the experience".
- Members sign up or get help somewhere the company does not control.

Do not use for:
- outside access to the company's data: tailered-ai:open-platform-gate;
- posts and attention: tailered-ai:story-not-ads;
- paid access after a sale: tailered-ai:after-sale-check.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: every place members or visitors meet the company, with weekly counts where known.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank. When you cannot open the page, file or data a step asks for, still fill every row: name the exact page, file or command to check and the value you expect there, marked `proposal`. Every row of every table gets a verdict word and an owner.

Output: `doors.md`: the door table, help times, and drafts for the owner.

## Steps

Lead the reply with the door table, then the verdict line, then detail.

### 1. Map every door

List each place members meet the company's numbers or help: main product, landing page, Discord, X, partner sites, email, support. For each: who controls it, people per week, and what they see (fresh or stale, with source and time, or stripped).

Completion: a table row for every door with controller, weekly count and what is seen.

### 2. Judge each door

Keep (the company runs it and it shows the real product), bring home (an outside door shows stale or stripped numbers; point it to the main product), or stop (it costs more than it brings, or misleads). Give each an owner.

Completion: every door has a verdict word, the number behind it, and an owner.

### 3. Check help at the door

Where members ask for help, write who answers and the first-answer time (proposal target: within 4 hours on game days). Help pointing members off the company to get an answer is a bring-home.

Completion: the help doors, who answers each, and the measured or proposed time.

### 4. Route the changes

Changes to the company's own surfaces go through tailered-ai:workflow and the release coordinator on the owner's word. Any post, message or change on an outside platform is drafted for the owner; this skill posts and sends nothing.

Completion: each change has its route, and outside changes are saved as drafts for the owner.

## Anti-Patterns

- Letting screenshots on other sites stand in for the main product.
- Paying for a channel before members use it.
- A door that hides other books to keep members.
- Help that sends members elsewhere for answers.

## Source and adaptation

Source: original Tailered AI skill, which cites the first Apple Stores (May 2001), the Genius Bar, and Gateway's store closures (2004). No third-party skill text is copied.
