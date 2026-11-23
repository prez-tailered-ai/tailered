#!/usr/bin/env python3
"""Judge a one-league trial. Usage: trial_table.py <trial.json> | --check-copy <dir> [--against <source dir>] | --selftest. Exit 0 decided or copy ok, 2 INCOMPLETE, bad copy or bad input.
Each run has source "ran" or "reported". failures names each failed check; use "unnamed-1" when only a count is known. A winner must beat the baseline by margin_pct (default 5), measured on its slower run. Record a rerun as second_seconds on the baseline and the winner."""
import json, os, sys, tempfile

MIN_SETTINGS = 3

def listing(path):
    out = {}
    for root, _, files in os.walk(path):
        for n in files:
            p = os.path.join(root, n)
            out[os.path.relpath(p, path)] = os.path.getsize(p) if os.path.exists(p) else None  # size through a link, as cp -RL copies it
    return out

def check_copy(path, against=None):
    if os.path.islink(path) or not os.path.isdir(path):
        return [f"{path}: is a link or not a folder"]
    bad = []
    for root, dirs, files in os.walk(path):
        for n in dirs + files:
            p = os.path.join(root, n)
            if os.path.islink(p):
                bad.append(f"link: {p}")
    have = listing(path)
    if not have:
        bad.append(f"{path}: empty")
    if against:
        want = listing(against)
        if not want:
            bad.append(f"{against}: the source is missing or empty, so nothing was compared")
        bad += [f"missing from copy: {k}" for k in want if k not in have]
        bad += [f"size differs: {k}" for k in want if k in have and have[k] != want[k]]
    return bad

def complete(r):
    return isinstance(r.get("seconds"), (int, float)) and r["seconds"] > 0 and isinstance(r.get("checks_passed"), int) \
        and isinstance(r.get("checks_total"), int) and r["checks_total"] > 0 and isinstance(r.get("failures"), list) \
        and r.get("source") in {"ran", "reported"} and len(r["failures"]) >= r["checks_total"] - r["checks_passed"]

def judge(t):
    base, settings = t.get("baseline") or {}, t.get("settings") or []
    margin = t.get("margin_pct", 5)
    missing = []
    if not isinstance(margin, (int, float)) or isinstance(margin, bool) or margin < 0:
        missing.append("margin_pct must be zero or more")
    if not t.get("league"):
        missing.append("league")
    if not complete(base):
        missing.append("baseline: seconds, checks, source, and one failure named per failed check")
    if len(settings) < MIN_SETTINGS:
        missing.append(f"at least {MIN_SETTINGS} settings, got {len(settings)}")
    missing += [f"setting {s.get('name', '?')}: seconds, checks, source, and one failure named per failed check" for s in settings if not complete(s)]
    if missing:
        return {"status": "INCOMPLETE", "missing": missing}
    known = set(base["failures"])
    rows = []
    def worst(r):  # a repeat counts by its slower run, so a repeat that disagrees cannot hide
        return max(r["seconds"], r.get("second_seconds") or 0)
    for s in settings:
        new = sorted(set(s["failures"]) - known)
        worse = s["checks_passed"] < base["checks_passed"] or s["checks_total"] < base["checks_total"]
        ratio = 100 * (worst(s) - base["seconds"]) / base["seconds"]
        if base.get("second_seconds"):
            ratio = max(ratio, 100 * (worst(s) - base["second_seconds"]) / base["second_seconds"])
        rows.append({"name": s["name"], "seconds": s["seconds"], "second_seconds": s.get("second_seconds"), "vs_baseline_pct": round(ratio, 1), "_ratio": ratio, "checks": f"{s['checks_passed']}/{s['checks_total']}", "new_failures": new, "worse_checks": worse, "source": s["source"], "failures": s["failures"]})
    good = [r for r in rows if not r["new_failures"] and not r["worse_checks"] and r["_ratio"] <= -margin]
    win = min(good, key=lambda r: r["seconds"]) if good else None
    repeated = bool(win and win["second_seconds"] and base.get("second_seconds"))
    reported = base["source"] == "reported" or bool(win and win["source"] == "reported")
    count_only = bool(win and any(str(x).startswith("unnamed") for x in list(base["failures"]) + list(win["failures"])))
    for r in rows:
        r.pop("_ratio"); r.pop("failures")
    return {"status": "EXPAND" if win else "STOP", "league": t["league"], "baseline_seconds": base["seconds"], "margin_pct": margin, "winner": win["name"] if win else None,
            "needs_repeat": bool(win and not repeated), "unverified_numbers": reported, "failures_known_by_count_only": count_only,
            "ready_for_next_league": bool(win and repeated and not reported and not count_only), "baseline": {k: base.get(k) for k in ("seconds", "second_seconds", "checks_passed", "checks_total", "failures", "source")}, "settings": rows}

