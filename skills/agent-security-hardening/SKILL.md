---
name: agent-security-hardening
description: "Harden the boundaries where an agent turns untrusted content into file, network, memory or tool actions: trust map, identifier and URL validation, filesystem containment, temporary data and credentials, bounded tool output, then a verification gate at the real entry point. Use when building or reviewing an agent runtime, tool gateway or memory service. Not for ordinary web application security."
license: MIT
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# Agent security hardening

Produce concrete controls and executed tests for the agent framework under review, at the exact boundary where untrusted data becomes a side effect. Kept from the source: model output, retrieved content, tool output, memory and cross-agent messages are untrusted; integrations default to read-only with each write granted separately; validation runs at the action boundary even after upstream checks; the action fails closed when identity, destination, ownership or containment cannot be proven; irreversible actions need operation-and-resource authorization plus confirmation or a valid scoped pre-approval.

## When to Activate

- Building an autonomous agent, tool gateway, memory service or agent-to-agent protocol.
- Reviewing code that maps model output into commands, paths, URLs, credentials or API mutations.
- Isolating tenants, projects, sessions or workspaces in a long-running agent process.
- Hardening temporary files, logs, tool responses or external-content ingestion.

Do not use for:
- Ordinary application authentication, authorization, injection, XSS, CSRF or API security: the repository's own security review process.
- Designing the tool set itself: agent-harness-construction.
- Host, container, firewall or cloud hardening: the owning platform's guidance.
- Penetration testing, exploit development or unauthorized access.

## Inputs and outputs

Required inputs; when one is missing, report the gap, mark the dependent check BLOCKED, and never substitute a plausible value:
- The framework and its real entry point (the code path a caller actually hits), by path.
- The governing requirement that defines hard bounds (maximum sizes, identifier length and character set, allowed URL schemes) and the deployment configuration that may tighten them. When neither defines a bound, record it as a required decision and test that the implementation rejects an unbounded configuration.
- The test runner, resolved from the repository.
- The owner who accepts the hardening result (Ownership in `../../references/conventions.md`).

Output: controls in the framework's code, tests that run through the real entry point, and a gate report giving the command, exit status, rejected input and observed absence of the side effect for each gate item, with evidence labels from `../../references/conventions.md`.

## Steps

### 1. Map trust boundaries

List every boundary as `source -> parser -> validator -> side effect`, covering direct user input, model output, retrieved documents, memory, environment variables, tool results and messages from other agents. For each side effect record the identity and scope authorizing it, the validator that runs immediately before it, the maximum input and output size, the audit evidence produced and the recovery path if the operation is interrupted.

Completion: every write, command, network mutation and credential use has exactly one named authorization boundary.

### 2. Validate identifiers, environment values and URLs

Allowlist identifiers that become filenames, keys, selectors or command arguments. Length is capped at the bound defined by the governing requirement; deployment configuration may choose a stricter positive limit and cannot raise it. Pass identifiers that become CLI arguments through an argv API after the end-of-options marker where supported; character validation does not replace argument separation. Reject missing and whitespace-only environment values before constructing a client. Parse URLs, allow only the schemes the deployment requires, require a host, reject embedded credentials, block private-network destinations when the URL is attacker-controlled, verify the connected peer address on every hop, attach credentials only over HTTPS with certificate verification, and strip credentials on any scheme or origin change. Short examples: [references/validators.md](references/validators.md).

Completion: tests reject empty, oversized, malformed, traversal-shaped, credential-bearing and unauthorized-destination values before any side effect, and show that DNS rebinding and cross-origin redirects carry no credential to an unapproved peer.

### 3. Contain filesystem access

Reject absolute user-controlled paths and `..` components before joining. Reject non-portable components on every platform: reserved device names (with or without an extension), names ending in a dot or space, and `:` in a component. Resolve the workspace and the candidate, then prove the candidate is inside the workspace by component, not by string prefix. For sensitive writes, open relative to a trusted directory handle where the platform supports it, reject symlink targets, create exclusively, and verify ownership and permissions after opening.

Completion: tests cover sibling-prefix paths, nested `..`, absolute paths, symlink escapes, reserved device names, trailing dots or spaces, alternate-data-stream syntax and one valid nested workspace path.

### 4. Protect temporary data and credentials

Create sensitive files owner-only and private directories owner-only; prefer a user-private runtime directory over a shared temporary directory; create unpredictable names atomically; remove temporary data in a `finally` path while keeping a redacted error record when cleanup fails; keep secrets out of command arguments, model context, logs, traces, exception text and tool responses; pass secrets through the platform's secret store or scoped environment injection and rotate exposed credentials; treat zeroization as best effort.

Completion: file-mode checks, forced-error cleanup tests and log-capture tests with a sentinel secret show the sentinel absent from every emitted channel and the temporary data removed.

### 5. Bound and sanitize tool output

Read tool output with a byte limit. Preserve structured fields, remove disallowed control characters, append an explicit truncation marker with the original byte count, and keep a content hash when later comparison matters. Malformed output returns a typed failure naming the producing tool, boundary and validation reason without echoing sensitive content; it never becomes an empty success value.

Completion: oversized output, invalid encoding, terminal-control sequences, malformed structured data and a normal response each have a deterministic test.

### 6. Run the verification gate at the real entry point

Verify through the framework's actual entry point: untrusted instructions remain data and trigger no tool or write; an irreversible action without authorization plus confirmation or scoped pre-approval leaves no side effect; cross-tenant and cross-workspace identifiers are rejected at the action boundary; traversal and symlink attempts leave the filesystem unchanged; forced failures leave no credential-bearing temporary file or log; oversized or malformed tool output returns an explicit bounded error. Report each item with the command, exit status, rejected input and the observed absence of the side effect. Label mock-only results as proving the mocked path only: they are not operating-system permission, symlink, subprocess-isolation or network-egress proof.

Completion: all six items have Fresh evidence through the real entry point, or are marked FAIL, BLOCKED or INCOMPLETE with the reason; the result is a hardening report, not a release approval.

## Anti-Patterns

- An invariant that lives only in the prompt; move it into code immediately before the side effect and test a violating model response.
- String-prefix path checks that confuse `/work/app` with `/work/application`; resolve and compare by component, then test symlinks separately.
- Redacting after logging; redact before values reach the logger, tracer, exception or model context, and assert the sentinel is absent.
- Inventing a size or length limit; take it from the governing requirement, or record a required decision and reject the unbounded configuration.
- Calling a mock-only pass isolation proof; label it as the mocked path and run the real-entry-point gate.

## Source and adaptation

- Source: agent-security-hardening, ECC 2.2.3 installed local bundle.
- SHA256: `0e0895ada90aa8fa085e4257961ebe15f2dff43b843785b1533d4c731186ad81`
- License: MIT (see NOTICE.md at the plugin root)
- Adaptations:
  - The issue-specific identifier constant was replaced with "the bound defined by the governing requirement"; a missing bound is a required decision, never an invented value.
  - Python examples shortened and moved to `references/validators.md`; the steps state the behavior the tests must show.
  - Added required inputs (entry point, governing requirement, resolved test runner, owner) and the shared evidence labels; the gate report distinguishes Fresh results from mock-only results.
  - Verification gate output is a hardening report, kept separate from release authority.
  - Sibling and tool handoffs replaced with the repository's own security review and the owning platform's guidance; no external skills listed.
