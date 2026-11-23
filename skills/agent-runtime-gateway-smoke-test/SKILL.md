---
name: agent-runtime-gateway-smoke-test
description: Verify the path from a remote sandbox through a gateway tunnel to a local agent API with one tool-free task, distinguishing an edge response from a callback proven in local logs, requiring a terminal state with the exact expected answer, then restoring the original route and removing only test-created resources. Use for an end-to-end runtime check. Not for opening or owning the tunnel.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Agent runtime gateway smoke test

Prove that a task dispatched to a remote sandbox calls back to the local agent API through the gateway, without connected tools or private production data, and leave the web app on its original route. Kept from the source: the required inputs, the authorization and cleanup rules, the five-step smoke test, the failure table and the short output contract.

## When to Activate

- A local agent API needs an end-to-end runtime check through the gateway.
- A task stalls after dispatch and the gateway or tunnel may be unreachable.
- An isolated web app is temporarily pointed at a local API for agent testing.
- A previous test left the web app pointing at a stopped API.

Do not use for:
- Opening, owning or authorizing the tunnel; that belongs to the tunnel owner named in the inputs.
- Diagnosing a failing agent run once the path is proven: agent-introspection-debugging.
- Testing connected tools or write actions against a real account; that is a separate test with its own grants.

## Inputs and outputs

Required inputs; when one is missing, report it and stop before any route change, never guess an endpoint, a grant or an account:
- API: repository-relative instructions for starting the local API and the isolated web app, with the health URL.
- Route: the gateway route path and its documented anonymous response.
- Tunnel owner: who holds the tunnel, its provider authorization and its lifetime; the tunnel is already up or is opened by that owner, not by this skill.
- Callback identity: how a callback is recognized in the local API log (request path, task identifier or agent identifier).
- Task: an isolated test agent, a tool-free prompt, its exact expected answer, and the way to read task status.
- Cleanup: the recorded original web-app API target and the command that restores it.
- Credentials through the project's secret store; values never appear in the skill, commands or report.

Output: the short report in Step 7, with evidence labels from `../../references/conventions.md`.

## Steps

### 1. Bind inputs and authorization

Confirm each input above and the authorization to dispatch the test task and to change the route of the isolated web app. Confirm the test agent and data are isolated from real users. A shared production app is out of scope; stop if the only web app is a shared one. Record the limits: one task, the timeout, and who owns a failure.

Completion: every input is present with a value or the skill has stopped with the named gap.

### 2. Record and check the original route

Read the web app's current API target, keep it locally for restoration, and verify it is healthy. Write the cleanup plan before any change: on success, error, timeout, interruption or cancellation, restore the recorded target, verify its health, then stop only processes this test started.

Completion: the original target and its healthy status are recorded, and the cleanup plan names only test-created resources.

### 3. Start the local API and confirm the tunnel

Start the local API with the project's process manager so it stays alive for the whole test; record the process identifiers created. Confirm with the tunnel owner that the tunnel is up and scoped to the required authenticated route. Verify API health with the project's HTTP probe command against the health URL.

Completion: API health returns the documented healthy status; the tunnel is confirmed by its owner, not assumed.

### 4. Probe the gateway and prove the callback in local logs

Probe the gateway route anonymously and record the status code. Then find the matching entry in the local API log using the callback identity. A documented authentication status with no local log entry is an edge-only observation, which may come from the tunnel edge and proves nothing about the API. Sample observations of each kind: [references/probe-fixtures.md](references/probe-fixtures.md).

Completion: the probe status matches the documented anonymous response and the local log shows the matching entry; otherwise the result is FAIL with the edge-only observation recorded.

### 5. Switch the isolated web app

Only after Steps 3 and 4 pass, point the isolated web app at the local API. Verify a request from the web app reaches the local API log. Re-check the route after any web server restart or configuration reload.

Completion: a web-app request appears in the local API log after the switch.

### 6. Run one tool-free task

Dispatch the prompt to the isolated test agent. Wait within the recorded timeout for a terminal state. Check three facts separately: the remote sandbox called the local gateway (local log entry with the callback identity and the task identifier), the task reached a terminal state, and the returned answer equals the exact expected answer. Queued or running is not PASS; a wrong answer is FAIL with the task status and redacted error captured. Use the failure table in [references/probe-fixtures.md](references/probe-fixtures.md) for the next check.

Completion: PASS only when all three facts hold; otherwise FAIL, BLOCKED or INCOMPLETE with the captured status.

### 7. Restore the route, clean up and report

Set the web app back to the recorded target, verify that target and a representative page load, then stop the API processes this test started and nothing else; the tunnel is returned to its owner. If restoration fails, report the broken route immediately and keep the evidence needed to recover. Report: local API healthy (yes or no); gateway probe status with local log confirmation (yes or no); remote callback observed (yes or no); task terminal status and exact-answer match; original route restored and healthy (yes or no); one unresolved blocker or next action when any. Keep account details, credential values, personal paths, public tunnel URLs and raw private logs out of the report.

Completion: the original route is verified healthy and only test-created processes were stopped, or the restoration failure is reported with evidence.

## Anti-Patterns

- Calling an edge status a callback; prove the callback with the local log entry.
- Counting a queued or running task as PASS; wait for the terminal state within the timeout.
- Switching a shared production app; use the isolated app or stop.
- Opening a tunnel or widening its scope from the skill; confirm it with its owner.
- Stopping processes the test did not start; track and stop only test-created identifiers.
- Guessing an endpoint, grant or account when an input is missing; report the gap.

## Source and adaptation

- Source: agent-runtime-gateway-smoke-test, ECC 2.2.3 installed local bundle.
- SHA256: `69c3a3825244aed5b5d3b2de517185f9cf0adfc3db83b128049440a626f2ddbf`
- License: MIT (see NOTICE.md at the plugin root)
- Adaptations:
  - Required inputs are bound explicitly: API, route, tunnel owner, callback identity, task and cleanup; the skill opens no tunnel and treats the tunnel owner as a separate authority.
  - Edge response and local-log-proven callback are separated into distinct completion conditions, with sample observations in `references/probe-fixtures.md`.
  - The task check names three separate facts (callback, terminal state, exact answer); queued or running is explicitly not PASS.
  - Cleanup restores only test-created resources and verifies the original route; the connected-tool follow-up and external skill handoffs were removed from scope.
