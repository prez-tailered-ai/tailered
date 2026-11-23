---
name: builder-starter-kit
description: "Use when approved outside builders on the company's data, such as a developer, modeler, affiliate site or partner app, stall, repeat questions or never ship; when the owner says help them build, developer docs or sample code; or before the first outside builder starts. Not for deciding who gets access; use tailered-ai:open-platform-gate. Not for hiring an outside builder; use tailered-ai:bring-in-the-builders."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Builder starter kit

Microsoft's first product, BASIC, was a tool for developers, and it kept winning them with Visual Basic, the developer network and evangelists. The practice: help outside builders succeed fast with tools, samples and a named contact. The guard: the 2001 appeals ruling upheld that Microsoft misled Java developers into Windows-only tools. Builders on the company keep a way out.

## When to Activate

- Approved outside builders stall, repeat the same questions or never ship.
- The owner says "help them build", "developer docs" or "sample code".
- The first outside builder is about to start.

Do not use for:
- deciding who gets access or a key: tailered-ai:open-platform-gate;
- hiring an outside builder: tailered-ai:bring-in-the-builders;
- a public launch explainer: tailered-ai:teach-every-launch.

## Inputs and outputs

Where to work: create a task folder, `artifacts/<skill name>-<YYYYMMDD>/` in the current project (this session's scratchpad if the project is read-only), and write the output there. Tables go in your reply.

Inputs: the builders, the access tailered-ai:open-platform-gate approved, and what they want to build.

Missing inputs never leave a blank. Put in a concrete proposal from what you know, mark it `proposal`, finish every step, and end with the one or two inputs that would change the result. A proposal is a real value: a dollar figure, a name, a date, a game, a list of likely items. Writing missing, pending, unknown, TBD or $X in its place is still a blank.

Output: `starter-kit.md`: first-build target, kit, contact, exit terms, verdict.

## Steps

Your reply leads with the kit table (item, exists or to make, owner), then the verdict line: ready, change or hold.

### 1. Set the first-build target

Pick the smallest thing a builder should get working, such as tonight's NBA projections beside one market price. Set a time target of one hour (proposal), checked with the first builders.

Completion: the first build in one sentence and a time target.

### 2. Make the kit

List what a builder needs: a one-page guide, a sample request and response, test data with no live keys, field meanings, known limits. Mark each exists or to make, with an owner. No member data in any sample.

Completion: every item marked with an owner, and no member data in it.

### 3. Name the contact

Name one person or session who answers builders, the reply time, one working day (proposal), and who adds repeated questions to the guide.

Completion: a named contact and a reply time.

### 4. Keep the way out

Builders own what they build. Data comes as CSV or JSON. No term bars them from other sources or ties their work to the company only.

Completion: the exit terms, and each lock-in term struck or "none found".

### 5. Verdict and route

Verdict: ready, change or hold. Publishing the guide or a live endpoint goes through tailered-ai:workflow and the release coordinator on the owner's word. Nothing is sent to builders from here.

Completion: the verdict, the owner and the route.

## Anti-Patterns

- Docs written for the company, not the builder.
- Samples with live keys or member data.
- Counting builders signed up, not builds working.
- Formats or terms that trap builders.

## Source and adaptation

Source: original Tailered AI skill, which cites Altair BASIC (1975), Visual Basic (1991), the Microsoft Developer Network (1992), reported accounts of Microsoft's developer evangelism, and the 2001 appeals ruling in United States v. Microsoft. No third-party skill text is copied.
