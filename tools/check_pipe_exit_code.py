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

NOT flagged, because these make `$?` correct:
  * `PIPESTATUS` read within the window — the documented fix at the use site.
  * `set -o pipefail` **enabled on a non-comment line ABOVE the pipe** — `$?`
    then reflects the pipeline's rightmost non-zero status. Checked positionally
    on purpose: an earlier version substring-searched the WHOLE file, so
    `pipefail` set *after* the pipe, inside a subshell, or merely named in a
    comment silently exempted every pipe in the file. That was miss-biased well
    past what "exempt the fix" needs.
  * A `||` short-circuit; only a real `|` counts.

Static shell analysis has real limits and this does not pretend otherwise: a
`pipefail` set in a sourced file, or inside a function defined above but called
below, is not tracked. The bias is still toward MISSING a real instance rather
than crying wolf — an instrument nobody trusts gets ignored — but the exemption
is now positional rather than "the word appears somewhere".

Exit 0 clean; exit 1 on findings under --strict.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GLOBS = (".github/workflows/*.yml", ".github/workflows/*.yaml", "**/*.sh")
# Extension is not the definition of a shell script. Extensionless executables
# with a shell shebang are scanned too — MEASURED 2026-08-23: this repo has
# zero of them today, so this closes a latent gap rather than a live one.
SHEBANG = re.compile(rb"^#!.*\b(ba|z|k|da)?sh\b")
SKIP_DIRS = {".git", "node_modules", ".substrate", "dist", "build"}

# A real pipe: `|` not part of `||`, and not inside an obvious regex/alternation
# character class. Conservative — we would rather miss than misfire.
PIPE = re.compile(r"(?<!\|)\|(?!\|)")
READS_STATUS = re.compile(r"\$\?")
PIPESTATUS_RE = re.compile(r"PIPESTATUS")
PIPEFAIL_SET = re.compile(r"^\s*set\s+[-+]\S*o\s+pipefail|^\s*set\s+-o\s+pipefail")
# How far after the pipe a `$?` still plausibly refers to it.
WINDOW = 4


def _skipped(p: Path) -> bool:
    return any(part in SKIP_DIRS for part in p.parts)


def candidates() -> list[Path]:
    out: list[Path] = []
    for pattern in GLOBS:
        for p in REPO.glob(pattern):
            if p.is_file() and not _skipped(p):
                out.append(p)
    # Extensionless files carrying a shell shebang.
    for p in REPO.rglob("*"):
        if not p.is_file() or p.suffix or _skipped(p):
            continue
        try:
            with p.open("rb") as fh:
                first = fh.readline(200)
        except OSError:
            continue
        if SHEBANG.match(first):
            out.append(p)
    return sorted(set(out))


def scan(path: Path) -> list[tuple[int, str]]:
    try:
        text = path.read_text(errors="replace")
    except OSError:
        return []
    lines = text.splitlines()
    hits: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if not PIPE.search(line):
            continue
        # pipefail is positional: only an enabling line ABOVE this pipe counts,
        # and a comment mentioning it does not.
        if any(PIPEFAIL_SET.search(prev)
               for prev in lines[:i]
               if not prev.strip().startswith("#")):
            continue
        window = lines[i:i + WINDOW + 1]
        if any(PIPESTATUS_RE.search(w) for w in window):
            continue                   # the documented fix, at the use site
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
