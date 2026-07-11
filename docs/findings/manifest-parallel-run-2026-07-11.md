# Parallel-run: fm roster gen #4 vs superbot fleet-manifest — 2026-07-11

> **Status:** `finding` — the one-parallel-run-wake condition from
> `docs/proposals/generated-roster-from-heartbeats.md` (phase 2) is MET by this run.
> Produced by the roster-gen-4 lane worker (model: fable-5), dispatched by successor
> coordinator cse_012o8pySy5K3AV6JWoPKryZL.
>
> **Compared:** fm `docs/roster.md` **generation #4** (generated-at 2026-07-11T01:58Z;
> 232-record trigger sweep ~01:52Z + ls-remote-verified heartbeats) vs superbot
> **`docs/eap/fleet-manifest.md`** @ blob SHA `d3c0e1c2d2a186c622564a5eb399975fc4c97f87`
> (fetched at superbot HEAD `a7623844`, 2026-07-11T01:26:07Z). The manifest's own header
> says it was last re-stamped **2026-07-10T16:38Z** — **~33.5h before this run**.

## Verdict, one line

The manifest is stale on every axis the roster measures: **5 live lanes missing, 9 of
10 live-lane rows factually wrong on trigger/cadence/kit/status; only the websites
trigger id survives contact with the live registry.**

## Discrepancy table (per lane)

