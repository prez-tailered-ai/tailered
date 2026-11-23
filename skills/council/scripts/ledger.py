#!/usr/bin/env python3
"""Append-only council and confidence ledgers, with scoring. The owner's confidence rule."""
import argparse, datetime, hashlib, json, os, sys, tempfile

def now(): return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def path(root, name): d = os.path.join(root, "ledgers"); os.makedirs(d, exist_ok=True); return os.path.join(d, name)
def read(p): return [json.loads(l) for l in open(p)] if os.path.exists(p) else []
def append(p, rec):
    rec["id"] = hashlib.sha256(json.dumps(rec, sort_keys=True).encode()).hexdigest()[:12]
    with open(p, "a") as f: f.write(json.dumps(rec, sort_keys=True) + "\n")
    print(json.dumps(rec, sort_keys=True)); return rec

def fail(msg): print("REFUSED: " + msg, file=sys.stderr); sys.exit(2)

def stats(lines):
    claims = {l["id"]: l for l in lines if l.get("kind") == "claim" and "low" in l}
    settled = [l for l in lines if l.get("kind") == "settle"]
    briers, inside, unsettleable = [], 0, 0
    for s in settled:
        c = claims.get(s["claim_id"])
        if not c: continue
        if s.get("unsettleable"): unsettleable += 1; briers.append(1.0); continue
        p = (c["low"] + c["high"]) / 200.0; o = s["outcome"]; briers.append((p - o) ** 2)
        inside += 1 if (o == 1 and c["high"] >= 50) or (o == 0 and c["low"] <= 50) else 0
    n = len(briers); scored = n - unsettleable
    cov = inside / scored if scored else None
    return {"settled": n, "unsettleable": unsettleable, "mean_brier": round(sum(briers) / n, 4) if n else None,
            "coverage": round(cov, 3) if cov is not None else None,
            "widen_by": 10 if (n >= 20 and cov is not None and cov < 0.6) else 0}

def main(argv=None):
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("confidence"); c.add_argument("--root", required=True); c.add_argument("--claim", required=True)
    c.add_argument("--low", type=int); c.add_argument("--high", type=int); c.add_argument("--level", choices=["High", "Medium", "Low"])
    c.add_argument("--fact", action="append", default=[]); c.add_argument("--critical-assumed", default="none")
    c.add_argument("--narrowed-by"); c.add_argument("--settle-by"); c.add_argument("--settle-source"); c.add_argument("--session", required=True)
    k = sub.add_parser("council"); k.add_argument("--root", required=True); k.add_argument("--question", required=True)
    k.add_argument("--mode", choices=["quick", "standard", "deep"], required=True); k.add_argument("--position", action="append", default=[])
    k.add_argument("--recommendation", required=True); k.add_argument("--session", required=True)
    s = sub.add_parser("settle"); s.add_argument("--root", required=True); s.add_argument("--id", required=True)
    s.add_argument("--outcome", type=int, choices=[0, 1]); s.add_argument("--unsettleable", action="store_true")
    r = sub.add_parser("report"); r.add_argument("--root", required=True)
    sub.add_parser("selftest")
    a = ap.parse_args(argv)
    if a.cmd == "selftest": return selftest()
    if a.cmd == "council":
        if len(a.position) < 3: fail("a council has at least three voices")
        return append(path(a.root, "council.jsonl"), {"kind": "council", "at": now(), "question": a.question, "mode": a.mode,
                      "positions": a.position, "recommendation": a.recommendation, "session": a.session})
    p = path(a.root, "confidence.jsonl")
    if a.cmd == "confidence":
        tags = [f.split(":", 1)[0] for f in a.fact]
        if any(t not in ("verified", "given", "assumed") for t in tags): fail("every fact is tagged verified, given or assumed")
        if not a.fact: fail("list the facts the answer rests on")
        rec = {"kind": "claim", "at": now(), "claim": a.claim, "facts": a.fact, "critical_assumed": a.critical_assumed, "session": a.session}
        if a.level and a.low is None:
            if a.level == "High" and a.critical_assumed != "none": fail("no High level while a critical fact is assumed: " + a.critical_assumed)
            rec["level"] = a.level; return append(p, rec)
        if a.low is None or a.high is None: fail("a percentage needs --low and --high, or give --level")
        if "verified" not in tags: fail("No percentage: nothing here is verified")
        if not (0 <= a.low < a.high <= 100): fail("range must satisfy 0 <= low < high <= 100")
        track = stats(read(p)); need = 10 + track["widen_by"]
        if a.high - a.low != need and not a.narrowed_by: fail("the range is %d points wide unless --narrowed-by names the source" % need)
        if a.critical_assumed != "none" and a.high > 70: fail("cap at 70% while a critical fact is assumed: " + a.critical_assumed)
        if not a.settle_by or not a.settle_source: fail("name the settle-by date and the settle source")
        rec.update(low=a.low, high=a.high, settle_by=a.settle_by, settle_source=a.settle_source, narrowed_by=a.narrowed_by)
        if track["settled"] >= 20: rec["track_record"] = track
        return append(p, rec)
    if a.cmd == "settle":
        if a.outcome is None and not a.unsettleable: fail("give --outcome 0|1 or --unsettleable")
        if not any(l.get("id") == a.id and l.get("kind") == "claim" for l in read(p)): fail("no claim with id " + a.id)
        if any(l.get("claim_id") == a.id and l.get("kind") == "settle" for l in read(p)): fail("claim " + a.id + " is already settled")
        return append(p, {"kind": "settle", "at": now(), "claim_id": a.id, "outcome": a.outcome, "unsettleable": a.unsettleable})
    if a.cmd == "report":
        print(json.dumps(stats(read(p)), sort_keys=True)); return 0

