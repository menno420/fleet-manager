#!/usr/bin/env python3
"""seat_digest_sync — consume the substrate-kit seat-digest extraction contract.

The fm side of grounded-skills slice 6 (kit plan
docs/planning/2026-07-12-grounded-skills-program.md §7.6, §4.2e; kit side
merged substrate-kit PR #279 @ dc8aeb1, released v1.15.0; fm adopted v1.15.0
via PR #123 @ d7d264b0). Owner-directed 2026-07-12.

THE CONTRACT (kit src/engine/grammar.py, documented in every adopter's
generated docs/seat-digest.md): three HTML-comment fence-prefix pairs —
skills-digest, walls-digest, capability-seed. Consumers match the PREFIX
only (trailing marker wording may evolve without orphaning a fence); the
bytes between a BEGIN/END pair are the canonical block. Consumption is
**tree scan + fence-prefix match + byte compare — NEVER executing kit code**
(no importing/running bootstrap.py or kit modules from adopter trees; this
module reads committed files as text, nothing else).

NO-THIRD-COPY CHAIN (kit plan §4.2e — the venture-lab I-44 duplicate class):

  1. adopter docs/CAPABILITIES.md      — seat-local source of truth
  2. adopter docs/seat-digest.md       — kit-DERIVED render (regenerated,
                                          never edited)
  3. projects/<seat>/seat-digest.md    — fm registry RENDER of (2), written
                                          only by this tool's --sync
  4. prompt blocks                     — renders of (3): any
                                          substrate-kit:*-digest fence in a
                                          paste must BYTE-MATCH (3)

No third *authored* copy is ever minted. Drift is fixed at the source and
re-synced forward — never merged back by hand.

MODES

    python3 docs/prompts/v3/tools/seat_digest_sync.py [--check] [--trees DIR]
        Drift guard (default mode; --check-registry-style). Exit non-zero on:
        - a projects/<seat>/seat-digest.md without the GENERATED header
          marker (a hand-authored third copy);
        - body content outside the derived shape (heading + the two fenced
          blocks per source repo — hand-grown content);
        - a fenced block over the kit budget (1,500 chars — the one drift
          class that breaks the 8,000-char seat-paste budget outright);
        - a committed block that does not byte-match a fresh extraction
          from its source tree (when the tree is available under --trees);
        - a digest fence embedded in ANY per-seat paste or registry prompt
          copy that does not byte-match the seat's registry render;
        - the vendored contract failing against fm's own committed
          docs/seat-digest.md + docs/CAPABILITIES.md (contract drift alarm).
        Unavailable source trees are SKIP notes, never failures (CI has no
        sibling checkouts; the guard degrades to structure + budget there).

    python3 docs/prompts/v3/tools/seat_digest_sync.py --sync [--trees DIR]
        Regenerate projects/<seat>/seat-digest.md for every seat with at
        least one available source digest. A tree is "available" when
        <trees>/<repo>/docs/seat-digest.md exists (default trees dir: the
        parent of this repo checkout — where fleet session environments
        keep sibling repo checkouts). The fleet-manager seat's own source
        is always this repo itself. NOTE: extraction is only as fresh as
        the tree — sync sibling checkouts to origin/main first.

    python3 docs/prompts/v3/tools/seat_digest_sync.py --selftest
        Fixture suite in a temp dir (no network, no repo writes).

Reliability (kit PL-008 posture): UNVERIFIED — confirm findings against
ground truth a few times across sessions before trusting it; delete this if
it proves unreliable over multiple sessions. The regen_b_files.py default
run calls advisory() (print-only) until this graduates.

Provenance: vendored constants below are byte-copies of kit
src/engine/grammar.py @ v1.15.0 (dc8aeb1); extraction semantics mirror the
kit's check_seat_digest._fenced_block (markers inclusive, line-anchored,
first BEGIN wins, unmatched fence = no verdict). Seat→repo map cited from
projects/<seat>/meta.md "Writable repos" lines, verified at fm b25b348.
"""

