#!/usr/bin/env python3
"""Split a session's tool time into gather, wait and work. Usage: walking_time.py [--session <id>] <a.jsonl> [b.jsonl] | --steps steps.json | --selftest.
A forked or resumed session's history can sit in a later session's file: --session keeps only that session's records. Main thread only; helper agents are not counted.
Prints tool names, read paths and first words of shell commands only: never command text or file contents. Exit 0 ok, 2 bad input."""
import collections, datetime as dt, json, os, re, shlex, sys, tempfile

GATHER = {"Read", "Grep", "Glob", "WebFetch", "WebSearch", "ToolSearch", "ListAgents", "LS", "NotebookRead"}
WAIT = {"Monitor", "TaskOutput", "ScheduleWakeup", "Agent", "Task", "Workflow", "BashOutput"}
HUMAN = {"AskUserQuestion", "mcp__ccd_turn__wrap_up"}  # time the owner takes to answer is not the session walking
READ_WORDS = {"cat", "sed", "head", "tail", "ls", "grep", "rg", "find", "wc", "du", "df", "awk", "stat", "file", "cut", "sort", "uniq", "which", "pwd", "echo", "date", "tree", "shasum", "sha256sum", "diff", "jq", "curl", "ps", "uptime", "lsof"}
WAIT_WORDS = {"sleep", "wait"}
GATHER_MCP = re.compile(r"(read|get|list|find|search|query|status|snapshot|screenshot)", re.I)

ASSIGN = re.compile(r"""^\s*[A-Za-z_][A-Za-z0-9_]*=(?:\$\([^)]*\)|"[^"]*"|'[^']*'|\S*)\s*;?\s*""")

def first_word(cmd):
    cmd = cmd or ""
    while True:
        m = ASSIGN.match(cmd)
        if not m or not m.group(0):
            break
        cmd = cmd[m.end():]
    cmd = re.sub(r"^(?:cd\s+[^;&]+(?:&&|;)\s*)+", "", cmd)
    cmd = re.sub(r"^for\s+.*?;\s*do\s+", "", cmd, flags=re.S)
    cmd = re.sub(r"^(?:command|time|nice)\s+", "", cmd)
    w = cmd.split()
    if w and w[0].startswith("$") and "/" in w[0]:
        w[0] = w[0].rsplit("/", 1)[1]
    word = os.path.basename(w[0]) if w else ""
    return word if re.fullmatch(r"[A-Za-z0-9_.+-]+", word) else "shell"  # never pass an odd fragment through as a label

SEGMENTS = re.compile(r"&&|\|\||;|\||\n")
WRITES = re.compile(r"(?<![0-9&])>>?(?!\s*&|\s*/dev/null)|\s-i(?:\s|$)|\s--in-place|\s-delete(?:\s|$)|\s-exec\s|\s(?:-X|--request)\s*(?:POST|PUT|PATCH|DELETE)|\s(?:-d|--data)[\s=]")

def classify_bash(cmd):
    """Read-only only if every segment starts with a read-only command and nothing writes. Returns class and the first real word."""
    cmd = cmd or ""
    label, cls = "", "gather"
    if WRITES.search(cmd):
        cls = "work"
    for seg in SEGMENTS.split(cmd):
        if not seg.strip() or re.fullmatch(r"\s*(?:done|fi|then|else|do)\s*", seg):
            continue
        if re.match(r"\s*(?:cd\s|for\s|[A-Za-z_][A-Za-z0-9_]*=\S*\s*$)", seg):
            continue
        w = first_word(seg)
        label = label or w
        if w in WAIT_WORDS:
            return "wait", w
        if w == "git":
            parts = re.sub(r"\s-C\s+(?:\"[^\"]*\"|'[^']*'|\S+)", " ", seg).split()
            sub = parts[parts.index("git") + 1] if "git" in parts[:-1] else ""
            if sub not in {"status", "log", "diff", "show", "branch", "rev-parse", "ls-files"}:
                cls = "work"
        elif w not in READ_WORDS:
            cls = "work"
    return cls, label or "shell"

def classify(name, inp):
    if name == "Bash":
        return classify_bash((inp or {}).get("command", ""))
    if name in HUMAN:
        return "human", name
    if name in GATHER:
        return "gather", name
    if name in WAIT:
        return "wait", name
    if name.startswith("mcp__"):
        return ("gather" if GATHER_MCP.search(name.rsplit("__", 1)[-1]) else "work"), name
    return "work", name

def ts(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))

PATHISH = re.compile(r"^(?:/|~/)[^=$]+$")
TOOL_DIRS = ("/bin/", "/usr/", "/opt/", "/dev/", "/tmp/")

