# Staleness sweep — first sweep under the 8-seat registry — 2026-07-12

> **Status:** `audit`
>
> First fleet staleness sweep under the new 8-seat registry (`projects/` @
> main `cb91fda`). Method: per-repo heartbeat-vs-git verification at
> `origin/main` HEAD, run 2026-07-12 ~04:00–05:00Z — each repo's
> `control/status.md` claims spot-checked against last commits, open PRs, and
> CI (GitHub MCP + fetched local checkouts). Trigger snapshot refreshed the
> same session: **783 triggers** (8 MCP pages, all ids unique) →
> `telemetry/triggers-snapshot.json`. Verdicts are claims-vs-reality within a
> ~3-day heartbeat window; a <1-day-old heartbeat whose claims are
> contradicted by git is STALE, an hours-lagged but accurate one is FRESH.

## Verdict table

One row per repo, grouped by seat. Seat roll-up = worst constituent repo.

| Seat | Repo | Heartbeat stamp | Last main commit (sha, date) | Open PRs | CI | Verdict |
|---|---|---|---|---|---|---|
| **fleet-manager** — FRESH | menno420/fleet-manager | 2026-07-11T23:50:47Z | `cb91fda3` 2026-07-12T03:28:51Z | #103, #92 | substrate-gate green on `cb91fda3` | **FRESH** (~3.5h benign lag) |
| **superbot-2.0** — FRESH | menno420/superbot | 2026-07-11T19:45:00Z | `1ecc211` 2026-07-11T23:32:12Z (#2014) | none | green on `1ecc211` (all workflows success) | **FRESH** |
| | menno420/superbot-next | 2026-07-12T03:45Z | `95b6fda` 2026-07-12T03:35:04Z (#231) | none | `ci` + `named-gates` green on `95b6fda`; `golden-parity` workflow red-by-design (non-required `report` job; required gate GREEN 346/346) | **FRESH** |
| **websites** — FRESH | menno420/websites | 2026-07-11T19:49:00Z | `8f97654` 2026-07-11T22:33:14Z (#156) | none | green — quality.yml run #377 success on `8f97654` | **FRESH** |
| **self-improvement** — FRESH | menno420/substrate-kit | 2026-07-12T00:24:29Z | `8a544a6` 2026-07-12T00:26:33Z (#256) | #238, #220 (both deliberate `do-not-automerge` owner-ratification pins) | success (run 581, `1295d73`); newest 2 control-only merges path-filtered | **FRESH** |
| **superbot-world** — **STALE** | menno420/superbot-games | 2026-07-11T19:39:14Z | `5ddfbee` 2026-07-11T22:29:02Z (#58) | #59, #60 (both post-heartbeat) | substrate-gate + tests green on `5ddfbee` | **STALE** — heartbeat contradicted (see below) |
| | menno420/superbot-idle | 2026-07-11T19:37:36Z | `c6a349d` 2026-07-11T19:42:13Z (#71) | #72 | substrate-gate + theme-gate green on `c6a349d` | **FRESH** (dormant lane resumed via #72 without re-stamp) |
| | menno420/superbot-mineverse | 2026-07-11T19:45:00Z | `76be821` 2026-07-11T19:46:19Z (#41) | #42, #31 | green on parent `a19e420`; **no workflow runs for HEAD `76be821` or PR #42's head** | **FRESH** (2 anomalies) |
| **game-lab** — FRESH | menno420/gba-homebrew | 2026-07-11T21:03:45Z | `d1ec24f` 2026-07-11T22:29:21Z (#59) | none | substrate-gate + ROM builds green on `d1ec24f` | **FRESH** |
| | menno420/pokemon-mod-lab | 2026-07-11T21:03:45Z | `08d2611` 2026-07-11T22:29:20Z (#52) | none | substrate-gate + rom-builds green on `08d2611` | **FRESH** |
| **ideas-lab** — FRESH | menno420/idea-engine | 2026-07-12T03:29:00Z | `6d40f6f` 2026-07-12T03:38:47Z (#250) | none | success @ `ef46497`; HEAD run 2-min propagation lag | **FRESH** |
| | menno420/sim-lab | 2026-07-12T03:25:00Z | `e857b24` 2026-07-12T03:27:15Z (#48) | none | substrate-gate green on `e857b24` | **FRESH** |
| **venture-lab** — FRESH | menno420/venture-lab | 2026-07-12T00:26:56Z | `b633db6` 2026-07-12T00:32:21Z (#61) | #57 (parked owner-merge), #51 (⚑ HOT owner upload) | green at `296a1a9`; **no main runs for 3 newest bot-merged commits** | **FRESH** |
| | menno420/trading-strategy | 2026-07-11T19:33:12Z | `ea22323` 2026-07-11T22:33:39Z (#63) | #65, #64 (parked green) | substrate-gate + tests green on `ea22323` | **FRESH-borderline** — drifts STALE if parked PR #64 isn't merged by ~2026-07-14 |

### The one STALE: superbot-games

The heartbeat (`updated: 2026-07-11T19:39:14Z`) claims 5 open PRs (#50, #52,
#53, #54, #55) "parked on branches for owner merge" with main HEAD `5d38593`
and kit v1.12.0. Reality: **all five merged 2026-07-11 20:25–20:43Z**, ~1h
after the stamp, plus #56/#57/#58 after that; HEAD moved **8 merges** to
`5ddfbee` (kit now v1.12.1); two new PRs #59/#60 (2026-07-12) are open and
unmentioned. The heartbeat was accurate when written but the lane resumed
activity after its "close-out" stamp without re-stamping `control/status.md`.

## Needs attention (manager shortlist, priority order)

1. **venture-lab PR #51 — ⚑ HOT, owner-only cleanup.** 10 full-res
   unwatermarked owner photos publicly downloadable since 2026-07-11T18:24Z
   (branch `menno420-patch-1`). Owner must close the PR + delete the branch.
2. **superbot-games heartbeat contradicted** — lane must re-stamp
   `control/status.md` (see STALE verdict above).
3. **superbot-mineverse PR #42** (login-CSRF security fix) — zero check runs
   ever started on its head (known platform issue: merge ref never built);
   merge blocked until checks are (re)triggered.
4. **trading-strategy succession fix stuck in parked PR #64** — the
   2026-07-17 grading-pass executor fix (re-armed trigger
   `trig_015aNMg5ncoSE2Roe4MKjQnr`) rides unmerged #64 while main still says
   "NO executor" (⚑ (g)); a reader of main gets a materially wrong risk
   picture.
5. **Bot-merged commits skip main-branch CI in venture-lab** — GITHUB_TOKEN
   (auto-merge enabler) merges don't trigger push workflows; last verified
   main run is at `296a1a9`, nothing for `305646f`/`8d77a08`/`b633db6`.
6. **superbot-next golden-parity workflow is red-by-design on every main
   push** (non-required `report` job stays red until full parity). Oversight
   tooling keying on workflow-run *conclusion* will falsely flag it every
   sweep — key on required-check conclusions instead.
7. **fleet-manager roster-regen run failed 03:02:09Z on main** (`ff4be550`)
   though its output PR #104 merged 2 min later — unexplained; and open PR
   #103 (prompts v3.1, a major deliverable) is absent from the manager
   heartbeat's Landed/parked section.
8. **idea-engine coordinator triggers were dismantled at archive** — the
   failsafe cron + send_later chain must be re-armed at next wake (Q-0265).
9. **Archived superbot-world lanes resumed activity without re-stamping** —
   all three "archived/dormant" lanes resumed within hours (games: 8 merges +
   2 PRs; idle: PR #72; mineverse: PR #42); only games crossed into
   contradiction so far.

## Roster cross-check (gen #12 vs this sweep)

Compared against the regenerated `docs/roster.md` (generation #12,
2026-07-12T03:52Z, built from the same 783-trigger snapshot). Mismatches are
**noted only** — the roster tables are generated output and out of scope for
this sweep.

**Agreements:** superbot-next, substrate-kit, venture-lab, idea-engine,
sim-lab — FRESH in both. superbot-games — STALE in both, but for different
reasons (roster: heartbeat age ~8h; sweep: contradicted claims). The
agreement is coincidental, not method agreement.

**Mismatches (8):** the roster marks **superbot (hub), websites,
trading-strategy, superbot-idle, superbot-mineverse, pokemon-mod-lab,
gba-homebrew, and fleet-manager** as STALE; this sweep verified all eight
**FRESH** (trading-strategy FRESH-borderline). Root cause: `gen_roster.py`
verdicts are purely heartbeat-age-threshold based (hours-scale), while the
sweep verdict is claims-vs-reality within a ~3-day window — an 8h-old but
accurate heartbeat is roster-STALE yet sweep-FRESH, and conversely an
age-based verdict cannot detect a minutes-old heartbeat whose claims are
already contradicted. Recommendation (not applied here): either widen the
roster's age threshold to match the sweep doctrine, or relabel the roster
column "heartbeat age class" so the two verdict kinds stop colliding.

**Not covered by this sweep** (roster rows with no sweep counterpart):
product-forge, retro-games coordinator (registry-only seat), the three
codetool-lab lanes (STALE-BY-DESIGN), and the DARK/DEAD `↳` sub-row
heartbeat files — the 8-seat sweep scope was the seats in `projects/`.

## Citations by seat

- **fleet-manager:** heartbeat `control/status.md` @ main `cb91fda3e742e43b65f9a7e4e3a888b2db1ce964`; commits via MCP `list_commits` (cb91fda3, bed56290, ec0b5f01, 639b0f09, 97e69c12); open PRs via `list_pull_requests` → #103, #92; CI via `actions_list` (substrate-gate success ×5, roster-regen failure 03:02:09Z on `ff4be550`).
- **superbot-2.0:** `git show origin/main:control/status.md` in `/home/user/superbot` and `/home/user/superbot-next`; `git log origin/main -5` each; MCP open PRs → `[]` both; CI via `actions_list` branch=main; superbot-next parity counts hand-verified against `origin/main:parity/parity.yml` (44 ported + kernel = 45 gate rows; gate 346/346, run 29178063196 job 86610739481).
- **websites:** `origin/main` = `8f9765483a7df57ce426e7d11d200f10b5495ed7` via local checkout; heartbeat `control/status.md` (19:49:00Z); MCP open PRs → `[]`; quality.yml run #377 success; PR #141 merged by owner 2026-07-11T20:24:48Z.
- **self-improvement:** `/home/user/substrate-kit` @ origin/main `8a544a6`; heartbeat 00:24:29Z; claims confirmed — #256 merge is HEAD, `b862e9a` ancestor of main, tag v1.12.1 → `203bb09`; open PRs #238/#220 both `do-not-automerge`; CI run 581 success on `1295d73`.
- **superbot-world:** `git -C /home/user/<repo> fetch origin main` + `show origin/main:control/status.md` ×3 + MCP PRs/CI. games: 5 claimed-parked PRs all merged 20:25–20:43Z, HEAD `5ddfbee`, open #59/#60. idle: HEAD `c6a349d` = heartbeat commit; open #72 (00:21Z). mineverse: HEAD `76be821` (#41); open #42 (23:26Z) + #31; no Actions runs after 19:27Z (checked 30 of 71 runs newest-first).
- **game-lab:** local checkouts @ origin/main; both heartbeats stamped identically 2026-07-11T21:03:45Z (same scheduler minute); gba-homebrew ROM claims byte- and sha256-verified (`gloamline.nds` 110,080 B `25ae4f81…`; `brineward.nds` 108,032 B `89e68dc2…`); pokemon-mod-lab stale refs `track-a/session-019`/`-024` confirmed via `ls-remote`; CI green on both HEADs.
- **ideas-lab:** heartbeats 03:29:00Z / 03:25:00Z read at origin/main; cross-references byte-consistent both directions (idea-engine cites sim-lab #47 `4984069` / #48 `e857b24`; sim-lab's promised fan-in landed as idea-engine #249 `ef46497`); 0 open PRs; CI green (HEAD `6d40f6f` run 2-min propagation lag).
- **venture-lab:** heartbeats 00:26:56Z / 19:33:12Z at origin/main after fetch (advanced `2044dc6`→`b633db6`, `d3ae8f4`→`ea22323`); venture-lab open [#57](https://github.com/menno420/venture-lab/pull/57), [#51](https://github.com/menno420/venture-lab/pull/51); trading-strategy open [#65](https://github.com/menno420/trading-strategy/pull/65), [#64](https://github.com/menno420/trading-strategy/pull/64); CI green at `296a1a9` / `ea22323`.