import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V3 = HERE.parent
REPO = V3.parent.parent.parent
PROJECTS = REPO / "projects"
MARKER = "<!-- registry-header-end -->"
PROVENANCE_DATE = "2026-07-12"
DIGEST_ARTIFACT_VERSION = "v1"
GITHUB_OWNER = "menno420"

# ── vendored extraction contract (kit grammar.py @ v1.15.0, byte-identical) ──
SKILLS_DIGEST_BEGIN_PREFIX = "<!-- substrate-kit:skills-digest BEGIN"
SKILLS_DIGEST_END_PREFIX = "<!-- substrate-kit:skills-digest END"
WALLS_DIGEST_BEGIN_PREFIX = "<!-- substrate-kit:walls-digest BEGIN"
WALLS_DIGEST_END_PREFIX = "<!-- substrate-kit:walls-digest END"
CAPABILITY_SEED_BEGIN_PREFIX = "<!-- substrate-kit:capability-seed BEGIN"
CAPABILITY_SEED_END_PREFIX = "<!-- substrate-kit:capability-seed END"
WALLS_DIGEST_VENUES_RE = re.compile(r"venues=([a-z][a-z,-]*)")
SEAT_DIGEST_BLOCK_BUDGET = 1500

DIGEST_RELPATH = "docs/seat-digest.md"
LEDGER_RELPATH = "docs/CAPABILITIES.md"

# Seat reg-dir → source repos (order = meta.md order). Provenance:
# projects/<seat>/meta.md "Writable repos" @ fm b25b348. Repos gain a
# committed docs/seat-digest.md at their kit >= v1.15.0 upgrade; --sync
# picks each up incrementally as its wave lands.
SEAT_REPOS = {
    "fleet-manager": ["fleet-manager"],
    "superbot-2.0": ["superbot", "superbot-next"],
    "websites": ["websites"],
    "self-improvement": ["substrate-kit"],
    "superbot-world": ["superbot-mineverse", "superbot-games", "superbot-idle"],
    "game-lab": ["gba-homebrew", "pokemon-mod-lab"],
    "ideas-lab": ["idea-engine", "sim-lab"],
    "venture-lab": ["venture-lab"],
}


def extract_block(text: str, begin_prefix: str, end_prefix: str):
    """The fenced block, markers inclusive, or None when unmatched.

    Byte-identical semantics to the kit's check_seat_digest._fenced_block /
    upgrade._capability_fence: line-anchored prefix match on stripped lines,
    first BEGIN wins, unmatched fence returns None (no verdict, never a
    guess).
    """
    lines = text.splitlines(keepends=True)
    begin = end = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if begin is None and stripped.startswith(begin_prefix):
            begin = i
        elif begin is not None and stripped.startswith(end_prefix):
            end = i
            break
    if begin is None or end is None:
        return None
    return "".join(lines[begin : end + 1])


def walls_venues(walls_block: str):
    """The venues= token off the walls BEGIN marker, or None."""
    first = walls_block.splitlines()[0] if walls_block else ""
    m = WALLS_DIGEST_VENUES_RE.search(first)
    return m.group(1) if m else None


def extract_digest(digest_text: str):
    """(skills_block, walls_block) from an adopter's seat-digest doc.

    Either may be None when its fence is unmatched.
    """
    skills = extract_block(
        digest_text, SKILLS_DIGEST_BEGIN_PREFIX, SKILLS_DIGEST_END_PREFIX)
    walls = extract_block(
        digest_text, WALLS_DIGEST_BEGIN_PREFIX, WALLS_DIGEST_END_PREFIX)
    return skills, walls


def source_digest_path(repo_name: str, trees: Path, repo_root: Path) -> Path:
    """Where a source repo's committed digest lives. fm's own source is
    always this checkout itself (works in CI, where no siblings exist)."""
    if repo_name == repo_root.name or repo_name == "fleet-manager":
        return repo_root / DIGEST_RELPATH
    return trees / repo_name / DIGEST_RELPATH


