---
name: agent-payment-x402
description: Specify policy-gated agent payments over the x402 HTTP 402 challenge flow, per-task and session budgets, origin, recipient, network and asset allowlists, reservation before any await, fail-closed checks and confirmation before the first paid request, checked offline against challenge fixtures. Use when an agent must pay for an API or service itself. Not for live wallet, signing or settlement work.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Agent Payment Execution (x402)

Specify how an agent pays for a resource under policy. Kept from the source: the 402 challenge negotiation, per-task and per-session budgets, allowlists for origin, recipient, network and asset, reservation before any await, fail-closed behavior when anything is unreachable or unparseable, explicit confirmation before the first paid request, the buyer and seller integration paths, and facilitator choice as the resource server's decision. The skill produces a policy and its offline fixtures; wallet access, SDK installation, signing and settlement each need separately scoped authority.

## When to Activate

- An agent must pay for an API call, a service or another agent's work from its own budget.
- A resource returns HTTP 402 and the user asks how the agent should respond.
- The user asks for spending limits, recipient allowlists or budget enforcement around agent calls.

Do not use for:
- querying a wallet, installing a payment SDK, signing or settling: a separately authorized task with its own owner and budget;
- charging other agents from a service you run: the seller path in step 2 names the dependency, but server middleware setup is a release through the release coordinator;
- general cost tracking of model usage: `agentic-engineering`.

## Inputs and outputs

Required inputs: the approved origins, recipients, networks and assets; the per-task and per-session caps in human units with their atomic scale; the confirmation route to the user; and whether a runtime implementation already exists. When any allowlist or cap is missing, report the gap and produce no policy; an empty allowlist means nothing is acceptable, never everything.

Output: a payment policy written as [policy pseudocode](references/payment-policy.md) with the values filled in, a fixture run result against [the six challenges](references/challenge-fixtures.json) with the expected decision for each, and a list of the runtime tests required once code exists.

## Steps

### 1. Record the payment scope and the confirmation rule

Write the approved origins (exact HTTPS origins), recipients, networks, assets, per-task cap and session cap. Confirmation is asked once before the first paid request, names all of those values in human units, and its answer is shared by concurrent calls; a decline ends every pending paid call with no retry prompt.

Completion: the scope lists every allowlist and cap, and the confirmation text is written out.

### 2. Choose the integration path

Buyer paths: a payment tool server that holds policy set by the orchestrator, or a client wrapper around the agent's HTTP client with a policy that filters the server's challenge. Seller path: protocol middleware on the service with a facilitator chosen by the resource server. Package names, versions, network identifiers, facilitator lists and discovery endpoints from the source are to be verified against the official protocol documentation at implementation time; the policy is set by the orchestrator, never by the agent through a callable tool.

Completion: the path is named with its dependencies marked "to be verified", and policy ownership is the orchestrator's.

### 3. Define challenge validation in order

Before reservation, prompt, fetch or signature: the request origin must be in the origin allowlist, with no credentials in the URL and redirects refused. For each requirement in the challenge: network in the allowlist; asset in the allowlist (EVM addresses compared lowercased, base58 addresses compared exactly); recipient in the allowlist; amount parsed as an integer, non-negative and at most the per-task cap. A requirement failing any check is dropped; when none remain, the client refuses instead of falling back.

Completion: the policy lists the checks in this order and the refusal when the filtered set is empty.

### 4. Define reservation and release

Reserve the per-task cap against the session cap before any await; when the reservation would exceed the session cap, block the call. Release the reservation only when no signed request left the process (declined confirmation, rejected challenge, free response or a transport failure before signing). A sent signed request stays counted whether or not settlement is confirmed.

Completion: the policy states the reserve point, the block condition and the only release conditions.

### 5. Run the fixtures offline

Apply the policy to the six challenges by hand or with a pure function that has no signer, wallet, network or SDK. Expected: one accepted; wrong origin, wrong recipient, wrong network, wrong asset and over-budget amount each rejected before any signature. Record the decision per fixture as Fresh evidence.

Completion: six decisions match the fixtures' `expected_decision`, with the rejected reason matching `expected_reason`.

### 6. List the runtime tests required when code exists

Concurrent calls share one reservation path and one confirmation decision; a declined confirmation attempts no payment; an unreachable payment service or a malformed budget response blocks the action; a non-finite or negative cost is rejected; a redirect on either the challenge or the signed retry is refused; a tool error on setting policy stops delegation. These run only when runtime code exists, against a test double, with no funded account.

Completion: the list names each test, its expected outcome and that it runs with no funded account.

### 7. Hand off implementation under separate authority

Wallet query, SDK installation, a funded request, signing and settlement are each a separately scoped task with its own owner, permission, budget, cleanup and isolated acceptance per `../../references/conventions.md`. The policy and fixtures are the hand-off artifact; this skill performs none of those actions.

Completion: each of the five actions is listed as Proposed with its missing authority named.

## Anti-Patterns

- Comparing the budget against a number the agent supplied; validate the server's challenge values.
- Letting a challenge populate the origin or recipient allowlist; the orchestrator sets them before delegation.
- Checking the budget after an await; reserve first so concurrent calls cannot all pass.
- Falling back to unmetered access when the payment service is unreachable; block the action.
- Claiming a key-custody arrangement is free of custodial risk; name the custody model and its owner instead.
- Copying package versions, network identifiers or facilitator names as current; verify them at implementation time.
- Prompting again after a decline; the shared decision stands for the session.

## Source and adaptation

Source: `agent-payment-x402` from the ECC bundle 2.2.3 (installed local bundle; origin `community`, with a contributor disclosure retained in NOTICE.md). SHA256 of the source entrypoint: `07e9231d4bf62a3fbdead8937d707001ddb4e266328fc769950aecae82c3f1a3`. License: MIT (see NOTICE.md at the plugin root).

- Kept the 402 negotiation, budgets, allowlists, reservation-before-await, fail-closed rules, first-request confirmation and facilitator-as-server-decision as policy steps.
- Removed the "no custodial risk" and "non-custodial" claims; custody is named as a separately owned decision.
- Removed the MCP server registration, package installation, signer construction, token-account provisioning commands and discovery endpoints; package names, versions and facilitator lists are to be verified at implementation time.
- Condensed the TypeScript client example into policy pseudocode in `references/payment-policy.md`.
- Added `references/challenge-fixtures.json` with six challenges (one acceptable; five rejected before any signature) and the expected decisions, using synthetic addresses.
- Required offline or isolated acceptance only, with wallet, SDK, funded request, signing and settlement under separate authority.
