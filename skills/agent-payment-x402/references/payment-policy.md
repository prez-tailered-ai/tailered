# Payment policy pseudocode

Condensed from the source's client example. Fill the values from the approved scope; keep the client and its policy private to the orchestrator. Library names and call signatures are to be verified against the official protocol documentation at implementation time.

```
policy:
  allowed_origins     = { exact HTTPS origins set by the orchestrator }
  allowed_networks    = { network identifiers }
  allowed_assets      = { asset identifiers; EVM lowercased, base58 exact }
  allowed_recipients  = { recipient addresses; same normalization as assets }
  per_task_cap        = integer atomic units
  session_cap         = integer atomic units
  session_spent       = 0
  session_decision    = unset            # one shared confirmation for the session

normalize(a): a starts with "0x" ? lowercase(a) : a

check_origin(url):
  u = parse(url)
  require u.origin in allowed_origins and u.username == "" and u.password == ""
  # on failure: refuse before reservation, prompt, fetch or signature

filter_requirements(reqs):            # runs against the SERVER's challenge
  keep r in reqs where
    r.network in allowed_networks
    and normalize(r.asset) in allowed_assets
    and normalize(r.pay_to) in allowed_recipients
    and parse_int(r.amount) succeeds
    and 0 <= parse_int(r.amount) <= per_task_cap
  # empty result = refuse to pay; never fall back to another requirement

pay_once(url, init):
  check_origin(url)
  if session_spent + per_task_cap > session_cap: block "session budget exhausted"
  session_spent += per_task_cap              # reserve BEFORE any await
  signed_sent = false
  try:
    if session_decision is unset:
      session_decision = ask_user(scope summary in human units)   # installed once; concurrent calls await the same promise
    if not await session_decision: block "user declined; no payment attempted"
    response = fetch_with_payment(url, init,
                 transport = tracking_fetch, policy = filter_requirements)
    return response
  finally:
    if not signed_sent: session_spent -= per_task_cap   # release only when nothing signed left the process

tracking_fetch(request):
  request.redirect = "error"                 # applies to the challenge and the signed retry
  check_origin(request.url)
  if request has a payment signature header: signed_sent = true
  response = fetch(request)
  if response.redirected or 300 <= response.status < 400: block "paid request redirects are blocked"
  return response
```

## Required decisions on failure

| Condition | Decision |
| --- | --- |
| payment service unreachable | block the action |
| budget response malformed or non-finite | block the action |
| cost non-finite or negative | block the action |
| setting policy returns an error | do not delegate |
| confirmation declined | end every pending paid call; no re-prompt this session |
