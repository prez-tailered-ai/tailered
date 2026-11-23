# Council archetypes and configurations

Read by step 3 when the default Skeptic, Pragmatist and Critic do not fit the question, and when the user names a configuration word, a domain mix, a custom archetype, scoring or rounds. These are deliberation heuristics for simulated or helper viewpoints, not validated measures of expertise.

## The twelve archetypes

| #   | Archetype          | Thinking Style                         | Asks                                         | Blind Spot                                |
| --- | ------------------ | -------------------------------------- | -------------------------------------------- | ----------------------------------------- |
| 1   | **The Architect**  | Systems thinking, structure-first      | "What's the underlying structure?"           | Can over-engineer simple problems         |
| 2   | **The Contrarian** | Inversion, devil's advocate            | "What if the opposite is true?"              | Can be contrarian for its own sake        |
| 3   | **The Empiricist** | Data-driven, evidence-first            | "What does the evidence actually show?"      | Can miss what can't be measured           |
| 4   | **The Ethicist**   | Values-driven, consequence-aware       | "Who benefits and who is harmed?"            | Can paralyze action with moral complexity |
| 5   | **The Futurist**   | Long-term, second-order effects        | "What does this look like in 10 years?"      | Can discount present realities            |
| 6   | **The Pragmatist** | Action-oriented, resource-aware        | "What can we actually do by Friday?"         | Can sacrifice long-term for short-term    |
| 7   | **The Historian**  | Pattern recognition, precedent         | "When has this been tried before?"           | Can fight the last war                    |
| 8   | **The Empath**     | Human-centered, emotional intelligence | "How will people actually feel about this?"  | Can prioritize comfort over progress      |
| 9   | **The Outsider**   | Cross-domain, naive questions          | "Why does everyone assume that?"             | Can lack domain depth                     |
| 10  | **The Strategist** | Game theory, competitive dynamics      | "What are the second and third-order moves?" | Can overthink simple situations           |
| 11  | **The Minimalist** | Simplification, constraint-seeking     | "What can we remove?"                        | Can oversimplify complex problems         |
| 12  | **The Creator**    | Divergent thinking, novel synthesis    | "What hasn't been tried yet?"                | Can chase novelty over reliability        |

Pick by the domain mixes below; adapt them to the question.

## Configuration words

The user can customize the Council:

- **"Quick council"** or **"fast deliberation"** → Use 3 members, shorter responses
- **"Deep council"** or **"full deliberation"** → independent helper voices (step 3), extended reasoning
- **"Add [archetype]"** → Include a specific archetype
- **"Without [archetype]"** → Exclude a specific archetype
- **"Custom council: [list]"** → User picks exact members
- **"Anonymous council"** → Use neutral labels until synthesis. This is a presentation option; no bias-reduction effect is established for this skill.
- **"Devil's advocate mode"** → Stress-test the intuitive choice with plausible failure cases and label hypothetical premises. Retain facts that survive the challenge.
- **"Rounds mode"** → After initial positions, members respond to each other for a second round

## Domain-Specific Councils

### Startup Decisions
**Members:** Strategist, Pragmatist, Contrarian, Futurist, Empiricist
**Why this mix:** Startups need vision (Futurist) grounded in reality (Pragmatist), challenged by skepticism (Contrarian), backed by data (Empiricist), with competitive awareness (Strategist).
**Key tension to watch:** Futurist vs. Pragmatist — ambition vs. execution capacity.

### Technical Architecture
**Members:** Architect, Minimalist, Empiricist, Outsider, Pragmatist
**Why this mix:** Architecture needs structure (Architect) that's not over-engineered (Minimalist), validated by evidence (Empiricist), challenged by fresh eyes (Outsider), and actually buildable (Pragmatist).
**Key tension to watch:** Architect vs. Minimalist — elegance vs. simplicity.

### Hiring / People Decisions
**Members:** Empath, Strategist, Pragmatist, Ethicist, Historian
**Why this mix:** People decisions need emotional intelligence (Empath), strategic fit (Strategist), practical constraints (Pragmatist), fairness (Ethicist), and pattern recognition (Historian).
**Key tension to watch:** Empath vs. Strategist — caring for the person vs. optimizing for the team.

### Creative Direction
**Members:** Creator, Outsider, Historian, Empiricist, Minimalist
**Why this mix:** Creativity needs divergent thinking (Creator), fresh perspective (Outsider), awareness of what's been done (Historian), audience validation (Empiricist), and restraint (Minimalist).
**Key tension to watch:** Creator vs. Historian — novelty vs. proven patterns.

