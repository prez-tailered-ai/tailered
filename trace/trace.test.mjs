import test from "node:test";
import assert from "node:assert/strict";
import { TRACE_POINTS, buildTrace } from "./trace.mjs";

const at = (ms) => new Date(Date.UTC(2026, 7, 28, 0, 0, 0, ms)).toISOString();
const spansFor = (points, step = 10) => points.map((point, i) => ({ point, at: at(i * step) }));
const fullSpans = () => spansFor(TRACE_POINTS);

// PROPERTY: the nine trace points are a closed, ordered, frozen allow-list.
// WHY_THIS_TEST: the trace is the only artifact that can show intent reaching a verified result.
//   A point silently dropped from the list is a hop nobody will ever notice was never observed.
// INPUT: TRACE_POINTS itself.
// EXPECTED_RESULT: exactly the nine T0..T8 points, unique, frozen, in order.
// PASS_MEANING: the trace measures the whole path, and cannot be shortened at runtime.
// FAIL_MEANING: a run can be "complete" while a whole leg of the path was never instrumented.
test("TRACE_POINTS is the frozen ordered set of nine", () => {
  assert.ok(Object.isFrozen(TRACE_POINTS));
  assert.deepEqual([...TRACE_POINTS], [
    "T0_INTENT_RECEIVED", "T1_AGENT_CONTEXT_READY", "T2_ACTION_AUTHORIZED",
    "T3_WORKSPACE_COMMAND_ACCEPTED", "T4_RUNTIME_OPERATION_COMPLETE", "T5_BUILD_COMPLETE",
    "T6_PREVIEW_READY", "T7_INTERACTION_COMPLETE", "T8_VERIFICATION_COMPLETE",
  ]);
  assert.throws(() => TRACE_POINTS.push("T9_SHIPPED"));
});

// PROPERTY: a complete trace is complete, and every adjacent duration is measured.
// WHY_THIS_TEST: the happy path must actually work, or `missing` below proves nothing.
// INPUT: nine spans, 10ms apart, in order.
// EXPECTED_RESULT: missing empty, complete true, eight adjacent durations of 10ms each.
// PASS_MEANING: buildTrace can report completeness when completeness is real.
// FAIL_MEANING: the function is stuck reporting incomplete and its `missing` carries no signal.
test("nine present points give a complete trace and eight adjacent durations", () => {
  const trace = buildTrace({ trace_id: "tr-1", spans: fullSpans() });
  assert.equal(trace.trace_id, "tr-1");
  assert.deepEqual(trace.missing, []);
  assert.equal(trace.complete, true);
  assert.equal(Object.keys(trace.durations).length, 8);
  assert.equal(trace.durations["T0_INTENT_RECEIVED->T1_AGENT_CONTEXT_READY"], 10);
  assert.equal(trace.durations["T7_INTERACTION_COMPLETE->T8_VERIFICATION_COMPLETE"], 10);
});

// PROPERTY: a duration is NEVER computed across a missing point.
// WHY_THIS_TEST: this is the whole trap. Zipping the spans that are present pairwise produces a
//   T4->T6 number that looks like a measured latency and is actually a hole with a stopwatch on
//   it -- the missing preview step disappears into a plausible figure.
// INPUT: nine points with T5_BUILD_COMPLETE removed.
// EXPECTED_RESULT: missing names T5; complete false; NO duration key mentions T5 and none
//   bridges T4 to T6; the surviving durations are only the adjacent pairs that are both present.
// PASS_MEANING: a gap is reported as a gap and cannot be spanned by a number.
// FAIL_MEANING: an unobserved leg is presented as a measured one -- a fabricated observation.
test("a missing point is reported and no duration is computed across it", () => {
  const spans = fullSpans().filter((s) => s.point !== "T5_BUILD_COMPLETE");
  const trace = buildTrace({ trace_id: "tr-2", spans });
  assert.deepEqual(trace.missing, ["T5_BUILD_COMPLETE"]);
  assert.equal(trace.complete, false);
  for (const key of Object.keys(trace.durations)) {
    assert.ok(!key.includes("T5_BUILD_COMPLETE"), `duration ${key} names a missing point`);
  }
  assert.equal(trace.durations["T4_RUNTIME_OPERATION_COMPLETE->T6_PREVIEW_READY"], undefined);
  assert.deepEqual(Object.keys(trace.durations), [
    "T0_INTENT_RECEIVED->T1_AGENT_CONTEXT_READY",
    "T1_AGENT_CONTEXT_READY->T2_ACTION_AUTHORIZED",
    "T2_ACTION_AUTHORIZED->T3_WORKSPACE_COMMAND_ACCEPTED",
    "T3_WORKSPACE_COMMAND_ACCEPTED->T4_RUNTIME_OPERATION_COMPLETE",
    "T6_PREVIEW_READY->T7_INTERACTION_COMPLETE",
    "T7_INTERACTION_COMPLETE->T8_VERIFICATION_COMPLETE",
  ]);
});