def section_heading(repo_name: str) -> str:
    return f"## {GITHUB_OWNER}/{repo_name} — {DIGEST_RELPATH}"


def render_body(sections) -> str:
    """Deterministic registry body from [(repo, skills, walls), ...].

    Pure function of the extracted bytes — no dates, no env reads — so the
    drift guard can re-derive and byte-compare it in any environment.
    """
    parts = []
    for repo_name, skills, walls in sections:
        parts.append(f"{section_heading(repo_name)}\n\n{skills}\n{walls}")
    return "\n".join(parts)


def render_header(seat_name: str, sources) -> str:
    src_lines = "\n".join(
        f"> - {GITHUB_OWNER}/{repo}/{DIGEST_RELPATH} · sha256 {sha[:12]} · venues={venues}"
        for repo, sha, venues in sources)
    return (
        f"<!-- {DIGEST_ARTIFACT_VERSION} · {PROVENANCE_DATE} · fleet-manager projects registry — GENERATED COPY, do not edit\n"
        "     (regenerate: docs/prompts/v3/tools/seat_digest_sync.py --sync; drift guard: --check) -->\n"
        "<!-- extracted per the substrate-kit machine extraction contract (kit v1.15.0, PR #279 @ dc8aeb1):\n"
        "     tree scan + fence-prefix match + byte compare — kit code NEVER executed -->\n"
        f"# {seat_name} — seat digest (registry render, extraction contract)\n\n"
        "> **GENERATED COPY — NOT SOURCE OF TRUTH.** Each section below is the fenced\n"
        "> digest pair extracted VERBATIM from the source repo's committed\n"
        "> docs/seat-digest.md (itself a kit-derived render of that repo's\n"
        "> docs/CAPABILITIES.md ledger + skill index — regenerated there, never edited).\n"
        "> No-third-copy chain (kit grounded-skills plan §4.2e): ledger → seat digest\n"
        "> (derived render) → this registry render → prompt blocks. A prompt block\n"
        "> embedding a substrate-kit:*-digest fence must BYTE-MATCH this render\n"
        "> (enforced by seat_digest_sync.py --check). Fix drift at the source and\n"
        "> re-run --sync; never edit this file, never merge content back by hand.\n"
        "> Sources at last sync:\n"
        f"{src_lines}\n\n"
        f"{MARKER}\n"
    )


def gather_sections(reg: str, trees: Path, repo_root: Path, seat_repos=None):
    """Extract available sections for one seat.

    Returns (sections, sources, notes): sections/sources feed the render;
    notes are human-readable skip reasons.
    """
    seat_repos = seat_repos if seat_repos is not None else SEAT_REPOS
    sections, sources, notes = [], [], []
    for repo_name in seat_repos[reg]:
        path = source_digest_path(repo_name, trees, repo_root)
        if not path.is_file():
            notes.append(
                f"{reg}: source {repo_name}/{DIGEST_RELPATH} not available "
                "(tree missing or digest not yet planted — kit < v1.15.0 or "
                "pre-wave); skipped")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            notes.append(f"{reg}: source {repo_name} unreadable ({exc}); skipped")
            continue
        skills, walls = extract_digest(text)
        if skills is None or walls is None:
            notes.append(
                f"{reg}: source {repo_name} digest present but a contract "
                "fence is UNMATCHED — vendored contract may have drifted "
                "from the kit; not extracted")
            continue
        sections.append((repo_name, skills, walls))
        sources.append((
            repo_name,
            hashlib.sha256(text.encode("utf-8")).hexdigest(),
            walls_venues(walls) or "?",
        ))
    return sections, sources, notes


# ---------------------------------------------------------------- sync


