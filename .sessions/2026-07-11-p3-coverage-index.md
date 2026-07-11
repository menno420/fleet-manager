# 2026-07-11 — P3 COVERAGE + INDEX (fleet centralization plan, final phase)

> **Status:** `in-progress`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11T~20:10Z · lane
worker dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL

## Declared at open (born-red)

Scope: **P3 of the fleet centralization plan** (superbot
`docs/planning/fleet-centralization-plan-2026-07-11.md` §3c/§3e/§4, Option A
custodian-primary in force; P1 = fm PRs #81–#84, P2 = fm #85 → `70c9520`
already live). This slice ships, on branch `claude/p3-coverage-index`:

0. **Queue curation** — verify (live, per-PR, Q-0120) the 8 stale items
   `check_owner_queue.py` flags at HEAD (the (A) merge group: games
   #27/#32/#38 + kit #181; plus the RESOLVED-PENDING-MERGE trail items citing
   fm #47/#68/#76/#77) and sweep verified-merged items to the dated Resolved
   section with merge SHAs.
1. **Per-lane heartbeat sub-rows** in `gen_roster.py` — enumerate ALL
   `control/status*.md` per repo (`substrate.config.json` `heartbeat_files`
   where present, glob fallback) and emit one roster sub-row per extra
   heartbeat file (closes the superbot-games mining/exploration blind spot);
   wired into the same regen paths (workflow + manual).
2. **Generated cross-repo evidence index** (`docs/evidence-index.md`,
   NOT-SOURCE-OF-TRUTH banner) — each roster row → its evidence home
   (superbot `docs/eap` pointer, lane `docs/current-state.md`, latest
   `.sessions/` card, `docs/retro` when present); regenerated with the roster.
3. **Hub heartbeat consumed** — superbot now HAS `control/status.md`
   (superbot PR #2003 → `c18a9c3`); retire the `hub` n/a-fallback disposition
   and verify the generated hub row is real.
4. **fm self-ledger** — fill (decide-and-flag) `docs/current-state.md` +
   `project.index.json` (both stubs; the custodian must meet its own bar).
5. **Port the fleet-triage register** → `docs/fleet-triage.md` (seed: the
   2026-07-11 fleet review §1 table) + a small docs-only superbot pointer PR.
6. **`gen_roster.py` graduation run 3** — 3+-lane hand-check vs ground truth;
   graduate the Q-0105 UNVERIFIED header if clean (kill-switch stays).
7. **Heartbeat** (P3 record + P1/P2/P3 build-complete summary) as the last
   content commit, then flip this card `complete` → REST squash-merge on
   green (one attempt; park on denial).

NOTE: the roster-regen cron fires 20:40Z — if a roster commit lands on main
mid-slice, this branch rebases onto it.
