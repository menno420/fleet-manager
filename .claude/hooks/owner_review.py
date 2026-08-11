#!/usr/bin/env python3
"""owner-review Stop hook — the measured review mechanism, zero agent initiative.

Fires when a session's turn ends. Reads the final assistant reply from the
transcript and **blocks ONCE, unconditionally**, with the fixed question — "what
made you draw this conclusion?" needs no model (docstring corrected 2026-08-11;
it described the v1 design until then, while main() had inverted it). The
reviewer model (free AI Studio key first, Vertex as the 429 fallback — see the
routing note below) is strictly ADDITIVE enrichment: when it returns specifics
they are appended under "And specifically:", and NO QUESTIONS simply appends
nothing — the block still happens, because selective firing measured as the
worst of the three designs (README § "the fixed question IS the hook").
`stop_hook_active` guards the second pass: one round, ever, per turn.

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

Routing, revised 2026-08-08: **free AI Studio key first, Vertex as fallback.**
Asked why this hook needed Google auth at all, the measured answer was that it
did not — free-tier gemini-flash-latest, given the same system prompt, returned
the SAME two findings the Vertex/Pro reviewer had produced on the previous turn,
in 7.1s and 70 output tokens at no cost. That is § 1 restated: the system prompt
is the load-bearing component, not the model. The auth chain was buying a bigger
model for a job the small one does. (An earlier version of this sentence added
"and it was the only part that ever broke" — an overstatement the estate logged
as an owner-caught incident: Vertex itself never broke, the google-auth LIBRARY
was absent once and a logging defect was misfiled as auth; the cold re-measure
is 7.5s end to end. See _free_review's docstring and README § Correction.)
The free tier's requests-per-day cap is the real risk for a per-turn hook, so
Vertex stays wired underneath for exactly that (429 → fall through), per
docs/conventions/vertex-first-for-gemini.md, which reserves the Vertex default
for volume/image/video and otherwise says "free key unless its daily cap is
genuinely in the way". Which route answered is recorded per firing.
"""
import base64
import json
import os
import ssl
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request

CA = "/root/.ccr/ca-bundle.crt"
MODEL = "gemini-3.1-pro-preview"   # Vertex fallback
FREE_MODEL = "gemini-flash-latest"  # AI Studio primary — free tier, no auth chain
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

# The mechanism itself — no model, no network, no credentials, no failure mode.
# findings § 8, MEASURED: both questions are CONTENT-INDEPENDENT. The owner
# composed Q1 *before* the output it was fired at existed, pre-committed to
# firing it regardless of content, and screenshotted the pre-commitment — it
# landed anyway. That falsified the claim that per-turn selection carries the
# payload: **no selector is required.** The same section rates the options —
# "fixed-and-always-on and blended-into-conversation both avoid the test-signal;
# SELECTIVE FIRING IS THE WORST OF THE THREE" — and a reviewer that returns
# NO QUESTIONS on some turns *is* selective firing. So the fixed question is the
# hook, and the model is an optional enrichment that can never be load-bearing.
FIXED = """1. What made you draw that conclusion? Name the load-bearing claim in the reply
above and what you actually ran, read or measured to establish it — a command, a path and
line, an exact error. If you only inferred it, say so in the reply.

2. ONLY IF that surfaced a weak link: can you simplify the mistake? A sound derivation
reduces to one sentence; a confabulated one either drops the load-bearing part under
compression or grows a new one, and the compression must be derivable from the expansion.
If question 1 came back clean, say so in one line and skip this — the pair is a check, not
a quota, and question 2 has no referent when nothing was surfaced."""

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


