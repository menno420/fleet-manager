# 2026-07-19 · fm build slice — regen-window skip detector in `check_roster_freshness.py`

> **Status:** `complete`

About to happen (declared born-red): build slice #2 from
`docs/planning/2026-07-19-next-slices.md` — extend `scripts/check_roster_freshness.py`
(stdlib only, exit-code contract untouched) to parse the cron line(s) out of
`.github/workflows/roster-regen.yml`, compute the scheduled regen windows between the
roster's `generated-at` stamp and now, and report
`REGEN WINDOWS: N scheduled since generated-at, M missed (grace 2h)` as informational
WARN lines — never a new exit-red (the 4h freshness bar stays the only red);
`--strict-windows` opt-in flag for future CI use. Motivation: GitHub's cron silently
dropped the 00:40Z + 02:40Z windows tonight (second consecutive skip night) and the
checker stayed green until the 4h bar nearly crossed — drops were invisible until a
human diffed run history. Complements parked PR #344 (odd-hour second cron): #344
reduces drop impact, this makes drops self-announce at every wake. Also:
`control/status.md` baton advance (slice 3 = seat-provenance-aware I8 remedy next),
claim `control/claims/claude-fm-regen-skip-detector.md` (deleted in the flip commit).
No trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · feature build — extend verified checker, tooling+docs (Q-0105 provenance tier)

## What shipped (PR #352)

- `scripts/check_roster_freshness.py` — regen-window skip detector block
  (Q-0105 provenance header): `parse_workflow_crons` (comment-safe line scan,
  tolerates missing/moved workflow → "not measured"), a stdlib 5-field cron
  matcher (`*`, `*/n`, `a-b`, `a-b/n`, lists; standard dom/dow OR semantics;
  unsupported tokens like names → "not measured", never a guess), a
  minute-walk `scheduled_windows` (30-day scan cap, honest truncation note),
  and `report_windows`. A window is MISSED when it is older than the grace
  period (default 2h, `--window-grace-hours`) — with a single generated-at
  stamp every in-range window is by construction uncovered; a covered window
  would have advanced generated-at past itself. Report runs on both the OK
  and stale-RED paths; a future stamp skips it (poisoned clock). New flags:
  `--workflow`, `--window-grace-hours`, `--strict-windows` (opt-in exit-1 on
  miss for future CI; `--advisory` still beats it). **Exit contract
  unchanged** — regression-checked against main at a pinned `--now`:
  identical codes, only informational lines added.
- `control/status.md` — `updated:` → 08:59Z; slice-2 facts subsection; baton
  advanced (slice 2 DONE, next = seat-provenance-aware I8 remedy in
  `check_trigger_health.py`).

## Ground-truth run 1 (2026-07-19T08:58Z, real repo, verbatim)

```
REGEN WINDOWS: 1 scheduled since generated-at 2026-07-19T07:08Z (cron 40 */2 * * *), 0 missed (grace 2h, 1 still within grace)
ROSTER FRESHNESS: OK — generated-at 2026-07-19T07:08Z, 1.8h old (threshold 4h)
```
(exit 0 — the 08:40Z window is pending within grace, correctly not alarmed.)

## Synthetic replay — the incident night (fixture stamp 2026-07-18T23:31Z, verbatim)

Read at 03:30Z (pre-bar, where tonight's checker stayed silently green):

```
REGEN WINDOWS: 2 scheduled since generated-at 2026-07-18T23:31Z (cron 40 */2 * * *), 1 missed (grace 2h, 1 still within grace)
REGEN WINDOWS: WARN — window 2026-07-19T00:40Z MISSED (2.8h ago, no covering regen stamp): the Actions cron dropped or the landing failed — check .github/workflows/roster-regen.yml run history
ROSTER FRESHNESS: OK — generated-at 2026-07-18T23:31Z, 4.0h old (threshold 4h)
```
(exit 0; with `--strict-windows` the same run exits 1 with a STRICT line.)
Read at 04:45Z the report shows the full double-drop — `2 missed` (00:40Z
4.1h, 02:40Z 2.1h) — alongside the freshness RED (exit 1, contract intact).
Also exercised verbatim in-session: missing workflow → `not measured —
cannot read workflow …` (exit 0); unsupported token `40 */2 * * MON` →
`not measured — unsupported cron syntax` (exit 0); a two-cron fixture (the
PR #344 odd-hours shape) → both crons listed, hourly windows counted;
future stamp → windows skipped, RED preserved; `--strict-windows
--advisory` → exit 0 (advisory stays supreme).

## Enders

- 💡 **Session idea (dedup-checked — `docs/ideas/` 16 files, planning docs,
  2026-07-18/19 cards):** **regen run-history probe (`--probe-runs`) to name
  the drop's cause.** The WARN line can say a window was missed but not WHY —
  "the Actions cron dropped or the landing failed" is a disjunction the
  reader must resolve by hand in the Actions UI. A small opt-in probe
  (GITHUB_TOKEN path, `/actions/workflows/roster-regen.yml/runs` since
  generated-at) could label each missed window `no run recorded` (GitHub
  dropped the cron) vs `run <id> concluded <failure/cancelled>` (landing
  failed — different fix). Distinct from this slice (schedule math vs run
  telemetry) and from `check_owner_queue.py` (PR states, not runs); network
  degrades to today's honest disjunction.
- ⟲ **Previous-session review (PR #351, nothing-stuck records slice):** it
  set the bar this card copied — the owner's directive captured verbatim
  with a provenance timestamp, every merge re-verified live with sha +
  instant, and the two worker-stoppages recorded as dated venue states
  routed to the baton rather than as walls. Miss/improvement: the same
  execution facts are restated across three homes (status.md subsection,
  fleet-triage.md section, owner-queue.md rows) — a real drift surface; the
  leaner shape is one canonical record (triage) + pointer lines elsewhere,
  and the baton already demonstrates that pointer style.
- **Doc-audit:** everything durable is homed — detector rationale + evidence
  pointer in the code's own Q-0105 header, facts + baton in
  `control/status.md`, verbatim outputs in this card; the plan doc's
  standing-queue section mirrors the baton by design (DONE marks live in the
  baton, not the dated plan). No orphaned chat-only conclusions.
- **Guard-fires:** `.substrate/guard-fires.jsonl` delta committed
  (do-not-revert); born-red HOLD was the only red in `bootstrap.py check
  --strict` pre-flip.
- **Claim:** `control/claims/claude-fm-regen-skip-detector.md` deleted in
  this flip commit.
