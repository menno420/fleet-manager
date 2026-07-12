# 2026-07-12 — kit upgrade v1.14.0 → v1.15.0

> **Status:** `complete`

Scope: upgrade the vendored substrate-kit from v1.14.0 to v1.15.0 (distribution wave, kit-owned files only — no control-plane or domain work).

📊 Model: fable-5

## What shipped (PR #123)

- Two-command upgrade: `bootstrap.py.new upgrade` → `bootstrap.py upgrade --apply-docs` → `check --strict` green (only red = this card's designed born-red hold).
- Asset three-way verified: sha256 `25d22af9…c650e`, 828,825 B, release run 29198852306.
- Applied via --apply-docs: CONSTITUTION.md, docs/SKILLS.md. New plants: docs/ROUTINES.md, docs/seat-digest.md.
- Hand-merged the MINIMAL ROUTINES.md wiring hunk into the diverged docs/AGENT_ORIENTATION.md (v1.13.0 #114 precedent) to clear the `[reachable]` orphan.
- Banked exactly one new `.substrate/backup/bootstrap-1.14.0.py` (sha256 47c1b8b9… = v1.14.0 dist); pre-existing banks byte-identical.
- Carve-out scan: ran, 0 found; live gate kept (kit-owned, already current).

## Lane-owed (flagged, untouched per Q-0261.3)

- control/README.md diverged (v1.15.0 heartbeat-grammar delta + still-unapplied v1.14.0 owner-assist/RISK delta).
- control/status.md diverged (heartbeats never edited by distribution) + chronic `kit:` self-report lag (v1.7.0).
- docs/AGENT_ORIENTATION.md remaining template delta (preflight hard-reset section).
- Q-0270 posture-rule collapse note.
- fm seat-digest fence CONSUMPTION (prompt v3.3 regen-tool wiring) = separate fm follow-up slice, not this lane.

💡 Session idea: the upgrade engine could auto-wire a newly planted doc's minimal read-path pointer into a DIVERGED orientation file when the insertion anchor (the planted-doc list) is still byte-recognizable — the SKILLS.md (v1.13.0) and ROUTINES.md (v1.15.0) orphans were both cleared by the same mechanical minimal-hunk merge; two live precedents make it a pattern worth encoding.

⟲ Previous-session review: the v1.14.0 upgrade session (#115) landed cleanly and its report correctly preserved the control/README.md diverged delta — but that delta (RISK line + owner-assist standard) is still unapplied a wave later and was only re-surfaced because this session re-checked the previous PR's report per the wholesale-overwrite gotcha. Improvement: the kit's planned "outstanding deltas" carry-forward section in upgrade-report.md would make this re-check unnecessary — until then the preflight re-check stays mandatory doctrine.
