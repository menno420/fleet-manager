#!/usr/bin/env python3
"""Suite for `.claude/hooks/owner_review.py` — the two 2026-09-02 corrections.

Same shape as `test_codex_round_guard.py`: the executable prints its own case
count, so no prose restates a number that goes stale. The motivating cases:

* **The 503 retry.** Both firings of the session that measured it logged
  `HTTPError: HTTP Error 503: Service Unavailable` — Google's free tier
  shedding load, answered in 1–6 s, the next call succeeding. One unretried
  attempt lost the enrichment both times. `_free_review` now retries a 503
  twice and records `attempts`; a 429 (a daily cap, which six seconds do not
  clear) is not retried; a third 503 propagates so `main()` logs it.
* **The `REASON` text.** The owner has already seen the reply when the Stop
  block fires, so the text must ask for only what is new and must not ask the
  session to "amend the reply" — that instruction re-sent every message twice.

The network layer is stubbed at `_http`; nothing here calls Google, and
`time.sleep` is replaced so the backoff costs no wall-clock.
"""

from __future__ import annotations

import io
import os
import sys
import urllib.error
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / ".claude" / "hooks"))
import owner_review as hook  # noqa: E402

passed = failed = 0


def check(name: str, got, want) -> None:
    global passed, failed
    ok = got == want
    passed += ok
    failed += not ok
    print(f"  {'ok ' if ok else 'FAIL'}  {name}" + ("" if ok else f"  (got {got!r}, want {want!r})"))


OK_BODY = {
    "candidates": [{"content": {"parts": [{"text": "NO QUESTIONS"}]},
                    "finishReason": "STOP"}],
    "usageMetadata": {"promptTokenCount": 10, "candidatesTokenCount": 2},
}


def stub(codes: tuple[int, ...]):
    """An `_http` that answers each call with the next status code (200 = OK body)."""
    it = iter(codes)
    calls: list[int] = []

    def _http(url, payload, headers):
        code = next(it)
        calls.append(code)
        if code == 200:
            return OK_BODY
        raise urllib.error.HTTPError(url, code, "stubbed", {}, io.BytesIO(b"{}"))

    _http.calls = calls  # type: ignore[attr-defined]
    return _http


def attempt(codes: tuple[int, ...]):
    hook._http = stub(codes)
    try:
        _out, um = hook._free_review("x" * 500)
        return f"attempts={um['attempts']}"
    except urllib.error.HTTPError as exc:
        return f"HTTPError {exc.code}"


os.environ["GEMINI_API_KEY"] = "stub-key-for-the-suite"
slept: list[float] = []
hook.time.sleep = lambda s: slept.append(s)

print("retry on 503")
check("200 first time: one attempt", attempt((200,)), "attempts=1")
check("503 then 200: two attempts", attempt((503, 200)), "attempts=2")
check("503, 503, 200: three attempts (the cap)", attempt((503, 503, 200)), "attempts=3")
check("backoff was 2 s then 4 s", slept[-2:], [2, 4])
check("three 503s: the third propagates", attempt((503, 503, 503)), "HTTPError 503")
check("... after exactly RETRIES+1 calls", len(hook._http.calls), hook.RETRIES + 1)
check("429 is not retried", attempt((429,)), "HTTPError 429")
check("... one call only", len(hook._http.calls), 1)
check("500 is not retried either", attempt((500,)), "HTTPError 500")
check("worst case fits the 120 s registration",
      (hook.RETRIES + 1) * hook.NET_TIMEOUT + hook.BACKOFF_S * sum(range(1, hook.RETRIES + 1)) < 120,
      True)

print("no key")
os.environ.pop("GEMINI_API_KEY", None)
hook._http = stub((200,))
try:
    hook._free_review("x" * 500)
    check("missing key raises (countable), never returns None", "returned", "raised no-key")
except RuntimeError as exc:
    check("missing key raises (countable), never returns None",
          str(exc).startswith("no-key:"), True)
check("... and made no network call", len(hook._http.calls), 0)

print("the REASON text")
reason = hook.REASON
check("says the owner has already seen the reply", "ALREADY SEEN THAT REPLY" in reason, True)
check("asks for only what is new", "ONLY what is new" in reason, True)
check("no longer asks to amend the reply", "amend the reply" in reason, False)
check("no longer asks to answer IN the reply", "IN\nthe reply" in reason or "IN the reply" in reason, False)
check("still carries the [survived] marker", "[survived]" in reason, True)
check("still carries the question slot", "{q}" in reason, True)
check("the fixed question is still question 1", hook.FIXED.startswith("1. What made you draw"), True)

print()
print(f"{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
