# Audit report shape

Produce findings, diagnosis and fix plan in this shape. `evidence` and `uncertainty` are prose; the report has no numeric confidence.

```json
{
  "schema_version": "tailered-ai.agent-architecture-audit.report.v1",
  "executive_verdict": {
    "overall_health": "high_risk | degraded | stable",
    "primary_failure_mode": "string",
    "most_urgent_fix": "string"
  },
  "scope": {
    "target_name": "string",
    "entry_points": ["string"],
    "model_stack": ["configured identifier or unavailable"],
    "symptom": "string",
    "time_window": "string",
    "layers_audited": ["string"],
    "layers_excluded": [{ "layer": "string", "reason": "string" }]
  },
  "findings": [
    {
      "severity": "critical | high | medium | low",
      "title": "string",
      "symptom": "string",
      "mechanism": "string",
      "source_layer": "string",
      "root_cause": "string",
      "evidence_refs": ["file:line or log:row"],
      "evidence_label": "Fresh | Retained",
      "evidence": "what the references show",
      "uncertainty": "what remains unknown and the observation that would settle it",
      "recommended_fix": "string",
      "enforcement": "runtime-enforced | advisory | gap for runtime owner"
    }
  ],
  "hypotheses": [{ "title": "string", "needed_observation": "string" }],
  "ordered_fix_plan": [
    { "order": 1, "goal": "string", "why_now": "string", "expected_effect": "string", "enforcement": "runtime-enforced | advisory" }
  ]
}
```