def shell_paths(cmd):
    """Files named by a read-only shell command, only if they really exist as paths, so a quoted argument can never leak through. cd targets and redirect targets do not count."""
    cmd = cmd or ""
    for name, val in re.findall(r"""(?:^|[;\s])([A-Za-z_][A-Za-z0-9_]*)=["']?((?:/|~/)[^"';\s]+)""", cmd):
        cmd = re.sub(rf"\$\{{?{name}\}}?(?![A-Za-z0-9_])", lambda _: val, cmd)
    cmd = re.sub(r"""(?:^|(?<=[;\s]))[A-Za-z_][A-Za-z0-9_]*=\S*""", " ", cmd)
    try:
        lex = shlex.shlex(cmd, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        toks = list(lex)
    except ValueError:
        return []
    out, prev = [], ""
    for t in toks:
        if PATHISH.match(t) and not t.startswith(TOOL_DIRS) and prev not in {"cd", ">", ">>"} and os.path.isfile(os.path.expanduser(t)):
            out.append(t)
        prev = t
    return out

def analyze(paths, session=None):
    pending, totals, reads, slow = {}, collections.Counter(), collections.Counter(), []
    calls = 0; model = 0.0; last_result = None; usage = {}; latest = None; elapsed = 0.0; prompt_gap = 0.0; seen = set(); cut_short = []; spans = []
    for path in paths:
        last_result = None; first = last = None
        with open(path, errors="ignore") as f:
            for line in f:
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                if d.get("isSidechain") or d.get("type") not in {"assistant", "user"} or not d.get("timestamp"):
                    continue
                if session and d.get("sessionId") != session:
                    continue
                if d.get("uuid"):
                    if d["uuid"] in seen:  # forks copy history, so the same record can sit in several files
                        continue
                    seen.add(d["uuid"])
                content = (d.get("message") or {}).get("content")
                t = ts(d["timestamp"])
                latest = t
                first = first or t
                last = t
                msg = d.get("message") or {}
                if d["type"] == "assistant" and isinstance(msg.get("usage"), dict) and msg.get("id"):
                    usage[msg["id"]] = msg["usage"]
                has_tool_use = isinstance(content, list) and any(isinstance(b, dict) and b.get("type") == "tool_use" for b in content)
                if d["type"] == "assistant" and not has_tool_use and last_result is not None:
                    gap = (t - last_result).total_seconds()  # the model writing its reply
                    if 0 <= gap < 3600:
                        model += gap
                    last_result = t
                if d["type"] == "user" and (isinstance(content, str) or (isinstance(content, list) and not any(isinstance(b, dict) and b.get("type") == "tool_result" for b in content))):
                    text = content if isinstance(content, str) else " ".join(str(b.get("text", "")) for b in content if isinstance(b, dict))
                    if not d.get("isMeta") and not text.lstrip().startswith("<"):  # a person typing, not a system note or task notification
                        if last_result is not None:
                            gap = (t - last_result).total_seconds()
                            if gap > 0:
                                prompt_gap += gap
                        last_result = None  # the pause before a person speaks is theirs, not the model's
                if not isinstance(content, list):
                    continue
                for b in content:
                    if not isinstance(b, dict):
                        continue
                    if b.get("type") == "tool_use":
                        cls, label = classify(b.get("name", ""), b.get("input"))
                        pending[b.get("id")] = (t, cls, label)
                        if cls == "gather" and b.get("name") == "Bash":
                            for sp in shell_paths((b.get("input") or {}).get("command", "")):
                                reads[sp] += 1
                        calls += 1
                        if last_result is not None:
                            gap = (t - last_result).total_seconds()
                            if 0 <= gap < 3600:
                                model += gap
                            last_result = None
                        if b.get("name") == "Read":
                            reads[(b.get("input") or {}).get("file_path", "?")] += 1
                    elif b.get("type") == "tool_result" and b.get("tool_use_id") in pending:
                        body = str(b.get("content"))
                        if "Tool call interrupted" in body or "session ended before" in body:
                            continue  # stays in pending: the tool did not run all that time
                        start, cls, label = pending.pop(b["tool_use_id"])
                        sec = (t - start).total_seconds()
                        if sec < 0:
                            continue
                        if "moved to the background" in body:
                            cut_short.append({"at": d["timestamp"], "label": label, "id": b["tool_use_id"], "seconds_until_moved": round(sec, 1)})
                        if cls != "human":
                            spans.append((start, t))
                        totals[cls] += sec
                        slow.append((sec, cls, label, d["timestamp"], b["tool_use_id"]))
                        last_result = t
        if first:
            elapsed += (last - first).total_seconds()
    open_calls = [{"started": s.strftime("%Y-%m-%dT%H:%M:%SZ"), "class": c, "label": l, "seconds_to_end_of_file": round((latest - s).total_seconds(), 1), "id": i} for i, (s, c, l) in pending.items()]
    tokens = {k: sum(u.get(k) or 0 for u in usage.values()) for k in ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")}
    out = summarize(totals, calls, model, reads, slow, open_calls, tokens)
    union, end = 0.0, None
    for s, e in sorted(spans):
        if end is None or s > end:
            union += (e - s).total_seconds(); end = e
        elif e > end:
            union += (e - end).total_seconds(); end = e
    accounted = union + totals.get("human", 0) + model + prompt_gap
    out.update(elapsed_seconds=round(elapsed, 1), tool_clock_seconds=round(union, 1), before_typed_prompts_seconds=round(prompt_gap, 1), unaccounted_seconds=round(max(elapsed - accounted, 0), 1), moved_to_background=cut_short)
    return out

def summarize(totals, calls, model, reads, slow, open_calls=(), tokens=None):
    tool = sum(v for k, v in totals.items() if k != "human")
    all_rep = [(p, n) for p, n in reads.most_common() if n > 1]
    rep = [{"path": p, "reads": n} for p, n in all_rep[:10]]
    return {"tool_calls": calls, "tool_seconds": round(tool, 1), "model_seconds": round(model, 1), "human_seconds": round(totals.get("human", 0), 1), "unfinished_calls": sorted(open_calls, key=lambda c: -c["seconds_to_end_of_file"])[:5], "tokens": tokens,
            "seconds": {k: round(totals.get(k, 0), 1) for k in ("gather", "wait", "work")},
            "share_pct": {k: round(100 * totals.get(k, 0) / tool, 1) if tool else 0 for k in ("gather", "wait", "work")},
            "repeated_reads": rep, "repeat_read_count": sum(n - 1 for _, n in all_rep), "repeated_paths": len(all_rep),
            "slowest": [{"seconds": round(x[0], 1), "class": x[1], "label": x[2], "at": x[3], "id": x[4]} for x in sorted((x for x in slow if x[1] != "human"), key=lambda x: -x[0])[:5]]}

def steps(path):
    rows = json.load(open(path))
    bad = [r for r in rows if r.get("class") not in {"gather", "wait", "work"} or not isinstance(r.get("seconds"), (int, float))]
    if not rows or bad:
        raise ValueError(f"bad steps: {bad or 'empty'}")
    totals = collections.Counter()
    for r in rows:
        totals[r["class"]] += r["seconds"]
    return summarize(totals, len(rows), 0.0, collections.Counter(), [(r["seconds"], r["class"], r.get("name", "?"), None, None) for r in rows])

def selftest():
    a = lambda i, n, inp, t: json.dumps({"type": "assistant", "timestamp": f"2026-11-05T00:00:{t:02d}Z", "message": {"content": [{"type": "tool_use", "id": i, "name": n, "input": inp}]}})
    u = lambda i, t: json.dumps({"type": "user", "timestamp": f"2026-11-05T00:00:{t:02d}Z", "message": {"content": [{"type": "tool_result", "tool_use_id": i}]}})
    secret = "SECRETVALUE"
    log = [a("1", "Read", {"file_path": "/x"}, 0), u("1", 10), a("2", "Read", {"file_path": "/x"}, 12), u("2", 16),
           a("3", "Bash", {"command": f"cat /y # {secret}"}, 20), u("3", 22), a("4", "Edit", {"file_path": "/x"}, 25), u("4", 35),
           a("5", "Bash", {"command": f"X=1 sleep 5 # {secret}"}, 35), u("5", 40), a("6", "Bash", {"command": "cd /a && npm test"}, 40), u("6", 50), a("7", "AskUserQuestion", {}, 50), u("7", 59),
           json.dumps({"type": "user", "timestamp": "2026-11-05T00:30:00Z", "message": {"content": "next request"}}), a("8", "Read", {"file_path": "/z"}, 59), u("8", 59), "not json"]
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "s.jsonl")
        tagged = [json.dumps({**json.loads(x), "sessionId": "A"}) if x != "not json" else x for x in log]
        other = json.dumps({"type": "assistant", "sessionId": "B", "timestamp": "2026-11-05T00:00:01Z", "message": {"id": "m", "usage": {"input_tokens": 5}, "content": [{"type": "tool_use", "id": "b", "name": "Edit", "input": {}}]}})
        open(p, "w").write("\n".join(tagged + [other]))
        cut = [json.dumps({"type": "assistant", "uuid": "u1", "timestamp": "2026-11-05T00:00:00Z", "message": {"content": [{"type": "tool_use", "id": "z", "name": "Read", "input": {"file_path": "/q"}}]}}),
               json.dumps({"type": "user", "uuid": "u2", "timestamp": "2026-11-05T07:00:00Z", "message": {"content": [{"type": "tool_result", "tool_use_id": "z", "content": "[Tool call interrupted: the session ended before this call's result was recorded]"}]}})]
        c1 = os.path.join(d, "c.jsonl"); open(c1, "w").write("\n".join(cut))
        cr = analyze([c1])
        assert cr["tool_seconds"] == 0 and len(cr["unfinished_calls"]) == 1, cr
        assert analyze([c1, c1])["tool_calls"] == 1, "records copied across forks must count once"
        par = [json.dumps({"type": "assistant", "timestamp": "2026-11-05T00:00:00Z", "message": {"content": [{"type": "tool_use", "id": i, "name": "Read", "input": {}} for i in "ab"]}}),
               json.dumps({"type": "user", "timestamp": "2026-11-05T00:01:40Z", "message": {"content": [{"type": "tool_result", "tool_use_id": i} for i in "ab"]}})]
        c2 = os.path.join(d, "par.jsonl"); open(c2, "w").write("\n".join(par))
        pr = analyze([c2])
        assert pr["tool_seconds"] == 200 and pr["tool_clock_seconds"] == 100, pr
        all_ = analyze([p])
        assert all_["tool_calls"] == 9 and len(all_["unfinished_calls"]) == 1 and all_["tokens"]["input_tokens"] == 5, all_
        r = analyze([p], session="A")
    assert r["tool_calls"] == 8, r
    assert classify("mcp__ccd_turn__wrap_up", {})[0] == "human"
    assert first_word('command cat /x') == "cat" and first_word('for f in a b; do sed -n 1p $f; done') == "sed" and first_word('$HOME/bin/grep x') == "grep"
    assert classify("Bash", {"command": 'git -C "/a b" status'})[0] == "gather" and classify("Bash", {"command": "cat /x"})[0] == "gather"
    with tempfile.TemporaryDirectory() as d2:
        fp = os.path.join(d2, "b c.md"); open(fp, "w").close()
        assert shell_paths(f'/bin/ls; sed -n 1,2p "{fp}"; X=/secret TOKEN=abc') == [fp]
        assert shell_paths(f'F="{d2}/x"; grep "/login password hunter2" notes') == []
        assert shell_paths(f'cd {d2}; cat > "{fp}"') == []
        np = os.path.join(d2, "c.md"); open(np, "w").close()
        assert shell_paths(f"F={np}; sed -n 1,2p $F") == [np]
    assert shell_paths(r"F=/a/b\d.md; cat $F") == []
    for cmd in ("curl -X POST u", "sed -i s/a/b/ f", "find . -delete", "cat > f", "cat f && npm run build"):
        assert classify("Bash", {"command": cmd})[0] == "work", cmd
    for cmd in ("ls; cat /x", "cd /a; X=1; cat /x", "cat /x 2>/dev/null", "cat /x | wc -l"):
        assert classify("Bash", {"command": cmd})[0] == "gather", cmd
    assert r["elapsed_seconds"] >= r["tool_seconds"] and "before_typed_prompts_seconds" in r, r
    assert r["human_seconds"] == 9 and "human" not in r["share_pct"] and all(x["class"] != "human" for x in r["slowest"]), r
    assert r["seconds"] == {"gather": 16, "wait": 5, "work": 20}, r["seconds"]
    assert {"path": "/x", "reads": 2} in r["repeated_reads"], r
    assert r["model_seconds"] == 2 + 4 + 3 + 0 + 0, r["model_seconds"]
    assert secret not in json.dumps(r), "leaked command text"
    assert classify("Bash", {"command": "git status"})[0] == "gather" and classify("Bash", {"command": "git commit -m x"})[0] == "work"
    assert first_word('NOW=$(date -u +%F) TOK="a b" node x.mjs') == "node" and first_word("S=/tmp; cat f") == "cat" and first_word("$(secret-thing)") == "shell"
    print("selftest pass")

if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--selftest"]:
        selftest(); sys.exit(0)
    if not a:
        print(__doc__, file=sys.stderr); sys.exit(2)
    try:
        if a[0] == "--steps":
            r = steps(a[1])
        elif a[0] == "--session":
            r = analyze(a[2:], session=a[1])
        else:
            r = analyze(a)
    except (OSError, ValueError, IndexError) as e:
        print(f"error: {e}", file=sys.stderr); sys.exit(2)
    if not r["tool_calls"]:
        print("error: no tool calls found", file=sys.stderr); sys.exit(2)
    print(json.dumps(r, indent=1))
