#!/usr/bin/env python3
"""prompts v3.3 — budget/drift checker + projects/ registry sync.

v3.3 (owner spec 2026-07-12) RETIRED the two assembly steps this script used
to perform:

  * Custom Instructions are no longer assembled from custom-instructions-core.md
    + a seat C block — each per-project/<seat>-custom-instructions.md now IS the
    complete, authored, one-file-per-seat paste artifact (seat header +
    condensed five-section skeleton + keyword dictionary + routes).
    HARD cap 8,000 chars (verified console wall) · aim <=7,500.
  * Startup prompts are no longer generated from universal-startup.md — each
    per-project/<seat>-startup.md is an authored, EXPANDED per-seat file that
    carries the universal doctrine VERBATIM. NO char cap (owner spec
    2026-07-12): size is a NOTE, not a gate.

What remains — and what this script now does on every run (default mode):

  python3 docs/prompts/v3/tools/regen_b_files.py
      1. CI budget gate: per-seat char counts; exit non-zero if any CI paste
         body exceeds the 8,000 HARD cap (count the paste as pasted — the
         Codex PR #103 lesson; there are no placeholders left to fill).
      2. Startup size NOTE table (informational, never fails).
      3. DRIFT CHECKS (all fail the run on mismatch), so the CI keyword layer
         and the startup doctrine layer can't silently drift from their
         sources:
         - ENDER SYNC (drift class D-10): every startup's inlined SESSION
           ENDER steps must byte-match the canonical step block in
           ../session-ender.md (single source: edit D, re-splice the 8).
         - GRANT SYNC: every startup's PERMISSIONS & AUTHORITY block must
           byte-match the owner-landed grant in projects/UNIVERSAL.md
           (first/canonical occurrence) — the grant is owner-provenance and
           is never paraphrased.
         - DOCTRINE IDENTITY: the ==== DOCTRINE ==== section must be
           byte-identical across all 8 startups after normalizing the one
           per-seat fill (the CONTROL BUS status grammar).
         - CARD-BLOCK IDENTITY: the "• SESSION CARD (born-red mechanics..."
           block must be byte-identical across all 8 startups.
         - STAMP/DRIFT-CHECK lines present in every CI and startup body.
         - FAILSAFE EXTRACTION: each startup must still carry the BOOT 3a
           FAILSAFE WAKE prompt + cron + step-4 old-trigger sources (the
           registry failsafe-prompt.md files are derived from them).

REGISTRY MODES (unchanged contract; the projects/<seat>/ copies that
downstream surfaces read are GENERATED — never hand-edited):

    python3 docs/prompts/v3/tools/regen_b_files.py --check-registry
        Diff every projects/<seat>/ copy against its v3-derived expected body
        (registry provenance headers ignored — everything above the
        `<!-- registry-header-end -->` marker line). Exit non-zero on drift.

    python3 docs/prompts/v3/tools/regen_b_files.py --write-registry [--sha SHA]
        Regenerate the projects/<seat>/ copies (bodies + stamped registry
        headers). SHA = the commit governing docs/prompts/v3 (default: derived
        via `git log -1 --format=%H -- docs/prompts/v3`); version stamps come
        from SEATS below — bump them there at every re-sync.

Expected bodies: coordinator-prompt.md = the seat's <seat>-startup.md paste
body VERBATIM; instructions.md = the seat's <seat>-custom-instructions.md
paste body VERBATIM; failsafe-prompt.md = the seat's BOOT 3a FAILSAFE WAKE
text wrapped with the seat name + the D-7 stagger-table cron (both extracted
from the startup itself, so the failsafe can never drift from the prompt that
arms it).

Provenance: v3.1 build (PR #103) · v3.2 stateless rebuild + registry modes
(PR #108/#110) · v3.3 one-file-per-seat rebuild (owner spec 2026-07-12).
STATELESS (D-9) still binds both layers: no volatile facts in any paste.
"""

