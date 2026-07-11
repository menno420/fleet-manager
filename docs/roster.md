# Fleet roster — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — do not hand-edit; regenerated each manager wake (`scripts/gen_roster.py`, R25).**
>
> **Generation #6** · generated-at **2026-07-11T18:46Z** · by lane worker (fable-5), dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL · machine generation (`scripts/gen_roster.py`)
>
> **Source of truth = the lane heartbeats** (each repo's `control/status*.md` at an ls-remote-verified HEAD over git transport) + the live trigger registry (`list_triggers` export). This file is a derived snapshot. **Kill-switch: if this file's generated-at goes stale >24h, trust the heartbeats directly** — do not act on a stale roster row.
>
> **Transport verification:** every repo HEAD below was fetched shallow and re-fetched until FETCH_HEAD == a fresh `git ls-remote` (stale-proxy-pack doctrine, roster gen #3); all repos converged on the first fetch. Repos that could not be read are marked NOT MEASURED with the verbatim wall reason — never guessed.
>
> **Trigger evidence:** 690-record export, **21 enabled**: 7 standing crons + 2 poke-only + 12 one-shots.

| Lane | Heartbeat `updated:` | Age | Verdict | Phase (machine-truncated) | Orders | Kit | Wake state (trigger · cron · last fire) | Evidence (repo @ HEAD) |
|---|---|---|---|---|---|---|---|---|
| superbot (hub) | n/a — no control/status*.md at HEAD; HEAD committer date 2026-07-11T18:26Z used | ~19m | FRESH | — | — | — | poke-only `superbot night executor`; poke-only `suberbot docs reconciliation` | `d647b2e` 2026-07-11T18:26:07 |
| superbot-next | 2026-07-11T17:40Z | ~1h06m | FRESH | band-5 COMPLETE — live-bug fix lane DONE via #111 (merge `569beea`; CI https://github.com/menno420/superbot-next/actions/runs/29116022101 — all 6 checks in tha… | acked=001,002,003,004,005,006,007,008,009,010,011,012,013 done=003,005,006,007,008,009,010,011,012,… | v1.10.1 · check: green (#166 2026-07-11… | **Builder failsafe wake** `trig_01GLBYyf4aDS6AwpLVybZvVy` · `0 */2 * * *` · last 2026-07-11T18:06:28 · next 2026-07-11T20:07; +1 one-shot(s), next 2026-07-11T18:49 | `ab1e916` 2026-07-11T18:34:44 |
| substrate-kit | 2026-07-11T18:25:00Z | ~21m | FRESH | v1.12.0-WAVE SLICE CLOSED — KIT FIX + DISTRIBUTION (kit-dev lane, coordinator-dispatched worker) — two items shipped and merged this slice: **(1) currency scan… | acked=001,002,003,004,005,006,007,008,009,010,011,012,013 done=001,002,003,004,005,006,007,008,009,… | v1.12.0 · check: green · engaged: yes | +1 one-shot(s), next 2026-07-11T18:45 | `21f4450` 2026-07-11T18:22:01 |
| websites | 2026-07-11T16:27:00Z | ~2h19m | FRESH | CONTINUOUS MODE (manager Q-0265): 16:16Z nudge — slice 32 landed: #142 (rung-5 upkeep, buildable-now backlog empty): (a) HAND-KEPT-LIST AUDIT SWEEP — CLASS CLE… | acked=001-011 done=001-011 | v1.11.0 · check: green · engaged: yes | **websites lane wake — 4-hourly inbox ritual (ORDER 008)** `trig_017H9Qb9oxtLgUy6sw2gnSHg` · `0 */4 * * *` · last 2026-07-11T16:02:27 · next 2026-07-11T20:01 | `31cfd9f` 2026-07-11T17:20:42 |
| trading-strategy | 2026-07-11T10:09:08Z | ~8h36m | STALE | PAPER LANE OPERATIONAL — foundation complete on main. The standing mission after ORDER 008 (holdout SPENT, program complete, final report on main as ffdd6f6) i… | acked=001–010, done=001–010. ORDER 010 (P1, owner-directed fleet self-review): executed 2026-07-11 … | substrate-kit v1.7.1 — upgraded from v1… | +1 one-shot(s), next 2026-07-17T09:00 | `2dd955d` 2026-07-11T17:20:32 |
| venture-lab | 2026-07-11T18:17:33Z | ~28m | FRESH | work loop — **owner-engaged creative wave landed (#44–#48) + 3 digital products launch-ready**. The frontier is **owner-gated** on two axes: **publish clicks**… | — | — | **NONE** | `dfe3332` 2026-07-11T18:44:54 |
| superbot-games · Seat A | 2026-07-11T13:19:52Z | ~5h26m | STALE | ORDER-004 owner-requested lane self-review — committed to this file (below) and shipped as a READY PR parked ⚑ for the owner's merge click; five feature PRs re… | acked=001,002,003,004 done=001,002 | — | **NONE** | `5d38593` 2026-07-11T17:22:53 |
| superbot-idle (Seat B) | 2026-07-11T18:41:14Z | ~4m | FRESH | STEADY-STATE HOLD — owner-requested idea batch fully shipped (PRs #52–#68: sim harness + provisional run, achievements + save v2, buy-max, bounded multipliers,… | acked=000-002 done=000-002 | v1.7.1 · check: green | +1 one-shot(s), next 2026-07-11T18:52 | `4b40be5` 2026-07-11T18:42:23 |
| superbot-mineverse | 2026-07-11T18:21:00Z | ~25m | FRESH | POLISH + ROBUSTNESS SHIPPED — PRs #32 (housekeeping) / #33 (a11y+responsive) / #34 (server robustness) all merged on green; pytest is now a VERIFIED-BLOCKING r… | acked=001,002 done=001,002 | v1.8.0 · check: green · engaged: yes # … | **superbot-mineverse failsafe wake** `trig_01K8xmAKYS5S2HLy1HPANM7j` · `20 */2 * * *` · last 2026-07-11T18:20:06 · next 2026-07-11T20:20; +1 one-shot(s), next 2026-07-11T18:43 | `8ee029d` 2026-07-11T18:44:17 |
| retro-games coordinator (no repo) | n/a — registry-only seat (no repo) | n/a | n/a (registry-only seat) | — | — | — | **superbot-retro failsafe wake** `trig_01Y99uDKNtKTz2EtRYPWZkGY` · `50 */2 * * *` · last 2026-07-11T16:50:09 · next 2026-07-11T18:50 | trigger registry only |
| pokemon-mod-lab | 2026-07-11T18:37:02Z | ~8m | FRESH | Option A (Emerald QoL+ deepening, Q-0266 flagged reversible | — | v1.12.0 (bumped by PR #43 since the las… | **pokemon-mod-lab hourly wake (ORDER 002)** `trig_01BTJjkMVMKtWPjuYe7643Hi` · `30 * * * *` · last 2026-07-11T18:36:24 · next 2026-07-11T19:36 | `24ed070` 2026-07-11T18:43:32 |
| gba-homebrew | 2026-07-11T18:25:00Z | ~21m | FRESH | **GLOAMLINE ARC — session 17 (slice 3): WALKING SKELETON SHIPPED.** | — | v1.12.0 · engaged: yes | **gba-homebrew hourly wake (ORDER 002)** `trig_0137SkvhXEJvwepX8aVNkcSn` · `0 * * * *` · last 2026-07-11T18:02:06 · next 2026-07-11T19:01 | `bc92ad1` 2026-07-11T18:30:11 |
| product-forge | 2026-07-11T10:27:30Z | ~8h18m | STALE | (no phase line; lane: builder (ORDER 001 · games-web) · continuous-mode) | acked=001,002,003,004 done=001,002,003 | — | **NONE** | `097f9b1` 2026-07-11T10:31:16 |
| idea-engine | 2026-07-11T18:40:08Z (real wall-clock via date -u, per the … | ~5m | FRESH | PROBE — this slice (branch probe/rebuild-release-testing-loop, claim #199): third TOP-5 item 2 rebuild-release-testing-loop PROBED (single-pass full battery, G… | acked=001-002 done=001-002 (inbox read FIRST this session at wake HEAD 5905208 — no new orders; ORD… | v1.10.0 · check: green · engaged: yes | +2 one-shot(s), next 2026-07-11T18:47 | `0a682a3` 2026-07-11T18:41:17 |
| sim-lab | 2026-07-11T18:26:30Z | ~19m | FRESH | continuous mode; VERDICT 011 (owner-002 — four-websites purpose-fit + nav-health audit, OWNER-DIRECT) FINALIZED — approve (serves-purpose on all four sites) + … | acked=ORDER-001 ORDER-002 done= (ORDER-001 model-attribution carried on the VERDICT 011 session car… | v1.7.0 · check: green (bootstrap.py che… | +1 one-shot(s), next 2026-07-11T18:47 | `45613e6` 2026-07-11T18:44:04 |
| codetool-lab-fable5 | 2026-07-09T20:06Z | ~46h40m | STALE-BY-DESIGN | wind-down complete — ready for archive + fresh session | acked=001,002,003,004 done=001,002,003,004 | — | **NONE** | `a6cf1a9` 2026-07-10T12:07:20 |
| codetool-lab-opus4.8 | 2026-07-09T20:11:35Z | ~46h34m | STALE-BY-DESIGN | wind-down complete — ready for archive + fresh session | acked=001,002,003,004 done=001,002,003,004 | — | **NONE** | `80f6cd1` 2026-07-09T20:13:54 |
| codetool-lab-sonnet5 | 2026-07-09T20:02:14Z | ~46h43m | STALE-BY-DESIGN | wind-down complete — ready for archive + fresh session | acked=001,002,003,004 done=001,002,003,004 | — | **NONE** | `66c3dfc` 2026-07-09T20:09:52 |
| fleet-manager (this repo) | 2026-07-11T17:05:00Z — ORDER 017 EXECUTED (all 15 instructi… | ~1h41m | FRESH | **ORDER 017 DONE — THE FLEET-WIDE WALLED-INSTRUCTION RE-ISSUE IS BUILT (PR #77, PARKED READY for the owner's click): all 15 `projects/<repo>/instructions.md` v… | **016 DONE for its now-scope (PR #68 parked READY+green awaiting non-author landing; re-issue owner… | v1.7.0 · check: green · engaged: yes | **fleet-manager failsafe wake** `trig_01F9UdoUtLy8oknBPBkHLshS` · `30 */2 * * *` · last 2026-07-11T18:37:07 · next 2026-07-11T20:36; +1 one-shot(s), next 2026-07-11T19:10 | `39b888a` 2026-07-11T18:40:11 |

## Staleness verdicts (generation #6)

- **STALE:** trading-strategy, superbot-games · Seat A, product-forge
- **FRESH:** superbot (hub), superbot-next, substrate-kit, websites, venture-lab, superbot-idle (Seat B), superbot-mineverse, pokemon-mod-lab, gba-homebrew, idea-engine, sim-lab, fleet-manager (this repo)
- **STALE-BY-DESIGN:** codetool-lab-fable5, codetool-lab-opus4.8, codetool-lab-sonnet5
- **n/a (registry-only seat):** retro-games coordinator (no repo)

> Machine generation: the hand generations' "Deltas vs generation #N-1" narrative is coordinator judgment and is NOT auto-derived — read `git diff` on this file, or append prose below before committing.

## Deltas vs generation #5 (04:28Z → 18:46Z) — negative findings first

1. **NINE LANE FAILSAFES AUTO-DISABLED — `ended_reason=auto_disabled_env_deleted` (the
   sweep's headline).** Between ~14:45Z and ~16:16Z every 2-hourly lane failsafe bound to a
   deleted environment was auto-disabled by the platform (each id verbatim in the 690-record
   export, with its final fire): superbot-next `trig_01L5JBefGSCM1fUdwm4SRQnY` (last fired
   16:06:08Z), substrate-kit `trig_019nbVSWfu9grKjeHks97CeU` (16:01:50Z), trading-strategy
   `trig_01YBaVeKAW2fSD83S9F37s2d` (16:02:17Z), venture-lab `trig_01X1dw1L1Udgt8atzzNWEJic`
   (16:09:44Z), superbot-games `trig_019ZgWyL78Rx1sr6LhvL8NE3` (16:16:02Z), superbot-idle
   `trig_01TWKGFW8RUsMvxUMt2ndzqA` (14:45:48Z), product-forge `trig_012EvztCrHHg7s4mBsKT3VKs`
   (16:08:17Z), idea-engine `trig_0178q9Je2xRFJgthwamrg9Br` (16:05:09Z), sim-lab
   `trig_01SHfnLv6EqZesr4tC3T9kUU` (15:04:20Z). Timing correlates with the env-consolidation
   wave (fm ORDER 018 lineage / owner env deletions). **Only superbot-next re-armed** — new
   "Builder failsafe wake" `trig_01GLBYyf4aDS6AwpLVybZvVy` (`0 */2 * * *`, firing, last
   18:06:28Z). Net: **8 live lanes now have NO standing wake** and survive on send_later
   chain links alone (12 enabled one-shots at export time) — a chain break makes a lane go
   dark *silently*. ⚑ ESCALATE: re-arm failsafes for the 8 lanes (or record the intended
   consolidation target). Standing crons 15 → 7; enabled 32 → 21; export 324 → 690 records
   (growth is mostly spent one-shot chain links).
2. **STALE ×3 (gen #5 had 1, and it recovered).** (a) **trading-strategy** ~8h36m —
   `updated: 2026-07-11T10:09:08Z` at HEAD `2dd955d` (17:20:32Z, a kit-v1.12.0 session, not
   the lane); lane idles by design pending the weekly grading cadence (protocol §6, next
   2026-07-17) but its failsafe is among the 9 dead → nothing wakes it for that pass. (b)
   **superbot-games** ~5h26m — heartbeat lag, not idleness: `updated: 13:19:52Z` while the
   repo ran hot to `5d38593` 17:22:53Z (see recovery, item 3). (c) **product-forge** ~8h18m —
   `updated: 10:27:30Z`, HEAD `097f9b1` 10:31:16Z: heartbeat AND repo both idle ~8h **and**
   its failsafe is dead → the fleet's top DARK candidate for gen #7. Its gen-#5 FUTURE-DATED
   stamp bug (12:00:00Z) is meanwhile FIXED — the stamp is now sane and past-dated.
3. **superbot-games seat RECOVERED (the gen-#5→#6 window's good news), verified against
   commits.** The lane itself owns the gap in its status at `5d38593`: "no lane output
   ~02:15Z → ~11:xxZ; ORDER 003 (filed 03:32Z) and ORDER 004 (filed 09:59Z) sat unconsumed;
   status.md went stale (last written 01:49Z)". Recovery evidence: ORDERs 003+004 executed
   13:41Z (`82084aa` PR #46, `201f8dd` PR #47); the owner cleared the five parked PRs
   (#34 `5147a23` 13:40:40Z, #36 `325c567` 13:40:49Z, #27 `50f6774` 14:56:05Z, #32 `f9c2f7a`
   14:56:17Z, #38 `2f1e7cd` 14:56:26Z); D&D walking skeleton landed (#48 `b835f59` 15:03:41Z)
   and the menu-balance sim (#49 `5d38593` 17:22:53Z). Residual watch: heartbeat discipline
   (item 2b) — activity outran the status stamp by ~4h.
4. **Fleet self-review (owner order, due since ~10:00Z): sim-lab ANSWERED · superbot hub
   STILL MISSING.** (a) **sim-lab**: "Self-review 2026-07-11 (ORDER-002)" landed in
   control/status.md at `87ca0dfb` (17:17:30Z, PR #37) — digest: VERDICTs 009+010 finalized
   clean; the self-check battery caught a real escrow-pot model bug BEFORE finalization;
   standing watches OA-002 (Codex usage-capped — no Codex evidence folded into any verdict
   yet) + OA-004 (tag-push 403). Note: later wholesale heartbeat overwrites (#39 `d461932`,
   #41 `4c74d7aa`) dropped the section — it survives only in git history and the current
   status says "section stands from the prior heartbeat"; harmless but a
   single-writer-overwrite convention gap. (b) **superbot hub**: ORDER 002 (filed 10:01Z)
   still `status: new` in control/inbox.md at HEAD `d647b2e` — hub-touching sessions since
   (fleet review PR #1998, merged 18:26:07Z) did NOT consume it; no "Self-review 2026-07-11"
   exists anywhere in the repo (code search, 1 hit = the order text itself). Also answered
   elsewhere this window, for the record: superbot-games ORDER 004 (`201f8dd`),
   trading ORDER 010 (`ed8add3` 10:13:19Z), venture-lab ORDER 006 (status at `dfe3332`).
5. **fm PR #77 (ORDER 017 instruction re-issue) is MERGED, not parked** — on main as
   `39b888a` (18:40:11Z); the owner's click landed between gen #5 and this sweep. The
   fleet-manager row's heartbeat (17:05Z) still describes it as parked — superseded by this
   note; next fm heartbeat should re-stamp.
6. **Kit v1.11→v1.12 wave spread during the window:** substrate-kit itself v1.12.0
   (`21f4450`), pokemon v1.12.0 (PR #43), gba v1.12.0, superbot-games v1.12.0 (#51
   `396144d`), trading v1.12.0 (#61 `2dd955d`); websites at v1.11.0, superbot-next v1.10.1,
   idle v1.7.1, sim-lab v1.7.0 — spread is wide but no lane reports a red kit gate.
7. **No DARK, no DEAD, no walls:** every repo converged on the first ls-remote-verified
   fetch; the surviving 7 standing crons all fired on schedule in the last cycle (retro
   16:50:09Z, fm 18:37:07Z, mineverse 18:20:06Z, pokemon 18:36:24Z, gba 18:02:06Z, websites
   16:02:27Z, next 18:06:28Z). No seats born or retired; the three codetool seats stay
   STALE-BY-DESIGN (~46h, unchanged since wind-down).

## Tool-verification run 2 — hand sample vs machine output (generation #6)

Sample: 6 lanes spanning every verdict class present this generation (no DARK/DEAD exist to
sample). Ground truth: GitHub MCP Contents API pinned to the roster's evidence SHA +
`list_commits`; ages hand-computed against --date 2026-07-11T18:46Z; hand verdicts derived
independently from the documented ladder.

| Lane (sample class) | Machine verdict | Hand verdict | Cell-by-cell | Match? |
|---|---|---|---|---|
| trading-strategy (STALE) | STALE | STALE | `updated:` 10:09:08Z ✓ (file@`2dd955d`) · age ~8h36m ✓ (hand 8h36m52s, floored) · evidence `2dd955d` 17:20:32Z ✓ · wake = one-shot only ✓ (failsafe auto-disabled) | ✅ |
| superbot-games (STALE) | STALE | STALE | `updated:` 13:19:52Z ✓ (file@`5d38593`) · age ~5h26m ✓ (hand 5h26m08s) · evidence `5d38593` 17:22:53Z ✓ (= PR #49 merge) · wake NONE ✓ | ✅ |
| venture-lab (FRESH, triggerless probe) | FRESH | FRESH | `updated:` 18:17:33Z ✓ (file@`dfe3332`) · age ~28m ✓ (hand 28m27s) · evidence `dfe3332` 18:44:54Z ✓ (PR #52 merge) · wake NONE ✓ (failsafe auto-disabled; chain-only) | ✅ |
| sim-lab (FRESH, moved mid-sweep) | FRESH | FRESH | `updated:` 18:26:30Z ✓ at the fetched HEAD `45613e6` · age ~19m ✓ (hand 19m30s) · repo moved to `4c74d7aa` (18:46:48Z) seconds AFTER the verified fetch — world movement, not a tool error | ✅ |
| superbot (hub fallback) | FRESH | FRESH | no control/status.md at HEAD confirmed via Contents API (verbatim: "path does not point to a file…") ✓ · HEAD-date fallback `d647b2e` 18:26:07Z ✓ (PR #1998 merge) · age ~19m ✓ (hand 19m53s) | ✅ |
| codetool-lab-opus4.8 (parked) | STALE-BY-DESIGN | STALE-BY-DESIGN | `updated:` 2026-07-09T20:11:35Z ✓ · age ~46h34m ✓ (hand 46h34m25s) · evidence `80f6cd1` 2026-07-09T20:13:54Z ✓ (list_commits exact) | ✅ |

**Outcome: verdicts 6/6 correct, every heartbeat/age/evidence cell matched ground truth,
zero fixes needed. This is verification run 2 (run 1 found + fixed the age_str display bug);
the Q-0105 UNVERIFIED header stays until more clean runs accumulate per its own criteria.**
