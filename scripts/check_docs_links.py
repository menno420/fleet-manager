#!/usr/bin/env python3
"""check_docs_links.py — flag dead intra-repo markdown links (S5 link-drift sweep).

================================ PROVENANCE ================================
Why added : NEXT-TASKS.md item S5 (first-build set for the recreated
            fleet-manager). The 2026-07-17 wind-down moved/retired several
            docs, and a relative markdown link that points at a moved or
            deleted file rots SILENTLY — nothing reds when a doc says
            `[x](../gone.md)`. The kit's built-in `check_links`
            (bootstrap.py, engine.checks.check_docs) already guards this,
            but ONLY inside `docs/` and WITHOUT anchor validation. This
            checker extends the same idea to the other living committed
            markdown surfaces the wind-down touched — `control/README.md`,
            root docs, `projects/`, `environments/`, `registry/`,
            `templates/` — and optionally validates `#anchor` fragments
            against the target file's headings. It complements, never
            duplicates, the gate: it runs advisory + standalone (not wired
            into `bootstrap.py check`), so it can never jam a merge.
Date      : 2026-07-17 (lane worker, model: Opus 4.8, dispatched by the
            recreated fleet-manager coordinator; fleet-manager PR #293)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it. The GitHub heading
            slug algorithm re-implemented here for anchor checks is a close
            approximation, not GitHub's exact renderer; anchor findings are
            reported as a SEPARATE `dead-anchor` kind so a slug mismatch
            never masquerades as a missing-file finding.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT CHECKS
  Every INTRA-repo markdown link in the living scan set resolves to a file
  that exists on disk. Link forms parsed:
    - inline            [text](target)              and bare <target>
    - reference defs    [label]: target
  For each target, the optional `#anchor` fragment is split off. External
  links (http://, https://, mailto:, tel:, ftp://), protocol-relative
  (//host), and pure same-page anchors (#foo) are SKIPPED. A relative
  target is resolved against the source file's directory; a root-absolute
  target (/docs/x.md) against the repo root. A target whose file does not
  exist is a `dead-link` finding (source file + line number). When the file
  exists and an `#anchor` is present and the target is markdown, the anchor
  is checked against the file's heading slugs (+ explicit <a name/id> and
  `{#custom}` anchors); a miss is a softer `dead-anchor` finding.

SCAN SET (living surfaces only — see --list)
  docs/**  +  control/README.md  +  root *.md  +  projects/**  +
  environments/**  +  registry/**  +  templates/**  (committed *.md).
  EXCLUDED: .substrate/ (kit machinery), scripts/fixtures/ (deliberately
  broken test fixtures), .sessions/ + .session-journal*.md (append-only
  historical byte records — the same OUT-of-scope discipline
  check_owner_queue.py check 3 applies to positional-ref lint).

SEVERITY CONTRACT (sibling-parity: check_owner_queue.py / check_roster_freshness.py)
  Default DIRECT run exits 1 when anything is dead, 0 when clean — the same
  as the other scripts/ checkers, so a local pre-push run reds honestly.
  `--advisory` prints FLAG lines as `::warning::` and always exits 0, for a
  report-only workflow venue (S5 is specced advisory / never merge-blocking,
  and this checker is NOT wired into the blocking substrate-gate).

USAGE
  python3 scripts/check_docs_links.py                 # scan the repo
  python3 scripts/check_docs_links.py --advisory      # report-only, exit 0
  python3 scripts/check_docs_links.py --no-anchors    # skip anchor checks
  python3 scripts/check_docs_links.py --list          # print the scan set
  python3 scripts/check_docs_links.py --root PATH      # scan a fixture tree
  python3 scripts/check_docs_links.py --selftest      # offline fixtures

No third-party deps: stdlib only.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile

# Inline link `](target)` — capture up to the first unescaped ')'. Titles
# (` "..."`) are stripped later. Reference definitions `[label]: target`.
INLINE_LINK_RE = re.compile(r"\]\(\s*([^)]+?)\s*\)")
REF_DEF_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s+(\S+)")
# Fenced code blocks (``` or ~~~) are skipped line-by-line so a link inside a
# code sample is never treated as a live link.
FENCE_RE = re.compile(r"^\s*(```|~~~)")
# Anchor sources inside a target file: markdown headings, plus explicit HTML
# anchors and `{#custom-id}` heading suffixes.
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
HTML_ANCHOR_RE = re.compile(r'<a\s+(?:name|id)\s*=\s*["\']([^"\']+)["\']',
                            re.IGNORECASE)
CUSTOM_ID_RE = re.compile(r"\{#([A-Za-z0-9_-]+)\}\s*$")
# Markdown formatting stripped from heading text before slugging.
MD_LINK_TEXT_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")

EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "ftp://",
                     "ftps://", "//")

# Directories whose *.md are living config surfaces (scanned).
SCAN_DIRS = ("docs", "projects", "environments", "registry", "templates")
# Root-level living docs that carry cross-doc links.
ROOT_FILES = ("README.md", "CONSTITUTION.md", "MISSION.md")
# control/README.md is the one control/ file named by S5; the rest of
# control/ is append-only protocol (inbox/outbox) or regenerated status.
CONTROL_FILES = (os.path.join("control", "README.md"),)
# Excluded subtrees (kit machinery, fixtures, append-only history).
EXCLUDE_DIRS = (".substrate", "scripts", ".git", ".sessions")


def repo_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ------------------------------------------------------------ scan set -----

def collect_files(root: str) -> list[str]:
    """The living-surface *.md scan set under ``root`` (absolute paths)."""
    found: list[str] = []
    for rel in ROOT_FILES:
        p = os.path.join(root, rel)
        if os.path.isfile(p):
            found.append(p)
    for rel in CONTROL_FILES:
        p = os.path.join(root, rel)
        if os.path.isfile(p):
            found.append(p)
    for d in SCAN_DIRS:
        base = os.path.join(root, d)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [x for x in dirnames if x not in EXCLUDE_DIRS]
            for fn in sorted(filenames):
                if fn.endswith(".md"):
                    found.append(os.path.join(dirpath, fn))
    # Stable, de-duplicated order.
    return sorted(dict.fromkeys(found))


# ----------------------------------------------------------- link parse ----

def _clean_target(raw: str) -> str:
    """Strip a surrounding <...>, a trailing ` "title"`, and whitespace."""
    t = raw.strip()
    if t.startswith("<") and t.endswith(">"):
        t = t[1:-1].strip()
    # Drop an inline title: target "Some title" or target 'Some title'.
    m = re.match(r'^(\S+)\s+["\'].*["\']$', t)
    if m:
        t = m.group(1)
    return t.strip()


def iter_links(text: str):
    """Yield (lineno, raw_target) for every link outside code fences."""
    in_fence = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for m in INLINE_LINK_RE.finditer(line):
            yield lineno, m.group(1)
        rm = REF_DEF_RE.match(line)
        if rm:
            yield lineno, rm.group(1)


def is_intra_repo(target: str) -> bool:
    t = target.strip()
    if not t:
        return False
    if t.startswith("#"):          # pure same-page anchor
        return False
    low = t.lower()
    if low.startswith(EXTERNAL_PREFIXES):
        return False
    if ":" in t.split("/")[0]:     # scheme:… (e.g. custom:) — treat external
        return False
    return True


# ------------------------------------------------------------- anchors -----

def slugify(heading_text: str) -> str:
    """Approximate GitHub's heading-anchor slug algorithm."""
    text = MD_LINK_TEXT_RE.sub(r"\1", heading_text)  # [t](u) -> t
    text = CUSTOM_ID_RE.sub("", text).strip()
    text = text.lower()
    # Drop everything that is not a letter, number, space, hyphen or
    # underscore (removes backticks, punctuation, emoji, middots, etc.).
    out = []
    for ch in text:
        if ch.isalnum() or ch in " -_":
            out.append(ch)
    slug = "".join(out).strip()
    slug = slug.replace(" ", "-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug


def anchors_of(path: str) -> set[str] | None:
    """Set of valid anchor slugs in a markdown file; None if unreadable."""
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except (OSError, UnicodeDecodeError):
        return None
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        hm = HEADING_RE.match(line)
        if hm:
            base = slugify(hm.group(2))
            cm = CUSTOM_ID_RE.search(hm.group(2))
            if cm:
                anchors.add(cm.group(1).lower())
            if not base:
                continue
            n = counts.get(base, 0)
            anchors.add(base if n == 0 else f"{base}-{n}")
            counts[base] = n + 1
        for am in HTML_ANCHOR_RE.finditer(line):
            anchors.add(am.group(1).lower())
    return anchors


# -------------------------------------------------------------- checks -----

def check_files(files: list[str], root: str, check_anchors: bool,
                out: list[str]) -> int:
    """Scan ``files`` for dead links/anchors. Returns the flag count."""
    flags = 0
    anchor_cache: dict[str, set[str] | None] = {}
    for path in files:
        rel = os.path.relpath(path, root)
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except (OSError, UnicodeDecodeError) as exc:
            flags += 1
            out.append(f"FLAG [encoding] {rel}: unreadable as UTF-8: {exc}")
            continue
        for lineno, raw in iter_links(text):
            target = _clean_target(raw)
            if not is_intra_repo(target):
                continue
            frag = ""
            if "#" in target:
                target, frag = target.split("#", 1)
            target = target.strip()
            if not target:
                continue  # was a pure #anchor after cleaning
            if target.startswith("/"):
                resolved = os.path.normpath(
                    os.path.join(root, target.lstrip("/")))
            else:
                resolved = os.path.normpath(
                    os.path.join(os.path.dirname(path), target))
            if not os.path.exists(resolved):
                flags += 1
                out.append(f"FLAG [dead-link] {rel}:{lineno}: target "
                           f"{target!r} does not exist "
                           f"(link: [...]({raw.strip()}))")
                continue
            if (check_anchors and frag and os.path.isfile(resolved)
                    and resolved.endswith(".md")):
                if resolved not in anchor_cache:
                    anchor_cache[resolved] = anchors_of(resolved)
                anchors = anchor_cache[resolved]
                if anchors is not None and frag.lower() not in anchors:
                    flags += 1
                    out.append(f"FLAG [dead-anchor] {rel}:{lineno}: "
                               f"{os.path.relpath(resolved, root)} has no "
                               f"anchor #{frag} (slug not found among its "
                               "headings)")
    return flags


# ------------------------------------------------------------ selftest -----

_GOOD_FIXTURE = {
    "docs/a.md": "# Title A\n\nSee [b](b.md) and [sec](b.md#a-heading).\n"
                 "Root link: [home](/README.md).\n",
    "docs/b.md": "# B\n\n## A Heading\n\ntext\n",
    "README.md": "# Repo\n\nlink [a](docs/a.md)\n",
    "control/README.md": "# Control\n\nsee [a](../docs/a.md)\n",
}
_BAD_FIXTURE = {
    "docs/a.md": "# Title A\n\n[gone](../docs/moved-away.md)\n"
                 "[bad anchor](b.md#no-such-heading)\n"
                 "```\n[fenced](should-not-count.md)\n```\n"
                 "[ext](https://example.com/x.md) is skipped\n"
                 "[ref-style][r]\n\n[r]: ./deleted-ref-target.md\n",
    "docs/b.md": "# B\n\n## A Heading\n",
    "control/README.md": "# Control\n\n[dead](./nope.md)\n",
}


def _write_tree(base: str, tree: dict) -> None:
    for rel, content in tree.items():
        p = os.path.join(base, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(content)


def selftest() -> int:
    fails: list[str] = []
    with tempfile.TemporaryDirectory() as good, \
            tempfile.TemporaryDirectory() as bad:
        _write_tree(good, _GOOD_FIXTURE)
        _write_tree(bad, _BAD_FIXTURE)

        good_out: list[str] = []
        good_flags = check_files(collect_files(good), good, True, good_out)
        if good_flags != 0:
            fails.append(f"known-good fixture must be clean, got "
                         f"{good_flags} flag(s): {good_out}")

        bad_out: list[str] = []
        bad_flags = check_files(collect_files(bad), bad, True, bad_out)
        want = [
            ("[dead-link]", "moved-away.md"),
            ("[dead-anchor]", "no-such-heading"),
            ("[dead-link]", "deleted-ref-target.md"),
            ("[dead-link]", "nope.md"),
        ]
        for kind, needle in want:
            if not any(kind in ln and needle in ln for ln in bad_out):
                fails.append(f"known-bad: expected a {kind} finding "
                             f"mentioning {needle!r}; got {bad_out}")
        if any("should-not-count.md" in ln for ln in bad_out):
            fails.append("known-bad: a link inside a code fence was flagged "
                         "(fence skipping is broken)")
        if any("example.com" in ln for ln in bad_out):
            fails.append("known-bad: an external https link was flagged")

    for msg in fails:
        print(f"SELFTEST FAIL: {msg}", file=sys.stderr)
    print(f"selftest: {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s))")
    if not fails:
        print("--- known-bad fixture output ---")
        print("\n".join(bad_out))
        print("--- known-good fixture output ---")
        print("\n".join(good_out) or "(clean)")
    return 1 if fails else 0


# ---------------------------------------------------------------- main -----

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=repo_root(),
                    help="repo/fixture root to scan (default: this repo)")
    ap.add_argument("--advisory", action="store_true",
                    help="report-only: print flags as ::warning::, exit 0")
    ap.add_argument("--no-anchors", action="store_true",
                    help="skip #anchor validation (files-exist only)")
    ap.add_argument("--list", action="store_true",
                    help="print the scan set and exit")
    ap.add_argument("--selftest", action="store_true",
                    help="offline fixture assertions (no network) and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    root = os.path.abspath(args.root)
    files = collect_files(root)
    if args.list:
        for f in files:
            print(os.path.relpath(f, root))
        print(f"\ncheck_docs_links: {len(files)} file(s) in the scan set")
        return 0

    out: list[str] = []
    flags = check_files(files, root, not args.no_anchors, out)
    for line in out:
        if args.advisory and line.startswith("FLAG"):
            print(f"::warning::{line}")
        else:
            print(line)
    verdict = (f"CLEAN — every intra-repo link in {len(files)} file(s) resolves"
               if flags == 0
               else f"{flags} DEAD LINK/ANCHOR(S) across {len(files)} file(s) "
                    "— retarget the moved doc or de-link the retired one")
    print(f"check_docs_links: {verdict}")
    return 0 if (flags == 0 or args.advisory) else 1


if __name__ == "__main__":
    sys.exit(main())
