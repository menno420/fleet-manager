# 2026-07-13 — Trigger-health I1 absent-enabled fix (coordinator-dispatched worker)

> **Status:** `in-progress`

Intent: Slice A — close the `check_trigger_health.py` I1 absent-`enabled` blind spot (records with the `enabled` key ABSENT are skipped by I1 entirely; observed live: `trig_011XAWqPeksS8LBrS5G9RvVc`, next_run frozen 2026-07-02T03:07Z) by surfacing them as a distinct report class matching the checker's grammar, WARN on ambiguous+frozen, with before/after runs against the committed snapshot @ `f09ba87`. Slice B — record the Q-0264 relay consumption sweep (baton item 1 follow-up).

📊 Model: Fable 5

## Work record

- **Slice A shipped:** `scripts/check_trigger_health.py` gains **I1b
  AMBIGUOUS-ENABLED** — records with the `enabled` key ABSENT (not False) were
  skipped by every invariant; I1b splits them into explained remnants (carry an
  `ended_reason`; counted, not listed — 1199 in the committed snapshot) vs
  AMBIGUOUS (no `ended_reason`; listed, liveness never guessed), and an
  ambiguous standing cron with `next_run_at` frozen > grace in the past is a
  **WARN** (truthy status — never affects the exit code; remnants are expected
  history). Before: 7/7 PASS, `trig_011XAWqPeksS8LBrS5G9RvVc` (next_run frozen
  2026-07-02T03:07Z) invisible. After: 7/8 green + 1 WARN, exit 0, the frozen
  dispatch cron listed with the live-verify remedy; second ambiguous record
  surfaced too (`trig_01MWHvQFnRF1dVdZFSP6SM5L`, sentinel next_run, no frozen
  signal). Test pattern: the script's own `--selfcheck` (the PR #133 harness) —
  7 new assertions, PASS. Verifies: roster-freshness OK · owner-queue CLEAN ·
  `bootstrap.py check --strict` red ONLY on this card's designed born-red hold.
- **Slice B shipped:** Q-0264 relay-consumption sweep recorded. Findings: all
  9 verdicts V037–V045 (sim-lab @ `afe18f3`; relay pointers fm
  control/outbox.md L468–502 @ `a32eb2c`) + idea-engine ASK 002 are **pending
  manager fan-out — zero lane-side consumption**, verified read-only at lane
  HEADs venture-lab `765e1f8` · superbot-idle `b03cc96` · superbot-games
  `57f69be` · idea-engine `c807960` · substrate-kit `949875c`. Four
  lane-inbox writes owed: venture-lab ← V037/V039/V040/V041 · superbot-idle ←
  V038 (clears its declared RESUME TRIGGER) · superbot-games ←
  V042/V043/V044/V045 · substrate-kit (Self Improvement) ← ASK 002. Full
  SHA-cited table: `docs/fleet-triage.md` § "2026-07-13 · Q-0264
  relay-consumption sweep"; verification note appended to control/outbox.md
  (append-only grammar). Upkeep: deleted stale claim
  `control/claims/claude-wake-2026-07-13.md` (its PR #166 merged — claims are
  delete-at-close).

## Session enders

💡 Session idea: extend `scripts/check_trigger_health.py` (or a sibling
`check_relay_consumption.py`) to cross-check fm `control/outbox.md` relay
pointers against lane-side consumption — parse "relay pointer / fan-out owed"
sections, `git show origin/main:control/inbox.md` per target lane, and WARN
when a pointer ages past a grace window with no lane-side trace, so "pending
fan-out" ages out visibly instead of silently. This session's sweep was fully
manual; an ager would catch a forgotten fan-out. Dedup-checked: no
relay/consumption checker or idea exists in docs/ideas/, scripts/, or
control/ (grep 2026-07-13).

⟲ Previous-session review: the wake session (PR #166) shipped the Q-0264
relay pointers and successor baton cleanly — the relay record's SHA-cited,
seat-bucketed format made this session's consumption sweep mechanical. Miss:
it left its own claim file `control/claims/claude-wake-2026-07-13.md`
undeleted at merge (claims are delete-at-close); this session cleaned it up.
Improvement: add a claims-hygiene step to session close — a checker (or a
`bootstrap.py check` leg) that flags any `control/claims/*.md` whose branch's
PR is already terminal.
