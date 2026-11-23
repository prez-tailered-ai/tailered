import assert from "node:assert/strict";
import { test } from "node:test";
import { sanitizeLog } from "./sanitize.mjs";

test("secret-shaped keys and values are redacted", () => {
  const sanitized = sanitizeLog({
    event: "request_received",
    token: "secret",
    authorization: "Bearer abc",
    note: "ghp_notarealtoken",
  });
  assert.equal(sanitized.event, "request_received");
  assert.equal(sanitized.token, "[redacted]");
  assert.equal(sanitized.authorization, "[redacted]");
  assert.equal(sanitized.note, "[redacted]");
});

test("raw payload keys are redacted", () => {
  const sanitized = sanitizeLog({ payload: { body: "raw" }, delivery_id: "d1" });
  assert.equal(sanitized.payload, "[redacted]");
  assert.equal(sanitized.delivery_id, "d1");
});

test("key names are matched whatever their case", () => {
  const sanitized = sanitizeLog({ Authorization: "Basic dXNlcjpwYXNz", API_KEY: "abc", client_secret: "abc", note: "ok" });
  assert.equal(sanitized.Authorization, "[redacted]");
  assert.equal(sanitized.API_KEY, "[redacted]");
  assert.equal(sanitized.client_secret, "[redacted]");
  assert.equal(sanitized.note, "ok");
});

test("secret-shaped values are redacted under any key", () => {
  const shapes = ["xoxb-1234567890-abcdefghij", `gho_${"a".repeat(24)}`, `sk_live_${"b".repeat(24)}`, `AIza${"c".repeat(35)}`,
    `eyJ${"d".repeat(12)}.${"e".repeat(12)}.${"f".repeat(12)}`, "Basic dXNlcjpwYXNz"];
  for (const shape of shapes) assert.equal(sanitizeLog({ note: shape }).note, "[redacted]", shape.slice(0, 8));
  assert.equal(sanitizeLog({ note: "a basic check of the task-list" }).note, "a basic check of the task-list");
});

test("dates and errors keep their content", () => {
  const sanitized = sanitizeLog({ at: new Date(0), err: new Error("boom") });
  assert.equal(sanitized.at, "1970-01-01T00:00:00.000Z");
  assert.deepEqual(sanitized.err, { name: "Error", message: "boom" });
});

test("ordinary text containing cf- is not redacted", () => {
  assert.equal(sanitizeLog("cf-ray: 8a1b"), "cf-ray: 8a1b");
  assert.equal(sanitizeLog("header cf-ray seen"), "header cf-ray seen");
});