def selftest():
    root = tempfile.mkdtemp(prefix="council-ledger-"); ok = True
    def run(args, want):
        nonlocal ok
        try: main(args); got = 0
        except SystemExit as e: got = e.code
        if got != want: ok = False; print(f"FAIL {args[:3]} exit {got}, want {want}", file=sys.stderr)
    base = ["confidence", "--root", root, "--claim", "c", "--session", "t", "--settle-by", "2026-12-01", "--settle-source", "db"]
    run(base + ["--low", "60", "--high", "70", "--fact", "verified:x (q)"], 0)
    run(base + ["--low", "60", "--high", "70", "--fact", "assumed:x"], 2)                       # no verified fact
    run(base + ["--low", "50", "--high", "80", "--fact", "verified:x (q)"], 2)                  # 30 points wide
    run(base + ["--low", "65", "--high", "75", "--fact", "verified:x (q)", "--critical-assumed", "y"], 2)  # over the cap
    run(["confidence", "--root", root, "--claim", "c", "--session", "t", "--low", "60", "--high", "70", "--fact", "verified:x (q)"], 2)  # no settle
    run(base + ["--level", "Medium", "--fact", "given:x"], 0)
    run(base + ["--level", "High", "--fact", "given:x", "--critical-assumed", "y"], 2)       # no High level while a critical fact is assumed
    run(["council", "--root", root, "--question", "q", "--mode", "quick", "--position", "a", "--position", "b", "--recommendation", "r", "--session", "t"], 2)
    lines = read(os.path.join(root, "ledgers", "confidence.jsonl"))
    if len(lines) != 2: ok = False; print("FAIL expected 2 ledger lines, got %d" % len(lines), file=sys.stderr)
    cid = lines[0]["id"]; run(["settle", "--root", root, "--id", cid, "--outcome", "1"], 0)
    run(["settle", "--root", root, "--id", cid, "--outcome", "0"], 2)                           # a claim settles once
    st = stats(read(os.path.join(root, "ledgers", "confidence.jsonl")))
    if abs(st["mean_brier"] - 0.1225) > 1e-9 or st["coverage"] != 1.0: ok = False; print("FAIL scoring", st, file=sys.stderr)
    for i in range(25):   # 25 settled misses at 60-70 -> coverage 1/26 < 0.6 -> widen
        wide = stats(read(os.path.join(root, "ledgers", "confidence.jsonl")))["widen_by"]   # once widened, the misses use the wider range
        b = ["confidence", "--root", root, "--claim", "c%d" % i, "--session", "t", "--settle-by", "2026-12-01", "--settle-source", "db"]   # a distinct claim each time: one claim settles once
        r = main(b + ["--low", "55" if wide else "60", "--high", "75" if wide else "70", "--fact", "verified:x (q)"]); main(["settle", "--root", root, "--id", r["id"], "--outcome", "0"])
    if stats(read(os.path.join(root, "ledgers", "confidence.jsonl")))["widen_by"] != 10: ok = False; print("FAIL widening", file=sys.stderr)
    wb = ["confidence", "--root", root, "--claim", "after-widening", "--session", "t", "--settle-by", "2026-12-01", "--settle-source", "db"]
    run(wb + ["--low", "60", "--high", "70", "--fact", "verified:x (q)"], 2)                    # widened: 10 points is now refused
    run(wb + ["--low", "55", "--high", "75", "--fact", "verified:x (q)"], 0)                    # widened: 20 points is accepted
    print("selftest ok" if ok else "selftest FAILED"); sys.exit(0 if ok else 1)

if __name__ == "__main__":
    r = main(); sys.exit(0 if r is None or isinstance(r, dict) or r == 0 else r)