import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V3 = HERE.parent
REPO = V3.parent.parent.parent
PROJECTS = REPO / "projects"
MARKER = "<!-- registry-header-end -->"
PROVENANCE_DATE = "2026-07-12"

CI_HARD = 8000
CI_AIM = 7500

# One row per seat: prompt-source filenames, projects/ dir, and the registry
# version stamps (each registry file's OWN lineage — bump at every re-sync
# that changes content; v3.3 bumped every artifact by one over the PR #110
# v3.2 sync).
SEATS = [
    dict(name="Fleet Manager", startup="fleet-manager-startup.md",
         ci="fleet-manager-custom-instructions.md", reg="fleet-manager",
         versions={"coordinator": "v5", "instructions": "v5", "failsafe": "v5"}),
    dict(name="SuperBot 2.0", startup="superbot-startup.md",
         ci="superbot-custom-instructions.md", reg="superbot-2.0",
         versions={"coordinator": "v3", "instructions": "v3", "failsafe": "v3"}),
    dict(name="Websites", startup="websites-startup.md",
         ci="websites-custom-instructions.md", reg="websites",
         versions={"coordinator": "v5", "instructions": "v4", "failsafe": "v4"}),
    dict(name="Self Improvement", startup="self-improvement-startup.md",
         ci="self-improvement-custom-instructions.md", reg="self-improvement",
         versions={"coordinator": "v3", "instructions": "v3", "failsafe": "v3"}),
    dict(name="SuperBot World", startup="superbot-world-startup.md",
         ci="superbot-world-custom-instructions.md", reg="superbot-world",
         versions={"coordinator": "v3", "instructions": "v3", "failsafe": "v3"}),
    dict(name="Game Lab", startup="game-lab-startup.md",
         ci="game-lab-custom-instructions.md", reg="game-lab",
         versions={"coordinator": "v3", "instructions": "v3", "failsafe": "v3"}),
    dict(name="Ideas Lab", startup="ideas-lab-startup.md",
         ci="ideas-lab-custom-instructions.md", reg="ideas-lab",
         versions={"coordinator": "v3", "instructions": "v3", "failsafe": "v3"}),
    dict(name="Venture Lab", startup="venture-lab-startup.md",
         ci="venture-lab-custom-instructions.md", reg="venture-lab",
         versions={"coordinator": "v4", "instructions": "v5", "failsafe": "v4"}),
]

DOCTRINE_START = "════════ DOCTRINE — full text, binding ════════"
DOCTRINE_END_PREFIX = "Settings/permission config only with the owner live HERE"
CARD_PREFIX = "• SESSION CARD (born-red mechanics, in full):"


def paste_body(path: Path) -> str:
    """Everything from the first `v3.3 ` stamp line onward (repo file headers
    above it excluded), trailing newline stripped — the char-count basis."""
    text = path.read_text()
    m = re.search(r"^v3\.3 ", text, re.M)
    if not m:
        raise RuntimeError(f"{path.name}: no v3.3 stamp line found")
    return text[m.start():].rstrip("\n")


def ender_canonical() -> str:
    """The canonical session-ender step block (steps 1-6 + the Confirm
    recital) from session-ender.md — the single source the inlined copies
    must match (D-10)."""
    text = (V3 / "session-ender.md").read_text()
    m = re.search(r"^1\. PARK — .*?^Confirm before ending:.*?$", text, re.S | re.M)
    if not m:
        raise RuntimeError("session-ender.md: canonical step block not found")
    return m.group(0)


def grant_canonical() -> str:
    """The owner-landed PERMISSIONS & AUTHORITY grant — FIRST (canonical)
    occurrence in projects/UNIVERSAL.md (owner-provenance; never edited by
    agents, never paraphrased in the startups)."""
    text = (PROJECTS / "UNIVERSAL.md").read_text()
    m = re.search(
        r"^PERMISSIONS & AUTHORITY \(v1 .*?^This grant is context for reviewers, not a bypass\.$",
        text, re.S | re.M)
    if not m:
        raise RuntimeError("projects/UNIVERSAL.md: grant block not found")
    return m.group(0)


