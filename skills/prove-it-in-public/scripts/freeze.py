#!/usr/bin/env python3
"""Freeze, verify, grade and size a public test. Exit 0 ok, 2 refused, incomplete or bad input.
Usage: freeze.py freeze <plan or one-shot.json> | freeze <slate.json> --plan <plan.json> | canon <file.json> | verify <file.json> <manifest.json>
       grade <file.json> <manifest.json> <results.json> | tally <plan.json> [--missed "<reason>"] <file> <manifest> <results> [more triples] | power <entries> <win_pct> <true_rate> | --selftest
A plan holds the rules, a selection rule and expected_slates. A slate holds plan_sha256 and entries, each with id, start, side and number. A one-shot test puts rules and entries in one file, with no selection.
Results need id, outcome and evidence (the close or score it was graded from). tally recomputes everything from the frozen files and results; it never trusts a saved count.
The hash is the sha256 of the canonical bytes from `canon`: publish those bytes so anyone can reproduce it. A manifest is local: only the publicly posted hash proves when."""
import datetime as dt, hashlib, json, math, sys

RULES = ("claim", "metric", "benchmark", "min_entries", "ends", "win_if", "win_pct")
OUTCOMES = {"win", "loss", "push", "void"}

def canon_bytes(doc):
    return json.dumps(doc, sort_keys=True, separators=(",", ":")).encode()

def sha(doc):
    return hashlib.sha256(canon_bytes(doc)).hexdigest()

def parse(s):
    t = dt.datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    if t.tzinfo is None:
        raise ValueError("needs a timezone")
    return t

def end_of(ends):
    d = dt.date.fromisoformat(str(ends)[:10])
    return dt.datetime(d.year, d.month, d.day, 23, 59, 59, tzinfo=dt.timezone.utc) + dt.timedelta(hours=12)  # a night game on the last day can start after midnight UTC

def check_rules(d):
    p = [f"missing {k}" for k in RULES if d.get(k) in (None, "")]
    if p:
        return p
    if not isinstance(d["min_entries"], int) or d["min_entries"] < 1:
        p.append("min_entries must be a positive whole number")
    if not (isinstance(d["win_pct"], (int, float)) and 0 < d["win_pct"] < 1):
        p.append("win_pct must be a fraction between 0 and 1")
    try:
        end_of(d["ends"])
    except ValueError:
        p.append("ends must be a date, YYYY-MM-DD")
    return p

def freeze(d, now, plan=None):
    entries = d.get("entries") or []
    is_slate = bool(d.get("plan_sha256"))
    problems = []
    if is_slate:
        if plan is None:
            return {"status": "REFUSED", "problems": ["a slate needs --plan, so a wrong plan hash is caught while it can still be fixed"]}
        if sha(plan) != d["plan_sha256"]:
            return {"status": "REFUSED", "problems": ["plan_sha256 does not match that plan"]}
        if not entries:
            problems.append("a slate needs entries")
    else:
        problems += check_rules(d)
        if entries and d.get("selection"):
            problems.append("a file with entries is a one-shot test and takes no selection rule; split it into a plan and slates")
        if not entries and not d.get("selection"):
            problems.append("a plan with no entries needs a selection rule")
        if not entries and not (isinstance(d.get("expected_slates"), int) and d["expected_slates"] > 0):
            problems.append("a plan needs expected_slates, so a losing night cannot be dropped")
        if entries and not problems and len(entries) < d["min_entries"]:
            problems.append("fewer entries than min_entries; use a plan and slates, or more entries")
    if problems:
        return {"status": "REFUSED", "problems": problems}
    ids = [e.get("id") for e in entries]
    if None in ids or len(set(ids)) != len(ids):
        return {"status": "REFUSED", "problems": ["every entry needs its own id"]}
    limit = end_of((plan or d)["ends"]) if entries else None
    starts = []
    for e in entries:
        try:
            t = parse(e.get("start", ""))
        except ValueError:
            return {"status": "REFUSED", "problems": [f"{e['id']}: bad start"]}
        if t <= now:
            problems.append(f"{e['id']}: already started")
        if t > limit:
            problems.append(f"{e['id']}: starts after the test ends")
        if not e.get("side") or e.get("number") in (None, ""):
            problems.append(f"{e['id']}: needs side and number; a hash over an empty prediction proves nothing")
        starts.append(t)
    if problems:
        return {"status": "REFUSED", "problems": problems}
    rehearsal = bool(d.get("rehearsal") or (plan or {}).get("rehearsal"))
    if is_slate and bool(plan.get("rehearsal")) != bool(d.get("rehearsal")):
        return {"status": "REFUSED", "problems": ["a slate's rehearsal mark must match its plan"]}
    return {"status": "FROZEN", "kind": "slate" if is_slate else "one-shot" if entries else "plan", "sha256": sha(d), "frozen_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "entries": len(ids),
            "first_start": min(starts).strftime("%Y-%m-%dT%H:%M:%SZ") if starts else None, "plan_sha256": d.get("plan_sha256"), "rehearsal": rehearsal,
            "note": "REHEARSAL: test ids; do not post this hash" if rehearsal else "the owner posts this hash and publishes the canonical bytes before the first start; a local timestamp alone proves nothing to a skeptic"}

