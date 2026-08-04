#!/usr/bin/env python3
"""Delegate a read-heavy job to Gemini, then verify every citation it returns.

Why this exists (2026-08-05). A free-tier `GEMINI_API_KEY` reaches
`gemini-3.6-flash` at a 1M-token input window, which makes whole-corpus reads
— every session card, every bench result — cheap in a way they have never been
here. The catch was measured the same day: asked to build a dashboard over
substrate-kit, Gemini invented 18 plausible "decisions" while the real
`docs/decisions.md` (10 entries) sat unread in its own workspace. Fluent,
confident, wrong.

So the contract this tool enforces is not "trust the summary". It is:

    delegate the reading, never the record — every claim ships a
    file + line + verbatim quote, and this tool checks each one
    against the tree before a human ever reads it.

A claim whose quote is not in the file at the line it named is dropped, loudly.
That turns verification from a judgement call into a string comparison, which
is the only reason delegating to a model with no stake in our correctness is
safe at all. It is PL-014 pointed at a subcontractor: the claim carries its
instrument.

Usage:

    python3 tools/gemini_delegate.py bundle  --glob '.sessions/*.md' [--repo P]
    python3 tools/gemini_delegate.py run     --glob '.sessions/*.md' \
        --task-file task.md [--repo P] [-o out.json] [--model M]
    python3 tools/gemini_delegate.py verify  out.json [--repo P]

`bundle` prints the corpus size and its exact token count (measured via the
API's own counter, not estimated) and writes nothing — run it first to see
whether a job fits. `run` bundles, calls, verifies, and writes a JSON report.
`verify` re-checks a saved report against the current tree, which is how a
stale finding gets caught after the repo moves.

Stdlib only, direct egress (the proxied path 403s), fail-loud on a missing key.

Reliability: UNVERIFIED beyond its first run — confirm the verifier's verdicts
against ground truth a few times before trusting a green report. Delete this
tool if it proves unreliable over multiple sessions.
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

API_ROOT = "https://generativelanguage.googleapis.com/v1beta"
DEFAULT_MODEL = "gemini-3.6-flash"

# The citation contract, enforced structurally rather than asked for politely.
# Every finding must carry at least one citation; every citation must name a
# file, a line, and the text as it appears there.
RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "findings": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "claim": {"type": "string"},
                    "detail": {"type": "string"},
                    "category": {"type": "string"},
                    "citations": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "file": {"type": "string"},
                                "line": {"type": "integer"},
                                "quote": {"type": "string"},
                            },
                            "required": ["file", "line", "quote"],
                        },
                    },
                },
                "required": ["claim", "detail", "citations"],
            },
        },
    },
    "required": ["findings"],
}

CONTRACT = """\
You are reading a corpus assembled from a real repository. Every file is
delimited by a `===== FILE: <path> =====` marker and every content line is
prefixed with its exact line number in that file.

THE CONTRACT — this is the whole job, not a formatting preference:

1. Every finding you report MUST carry at least one citation: the file path
   exactly as it appears in the FILE marker, the line number as printed, and
   the quote EXACTLY as it appears on that line (copy it, do not retype or
   tidy it).
1b. A quote is ONE line and AT MOST 200 characters. Where the evidence runs
   long, quote the single most load-bearing fragment of the single most
   load-bearing line — never stitch text from several places into one quote,
   and never smooth a passage while copying it. This limit is not tidiness:
   long quotes measurably get reconstructed rather than copied (2026-08-05 —
   both rejected citations in the tool's first run quoted 699 and 1392
   characters, each stitching real fragments into a passage that appears
   nowhere in the file). Short quotes are copied. Long ones get rewritten.
2. Quotes are checked mechanically against the repository after you answer.
   A finding whose quote does not appear at the line it names is DISCARDED,
   and a discarded finding is worse than no finding at all.
3. Report only what the corpus says. If the corpus does not support a claim,
   omit the claim. Do NOT infer, reconstruct, or fill gaps with plausible
   material — an invented finding survives review far longer than an absent
   one, which is why it costs more.
4. If you find nothing, return an empty findings list. An honest null is a
   correct answer here.
