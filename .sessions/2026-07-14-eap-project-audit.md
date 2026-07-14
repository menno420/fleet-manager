# 2026-07-14 — EAP close-out project audit

> **Status:** `in-progress`

📊 Model: Claude Fable · start 2026-07-14 ·
coordinator-dispatched worker (EAP close-out audit lane)

## Declared at open (born-red)

EAP close-out project audit of the fleet-manager seat — mining sessions/PRs/CI/walls into docs/audits/eap-project-audit-2026-07-14.md (owner-directed self-test of the universal audit prompt).

## Close-out (synthesis worker; coordinator flips the badge after heartbeat)

**Shipped:** `docs/audits/eap-project-audit-2026-07-14.md` — 11-section
measured audit synthesized from four evidence-mining passes, dispositioned
throughout (FLEET-FIX / ANTHROPIC / ACCEPTED), deltaing
`docs/eap-retrospective.md`. Linked from the root `README.md` map and
`docs/current-state.md` (docs-gate reachability).

**Key numbers:** window ≈4.6 days · 204 commits on main (post-unshallow) ·
**138 session cards** (recounted: 139 files minus README) · 190 PRs (187
merged at 07:58Z, 1 closed-unmerged #116, 1 open #189) · time-to-land sample
n=20: median ≈7.1 min, session-PR median ≈21 min (designed born-red hold),
worst 3 all classifier-denied merges (2.6–5.1 h, owner clicks) · ≥5
documented owner-click landings · ~33–34 stale `claude/*` branches ·
scheduler incidents: 6h outage 07-12, recurrence-in-miniature 07-13, 9
failsafes env-teardown-disabled 07-11 · wake overhead 4/18 pure heartbeats ·
top-5 pains each with a paste-ready Anthropic ask sentence.

**Reconciliations:** card count 139→138; born-red arming wall stated per the
verified R21 correction (arm-timing + required-check config, not repo class);
R24=codex relay / R25=roster regen; shallow-clone caveat resolved by
`git fetch --unshallow`.

**Checks at close:** `check_roster_freshness.py` OK (1.5h) ·
`check_owner_queue.py` CLEAN · `check_trigger_health.py` 8/9 PASS, I6
SNAPSHOT-FRESH FAIL (export 4.7h old — coordinator wake action, flagged, out
of this audit's write scope: control/ untouched) · `bootstrap.py check
--strict` green except the designed in-progress card hold.

💡 Session idea: feed `telemetry/model-usage.jsonl` for real — the schema
exists but holds one null record; a session-close harvester that appends the
card's `📊 Model:` line + PR number + guard-fire count per session would give
the fleet its first longitudinal ritual-cost dataset and shrink §11's
"not measured" column for free.

⟲ Previous-session review: the four evidence miners were excellent on
verbatim-citation discipline and honest nulls, but disagreed on the session
count (138 vs 139) and one worked a shallow clone the other had already
unshallowed — a shared "measurement preamble" (unshallow + canonical counts
first, then fan out) would have removed both discrepancies at source.

⚑ Self-initiated: none (owner-directed)