def grade(d, manifest, results):
    if manifest.get("status") != "FROZEN" or sha(d) != manifest.get("sha256"):
        return {"status": "REFUSED", "problems": ["not the file that was frozen"]}
    try:
        frozen = parse(manifest.get("frozen_at"))
        late = [e["id"] for e in d.get("entries", []) if parse(e["start"]) <= frozen]
    except (ValueError, KeyError):
        return {"status": "REFUSED", "problems": ["manifest or entry has a bad time"]}
    if late:
        return {"status": "REFUSED", "problems": [f"{i}: started before the freeze" for i in late]}
    by, problems = {}, []
    for r in results:
        if r.get("outcome") not in OUTCOMES:
            problems.append(f"{r.get('id')}: outcome")
        if not r.get("evidence"):
            problems.append(f"{r.get('id')}: needs evidence, the close or score it was graded from")
        if r.get("outcome") == "void" and not r.get("reason"):
            problems.append(f"{r.get('id')}: a void needs a reason")
        if r.get("id") in by:
            problems.append(f"{r.get('id')}: result given twice")
        by[r.get("id")] = r
    ids = [e["id"] for e in d.get("entries", [])]
    problems += [f"{i}: no result" for i in ids if i not in by]
    problems += [f"{i}: not a frozen entry" for i in by if i not in ids]
    if not ids:
        problems.append("nothing to grade: this file has no entries")
    if problems:
        return {"status": "INCOMPLETE", "problems": problems}
    c = {k: sum(by[i]["outcome"] == k for i in ids) for k in OUTCOMES}
    return {"status": "GRADED", "sha256": manifest["sha256"], "plan_sha256": d.get("plan_sha256"), "rehearsal": bool(manifest.get("rehearsal")), **c,
            "games": [{"id": i, "outcome": by[i]["outcome"], "evidence": by[i]["evidence"], "reason": by[i].get("reason")} for i in ids]}

def tally(plan, triples, missed_reason=None):
    p = check_rules(plan)
    if p:
        return {"status": "REFUSED", "problems": p}
    graded = []
    for d, m, r in triples:
        g = grade(d, m, r)
        if g["status"] != "GRADED":
            return {"status": g["status"], "problems": g["problems"]}
        graded.append(g)
    if not graded or len({g["sha256"] for g in graded}) != len(graded):
        return {"status": "REFUSED", "problems": ["at least one file, and each slate counted once"]}
    if plan.get("selection"):
        if any(g["plan_sha256"] != sha(plan) for g in graded):
            return {"status": "REFUSED", "problems": ["a slate was frozen against a different plan"]}
    elif len(graded) != 1 or graded[0]["sha256"] != sha(plan):
        return {"status": "REFUSED", "problems": ["a one-shot test tallies only its own file"]}
    games = [x for g in graded for x in g["games"]]
    ids = [x["id"] for x in games]
    if len(set(ids)) != len(ids):
        return {"status": "REFUSED", "problems": ["a game appears in two slates"]}
    missed = max((plan.get("expected_slates") or len(graded)) - len(graded), 0)
    if missed and not missed_reason:
        return {"status": "REFUSED", "problems": [f"{missed} expected slate(s) missing: pass --missed with the reason, so the night is reported, never silently left out"]}
    c = {k: sum(x["outcome"] == k for x in games) for k in OUTCOMES}
    decided = c["win"] + c["loss"]
    rate = c["win"] / decided if decided else None
    enough = decided >= plan["min_entries"]
    rehearsal = bool(plan.get("rehearsal"))
    verdict = "TOO_FEW" if not enough else "WIN" if rate >= plan["win_pct"] else "LOSS"
    return {"status": "TALLIED", **c, "decided": decided, "win_rate": None if rate is None else round(rate, 4), "win_pct": plan["win_pct"], "min_entries": plan["min_entries"],
            "may_say_record": enough and not missed and not rehearsal, "verdict": verdict, "rehearsal": rehearsal, "missed_slates": missed, "missed_reason": missed_reason,
            "plan_sha256": sha(plan), "slates": [g["sha256"] for g in graded], "games": games}

