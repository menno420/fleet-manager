# 2026-07-11 — P1 FRESHNESS: triggers snapshot + automated roster regen + freshness checker

> **Status:** `in-progress`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11T~19:00Z · lane
worker dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL

## Declared at open (born-red)

Scope: **phase P1 (FRESHNESS) of the fleet centralization plan** (superbot
`docs/planning/fleet-centralization-plan-2026-07-11.md` §3a/§5, owner-directed,
Option A custodian-primary in force). Kills the single-point-of-freshness that
let the roster go ~13h stale and the silent-dark class that gen #6 caught
(NINE lane failsafes auto-disabled `ended_reason=auto_disabled_env_deleted`,
14:45–16:16Z today). Deliverables this PR:

1. **`telemetry/triggers-snapshot.json`** — full `list_triggers` export
   committed at each manager wake (first snapshot produced live this session;
   stable-sorted by trigger id; gives `gen_roster.py` a headless source + a
   git-visible registry history).
2. **`.github/workflows/roster-regen.yml`** — Actions cron `40 */2 * * *`
   (offset from lane heartbeats): regenerates `docs/roster.md` from the
   committed snapshot + live heartbeat re-fetch, commits on change.
3. **`scripts/check_roster_freshness.py`** — reds LOUDLY when the roster's
   generated-at stamp is older than 2× cadence (~4h); wired into CI via a
   separate workflow (substrate-gate.yml is kit-owned, never hand-edited);
   Q-0105 provenance header; verified against known-bad + known-good fixtures.
4. **Docs**: snapshot dump documented as a REQUIRED verified wake step in
   `projects/fleet-manager/coordinator-prompt.md` § work loop + the
   `gen_roster.py` regen recipe; CCR create_trigger alternative recorded as
   fallback.

Landing path: heartbeat LAST → flip this card `complete` → bootstrap check
--strict green → one REST squash-merge attempt on green (park verbatim on
denial; no auto-merge arming — known wall in this repo).

## Shipped (close-out)

(to be written at close)
