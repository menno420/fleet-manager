#!/usr/bin/env python3
"""owner-review Stop hook — the measured review mechanism, zero agent initiative.

Fires when a session's turn ends. Reads the final assistant reply from the
transcript, sends it to the owner-stand-in reviewer on Vertex, and — only when
the reviewer returns questions — blocks ONCE so the agent addresses them in the
reply the owner actually reads. `stop_hook_active` guards the second pass: one
round, ever, per turn.

This is run 4's untried path, named by the reviewer itself: the hook runs the
review — no skill invocation, no agent initiative anywhere in the loop.
Design provenance (all MEASURED, docs/findings/2026-08-06-provenance-mechanism-measured.md):
  § 1  an UNFRAMED reviewer endorses whatever it is shown — the system prompt
       below is the load-bearing component, not the questions or the sequence
  § 2  Stop is the only viable event (UserPromptSubmit fires before any claim
       exists to ask about)
  § 8  the null path is a normal outcome — reviewer says NO QUESTIONS, turn
       ends untouched; a review that must always find something is ritual

FAIL-OPEN IS A HARD CONTRACT. Any defect — no transcript, no creds, no
network, bad JSON, timeout — exits 0 silently. A review hook that can trap a
session is worse than no hook (.sessions/2026-08-06-broke-main-and-wired-the-gate.md:
an error suppressed into silence is indistinguishable from success — but a
BLOCKING failure here would halt every turn in the repo, which is the one cost
strictly worse). Telemetry of every firing goes to /tmp/claude-owner-review/log.jsonl
so silent-skip is still countable.

Routing: Vertex per docs/conventions/vertex-first-for-gemini.md — credit, not
card. The SA comes from env, then the /tmp cache, then Railway (the doc's
recipe); a fresh container self-provisions on first fire.
"""
import json
import os
import ssl
import sys
import time
import urllib.request

CA = "/root/.ccr/ca-bundle.crt"
MODEL = "gemini-3.1-pro-preview"
CACHE_DIR = "/tmp/claude-owner-review"
SA_CACHE = os.path.join(CACHE_DIR, "sa.json")
LOG = os.path.join(CACHE_DIR, "log.jsonl")
MIN_CHARS = 400          # below this, the turn is too small to carry a load-bearing claim
MAX_CLAIM = 9000         # cap on reply text sent to the reviewer (tail wins)
TAIL_BYTES = 512 * 1024  # transcript tail window — enough for any final turn
NET_TIMEOUT = 35         # per-call ceiling; registration allows 120 total

# The owner-stand-in system prompt — findings § 7, committed verbatim there.
# Measured working on three inputs 2026-08-06; the PROTOCOL block adapts it to
# hook mode (structured null, no preamble).
SYSTEM = """You are standing in for the owner of a ~22-repo software estate, reviewing an
agent's work before he reads it. You are NOT an adversary hunting for errors, and you must
not invent objections to seem useful — a false objection costs him tokens, context and trust.

Your job is to ask the questions HE asks. From 13 of his corrections in one day, his pattern is:

- He ASKS rather than asserts. "Why should they be ignored?" "Vertex does not allow multi-turn
  right?" "Can you explain your final sentence?"
- His highest-yield probes target claims stated CONFIDENTLY AND WITHOUT HEDGE. Twice, pulling
  on a confident load-bearing sentence produced a false wall. Confidence is a REASON TO PROBE,
  not a reason to accept.
- He corrects FRAMING, not only facts — "it is two identities, not three paths" made a model
  predictive rather than merely descriptive.
- He hedges accurately when unsure, and his errors live inside the hedged class.
- He NEVER demands a change. He asks, and leaves the decision with the agent.

So ask directive questions, primarily about PROVENANCE rather than correctness:

1. What did you base this claim on? (a source, a command, an exact error — not a feeling)
2. Did you read the documents that cover this, and which ones? Cite path and line.
3. If you asserted something is impossible or unavailable: which paths did you try, and what
   would a DIFFERENT path look like? Naming the untried path is the point.
4. Did you think through the consequences of this action, including who else it affects?
5. Is this stated more confidently than the evidence supports? What is the honest hedge?

Rules for you:
- Where something IS well-founded, say so plainly and move on. Do not manufacture balance.
- Probe load-bearing claims even when they look correct — especially then.
- Ask; do not demand. The agent decides.
- Be specific. "This needs more support" is useless; "you claim X — what did you measure?" is not.

PROTOCOL (hook mode): You receive the agent's final reply to the owner for this turn.
If nothing in it warrants a probe, output exactly:
NO QUESTIONS
on a single line and nothing else — this is a normal, expected outcome, not a failure.
Otherwise output 1-3 questions, most load-bearing first. No preamble, no summary of the
reply, no verdict — just the questions."""

