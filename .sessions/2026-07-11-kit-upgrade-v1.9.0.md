# 2026-07-11 — kit upgrade v1.8.0 → v1.9.0

> **Status:** `complete`

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

## Shipped (close-out)

- **bootstrap.py v1.8.0 → v1.9.0** — staged asset self-verified against
  release.json (`upgrade: verified: sha256 + version against release.json`);
  dist sha256 `55181082c796…dc90`; old dist archived byte-exact as
  `.substrate/backup/bootstrap-1.8.0.py` (sha256 `28c5dcb6…89b9b` — matches
  the pre-upgrade `bootstrap.py` hash recorded before the swap); all three
  pre-existing backup banks (1.4.0 / 1.7.0 / 1.7.1) hashed before AND after —
  byte-identical. Upgrade inputs self-cleaned by the upgrader.
- **New v1.9.0 plants:** root `.ignore` + `.gitattributes` (search hygiene;
  both were new files here, kit-appended entries only), staged
  `.substrate/claude/CLAUDE.md` gained the "Kit machinery — search hygiene"
  section, SessionStart orientation now pushes the previous session's handoff
  (exercised live: `## Handoff — the previous session's trail` pointed at
  this very card). `.sessions/README.md` was kept (consumer file already
  carried the Model-line marker doctrine).
- **Gate regenerated** (live + staged copies byte-identical): carries the
  `check --added-card` grammar lint and the mid-PR tighten-only locked-door
  semantics. First live exercise on this PR: run 203 took the locked-door
  path (this PR adds a card AND touches the gate) and emitted the
  `##[notice]` "Designed hold — not a CI failure to investigate" annotation
  while this card was in-progress.
- **Upgrade report:** carve-out scan line verbatim: `- carve-out scan:
  .github/workflows/substrate-gate.yml — ran, 0 found`. control/* files all
  classified `consumer-edited — template unchanged, nothing to apply` (the
  v1.8.0-wave `diverged` classification did not recur). No required_context
  advisory was emitted (nothing pending).
- `python3 bootstrap.py check --strict` exit 0 pending only this card's flip
  (pre-flip run showed exactly the designed born-red hold + one pre-existing
  owner-action-fields advisory on control/status.md — not this lane's file).
- **Lane-owed (NOT done here, one-writer rule):** heartbeat `kit: 1.9.0`
  bump in control/status.md.
- Next session should know: kit is at v1.9.0 on main once PR #66 merges; the
  heartbeat `kit:` line still says 1.8.0 until the lane bumps it.

## 💡 Session idea

The upgrader's report classifies every kept doc but stays silent about root
`CLAUDE.md` when the host has none (fleet-manager's agent guidance lives only
in the staged `.substrate/claude/CLAUDE.md`). A one-line report note —
"root CLAUDE.md absent; search-hygiene note staged only" — would tell a
distribution worker at a glance that the hygiene doctrine is NOT live in the
repo's active agent context and needs a host adoption step, instead of that
being re-derived by grep every wave.

## ⟲ Previous-session review

PR #65 (roster gen #5 + gen_roster.py verification run 1) was a model slice:
it hand-verified 6 lanes cell-by-cell before trusting the tool, found and
root-caused a real display bug (age_str float truncation), and kept the
UNVERIFIED header honest. One miss visible from this seat: its close-out
left the `control/status.md` ⚑ needs-owner asks unstructured — the
owner-action-fields advisory has now fired on four consecutive check runs
(guard-fires.jsonl 03:56Z → 04:45Z) without anyone converting the asks to
OWNER-ACTION format or withdrawing them. Workflow improvement: an advisory
that fires N times unactioned should escalate into the heartbeat's own next
steps line — repetition without escalation is how advisories go permanently
unread.
