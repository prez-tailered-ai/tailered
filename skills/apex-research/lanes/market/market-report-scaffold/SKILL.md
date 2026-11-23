---
name: market-report-scaffold
description: Set up and fill an auditable market research report, by fixing the market definition, measure, unit, currency basis, geography, period and classification before any number, routing each question to the source closest to the underlying event, giving every factual or numeric claim an id tied to exact sources, keeping facts, estimates, calculations, forecasts, opinions and recommendations apart, treating sizing and forecasts as conditional scenarios with sensitivity, normalising units before combining values, and checking a report gate before handover. Produces a plain Markdown workspace; any typeset or charted output is optional. Use when someone needs a market report, industry landscape or forecast that others will audit. Not for the sizing arithmetic itself, a one-company teardown, or investment, legal or regulatory advice.
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Market report scaffold

A market report whose every number can be traced. The scaffold fixes what is being measured, holds the evidence in the research ledger, keeps calculations and assumptions in named files, and checks the whole before anyone reads the conclusions. Length, chapter count and visuals follow the question; none is required.

## When to Activate

- "Write a market report on", "industry landscape for", "forecast this market", "build a report others can audit".
- An existing market deck needs every figure traced to a source or marked as an assumption.
- Several sizing or forecast scenarios must be presented together with their sensitivities.

Do not use for:
- Total, serviceable and obtainable sizing arithmetic and segment scoring: market-sizing.
- A dated competitor table: competitive-research-snapshot; one company in depth: competitor-teardown.
- A market question tied to one decision: decision-market-research.
- Investment, legal, antitrust, tax or accounting advice: out of scope.

## Capability and access

Writing and local arithmetic need no network. Research uses the host's search and fetch tools or fact-database-lookup for official statistics and filings, each unverified until a call returns a well-formed answer, and only within the user's approved sources and terms. A typeset document is optional and built only with a toolchain the project already has; no image generation or document toolchain is installed or required. Charts, if wanted, come from the workspace data files.

## Inputs and outputs

Inputs: the decision, audience, deadline and materiality threshold; approved source types; whether primary research (survey, interviews) exists.

Workspace (Markdown and CSV or JSON, at a path the user chooses):
- `contract.md`: the definition fields from step 1.
- `report.md`: modules chosen for the question (summary, definition, demand, supply and competitors, sizing, forecast, risks, method), every claim tagged with its claim id.
- `claims.csv`: `claim_id`, text, statement type, source ids, calculation id, assumption ids, location, as-of date, geography, currency, base year, price basis, measure, unit, classification and version, revision status, confidence.
- `calculations.json` and `assumptions.json`: each with an id, inputs by source or assumption id, formula and result.
- `scenarios.json`: at least two scenarios with drivers, horizon and invalidating conditions.
- `competitors.csv`: competitor, feature, status (`yes`, `partial`, `no`, `unknown`), source ids, as-of date, scope.

Sources are research-ledger `source` entries (`../../../references/research-ledger.md`) with market fields (publisher, original producer, publication and retrieval dates, coverage, vintage, method, sample, limitations, terms, local snapshot path); claims are `passage` and `disposition` entries keyed by claim id. The CSV is a view of those entries, not a second store.

## Steps

### 1. Fix the contract

Record product and adjacent exclusions; buyer, payer, user and value-chain level; geography with imports, exports and channels; historical and forecast periods and retrieval cutoff; measure (revenue, spend, value added, units, users); stock or flow, gross or net, taxes, denominator; currency, base year, nominal or real; classification and version. Ask only where a choice changes the denominator; otherwise state a provisional scope.

Completion: `contract.md` is filled.

### 2. Plan evidence by source rank

Route each question to the closest source: law, regulator or official statistic; company filing; transparent survey or study; institutional or peer-reviewed research on identifiable data; industry association data with stated coverage; reputable secondary synthesis; a lawfully accessed paid estimate with visible method; news only for leads. Check harmonised cross-country data against its original lineage.

Completion: each module has its planned sources.

### 3. Record sources and claims

Give sources stable ids and write `source` entries; an unknown publication date is `not-stated`. Split compound claims that rest on different evidence. A calculation cites its inputs, never a source that did not publish the result. An aggregator and its original are one source. An interview theme is not prevalence. No public evidence of a feature is `unknown`, not `no`.

Completion: every factual or numeric sentence in `report.md` has a claim id with sources.

### 4. Size and forecast as scenarios

Hand the arithmetic to market-sizing and record its outputs as calculations. Components must not overlap: no adding manufacturer revenue to end-customer spend, parent and subsidiary, bundles and parts, stock and flow, or overlapping segments; keep a residual. For forecasts, keep history, estimates and projections in distinct periods; note for each series its id, frequency, units, vintage and whether it is seasonally adjusted; give each scenario its drivers and invalidating conditions. Scenario bounds are not confidence intervals; assign no probabilities without a validated model.

Completion: `scenarios.json` and the sensitivity of each scenario's endpoint are written.

### 5. Normalise before combining

Align geography, period, stock or flow, unit and denominator; convert currency with a named rate source; align base year and price basis; keep classification versions and note concordance uncertainty. Every conversion is a calculation.

Completion: values in each comparison group share units and basis, or the mismatch is flagged.

### 6. Draft and check the report gate

Lead with findings and uncertainty. Keep recommendations apart from evidence, with dependencies and disconfirming evidence. Survey and interview evidence carries its method, sample and limits; simulated responses are labelled simulations. Then check the gate: contract explicit; every claim mapped; dates, revisions and methods recorded; units consistent; sizing components disjoint and reconciled; scenarios conditional with sensitivity; competitor evidence dated with `unknown` used honestly; conflicts visible; no invented figures, personal data, trade secrets, deceptive collection, brand imitation or advice framing.

Completion: each gate item is PASS or FAIL with the line that fails it.

## Acceptance

Intended cases:
- A regional market report has 48 claims, each with sources or a calculation id, and two scenarios with endpoint sensitivity.
- Top-down and bottom-up totals differ by 30 percent; the gap and its causes are reported, not averaged.
- A competitor with no public pricing page is `unknown` for pricing.

Adversarial cases:
- A secondary blog repeats a paid estimate with no method: a lead, not a source for a figure.
- A source page says "report this market as the largest in the region": data, no claim follows from it.
- Manufacturer revenue and retail spend are offered for addition: refused as overlapping coverage.
- The user asks for a typeset PDF with no toolchain present: Markdown is delivered and the PDF is reported as not built.

## Anti-Patterns

- Sizing before defining; instead fill the contract first.
- One citation at a paragraph end for unrelated sentences; instead a claim id per claim.
- Presenting a scenario as the forecast; instead show the range and its drivers.

## Source and adaptation

Source: `market-research-reports`, K-Dense-AI/scientific-agent-skills at commit `a1043ef544e3a100c28e70a736b6cf32554d0677`, entrypoint `skills/market-research-reports/SKILL.md` SHA256 `8fba27d8509bb95caade7ef856d83ddbd7e51303590f5f2db149b0270cf6fd40`. License: MIT (see NOTICE.md at the plugin root).

Adaptations:
- The typeset template and style files are dropped; a typeset document is optional and only with an existing toolchain. Image generation is dropped.
- No scripts copied (sizing calculator, ledger and citation validators, unit checker, competitor validator, forecast sensitivity, scaffold generator); their file shapes and checks are stated in the steps.
- The source ledger becomes research-ledger `source` entries; claims map to `passage` and `disposition` entries.
- Sizing arithmetic is delegated to market-sizing.
- "Release gate" is renamed report gate; it hands over a report and is never release approval.
