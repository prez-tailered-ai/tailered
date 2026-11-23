// The end-to-end trace: nine points from a human intent to a verified result.
//
//   T0 intent ─► T1 context ─► T2 authorized ─► T3 command ─► T4 runtime
//                                 ─► T5 build ─► T6 preview ─► T7 interaction ─► T8 verified
//
// The whole value of this file is one refusal: a duration is NEVER computed across a missing
// point. Zipping the spans that happen to be present produces a T4->T6 number that reads like a
// measured latency and is really a hole with a stopwatch on it -- the unobserved build step
// vanishes into a plausible figure, and the trace reports "complete" for a path it never saw.
//
// So: durations exist only for ADJACENT pairs in TRACE_POINTS where BOTH points were observed,
// and every point that was not observed is named in `missing`.
export const TRACE_POINTS = Object.freeze([
  "T0_INTENT_RECEIVED", "T1_AGENT_CONTEXT_READY", "T2_ACTION_AUTHORIZED",
  "T3_WORKSPACE_COMMAND_ACCEPTED", "T4_RUNTIME_OPERATION_COMPLETE", "T5_BUILD_COMPLETE",
  "T6_PREVIEW_READY", "T7_INTERACTION_COMPLETE", "T8_VERIFICATION_COMPLETE",
]);

const POINTS = new Set(TRACE_POINTS);

// An unreadable timestamp is refused rather than defaulted: Date.parse("whenever") is NaN and
// NaN arithmetic yields NaN durations that serialize to null and read as "not measured".
const ISO_WITH_ZONE = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:\d{2})$/;

function instant(span) {
  const raw = span.at;
  let ms = NaN;
  if (typeof raw === "number") ms = raw;
  else if (raw instanceof Date) ms = raw.getTime();
  // A bare "0" or a date with no zone parses differently per machine, so only a full ISO time counts.
  else if (typeof raw === "string" && ISO_WITH_ZONE.test(raw)) ms = Date.parse(raw);
  if (!Number.isFinite(ms)) throw new TypeError(`span ${span.point} carries an unreadable timestamp ${JSON.stringify(raw)}`);
  return ms;
}

// -> { trace_id, spans, durations, missing: string[], complete: boolean }
export function buildTrace({ trace_id, spans }) {
  if (!Array.isArray(spans)) throw new TypeError(`spans must be an array, got ${typeof spans}`);
  const observed = new Map();
  for (const span of spans) {
    if (span === null || typeof span !== "object" || typeof span.point !== "string") {
      throw new TypeError(`each span needs a point: ${JSON.stringify(span)}`);
    }
    // Closed set: a point not on the list is refused, never assumed adjacent to one that is.
    if (!POINTS.has(span.point)) throw new TypeError(`unknown trace point ${span.point}`);
    // A duplicate makes the trace ambiguous -- two different times for one hop -- and picking
    // either one is picking an answer.
    if (observed.has(span.point)) throw new TypeError(`trace point ${span.point} observed twice`);
    observed.set(span.point, { ...span, at_ms: instant(span) });
  }
  const missing = TRACE_POINTS.filter((point) => !observed.has(point));
  // Time may not run backwards between any two observed points, even across a missing one.
  const seen = TRACE_POINTS.filter((point) => observed.has(point));
  for (let i = 0; i + 1 < seen.length; i += 1) {
    const delta = observed.get(seen[i + 1]).at_ms - observed.get(seen[i]).at_ms;
    if (delta < 0) throw new TypeError(`${seen[i]}->${seen[i + 1]} runs backwards by ${-delta}ms`);
  }
  const durations = {};
  for (let i = 0; i + 1 < TRACE_POINTS.length; i += 1) {
    const [from, to] = [TRACE_POINTS[i], TRACE_POINTS[i + 1]];
    const a = observed.get(from);
    const b = observed.get(to);
    if (a === undefined || b === undefined) continue;   // the refusal this file exists for
    durations[`${from}->${to}`] = b.at_ms - a.at_ms;
  }
  // Canonical order, so two emitters that queue differently produce the same trace.
  const ordered = TRACE_POINTS.filter((p) => observed.has(p)).map((p) => observed.get(p));
  return { trace_id, spans: ordered, durations, missing, complete: missing.length === 0 };
}
