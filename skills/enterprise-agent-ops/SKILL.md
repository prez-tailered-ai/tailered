---
name: enterprise-agent-ops
description: Operate a long-lived agent runtime with lifecycle, observability, safety-scope and change controls bound to the actual runtime and to the release coordinator as release owner, keeping planned controls distinct from observed enforcement. Use for restart, stop, rollout, rollback, incident or metrics work on a running agent service. Not for release approval itself, which stays with the release coordinator.
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Enterprise Agent Ops

Operational controls for agent systems that run beyond one session. Kept from the source: the four domains (runtime lifecycle, observability, safety controls, change management), the baseline controls, the five metrics and the six-step incident pattern. Each control is bound to the runtime that actually hosts the service and recorded as planned or observed; a control described in a document is not an enforced one.

## When to Activate

- A running agent service needs start, pause, stop or restart handling.
- The user asks for logs, metrics, traces, a kill switch, a rollout or a rollback of an agent runtime.
- Failures are spiking on a live route and an incident needs a bounded response.

Do not use for:
- approving or executing a release: The release coordinator, per `../../references/conventions.md`;
- one in-session task loop: `continuous-agent-loop`;
- declaring scheduling or dispatch capabilities: `autonomous-agent-harness`;
- a report of what a session did: `checklist-session`.

## Inputs and outputs

Required inputs: the service name, the supervisor that runs it (resolved from the host, not assumed), its route and host, the existing operator, the release record held by the release coordinator, and the explicitly authorized isolated target for any control exercise. When the supervisor, operator or authorized target is unknown, report the gap and exercise nothing.

Output: a controls ledger (control, planned, observed evidence), a metrics table labeled measured, configured or unavailable, and for an incident a record of affected route, existing operator, bounded recovery and the smallest change made.

## Steps

### 1. Bind the runtime

Record service, supervisor, host, route, operator and the release owner. Resolve the supervisor from the host (its unit, process-manager entry or container definition) and read its configuration rather than inferring it from the source's examples.

Completion: the binding names all six fields from inspected configuration.

### 2. Keep a planned-versus-observed ledger

List each baseline control: immutable deployment artifact, least-privilege credentials, environment-level secret injection, hard timeout and retry budgets, audit log for high-risk actions, kill switch. For each, record what is planned and the Fresh or Retained evidence that it is enforced; absence of evidence leaves the observed column empty.

Completion: every control has a planned entry and an observed entry that is evidence or empty.

### 3. Exercise lifecycle controls only on authorized isolated targets

Start, pause, stop and restart are exercised on a target the operator explicitly authorized and that is isolated from the live route. Record the command, exit status and the service state before and after. The live service changes only through a release.

Completion: each exercised control has target, authorization, command, exit status and before-and-after state.

### 4. Bind observability to where the data is

Name the actual log location, metric source and trace store. Report the five metrics (success rate, mean retries per task, time to recovery, cost per successful task, failure class distribution) as measured with the window and source, configured but not yet collected, or unavailable.

Completion: each metric carries one of the three labels and, when measured, its source and window.

### 5. Verify safety scopes

Confirm the credentials the service holds, the scopes it can reach and the kill switch path, by inspecting configuration and one observed denial where safe. A scope listed in a policy document without an observed denial stays planned.

Completion: credentials, scopes and the kill switch each have an observed entry or are marked planned.

### 6. Evidence change management separately

Record four distinct items: the immutable artifact (its hash and build identity), the live identity (what the route serves now, read from the running service), the rollback path (the previous artifact and the tested command to restore it), and the measured outcome after the change. Rollout and rollback are releases coordinated by the release coordinator with the owner's exact word.

Completion: artifact, live identity, rollback and outcome each have their own evidence entry.

### 7. Run the incident pattern within bounds

When failures spike: freeze new rollout; capture representative traces; isolate the failing route and record the affected route, the existing operator and the bounded recovery (limits on attempts, time and effects); patch with the smallest safe change; run regression and security checks; resume gradually. Resuming the live route is a release step.

Completion: the incident record has route, operator, bounded recovery, the change, the check results and the resume decision's owner.

## Anti-Patterns

- Reporting a documented control as enforced; show the observed evidence or leave it planned.
- Restarting the live service to test a control; use the authorized isolated target.
- Treating the deployed artifact's hash as proof of what is live; read the live identity separately.
- Calling a rollback plan tested when its command has never run; exercise it on the isolated target.
- Inventing a success rate or cost figure; label it unavailable.
- Resuming rollout from inside the incident record; hand the resume to the release coordinator.

## Source and adaptation

Source: `enterprise-agent-ops` from the ECC bundle 2.2.3 (installed local bundle). SHA256 of the source entrypoint: `468a10e507520d1fd2f15e5cf326499456206740697fd9462570321996ddfb35`. License: MIT (see NOTICE.md at the plugin root).

- Bound lifecycle, observability and rollback to the runtime resolved from the host and to the release coordinator as release owner, replacing the generic PM2, systemd, container and CI/CD pairing list.
- Added a planned-versus-observed ledger so a listed control is not reported as enforcement.
- Restricted restart, stop and rollout exercises to explicitly authorized isolated targets.
- Required immutable artifact, live identity, rollback and measured outcomes as four separate evidence entries.
- Labeled metrics measured, configured or unavailable and made the incident record name route, operator and bounded recovery.
