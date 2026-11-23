// Key names that always hold a secret. Compared in lower case, so Authorization and API_KEY match.
const SECRET_KEYS = new Set([
  "token", "secret", "password", "credential", "apikey", "api_key", "authorization",
  "accesstoken", "access_token", "refreshtoken", "refresh_token", "clientsecret",
  "client_secret", "payload",
]);

// Value shapes that are a secret wherever they appear.
const SECRETISH = /(?:^|[^A-Za-z0-9])(?:ghp_|gho_|ghs_|ghu_|ghr_|github_pat_|ntn_|sk-|sk_live_|sk_test_|rk_live_|rk_test_|xox[baprs]-|AKIA|AIza|Bearer )/i;
const JWT = /\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]+\./;
const BASIC = /\bBasic [A-Za-z0-9+/]{8,}={0,2}/;

const isSecretText = (text) => SECRETISH.test(text) || JWT.test(text) || BASIC.test(text);

function isPlainObject(value) {
  const proto = Object.getPrototypeOf(value);
  return proto === Object.prototype || proto === null;
}

export function sanitizeLog(value) {
  if (Array.isArray(value)) return value.map((item) => sanitizeLog(item));
  if (typeof value === "string") return isSecretText(value) ? "[redacted]" : value;
  if (value === null || typeof value !== "object") return value;
  // A Date or an Error is a value, not a bag of keys: keep what a log needs from it.
  if (value instanceof Date) return Number.isNaN(value.getTime()) ? "Invalid Date" : value.toISOString();
  if (value instanceof Error) return { name: value.name, message: sanitizeLog(value.message) };
  if (!isPlainObject(value)) return sanitizeLog(String(value));
  const out = {};
  for (const [key, item] of Object.entries(value)) {
    out[key] = SECRET_KEYS.has(key.toLowerCase()) ? "[redacted]" : sanitizeLog(item);
  }
  return out;
}
