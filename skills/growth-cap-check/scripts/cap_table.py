#!/usr/bin/env python3
"""Check caps against the document and size them. Usage: cap_table.py <terms.txt> <caps.json> | --selftest. Exit 0 complete, 2 INCOMPLETE or bad input.
COMPLETE covers quotes, arithmetic and filled-in walk-aways only, not whether the judgment is right. caps.json: {"clauses": n, "no_cap_clauses": n, "caps": [...]}."""
import json, re, sys

SCALE = 10

def squash(s):
    return re.sub(r"\s+", " ", s).strip().lower()

def judge(text, spec):
    if not squash(text):
        return {"status": "INCOMPLETE", "problems": ["the document is empty"]}
    if not isinstance(spec, dict) or not isinstance(spec.get("caps"), list):
        return {"status": "INCOMPLETE", "problems": ["caps.json needs clauses, no_cap_clauses and a caps list"]}
    doc, problems, rows = squash(text), [], []
    caps, n, none = spec["caps"], spec.get("clauses"), spec.get("no_cap_clauses")
    if not isinstance(n, int) or not isinstance(none, int) or n < 1 or none < 0 or none > n:
        problems.append("clauses and no_cap_clauses must be whole numbers that count the document")
    elif n != none + len(caps):
        problems.append(f"clauses ({n}) must equal no_cap_clauses ({none}) plus caps ({len(caps)})")
    for c in caps:
        q = c.get("quote") or ""
        tag = (c.get("caps") or q[:30] or "?")
        if not squash(q) or squash(q) not in doc:
            problems.append(f"{tag}: quote not found word for word in the document")
        if not c.get("caps"):
            problems.append(f"{tag}: say what it caps")
        limit, today = c.get("limit"), c.get("today")
        if limit is None:
            bites = 0
        elif not isinstance(limit, (int, float)) or not isinstance(today, (int, float)) or today <= 0:
            problems.append(f"{tag}: limit and today must be numbers, or limit null for an approval right"); continue
        else:
            bites = round(limit / today, 2)
        inside = bites < SCALE
        if inside and not (c.get("walk_away") and c.get("walk_cost") and c.get("ask")):
            problems.append(f"{tag}: bites inside {SCALE}x and needs ask, walk_away and walk_cost")
        rows.append({"caps": c.get("caps"), "quote": q, "limit": limit, "today": today, "bites_at_multiple": bites, "inside_10x": inside, "unit_doubt": c.get("unit_doubt"), "ask": c.get("ask"), "walk_away": c.get("walk_away"), "walk_cost": c.get("walk_cost")})
    if problems:
        return {"status": "INCOMPLETE", "problems": problems}
    return {"status": "COMPLETE", "clauses": n, "no_cap_clauses": none, "caps": sorted(rows, key=lambda r: r["bites_at_multiple"]), "inside_10x": sum(r["inside_10x"] for r in rows), "uncertain_units": [r["caps"] for r in rows if r["unit_doubt"]]}

def selftest():
    doc = "Partner may list up to  5,000\nmembers. Partner must approve any price change. Fees are 2%."
    a = {"quote": "up to 5,000 members", "caps": "members", "limit": 5000, "today": 800, "ask": "x", "walk_away": "w", "walk_cost": "c", "unit_doubt": "whose members?"}
    b = {"quote": "must approve any price change", "caps": "price", "limit": None, "ask": "x", "walk_away": "w", "walk_cost": "c"}
    sp = lambda *c, none=1: {"clauses": none + len(c), "no_cap_clauses": none, "caps": list(c)}
    r = judge(doc, sp(a, b))
    assert r["status"] == "COMPLETE" and r["caps"][0]["caps"] == "price" and r["caps"][1]["bites_at_multiple"] == 6.25 and r["inside_10x"] == 2 and r["uncertain_units"] == ["members"], r
    assert judge(doc, sp({**a, "quote": "up to 9,000 members"}))["status"] == "INCOMPLETE"
    assert judge(doc, sp({**a, "walk_away": ""}))["status"] == "INCOMPLETE"
    assert judge(doc, sp({**a, "walk_cost": ""}))["status"] == "INCOMPLETE"
    assert judge(doc, sp({**a, "limit": 50000, "walk_away": "", "walk_cost": ""}))["status"] == "COMPLETE"
    assert judge(doc, sp({**b, "walk_away": ""}))["status"] == "INCOMPLETE"
    assert judge("", sp())["status"] == "INCOMPLETE"
    assert judge(doc, sp(none=3))["status"] == "COMPLETE"
    assert judge(doc, {"clauses": 99, "no_cap_clauses": 0, "caps": [a]})["status"] == "INCOMPLETE"
    assert judge(doc, sp({**a, "ask": ""}))["status"] == "INCOMPLETE"
    assert judge(doc, [])["status"] == "INCOMPLETE"
    assert judge(doc, {"caps": []})["status"] == "INCOMPLETE"
    print("selftest pass")

if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest(); sys.exit(0)
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr); sys.exit(2)
    try:
        r = judge(open(sys.argv[1], errors="ignore").read(), json.load(open(sys.argv[2])))
    except (OSError, ValueError, AttributeError, TypeError) as e:
        print(f"error: {e}", file=sys.stderr); sys.exit(2)
    print(json.dumps(r, indent=1))
    sys.exit(2 if r["status"] == "INCOMPLETE" else 0)
