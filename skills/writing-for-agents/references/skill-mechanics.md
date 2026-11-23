# Skill mechanics

The skill-specific branch of `writing-for-agents`, read when the document being written is a skill. Everything else about writing it is in the parent skill.

## Frontmatter in this plugin

Every skill in this plugin carries exactly `name`, `description` and `license` (see the plugin manifest and conventions). The description is the skill's top-level context pointer and stays loaded on every turn: it names what the skill does, the trigger branches and one exclusion, in plain text within the plugin's length limit. The pointer-writing rules of the parent skill apply in full.

## Invocation

Two choices, trading the two loads:

- A model-invoked skill keeps a description the agent can act on, so the agent fires it on its own and sibling skills can name it. The human can still type its name. Cost: permanent context load for the description. Shared reference that several skills need can live in one model-invoked skill they all name.
- A user-invoked skill is reachable only by a person typing its name: zero context load, but the person is the index that must remember it. Shared reference that two user-invoked skills both need lives in neither; push it to a plain file outside the skill system that any skill can point at.

The mechanism that marks a skill user-invoked is host-specific. Record the host's own key or setting before relying on it; this plugin's fixed frontmatter keys do not include one, so skills here are model-invoked and their descriptions carry the trigger branches.

Pick model-invocation only when the agent must reach the skill on its own or another skill must. If it only ever fires by hand, make it user-invoked and pay no context load.

## Splitting by invocation

Split off a model-invoked skill when a distinct leading word should trigger it on its own (a word you use in prompts) or another skill must reach it. The new always-loaded description costs context load, so the independent reach has to be worth it. The sequence cut lives in the parent skill.

## Router skills

When user-invoked skills multiply past what a person can remember, one user-invoked router skill names the others and when to reach for each. It can only hint, never fire them.
