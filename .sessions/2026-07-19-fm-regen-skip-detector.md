# 2026-07-19 · fm build slice — regen-window skip detector in `check_roster_freshness.py`

> **Status:** `in-progress`

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
