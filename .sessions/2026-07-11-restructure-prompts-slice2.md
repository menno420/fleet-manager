# 2026-07-11 — fleet restructure slice 2: prompt re-sync (coordinator + failsafe, all live seats)

> **Status:** `complete`

📊 Model: fable-5 · lane worker dispatched by coordinator (restructure program, slice 2 of the 2026-07-11 owner directive) · start 2026-07-11 (born-red at open)

## Declared at open (born-red)

Re-sync every `coordinator-prompt.md` + `failsafe-prompt.md` across the 8
standing seats (venture-lab, superbot-world, game-lab, ideas-lab,
self-improvement, superbot-2.0, websites, fleet-manager) to their slice-1
v2/v3 instructions: replace the v0 placeholders in the 5 new seat dirs with
real prompt bodies, refresh venture-lab/websites prompts to the merged seat
shape, and sweep product-forge + all live prompts for references to retired
or merged seats. Branch `claude/restructure-prompts` STACKED on
`claude/restructure-seats` (PR #88); PR opens with base =
`claude/restructure-seats`. No trigger calls, no merges, no auto-merge
arming.

## What landed (PR #89)

**New seat prompt pairs (v0 placeholder → v1 real body), each with a
trigger rebind-then-delete cutover recipe carrying the old seats' armed
trigger ids (last committed registry state, re-verify via list_triggers):**

- `projects/superbot-world/` — coordinator + failsafe v1; cron `20 */2`
  (flagship mineverse slot); retires games/idle/mineverse failsafes
  (trig_019ZgWyL78Rx1sr6LhvL8NE3 / trig_01TWKGFW8RUsMvxUMt2ndzqA /
  trig_01K8xmAKYS5S2HLy1HPANM7j); heartbeat home = mineverse control/.
- `projects/game-lab/` — v1; cron `50 */2` (retro slot); retires the retro
  failsafe + BOTH hourly child wakes (trig_01Y99uDKNtKTz2EtRYPWZkGY,
  trig_0137SkvhXEJvwepX8aVNkcSn, trig_01BTJjkMVMKtWPjuYe7643Hi); heartbeat
  home = gba-homebrew control/ (public track).
- `projects/ideas-lab/` — v1; cron `0 */2` (even/odd pairing retired);
  retires idea-engine trig_0178q9Je2xRFJgthwamrg9Br + sim-lab
  trig_01SHfnLv6EqZesr4tC3T9kUU; heartbeat home = idea-engine control/.
- `projects/self-improvement/` — v1; cron `0 */2`; retires the OLD
  pre-Q-0265 standing wake trig_016EfUawz6KxEYqUM6f1BqDw (re-arm was
  already due); heartbeat home = substrate-kit control/.
- `projects/superbot-2.0/` — v1; cron `0 */2` (Builder slot); retires the
  Builder failsafe trig_01L5JBefGSCM1fUdwm4SRQnY; superbot hub triggers
  explicitly left alone; heartbeat home = superbot-next control/.

**Refreshed live seats:**

- `projects/venture-lab/` — coordinator + failsafe v1→v2: merged-seat brief
  (+ trading-strategy research annex, holdout-spent rails), stale ORDER
  002/003/004 boot hardcoding replaced by state-at-HEAD boot; cutover
  retires the old trading-strategy failsafe trig_01YBaVeKAW2fSD83S9F37s2d.
- `projects/websites/` — coordinator →v3 (header/in-paste stamp aligned —
  v2 had bumped only the in-paste line; Ideas Lab naming); failsafe →v2
  (prescribed block re-synced to the corrected ORDER-017 merge clause — the
  v1 copy still said "squash-merge on green"; deployed v1-era VERBATIM
  registry record kept untouched by design).
- `projects/fleet-manager/` — coordinator v2→v3: 8-seat FLEET SHAPE rider;
  stale "live as trig_014odnv5h…" failsafe claim (superseded by the F-1
  cutover) replaced by a pointer to failsafe-prompt.md v3; in-paste stamp
  aligned. failsafe-prompt.md deliberately UNTOUCHED (current v3
  VERBATIM-FROM-REGISTRY deployed record). instructions v2→v3 (Ideas Lab
  routing).
- `projects/product-forge/` (stale-reference fixes only — seat awaits owner
  disposition): coordinator v1→v2 + instructions v2→v3 — the Q-0264 loop
  position / simulation escalation now name the Ideas Lab seat. Its
  failsafe file untouched (verbatim deployed record; no retired-seat refs).
- Metas of the 5 new seats + venture-lab/websites part-rows updated to the
  slice-2 state; `projects/README.md` restructure banner updated (slice 2
  landed; MATRIX/paste-wave regen stays a flagged follow-up).

**Post-change retired-name grep (whole projects/ tree):** remaining matches
are only meta stubs, `_inventory/` historical records, instructions naming
the merged seats' source REPOS, evidence-citation paths
(substrate-kit/docs/CAPABILITIES.md), and the 8-seat fleet-shape lists —
no live prompt treats a retired/merged dir as a standing seat.

**Deliberately NOT done:** no trigger MCP calls (cutovers ride each seat's
boot, per the seats' own wake-mechanics grant); no merges, no auto-merge
arming (#88 and #89 park READY for the coordinator/owner); no MATRIX /
paste-wave regeneration (follow-up flagged in the README banner).

⚑ Decide-and-flag (reversible, vetoable at the gate): new-seat failsafe
cadences inherit each merged seat's flagship slot (world `20 */2`, game-lab
`50 */2`, ideas-lab/self-improvement/superbot-2.0/venture-lab `0 */2`);
heartbeat homes = flagship/primary repo control/ as listed above; game-lab
replaces the retro parent+children trigger pattern with one seat + one
failsafe; superbot-2.0's continuous loop lives on the superbot-next side
(superbot keeps its no-seat/owner-session character inside the merged
seat).

## 💡 Session idea

A **registry stamp-consistency checker** (fleet-manager `scripts/`): walk
`projects/*/` and fail when a prompt-bearing file's header `vN` differs
from its in-paste stamp `vN`, or when a placeholder marker (`PLACEHOLDER`)
survives past its owed slice. This session found BOTH drift classes live —
websites (header v1 vs in-paste v2) and fleet-manager coordinator (header
v2 vs in-paste v1) — exactly the "quote your version header" drift check
the registry relies on, silently broken at the source. Cheap (one script +
substrate-gate step), enforcing, and it guards the registry's core
invariant.

## ⟲ Previous-session review

Slice 1 (PR #88) did the hard part well: clean 8-seat dir grammar, honest
v0 placeholders instead of fake prompts, and metas that carried the old
armed trigger ids forward — that last habit is what let this slice write
executable cutover recipes without re-deriving registry state. One miss:
slice 1's new instructions bodies name each seat's enabler state ("mineverse
HAS the enabler; games/idle do NOT") without a verification citation — those
claims were inherited from the source packages, not re-verified at the
merge. Workflow improvement: when a restructure folds N packages into one,
the fold should re-verify inherited infrastructure facts (enabler installed?
required checks?) against the live repos, or mark them "inherited,
unverified" — a wrong enabler claim in instructions sends a seat down the
wrong landing path on its first PR.
