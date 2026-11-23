#!/usr/bin/env python3
"""Compare labeled variant folders, ignoring league names and dates. Usage: chassis_diff.py label=dir label=dir ... | --selftest. Exit 0 ok, 2 bad input.
Kinds: shared, near (at least 80 percent the same), different, only_one. An only_one file with a similar file under another name lists it in possible_twins."""
import difflib, json, os, re, sys, tempfile

LEAGUE = r"(?:nfl|nba|nhl|ncaaf|ncaam|mlb)"
TOKENS = re.compile(rf"(?<![A-Za-z0-9]){LEAGUE}(?![A-Za-z0-9])", re.I)
NAME_DATE = re.compile(r"(?<!\d)(?:20\d\d-?\d\d-?\d\d|\d{4})(?!\d)")
BODY_DATE = re.compile(r"(?<!\d)20\d\d-?\d\d-?\d\d(?!\d)")
SKIP = {"node_modules", ".git", "__pycache__", ".venv", "out"}
EXT = (".py", ".mjs", ".js", ".cjs", ".sh", ".ts", ".sql", ".yaml", ".yml", ".toml")
NEAR, TWIN = 0.8, 0.6

def norm_name(s):
    return NAME_DATE.sub("<date>", TOKENS.sub("<league>", s))

def norm_body(s):
    return BODY_DATE.sub("<date>", TOKENS.sub("<league>", s))

def files(root):
    found, skipped = {}, 0
    for base, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for n in names:
            p = os.path.join(base, n)
            if n.endswith(EXT):
                found.setdefault(norm_name(os.path.relpath(p, root)), []).append(p)
            else:
                skipped += 1
    out = {}
    for key, paths in found.items():
        if len(paths) == 1:
            out[key] = paths[0]
        else:  # two files in one variant normalize alike, such as nhl/ and nfl/: keep both, keyed by their real path with dates masked
            for p in paths:
                out[NAME_DATE.sub("<date>", os.path.relpath(p, root))] = p
    return out, skipped

def lines(p):
    with open(p, errors="ignore") as f:
        return [norm_body(l.rstrip()) for l in f if l.strip()]

def ratio(a, b):
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()

def compare(variants):
    tree, skipped = {}, {}
    for k, v in variants.items():
        tree[k], skipped[k] = files(v)
    names = sorted(set().union(*[set(t) for t in tree.values()]))
    groups = []
    for n in names:
        have = {k: t[n] for k, t in tree.items() if n in t}
        body = {k: lines(p) for k, p in have.items()}
        first = next(iter(body))
        ratios = [ratio(body[first], b) for k, b in body.items() if k != first]
        worst = min(ratios) if ratios else None
        kind = "only_one" if len(have) == 1 else "shared" if worst == 1 else "near" if worst >= NEAR else "different"
        groups.append({"file": n, "kind": kind, "similarity": None if worst is None else round(worst, 3), "lines": {k: len(b) for k, b in body.items()}, "missing_in": sorted(set(variants) - set(have)), "paths": have})
    singles = [g for g in groups if g["kind"] == "only_one"]
    for g in singles:
        k, p = next(iter(g["paths"].items()))
        mine, twins = lines(p), []
        for o in singles:
            ok, op = next(iter(o["paths"].items()))
            if o is not g and mine:
                r = ratio(mine, lines(op))
                if r >= TWIN:
                    twins.append({"file": o["file"], "variant": ok, "similarity": round(r, 3)})
        if twins:
            g["possible_twins"] = sorted(twins, key=lambda t: -t["similarity"])[:3]
    counts = {}
    for g in groups:
        counts[g["kind"]] = counts.get(g["kind"], 0) + 1
    return {"variants": variants, "file_groups": len(groups), "counts": counts, "skipped_other_file_types": skipped, "extensions_read": list(EXT), "groups": sorted(groups, key=lambda g: (g["kind"] == "only_one", -(g["similarity"] or 0)))}

def selftest():
    with tempfile.TemporaryDirectory() as d:
        a, b = os.path.join(d, "a"), os.path.join(d, "b")
        os.makedirs(a); os.makedirs(b)
        w = lambda r, n, t: (os.makedirs(os.path.dirname(os.path.join(r, n)), exist_ok=True), open(os.path.join(r, n), "w").write(t))
        w(a, "publish-mlb-0704.mjs", "const league='mlb'\nconst day='20260704'\nrun()\n")
        w(b, "publish-nba-0705.mjs", "const league='nba'\nconst day='20260705'\nrun()\n")
        body = "".join(f"line {i}\n" for i in range(20))
        w(a, "ladder.py", body); w(b, "ladder.py", body + "extra\n")
        w(a, "x.py", "alpha\nbeta\n"); w(b, "x.py", "gamma\ndelta\n")
        w(a, "only.py", "x\n")
        w(a, "limit.py", "limit=1000\n"); w(b, "limit.py", "limit=2000\n")
        w(a, "nhl/check.py", "one\n"); w(a, "nfl/check.py", "two\n"); w(b, "nhl/check.py", "one\n"); w(b, "nfl/check.py", "two\n")
        w(a, "slate_runner.py", body + "s\n"); w(b, "run_v2.py", body + "t\n")
        w(a, "notes.bak", "x\n")
        r = compare({"a": a, "b": b})
        k = {g["file"]: g for g in r["groups"]}
        assert k["publish-<league>-<date>.mjs"]["kind"] == "shared", k
        assert k["ladder.py"]["kind"] == "near", k
        assert k["x.py"]["kind"] == "different", k
        assert k["only.py"]["kind"] == "only_one" and k["only.py"]["missing_in"] == ["b"], k
        assert k["limit.py"]["similarity"] == 0, k["limit.py"]
        assert k["nhl/check.py"]["kind"] == "shared" and k["nfl/check.py"]["kind"] == "shared", list(k)
        assert k["slate_runner.py"]["possible_twins"][0]["file"] == "run_v2.py", k["slate_runner.py"]
        assert r["skipped_other_file_types"] == {"a": 1, "b": 0}, r["skipped_other_file_types"]
    print("selftest pass")

if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--selftest"]:
        selftest(); sys.exit(0)
    pairs = dict(x.split("=", 1) for x in a if "=" in x)
    if len(pairs) < 2 or len(pairs) != len(a):
        print(__doc__, file=sys.stderr); sys.exit(2)
    bad = [v for v in pairs.values() if not os.path.isdir(v)]
    if bad:
        print("not a folder: " + ", ".join(bad), file=sys.stderr); sys.exit(2)
    r = compare(pairs)
    if not r["file_groups"]:
        print("no script files found in any variant", file=sys.stderr); sys.exit(2)
    print(json.dumps(r, indent=1))
