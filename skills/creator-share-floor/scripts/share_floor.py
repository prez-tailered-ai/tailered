#!/usr/bin/env python3
"""Creator share floor. Usage: share_floor.py <share.json> [--set field=value ...] | --selftest. --set changes a value for one run, to test how far the verdict moves. Exit 0 decided, 2 INCOMPLETE or bad input.
Each field is {"value": n, "source": "..."}; source "assumption" also needs "why". break_even_monthly_departure assumes the raise removes the departure risk, so it is the most favorable case for raising."""
import json, sys

F = ["subs", "gross_per_sub", "cost_per_sub", "current_share", "alternative_monthly", "lost_sub_fraction", "loss_months", "rework_cost"]

def judge(spec):
    missing = []
    for k in F:
        f = spec.get(k) or {}
        if not isinstance(f.get("value"), (int, float)) or isinstance(f.get("value"), bool) or f["value"] < 0 or not f.get("source"):
            missing.append(k)
        elif f["source"] == "assumption" and not f.get("why"):
            missing.append(f"{k}: an assumption needs why")
    v = {k: spec[k]["value"] for k in F if k in spec and isinstance((spec[k] or {}).get("value"), (int, float))}
    if not missing:
        if v["subs"] == 0 or v["gross_per_sub"] == 0:
            missing.append("subs and gross_per_sub must be above zero")
        if v["current_share"] > 1 or v["lost_sub_fraction"] > 1:
            missing.append("current_share and lost_sub_fraction are fractions from 0 to 1")
    if missing:
        return {"status": "INCOMPLETE", "missing": missing}
    gross = v["subs"] * v["gross_per_sub"]
    unit_margin = v["gross_per_sub"] - v["cost_per_sub"]
    assumptions = {k: spec[k]["why"] for k in F if spec[k]["source"] == "assumption"}
    floor = v["alternative_monthly"] / gross
    max_share = max(unit_margin, 0) / v["gross_per_sub"]
    keep_now = max(unit_margin - v["current_share"] * v["gross_per_sub"], 0)  # what the company keeps per subscriber at today's share: what a departure loses
    departure = v["subs"] * v["lost_sub_fraction"] * keep_now * v["loss_months"] + v["rework_cost"]
    base = {"floor_share": round(floor, 4), "max_payable_share": round(max_share, 4), "current_share": v["current_share"], "departure_cost": round(departure, 2), "assumptions": assumptions}
    if floor > max_share:
        return {**base, "status": "NOT_VIABLE", "shortfall_monthly": round((floor - max_share) * gross, 2)}
    if floor <= v["current_share"]:
        return {**base, "status": "HOLD", "extra_monthly": 0, "break_even_monthly_departure": None}
    extra = (floor - v["current_share"]) * gross
    be = extra / departure if departure else None
    if be is None or be >= 1:
        return {**base, "status": "RAISE_NEVER_PAYS", "extra_monthly": round(extra, 2), "break_even_monthly_departure": be and round(be, 4)}
    return {**base, "status": "RAISE", "extra_monthly": round(extra, 2), "break_even_monthly_departure": round(be, 4)}

def selftest():
    def mk(**k):
        d = dict(subs=100, gross_per_sub=30, cost_per_sub=5, current_share=0.2, alternative_monthly=1200, lost_sub_fraction=0.5, loss_months=6, rework_cost=500)
        d.update(k)
        return {f: ({"value": x, "source": "assumption", "why": "guess"} if f == "subs" else {"value": x, "source": "bill"}) for f, x in d.items()}
    r = judge(mk())
    assert r["status"] == "RAISE" and r["floor_share"] == 0.4 and r["extra_monthly"] == 600, r
    assert r["departure_cost"] == 100 * 0.5 * 19 * 6 + 500 == 6200, r
    assert r["break_even_monthly_departure"] == round(600 / 6200, 4), r
    assert r["assumptions"] == {"subs": "guess"}, r
    h = judge(mk(alternative_monthly=300))
    assert h["status"] == "HOLD" and h["departure_cost"] == 6200, h
    assert judge(mk(alternative_monthly=2900))["status"] == "NOT_VIABLE"
    assert judge(mk(alternative_monthly=2400, lost_sub_fraction=0, rework_cost=500))["status"] == "RAISE_NEVER_PAYS"
    bad = mk(); bad["rework_cost"] = {"value": 500}
    assert judge(bad)["status"] == "INCOMPLETE"
    bad = mk(); bad["subs"] = {"value": 100, "source": "assumption"}
    assert judge(bad)["status"] == "INCOMPLETE"
    assert judge(mk(current_share=20))["status"] == "INCOMPLETE"
    assert judge({})["status"] == "INCOMPLETE"
    print("selftest pass")

if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest(); sys.exit(0)
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr); sys.exit(2)
    try:
        spec = json.load(open(sys.argv[1]))
        args = sys.argv[2:]
        if len(args) % 2:
            raise ValueError("--set needs field=value")
        for flag, kv in zip(args[::2], args[1::2]):
            k, v = kv.split("=", 1)
            if flag != "--set" or k not in F:
                raise ValueError(f"bad option {flag} {kv}")
            spec[k]["value"] = float(v)
        r = judge(spec)
    except (OSError, ValueError, AttributeError, TypeError) as e:
        print(f"error: {e}", file=sys.stderr); sys.exit(2)
    print(json.dumps(r, indent=1))
    sys.exit(2 if r["status"] == "INCOMPLETE" else 0)
