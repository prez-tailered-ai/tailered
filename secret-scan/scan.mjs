// Patterns are written so the source file itself does not contain a live token.

const TOKEN = "[A-Za-z0-9_-]";

export const SECRET_RULES = Object.freeze([
  { id: "github_pat", source: String.raw`\b(ghp_${TOKEN}{20,}|github_pat_${TOKEN}{20,}|gho_${TOKEN}{20,}|ghs_${TOKEN}{20,}|ghu_${TOKEN}{20,}|ghr_${TOKEN}{20,})\b` },
  { id: "openai_sk", source: String.raw`\bsk-(?:proj-[A-Za-z0-9_-]{16,}|[A-Za-z0-9]{20,})\b` },
  { id: "anthropic_sk", source: String.raw`\bsk-ant-[A-Za-z0-9_-]{20,}\b` },
  { id: "google_api", source: String.raw`\bAIza[0-9A-Za-z_-]{35}(?![0-9A-Za-z_-])` },
  { id: "stripe", source: String.raw`\b[sr]k_(?:live|test)_[A-Za-z0-9]{16,}\b` },
  { id: "jwt", source: String.raw`\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b` },
  { id: "aws_akia", source: String.raw`\bAKIA[0-9A-Z]{16}\b` },
  { id: "notion", source: String.raw`\b(?:ntn_|secret_)[A-Za-z0-9]{16,}\b` },
  { id: "cloudflare_api", source: String.raw`\b(?:CF_API_TOKEN|CLOUDFLARE_API_TOKEN)\s*[:=]\s*\S+` },
  { id: "discord_bot", source: String.raw`\b[A-Za-z0-9_-]{24}\.[A-Za-z0-9_-]{6}\.[A-Za-z0-9_-]{27,}\b` },
  { id: "pem", source: "-----BEGIN [A-Z ]*PRIVATE KEY-----" },
  { id: "onepassword", source: String.raw`\bops_eyJ[A-Za-z0-9._=-]{20,}\b` },
  { id: "railway", source: String.raw`\bRAILWAY_TOKEN\s*[:=]\s*\S+` },
  { id: "slack", source: String.raw`\bxox[baprs]-[A-Za-z0-9-]{10,}\b` },
  { id: "cf_ai_gateway", source: String.raw`\bCF_AI_GATEWAY(?:_API_TOKEN)?\s*[:=]\s*\S+` },
]);

export const SECRET_SHAPE = new RegExp(SECRET_RULES.map((rule) => `(?:${rule.source})`).join("|"));

// Words that mark the surrounding text as an example, and marks that make the token itself a placeholder.
const EXAMPLE_NEARBY = /example|placeholder|redacted/i;
const PLACEHOLDER_TOKEN = /\.{3}|xxx+|your-|<[^>]+>/i;

function fenceSpans(text) {
  const spans = [];
  const fence = /```[\s\S]*?```/g;
  let match;
  while ((match = fence.exec(text))) {
    spans.push([match.index, match.index + match[0].length]);
  }
  return spans;
}

function inSpan(index, spans) {
  return spans.some(([start, end]) => index >= start && index < end);
}

function nearExample(text, index, length) {
  const from = Math.max(0, index - 80);
  const to = Math.min(text.length, index + length + 80);
  return EXAMPLE_NEARBY.test(text.slice(from, to));
}

export function scanSecrets(text) {
  if (typeof text !== "string" || text.length < 1) {
    return { hits: [], live: false, fenced_only: false };
  }
  const spans = fenceSpans(text);
  const hits = [];
  for (const rule of SECRET_RULES) {
    const re = new RegExp(rule.source, "g");
    let match;
    while ((match = re.exec(text))) {
      const fenced = inSpan(match.index, spans) || PLACEHOLDER_TOKEN.test(match[0]) || nearExample(text, match.index, match[0].length);
      hits.push({
        rule_id: rule.id,
        live: !fenced,
        index: match.index,
      });
    }
  }
  const live = hits.some((hit) => hit.live);
  return {
    hits,
    live,
    fenced_only: hits.length > 0 && !live,
  };
}