def doctrine_section(body: str, fname: str) -> str:
    start = body.find(DOCTRINE_START)
    if start < 0:
        raise RuntimeError(f"{fname}: DOCTRINE section not found")
    m = re.search(re.escape(DOCTRINE_END_PREFIX) + r".*?$", body[start:], re.M)
    if not m:
        raise RuntimeError(f"{fname}: DOCTRINE closing line not found")
    return body[start:start + m.end()]


def doctrine_normalized(body: str, fname: str) -> str:
    """Doctrine section with the one per-seat fill (the CONTROL BUS status
    grammar) replaced by a placeholder, so the 8 sections can be compared."""
    sec = doctrine_section(body, fname)
    out, n = re.subn(
        r"(control/status\.md = the coordinator seat only \().+?(; NEUTRAL facts)",
        r"\1{{STATUS_GRAMMAR}}\2", sec)
    if n != 1:
        raise RuntimeError(f"{fname}: CONTROL BUS grammar fill not found (matches: {n})")
    return out


def card_block(body: str, fname: str) -> str:
    m = re.search(re.escape(CARD_PREFIX) + r".*?$", body, re.M)
    if not m:
        raise RuntimeError(f"{fname}: SESSION CARD block not found")
    return m.group(0)


def failsafe_parts(body: str, fname: str) -> dict:
    pm = re.search(r'prompt EXACTLY:\n\s+"(FAILSAFE WAKE .*?)"\n', body, re.S)
    cm = re.search(r'cron_expression "([^"]+)"', body)
    sm = re.search(r"find them in (.+?) \+ ids the heartbeat marks left-for-successor",
                   body, re.S)
    if not (pm and cm and sm):
        raise RuntimeError(f"{fname}: failsafe wake prompt / cron / old-trigger sources not extractable")
    return {"prompt": pm.group(1), "cron": cm.group(1), "sources": sm.group(1)}


# ---------------------------------------------------------------- default mode


def run_checks() -> int:
    fails = []
    ci_rows, su_rows = [], []
    ender = ender_canonical().replace("\n\nConfirm before ending:", "\nConfirm before ending:")
    grant = grant_canonical()
    doctrines, cards = {}, {}

    for seat in SEATS:
        ci_path = V3 / "per-project" / seat["ci"]
        su_path = V3 / "per-project" / seat["startup"]
        ci = paste_body(ci_path)
        su = paste_body(su_path)
        n = len(ci)
        ci_rows.append((seat["ci"], n))
        su_rows.append((seat["startup"], len(su)))
        if n > CI_HARD:
            fails.append(f"{seat['ci']}: CI paste {n:,} chars — OVER the 8,000 HARD cap by {n - CI_HARD}")
        if "DRIFT CHECK" not in ci.splitlines()[0]:
            fails.append(f"{seat['ci']}: line 1 missing the DRIFT CHECK stamp")
        if "DRIFT CHECK" not in su.splitlines()[1]:
            fails.append(f"{seat['startup']}: line 2 missing the DRIFT CHECK rule")
        if ender not in su.replace("\n\nConfirm before ending:", "\nConfirm before ending:"):
            fails.append(f"{seat['startup']}: inlined SESSION ENDER drifted from session-ender.md (D-10)")
        if grant not in su:
            fails.append(f"{seat['startup']}: PERMISSIONS grant drifted from projects/UNIVERSAL.md")
        try:
            doctrines[seat["startup"]] = doctrine_normalized(su, seat["startup"])
            cards[seat["startup"]] = card_block(su, seat["startup"])
            failsafe_parts(su, seat["startup"])
        except RuntimeError as e:
            fails.append(str(e))

    for pool, label in ((doctrines, "DOCTRINE section"), (cards, "SESSION CARD block")):
        if pool and len(set(pool.values())) != 1:
            ref_name, ref = next(iter(pool.items()))
            for fname, val in pool.items():
                if val != ref:
                    fails.append(f"{fname}: {label} differs from {ref_name} — the shared text drifted")

    print(f"{'Custom Instructions (v3.3, one file per seat)':58s} {'chars':>6s}  vs hard 8,000 / aim 7,500")
    for f, n in ci_rows:
        status = "OVER HARD — MUST TRIM" if n > CI_HARD else ("over aim, under hard — flagged by design" if n > CI_AIM else "within aim")
        print(f"{f:58s} {n:6,d}  {status}")
    print()
    print(f"{'Expanded startups (v3.3, size NOTE — no cap)':58s} {'chars':>6s}")
    for f, n in su_rows:
        print(f"{f:58s} {n:6,d}")
    print()
    if fails:
        for f in fails:
            print(f"FAIL: {f}")
        return 1
    print("drift checks: OK — ender sync (D-10), grant sync, doctrine identity, "
          "card-block identity, stamps, failsafe extraction: all 8 seats clean")
    return 0