def _access_token(info):
    """Service-account OAuth with no google-auth dependency.

    This used to be `from google.oauth2 import service_account`, guarded by a
    comment reading *"absence of google-auth in some container = silent skip"* —
    the failure was anticipated and answered with silence. MEASURED 2026-08-08:
    `google.auth` is **absent from this container**, so every Stop since the hook
    landed raised ModuleNotFoundError inside `_review`, got swallowed by the
    fail-open wrapper, and exited 0. The hook was believed live and had never
    once run. A false guardrail, which this estate already rates as costlier
    than a false wall.

    The self-signed-JWT flow needs only `cryptography` (present) plus stdlib, so
    the whole class of failure goes away rather than being caught more loudly.
    google-auth is still preferred when it happens to be installed.
    """
    scope = "https://www.googleapis.com/auth/cloud-platform"
    try:  # if the library is here, use it — it handles more edge cases than we do
        from google.auth.transport.requests import Request as GR
        from google.oauth2 import service_account
        import requests
        cred = service_account.Credentials.from_service_account_info(info, scopes=[scope])
        s = requests.Session()
        s.trust_env = False
        s.verify = CA if os.path.exists(CA) else True
        cred.refresh(GR(session=s))
        return cred.token
    except ImportError:
        pass

    # Sign with the openssl BINARY, not the `cryptography` package. MEASURED
    # 2026-08-08: `import cryptography...` in this container fails on a missing
    # `_cffi_backend` and its Rust layer raises **PanicException, which
    # subclasses BaseException** — so `except Exception` does not catch it and
    # the hook exits 1. A Stop hook exiting non-zero TRAPS THE SESSION, the one
    # cost this file's header calls strictly worse than no hook. A subprocess
    # cannot do that: a broken openssl is a non-zero return code, not a panic
    # inside our own interpreter.
    def b64(raw):
        return base64.urlsafe_b64encode(raw).rstrip(b"=")

    now = int(time.time())
    aud = info.get("token_uri", "https://oauth2.googleapis.com/token")
    seg = b64(json.dumps({"alg": "RS256", "typ": "JWT"}).encode()) + b"." + b64(
        json.dumps({"iss": info["client_email"], "scope": scope, "aud": aud,
                    "iat": now, "exp": now + 3600}).encode())
    kd = tempfile.mkdtemp()
    kp = os.path.join(kd, "k.pem")
    try:
        fd = os.open(kp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w") as f:
            f.write(info["private_key"])
        p = subprocess.run(["openssl", "dgst", "-sha256", "-sign", kp],
                           input=seg, capture_output=True, timeout=15)
        if p.returncode != 0 or not p.stdout:
            raise RuntimeError("openssl sign failed: " + p.stderr.decode()[:200])
        assertion = seg + b"." + b64(p.stdout)
    finally:
        try:
            os.remove(kp)
            os.rmdir(kd)
        except OSError:
            pass

    body = urllib.parse.urlencode({
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": assertion.decode(),
    }).encode()
    req = urllib.request.Request(aud, data=body, method="POST", headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "fleet-manager-owner-review-hook/1.0"})
    ctx = (ssl.create_default_context(cafile=CA) if os.path.exists(CA)
           else ssl.create_default_context())
    op = urllib.request.build_opener(
        urllib.request.ProxyHandler({}), urllib.request.HTTPSHandler(context=ctx))
    return json.loads(op.open(req, timeout=NET_TIMEOUT).read())["access_token"]


def _extract(r, route):
    cand = (r.get("candidates") or [{}])[0]
    out = "".join(p.get("text", "")
                  for p in (cand.get("content") or {}).get("parts", []))
    um = dict(r.get("usageMetadata", {}))
    um["finishReason"] = cand.get("finishReason")  # truncation is countable
    um["route"] = route                            # which path answered, per firing
    return out.strip(), um


def _payload(text):
    return {
        "contents": [{"role": "user", "parts": [{"text":
            "The agent's reply to the owner, about to be delivered:\n\n" + text
            + "\n\nAsk your questions about it, or output exactly NO QUESTIONS."}]}],
        "systemInstruction": {"parts": [{"text": SYSTEM}]},
        # 4000, not 1200: on a thinking model the reasoning tokens draw from
        # the same budget, and the first live firing (2026-08-07) had its
        # question truncated mid-sentence at out_tokens=47.
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 4000},
    }