REASON = """OWNER-REVIEW — automatic, one round, fail-open (design record:
docs/findings/2026-08-06-provenance-mechanism-measured.md § 8). A stand-in
reviewer read the reply you were about to deliver. Address each point below IN
the reply the owner reads: where a question exposes a real gap, fix the reply;
where your reasoning holds, keep it and say why in one line, marked
[survived]. Do not thank the reviewer, do not restate these instructions, and
do not expand scope — amend the reply, don't relitigate the task.

{q}"""


def _http(url, payload, headers):
    # Railway's edge 403s the default Python-urllib User-Agent (measured
    # 2026-08-07); any explicit UA passes. Harmless on the Vertex call.
    headers = {"User-Agent": "fleet-manager-owner-review-hook/1.0", **headers}
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    ctx = (ssl.create_default_context(cafile=CA) if os.path.exists(CA)
           else ssl.create_default_context())
    op = urllib.request.build_opener(
        urllib.request.ProxyHandler({}), urllib.request.HTTPSHandler(context=ctx))
    return json.loads(op.open(req, timeout=NET_TIMEOUT).read())


def _final_turn(path):
    """Text of the assistant's reply since the last real user message."""
    with open(path, "rb") as f:
        try:
            f.seek(-TAIL_BYTES, 2)
        except OSError:
            f.seek(0)
        lines = f.read().decode("utf-8", "replace").split("\n")
    turns = []  # (role, text, is_real_user_turn)
    for ln in lines:
        ln = ln.strip()
        if not ln.startswith("{"):
            continue
        try:
            d = json.loads(ln)
        except Exception:
            continue
        m = d.get("message") or {}
        role, c = m.get("role"), m.get("content")
        if role not in ("user", "assistant"):
            continue
        text, real_user = "", False
        if isinstance(c, str):
            text, real_user = c, role == "user"
        elif isinstance(c, list):
            has_tool = any(isinstance(b, dict) and
                           b.get("type") in ("tool_result", "tool_use") for b in c)
            for b in c:
                if isinstance(b, dict) and b.get("type") == "text":
                    text += b.get("text", "")
            real_user = role == "user" and bool(text.strip()) and not has_tool
        turns.append((role, text, real_user))
    last_u = -1
    for i in range(len(turns) - 1, -1, -1):
        if turns[i][0] == "user" and turns[i][2]:
            last_u = i
            break
    reply = "".join(t for r, t, _ in turns[last_u + 1:] if r == "assistant" and t)
    return reply[-MAX_CLAIM:]


