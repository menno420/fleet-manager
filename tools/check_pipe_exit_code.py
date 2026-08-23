#!/usr/bin/env python3
"""TRAP-002 checker — an exit code read after a pipe, in EXECUTABLE surfaces.

`docs/traps.md` TRAP-002: after `a | b`, `$?` is **b's** exit code. The failure
is silent and inverted — the real command fails, the check reports success.

The `exit-code-after-a-pipe` doc-route catches this while an agent is composing
a command. This checker closes the other half: the same bug **committed** into
automation, where it silently passes CI for as long as it lives there. Roadmap
§ 5.4's lifecycle ends at *deterministic checker where possible*, and this is
the one registered trap mechanical enough to reach that end.

SCOPE, deliberately narrow so the instrument stays trustworthy:
  * `.github/workflows/*.yml|yaml` and `*.sh` — surfaces that EXECUTE.
  * Prose is NOT scanned. Session cards and findings quote this trap as an
    example constantly (fm #915 counted 26 of 389 cards); flagging those would
    make the checker cry wolf on its own documentation.

NOT flagged, because these make `$?` correct or unknowable:
  * `PIPESTATUS` present — the documented fix.
  * `set -o pipefail` / `set -eo pipefail` in the same file — `$?` then reflects
    the pipeline's rightmost non-zero status.
  * A `||` or `&&` pipe-less short-circuit; only a real `|` counts (`||` is
    excluded explicitly).

Exit 0 clean; exit 1 on findings under --strict.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GLOBS = (".github/workflows/*.yml", ".github/workflows/*.yaml", "**/*.sh")
SKIP_DIRS = {".git", "node_modules", ".substrate", "dist", "build"}

# A real pipe: `|` not part of `||`, and not inside an obvious regex/alternation
# character class. Conservative — we would rather miss than misfire.
PIPE = re.compile(r"(?<!\|)\|(?!\|)")
READS_STATUS = re.compile(r"\$\?")
EXEMPT = re.compile(r"PIPESTATUS|pipefail")
# How far after the pipe a `$?` still plausibly refers to it.
WINDOW = 4


def candidates() -> list[Path]:
    out: list[Path] = []
    for pattern in GLOBS:
        for p in REPO.glob(pattern):
            if not p.is_file():
                continue
            if any(part in SKIP_DIRS for part in p.parts):
                continue
            out.append(p)
    return sorted(set(out))


def scan(path: Path) -> list[tuple[int, str]]:
    try:
        text = path.read_text(errors="replace")
    except OSError:
        return []
    if EXEMPT.search(text):
        return []                      # file-level fix in place
    lines = text.splitlines()
    hits: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if not PIPE.search(line):
            continue
        window = lines[i:i + WINDOW + 1]
        for j, follow in enumerate(window):
            if j == 0 and not READS_STATUS.search(follow):
                continue
            if READS_STATUS.search(follow):
                hits.append((i + 1, stripped[:120]))
                break
    return hits


def main() -> int:
    strict = "--strict" in sys.argv
    findings: list[str] = []
    scanned = 0
    for path in candidates():
        scanned += 1
        for lineno, snippet in scan(path):
            rel = path.relative_to(REPO)
            findings.append(f"{rel}:{lineno}: pipes, then reads `$?` — {snippet}")

    for f in findings:
        print(f"ERROR  {f}")
    print(
        f"\ncheck_pipe_exit_code: {scanned} executable file(s) scanned · "
        f"{len(findings)} finding(s)"
        + ("" if findings else " — CLEAN")
    )
    if findings:
        print(
            "FIX: redirect instead of piping (`cmd > out.txt 2>&1; echo $?`), "
            "or use `${PIPESTATUS[0]}`, or `set -o pipefail`. "
            "Trap: docs/traps.md TRAP-002."
        )
    return 1 if (findings and strict) else 0


if __name__ == "__main__":
    sys.exit(main())