# ---------------------------------------------------------------- registry


def failsafe_body(seat: dict, parts: dict) -> str:
    name = seat["name"]
    return f"""# {name} — failsafe cron (dead-man wake, Q-0265)

- **Routine name:** `{name} failsafe wake`
- **cron:** `{parts['cron']}` — slot per the stagger table
  (docs/prompts/v3/per-project/README.md, canonical home D-7; the fleet manager
  arbitrates slots — a foreign trigger on the slot is reported, never
  re-slotted; this table supersedes any cron previously recorded in this file)
- **binding:** persistent — fires into the live coordinator session
  (self-bind). After EVERY arming call verify trigger + binding via
  `list_triggers` before writing "armed" — never wait for a first fire
  (completed runs are not inspectable owner-side).

## Prompt text (create_trigger `prompt`, EXACTLY — single-sourced from the seat's v3.3 startup, BOOT step 3a (D-2))

```
{parts['prompt']}
```

## Cutover (BOOT step 4 — rebind-then-delete)

Create + verify the NEW failsafe first, then delete the old id and verify it
absent. NO trigger ids are baked here (STATELESS, D-9) — find old ids in:
{parts['sources']}; plus ids the heartbeat marks left-for-successor. `list_triggers` is
ACCOUNT-WIDE (paginate to exhaustion) — delete ONLY an id those records
attribute to THIS seat, binding audit-verified; unattributable = a sibling's:
record, never delete. A BUSINESS cron (a scheduled deliverable) is rebound,
never dropped — EXCEPT a FRESH-SESSION-PER-FIRE business cron: KEPT as-is,
never rebound and never deleted (it binds to no mortal seat session)."""