"""


def _key() -> str:
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not key:
        sys.exit("GEMINI_API_KEY is not set in this environment")
    return key


def _post(url: str, payload: dict, retries: int = 3) -> dict:
    """POST JSON over direct egress — the proxied path 403s for this host."""
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    # Empty ProxyHandler = ignore HTTPS_PROXY/HTTP_PROXY from the environment.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(request, timeout=900) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as error:
        body = error.read().decode()[:600]
        if error.code == 429 and retries > 0:
            # The free tier meters input tokens per minute and tells you exactly
            # how long to wait. Honour its number rather than guessing, and say
            # so out loud — a silent sleep looks like a hang.
            match = re.search(r"retry in ([\d.]+)s", body, re.IGNORECASE)
            delay = min(float(match.group(1)) + 3 if match else 65.0, 120.0)
            print(f"  quota: waiting {delay:.0f}s then retrying", file=sys.stderr)
            time.sleep(delay)
            return _post(url, payload, retries - 1)
        sys.exit(f"API error {error.code}: {body}")


def collect(repo: pathlib.Path, globs: list[str]) -> list[pathlib.Path]:
    paths: list[pathlib.Path] = []
    for pattern in globs:
        paths.extend(sorted(repo.glob(pattern)))
    return [p for p in paths if p.is_file()]


def build_bundle(repo: pathlib.Path, paths: list[pathlib.Path]) -> str:
    chunks: list[str] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue  # fail open — an unreadable file is not a verdict
        relative = path.relative_to(repo).as_posix()
        numbered = "\n".join(
            f"{index}: {line}" for index, line in enumerate(text.splitlines(), 1)
        )
        chunks.append(f"===== FILE: {relative} =====\n{numbered}")
    return "\n\n".join(chunks)


def count_tokens(model: str, text: str) -> int:
    url = f"{API_ROOT}/models/{model}:countTokens?key={_key()}"
    payload = {"contents": [{"parts": [{"text": text}]}]}
    return _post(url, payload).get("totalTokens", -1)


def chunk_paths(
    repo: pathlib.Path, paths: list[pathlib.Path], budget: int
) -> list[list[pathlib.Path]]:
    """Split the corpus into batches that fit the free tier's input ceiling.

    Measured 2026-08-05: the model's window is 1,048,576 tokens, but the free
    tier meters `generate_content_free_tier_input_token_count` at **250,000 per
    minute**. The window is a capability; the quota is the real constraint, and
    they are two different numbers. Budget defaults below the ceiling because a
    batch that overshoots costs a full minute of backoff.

    Sizing uses a local chars-per-token estimate (measured 3.07 on this repo's
    session cards, taken conservatively at 2.7) rather than a countTokens call
    per candidate batch — the estimate is cheap and only has to be safe.
    """
    chunks: list[list[pathlib.Path]] = []
    current: list[pathlib.Path] = []
    used = 0
    for path in paths:
        try:
            size = len(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError):
            continue
        cost = int(size / 2.7) + 32  # +32 for the FILE marker and numbering
        if current and used + cost > budget:
            chunks.append(current)
            current, used = [], 0
        current.append(path)
        used += cost
    if current:
        chunks.append(current)
    return chunks


def generate(model: str, task: str, bundle: str) -> tuple[dict, dict]:
    url = f"{API_ROOT}/models/{model}:generateContent?key={_key()}"
    payload = {
        "contents": [{"parts": [{"text": f"{CONTRACT}\n\n{task}\n\n{bundle}"}]}],
        "generationConfig": {
            "temperature": 0,  # deterministic: this is extraction, not writing
            "maxOutputTokens": 65536,
            "responseMimeType": "application/json",
            "responseSchema": RESPONSE_SCHEMA,
        },
    }
    response = _post(url, payload)
    usage = response.get("usageMetadata", {})
    candidates = response.get("candidates", [])
    if not candidates:
        sys.exit(f"no candidate returned: {json.dumps(response)[:400]}")
    candidate = candidates[0]
    # `.get("content", {})` returns None when the key is present and null, which
    # is what a safety block or a non-STOP finish actually sends — so the `or {}`
    # is load-bearing, not belt-and-braces. Same review.
    content = candidate.get("content") or {}
    text = "".join(part.get("text", "") for part in content.get("parts") or [])
    if candidate.get("finishReason") not in (None, "STOP"):
        # Truncation is a real outcome, not a detail to swallow: a MAX_TOKENS
        # cut yields invalid JSON and the run must be re-scoped, not retried.
        print(
            f"warning: finishReason={candidate.get('finishReason')} — output may "
            "be truncated; narrow the glob or split the job",
            file=sys.stderr,
        )
    try:
        return json.loads(text), usage
    except json.JSONDecodeError as error:
        sys.exit(f"model returned non-JSON ({error}): {text[:400]}")


def _normalise(text: str) -> str:
    """Collapse whitespace, case, and markdown decoration.

    Decoration is stripped because it is not evidence: the same idea is written
    `## 💡 Session idea` on one card and `- **💡 Session idea:**` on another, and
    a model quoting one style while reading the other has still located the
    right text. Measured 2026-08-05: six of six rejects in the second run
    diverged at exactly four characters — the bullet-vs-heading marker — while
    the sentence after it matched perfectly.

    Stripping is applied to BOTH sides, so it can only remove formatting noise.
    Invented content still fails: a fabricated passage does not become real by
    losing its asterisks.
    """
    text = re.sub(r"[*`_#>]+", "", text)
    text = re.sub(r"^\s*[-+]\s+", " ", text, flags=re.MULTILINE)
    return re.sub(r"\s+", " ", text).strip().lower()


def verify_citation(repo: pathlib.Path, citation: dict, window: int = 4) -> dict:
    """Check one citation against the tree. Returns a verdict dict.

    The line number is checked with a small window rather than exactly: a model
    that copies the right text but is off by a line has still located real
    evidence, while one that invents the text has not. The QUOTE is the
    load-bearing half — an off-by-one is a slip, a wrong quote is a fabrication.
    """
    # The path comes from the model, so it is untrusted input: pathlib discards
    # the left operand when the right is absolute (`repo / "/etc/passwd"` IS
    # "/etc/passwd"), and `../` climbs out. Resolve, then confine to the repo.
    # Found by Gemini reviewing this file, 2026-08-05.
    path = (repo / citation.get("file", "")).resolve()
    if not path.is_relative_to(repo.resolve()):
        return {"ok": False, "reason": "path escapes the repository root"}
    if not path.is_file():
        return {"ok": False, "reason": "file does not exist"}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return {"ok": False, "reason": "file unreadable"}
    line_number = citation.get("line", 0)
    quote = _normalise(citation.get("quote", ""))
    if not quote:
        return {"ok": False, "reason": "empty quote"}
    low = max(0, line_number - 1 - window)
    high = min(len(lines), line_number + window)
    if quote in _normalise(" ".join(lines[low:high])):
        exact = 1 <= line_number <= len(lines) and quote in _normalise(
            lines[line_number - 1]
        )
        return {"ok": True, "reason": "exact" if exact else f"within ±{window} lines"}
    whole = _normalise(" ".join(lines))
    if quote in whole:
        return {"ok": True, "reason": "found in file, wrong line"}
    # Substring matching alone cannot tell a MARKER mismatch from a FABRICATION,
    # and the difference is the whole point. Coverage can: measured 2026-08-05,
    # a quote differing only in its `## 💡 Session idea` vs `- **💡 Session
    # idea:**` marker still shares 93% of its characters with one contiguous run
    # of the file, while the two genuinely stitched passages shared 12% and 29%.
    # So accept on one long contiguous run covering most of the quote, and let
    # anything reconstructed fall through.
    match = difflib.SequenceMatcher(None, quote, whole, autojunk=False).find_longest_match(
        0, len(quote), 0, len(whole)
    )
    coverage = match.size / len(quote)
    if coverage >= 0.85 and match.size >= 60:
        return {"ok": True, "reason": f"contiguous run covers {coverage:.0%} of quote"}
    return {
        "ok": False,
        "reason": f"quote not present in file (longest run covers {coverage:.0%})",
    }


def verify_report(repo: pathlib.Path, report: dict) -> dict:
    kept, dropped = [], []
    for finding in report.get("findings", []):
        verdicts = [
            {**citation, **verify_citation(repo, citation)}
            for citation in finding.get("citations", [])
        ]
        finding = {**finding, "citations": verdicts}
        (kept if any(v["ok"] for v in verdicts) else dropped).append(finding)
    return {"verified": kept, "rejected": dropped}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("bundle", "run", "verify"))
    parser.add_argument("report", nargs="?", help="report path (verify only)")
    parser.add_argument("--repo", default=".", help="repository root")
    parser.add_argument("--glob", action="append", default=[], help="repeatable")
    parser.add_argument("--task-file", help="file holding the job description")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("-o", "--out", default="gemini-report.json")
    parser.add_argument(
        "--max-input-tokens",
        type=int,
        default=200_000,
        help="per-call input budget (free tier meters 250k/min; stay under)",
    )
    args = parser.parse_args()

    repo = pathlib.Path(args.repo).resolve()

    if args.command == "verify":
        if not args.report:
            return parser.error("verify needs a report path")
        result = verify_report(repo, json.loads(pathlib.Path(args.report).read_text()))
        print(f"verified {len(result['verified'])} · rejected {len(result['rejected'])}")
        return 1 if result["rejected"] else 0

    if not args.glob:
        return parser.error("--glob is required")
    paths = collect(repo, args.glob)
    bundle = build_bundle(repo, paths)
    print(f"bundle: {len(paths)} files · {len(bundle)} chars", file=sys.stderr)

    if args.command == "bundle":
        print(f"tokens: {count_tokens(args.model, bundle)}")
        return 0

    if not args.task_file:
        return parser.error("run needs --task-file")
    task = pathlib.Path(args.task_file).read_text(encoding="utf-8")

    batches = chunk_paths(repo, paths, args.max_input_tokens)
    findings: list[dict] = []
    totals = {"promptTokenCount": 0, "candidatesTokenCount": 0}
    for index, batch in enumerate(batches, 1):
        print(f"batch {index}/{len(batches)} · {len(batch)} files", file=sys.stderr)
        report, usage = generate(args.model, task, build_bundle(repo, batch))
        findings.extend(report.get("findings", []))
        for metric in totals:
            totals[metric] += usage.get(metric, 0)
        if index < len(batches):
            # Space the batches so the per-minute input meter refills rather
            # than 429-ing every call and paying the backoff anyway.
            time.sleep(62)

    result = verify_report(repo, {"findings": findings})
    result["_meta"] = {
        "model": args.model,
        "files": len(paths),
        "batches": len(batches),
        "usage": totals,
        "globs": args.glob,
    }
    pathlib.Path(args.out).write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(
        f"verified {len(result['verified'])} · rejected {len(result['rejected'])} "
        f"· tokens in/out {totals['promptTokenCount']}/"
        f"{totals['candidatesTokenCount']} → {args.out}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
