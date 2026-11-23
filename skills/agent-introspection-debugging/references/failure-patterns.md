# Failure patterns

| Pattern | Likely cause | Discriminating check |
| --- | --- | --- |
| Maximum tool calls, same command repeated | loop or no-exit observer path | list the last N tool calls and count exact repeats |
| Context overflow, degraded reasoning | unbounded notes, repeated plans, oversized logs | measure recent context for duplicated or low-signal bulk |
| Connection refused or timeout | service unavailable or wrong port | probe the service health, URL and port actually configured |
| Rate limit or quota exhaustion | retry storm or missing backoff | count repeated calls and inspect retry spacing |
| File missing after write, stale diff | race, wrong working directory, branch drift | check path, working directory, branch and actual file presence |
| Tests still failing after a fix | wrong hypothesis | isolate the one failing test and re-derive the bug from its output |

## Capture template

```markdown
## Failure capture
- Session / task:
- Goal in progress:
- Original error (verbatim, never overwritten):
- Last successful step:
- Last failed tool / command:
- Repeated pattern seen:
- Environment assumptions to verify:
- Attempts so far / limit:
```

## Recovery record

```markdown
## Recovery action
- Pattern and hypothesis:
- Discriminating check and its result:
- Smallest action taken (through which tool):
- Why this is safe:
- Evidence that proves it worked, or reason it stopped:
```