| Lane | superbot manifest says (@ `d3c0e1c`) | fm roster gen #4 verified reality | Citation |
|---|---|---|---|
| manager (fleet-manager) | trigger `trig_01QBrp5MjZL3F9mv6KsTXTzN` "WORKS"; kit v1.4.0; ORDERs 001/003/007/008 open | that trigger deleted TWICE over (→ `trig_014odnv5h1tkJAFRhix3tGLq` Q-0265 cutover → deleted → successor `trig_01F9UdoUtLy8oknBPBkHLshS`, created 01:04:10Z); kit v1.7.0; inbox CLEAR, ORDERs 001–015 ALL done | fm PR #57/#58 + `control/status.md` @ `95a61cb`; live registry sweep 01:52Z |
| superbot (hub) | "Idea Engine seat pending owner Project click" | idea-engine is a LIVE lane with its own repo, failsafe + hot chain (heartbeat 01:52:41Z) | `idea-engine` @ `5b8fca7`; `trig_0178q9Je2xRFJgthwamrg9Br` |
| superbot-next (Builder) | "**none** — ORDER 008 unacked; no Builder trigger in the registry"; band 5 mid-mission; kit v1.6.0 | **Builder failsafe wake LIVE** `trig_01L5JBefGSCM1fUdwm4SRQnY` `0 */2 * * *` (fired 01:08:59Z) + chain; band-5 COMPLETE (#111 `569beea`); kit v1.8.0 (#135 `3dfc194`) | registry sweep; `superbot-next/control/status.md` @ `38d8999` |
| kit-lab (substrate-kit) | trigger `trig_016EfUawz6KxEYqUM6f1BqDw`; v1.7.0 | trigger superseded by `trig_019nbVSWfu9grKjeHks97CeU` (created 2026-07-10T23:09:56Z, the gen-#3 cutover); **v1.8.0 RELEASED** fully agent-side (claim #158 `c7c430f`, 938 tests) | registry sweep; `substrate-kit/control/status.md` @ `3179b31` |
| websites | trigger `trig_017H9Qb9oxtLgUy6sw2gnSHg` `0 */4` — **CORRECT (the only surviving trigger row)**; kit v1.6.0; ORDERs 001–008 | same trigger live (fired 00:02:41Z) ✓; but kit v1.8.0; ORDER 009 also done; slice 11 landed (#88) | registry sweep; `websites/control/status.md` @ `0c0ed95` |
| trading-strategy | trigger `trig_01Mvn5xRmqGmZJNRHgjqyLpN` `0 */4`; PARKED GREEN; holdout SEALED; kit v1.1.0 | trigger is `trig_01YBaVeKAW2fSD83S9F37s2d` **`0 */2`**; **PAPER LANE OPERATIONAL** (opens 07-11, 223 tests); holdout **SPENT** (consumed via #37, report FINAL); kit v1.7.1 (#44 `24649d7`) | registry sweep; `trading-strategy/control/status.md` @ `d0d789e` |
| venture-lab | "**none**"; ⚑B/⚑D FROZEN; ORDERs 002/003/004 pending; kit v1.6.0 | **failsafe LIVE** `trig_01X1dw1L1Udgt8atzzNWEJic` `0 */2` (armed 00:30:36Z) + chain; ORDERs 001–004 **ALL done** incl. the P0 Stripe fix (PR #16 `912da3e`); ⚑B/⚑D **UNFROZEN**, launch-ready; kit v1.8.0 (#17 `fb5ef4b`) | registry sweep; `venture-lab/control/status.md` @ `2021bab` |
| games-plugins (superbot-games) | "**none** — ORDER 002 unexecuted; relaunches clockless"; ORDER 001 P0 pending, boot-gating; kit v1.2.0 | **Seat A LIVE**: failsafe `trig_019ZgWyL78Rx1sr6LhvL8NE3` `15 */2` (fired 00:15:39Z) + chain; **ORDER 001 MERGED** (PR #24, merge `7d4c347`); 257 tests; kit v1.8.0 | registry sweep; `superbot-games/control/status.md` @ `8808374`; fm PR #58 |
| pokemon-mod-lab | "**none** — first relaunch must be externally fired"; LANE PARKED | **hourly wake LIVE** `trig_01BTJjkMVMKtWPjuYe7643Hi` `30 * * * *` (created 01:37:07Z, fresh-session mode); lane **UN-PARKED** — Q-0266 pick = Emerald QoL+ (the manifest's own recommendation, now taken) | registry sweep; `pokemon-mod-lab/control/status.md` @ `c692130` |
| gba-homebrew | "**none** — same clockless-first-session caveat"; 11 review-queue rows await; kit v1.6.0 | **hourly wake LIVE** `trig_0137SkvhXEJvwepX8aVNkcSn` `0 * * * *` (created 01:36:30Z); session 8 running — 11 of 12 review-queue rows closed, 2 engine defects fixed; kit v1.8.0 | registry sweep; `gba-homebrew/control/status.md` @ `6565458` |
| codetool ×3 | Projects CLOSED, repos retained | unchanged ✓ (`a6cf1a9` / `80f6cd1` / `66c3dfc`, ls-remote-verified) | roster gen #4 |
| mobile-lab | repos NOT created, ready-not-launched | unchanged as stated ✓ (no contrary evidence this sweep) | — |
| **superbot-idle** | **ROW MISSING** | live lane, Seat B: heartbeat 01:47:28Z, volume phase, kit v1.7.1, failsafe `trig_01TWKGFW8RUsMvxUMt2ndzqA` `45 */2` + chain | `superbot-idle/control/status.md` @ `97bfff2` |
| **superbot-mineverse** | **ROW MISSING** (repo born this window) | live lane: ORDER 000 walking skeleton merged; failsafe `trig_01K8xmAKYS5S2HLy1HPANM7j` `20 */2` (armed 01:30:43Z) + chain link `trig_01A9Zh2vh47V8fXwPtKYMSpk`; kit v1.8.0 | `superbot-mineverse/control/status.md` @ `1120a3b` |
| **retro-games coordinator** | **ROW MISSING** (seat born this window) | coordinator seat, NO repo (`superbot-retro` does not exist per ls-remote): failsafe `trig_01Y99uDKNtKTz2EtRYPWZkGY` `50 */2` (armed 01:16:16Z), drives gba + pokemon as child sessions | registry sweep (session `session_01BqCRbGYGeo97sFxMJHzu1e`) |
| **idea-engine** | **ROW MISSING** (only alluded to as "pending owner click" on the hub row) | live lane: heartbeat 01:52:41Z, kit v1.8.0, failsafe + chain | `idea-engine` @ `5b8fca7` |
| **sim-lab** | **ROW MISSING** | live lane: VERDICTs 001–005 finalized, harness v0.1.0 (#19), kit v1.7.0, failsafe `0 1-23/2` + idle-cadence pacemaker | `sim-lab` @ `0368600` |
| **product-forge** | **ROW MISSING** | live lane: games-web phase-1 complete, kit v1.7.0, failsafe + chain (WATCH: heartbeat 22:22Z) | `product-forge` @ `77f5231` |

## ⚑ Phase-2 recommendation (decide-and-flag — decided, owner may veto)

**Make fm `docs/roster.md` the canonical fleet registry; reduce
`docs/eap/fleet-manifest.md` to a pointer stub; retire superbot's
`check_manifest_freshness.py` per its own kill-switch header.**

One-line rationale: the manifest failed the parallel-run on every measured axis
(~33.5h stale, 5 live lanes missing, 9/10 live rows factually wrong) while the roster
regenerates ≤~2h (R25) from the live trigger registry + ls-remote-verified heartbeats —
keeping both is pure drift surface with no consumer the roster doesn't serve better.

**Not executed here:** this slice does not touch the superbot repo. The superbot-side
edit (pointer-stub the manifest + retire the checker) routes to a follow-up order.

## If the owner instead keeps the manifest: exact re-stamps it needs

1. manager row → successor trigger `trig_01F9UdoUtLy8oknBPBkHLshS`, kit v1.7.0, inbox clear (001–015 done).
2. superbot-next row → Builder failsafe live (`trig_01L5JBefGSCM1fUdwm4SRQnY`), band-5 complete, kit v1.8.0.
3. kit-lab row → trigger `trig_019nbVSWfu9grKjeHks97CeU`, v1.8.0 released.
4. websites row → kit v1.8.0, ORDERs 001–009 done.
5. trading row → trigger `trig_01YBaVeKAW2fSD83S9F37s2d` `0 */2`, PAPER LANE OPERATIONAL, holdout SPENT, kit v1.7.1.
6. venture-lab row → failsafe live, ORDERs 001–004 done, ⚑B/⚑D unfrozen, kit v1.8.0.
7. games-plugins row → Seat A live, ORDER 001 merged (PR #24 `7d4c347`), kit v1.8.0.
8. pokemon row → hourly wake live, lane UN-PARKED (Emerald QoL+).
9. gba row → hourly wake live, session 8, kit v1.8.0.
10. ADD six rows: superbot-idle, superbot-mineverse, retro-games coordinator (no repo), idea-engine, sim-lab, product-forge.
11. Post-launch note → its "remaining live lanes carry pending self-arm ORDERs" sentence is now false everywhere (all self-arms executed).
