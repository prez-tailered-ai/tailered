#!/usr/bin/env python3
"""Total money found inside. Usage: release_table.py <release.json> | --selftest. Exit 0 complete, 2 INCOMPLETE or bad input.
Every kind must be marked in searched. Totals keep measured and estimated money apart. COMPLETE means the table is filled in, not that the money is safe to take."""
import json, sys

KINDS = ("idle", "duplicate", "subscription", "speed", "byproduct")

def judge(spec):
    rows, searched, problems = spec.get("rows"), spec.get("searched"), []
    if not isinstance(rows, list) or not isinstance(searched, dict):
        return {"status": "INCOMPLETE", "problems": ["rows must be a list and searched a map of each kind"]}
    for k in KINDS:
        if not str(searched.get(k, "")).startswith(("found", "none found", "unavailable")):
            problems.append(f"searched {k}: must start found, none found or unavailable")
    with_rows = {r.get("kind") for r in rows if isinstance(r, dict)}
    for k in KINDS:
        if k in with_rows and not str(searched.get(k, "")).startswith("found"):
            problems.append(f"searched {k}: has rows, so it must start found")
        if k not in with_rows and str(searched.get(k, "")).startswith("found"):
            problems.append(f"searched {k}: says found but has no row")
    totals = {"measured": {"month": 0.0, "once": 0.0}, "estimate": {"month": 0.0, "once": 0.0}}
    unpriced, one_way, leads = [], [], []
    for r in rows:
        tag = r.get("source", "?")
        if r.get("kind") not in KINDS:
            problems.append(f"{tag}: kind")
        for k in ("source", "action"):
            if not r.get(k):
                problems.append(f"{tag}: {k}")
        if r.get("status") not in {"proven", "lead"}:
            problems.append(f"{tag}: status must be proven or lead")
        elif r["status"] == "lead":
            leads.append(tag)
        d = r.get("dollars")
        if d is None:
            unpriced.append(tag)
        elif not isinstance(d, (int, float)) or isinstance(d, bool) or d < 0:
            problems.append(f"{tag}: dollars")
        elif r.get("basis") not in totals:
            problems.append(f"{tag}: basis must be measured (a bill or meter) or estimate (a saved note or short reading)")
        elif not r.get("check"):
            problems.append(f"{tag}: a price needs a check")
        elif r.get("period") not in {"month", "once"}:
            problems.append(f"{tag}: period must be month or once")
        else:
            totals[r["basis"]][r["period"]] += d
        if r.get("retires") and "://" not in str(r.get("copied_to", "")):
            problems.append(f"{tag}: anything retired needs copied_to with the storage URL of its copy")
        if not r.get("undo"):
            one_way.append(tag)
        if r.get("kind") == "byproduct" and d is not None and not r.get("offer"):
            problems.append(f"{tag}: a by-product price needs a real offer or test in offer; otherwise dollars is null")
    if problems:
        return {"status": "INCOMPLETE", "problems": problems}
    out = {"status": "COMPLETE", "measured": totals["measured"], "estimate": totals["estimate"], "unpriced": unpriced, "leads": leads, "one_way": one_way, "rows": len(rows), "searched": searched}
    ask = spec.get("ask")
    if isinstance(ask, (int, float)):
        out["ask"] = ask
        out["measured_monthly_covers_ask"] = totals["measured"]["month"] >= ask
    return out

def selftest():
    sr = {k: "none found" for k in KINDS}
    fi = {**sr, "idle": "found"}
    by = {**sr, "byproduct": "found"}
    row = lambda **k: {"source": "a", "kind": "idle", "status": "proven", "dollars": 12, "basis": "measured", "period": "month", "check": "bill", "undo": "u", "action": "pause", **k}
    r = judge({"ask": 10, "searched": fi, "rows": [row(), row(source="b", dollars=100, period="once"), row(source="c", dollars=None, status="lead"), row(source="d", undo=""), row(source="e", basis="estimate")]})
    assert r["measured"] == {"month": 24, "once": 100} and r["estimate"]["month"] == 12 and r["unpriced"] == ["c"] and r["leads"] == ["c"] and r["one_way"] == ["d"] and r["measured_monthly_covers_ask"], r
    for bad in (row(check=""), row(period="year"), row(kind="byproduct"), row(basis=""), row(status=""), row(retires=True), row(retires=True, copied_to="/tmp/x")):
        assert judge({"searched": by if bad["kind"] == "byproduct" else fi, "rows": [bad]})["status"] == "INCOMPLETE", bad
    assert judge({"searched": by, "rows": [row(kind="byproduct", dollars=None)]})["status"] == "COMPLETE"
    assert judge({"searched": fi, "rows": [row(retires=True, copied_to="storage://example-bucket/path")]})["status"] == "COMPLETE"
    assert judge({"searched": sr, "rows": [row()]})["status"] == "INCOMPLETE"
    assert judge({"searched": fi, "rows": []})["status"] == "INCOMPLETE"
    assert judge({"searched": {**sr, "speed": ""}, "rows": []})["status"] == "INCOMPLETE"
    assert judge({"searched": sr, "rows": []})["status"] == "COMPLETE"
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