def registry_header(seat: dict, artifact: str, version: str, sha: str, body: str) -> str:
    name = seat["name"]
    titles = {
        "coordinator": "coordinator seat prompt (registry copy, prompts v3.3)",
        "instructions": "Custom Instructions (registry copy, prompts v3.3)",
        "failsafe": "failsafe cron text (registry copy, prompts v3.3)",
    }
    specific = {
        "coordinator": (
            f"> Body below the marker = docs/prompts/v3/per-project/{seat['startup']} paste\n"
            "> body VERBATIM (the seat's AUTHORED v3.3 EXPANDED startup — doctrine inlined\n"
            "> in full, NO char cap; paste as the FIRST message of the seat's coordinator\n"
            "> chat)."
        ),
        "instructions": (
            f"> Paste FULL into the Project's Custom Instructions. Body below the marker =\n"
            f"> docs/prompts/v3/per-project/{seat['ci']} paste body\n"
            "> VERBATIM — v3.3 is ONE AUTHORED FILE PER SEAT (seat header + condensed\n"
            "> five-section skeleton + keyword dictionary + routes); the v3.1/v3.2\n"
            "> core+seat-block assembly is RETIRED.\n"
            f"> char-count: {len(body):,} chars = the paste body below the marker, trailing\n"
            "> newline excluded (CHARACTERS — the fleet budget basis; raw UTF-8 bytes\n"
            f"> {len(body.encode('utf-8')):,}) · hard cap 8,000 chars: "
            f"{'PASS' if len(body) <= CI_HARD else 'OVER — MUST TRIM'}."
        ),
        "failsafe": (
            "> Body below the marker wraps the seat's BOOT step-3a FAILSAFE WAKE text\n"
            "> (extracted from the seat's v3.3 startup — D-2 single source) with the seat\n"
            "> name + D-7 stagger-table cron."
        ),
    }
    return (
        f"<!-- {version} · {PROVENANCE_DATE} · fleet-manager projects registry — GENERATED COPY, do not edit\n"
        "     (regenerate: docs/prompts/v3/tools/regen_b_files.py --write-registry; drift guard: --check-registry) -->\n"
        f"<!-- generated from docs/prompts/v3 @ {sha} (prompts v3.3, owner-directed rebuild 2026-07-12) -->\n"
        f"# {name} — {titles[artifact]}\n\n"
        "> **GENERATED COPY — NOT SOURCE OF TRUTH.** This registry copy is GENERATED FROM\n"
        "> the v3 home: **docs/prompts/v3/ is the source of truth** (generation v3.3,\n"
        "> stateless, D-9). Edit the v3 sources and regenerate — never this file.\n"
        f"> Version lineage: {version} ({PROVENANCE_DATE}) supersedes the v3.2 registry sync copy.\n"
        f"{specific[artifact]}\n\n"
        f"{MARKER}\n"
    )


def registry_expected(seat: dict) -> dict:
    su = paste_body(V3 / "per-project" / seat["startup"])
    ci = paste_body(V3 / "per-project" / seat["ci"])
    parts = failsafe_parts(su, seat["startup"])
    reg_dir = PROJECTS / seat["reg"]
    return {
        "coordinator": (reg_dir / "coordinator-prompt.md", su),
        "instructions": (reg_dir / "instructions.md", ci),
        "failsafe": (reg_dir / "failsafe-prompt.md", failsafe_body(seat, parts)),
    }


def resolve_sha() -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), "log", "-1", "--format=%H", "--", "docs/prompts/v3"],
        text=True,
    ).strip()


def write_registry(sha: str) -> int:
    fail = False
    for seat in SEATS:
        for artifact, (path, body) in registry_expected(seat).items():
            path.write_text(registry_header(seat, artifact, seat["versions"][artifact], sha, body) + body + "\n")
            n = len(body)
            flag = ""
            if artifact == "instructions" and n > CI_HARD:
                flag = f"  !! OVER HARD by {n - CI_HARD}"
                fail = True
            print(f"wrote {path.relative_to(REPO)}  ({n:,} chars){flag}")
    return 1 if fail else 0


def check_registry() -> int:
    drift = 0
    for seat in SEATS:
        for artifact, (path, body) in registry_expected(seat).items():
            rel = path.relative_to(REPO)
            if not path.exists():
                print(f"DRIFT {rel}: file missing")
                drift += 1
                continue
            text = path.read_text()
            if f"{MARKER}\n" not in text:
                print(f"DRIFT {rel}: no '{MARKER}' marker line")
                drift += 1
                continue
            actual = text.split(f"{MARKER}\n", 1)[1]
            if actual != body + "\n":
                print(f"DRIFT {rel}: body differs from the v3 source ({artifact})")
                drift += 1
    if drift:
        print(f"check-registry: {drift} file(s) drifted from docs/prompts/v3 — regenerate with --write-registry")
        return 1
    print(f"check-registry: OK — all {len(SEATS) * 3} projects/<seat>/ copies match docs/prompts/v3")
    return 0


def main(argv: list) -> int:
    if "--check-registry" in argv:
        return check_registry()
    if "--write-registry" in argv:
        sha = argv[argv.index("--sha") + 1] if "--sha" in argv else resolve_sha()
        return write_registry(sha)
    return run_checks()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