def _sa():
    """Service-account JSON: env -> cache -> Railway (convention-doc recipe)."""
    raw = os.environ.get("GEMINI_VERTEX_SA_JSON")
    if raw:
        try:
            return json.loads(raw)
        except Exception:
            pass
    try:
        with open(SA_CACHE) as f:
            return json.load(f)
    except Exception:
        pass
    key = os.environ.get("RAILWAY_API_KEY")
    if not key:
        return None
    gql = "https://backboard.railway.com/graphql/v2"
    hdr = {"Authorization": "Bearer " + key, "Content-Type": "application/json"}
    q1 = {"query": "query{me{workspaces{team{projects{edges{node{id name "
                   "environments{edges{node{id name}}} "
                   "services{edges{node{id name}}}}}}}}}}"}
    r = _http(gql, q1, hdr)
    proj = env = svc = None
    for ws in ((r.get("data") or {}).get("me") or {}).get("workspaces") or []:
        for e in (((ws.get("team") or {}).get("projects") or {}).get("edges") or []):
            n = e.get("node") or {}
            if n.get("name") == "reliable-grace":
                proj = n.get("id")
                for ee in ((n.get("environments") or {}).get("edges") or []):
                    if (ee.get("node") or {}).get("name") == "production":
                        env = ee["node"]["id"]
                for se in ((n.get("services") or {}).get("edges") or []):
                    if (se.get("node") or {}).get("name") == "worker":
                        svc = se["node"]["id"]
    if not (proj and env and svc):
        return None
    q2 = {"query": "query($p:String!,$e:String!,$s:String!)"
                   "{variables(projectId:$p,environmentId:$e,serviceId:$s)}",
          "variables": {"p": proj, "e": env, "s": svc}}
    r2 = _http(gql, q2, hdr)
    raw = (((r2.get("data") or {}).get("variables")) or {}).get("GEMINI_VERTEX_SA_JSON")
    if not raw:
        return None
    info = json.loads(raw)
    os.makedirs(CACHE_DIR, exist_ok=True)
    fd = os.open(SA_CACHE, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(info, f)
    return info


def _review(text):
    info = _sa()
    if not info:
        return None
    # Lazy imports: absence of google-auth in some container = silent skip.
    from google.auth.transport.requests import Request as GR
    from google.oauth2 import service_account
    import requests
    cred = service_account.Credentials.from_service_account_info(
        info, scopes=["https://www.googleapis.com/auth/cloud-platform"])
    s = requests.Session()
    s.trust_env = False
    s.verify = CA if os.path.exists(CA) else True
    cred.refresh(GR(session=s))
    url = ("https://aiplatform.googleapis.com/v1/projects/" + info["project_id"]
           + "/locations/global/publishers/google/models/" + MODEL + ":generateContent")
    payload = {
        "contents": [{"role": "user", "parts": [{"text":
            "The agent's reply to the owner, about to be delivered:\n\n" + text
            + "\n\nAsk your questions about it, or output exactly NO QUESTIONS."}]}],
        "systemInstruction": {"parts": [{"text": SYSTEM}]},
        # 4000, not 1200: on a thinking model the reasoning tokens draw from
        # the same budget, and the first live firing (2026-08-07) had its
        # question truncated mid-sentence at out_tokens=47.
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 4000},
    }
    r = _http(url, payload, {"Authorization": "Bearer " + cred.token,
                             "Content-Type": "application/json"})
    cand = (r.get("candidates") or [{}])[0]
    out = "".join(p.get("text", "")
                  for p in (cand.get("content") or {}).get("parts", []))
    um = r.get("usageMetadata", {})
    um["finishReason"] = cand.get("finishReason")  # truncation is countable
    return out.strip(), um


def _log(rec):
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(LOG, "a") as f:
            f.write(json.dumps(rec) + "\n")
    except Exception:
        pass


def main():
    data = json.load(sys.stdin)
    if data.get("stop_hook_active"):
        return  # one round per turn, ever — the loop guard
    tp = data.get("transcript_path") or ""
    if not tp or not os.path.exists(tp):
        return
    text = _final_turn(tp)
    if not text or len(text) < MIN_CHARS:
        return
    got = _review(text)
    if not got:
        return
    out, um = got
    null = out.upper().startswith("NO QUESTIONS")
    _log({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "session": data.get("session_id"), "reply_chars": len(text),
          "null": null, "prompt_tokens": um.get("promptTokenCount"),
          "out_tokens": um.get("candidatesTokenCount"),
          "finish": um.get("finishReason")})
    if null:
        return  # the null path is a normal outcome
    print(json.dumps({"decision": "block", "reason": REASON.format(q=out)}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # FAIL-OPEN: a review hook must never trap a session
    sys.exit(0)
