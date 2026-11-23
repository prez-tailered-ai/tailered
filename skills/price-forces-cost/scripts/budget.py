#!/usr/bin/env python3
"""Split a named target across steps. Usage: budget.py <budget.json> | --selftest. Exit 0 decided, 2 INCOMPLETE or bad input.
Every step needs source: "measured: <where>" or "stated: <who>". A floor above zero needs floor_reason. Stated numbers come back listed as unmeasured."""
import json, sys

def num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and x >= 0

def judge(spec):
    target, steps = spec.get("target"), spec.get("steps") or []
    missing = []
    if not num(target) or target == 0:
        missing.append("target")
    if not steps:
        missing.append("steps")
    for s in steps:
        n = s.get("name", "?")
        if not num(s.get("cost")):
            missing.append(f"{n}: cost")
        if not str(s.get("source", "")).startswith(("measured:", "stated:")):
            missing.append(f"{n}: source must start measured: or stated:")
        if num(s.get("floor")) and s["floor"] > 0 and not s.get("floor_reason"):
            missing.append(f"{n}: floor_reason")
        if num(s.get("floor")) and num(s.get("cost")) and s["floor"] > s["cost"]:
            missing.append(f"{n}: floor above cost")
    if missing:
        return {"status": "INCOMPLETE", "missing": missing}
    total = sum(s["cost"] for s in steps)
    floors = sum(s.get("floor") or 0 for s in steps)
    base = {"target": target, "unit": spec.get("unit"), "target_kind": spec.get("target_kind"), "total": round(total, 4), "floors": round(floors, 4),
            "unmeasured": [s["name"] for s in steps if s["source"].startswith("stated:")], "unmeasured_floors": [s["name"] for s in steps if s.get("floor") and not str(s.get("floor_reason", "")).startswith("measured:")], "no_floor_given": [s["name"] for s in steps if not s.get("floor")]}
    if total <= target:
        return {**base, "status": "MEETS", "steps": [{"name": s["name"], "cost": s["cost"], "budget": s["cost"], "cut": 0} for s in steps]}
    if floors > target:
        blocking = sorted((s for s in steps if s.get("floor")), key=lambda s: -s["floor"])
        return {**base, "status": "UNREACHABLE", "over_by": round(floors - target, 4), "blocking": [s["name"] for s in blocking]}
    room = total - floors
    out = []
    for s in steps:
        f = s.get("floor") or 0
        b = f + (s["cost"] - f) * (target - floors) / room
        cut = s["cost"] - b
        if cut > 1e-9 and not s.get("gives_up"):
            missing.append(f"{s['name']}: gives_up")
        out.append({"name": s["name"], "cost": s["cost"], "budget": round(b, 4), "cut": round(cut, 4), "gives_up": s.get("gives_up")})
    if missing:
        return {"status": "INCOMPLETE", "missing": missing}
    return {**base, "status": "REACHABLE", "steps": sorted(out, key=lambda r: -r["cut"])}

def selftest():
    g, m, st = "less", "measured: bill", "stated: the owner"
    cases = [
        ({"target": 5, "steps": [{"name": "a", "cost": 2, "source": m}, {"name": "b", "cost": 2, "source": st}]}, "MEETS"),
        ({"target": 2, "steps": [{"name": "a", "cost": 3, "floor": 1, "floor_reason": "r", "gives_up": g, "source": m}, {"name": "b", "cost": 1, "gives_up": g, "source": st}]}, "REACHABLE"),
        ({"target": 1, "steps": [{"name": "a", "cost": 3, "floor": 2, "floor_reason": "r", "gives_up": g, "source": m}]}, "UNREACHABLE"),
        ({"target": 1, "steps": [{"name": "a", "cost": None, "source": m}]}, "INCOMPLETE"),
        ({"target": 1, "steps": [{"name": "a", "cost": 3, "source": m}]}, "INCOMPLETE"),
        ({"target": 1, "steps": [{"name": "a", "cost": 3, "floor": 4, "floor_reason": "r", "source": m}]}, "INCOMPLETE"),
        ({"target": 1, "steps": [{"name": "a", "cost": 3, "floor": 1, "gives_up": g, "source": m}]}, "INCOMPLETE"),
        ({"target": 1, "steps": [{"name": "a", "cost": 3, "gives_up": g}]}, "INCOMPLETE"),
        ({"target": 0, "steps": [{"name": "a", "cost": 3, "source": m}]}, "INCOMPLETE"),
    ]
    for spec, want in cases:
        got = judge(spec)["status"]
        assert got == want, (spec, want, got)
    r = judge(cases[1][0])
    assert abs(sum(s["budget"] for s in r["steps"]) - 2) < 1e-3 and r["unmeasured"] == ["b"] and r["no_floor_given"] == ["b"], r
    assert judge(cases[2][0])["blocking"] == ["a"]
    assert judge({"target": 2, "steps": [{"name": "a", "cost": 3, "floor": 1, "floor_reason": "measured: bill", "gives_up": g, "source": m}]})["unmeasured_floors"] == []
    assert r["unmeasured_floors"] == ["a"], r
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