def _free_review(text):
    """AI Studio on the FREE key — the primary route, and it needs no auth chain.

    MEASURED 2026-08-08. Asked why this hook needed Google auth at all, the
    answer turned out to be "it does not". Given the same system prompt and the
    same reply, free-tier `gemini-flash-latest` returned **the same two findings**
    the Vertex/Pro reviewer had produced on the previous turn — the
    BaseException-swallows-SIGINT defect and an unfounded "openssl is present in
    all our environments" claim — in 7.1 s and 70 output tokens, at no cost.

    That is what findings § 1 already said and nobody had acted on: **the
    system prompt is the load-bearing component, not the model.** So the whole
    Railway → service-account → OAuth → JWT → openssl chain was buying a bigger
    model for a job the small one does.

    **Do not read that as "Vertex is fragile" — it is not, and the first version
    of this docstring implied it.** What was missing was the `google-auth`
    convenience LIBRARY, never the authentication: the service account, the
    OAuth token endpoint and Vertex itself were all present throughout.
    Re-measured cold 2026-08-08 with the credential cache deleted — Railway SA
    0.8 s, self-signed JWT → access token 0.1 s, Vertex `generateContent`
    HTTP 200 in 6.7 s, **7.5 s end to end**. Of the "three breakages" first
    claimed here, one was that missing library (a ten-minute fix), one was the
    uncountable-skip LOGGING defect which has nothing to do with auth, and one
    was self-inflicted by the first repair attempt reaching for `cryptography`.
    The free-first routing stands on its own merits — free, one header, and § 8
    says the model is not load-bearing at all — not on any unreliability of the
    credit-funded path.

    Consistent with docs/conventions/vertex-first-for-gemini.md, which reads
    "**free** key unless its daily cap is genuinely in the way" and reserves the
    Vertex default for volume, image and video work. One ~1 k-token call per turn
    is none of those. The daily cap IS the real risk for a per-turn hook, which
    is exactly why Vertex stays wired as the fallback below.
    Honest null: n=1 input, one run per model. Not a model comparison.
    """
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        return None
    r = _http("https://generativelanguage.googleapis.com/v1beta/models/"
              + FREE_MODEL + ":generateContent", _payload(text),
              {"x-goog-api-key": key, "Content-Type": "application/json"})
    return _extract(r, "free")


def _review(text):
    # Free first: no credentials to fetch, no key material, no subprocess. Vertex
    # is the fallback for exactly one failure — the requests-per-day cliff (429).
    try:
        got = _free_review(text)
        if got and got[0]:
            return got
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException:
        pass  # quota, network, shape — fall through to the credit-funded route

    info = _sa()
    if not info:
        return None
    token = _access_token(info)
    url = ("https://aiplatform.googleapis.com/v1/projects/" + info["project_id"]
           + "/locations/global/publishers/google/models/" + MODEL + ":generateContent")
    r = _http(url, _payload(text), {"Authorization": "Bearer " + token,
                                    "Content-Type": "application/json"})
    return _extract(r, "vertex")


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
        return  # one round per turn, ever — the loop guard. The only unlogged
                # exit, because it only happens on a pass that already logged.

    def rec(**kw):
        _log({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "session": data.get("session_id"), **kw})

    # EVERY other exit logs. The file header promised "silent-skip is still
    # countable" and it was not: _log sat downstream of every failure, so the
    # skips that mattered wrote nothing at all. MEASURED 2026-08-08 — the hook
    # had raised ModuleNotFoundError on google-auth at every single Stop since
    # it landed, and the telemetry directory held a credentials cache and not
    # one log line. A mechanism whose absence is invisible is indistinguishable
    # from one that is working.
    tp = data.get("transcript_path") or ""
    if not tp or not os.path.exists(tp):
        return rec(skip="no-transcript")
    text = _final_turn(tp)
    if not text or len(text) < MIN_CHARS:
        return rec(skip="reply-too-short", reply_chars=len(text or ""))
    # The model is BEST-EFFORT and strictly additive. Whatever happens here —
    # missing key, quota, network, a native panic — the fixed question below
    # still fires, so the mechanism has no dependency that can disable it.
    out, um, err = "", {}, None
    try:
        got = _review(text)
        if got:
            out, um = got
    except (KeyboardInterrupt, SystemExit):
        raise                                      # termination is not a defect
    except BaseException as exc:                   # creds, network, parse, timeout, native panic
        err = f"{type(exc).__name__}: {exc}"[:300]

    specifics = "" if out.upper().startswith("NO QUESTIONS") else out.strip()
    rec(reply_chars=len(text), route=um.get("route"), enriched=bool(specifics),
        prompt_tokens=um.get("promptTokenCount"),
        out_tokens=um.get("candidatesTokenCount"),
        finish=um.get("finishReason"), error=err)

    q = FIXED + ("\n\nAnd specifically:\n\n" + specifics if specifics else "")
    print(json.dumps({"decision": "block", "reason": REASON.format(q=q)}))


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        # Deliberate termination is NOT a defect. Swallowing it would make this
        # hook ignore the signals that shut a container down — fail-open is a
        # promise about bugs, not a licence to outlive the process that owns us.
        raise
    except BaseException:
        # BaseException rather than Exception, because MEASURED 2026-08-08 the
        # `cryptography` Rust layer raises PanicException whose MRO is
        # PanicException -> BaseException -> object. The narrower catch let it
        # escape and the hook exited 1, trapping the turn. "Any defect exits 0"
        # is only true if the catch covers everything a defect can raise — and
        # only safe if the two non-defects above are re-raised first.
        pass  # FAIL-OPEN: a review hook must never trap a session
    sys.exit(0)
