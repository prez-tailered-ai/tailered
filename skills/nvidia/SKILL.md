---
name: nvidia
description: "One entry for NVIDIA work, routed to exactly one of 25 NVIDIA-authored specialists: NeMo Relay instrumentation and observability, Nemotron content-safety policies, Dynamo deployment, routing, interconnect and troubleshooting, NeMo AutoModel training, NeMo Fabric, Megatron Bridge memory and resiliency, NeMo Retriever, the RAG Blueprint and its eval and performance tests, cuDF, DALI and Data Designer. Use when a request names one of these NVIDIA products or tasks. Not for Tailered sports models or general GPU questions with no NVIDIA product named."
license: "Apache-2.0 AND CC-BY-4.0"
verified: no
last-run: never
evidence: none
owner: unassigned
test-date: never
---

# NVIDIA

One router over 25 specialists that NVIDIA wrote and signed. Each specialist sits unchanged under `<area>/<name>/`; this file and `scripts/route.mjs` decide which one to load. Reading this file changes nothing and installs nothing.

## When to Activate

| Area | Specialists (folder) | Typical request |
|---|---|---|
| relay | nemo-relay-get-started, -instrument-calls, -instrument-context-isolation, -debug-runtime-integration, -plugin-adaptive-tuning, -plugin-observability; nemotron-policy-generator | instrument or debug NeMo Relay; write a Nemotron safety policy |
| dynamo | dynamo-recipe-runner, -router-starter, -interconnect-check, -troubleshoot | deploy, route, check or fix Dynamo on Kubernetes |
| nemo | nemo-automodel-distributed-training, -recipe-development; nemo-fabric-build-adapter, -integrate; nemo-mbridge-perf-memory-tuning, -resiliency; nemo-retriever, -retriever-mcp | train with AutoModel, adapt or integrate Fabric, tune Megatron Bridge, search with Retriever |
| rag | rag-blueprint, rag-eval, rag-perf | deploy, score or load-test the RAG Blueprint |
| data | accelerated-computing-cudf, dali-dynamic-mode, data-designer | GPU DataFrames, DALI dynamic mode, synthetic data |

Every specialist, its trigger phrases and what it needs: `references/routes.md` (generated from `references/routes.json`).

Do not use for:
- Tailered sports models or odds: `tailered-ai:ai-model-research`, `tailered-ai:ai-model-scrape-odds`;
- general GPU or CUDA questions that name no NVIDIA product here;
- writing or changing a specialist's text: the specialists are signed; changes are new Tailered files beside them, never edits.

## Inputs and outputs

Input: the user's request. Output: one loaded specialist and its work, or one question when the request matches none or two specialists equally. Only the chosen specialist's folder is read.

## Steps

### 1. Route

Run `node scripts/route.mjs "<request>"` from this skill's folder. It prints the specialist's SKILL.md path or `none`.

Completion: one path is chosen, or `none` is returned.

### 2. Settle a miss

On `none`, pick from the area table above when the request clearly fits one row; otherwise ask the user one question naming the two closest specialists.

Completion: exactly one specialist is chosen, by the script, the table or the user's answer.

### 3. Load and follow the specialist

Read that specialist's SKILL.md and follow it, including its own references and scripts, by paths relative to its folder. Check its "needs" (GPU, cluster, packages) before running anything and report what is missing.

Completion: the specialist's own completion conditions are met, or the missing prerequisite is reported.

### 4. Keep the specialists intact

Never edit a file under `<area>/<name>/`. After any change to this skill, run `node scripts/check-signed.mjs` (all 236 files byte-identical) and `node scripts/route.mjs --self-test`.

Completion: both checks print PASS.

## Anti-Patterns

- Loading several specialists "to be safe"; route to one.
- Guessing on a `none`; ask one question.
- Editing a specialist to fix a path or wording; add a Tailered file beside it instead.
- Claiming the NVIDIA signatures verified; `check-signed.mjs` proves byte identity only.

## Source and adaptation

The 25 specialists are NVIDIA-authored skills (Apache-2.0; two also CC-BY-4.0), imported unchanged into the Tailered plugin and moved here on 2026-11-02 from `skills/nvidia-<name>/` with their bytes intact. The SHA256 of every file, with its old and new path, is in `references/signed-sha256.txt`; each folder keeps NVIDIA's `skill.oms.sig`. The router, routes, route script and byte check are original Tailered AI work. License: see NOTICE.md at the plugin root.
