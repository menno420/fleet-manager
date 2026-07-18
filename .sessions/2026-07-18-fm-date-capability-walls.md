# 2026-07-18 · date the undated capability walls (clear S9 advisory)

> **Status:** `complete`

Added evidence-based ledger-recorded dates to the 5 `docs/CAPABILITIES.md` WALL entries that
`scripts/check_capabilities_wall_age.py` (S9) reported as `[undated-wall]` notes. An undated
wall carries no freshness data, so it can never be aged for re-probe and silently hardens into
assumed-permanent — the exact failure mode S9 exists to catch (the 2026-07-17 self-scheduling
wall was recorded and refuted hours later). Dates come from `git blame` (the commit that
recorded each finding), not invented, so each wall is now an age-trackable re-probe candidate.

- **📊 Model:** opus-4.8 · high · docs-only

## What shipped

- `docs/CAPABILITIES.md` — 5 WALL entries dated:
  - Tag push / Release / branch-delete — recorded 2026-07-12 (8f92faa9)
  - Creating/editing claude.ai environments or Projects — recorded 2026-07-12 (8f92faa9)
  - GraphQL quota exhausts at fleet scale — recorded 2026-07-18 (4569cdff)
  - Force-push / amending pushed history — recorded 2026-07-12 (8f92faa9); clarified as a
    standing forward-only policy, not a probeable platform wall
  - Cross-session agent messaging — recorded 2026-07-12 (8f92faa9)
- `control/status.md` — heartbeat refreshed (FM sole writer; structure preserved).

## Effect

`check_capabilities_wall_age.py` `[undated-wall]` notes 5 → 0 (only the 2 legitimate
`[superseded]` notes remain). All 5 are ≤6d old, so they clear the notes without becoming
re-probe-due flags; each now ages toward the 30d re-probe prompt.

## Gates

- `python3 scripts/check_capabilities_wall_age.py` — CLEAN, 0 undated-wall notes for these 5
- `python3 bootstrap.py check --strict` — EXIT 0 (after this card flip; pre-flip EXIT 1 was the
  by-design born-red HOLD, not a defect)
- `python3 tools/check_no_false_walls.py` — EXIT 0

## 💡 Session idea

Give S9 a `--fill-dates` companion mode (or a sibling `date_capability_walls.py`) that, run in
a repo checkout, auto-annotates each `[undated-wall]` entry with its `git blame` recorded-date
and prints a diff for review — turning the manual dating this session did by hand into a
one-command, reproducible sweep the next drift catches automatically.

## ⟲ Previous-session review

The prior session (#323, seat-digest regen) correctly treated the strict-gate `[seat-digest-stale]`
advisory as real drift and regenerated the derived artifact rather than hand-editing it — good
discipline. What it (and the several sessions before it) left on the floor was the S9 advisory
sitting at 5 `[undated-wall]` notes wake after wake: an *advisory* checker's output is still drift
to close, not ambient noise to step over. **System improvement surfaced:** the born-red strict
gate blocks on `[seat-digest-stale]` but S9 is standalone/advisory and never enters
`bootstrap.py check`, so its notes never pressure a session — consider a periodic (non-blocking)
"advisory residue" line in the wake digest so standing advisory notes get picked up as routine
Rung-4 slices instead of accumulating.

## 📋 Doc-audit

Durable homes updated in-session: `docs/CAPABILITIES.md` (the 5 dated walls), `control/status.md`
(heartbeat + session entry), this session card. No chat-only residue; owner-queue/current-state
unchanged (no owner-facing state changed — this is a docs-hygiene slice). `check_no_false_walls`
EXIT 0 confirms no new capability-denial claim was introduced.
