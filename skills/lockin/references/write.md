# Write: plans, skills and agent docs

Source: superpowers 7.0.1 `writing-plans` and `writing-skills` (MIT, Copyright (c) 2025 Jesse Vincent), adapted for lockin. Source SKILL.md SHA256: writing-plans `a6c67c1900064347c2a329990dd3c555657c51c3ec53b259a08aa01a2c26139a`; writing-skills `8cb3ac68c6d8c4bb46886b998b09af7989643cab8bd0e46ee86dd62e64546bbe`.

Pick the branch, then follow only that section.

| You are writing | Branch | Go to |
|---|---|---|
| A step-by-step implementation plan from a spec or requirements, before touching code | plan | [Plan](#plan) |
| A new skill, or an edit to an existing skill | skill | [Skill](#skill) |
| An AGENTS.md, CLAUDE.md, pointer, reference file, completion criteria or handoff packet | agent-doc | [Agent doc](#agent-doc) |

Completion: one branch is named, and only that section is read.

## Plan

Write the plan for an engineer who has not seen this codebase or this spec. They write good code once they know the exact interface and the exact test. What they cannot know is what you decided: which files, which names and signatures, which values from the spec, which tests prove each task. Write those decisions down. Keep tasks small, avoid repetition, build only what the spec needs, test first, and commit often. Say at the start: "I'm using lockin write (plan) to create the implementation plan."

Save to `docs/superpowers/plans/YYYY-MM-DD-<name>.md`. A location the owner names overrides this default.

### 1. Scope check

If the spec covers several independent subsystems, suggest one plan per subsystem. Each plan must produce working, testable software on its own.

Completion: the plan covers one subsystem, or the split into separate plans is proposed in writing.

### 2. File structure

Before tasks, list the files to create or change and what each is responsible for. Give each file one clear job and a clear interface. Prefer small focused files. Keep files that change together in one place; split by responsibility, not by technical layer. In an existing codebase, follow its patterns; split an unwieldy file only when you are already changing it.

Completion: every file the tasks touch appears in the list with one stated responsibility.

### 3. Right-size the tasks

A task is the smallest unit that has its own test cycle and deserves its own reviewer. Fold setup, configuration, scaffolding and docs into the task that needs them. Split only where a reviewer could reject one task and approve its neighbor. Each task ends with something testable on its own.

Completion: each task has an independently testable deliverable, and no two tasks must be approved or rejected together.

### 4. Write the header

Every plan starts with this header:

```markdown
# [Feature Name] Implementation Plan

> **For agentic workers:** Execute natively under lockin lock, or with fresh subagents per task; then lockin verify (gates) and a lockin review of the whole change. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** [One sentence: what this builds]

**Architecture:** [2-3 sentences about the approach]

**Tech Stack:** [Key technologies and libraries]

**Spec:** [Path to the spec or design doc. Executors read both.]

## Global Constraints

[The spec's project-wide requirements (version floors, dependency limits, naming and copy rules, platform needs), one line each, with exact values copied from the spec. Every task includes these.]

## Review Focus

[Five input classes or failure modes the spec implies but no task's tests cover, most likely to bite a user first. One line each: the input or condition, and what a reasonable person expects. Then add the test for each line to the task that owns the code.]

---
```

Completion: the header has all six parts; Global Constraints values match the spec verbatim; Review Focus lists five items, or says none after a real check.

### 5. Write each task

````markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

**Interfaces:**
- Consumes: [what this task uses from earlier tasks, with exact signatures]
- Produces: [what later tasks rely on: exact function names, parameter and return types]

- [ ] **Step 1: Write the failing test**

```python
def test_specific_behavior():
    result = function(input)
    assert result == expected
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/path/test.py::test_name -v`
Expected: FAIL with "function not defined"

- [ ] **Step 3: Implement `function(input: InputType) -> ResultType` in `exact/path/to/file.py`**

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/path/test.py::test_name -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/path/test.py src/path/file.py
git commit -m "feat: add specific feature"
```
````

The implementer sees only their own task, so the Interfaces block is how they learn the names and types of neighboring tasks. Each step is one action with a checkable result: write the failing test, run it and see it fail, implement the minimum, run it and see it pass, commit.

Completion: every task has Files, Interfaces and checkbox steps, and every step is one action with a checkable result.

### 6. Say what each step contains

A step is done when the implementer can write exactly one reasonable thing from it.

- Test step: the test's name and assertions as code, using the spec's exact values.
- Code step: the exact signature (name, parameters, return type), the file, and the values the spec pins. The implementer writes the body. Include a body only for an algorithm the signature and tests do not determine, or for exact copy the spec fixes. Add one line on approach when a real choice is left (library call, data structure).
- Verification step: the command and the output that means it passed.
- Reference to another task: point to that task's Interfaces block; do not repeat its code.

A plan is the set of decisions the implementer cannot make alone. A plan longer than the code it describes has written the code instead. Lines that decide nothing ("TBD", "handle edge cases", "add appropriate validation", "write tests for the above", a type no task defines) are the opposite failure.

Completion: no step contains "TBD" or similar filler, and no code body appears where the signature and tests already decide it.

### 7. Self-review (five points)

Run this yourself; it is not a subagent dispatch. Compare the plan to the spec with fresh eyes.

1. Spec coverage: point to a task for every requirement; list gaps.
2. Step scan: each step allows exactly one reasonable implementation and carries no more than that.
3. Type consistency: names, signatures and properties in later tasks match earlier ones (`clearLayers()` in Task 3 must not become `clearFullLayers()` in Task 7).
4. Review Focus: each listed input class has a test in the task that owns the code.
5. Proportion: a plan several times longer than its spec is a transcript. If code blocks are most of the document, replace bodies with signatures, test names and assertions.

Fix problems inline; do not re-review. Add a task for any spec requirement with no task.

Completion: all five checks are recorded as passed or fixed, and every spec requirement maps to a task.

### 8. Save and hand off

Save the plan, then link it for the owner and ask for review. If the owner already named an execution method, ask only whether the plan captures what he wants and wait for the answer. If not, offer two ways and recommend one, with a one-sentence reason (how much tasks depend on each other's interfaces, how many there are, what a shipped mistake would cost):

- Execute natively under lockin lock, or with fresh subagents per task; then lockin verify (gates) and a lockin review of the whole change.

Completion: the plan file exists at the saved path, the link is given, and no implementation starts before the owner's reply.

## Skill

Writing a skill is test-driven development for process documentation. Run a pressure scenario with a subagent, watch it fail without the skill (RED), write the skill for those failures (GREEN), then close loopholes (REFACTOR). If you did not watch an agent fail without the skill, you do not know the skill teaches the right thing. Skills are reusable techniques, patterns and references; they are not stories about how you solved one problem. Do not make a skill for a one-off fix, a standard practice documented elsewhere, a project-only convention (use the project's instruction file), or a rule a regex or validator can enforce.

Iron law: no skill, and no edit to a skill, without a failing baseline first. Skill written before the baseline? Delete it and start over. "Simple addition", "just a docs update" and "I'll test later" are not exceptions.

### 1. Classify the skill and the failure

Pick the type: technique (steps), pattern (way of thinking), or reference (docs). Pick how you will test it:

| Type | Test with | Passes when |
|---|---|---|
| Discipline (rules) | Questions on the rules, plus pressure scenarios with 3 or more pressures combined (time, sunk cost, authority, exhaustion) | Agent follows the rule under maximum pressure |
| Technique | A new application scenario, variations, gaps in the instructions | Agent applies the technique to a new case |
| Pattern | Recognition, application and counter-example scenarios | Agent knows when the pattern applies and when not |
| Reference | Retrieval and application scenarios, coverage of common uses | Agent finds and uses the right information |

Then classify the baseline failure, because the form that fixes one failure backfires on another:

| Baseline failure | Right form | Wrong form |
|---|---|---|
| Breaks a rule under pressure | Prohibition, rationalization table, red flags | Soft words ("prefer", "consider") |
| Complies, but output has the wrong shape | A positive recipe: what the output is, its parts, in order | A list of "don't" |
| Leaves out a required element | A REQUIRED slot in the template they fill in | Prose reminders near the template |
| Behavior depends on a condition | A condition on something observable | A flat rule with exemption clauses |

Add no "unless it matters" clauses; state a real exception as its own condition.

Completion: the skill's type, the test kind and the baseline failure class are written down.

### 2. RED: baseline without the skill

Run the scenarios with a subagent that does not have the skill. Record the choices it made, its excuses word for word, and which pressures triggered the violation. Methods, pressure types and a worked campaign: [testing-skills-with-subagents.md](write/testing-skills-with-subagents.md) and [CLAUDE_MD_TESTING.md](write/CLAUDE_MD_TESTING.md). For behavior-shaping wording, also micro-test: one fresh sample per call, a no-guidance control (if the control does not fail, stop; there is nothing to fix), five or more repeats, and read every flagged match by hand.

Completion: a baseline record exists with verbatim excuses, and the no-guidance control either failed or the work stopped.

### 3. GREEN: write the minimal skill in the company format

Address only the failures you saw. Use this house format:

- Frontmatter: `name` (letters, numbers, hyphens), `description`, `license`. Description is third person, under 1024 characters (aim under 500), and says when to use the skill, never what it does or its steps. A workflow summary in the description makes agents follow the summary and skip the body. Good: "Use when executing implementation plans with independent tasks." Bad: "Use when executing plans; dispatches a subagent per task with review between tasks."
- `## When to Activate`: the triggers, then "Not for ...; use tailered-ai:<x>" for each near neighbor.
- `## Inputs and outputs`: what the skill needs and what it produces.
- `## Steps`: each step ends with a `Completion:` line an agent can check.
- `## Anti-Patterns`.
- `## Source and adaptation`: where it came from, the source SHA256, the license, and what you changed.

New skills live in `skills/<name>/` and must pass `node skills/workflow/scripts/check-skills.mjs` and `python3 -I tools/check-helper-calls.py`. Heavy reference (100+ lines) and reusable tools go in separate files; keep principles and short patterns inline. Call bundled scripts through their interpreter (`node scripts/x.js`, `bash scripts/x.sh`), never by bare path. One good runnable example beats five weak ones, in one language. Point to other skills by name (`tailered-ai:<name>`), never with an `@` file link, which loads the file at once.

Completion: the skill has all six house parts, the description contains only triggers, both checks pass, and agents comply when the scenarios are rerun with the skill.

### 4. Make it findable

Read [discovery.md](write/discovery.md) when you write or change the name, description or size. Short rules: name it verb-first or by its core insight (`condition-based-waiting`, not `async-test-helpers`); put error messages, symptoms, synonyms and tool names in the text agents will search; describe the problem, not one language's symptom. Keep frequently loaded skills lean (under about 200 words for always-loaded, under 500 for others); move flag lists to `--help`, point to other skills instead of repeating them, and compress examples. Check with `wc -w`.

Completion: name, description and keywords follow discovery.md, and the word count is within the target for how often the skill loads.

### 5. REFACTOR: close loopholes

When a baseline failure is a discipline failure, read [bulletproofing.md](write/bulletproofing.md) and [persuasion-principles.md](write/persuasion-principles.md). Forbid the specific workarounds, not only the rule. State that breaking the letter of a rule breaks its spirit. Build a rationalization table (Excuse, Reality) from every excuse you recorded, and a red-flags list the agent can self-check against. Rerun the scenarios after each change until the agent complies and finds no new excuse.

Completion: every recorded excuse has a counter, a red-flags list exists, and the last full rerun produced no new rationalization.

### 6. Flowcharts, examples and the stop rule

Use a flowchart only for a non-obvious decision, a loop where you might stop too early, or an "A or B" choice. Use tables for reference, code blocks for code, numbered lists for linear steps, and never use labels like `step1`. Rules and rendering: [flowcharts.md](write/flowcharts.md), [graphviz-conventions.dot](write/graphviz-conventions.dot), `node references/write/render-graphs.js <skill-dir>`. Official authoring guidance: [anthropic-best-practices.md](write/anthropic-best-practices.md).

Finish each skill before starting the next. Do not write several skills and test them in a batch. Run tests through `tailered-ai:skill-creator`'s eval loop.

Completion: each flowchart answers a real decision; the skill passed its eval loop; no other skill was started until this one did.

## Agent doc

Use `tailered-ai:writing-for-agents` for instruction files (AGENTS.md, CLAUDE.md), context pointers, reference files an agent reaches by pointer, step completion criteria, and handoff packets (including `/handoff-fable`). It stays a separate skill in this release. If the document is a skill, do the Skill branch above first for testing and house format, then use writing-for-agents for its pointers and wording.

Completion: `tailered-ai:writing-for-agents` is loaded and its fixture check is recorded for the document.
