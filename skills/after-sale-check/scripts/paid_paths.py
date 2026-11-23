#!/usr/bin/env python3
"""Judge the after-sale table. Usage: paid_paths.py <paths.json> | --selftest. Exit 0 table complete, 2 INCOMPLETE or bad input.
Exit 0 says the table is filled in, not that members are fine: read failed and unmeasured. Results: pass, fail, unmeasured (never a pass), not_on_sale, none_yet."""
import json, sys

RESULTS = {"pass", "fail", "unmeasured", "not_on_sale", "none_yet"}

def judge(spec):
    paths, problems = spec.get("paths"), []
    if not isinstance(paths, list) or not paths:
        return {"status": "INCOMPLETE", "problems": ["no paid path found; a check that saw nothing proves nothing"]}
    failed, unmeasured, off = [], [], []
    for p in paths:
        tag = p.get("path", "?")
        if not p.get("path") or not p.get("promise"):
            problems.append(f"{tag}: needs path and promise")
        r = p.get("result")
        if r not in RESULTS:
            problems.append(f"{tag}: result must be one of {sorted(RESULTS)}"); continue
        if not p.get("evidence"):
            problems.append(f"{tag}: needs evidence, or for unmeasured what stopped the check")
        if r != "unmeasured" and not p.get("at"):
            problems.append(f"{tag}: needs at")
        if r in {"fail", "unmeasured"}:
            (failed if r == "fail" else unmeasured).append(tag)
            if not p.get("fix") or not p.get("owner"):
                problems.append(f"{tag}: a {r} needs a fix and an owner")
        if r in {"not_on_sale", "none_yet"}:
            off.append(tag)
    if problems:
        return {"status": "INCOMPLETE", "problems": problems}
    return {"status": "COMPLETE", "checked": len(paths), "passed": sum(p["result"] == "pass" for p in paths), "failed": failed, "unmeasured": unmeasured, "not_sold_yet": off}

def selftest():
    ok = {"path": "/pricing", "promise": "p", "result": "pass", "evidence": "e", "at": "t"}
    assert judge({"paths": [ok]}) == {"status": "COMPLETE", "checked": 1, "passed": 1, "failed": [], "unmeasured": [], "not_sold_yet": []}
    assert judge({"paths": []})["status"] == "INCOMPLETE" and judge({})["status"] == "INCOMPLETE"
    assert judge({"paths": [{**ok, "evidence": ""}]})["status"] == "INCOMPLETE"
    assert judge({"paths": [{**ok, "result": "fail"}]})["status"] == "INCOMPLETE"
    assert judge({"paths": [{**ok, "result": "unmeasured", "evidence": "", "fix": "f", "owner": "o"}]})["status"] == "INCOMPLETE"
    r = judge({"paths": [{**ok, "result": "unmeasured", "at": "", "fix": "f", "owner": "o"}]})
    assert r["status"] == "COMPLETE" and r["unmeasured"] == ["/pricing"] and r["failed"] == [] and r["passed"] == 0, r
    r = judge({"paths": [{**ok, "result": "none_yet"}]})
    assert r["status"] == "COMPLETE" and r["not_sold_yet"] == ["/pricing"] and not r["failed"], r
    assert judge({"paths": [{**ok, "result": "maybe"}]})["status"] == "INCOMPLETE"
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
