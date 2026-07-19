#!/usr/bin/env python3
"""gen_idea_backlog.py — harvest session-card 💡 ideas into a generated backlog index.

================================ PROVENANCE ================================
Why added : PR #349 planning-groom session-card 💡 idea, decided top pick of
            the 2026-07-19 evening re-groom (PR #377). Grooming passes had
            to hand-grep ~19–25 `.sessions/*.md` cards for 💡 blocks because
            card-ideas have no aggregated home — `docs/ideas/` holds lane
            seeds, not the session-ender tooling ideas, so a card-idea that
            never makes a planning doc silently rots. This harvester makes
            the candidate list machine-built: every groom starts from the
            generated backlog instead of a fresh hand-grep, and an idea that
            has sat ungroomed for N days announces itself.
NEIGHBORS (complement, never duplicate):
            - docs/planning/*.md groom sections are the JUDGMENT layer —
              humans/agents rank, park, drop. This script never judges an
              idea; it only lists and cross-references.
            - docs/ideas/ is the curated idea home for lane seeds; this
              reads only `.sessions/` cards and never writes there.
            - bootstrap.py check / the docs gate own doc validity; the
              generated file carries the standard badge + link so it passes
              the same gates as any doc.
Date      : 2026-07-19 (build-slice worker, model: fable-5, dispatched by
            the coordinator; fleet-manager PR #377)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it. Title extraction and
            groomed-detection are heuristics over hand-written markdown
            (first non-header bold span; >=60% title-token overlap with a
            planning doc), not a schema; it fails SAFE — advisory (exit 0
            on harvest, exit 1 only for --check drift / I/O), standalone,
            NOT wired into `bootstrap.py check`.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT DOES

  1. Scans `.sessions/*.md` for top-level bullets carrying the 💡 marker
     (`- 💡 …` / `- **💡 …`), capturing each bullet plus its indented
     continuation lines. Inline 💡 mentions mid-prose are NOT harvested.
  2. Extracts an idea title: the first bold span that is not the
     "Session idea (dedup-checked …)" header; falls back to the block's
     first ~90 characters.
  3. Cross-references each idea against `docs/planning/*.md` (excluding the
     generated backlog itself): an idea is `groomed → <doc>` when >=60% of
     its significant title tokens appear in a planning doc, else
     `ungroomed`. Ungroomed ideas older than --max-age-days get a ⚠ flag.
  4. Writes `docs/planning/idea-backlog.md` (or --stdout), newest card
     first, deterministic within a card.

USAGE
  python3 scripts/gen_idea_backlog.py                  # write the backlog
  python3 scripts/gen_idea_backlog.py --stdout         # print, write nothing
  python3 scripts/gen_idea_backlog.py --check          # exit 1 if committed file is stale
  python3 scripts/gen_idea_backlog.py --selfcheck      # offline assertions
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

MARKER = "\U0001f4a1"  # 💡
BULLET_RE = re.compile(r"^- (?:\*\*)?" + MARKER)
BOLD_RE = re.compile(r"\*\*(.+?)\*\*", re.DOTALL)
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")
HEADER_SPAN_RE = re.compile(r"^" + MARKER + r"?\s*Session idea", re.IGNORECASE)
GENERATED_AT_PREFIX = "> generated-at "

STOP_TOKENS = {
    "session", "idea", "ideas", "card", "cards", "this", "that", "with",
    "from", "into", "would", "could", "the", "and", "for",
}


def _tokens(title: str) -> list[str]:
    toks = [t for t in re.findall(r"[a-z0-9_]+", title.lower())
            if len(t) >= 4 and t not in STOP_TOKENS]
    # preserve order, dedupe
    seen: set[str] = set()
    out = []
    for t in toks:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def harvest_blocks(card_text: str) -> list[str]:
    """Return each 💡 top-level bullet block (bullet + indented continuations)."""
    blocks: list[str] = []
    lines = card_text.splitlines()
    i = 0
    while i < len(lines):
        if BULLET_RE.match(lines[i]):
            block = [lines[i]]
            i += 1
            while i < len(lines) and (lines[i].startswith("  ") and lines[i].strip()):
                block.append(lines[i])
                i += 1
            blocks.append("\n".join(block))
        else:
            i += 1
    return blocks


def extract_title(block: str) -> str:
    for span in BOLD_RE.findall(block):
        flat = " ".join(span.split())
        if HEADER_SPAN_RE.match(flat):
            continue
        return flat.rstrip(".").rstrip(":")
    flat = " ".join(block.split())
    flat = flat.lstrip("- ").replace("**", "")
    flat = flat.replace(MARKER, "").strip()
    # Drop a leading "Session idea (dedup-checked — …):" header so the
    # fallback shows the idea, not the dedup boilerplate.
    m = re.match(r"Session idea(?:\s*\([^)]*\))?\s*:?\s*", flat, re.IGNORECASE)
    if m and m.end() < len(flat):
        flat = flat[m.end():]
    return (flat[:90] + "…") if len(flat) > 90 else flat


def groom_pointer(title: str, planning_docs: dict[str, str]) -> str | None:
    toks = _tokens(title)
    if not toks:
        return None
    need = -(-len(toks) * 6 // 10)  # ceil(0.6 * n)
    if len(toks) >= 2:
        need = max(need, 2)  # a single generic token never grooms
    best: tuple[int, str] | None = None
    # Newest-dated doc first on ties (reverse name sort ~ reverse date sort).
    for name in sorted(planning_docs, reverse=True):
        text = planning_docs[name]
        hits = sum(1 for t in toks if t in text)
        if hits >= need and (best is None or hits > best[0]):
            best = (hits, name)
    return best[1] if best else None


def build_backlog(sessions_dir: Path, planning_dir: Path, out_name: str,
                  max_age_days: int, now: _dt.date) -> str:
    planning_docs = {
        p.name: p.read_text(encoding="utf-8").lower()
        for p in sorted(planning_dir.glob("*.md"))
        if p.name != out_name
    }
    rows: list[tuple[str, str, str, str, bool]] = []
    ungroomed_stale = 0
    cards = sorted(sessions_dir.glob("*.md"), reverse=True)
    for card in cards:
        m = DATE_RE.match(card.name)
        card_date = m.group(1) if m else "unknown"
        for block in harvest_blocks(card.read_text(encoding="utf-8")):
            title = extract_title(block)
            ptr = groom_pointer(title, planning_docs)
            stale = False
            if ptr is None and m:
                age = (now - _dt.date.fromisoformat(card_date)).days
                stale = age > max_age_days
                if stale:
                    ungroomed_stale += 1
            status = f"groomed → `{ptr}`" if ptr else "**ungroomed**"
            if stale:
                status += f" ⚠ >{max_age_days}d"
            rows.append((card_date, card.name, title, status, stale))

    n = len(rows)
    n_ungroomed = sum(1 for r in rows if "ungroomed" in r[3])
    lines = [
        "# Session-card idea backlog — GENERATED",
        "",
        "> **Status:** `audit`",
        ">",
        "> **GENERATED — do not hand-edit; regenerate with "
        "`python3 scripts/gen_idea_backlog.py`.** NOT SOURCE OF TRUTH — the",
        "> source cards (`.sessions/*.md`) and the planning docs' groom",
        "> sections win. Groomed-detection is a token-overlap heuristic",
        "> (Q-0105 unverified tier — see the script header).",
        ">",
        GENERATED_AT_PREFIX + _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        ">",
        f"> {n} idea block(s) across {len(cards)} card(s) · "
        f"{n_ungroomed} ungroomed · {ungroomed_stale} ungroomed "
        f"older than {max_age_days}d.",
        "",
        "| Card date | Source card | Idea | Groom status |",
        "|---|---|---|---|",
    ]
    for card_date, card_name, title, status, _ in rows:
        safe_title = title.replace("|", "\\|")
        lines.append(f"| {card_date} | `{card_name}` | {safe_title} | {status} |")
    lines.append("")
    return "\n".join(lines)


def _strip_volatile(text: str) -> str:
    return "\n".join(l for l in text.splitlines()
                     if not l.startswith(GENERATED_AT_PREFIX))


def selfcheck() -> int:
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        sess = root / ".sessions"
        plan = root / "planning"
        sess.mkdir()
        plan.mkdir()
        # Card 1: classic form, multi-line, bold header span + real title.
        (sess / "2026-07-19-alpha.md").write_text(
            "# card\n\n"
            "- \U0001f4a1 **Session idea (dedup-checked — stuff):**\n"
            "  **widget frobnicator checker.** It checks widget\n"
            "  frobnication end to end.\n"
            "- ⟲ **Previous-session review:** not an idea.\n",
            encoding="utf-8")
        # Card 2: leading-bold form (`- **💡 Session idea`), plus inline 💡
        # mid-prose that must NOT be harvested; old date for staleness flag.
        (sess / "2026-07-01-beta.md").write_text(
            "# card\n\n"
            "the 8 harvested \U0001f4a1 blocks are prose, not a bullet.\n"
            "- **\U0001f4a1 Session idea (dedup-checked):** teach the parser\n"
            "  to **consult the gizmo fence directly** for verdicts.\n",
            encoding="utf-8")
        # Planning doc grooms the widget idea only.
        (plan / "2026-07-19-slices.md").write_text(
            "## ranked\n1. **widget frobnicator checker** · S — build it\n",
            encoding="utf-8")

        now = _dt.date(2026, 7, 19)
        out = build_backlog(sess, plan, "idea-backlog.md", 2, now)

        assert "widget frobnicator checker" in out, "title extraction failed"
        assert "groomed → `2026-07-19-slices.md`" in out, "groom pointer failed"
        assert "consult the gizmo fence directly" in out, "leading-bold form missed"
        assert "prose, not a bullet" not in out, "inline \U0001f4a1 wrongly harvested"
        assert "**ungroomed** ⚠ >2d" in out, "stale-ungroomed flag failed"
        assert "not an idea" not in out, "non-\U0001f4a1 bullet harvested"
        # Determinism (minus the volatile generated-at line).
        out2 = build_backlog(sess, plan, "idea-backlog.md", 2, now)
        assert _strip_volatile(out) == _strip_volatile(out2), "non-deterministic"
        # 2 ideas, 1 ungroomed, 1 stale in the summary line.
        assert "2 idea block(s) across 2 card(s) · 1 ungroomed · 1 ungroomed" in out
    print("selfcheck: OK — 6 harvest/format assertions + determinism")
    return 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="harvest session-card \U0001f4a1 ideas")
    ap.add_argument("--sessions-dir", default=".sessions")
    ap.add_argument("--planning-dir", default="docs/planning")
    ap.add_argument("--out", default="docs/planning/idea-backlog.md")
    ap.add_argument("--max-age-days", type=int, default=2)
    ap.add_argument("--stdout", action="store_true", help="print, write nothing")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the committed backlog is stale vs a fresh harvest")
    ap.add_argument("--selfcheck", action="store_true")
    args = ap.parse_args(argv)

    if args.selfcheck:
        return selfcheck()

    sessions_dir = Path(args.sessions_dir)
    planning_dir = Path(args.planning_dir)
    out_path = Path(args.out)
    if not sessions_dir.is_dir():
        print(f"ERROR: sessions dir not found: {sessions_dir}", file=sys.stderr)
        return 1

    content = build_backlog(sessions_dir, planning_dir, out_path.name,
                            args.max_age_days, _dt.datetime.now(_dt.timezone.utc).date())
    if args.stdout:
        print(content)
        return 0
    if args.check:
        if not out_path.exists():
            print(f"CHECK: {out_path} missing — run the generator")
            return 1
        if _strip_volatile(out_path.read_text(encoding="utf-8")) != _strip_volatile(content):
            print(f"CHECK: {out_path} is stale vs a fresh harvest — regenerate")
            return 1
        print("CHECK: backlog current")
        return 0
    out_path.write_text(content, encoding="utf-8")
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
