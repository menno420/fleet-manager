# Fleet roster — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — do not hand-edit; regenerated each manager wake (`scripts/gen_roster.py`, R25).**
>
> **Generation #5** · generated-at **2026-07-11T04:28Z** · by lane worker (fable-5), dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL · machine generation (`scripts/gen_roster.py`)
>
> **Source of truth = the lane heartbeats** (each repo's `control/status*.md` at an ls-remote-verified HEAD over git transport) + the live trigger registry (`list_triggers` export). This file is a derived snapshot. **Kill-switch: if this file's generated-at goes stale >24h, trust the heartbeats directly** — do not act on a stale roster row.
>
> **Transport verification:** every repo HEAD below was fetched shallow and re-fetched until FETCH_HEAD == a fresh `git ls-remote` (stale-proxy-pack doctrine, roster gen #3); all repos converged on the first fetch. Repos that could not be read are marked NOT MEASURED with the verbatim wall reason — never guessed.
>
> **Trigger evidence:** 324-record export, **32 enabled**: 15 standing crons + 2 poke-only + 15 one-shots.

| Lane | Heartbeat `updated:` | Age | Verdict | Phase (machine-truncated) | Orders | Kit | Wake state (trigger · cron · last fire) | Evidence (repo @ HEAD) |
|---|---|---|---|---|---|---|---|---|
| superbot (hub) | n/a — no control/status*.md at HEAD; HEAD committer date 2026-07-11T03:43Z used | ~44m | FRESH | — | — | — | poke-only `superbot night executor`; poke-only `suberbot docs reconciliation` | `bd80501` 2026-07-11T03:43:26 |
| superbot-next | 2026-07-11T03:30Z | ~58m | FRESH | band-5 COMPLETE — live-bug fix lane DONE via #111 (merge `569beea`; CI https://github.com/menno420/superbot-next/actions/runs/29116022101 — all 6 checks in tha… | acked=001,002,003,004,005,006,007,008,009,010,011 done=003,005,006,007,008,009,010,011 — ORDER 004:… | v1.8.0 · check: green (#135's own ladde… | **Builder failsafe wake** `trig_01L5JBefGSCM1fUdwm4SRQnY` · `0 */2 * * *` · last 2026-07-11T04:06:08 · next 2026-07-11T06:05; +1 one-shot(s), next 2026-07-11T04:28 | `531f14e` 2026-07-11T04:23:19 |
| substrate-kit | 2026-07-11T04:25:00Z | ~3m | FRESH | ORDER 012 EXECUTED (model-attribution ground truth, P3 — the last open inbox order). Check-first verdicts: item 1 (session-card template carries `📊 Model:`) AL… | acked=001,002,003,004,005,006,007,008,009,010,011,012 done=001,002,003,004,005,006,007,008,009,010,… | v1.8.0 · check: green · engaged: yes | **substrate-kit failsafe wake** `trig_019nbVSWfu9grKjeHks97CeU` · `0 */2 * * *` · last 2026-07-11T04:01:54 · next 2026-07-11T06:01; +1 one-shot(s), next 2026-07-11T04:28 | `2a779b5` 2026-07-11T04:26:15 |
| websites | 2026-07-11T04:24:00Z | ~4m | FRESH | CONTINUOUS MODE (manager Q-0265): 04:12Z nudge — slice 15 landed: #99 (bus doctrine "Landing other sessions' control-only work" in control/README.md — one WRIT… | acked=001-010 done=001-010 | v1.8.0 · check: green · engaged: yes | **websites lane wake — 4-hourly inbox ritual (ORDER 008)** `trig_017H9Qb9oxtLgUy6sw2gnSHg` · `0 */4 * * *` · last 2026-07-11T04:02:32 · next 2026-07-11T08:01 | `1b6dad9` 2026-07-11T04:24:08 |
| trading-strategy | 2026-07-11T04:07:33Z | ~20m | FRESH | PAPER LANE OPERATIONAL — foundation complete on main. The standing mission after ORDER 008 (holdout SPENT, program complete, final report on main as ffdd6f6) i… | acked=001–009, done=001–009. ORDER 009 (P3, model-attribution ground truth + trading#21 P1-drops re… | substrate-kit v1.7.1 — upgraded from v1… | **trading-strategy failsafe wake** `trig_01YBaVeKAW2fSD83S9F37s2d` · `0 */2 * * *` · last 2026-07-11T04:02:07 · next 2026-07-11T06:01; +1 one-shot(s), next 2026-07-17T09:00 | `f4d9669` 2026-07-11T04:11:01 |
| venture-lab | 2026-07-11T02:58:38Z | ~1h29m | FRESH | work loop — **launch-ready ×3 products (membership-kit, template-packs, stripe-webhook-test-kit)**. The frontier is now **owner-gated** (publish clicks + Strip… | — | — | **venture-lab failsafe wake** `trig_01X1dw1L1Udgt8atzzNWEJic` · `0 */2 * * *` · last 2026-07-11T04:09:44 · next 2026-07-11T06:08; +1 one-shot(s), next 2026-07-11T04:54 | `051ee59` 2026-07-11T03:30:13 |
| superbot-games · Seat A | 2026-07-11T01:49:48Z | ~2h38m | FRESH | theme leaks R2 cleared — mining's grid/market/taxonomy player-visible nouns moved out of branching logic into swappable DATA tables keyed on neutral ids; READY… | acked=001,002 done=001,002 | — | **superbot-games failsafe wake** `trig_019ZgWyL78Rx1sr6LhvL8NE3` · `15 */2 * * *` · last 2026-07-11T04:15:27 · next 2026-07-11T06:15; +1 one-shot(s), next 2026-07-11T04:54 | `72612a1` 2026-07-11T03:33:17 |
| superbot-idle (Seat B) | 2026-07-11T04:23:53Z | ~4m | FRESH | STEADY-STATE HOLD — founding package complete, volume backlog cleared honestly (44 PRs, zero denials, zero parked); lane deliberately holds new engine surface … | acked=000-001 done=000-001 | v1.7.1 · check: green | **superbot-idle failsafe wake** `trig_01TWKGFW8RUsMvxUMt2ndzqA` · `45 */2 * * *` · last 2026-07-11T02:45:09 · next 2026-07-11T04:45; +2 one-shot(s), next 2026-07-11T04:29 | `1b3a211` 2026-07-11T04:24:48 |
| superbot-mineverse | 2026-07-11T04:27:00Z | ~1m | FRESH | DEEPENING — micro-polish (PR #23) MERGED: read side now renders the ENTIRE v1 contract, the deepening well is dry; no in-flight lanes — all remaining work exte… | acked=001 done=001 | v1.8.0 · check: green · engaged: yes # … | **superbot-mineverse failsafe wake** `trig_01K8xmAKYS5S2HLy1HPANM7j` · `20 */2 * * *` · last 2026-07-11T04:20:41 · next 2026-07-11T06:20; +2 one-shot(s), next 2026-07-11T04:35 | `2b1bd0b` 2026-07-11T04:28:10 |
| retro-games coordinator (no repo) | n/a — registry-only seat (no repo) | n/a | n/a (registry-only seat) | — | — | — | **superbot-retro failsafe wake** `trig_01Y99uDKNtKTz2EtRYPWZkGY` · `50 */2 * * *` · last 2026-07-11T02:50:27 · next 2026-07-11T04:50; +1 one-shot(s), next 2026-07-11T04:31 | trigger registry only |
| pokemon-mod-lab | 2026-07-11T04:03:05Z | ~24m | FRESH | Option A (Emerald QoL+ deepening, Q-0266 flagged reversible | — | v1.6.0 · check: green · engaged: yes | **pokemon-mod-lab hourly wake (ORDER 002)** `trig_01BTJjkMVMKtWPjuYe7643Hi` · `30 * * * *` · last 2026-07-11T03:36:20 · next 2026-07-11T04:36 | `297f67b` 2026-07-11T04:13:49 |
| gba-homebrew | 2026-07-11T03:40:00Z | ~48m | FRESH | session 8 slice 6 (same worker continuing) — **CONSOLIDATION shipped as Lumen Drift v1.3**: slice 5's ranked polish debt items 1–3 all paid (route-recorder pro… | acked=001,002 done=001 (this repo's half), 002 EXECUTED (slice 2) — trigger `trig_0137SkvhXEJvwepX8… | v1.8.0 · check: green (full --strict ex… | **gba-homebrew hourly wake (ORDER 002)** `trig_0137SkvhXEJvwepX8aVNkcSn` · `0 * * * *` · last 2026-07-11T04:02:26 · next 2026-07-11T05:01 | `a168bf1` 2026-07-11T03:40:09 |
| product-forge | 2026-07-11T12:00:00Z | future? | FRESH | (no phase line; lane: builder (ORDER 001 · games-web) · continuous-mode) | acked=001,002 done=001,002 | — | **product-forge failsafe wake** `trig_012EvztCrHHg7s4mBsKT3VKs` · `0 */2 * * *` · last 2026-07-11T04:08:20 · next 2026-07-11T06:07; +1 one-shot(s), next 2026-07-11T04:54 | `8c64db4` 2026-07-11T03:51:51 |
| idea-engine | 2026-07-11T04:26:22Z (real wall-clock, per the control/READ… | ~1m | FRESH | STEADY — superbot-mineverse FIRST BATCH shipped (this slice, branch seed-superbot-mineverse-batch-1): the roster-born empty section (stub @ PR #66) gets its fi… | acked=001 done=001 (inbox re-read FIRST this session at origin/main HEAD b13aa36 and re-checked at … | v1.8.0 · check: green · engaged: yes | **idea-engine failsafe wake** `trig_0178q9Je2xRFJgthwamrg9Br` · `0 */2 * * *` · last 2026-07-11T04:05:14 · next 2026-07-11T06:04; +2 one-shot(s), next 2026-07-11T04:29 | `a1b320a` 2026-07-11T04:28:13 |
| sim-lab | 2026-07-10T23:50:16Z | ~4h37m | STALE | continuous mode; VERDICT 005 finalized (INTAKE 005 → needs-more-evidence; ruling: annotate per-seat-type sections (CAPABILITIES.v1) — single-seat whole-file re… | acked= done= | v1.7.0 · check: green (substrate-gate: … | **sim-lab failsafe wake** `trig_01SHfnLv6EqZesr4tC3T9kUU` · `0 1-23/2 * * *` · last 2026-07-11T03:04:16 · next 2026-07-11T05:03; +2 one-shot(s), next 2026-07-11T04:54 | `f70fbea` 2026-07-11T03:30:46 |
| codetool-lab-fable5 | 2026-07-09T20:06Z | ~32h22m | STALE-BY-DESIGN | wind-down complete — ready for archive + fresh session | acked=001,002,003,004 done=001,002,003,004 | — | **NONE** | `a6cf1a9` 2026-07-10T12:07:20 |
| codetool-lab-opus4.8 | 2026-07-09T20:11:35Z | ~32h16m | STALE-BY-DESIGN | wind-down complete — ready for archive + fresh session | acked=001,002,003,004 done=001,002,003,004 | — | **NONE** | `80f6cd1` 2026-07-09T20:13:54 |
| codetool-lab-sonnet5 | 2026-07-09T20:02:14Z | ~32h25m | STALE-BY-DESIGN | wind-down complete — ready for archive + fresh session | acked=001,002,003,004 done=001,002,003,004 | — | **NONE** | `66c3dfc` 2026-07-09T20:09:52 |
| fleet-manager (this repo) | 2026-07-11T04:10:00Z — ORDER 010 relay COMPLETION slice (su… | ~18m | FRESH | **ORDER 010 RELAY COMPLETION DONE (PR #64) — the two lanes PR #63 could not reach are relayed: superbot-idle inbox ORDER 001 (idle PR #46, merge `6f94109`) + s… | **NONE OPEN — inbox CLEAR (001–015 all DONE).** 015 DONE (registry centralization, PR #58) · 014 DO… | v1.7.0 · check: green · engaged: yes | **fleet-manager failsafe wake** `trig_01F9UdoUtLy8oknBPBkHLshS` · `30 */2 * * *` · last 2026-07-11T02:34:16 · next 2026-07-11T04:36; +1 one-shot(s), next 2026-07-11T04:25 | `acb786f` 2026-07-11T04:17:34 |

## Staleness verdicts (generation #5)

- **STALE:** sim-lab
- **FRESH:** superbot (hub), superbot-next, substrate-kit, websites, trading-strategy, venture-lab, superbot-games · Seat A, superbot-idle (Seat B), superbot-mineverse, pokemon-mod-lab, gba-homebrew, product-forge, idea-engine, fleet-manager (this repo)
- **STALE-BY-DESIGN:** codetool-lab-fable5, codetool-lab-opus4.8, codetool-lab-sonnet5
- **n/a (registry-only seat):** retro-games coordinator (no repo)

> Machine generation: the hand generations' "Deltas vs generation #N-1" narrative is coordinator judgment and is NOT auto-derived — read `git diff` on this file, or append prose below before committing.

## Deltas vs generation #4 (01:58Z → 04:28Z) — headline first

1. **FIRST MACHINE GENERATION + tool-verification run 1 EXECUTED (the slice's core
   point).** Gen #5 is the first roster produced by `scripts/gen_roster.py` (PR #62,
   still Q-0105-UNVERIFIED at run time). A 6-lane hand sample spanning verdict classes
   was verified cell-by-cell against ground truth (table below): **all verdicts and
   heartbeat/evidence cells matched; ONE display bug found and fixed at root cause** —
   `age_str` float truncation rendered an exact 32h18m as `~32h17m`
   (`int((hours-h)*60)` on `17.999…`); fixed by rounding to whole seconds before
   flooring to minutes, regression selfchecks added, this file regenerated post-fix.
   The script's UNVERIFIED header stays (this is run 1 of the several its header
   requires); a verification-run log line was added under its Reliability field.
2. **NO DARK, NO DEAD — zero unmeasurable lanes.** Every repo converged on the first
   fetch (no stale proxy packs this sweep); no lane heartbeat is >24h except the three
   archived codetool seats (STALE-BY-DESIGN, ~32h, unchanged since wind-down).
3. **Sole STALE: sim-lab** — heartbeat 2026-07-10T23:50:16Z (~4h37m vs its 2h cadence
   bar of 4h), HEAD `f70fbea` 03:30:46Z. The lane itself declares **idle-by-design**
   ("QUEUE STATE: EMPTY — pending next idea-engine outbox pull", verbatim at HEAD;
   failsafe fired 03:04:16Z, next 05:03Z). Gen #4 classed this "benign heartbeat-lag";
   the machine ladder honestly reports it STALE — watch, not action. If gen #6 sees the
   heartbeat still at 23:50:16Z with the queue claiming activity, escalate.
4. **product-forge RECOVERED from gen #4's WATCH (the escalation candidate is CLEARED)
   — but its heartbeat is FUTURE-DATED (lane-side bug).** Gen #4's stalest live lane
   (~3h36m, HEAD unmoved since 22:46Z) moved: HEAD `8c64db4` 03:51:51Z, ORDERs 001+002
   done, PRs #1–#13 all merged. However `control/status.md` at that HEAD carries
   `updated: 2026-07-11T12:00:00Z` — **~7.5h in the future** at generation time
   (verbatim in the file; read via Contents API at HEAD `8c64db4`). The machine
   rendered it honestly (`Age: future?`; verdict FRESH holds on ground truth — HEAD is
   ~36m old). ⚑ route a relay: the lane should fix its stamp discipline, and a future
   `updated:` should be treated as suspect data.
5. **Registry growth: 232 → 324 records; enabled 31 → 32** (15 standing crons — steady
   — + 2 legacy poke-only + 15 one-shots). **All 15 standing lane crons from gen #4
   survived with identical trigger ids** (spot-compared id-by-id against the gen #4
   table: superbot-next `trig_01L5JBefGSCM1fUdwm4SRQnY`, kit
   `trig_019nbVSWfu9grKjeHks97CeU`, websites `trig_017H9Qb9oxtLgUy6sw2gnSHg`, trading
   `trig_01YBaVeKAW2fSD83S9F37s2d`, venture `trig_01X1dw1L1Udgt8atzzNWEJic`, games
   `trig_019ZgWyL78Rx1sr6LhvL8NE3`, idle `trig_01TWKGFW8RUsMvxUMt2ndzqA`, mineverse
   `trig_01K8xmAKYS5S2HLy1HPANM7j`, retro `trig_01Y99uDKNtKTz2EtRYPWZkGY`, pokemon
   `trig_01BTJjkMVMKtWPjuYe7643Hi`, gba `trig_0137SkvhXEJvwepX8aVNkcSn`, forge
   `trig_012EvztCrHHg7s4mBsKT3VKs`, idea-engine `trig_0178q9Je2xRFJgthwamrg9Br`,
   sim-lab `trig_01SHfnLv6EqZesr4tC3T9kUU`, fleet-manager
   `trig_01F9UdoUtLy8oknBPBkHLshS`). **None disabled, none vanished; zero live lanes
   triggerless** (gen #4's first-ever headline holds).
6. **No new seats born this window** (gen #4 had two births; gen #5 has none —
   superbot-mineverse and the retro coordinator are now steady-state rows).
7. **The fleet is HOT:** 11 of 14 live-lane heartbeats are <1h old at 04:28Z;
   superbot-next merged PR #145 (proof_channel parity flip) at 04:23:19Z — seconds
   before this sweep's fetch — and the ls-remote verify loop caught it (evidence
   `531f14e`).

## Tool-verification run 1 — hand sample vs machine output (generation #5)

Sample: 6 lanes spanning every verdict class present this generation (no DARK/DEAD
exist to sample). Ground truth channels: GitHub MCP Contents API + `list_commits` at
HEAD for 5 lanes; **superbot-mineverse via an independent shallow `git fetch` +
`ls-remote`** after the Contents API returned the session-scope wall verbatim
(`Access denied: repository "menno420/superbot-mineverse" is not configured for this
session` — the same wall gen #4 recorded). Hand verdicts derived independently from
the documented ladder (FRESH ≤ 2×cadence · STALE ≤24h · DARK >24h · DEAD unmeasurable;
archived → STALE-BY-DESIGN). Run-1 values computed against the first generation pass
(`--date 2026-07-11T04:24Z`); the shipped table above is the post-fix regeneration at
04:28Z.

| Lane (sample class) | Machine verdict | Hand verdict | Cell-by-cell | Match? |
|---|---|---|---|---|
| superbot-next (FRESH) | FRESH | FRESH | `updated:` 03:30Z ✓ · age ~54m ✓ · evidence `531f14e` 04:23:19Z ✓ (= live HEAD, PR #145 merge) · trigger id+cron ✓ | ✅ |
| sim-lab (STALE) | STALE | STALE | `updated:` 2026-07-10T23:50:16Z ✓ · age ~4h33m ✓ (hand: 4h33m44s, floored) · evidence `f70fbea` 03:30:46Z ✓ · cadence 2h from `0 1-23/2 * * *` ✓ | ✅ |
| fleet-manager (manager row) | FRESH | FRESH | `updated:` 04:10:00Z ✓ · age ~14m ✓ · evidence `acb786f` = origin/main ✓ · failsafe id `trig_01F9UdoUtLy8oknBPBkHLshS` ✓ | ✅ |
| superbot-mineverse (young seat) | FRESH | FRESH | `updated:` 04:19:00Z ✓ · age ~5m ✓ · evidence `1d8abc5` 04:23:26Z ✓ (independent fetch matched ls-remote) | ✅ |
| codetool-lab-fable5 (parked) | STALE-BY-DESIGN | STALE-BY-DESIGN | `updated:` 2026-07-09T20:06Z ✓ · evidence `a6cf1a9` 2026-07-10T12:07:20Z ✓ · **age: machine `~32h17m` vs hand 32h18m — MISMATCH** | ❌ → **script bug, FIXED** (age_str float truncation; regression selfcheck added; regenerated) |
| product-forge (anomaly probe) | FRESH | FRESH | stamp `2026-07-11T12:00:00Z` verbatim in the lane's file at HEAD `8c64db4` (future-dated — **lane-side bug**, headline 4) · age `future?` is the honest render · ground-truth HEAD 03:51:51Z also ⇒ FRESH | ✅ (legit ambiguity, documented) |

**Outcome: verdicts 6/6 correct; one Age-cell display bug found and fixed at root
cause. This counts as verification run 1 of the several the script's Q-0105 header
requires — the UNVERIFIED header stays until more clean runs accumulate.**
