# `telemetry/` — committed machine-readable fleet telemetry

> **Status:** `binding` (conventions) / `living-data` (the files)

## `triggers-snapshot.json` — the committed trigger-registry export

**What:** the full `list_triggers` export from the claude-code-remote MCP
server, committed at each manager wake. One dict, all pages' records merged
under a single `data` key, **stable-sorted by trigger id**, verbatim record
bodies (no fields stripped). Matches the expected-shape block documented in
`scripts/gen_roster.py`.

**Why (P1 FRESHNESS, superbot
`docs/planning/fleet-centralization-plan-2026-07-11.md` §3a, fm PR #81):**
`list_triggers` is **MCP-only** — no headless process can call it — so the
snapshot dump is inherently a CCR-wake step. Committing it gives
(1) `gen_roster.py` a **headless source**, consumed by the roster-regen cron
(`.github/workflows/roster-regen.yml`, `40 */2 * * *`) so the roster no
longer freezes when the manager seat parks, and (2) a **git-visible registry
history** — e.g. the 2026-07-11 incident (NINE lane failsafes auto-disabled,
`ended_reason=auto_disabled_env_deleted`, 14:45–16:16Z) would be a plain
`git diff` on this file instead of a hand-derived roster-generation headline.

**Dump recipe (manager wake, REQUIRED + verified — see
`projects/fleet-manager/coordinator-prompt.md` § work loop):**

1. Paginate `list_triggers` to exhaustion (limit 100 per page, follow
   `next_cursor` until `has_more` is false).
2. Merge all pages' records under one `data` key; dedupe by id (first wins);
   **sort by trigger id** (stable diffs); record the count.
3. Write `telemetry/triggers-snapshot.json` (2-space indent, sorted keys,
   trailing newline) and commit it with the count in the message.
4. Regenerate the roster from it and verify freshness:
   `python3 scripts/gen_roster.py --triggers telemetry/triggers-snapshot.json`
   then `python3 scripts/check_roster_freshness.py` (must exit 0).

**Freshness semantics:** heartbeat columns of an auto-regenerated roster are
live; **trigger columns are only as fresh as this committed snapshot** (the
regen workflow warns when the snapshot is >24h old). The snapshot never
carries secrets — trigger records hold ids, crons, timestamps, session ids,
and stored wake prompts, all of which this repo already records verbatim.

**Fallback if Actions cron proves unreliable:** a dedicated CCR routine can
both refresh the snapshot AND regen (it has MCP) — the `create_trigger`
recipe is recorded in the header of `.github/workflows/roster-regen.yml`.

## `model-usage.jsonl`

Per-session model-attribution records (fleet standard, ORDER 010); one JSON
object per line, append-only.