def sync(trees: Path = None, repo_root: Path = REPO, projects: Path = None,
         seats=None, seat_repos=None) -> int:
    from regen_b_files import SEATS  # sibling module — the one seat table
    seats = seats if seats is not None else SEATS
    projects = projects if projects is not None else (repo_root / "projects")
    trees = trees if trees is not None else repo_root.parent
    wrote = 0
    for seat in seats:
        reg = seat["reg"]
        sections, sources, notes = gather_sections(
            reg, trees, repo_root, seat_repos)
        for note in notes:
            print(f"note: {note}")
        if not sections:
            print(f"{reg}: no source digest available — nothing written")
            continue
        path = projects / reg / "seat-digest.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            render_header(seat["name"], sources) + render_body(sections),
            encoding="utf-8")
        wrote += 1
        for repo_name, skills, walls in sections:
            print(f"wrote {path.relative_to(projects.parent)}  "
                  f"[{repo_name}: skills {len(skills):,} + walls {len(walls):,} chars, "
                  f"venues={walls_venues(walls)}]")
    print(f"sync: {wrote} seat render(s) written")
    return 0


# ---------------------------------------------------------------- check


def _parse_body(body: str):
    """Committed body → ({repo: (skills, walls)}, structural_faults).

    The derived shape is strict: repo section headings, blank lines, and the
    two fenced blocks per section — anything else is hand-grown content
    (the third-copy class this guard exists to catch).
    """
    heading_re = re.compile(
        rf"^## {re.escape(GITHUB_OWNER)}/([A-Za-z0-9._-]+) — {re.escape(DIGEST_RELPATH)}$")
    sections, faults = {}, []
    current = None
    chunks = {}
    for line in body.splitlines(keepends=True):
        m = heading_re.match(line.rstrip("\n"))
        if m:
            current = m.group(1)
            chunks[current] = []
            continue
        if current is None:
            if line.strip():
                faults.append(f"content before first section heading: {line.strip()[:60]!r}")
            continue
        chunks[current].append(line)
    for repo_name, lines in chunks.items():
        text = "".join(lines)
        skills, walls = extract_digest(text)
        if skills is None or walls is None:
            faults.append(f"section {repo_name}: missing/unmatched digest fence pair")
            continue
        leftover = text.replace(skills, "", 1).replace(walls, "", 1)
        if leftover.strip():
            faults.append(
                f"section {repo_name}: content outside the fenced blocks "
                f"(hand-grown — the no-third-copy violation): {leftover.strip()[:60]!r}")
        sections[repo_name] = (skills, walls)
    return sections, faults


def _check_paste_fences(seat, registry_sections, v3: Path, projects: Path):
    """Digest fences embedded in pastes must byte-match the registry render."""
    faults = []
    candidates = [
        v3 / "per-project" / seat["startup"],
        v3 / "per-project" / seat["ci"],
        projects / seat["reg"] / "coordinator-prompt.md",
        projects / seat["reg"] / "instructions.md",
        projects / seat["reg"] / "failsafe-prompt.md",
    ]
    for path in candidates:
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for label, bp, ep in (
                ("skills", SKILLS_DIGEST_BEGIN_PREFIX, SKILLS_DIGEST_END_PREFIX),
                ("walls", WALLS_DIGEST_BEGIN_PREFIX, WALLS_DIGEST_END_PREFIX)):
            block = extract_block(text, bp, ep)
            if block is None:
                continue
            idx = 0 if label == "skills" else 1
            expected = {r: pair[idx] for r, pair in registry_sections.items()}
            if not expected:
                faults.append(
                    f"{path.name}: embeds a {label}-digest fence but seat "
                    f"{seat['reg']} has no registry render — run --sync first")
            elif block not in expected.values():
                faults.append(
                    f"{path.name}: embedded {label}-digest fence does not "
                    f"byte-match the seat's registry render (prompt blocks "
                    "are renders of the digest — fix at the source, re-sync, "
                    "then re-splice)")
    return faults


