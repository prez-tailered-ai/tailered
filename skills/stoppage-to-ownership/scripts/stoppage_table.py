#!/usr/bin/env python3
"""Total stoppages per supplier and check the review is complete. Usage: stoppage_table.py <stoppages.json> | --selftest. Exit 0 complete, 2 INCOMPLETE or bad input.
COMPLETE means every source was accounted for and every decision is filled in. It does not mean the decision is right."""
import json, sys

CHOICES = {"own", "backup", "accept"}
SOURCES = ("service_logs", "build_receipts", "queue_records", "release_packets", "alert_messages")

def judge(spec):
    problems, totals = [], {}
    stops, decisions, suspected, sources = spec.get("stoppages"), spec.get("decisions"), spec.get("suspected"), spec.get("sources")
    if not isinstance(stops, list) or not isinstance(decisions, list) or not isinstance(suspected, list) or not isinstance(sources, dict):
        return {"status": "INCOMPLETE", "problems": ["stoppages, decisions and suspected must be lists, empty if none, and sources a map"]}
    for k in SOURCES:
        if not str(sources.get(k, "")).startswith(("searched", "unavailable")):
            problems.append(f"source {k}: mark searched or unavailable")
    for s in suspected:
        if not s.get("why_unproven") or not s.get("date"):
            problems.append(f"suspected {s.get('supplier', '?')}: needs date and why_unproven")
    for s in stops:
        tag = f"{s.get('supplier', '?')} {s.get('date', '?')}"
        if not s.get("supplier") or not s.get("date") or not s.get("evidence"):
            problems.append(f"{tag}: needs supplier, date and evidence")
        if not isinstance(s.get("hours"), (int, float)) or s["hours"] < 0:
            problems.append(f"{tag}: needs hours")
            continue
        t = totals.setdefault(s.get("supplier"), {"supplier": s.get("supplier"), "stoppages": 0, "hours": 0, "hours_are_upper_bound": False})
        t["stoppages"] += 1; t["hours"] += s["hours"]; t["hours_are_upper_bound"] |= bool(s.get("upper_bound"))
    by = {d.get("supplier"): d for d in decisions}
    for sup in totals:
        d = by.get(sup)
        if not d:
            problems.append(f"{sup}: no decision"); continue
        if d.get("choice") not in CHOICES:
            problems.append(f"{sup}: choice must be own, backup or accept")
        if not isinstance(d.get("new_monthly_cost"), (int, float)):
            problems.append(f"{sup}: needs new_monthly_cost")
        if d.get("one_time_cost") in (None, ""):
            problems.append(f"{sup}: needs one_time_cost, a number or why it is unpriced")
        if not d.get("compared_with"):
            problems.append(f"{sup}: compared_with must say what own and backup would cost, or that they are unpriced and why")
        if d.get("choice") in {"own", "backup"}:
            problems += [f"{sup}: {d.get('choice')} needs {k}" for k in ("downturn_cost", "exit", "advice") if not d.get(k) or str(d.get(k)).strip().lower().startswith(("missing", "none", "n/a", "tbd"))]
    for sup in by:
        if sup not in totals:
            problems.append(f"{sup}: decision with no proven stoppage")
    if problems:
        return {"status": "INCOMPLETE", "problems": problems}
    rows = [{**t, **{k: by[t["supplier"]].get(k) for k in ("choice", "new_monthly_cost", "one_time_cost", "compared_with", "downturn_cost", "exit", "advice")}} for t in totals.values()]
    return {"status": "COMPLETE", "total_hours": sum(t["hours"] for t in rows), "suppliers": sorted(rows, key=lambda r: -r["hours"]), "suspected_not_counted": suspected,
            "sources_unavailable": [k for k in SOURCES if sources[k].startswith("unavailable")]}

def selftest():
    src = {k: "searched" for k in SOURCES}
    st = lambda sup="f", h=3, e="p": {"supplier": sup, "date": "2026-01-15", "hours": h, "evidence": e}
    full = {"supplier": "f", "choice": "backup", "new_monthly_cost": 40, "one_time_cost": 0, "compared_with": "own $200", "downturn_cost": "d", "exit": "e", "advice": "a"}
    base = lambda **k: {"stoppages": [], "decisions": [], "suspected": [], "sources": src, **k}
    r = judge(base(stoppages=[st(), {**st(h=2), "upper_bound": True}], decisions=[full]))
    assert r["status"] == "COMPLETE" and r["suppliers"][0]["hours"] == 5 and r["suppliers"][0]["stoppages"] == 2 and r["suppliers"][0]["hours_are_upper_bound"], r
    assert judge(base())["status"] == "COMPLETE"
    assert judge(base(stoppages=[st(e="")], decisions=[full]))["status"] == "INCOMPLETE"
    assert judge(base(stoppages=[st()]))["status"] == "INCOMPLETE"
    assert judge(base(stoppages=[st()], decisions=[{**full, "exit": ""}]))["status"] == "INCOMPLETE"
    assert judge(base(stoppages=[st()], decisions=[{**full, "advice": "MISSING: nobody asked"}]))["status"] == "INCOMPLETE"
    assert judge(base(stoppages=[st()], decisions=[{k: v for k, v in full.items() if k != "one_time_cost"}]))["status"] == "INCOMPLETE"
    assert judge(base(stoppages=[st()], decisions=[{"supplier": "f", "choice": "accept", "new_monthly_cost": 0, "one_time_cost": 0, "compared_with": "unpriced: no quote"}]))["status"] == "COMPLETE"
    assert judge(base(stoppages=[st()], decisions=[{"supplier": "f", "choice": "accept", "new_monthly_cost": 0, "one_time_cost": 0}]))["status"] == "INCOMPLETE"
    assert judge(base(decisions=[full]))["status"] == "INCOMPLETE"
    assert judge(base(sources={**src, "alert_messages": ""}))["status"] == "INCOMPLETE"
    assert judge(base(suspected=[{"supplier": "x", "date": "d"}]))["status"] == "INCOMPLETE"
    r = judge(base(suspected=[{"supplier": "x", "date": "d", "why_unproven": "own lane"}], sources={**src, "alert_messages": "unavailable: no access"}))
    assert r["status"] == "COMPLETE" and r["suspected_not_counted"] and r["sources_unavailable"] == ["alert_messages"] and r["total_hours"] == 0, r
    assert judge({})["status"] == "INCOMPLETE"
    print("selftest pass")

if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest(); sys.exit(0)
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr); sys.exit(2)
    try:
        r = judge(json.load(open(sys.argv[1])))
    except (OSError, ValueError, AttributeError, TypeError) as e:
        print(f"error: {e}", file=sys.stderr); sys.exit(2)
    print(json.dumps(r, indent=1))
    sys.exit(2 if r["status"] == "INCOMPLETE" else 0)
