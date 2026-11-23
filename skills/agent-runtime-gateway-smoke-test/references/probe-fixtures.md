# Probe fixtures

Sample observations for Steps 4 and 6. Values are placeholders; the project supplies route, identifiers and log format.

## Edge-only observation (not proof of the API)

```text
probe:  GET /gateway/agent/callback  ->  401
local API log (last 60 s, filtered by callback identity):  no entry
```

Reading: the 401 may come from the tunnel edge. The local API was not shown to receive the request. Result for Step 4: FAIL, edge-only.

## Callback-proven observation

```text
probe:  GET /gateway/agent/callback  ->  401
local API log:  2026-10-16T14:02:11Z  GET /gateway/agent/callback  401  req=probe-7f3a
```

Reading: the same request reached the local API and was rejected as unauthenticated by the API itself. Result for Step 4: PASS.

## Task observations

```text
PASS       status=completed   answer="PONG"      expected="PONG"
           local API log: POST /gateway/agent/callback 200 task=t-0192 agent=smoke-isolated
FAIL       status=completed   answer="Pong."     expected="PONG"   (inexact answer)
NOT PASS   status=running     (terminal state not reached within timeout)
NOT PASS   status=queued      (check whether another dispatcher claimed it)
FAIL       status=completed   answer="PONG"      local API log: no entry for task=t-0192
           (answer arrived without a proven callback; the sandbox did not reach the local gateway)
```

## Failure table

| Observation | Next check |
| --- | --- |
| Web page loads but API requests fail | Compare the configured API target with the listening process; restore the original route. |
| Gateway probe gets a connection error or 404 | Check tunnel lifetime with its owner, route path and local API health before dispatching. |
| Gateway probe gets 401 or 403 with no local log entry | Edge-only; verify the callback path before dispatching. |
| Task stays queued or running | Check whether another dispatcher claimed it and whether the sandbox reached the local gateway. |
| Task finishes with the wrong answer | Capture task status and redacted error; the smoke test is FAIL. |
