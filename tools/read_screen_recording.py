#!/usr/bin/env python3
"""Send a video to Gemini on Vertex at a chosen sampling rate.

Gemini samples video at 1 fps by default. Vertex exposes an override via
`videoMetadata.fps` on the same part, which is the variable under test here:
a fast scroll at 1 fps sees almost nothing, and the question is whether
raising the rate recovers the skipped content.

usage: read_screen_recording.py <video> <fps|default> <prompt>
       Start at fps=8 for any scroll — the 1 fps default sees ~63% of one.
       Full rationale: docs/conventions/reading-screen-recordings.md
"""
import base64, json, os, ssl, sys, urllib.error, urllib.request

CA = "/root/.ccr/ca-bundle.crt"
SA = os.environ.get("VERTEX_SA", "")  # pull GEMINI_VERTEX_SA_JSON from Railway;
                                      # see docs/conventions/vertex-first-for-gemini.md § 1
MODEL = "gemini-3.1-pro-preview"
VIDEO, FPS, PROMPT = sys.argv[1], sys.argv[2], sys.argv[3]


def token():
    from google.auth.transport.requests import Request as GR
    from google.oauth2 import service_account
    import requests
    info = json.load(open(SA))
    c = service_account.Credentials.from_service_account_info(
        info, scopes=["https://www.googleapis.com/auth/cloud-platform"])
    s = requests.Session(); s.trust_env = False; s.verify = CA
    c.refresh(GR(session=s))
    return c.token, info["project_id"]


tok, proj = token()
part = {"inlineData": {"mimeType": "video/mp4",
                       "data": base64.b64encode(open(VIDEO, "rb").read()).decode()}}
if FPS != "default":
    part["videoMetadata"] = {"fps": float(FPS)}

url = (f"https://aiplatform.googleapis.com/v1/projects/{proj}"
       f"/locations/global/publishers/google/models/{MODEL}:generateContent")
payload = {"contents": [{"role": "user", "parts": [part, {"text": PROMPT}]}],
           "generationConfig": {"temperature": 0.1, "maxOutputTokens": 16000}}
req = urllib.request.Request(
    url, data=json.dumps(payload).encode(),
    headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json"},
    method="POST")
ctx = ssl.create_default_context(cafile=CA)
op = urllib.request.build_opener(urllib.request.ProxyHandler({}),
                                 urllib.request.HTTPSHandler(context=ctx))
try:
    r = json.loads(op.open(req, timeout=1200).read())
except urllib.error.HTTPError as e:
    raise SystemExit(f"HTTP {e.code}\n{e.read().decode()[:1500]}")
cand = (r.get("candidates") or [{}])[0]
print("".join(p.get("text", "") for p in (cand.get("content") or {}).get("parts", [])))
um = r.get("usageMetadata", {})
print(f"\n=== fps={FPS} · prompt tokens {um.get('promptTokenCount')} "
      f"(video share ≈ frames×~300) · output {um.get('candidatesTokenCount')} ===",
      file=sys.stderr)
