# 2026-07-12 — trigger-health remediation

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-12 ·
oversight boot worker (trigger-health remediation)

## Declared at open (born-red)

Fresh trigger snapshot + re-run check_trigger_health + doctrine-safe remediation of wedged/dead triggers (coordinator order, follows ORDER 020 / PR #133).

## Close-out

**Shipped (PR #135):**

- Fresh 941-record `telemetry/triggers-snapshot.json` (10 pages, captured_at
  2026-07-12T18:25:51Z, 0 dupes) with top-level `captured_at` per the ORDER 020
  recipe (telemetry/README.md).
- `scripts/check_trigger_health.py` vs the fresh snapshot: **PASS 6/6, exit 0**
  (evaluated 18:44Z; re-verified 18:49Z). Verbatim verdict in the PR body's
  before/after table.
- `gen_roster.py`: game-lab registry-only LANES row; roster regenerated gen-19.
- `control/status.md` trigger-health block overwritten with the post-remediation
  facts + updated stamp.

**Remediation outcome:** none needed — all 11:12Z BEFORE failures self-resolved
between 11:12Z and the 18:25Z capture: game-lab failsafe
`trig_01JD1t7rD5jUCqkJQJaNCi3E` live again (last_fired 16:50:26Z, next 18:50Z);
6 dropped one-shots cleared; both dead chains (`session_014Z1fPG7Wa6VHprJqLcux4f`,
`session_01SphTJEnN1PYjYZhHNWoJik`) have future ticks armed. No `send_message`
recovery, no trigger edits, no seat notifications.

**⚑ Flags:**

- **I1 blind spot (recorded, not changed):** `trig_011XAWqPeksS8LBrS5G9RvVc`
  ("superbot autonomous dispatch", cron `0 */3 * * *`, next_run_at 10 days past,
  no ended_reason) passes I1 because the list_triggers export **omits the
  `enabled` field on disabled routines** and `gen_roster.trigger_wedged`
  (scripts/gen_roster.py:409: `if not rec.get("enabled") ...: return False`)
  treats absent-`enabled` as disabled (schema comment gen_roster.py:96;
  health_report pre-filters the same way, gen_roster.py:452, reached from
  check_trigger_health.py:108). Repro: `trigger_wedged(rec, eval)` → False as-is,
  → True with `enabled=True` injected. Per doctrine, disabled + empty
  ended_reason = user-paused — so this record is a paused legacy routine, not a
  live wedge — but the checker cannot distinguish "paused" from "enabled-field
  missing" (917/941 snapshot records lack `enabled`; only 24 carry
  `enabled: true`, none carry `enabled: false`). Related shape: the two
  poke-only records `trig_01MWHvQFnRF1dVdZFSP6SM5L` (night executor, also
  enabled-absent) and `trig_018wP6XTPmf9DLnxrG4RpGVh` (docs reconciliation,
  `enabled: true`) show `next_run_at 0001-01-01T00:00:00Z` (zero-time sentinel =
  no own schedule); both escape I1 via the missing `cron_expression` guard on
  the same line, which is correct.
- **Unattributable legacy superbot triggers recorded, not deleted** — old
  superbot-console routines (dispatch / night executor / docs reconciliation)
  predate the fleet lane naming; left untouched per the verify-only order.

## 💡 Session idea

Add an advisory (never-red) tier to `check_trigger_health.py`: report
enabled-absent cron records whose `next_run_at` is > grace in the past and
whose `ended_reason` is empty (the exact shape of
`trig_011XAWqPeksS8LBrS5G9RvVc`). Per API semantics these are user-paused —
correct to not FAIL — but the class is invisible today, and an export that
ever dropped the `enabled` field would silently pass I1. One `[ADVISORY]`
line per record costs nothing and makes the blind spot self-announcing.

## ⟲ Previous-session review

The ORDER 020 session (PR #133) shipped a genuinely solid checker — the
capture-instant eval ladder and the replay proof against the mid-incident
snapshot were exactly right. What it missed: it encoded "absent `enabled` =>
disabled" (gen_roster.py:96) without recording that 917/941 real records
lack the field — so the dominant branch of the predicate was undocumented
and untested against a real export until this wake's anomaly check. System
improvement: when a schema comment declares a default for an optional field,
also record the field's observed frequency in the live data (one line in
telemetry/README.md), so the next agent knows which branch actually carries
the load.