def check(trees: Path = None, repo_root: Path = REPO, projects: Path = None,
          seats=None, seat_repos=None, quiet: bool = False) -> list:
    """All findings (fail-worthy) as strings; prints notes unless quiet."""
    from regen_b_files import SEATS
    seats = seats if seats is not None else SEATS
    projects = projects if projects is not None else (repo_root / "projects")
    trees = trees if trees is not None else repo_root.parent
    v3 = repo_root / "docs" / "prompts" / "v3"
    findings = []

    def note(msg):
        if not quiet:
            print(f"note: {msg}")

    # contract sanity: fm's own committed artifacts must satisfy the
    # vendored contract — if they stop matching, consumption is broken.
    own_digest = repo_root / DIGEST_RELPATH
    if own_digest.is_file():
        sk, wl = extract_digest(own_digest.read_text(encoding="utf-8"))
        if sk is None or wl is None:
            findings.append(
                f"{DIGEST_RELPATH}: vendored fence prefixes fail against this "
                "repo's own kit-generated digest — the extraction contract "
                "drifted; re-vendor from kit grammar.py before trusting any sync")
    own_ledger = repo_root / LEDGER_RELPATH
    if own_ledger.is_file():
        seed = extract_block(
            own_ledger.read_text(encoding="utf-8"),
            CAPABILITY_SEED_BEGIN_PREFIX, CAPABILITY_SEED_END_PREFIX)
        if seed is None:
            findings.append(
                f"{LEDGER_RELPATH}: capability-seed fence pair unmatched — "
                "contract drift alarm (third pair of the kit contract)")

    for seat in seats:
        reg = seat["reg"]
        path = projects / reg / "seat-digest.md"
        fresh_sections, _, fresh_notes = gather_sections(
            reg, trees, repo_root, seat_repos)
        fresh = {r: (s, w) for r, s, w in fresh_sections}
        if not path.is_file():
            if fresh:
                note(f"{reg}: source digest(s) available but no registry "
                     "render yet — run --sync to onboard")
            continue
        text = path.read_text(encoding="utf-8")
        if f"{MARKER}\n" not in text or "GENERATED COPY" not in text:
            findings.append(
                f"projects/{reg}/seat-digest.md: missing the GENERATED "
                "header/marker — reads as a hand-authored copy (the "
                "no-third-copy violation); delete it and --sync")
            continue
        body = text.split(f"{MARKER}\n", 1)[1]
        committed, faults = _parse_body(body)
        findings.extend(f"projects/{reg}/seat-digest.md: {f}" for f in faults)
        for repo_name, (skills, walls) in committed.items():
            for label, block in (("skills", skills), ("walls", walls)):
                if len(block) > SEAT_DIGEST_BLOCK_BUDGET:
                    findings.append(
                        f"projects/{reg}/seat-digest.md [{repo_name}]: "
                        f"{label} block {len(block)} chars > "
                        f"{SEAT_DIGEST_BLOCK_BUDGET} budget — breaks the "
                        "8,000-char seat-paste headroom; regenerate at the "
                        "source (`python3 bootstrap.py seat-digest`) and re-sync")
            if repo_name in fresh:
                if (skills, walls) != fresh[repo_name]:
                    findings.append(
                        f"projects/{reg}/seat-digest.md [{repo_name}]: DRIFT — "
                        "committed blocks differ from a fresh extraction of "
                        "the source tree; run --sync (and re-splice any "
                        "prompt blocks rendered from them)")
            else:
                src = source_digest_path(repo_name, trees, repo_root)
                if src.parent.parent.is_dir():
                    note(f"{reg}: {repo_name} tree present but digest "
                         "missing/unextractable — stale checkout? sync the "
                         "tree to origin/main and re-check")
                else:
                    note(f"{reg}: {repo_name} tree unavailable — byte-compare "
                         "skipped (structure + budget verified)")
        for repo_name in fresh:
            if repo_name not in committed:
                findings.append(
                    f"projects/{reg}/seat-digest.md: source {repo_name} digest "
                    "is available but has no committed section — run --sync")
        findings.extend(_check_paste_fences(seat, committed, v3, projects))
    return findings


