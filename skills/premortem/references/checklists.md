# Premortem checklists and record format

Read by step 2 (checklists) and step 3 (verification and record) of the premortem skill.

## Quick checklist (plans, PRs, localized changes)

1. What is the single biggest thing that could go wrong?
2. Which external dependency could fail, and what happens then?
3. Can this be rolled back if it breaks?
4. Which edge cases have no test?
5. Which unclear requirement could cause rework?
6. What input does the code not expect: a missing parameter, malformed input, an empty body?

## Deep checklist (before implementation)

- Technical: works at 10x and 100x load; external services have fallbacks; data availability, consistency and migrations are clear; latency targets are met; auth, injection and the OWASP Top 10 were considered; every failure mode is handled.
- Integration: breaking changes named; migration path defined; rollback strategy exists; feature flag needed or not.
- Process: requirements complete; stakeholder input gathered; tech debt tracked; upkeep owner named.
- Testing: coverage gaps named; integration test plan; load test needed or not; manual test plan.

## Verification before any tiger

```yaml
suspicion: "<what looked risky>"
verification:
  context_read: true    # 20 lines either side were read
  fallback_check: true  # try/catch, existence check, else branch looked for
  scope_check: true     # the item is in scope for this change
  dev_only_check: true  # not only in tests, scripts or dev-only code
result: tiger | paper_tiger | elephant | false_alarm | unverified
```

Any check `false` or unknown: the result is not `tiger`. A check the target cannot answer makes it `unverified`, not `false_alarm`.

## Record

```yaml
premortem:
  mode: quick | deep
  target: "<plan, PR or files>"
  frame: "It is three months from now and <target> failed. Why?"
  suspicions: ["<pass 1, unfiltered>"]
  tigers:
    - risk: "<what breaks>"
      location: "api.py:42"
      severity: high | medium
      category: security | dependency | data | integration | requirements | testing | scalability
      mitigation_checked: "<the mitigations looked for and not found>"
      suggested_fix: "<smallest fix>"   # deep mode
  paper_tigers:
    - risk: "<looks scary>"
      reason: "<why it is handled>"
      location: "api.py:44-47"          # where the mitigation is
  elephants:
    - risk: "<the unspoken concern>"
      severity: medium | high
  low_risks:                            # smaller real risks, including ones inside handled cases
    - risk: "<what>"
      location: "api.py:44"
  false_alarms:
    - finding: "<initial concern>"
      reason: "<why it is nothing>"
  unverified:
    - suspicion: "<what could not be settled here>"
      settling_check: "<the check, and who can run it>"
  checklist_gaps:                       # deep mode
    - category: "<checklist section>"
      items: ["<item>"]
```

## Severity

| Severity | Blocks? | Required |
|---|---|---|
| high | yes | mitigate, or the owner accepts it explicitly; includes unauthenticated input that can kill the process or corrupt data |
| medium | no | tell the owner; recommend a fix |
| low | no | record it under low_risks |
