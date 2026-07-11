# 2026-07-11 — kit upgrade v1.8.0 → v1.9.0

> **Status:** `in-progress`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11 · lane worker
dispatched by coordinator (distribution wave, Q-0261.3 kit-upgrade-only scope)

## Declared at open (born-red)

Scope: kit upgrade v1.8.0 → v1.9.0. Plan: verify staged release asset
(sha256 `55181082…`) + release.json adjacency → `python3 bootstrap.py.new
upgrade` (archive-first, self-verify, self-clean) → verify plants (.ignore /
.gitattributes append-only, CLAUDE.md search-hygiene note, .sessions/README
model-attribution doctrine, SessionStart handoff-push surface), regenerated
gate (`check --added-card` lint + "HOLD (by design)" notice), upgrade-report
carve-out line, exactly one new backup `.substrate/backup/bootstrap-1.8.0.py`
(sha256 `28c5dcb6…`) with pre-existing banks byte-identical → `bootstrap.py
check --strict` exit 0 → flip this card complete as the last commit; REST
squash-merge on green (R21). HARD SCOPE: no control/inbox.md or
control/status.md writes — heartbeat `kit:` bump is lane-owed.