def power(n, win_pct, true_rate):
    if n < 1 or not 0 < true_rate < 1 or not 0 < win_pct < 1:
        raise ValueError("entries must be positive; win_pct and true_rate are fractions")
    need = math.ceil(n * win_pct - 1e-9)
    lg = lambda k: math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1) + k * math.log(true_rate) + (n - k) * math.log(1 - true_rate)
    chance = sum(math.exp(lg(k)) for k in range(need, n + 1))
    return {"entries": n, "wins_needed": need, "true_rate": true_rate, "chance_of_passing": round(min(chance, 1.0), 4)}

def selftest():
    now = dt.datetime(2026, 11, 5, tzinfo=dt.timezone.utc)
    e = lambda i, st="2026-11-06T00:00:00Z", side="A", num=1.5: {"id": i, "start": st, "side": side, "number": num}
    rules = {"claim": "c", "metric": "m", "benchmark": "closing line", "min_entries": 2, "ends": "2026-12-01", "win_if": "w", "win_pct": 0.5}
    one = dict(rules, entries=[e("1"), e("2", "2026-11-07T00:00:00Z")])
    m1 = freeze(one, now)
    assert m1["status"] == "FROZEN" and m1["kind"] == "one-shot" and m1["first_start"] == "2026-11-06T00:00:00Z", m1
    assert hashlib.sha256(canon_bytes(one)).hexdigest() == m1["sha256"]
    r = lambda **k: dict(one, **k)
    for bad in (r(entries=[e("1", "2026-11-04T00:00:00Z"), e("2")]), r(win_if=""), r(win_pct=1.5), r(entries=[e("1", "2026-11-06T00:00:00"), e("2")]), r(entries=[e("1"), e("1")]),
                r(entries=[e("1", side=""), e("2")]), r(entries=[e("1", num=""), e("2")]), r(entries=[e("1")]), r(ends="banana"), r(selection="x"), r(entries=[e("1"), e("2", "2027-06-01T00:00:00Z")])):
        assert freeze(bad, now)["status"] == "REFUSED", bad
    assert freeze(rules, now)["status"] == "REFUSED"
    assert freeze(dict(rules, selection="x"), now)["status"] == "REFUSED"
    plan = dict(rules, selection="every NBA game", expected_slates=1)
    pm = freeze(plan, now)
    assert pm["kind"] == "plan" and pm["entries"] == 0, pm
    sl = {"plan_sha256": sha(plan), "entries": [e("1"), e("2")]}
    assert freeze(sl, now)["status"] == "REFUSED"
    assert freeze({**sl, "plan_sha256": "deadbeef"}, now, plan)["status"] == "REFUSED"
    assert freeze({**sl, "entries": [e("1", "2027-06-01T00:00:00Z")]}, now, plan)["status"] == "REFUSED"
    sm = freeze(sl, now, plan)
    assert sm["kind"] == "slate", sm
    res = lambda i, o, **k: {"id": i, "outcome": o, "evidence": "close -3", **k}
    win = [res("1", "win"), res("2", "loss")]
    g = grade(sl, sm, win)
    assert g["status"] == "GRADED" and g["win"] == 1 and g["games"][0]["evidence"], g
    for bad in (win[:1], win + [res("9", "win")], win + [res("2", "win")], [win[0], res("2", "void")], [win[0], {"id": "2", "outcome": "loss"}]):
        assert grade(sl, sm, bad)["status"] == "INCOMPLETE", bad
    assert grade({**sl, "plan_sha256": "x"}, sm, win)["status"] == "REFUSED"
    assert grade(sl, {"sha256": sm["sha256"]}, win)["status"] == "REFUSED"
    assert grade(sl, {**sm, "frozen_at": "2026-11-08T00:00:00Z"}, win)["status"] == "REFUSED"
    t = tally(plan, [(sl, sm, win)])
    assert t["verdict"] == "WIN" and t["may_say_record"] and t["decided"] == 2 and len(t["games"]) == 2, t
    assert tally(plan, [(sl, sm, win), (sl, sm, win)])["status"] == "REFUSED"
    assert tally(dict(plan, claim="other"), [(sl, sm, win)])["status"] == "REFUSED"
    p2 = dict(plan, expected_slates=2)
    s2 = {"plan_sha256": sha(p2), "entries": sl["entries"]}
    m2 = freeze(s2, now, p2)
    assert tally(p2, [(s2, m2, win)])["status"] == "REFUSED"
    mt = tally(p2, [(s2, m2, win)], "froze late on 11/06")
    assert mt["status"] == "TALLIED" and mt["missed_slates"] == 1 and not mt["may_say_record"] and mt["missed_reason"], mt
    assert tally(plan, [(sl, sm, [win[0], res("2", "void", reason="postponed")])])["verdict"] == "TOO_FEW"
    assert tally(one, [(one, m1, win)])["verdict"] == "WIN"
    assert tally(one, [(sl, sm, win)])["status"] == "REFUSED"
    pl = dict(plan, win_pct=0.6); s6 = {"plan_sha256": sha(pl), "entries": sl["entries"]}
    assert tally(pl, [(s6, freeze(s6, now, pl), win)])["verdict"] == "LOSS"
    rp = dict(plan, rehearsal=True); rs = {"plan_sha256": sha(rp), "entries": sl["entries"], "rehearsal": True}
    assert freeze({"plan_sha256": sha(rp), "entries": sl["entries"]}, now, rp)["status"] == "REFUSED"
    rm = freeze(rs, now, rp)
    assert "do not post" in rm["note"]
    rt = tally(rp, [(rs, rm, win)])
    assert rt["rehearsal"] and not rt["may_say_record"], rt
    pw = power(100, 0.62, 0.55)
    assert pw["wins_needed"] == 62 and 0.05 < pw["chance_of_passing"] < 0.14, pw
    assert power(100, 0.55, 0.55)["wins_needed"] == 55
    assert 0 <= power(1230, 0.55, 0.54)["chance_of_passing"] <= 1
    print("selftest pass")

