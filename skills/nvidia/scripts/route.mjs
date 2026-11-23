// Routes a request to one NVIDIA specialist by the trigger phrases in references/routes.json. Prints the specialist's
// SKILL.md path, or "none" when no phrase matches or two specialists tie (then ask which one). Usage:
//   node route.mjs "<request text>"   |   node route.mjs --table (writes references/routes.md)   |   node route.mjs --self-test
import fs from 'node:fs'; import {fileURLToPath} from 'node:url';
const ROOT = fileURLToPath(new URL('..', import.meta.url)), ROUTES = JSON.parse(fs.readFileSync(ROOT + 'references/routes.json', 'utf8'));
export function route(text) {
  const t = text.toLowerCase(), has = k => new RegExp(`(^|[^a-z0-9])${k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}($|[^a-z0-9])`).test(t);   // whole words: 'room' must not match 'oom'
  const scored = Object.entries(ROUTES).map(([p, r]) => [p, r.keys.filter(has).reduce((s, k) => s + k.length, 0)]).filter(([, s]) => s).sort((a, b) => b[1] - a[1]);
  return !scored.length || (scored[1] && scored[1][1] === scored[0][1]) ? 'none' : scored[0][0];
}
const table = () => '# NVIDIA routes\n\nGenerated from `routes.json` by `node scripts/route.mjs --table`; edit the JSON, not this file.\n\n| Specialist | Needs | Trigger phrases |\n|---|---|---|\n' +
  Object.entries(ROUTES).map(([p, r]) => `| [${p}](../${p}/SKILL.md) | ${r.needs} | ${r.keys.join(', ')} |`).join('\n') + '\n';
const arg = process.argv[2];
if (arg === '--table') fs.writeFileSync(ROOT + 'references/routes.md', table());
else if (arg === '--self-test') {   // every specialist reachable by its own first phrase; every path exists; routes.md in sync; negatives route nowhere
  const fails = [];
  for (const [p, r] of Object.entries(ROUTES)) {
    if (!fs.existsSync(`${ROOT}${p}/SKILL.md`)) fails.push(`missing ${p}`);
    if (route(`help me with ${r.keys[0]} please`) !== p) fails.push(`${r.keys[0]} -> ${route(r.keys[0])}, want ${p}`);
  }
  const dirs = fs.readdirSync(ROOT, {withFileTypes: true}).filter(d => d.isDirectory() && !['references', 'scripts'].includes(d.name)).flatMap(a => fs.readdirSync(ROOT + a.name).map(n => `${a.name}/${n}`));
  for (const d of dirs) if (!ROUTES[d]) fails.push(`unrouted folder ${d}`);
  for (const neg of ['write a poem about autumn', 'fix the main product table', 'price the Lakers spread', 'update the release queue', 'zoom call notes', 'a hand-drawn chart']) if (route(neg) !== 'none') fails.push(`negative "${neg}" -> ${route(neg)}`);
  if (fs.readFileSync(ROOT + 'references/routes.md', 'utf8') !== table()) fails.push('routes.md out of sync with routes.json');
  for (const f of fails) console.log('FAIL ' + f);
  console.log(fails.length ? `${fails.length} failures` : `PASS ${Object.keys(ROUTES).length} specialists routed, ${dirs.length} folders mapped, 6 negatives, table in sync`); process.exit(fails.length ? 1 : 0);
} else console.log(route(process.argv.slice(2).join(' ')) === 'none' ? 'none' : `${ROOT}${route(process.argv.slice(2).join(' '))}/SKILL.md`);