### Crisis Management
**Members:** Pragmatist, Strategist, Empath, Contrarian, Architect
**Why this mix:** Crisis needs immediate action (Pragmatist), long-term thinking (Strategist), human awareness (Empath), challenge to groupthink (Contrarian), and systemic fix (Architect).
**Key tension to watch:** Pragmatist vs. Architect — quick fix vs. root cause.

### Ethical Dilemmas
**Members:** Ethicist, Contrarian, Empath, Historian, Futurist, Empiricist
**Why this mix (6 members):** Examine values (Ethicist), assumptions (Contrarian), human impact (Empath), precedent (Historian), long-term consequences (Futurist), and evidence (Empiricist).
**Key tension to watch:** Ethicist vs. Futurist — present obligations vs. projected future consequences. Do not treat speculative future benefits as verified facts.

### Investment / Financial Decisions
**Members:** Empiricist, Strategist, Contrarian, Futurist, Pragmatist
**Why this mix:** Money decisions need data (Empiricist), game theory (Strategist), skepticism of hype (Contrarian), trend awareness (Futurist), and execution reality (Pragmatist).
**Key tension to watch:** Futurist vs. Empiricist — future potential vs. present evidence.

## Custom Archetype Creation

Users can define custom archetypes for domain-specific councils. When a user defines a custom member, capture:

1. **Name:** What this archetype is called
2. **Lens:** The primary frame through which they see everything
3. **Signature question:** The one question they always ask
4. **Blind spot:** What they consistently miss
5. **Checks:** Which other lens or assumption this archetype usefully tests

**Example custom archetype:**
```
Name: The Regulator
Lens: Compliance and risk management
Signature question: "What could go wrong legally?"
Blind spot: Can kill innovation with caution
Checks: Whether Creator and Futurist proposals satisfy verified constraints
```

## Scoring the Deliberation

After synthesis, the Council can optionally score the deliberation quality:

| Metric | Scale | What It Measures |
|--------|-------|-----------------|
| Diversity Score | 1-5 | Coverage of distinct relevant lenses (1 = one repeated lens, 5 = multiple relevant assumptions, constraints, and values examined); agreement can score highly |
| Tension Quality | 1-5 | Clarity of genuine trade-offs (1 = obscured, 5 = clearly explained); leave unscored when none exists |
| Blind Spot Discovery | 1-5 | Did the synthesis reveal something no individual member saw? |
| Actionability | 1-5 | How concrete and useful is the recommended path? |
| Overall CQS | 1-5 | Council Quality Score — weighted average only if all four component scores are applicable |

**CQS Formula:** (Diversity × 0.25) + (Tension × 0.30) + (Blind Spot × 0.25) + (Actionability × 0.20)

These scores and weights are optional editorial heuristics, not validated measures of accuracy, expertise, or decision quality. Do not convert CQS or archetype agreement into a probability of correctness.

For example, component ratings of 4, 3, 2, and 5 yield CQS = 3.40. The number is an editing aid, not a passing threshold. If no genuine tension or newly discovered blind spot exists, leave that component and the aggregate unscored instead of inventing one to complete the table. A high score never substitutes for the evidence checks.

## Multi-Round Deliberation

For complex questions, enable "Rounds Mode":

**Round 1:** Initial positions (standard deliberation)
**Round 2:** Each member tests a consequential assumption or unresolved claim from Round 1 against the evidence brief
**Round 3 (optional):** Revise only where a specific new source, corrected inference, or changed constraint warrants it; state that basis
**Final Synthesis:** Incorporates all rounds

Use one additional round by default when a substantive issue remains; stop after at most three total rounds unless the user requests more. Stop earlier when the next round would only restate positions. Preserve unresolved uncertainty instead of seeking unanimity. Extra rounds consume time and context; improved insight or accuracy is not guaranteed. If essential evidence is missing, the next useful step is to obtain it, not to repeat the debate.

## Silent Council Mode

Sometimes the user doesn't need the full deliberation output — they just need the synthesis. In "Silent Council" mode:

1. Apply the same evidence and assumption checks
2. Output the Synthesis section with concise supporting reasons
3. If asked for detail, provide a concise summary of the perspectives, evidence, assumptions, and trade-offs.

This shortens the visible response. It does not establish reduced runtime or independent hidden deliberation; do not promise either.