// PROPERTY: an empty span list is nine missing points, not a complete trace.
// WHY_THIS_TEST: 0 of 0 is the vacuous pass. A run that emitted nothing must not read as one
//   that had nothing to report.
// INPUT: spans: [].
// EXPECTED_RESULT: all nine points missing, complete false, no durations.
// PASS_MEANING: silence is measured as absence.
// FAIL_MEANING: a run that never started is indistinguishable from one that finished.
test("no spans at all is nine missing points, never complete", () => {
  const trace = buildTrace({ trace_id: "tr-3", spans: [] });
  assert.deepEqual(trace.missing, [...TRACE_POINTS]);
  assert.equal(trace.complete, false);
  assert.deepEqual(trace.durations, {});
});

// PROPERTY: the span list is validated as an allow-list; malformed traces are refused, not fixed.
// WHY_THIS_TEST: an unknown point name, a duplicated point, or an unreadable timestamp each make
//   the trace ambiguous. Repairing ambiguity silently is how a wrong number acquires authority.
// INPUT: an unlisted point; a duplicated point; a timestamp that is not a time; a missing point key.
// EXPECTED_RESULT: each throws, naming the offending value.
// PASS_MEANING: only a well-formed trace produces a trace object at all.
// FAIL_MEANING: a garbage span is folded into the durations and reported as an observation.
test("unknown, duplicated and unreadable spans are refused", () => {
  assert.throws(() => buildTrace({ trace_id: "t", spans: [{ point: "T9_SHIPPED", at: at(0) }] }), /T9_SHIPPED/);
  assert.throws(() => buildTrace({ trace_id: "t", spans: [...fullSpans(), { point: "T0_INTENT_RECEIVED", at: at(99) }] }), /T0_INTENT_RECEIVED/);
  assert.throws(() => buildTrace({ trace_id: "t", spans: [{ point: "T0_INTENT_RECEIVED", at: "whenever" }] }), /whenever/);
  assert.throws(() => buildTrace({ trace_id: "t", spans: [{ at: at(0) }] }), /point/);
  assert.throws(() => buildTrace({ trace_id: "t", spans: "T0" }), /spans/);
});

// PROPERTY: time may not run backwards between two adjacent observed points.
// WHY_THIS_TEST: a negative duration is a clock defect or a fabricated span. Averaged into a
//   latency table it silently improves the number it corrupts.
// INPUT: T1 stamped before T0.
// EXPECTED_RESULT: throws naming both points.
// PASS_MEANING: an impossible ordering is refused rather than reported as a small number.
// FAIL_MEANING: a negative latency is published as a measurement.
test("a backwards clock between adjacent points is refused", () => {
  const spans = fullSpans();
  spans[1] = { point: "T1_AGENT_CONTEXT_READY", at: at(0) };
  spans[0] = { point: "T0_INTENT_RECEIVED", at: at(50) };
  assert.throws(() => buildTrace({ trace_id: "t", spans }), /T0_INTENT_RECEIVED->T1_AGENT_CONTEXT_READY/);
});

// PROPERTY: the returned spans are ordered by the canonical point order, not by arrival.
// WHY_THIS_TEST: an emitter that writes spans out of order must not change what the trace says.
// INPUT: the nine spans shuffled, timestamps still consistent with the canonical order.
// EXPECTED_RESULT: same completeness and same durations as the ordered input.
// PASS_MEANING: the trace is a function of the observations, not of their arrival order.
// FAIL_MEANING: two identical runs disagree because of a queue.
test("span arrival order does not change the trace", () => {
  const ordered = buildTrace({ trace_id: "t", spans: fullSpans() });
  const shuffled = buildTrace({ trace_id: "t", spans: [...fullSpans()].reverse() });
  assert.deepEqual(shuffled.durations, ordered.durations);
  assert.deepEqual(shuffled.missing, ordered.missing);
  assert.deepEqual(shuffled.spans.map((s) => s.point), [...TRACE_POINTS]);
});

test("a Date keeps its milliseconds and a bare number string is refused", () => {
  const spans = [{ point: "T0_INTENT_RECEIVED", at: new Date(1000) }, { point: "T1_AGENT_CONTEXT_READY", at: new Date(1250) }];
  assert.equal(buildTrace({ trace_id: "t", spans }).durations["T0_INTENT_RECEIVED->T1_AGENT_CONTEXT_READY"], 250);
  assert.throws(() => buildTrace({ trace_id: "t", spans: [{ point: "T0_INTENT_RECEIVED", at: "0" }] }), /unreadable timestamp/);
  assert.throws(() => buildTrace({ trace_id: "t", spans: [{ point: "T0_INTENT_RECEIVED", at: "2026-01-01 10:00" }] }), /unreadable timestamp/);
});

test("a backwards clock across a missing point is refused", () => {
  const spans = [{ point: "T0_INTENT_RECEIVED", at: 500 }, { point: "T2_ACTION_AUTHORIZED", at: 100 }];
  assert.throws(() => buildTrace({ trace_id: "t", spans }), /T0_INTENT_RECEIVED->T2_ACTION_AUTHORIZED/);
});
