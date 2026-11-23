# Failure patterns and diagnostic questions

## Patterns

1. Wrapper regression. The base model answers correctly; wrapper layers degrade it. Signs: correct in a direct call, wrong in the agent; degradation after a new prompt layer; confident but wrong; "it worked before the last update".
2. Memory contamination. Old topics enter through history, memory retrieval or distillation. Signs: unrelated past topics; user corrections do not stick; same-session artifacts return as facts; memory grows without bound.
3. Tool discipline failure. Tools are declared in the prompt and not enforced in code. Signs: required tool skipped; results look right but no call executed; tools compete for one responsibility.
4. Rendering or transport corruption. The internal answer is correct; delivery mutates it. Signs: logs correct, user output broken; markdown, JSON or streaming fragments corrupt a valid response; output differs between terminal and UI.
5. Hidden agent layers. Repair, retry, summarization or recall passes run without a contract. Signs: output changes between generation and delivery; an auto-fix pass the user does not see; several agents modify one output without coordination.

## What to search for in the audited layers

- Tool requirements expressed only in prompt or markdown text.
- Tool call handling with no validation of the executed result.
- Model calls outside the main agent loop (completion, chat or invoke calls in helpers).
- Memory admission paths without user-correction priority.
- Fallback, retry-with-model, repair-prompt or re-prompt paths.
- Response rewriting, transforming or shaping before delivery.

## Quick diagnostic questions

| # | Question | If yes |
|---|----------|--------|
| 1 | Can the model skip a required tool and still answer? | Tool not code-gated |
| 2 | Does old conversation content appear in new turns? | Memory contamination |
| 3 | Is the same information in system prompt, memory and history? | Context duplication |
| 4 | Does the platform run a second model pass before delivery? | Hidden repair loop |
| 5 | Does output differ between internal generation and delivery? | Rendering corruption |
| 6 | Are "must use tool X" rules only in prompt text? | Tool discipline failure |
| 7 | Can the agent's own monologue become persistent memory? | Memory poisoning |
