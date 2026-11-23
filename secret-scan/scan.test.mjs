import assert from "node:assert/strict";
import { test } from "node:test";
import { scanSecrets, SECRET_SHAPE } from "./scan.mjs";

const openai = `sk-${"a".repeat(24)}`;
const openaiProj = `sk-proj-${"a".repeat(8)}-${"b".repeat(16)}`;
const github = `ghp_${"b".repeat(24)}`;
const stripe = `sk_live_${"c".repeat(24)}`;
const notion = `ntn_${"d".repeat(24)}`;
const slack = "xoxb-1234567890-abcdefghij";
const pem = "-----BEGIN PRIVATE KEY-----\nMII\n-----END PRIVATE KEY-----";

test("live unfenced hits reject", () => {
  for (const sample of [openai, openaiProj, github, stripe, notion, slack, pem]) {
    const result = scanSecrets(`token ${sample} in prose`);
    assert.equal(result.live, true, sample.slice(0, 12));
  }
  assert.equal(SECRET_SHAPE.test(`leak ${openai}`), true);
});

test("fenced and example hits are not live", () => {
  const fenced = scanSecrets("```\n" + openai + "\n```");
  assert.equal(fenced.live, false);
  assert.equal(fenced.fenced_only, true);

  const example = scanSecrets(`use the example ${openai} placeholder`);
  assert.equal(example.live, false);
  assert.equal(example.fenced_only, true);
});

test("clean text has no hits", () => {
  const result = scanSecrets("we decided CI Verify stays comment-only");
  assert.equal(result.hits.length, 0);
  assert.equal(result.live, false);
});

test("CF_AI_GATEWAY assignment is a hit", () => {
  const result = scanSecrets("CF_AI_GATEWAY_API_TOKEN=abc");
  assert.equal(result.live, true);
  assert.equal(result.hits[0].rule_id, "cf_ai_gateway");
});

test("anthropic and google api keys are secret-shaped", () => {
  const anthropic = scanSecrets("key sk-ant-api03-" + "A".repeat(24) + " here");
  assert.ok(anthropic.hits.some((h) => h.rule_id === "anthropic_sk"));
  const google = scanSecrets("k=AIza" + "B".repeat(35));
  assert.ok(google.hits.some((h) => h.rule_id === "google_api"));
});

test("more shapes: dash-terminated google key, ghu_/ghr_ tokens, stripe rk_, DSA key block", () => {
  const id = (text) => scanSecrets(text).hits.map((h) => h.rule_id);
  assert.ok(id("k=AIza" + "B".repeat(34) + "- ").includes("google_api"));
  assert.ok(id("t=ghu_" + "C".repeat(24)).includes("github_pat"));
  assert.ok(id("t=ghr_" + "C".repeat(24)).includes("github_pat"));
  assert.ok(id("k=rk_live_" + "d".repeat(24)).includes("stripe"));
  assert.ok(id("-----BEGIN DSA PRIVATE KEY-----").includes("pem"));
});

test("a token is still live inside single backticks or near unrelated marks", () => {
  for (const text of ["run `" + github + "` now", "wait... " + github, "line<br>" + github, "use your-own name with " + github]) {
    assert.equal(scanSecrets(text).live, true, text.slice(0, 16));
  }
});

test("a token that is itself a placeholder is not live", () => {
  assert.equal(scanSecrets("CF_API_TOKEN=<token>").live, false);
  assert.equal(scanSecrets("RAILWAY_TOKEN=your-token").live, false);
});