if __name__ == "__main__":
    a = sys.argv[1:]
    load = lambda p: json.load(open(p))
    def out(r, ok):
        print(json.dumps(r, indent=1)); sys.exit(0 if r["status"] == ok else 2)
    now = dt.datetime.now(dt.timezone.utc)
    try:
        if a == ["--selftest"]:
            selftest(); sys.exit(0)
        if len(a) == 2 and a[0] == "freeze":
            out(freeze(load(a[1]), now), "FROZEN")
        if len(a) == 4 and a[0] == "freeze" and a[2] == "--plan":
            out(freeze(load(a[1]), now, load(a[3])), "FROZEN")
        if len(a) == 2 and a[0] == "canon":
            sys.stdout.buffer.write(canon_bytes(load(a[1]))); sys.exit(0)
        if len(a) == 3 and a[0] == "verify":
            same = sha(load(a[1])) == load(a[2]).get("sha256")
            print("ok" if same else "FAIL file changed since the freeze"); sys.exit(0 if same else 2)
        if len(a) == 4 and a[0] == "grade":
            out(grade(load(a[1]), load(a[2]), load(a[3])), "GRADED")
        if len(a) >= 2 and a[0] == "tally":
            rest, reason = a[2:], None
            if rest[:1] == ["--missed"]:
                reason, rest = rest[1], rest[2:]
            if rest and len(rest) % 3 == 0:
                out(tally(load(a[1]), [(load(rest[i]), load(rest[i + 1]), load(rest[i + 2])) for i in range(0, len(rest), 3)], reason), "TALLIED")
        if len(a) == 4 and a[0] == "power":
            print(json.dumps(power(int(a[1]), float(a[2]), float(a[3])), indent=1)); sys.exit(0)
    except (OSError, ValueError, AttributeError, TypeError, KeyError, IndexError) as e:
        print(f"error: {e}", file=sys.stderr); sys.exit(2)
    print(__doc__, file=sys.stderr); sys.exit(2)
