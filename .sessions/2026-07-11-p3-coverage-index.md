# 2026-07-11 — P3 COVERAGE + INDEX (fleet centralization plan, final phase)

> **Status:** `complete`

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

## Shipped (close-out)

All seven declared items landed; **the centralization plan is
BUILD-COMPLETE (P1 #81–#84 · P2 #85 · P3 #86).**

- **Queue curation:** all 8 checker flags live-verified (Q-0120) and swept —
  games #27/#32/#38 MERGED (`50f6774`/`f9c2f7a`/`2f1e7cd`, 14:56Z), kit #181
  ratified (`f7aa633`), UNIVERSAL trail #76 `e1848ff` / #77 `39b888a` / #47
  `5625e3b` / #68 `c5e264f`; OQ-PASTE-WAVE click-ready. `check_owner_queue`:
  8 FLAGS → CLEAN.
- **Sub-rows:** gen #9 = 19 lane rows + **4 `↳` sub-rows** (games
  mining/exploration DARK/DEAD, kit ×2 legacy DARK) — `heartbeat_files`
  ordering honored, glob catches undeclared; sub-heartbeats feed the P2
  candidate extraction too.
- **Evidence index:** `docs/evidence-index.md` generated with the roster;
  per-lane current-state / latest card / retro links pinned at verified
  HEADs; wired into `roster-regen.yml`.
- **Hub row real:** superbot heartbeat consumed (FRESH ~33m at gen #9);
  `hub` disposition retired.
- **Self-ledger:** `docs/current-state.md` + `project.index.json` FILLED
  (decide-and-flag: fill over retire — boot readpath doc).
- **Triage register:** `docs/fleet-triage.md` ported (fleet-review §1 seed,
  post-seed corrections dated); superbot pointer PR #2006 open, auto-merge
  armed (Q-0127).
- **Graduation:** run 3 vs independently-fetched ground truth — verdicts
  8/8, cells exact; header UNVERIFIED → VERIFIED, kill-switch KEPT.
- **In-slice fix (friction → guard):** sub-rows quoting `D-NNN` ids tripped
  the kit stamp-discipline check on this repo — the P2 U+2011 swap extended
  to all roster cells, selfcheck-pinned (`gen_roster.py --selfcheck` PASS).

## 💡 Session idea

The evidence index now knows, per lane, whether `docs/retro/` exists and
how many notes it holds — but nothing alarms when a lane that is
ARCHIVE-READY (phase says so) has **zero** retro notes, which is exactly
the lane most likely to lose its chat-only knowledge. Cheap guard: a
`gen_roster.py` advisory section listing lanes whose phase matches
archive/close-out vocabulary but whose evidence row shows `docs/retro/ = —`
(all data already in the rows; ~15 lines + a selfcheck pin).

## ⟲ Previous-session review

The P2 session (PR #85) left an exemplary trail: its checker's fixture run
recorded verbatim known-bad output, which made this slice's step-0 curation
mechanical (the 8 flags were exactly where its card said they would be).
What it missed: it migrated 33 items to `OQ-` slugs but left the four
already-satisfied (A)-group merge asks in place un-swept even though its own
checker flagged them at HEAD — this slice inherited that sweep. Concrete
workflow improvement: when a NEW checker's first live run flags items, the
shipping session should either sweep them or write the sweep into its
hand-off scope line explicitly, so the debt is claimed rather than implied.

## Verification

- `python3 scripts/gen_roster.py --selfcheck` → PASS (0 failures).
- `python3 scripts/check_roster_freshness.py` → OK (gen #9, 0.0h).
- `python3 scripts/check_owner_queue.py` → CLEAN (post-curation).
- `python3 bootstrap.py check --strict` → only the designed born-red hold
  on this card (flips with this commit); stamp finding fixed in-slice.