def run_check(trees: Path = None) -> int:
    findings = check(trees=trees)
    if findings:
        for f in findings:
            print(f"FAIL: {f}")
        return 1
    print("seat-digest check: OK — registry renders match available sources; "
          "structure, budgets, paste fences, contract sanity all clean")
    return 0


def advisory() -> None:
    """Print-only check for the regen_b_files default run (PL-008
    advisory-first: never raises, never affects the caller's exit code)."""
    try:
        findings = check(quiet=True)
    except Exception as exc:  # noqa: BLE001 — advisory must not break regen
        print(f"seat-digest advisory skipped: {exc}")
        return
    if findings:
        for f in findings:
            print(f"seat-digest ADVISORY: {f}")
        print("seat-digest ADVISORY: findings above are advisory here; the "
              "gate is `seat_digest_sync.py --check`")
    else:
        print("seat-digest advisory: clean")


# ---------------------------------------------------------------- selftest


def _fixture_digest(repo_name: str, venues: str = "autonomous-project,any",
                    pad: str = "") -> str:
    return (
        f"# {repo_name} — seat digest\n\nheader prose\n\n"
        f"{SKILLS_DIGEST_BEGIN_PREFIX} — derived render, kit-generated. -->\n"
        f"## Skills digest\n\n- `alpha` — does a thing.\n{pad}"
        f"Full index: docs/SKILLS.md\n"
        f"{SKILLS_DIGEST_END_PREFIX} -->\n\n"
        f"{WALLS_DIGEST_BEGIN_PREFIX} venues={venues} — derived render. -->\n"
        f"## Walls digest\n\n- `any` · wall one.\n"
        f"Full ledger: docs/CAPABILITIES.md\n"
        f"{WALLS_DIGEST_END_PREFIX} -->\n\n"
        "## Extraction contract\n\ntrailing prose\n"
    )


