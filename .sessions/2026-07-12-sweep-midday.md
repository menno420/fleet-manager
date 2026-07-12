# 2026-07-12 — midday staleness sweep (8 seats)

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-12 ·
oversight boot worker (midday staleness sweep)

## Declared at open (born-red)

Midday staleness sweep (8 seats) + trigger snapshot + v3.3 adoption check — in progress.

## Close-out

- **Deliverable:** `docs/research/2026-07-12-staleness-sweep-midday.md` (indexed in `docs/research/README.md`).
- **Verdict roll-up:** 6 FRESH / 2 STALE seats — superbot-world 3/3 STALE (worsened from 1/3), game-lab new STALE (pokemon-mod-lab). No DARK, no DEAD.
- **Trigger snapshot:** 832 triggers (9 pages, 0 duplicate ids) → `telemetry/triggers-snapshot.json`; 28 enabled (9 standing crons + 19 pending one-shots), 804 ended (795 run_once_fired, 4 auto_disabled_session_gone, 3 auto_disabled_env_deleted, 2 user-paused).
- **Roster:** regenerated **gen 14** via `scripts/gen_roster.py`; `check_roster_freshness.py` → OK (0.0h old, threshold 4h).
- **Shortlist:** 9 ranked needs-attention items (top: mineverse PR #42 security merge; venture-lab #51 residual photo exposure).
- **Heartbeat:** `control/status.md` re-stamped 11:37:32Z with the sweep line.

💡 Session idea: `gen_roster.py` should ingest the sweep verdicts (a small `--sweep docs/research/<latest>.md` input or a sidecar JSON) so the roster's Verdict column and the human sweep never disagree — the 04:00Z sweep found 8 verdict mismatches against roster gen #12; one source of truth would retire that whole drift class.

⟲ Previous-session review: the v3.3 landing session (#111/#112) shipped a clean three-layer prompt generation and stamped the registry consistently — but its heartbeat left "Open: PR #112 only" as a claim that went stale the moment #112 merged, exactly the contradicted-heartbeat class this sweep dings other seats for. Improvement: heartbeat "Open:" lines should name the *class* ("this session's PR only") rather than a hard PR number, or be re-stamped by the merge itself; adopted the factual fix here (line updated to #113 with #112 marked merged).