def selftest():
    ok = {"seconds": 40, "checks_passed": 8, "checks_total": 9, "failures": ["E5"], "source": "ran"}
    s = lambda n, sec, f=("E5",), p=8: {"name": n, "seconds": sec, "checks_passed": p, "checks_total": 9, "failures": list(f), "source": "ran"}
    a = judge({"league": "NHL", "baseline": ok, "settings": [s("a", 50), s("b", 30), s("c", 20, ("E5", "new"))]})
    assert a["status"] == "EXPAND" and a["winner"] == "b" and a["needs_repeat"] and not a["unverified_numbers"] and not a["ready_for_next_league"], a
    twice = judge({"league": "NHL", "baseline": {**ok, "second_seconds": 41}, "settings": [{**s("a", 50), "source": "reported"}, {**s("b", 30), "second_seconds": 31}, s("c", 60)]})
    assert twice["ready_for_next_league"] and not twice["needs_repeat"], twice
    half = judge({"league": "NHL", "baseline": ok, "settings": [s("a", 50), {**s("b", 30), "second_seconds": 31}, s("c", 60)]})
    assert half["needs_repeat"], half
    assert judge({"league": "NHL", "baseline": {**ok, "second_seconds": 40}, "settings": [{**s("b", 30), "second_seconds": 45}, s("a", 50), s("c", 60)]})["status"] == "STOP"
    assert judge({"league": "NHL", "margin_pct": -100, "baseline": ok, "settings": [s("a", 70), s("b", 70), s("c", 70)]})["status"] == "INCOMPLETE"
    near = {"seconds": 100, "checks_passed": 8, "checks_total": 9, "failures": ["E5"], "source": "ran"}
    assert judge({"league": "NHL", "baseline": near, "settings": [s("a", 95.04), s("b", 120), s("c", 120)]})["status"] == "STOP"
    cnt = {**ok, "failures": ["unnamed-1"], "second_seconds": 40}
    c = judge({"league": "NHL", "baseline": cnt, "settings": [{**s("b", 30, ("unnamed-1",)), "second_seconds": 30}, s("a", 50), s("c", 50)]})
    assert c["failures_known_by_count_only"] and not c["ready_for_next_league"], c
    assert judge({"league": "NHL", "baseline": ok, "settings": [s("a", 50), s("b", 39.9), s("c", 20, ("E5", "x"), 7)]})["status"] == "STOP"
    assert judge({"league": "NHL", "baseline": ok, "settings": [s("a", 30)]})["status"] == "INCOMPLETE"
    assert judge({"baseline": ok, "settings": [s("a", 1), s("b", 1), s("c", 1)]})["status"] == "INCOMPLETE"
    assert judge({"league": "N", "baseline": ok, "settings": [s("a", 30, ()), s("b", 30), s("c", 30)]})["status"] == "INCOMPLETE"
    assert judge({"league": "N", "baseline": {**ok, "source": "reported"}, "settings": [s("a", 30), s("b", 30), s("c", 30)]})["unverified_numbers"]
    with tempfile.TemporaryDirectory() as d:
        src, cp = os.path.join(d, "src"), os.path.join(d, "cp")
        os.mkdir(src); os.mkdir(cp)
        assert check_copy(cp)
        open(os.path.join(src, "f"), "w").write("xx"); open(os.path.join(cp, "f"), "w").write("xx")
        assert check_copy(cp) == [] and check_copy(cp, src) == []
        assert check_copy(cp, os.path.join(d, "nope"))
        os.symlink(os.path.join(src, "f"), os.path.join(src, "lnk"))
        assert check_copy(cp, src), "a source link missing from the copy must fail"
        os.symlink(os.path.join(cp, "f"), os.path.join(cp, "l"))
        assert any("link" in b for b in check_copy(cp))
        l2 = cp + "-link"; os.symlink(cp, l2)
        assert check_copy(l2)
        os.unlink(l2)
    print("selftest pass")

if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--selftest"]:
        selftest(); sys.exit(0)
    if a[:1] == ["--check-copy"] and len(a) in (2, 4) and (len(a) == 2 or a[2] == "--against"):
        bad = check_copy(a[1], a[3] if len(a) == 4 else None)
        print("ok" if not bad else "FAIL\n" + "\n".join(bad)); sys.exit(2 if bad else 0)
    if len(a) != 1:
        print(__doc__, file=sys.stderr); sys.exit(2)
    try:
        r = judge(json.load(open(a[0])))
    except (OSError, ValueError, AttributeError, TypeError) as e:
        print(f"error: {e}", file=sys.stderr); sys.exit(2)
    print(json.dumps(r, indent=1))
    sys.exit(2 if r["status"] == "INCOMPLETE" else 0)
