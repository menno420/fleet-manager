# Gen-2 launch record — overnight 2026-07-09/10

> **Status:** `reference`
>
> The record of the gen-2 fleet launch (overnight 2026-07-09 evening →
> 2026-07-10 ~06:15Z) and the morning consolidation's verification of it.
> Every number below was re-derived from live GitHub at HEAD on the morning
> of 2026-07-10 (merged-PR search + per-repo status files), not taken from
> lane reports (playbook R2). Companion: the refreshed
> [`../owner-queue.md`](../owner-queue.md) and the rewritten
> [`../../control/status.md`](../../control/status.md).

## 1. Verified overnight numbers (00:00–06:15Z, 2026-07-10)

**116 PRs merged** across the menno420 fleet in the window, **zero stuck**
(the only open PR fleet-wide at the morning sweep was superbot #1926,
opened 06:22Z — a deliberate corrections PR, after the window). The
overnight brief's "~80" was an undercount. Per repo:

| Repo | merged | Highlights |
|---|---|---|
| substrate-kit | 35 | gen-2 walking skeleton → 12 build PRs → night-cap #109/#110; 814 tests; queue DRY |
| trading-strategy | 18 | ORDER 005 → P1 (3 lanes, 590 configs) → P2 (14 verdicts) → P3/P4 → P5 prep #30 |
| gba-homebrew | 18 | seed → skeleton → Lumen Drift incr. 1–3 + polish 1 (scope-complete) + CI pins |
| superbot | 13 | overnight shift #1915–#1925 (manifest un-drift, collision guard, dashboard feed, recon) |
| venture-lab | 8 | skeleton → ORDER 001 → kit+CI → candidates #1/#2 → sellable zips #9 |
| pokemon-mod-lab | 7 | seed → ORDER 001 skeleton → QoL+ increments 1–4 |
| websites | 6 | ORDER 007 → skeleton → ORDER 005 built (#53) → close #54 |
| superbot-games | 6 | **#5 (18-module port) MERGED 00:00:58Z** + #11/#14–#17 wind-down/CI/ideas |
| fleet-manager | 3 | #15 experiment pack · #16 ultracode verification · #17 Fable-5 review landing |
| superbot-next | 2 | #98 band-5 heartbeat · #99 ideas seed (stays gen-1 mid-mission by design) |

## 2. Launches and dispositions

**Launched overnight (gen-2, live):**

- **venture-lab** — the born-right pilot; 2 sellable products with buyer
  zips ON MAIN (#9, 05:11:50Z); revenue clicks ⚑A–D queued.
- **kit-lab gen-2 (substrate-kit)** — full overnight run; queue DRY at the
  night-cap; F-5 ruling is the HOT owner item.
- **game-lab, 2 repos** — pokemon-mod-lab (Track A, PRIVATE) + gba-homebrew
  (Track B, public); both completed ORDER 001; Track A shipped 4 QoL
  game-feel patches, Track B took Lumen Drift to scope-complete + polish.
- **websites gen-2** — ORDER 005 (the gen-1 trap) finally built + ORDER 007.
- **trading gen-2** — P1→P4 done, 1 promoted candidate (AAPL-donchian 15/5
  daily), P5 pre-registered and owner-gated.
- **superbot overnight shift** — 11 PRs of tooling/docs/recon on the legacy
  repo.

**Dispositions (decided at launch, recorded here):**

- **codetool arms ×3** — Projects → **CLOSE**; repos stay (release/PyPI
  asks parked in the owner queue).
- **games mining + exploration** — **merged into ONE games-plugins gen-2
  lane**; NOW UNBLOCKED by superbot-games #5 (the 18-module pure-domain
  port, merged 00:00:58Z — the gen-1 blocker is gone).
- **superbot-next** — stays **gen-1 mid-mission** (band-5 live-testing);
  relaunch waits for the mission boundary, not the calendar.
- **mobile-lab** + **6-repo harness experiment** — **ready-not-launched**:
  packages/prompts committed and paste-ready; verified this morning that
  none of the `harness-exp-*` repos exist (search: 0 results).

## 3. Environment archetype map (as launched)

| Archetype | Script | Lanes booted in it |
|---|---|---|
| python-lab | `environments/archetype-python-lab.sh` | substrate-kit (kit-lab), venture-lab, superbot-games, fleet-manager |
| pinned-research | `environments/archetype-pinned-research.sh` | trading-strategy (two-source layout), websites |
| gba-lab | `environments/archetype-gba-lab.sh` | gba-homebrew + pokemon-mod-lab (game-lab) |
| bot-prod | `environments/archetype-bot-prod.sh` | superbot-next (+ superbot legacy) |
| coordinator (multi-repo) | `environments/archetype-coordinator.sh` | manager / cross-repo sessions |

The overnight boots are the archetypes' live verification — the
provision-death class (three dead gen-1 trading sessions) did not recur.

## 4. Morning click-list snapshot (2026-07-10)

The full queue is [`../owner-queue.md`](../owner-queue.md) (8 active +
parked). Snapshot: **(1) HOT kit F-5 one-letter ruling** · (2) venture-lab
⚑A–D (Stripe test keys; upload the 2 committed zips) · (3) pokemon-mod-lab
playtest (4 game-feel patches, one pass) · (4) concept picks, both tracks ·
(5) kit P10 required-check swap + P4 daily loop · (6) trading P5 holdout
unlock · (7) wake-routine = PLATFORM GAP (walled on BOTH sides; interim =
a morning "continue" per Project) · (8) review the 10 instruction packages
(2 deployed fitted, 8 proposed).

## 5. Contradictions / nuances found at verification

1. **"~80 fleet PRs merged"** → actual **116** in the window (per-repo
   table above). Undercount, direction favorable; zero-stuck confirmed.
2. **venture-lab's own `control/status.md` (04:57Z) still says PR #9
   "awaiting owner merge"** — #9 merged 05:11:50Z, after the status write.
   The zips ARE on main; the lane's next session should refresh its status.
3. **kit's OWNER-ACTION 3 (P4 daily loop) assumes a console Schedules
   pane** — the owner's console lacked the routine/schedule option at the
   2026-07-10 paste session (the both-sides platform gap,
   `../capabilities.md`). The queue item carries the caveat; if the pane is
   truly absent for kit too, P4 collapses into the morning-"continue"
   interim.
4. **Custom Instructions 8,000-char cap** — both ~9k packages (websites
   9,209; trading 8,980) overflowed at paste; fitted ≤7,500-char versions
   are recorded in the two package files and are the texts actually live.
5. All other overnight claims verified exactly: games #5 merged 00:00:58Z;
   kit #26/#49 merged ~00:10Z; kit queue DRY + F-5 HOT; trading P1–P4 +
   1 promoted candidate + P5 owner-gated; both game-lab tracks' ORDER 001
   complete; harness experiment not launched.
