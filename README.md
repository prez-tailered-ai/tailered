# Tailered

Tailered AI: sports betting and prediction markets intelligence.

This repository is public. Work is added here after each part is cleared for public release.

## What is here

- `skills/`: 136 top-level agent skills, each in its own folder with a `SKILL.md` (205 `SKILL.md` files in all, counting nested skills). Start at `skills/INDEX.md`. Examples use neutral names (the company, the owner, a partner market).
- `skills/NOTICE.md`: where each adapted skill came from and its license.
- `skills/references/nvidia-import/`: the license texts for the NVIDIA-authored skills under `skills/nvidia/`.
- `secret-scan/`, `redact/`, `trace/`, `snapshot-files/`: small tools, each with tests (`node --test`).
- `CHANGELOG.md`: what shipped, by day, and commits per day since 2026-09-01.

## Skills named here but not included

Some skills refer to sibling skills by name (`tailered-ai:<name>`). These siblings are not published in this repository: `ai-model-capture-health`, `ai-model-capture-odds`, `ai-model-research`, `ai-model-scrape-odds`, `design-craft`, `design-document`, `design-extract`, `design-init`, `design-shape`, `design-teach`, `graphic`, `tailered-labs-browser`, `workflow`. Where a skill hands off to one of them, treat that step as outside this repository.

## License

Tailered AI's own work in this repository is under the MIT License (see `LICENSE`). Skills adapted from other projects keep their original licenses, listed in `skills/NOTICE.md`. The NVIDIA-authored skills under `skills/nvidia/` are under Apache-2.0, two also under CC-BY-4.0 (texts in `skills/references/nvidia-import/`).
