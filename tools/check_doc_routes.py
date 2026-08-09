#!/usr/bin/env python3
"""Validate .claude/hooks/doc-routes.json — the table the doc-routing hook reads.

A routing table decays in a specific way: the doc gets rewritten, moved or
narrowed, the route keeps pointing at it, and the hook confidently sends a
session to a page that no longer covers the thing it triggered on. That is
worse than no hook, because the session stops looking.

So the coverage check is the point of this script: **at least one of a route's
`when` patterns must actually occur in at least one of its docs.** A doc that
stops covering its trigger fails here instead of misrouting a session.

Two tiers, deliberately separated (see
docs/findings/2026-08-05-foundation-continuation.md § 5 — deterministic checks
belong on a gate, judgement calls do not):

  ERRORS   deterministic — bad regex, missing file, no coverage. `--strict`
           exits 1 on any of these.
  NOTES    informational — capability/method docs that no route and no boot
           file mentions. Printed, never fatal; deciding whether a doc deserves
           a route is a judgement, and a judgement wired to a gate produces an
           agent inventing routes to make a number go green.

Usage:  python3 tools/check_doc_routes.py [--strict]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TABLE = REPO / ".claude/hooks/doc-routes.json"

# The docs whose whole job is telling a session what it can do and how. If one
# of these is reachable from neither a route nor the boot file, a session finds
# it only by luck.
DOC_SET = ["docs/providers/*.md", "docs/conventions/*.md"]
DOC_EXTRA = ["docs/CAPABILITIES.md", "docs/execution-surfaces.md"]
# Files that count as "a session would be pointed here anyway".
REFERRERS = [".claude/CLAUDE.md", "docs/providers/README.md", "docs/SKILLS-local.md"]


def main() -> int:
    strict = "--strict" in sys.argv
    errors: list[str] = []
    notes: list[str] = []

    try:
        table = json.loads(TABLE.read_text())
    except Exception as exc:
        print(f"ERROR  {TABLE.relative_to(REPO)} does not parse: {exc}")
        return 1

    routes = table.get("routes")
    if not isinstance(routes, list) or not routes:
        print("ERROR  no `routes` list")
        return 1

    seen_ids: set[str] = set()
    routed_docs: set[str] = set()

    for i, route in enumerate(routes):
        rid = route.get("id") or f"<route {i}>"
        if rid in seen_ids:
            errors.append(f"{rid}: duplicate id")
        seen_ids.add(rid)

        if not (route.get("says") or "").strip():
            errors.append(f"{rid}: empty `says` — a bare path teaches nothing")

        # PROMPT ROUTES admission bar, rule 4 (doc-routes.json § _comment).
        # A prompt route must list UserPromptSubmit and nothing else. Mixing in
        # tool events lets any Bash/Grep/Read carrying the trigger word spend the
        # once-per-session budget before the owner's message can — measured
        # 2026-08-09, when a `grep repo-spider-swing` consumed this exact route.
        tools = route.get("tools") or []
        if "UserPromptSubmit" in tools and len(tools) > 1:
            others = ", ".join(t for t in tools if t != "UserPromptSubmit")
            base = rid[: -len("-prompt")] if rid.endswith("-prompt") else rid
            errors.append(
                f"{rid}: PROMPT-ROUTE BAR 4 — `tools` mixes UserPromptSubmit with "
                f"{others}. A tool call carrying the trigger word then burns the "
                f"once-per-session dedup before a prompt ever fires, converting a "
                f"false fire into false silence exactly when the route matters. "
                f"Split into two routes with distinct ids (`{base}` for the tool "
                f"events, `{base}-prompt` for UserPromptSubmit) so the dedup "
                f"counters are independent."
            )

        patterns = route.get("when") or []
        if not patterns:
            errors.append(f"{rid}: no `when` patterns")
        compiled = []
        for pat in patterns:
            try:
                compiled.append(re.compile(pat, re.I))
            except re.error as exc:
                errors.append(f"{rid}: pattern {pat!r} does not compile — {exc}")

        docs = route.get("docs") or []
        if not docs:
            errors.append(f"{rid}: no `docs`")
        bodies = []
        for rel in docs:
            path = REPO / rel
            if not path.is_file():
                errors.append(f"{rid}: docs path does not exist — {rel}")
                continue
            routed_docs.add(rel)
            bodies.append(path.read_text(errors="replace"))

        if compiled and bodies:
            if not any(rx.search(b) for rx in compiled for b in bodies):
                errors.append(
                    f"{rid}: COVERAGE — none of its {len(compiled)} patterns "
                    f"appears in {', '.join(docs)}. Either the doc no longer "
                    f"covers this trigger, or the route points at the wrong doc."
                )

    # Reverse coverage: which capability/method docs is nothing pointing at?
    candidates: set[str] = set(DOC_EXTRA)
    for pattern in DOC_SET:
        for path in REPO.glob(pattern):
            candidates.add(str(path.relative_to(REPO)))
    candidates -= set(REFERRERS)  # an index does not need routing to itself
    referrer_text = "\n".join(
        (REPO / r).read_text(errors="replace") for r in REFERRERS if (REPO / r).is_file()
    )
    for rel in sorted(candidates):
        if rel in routed_docs or Path(rel).name in referrer_text or rel in referrer_text:
            continue
        notes.append(f"unrouted: {rel} — no route triggers it, no boot file names it")

    for note in notes:
        print(f"NOTE   {note}")
    for err in errors:
        print(f"ERROR  {err}")

    print(
        f"\n{len(routes)} routes · {len(routed_docs)} docs routed · "
        f"{len(errors)} errors · {len(notes)} notes"
    )
    return 1 if (errors and strict) else 0


if __name__ == "__main__":
    sys.exit(main())