def selftest() -> int:
    import tempfile

    fails = []

    def expect(cond, label):
        print(("ok  " if cond else "FAIL") + f" — {label}")
        if not cond:
            fails.append(label)

    seats = [dict(name="Test Seat", startup="test-startup.md",
                  ci="test-ci.md", reg="test-seat")]
    seat_repos = {"test-seat": ["repo-a", "repo-b"]}

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        repo_root = root / "fm"
        trees = root / "trees"
        projects = repo_root / "projects"
        (repo_root / "docs" / "prompts" / "v3" / "per-project").mkdir(parents=True)
        (trees / "repo-a" / "docs").mkdir(parents=True)
        (trees / "repo-a" / "docs" / "seat-digest.md").write_text(
            _fixture_digest("repo-a"), encoding="utf-8")

        # extraction identity: markers inclusive, prefix-matched
        text = _fixture_digest("repo-a")
        sk, wl = extract_digest(text)
        expect(sk is not None and sk.startswith(SKILLS_DIGEST_BEGIN_PREFIX)
               and sk.rstrip("\n").endswith("-->"), "extract: markers inclusive")
        expect(extract_block("no fences here", SKILLS_DIGEST_BEGIN_PREFIX,
                             SKILLS_DIGEST_END_PREFIX) is None,
               "extract: unmatched fence -> None")
        expect(walls_venues(wl) == "autonomous-project,any", "venues token parsed")

        # sync writes the render; repo-b (unavailable) is skipped
        sync(trees=trees, repo_root=repo_root, projects=projects,
             seats=seats, seat_repos=seat_repos)
        reg_file = projects / "test-seat" / "seat-digest.md"
        expect(reg_file.is_file(), "sync: registry render written")
        expect(MARKER in reg_file.read_text(), "sync: header marker present")

        # clean check
        f = check(trees=trees, repo_root=repo_root, projects=projects,
                  seats=seats, seat_repos=seat_repos, quiet=True)
        expect(f == [], f"check: clean after sync (got {f})")

        # tampered committed block -> drift
        reg_file.write_text(reg_file.read_text().replace("wall one", "wall 1"),
                            encoding="utf-8")
        f = check(trees=trees, repo_root=repo_root, projects=projects,
                  seats=seats, seat_repos=seat_repos, quiet=True)
        expect(any("DRIFT" in x for x in f), "check: tampered block -> DRIFT")

        # source updated upstream -> drift too (same byte-compare)
        sync(trees=trees, repo_root=repo_root, projects=projects,
             seats=seats, seat_repos=seat_repos)
        (trees / "repo-a" / "docs" / "seat-digest.md").write_text(
            _fixture_digest("repo-a").replace("wall one", "wall two"),
            encoding="utf-8")
        f = check(trees=trees, repo_root=repo_root, projects=projects,
                  seats=seats, seat_repos=seat_repos, quiet=True)
        expect(any("DRIFT" in x for x in f), "check: stale render -> DRIFT")

        # hand-authored file without the generated header -> violation
        sync(trees=trees, repo_root=repo_root, projects=projects,
             seats=seats, seat_repos=seat_repos)
        reg_file.write_text("# my seat digest\n\nhand-written walls\n",
                            encoding="utf-8")
        f = check(trees=trees, repo_root=repo_root, projects=projects,
                  seats=seats, seat_repos=seat_repos, quiet=True)
        expect(any("no-third-copy" in x for x in f),
               "check: hand-authored copy -> violation")

        # hand-grown content inside the body -> violation
        sync(trees=trees, repo_root=repo_root, projects=projects,
             seats=seats, seat_repos=seat_repos)
        reg_file.write_text(
            reg_file.read_text() + "\nextra hand-written row\n", encoding="utf-8")
        f = check(trees=trees, repo_root=repo_root, projects=projects,
                  seats=seats, seat_repos=seat_repos, quiet=True)
        expect(any("outside the fenced blocks" in x for x in f),
               "check: hand-grown body content -> violation")

        # over-budget block -> budget fail
        (trees / "repo-a" / "docs" / "seat-digest.md").write_text(
            _fixture_digest("repo-a", pad="- `pad` — " + "x" * 1600 + "\n"),
            encoding="utf-8")
        sync(trees=trees, repo_root=repo_root, projects=projects,
             seats=seats, seat_repos=seat_repos)
        f = check(trees=trees, repo_root=repo_root, projects=projects,
                  seats=seats, seat_repos=seat_repos, quiet=True)
        expect(any("budget" in x for x in f), "check: over-budget block flagged")

        # paste-fence guard: matching embed passes, mismatching fails
        (trees / "repo-a" / "docs" / "seat-digest.md").write_text(
            _fixture_digest("repo-a"), encoding="utf-8")
        sync(trees=trees, repo_root=repo_root, projects=projects,
             seats=seats, seat_repos=seat_repos)
        committed, _ = _parse_body(
            reg_file.read_text().split(f"{MARKER}\n", 1)[1])
        good_paste = "paste prose\n\n" + committed["repo-a"][1] + "\nmore prose\n"
        paste_path = (repo_root / "docs" / "prompts" / "v3" / "per-project"
                      / "test-startup.md")
        paste_path.write_text(good_paste, encoding="utf-8")
        f = check(trees=trees, repo_root=repo_root, projects=projects,
                  seats=seats, seat_repos=seat_repos, quiet=True)
        expect(f == [], f"paste-fence: byte-matching embed passes (got {f})")
        paste_path.write_text(good_paste.replace("wall one", "wall x"),
                              encoding="utf-8")
        f = check(trees=trees, repo_root=repo_root, projects=projects,
                  seats=seats, seat_repos=seat_repos, quiet=True)
        expect(any("byte-match" in x for x in f),
               "paste-fence: drifted embed fails")

    if fails:
        print(f"selftest: {len(fails)} failure(s)")
        return 1
    print("selftest: OK")
    return 0


def main(argv: list) -> int:
    trees = None
    if "--trees" in argv:
        trees = Path(argv[argv.index("--trees") + 1]).resolve()
    if "--selftest" in argv:
        return selftest()
    if "--sync" in argv:
        return sync(trees=trees)
    return run_check(trees=trees)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
