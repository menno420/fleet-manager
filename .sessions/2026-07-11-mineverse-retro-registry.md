# 2026-07-11 — Registry-truth: superbot-mineverse + superbot-retro seat packages

> **Status:** `complete`

📊 Model: Claude (Fable family, fable-5) · lane worker dispatched by
coordinator cse_012o8pySy5K3AV6JWoPKryZL · PR #74

## Declared at open (born-red)

Scope: land centralized `projects/` packages for the two LIVE seats that have
none — `projects/superbot-mineverse/` (repo-bearing seat, HEAD `4be012e`,
failsafe `trig_01K8xmAKYS5S2HLy1HPANM7j` @ `20 */2 * * *`) and
`projects/superbot-retro/` (repo-less coordinator seat over gba-homebrew +
pokemon-mod-lab, failsafe `trig_01Y99uDKNtKTz2EtRYPWZkGY` @ `50 */2 * * *`,
plus the two ORDER-002 hourly wake triggers it drives) — regenerated ONLY
from verified reality (live trigger-registry extraction 2026-07-11T13:17:24Z,
superbot PR #1972 founding texts @ merge `10a7486`, mineverse repo state @
`4be012e`; never authored aspirationally). Plus: `projects/README.md` matrix
rows for both seats, owner-queue item 17 (re-paste consolidated setup
scripts, coordinator env FIRST), and the `control/status.md` heartbeat as
the deliberate last content change.

## Shipped (close-out)

- **`projects/superbot-mineverse/` v1** — `meta.md` (seat identity, LIVE @
  `4be012e`, founding provenance superbot PR #1972 @ `10a7486`, per-part
  deployed-state incl. two explicit no-committed-twin rows + a deliberate
  no-setup-script row per R4), `failsafe-prompt.md` (stored prompt
  VERBATIM-FROM-REGISTRY, extraction 2026-07-11T13:17:24Z, byte-checkable),
  `instructions.md` + `coordinator-prompt.md` (VERBATIM centralized copies
  of founding §1/§2 — the running pasted texts have NO committed twin and
  the files say so explicitly; known deployed-reality deltas recorded
  below the verbatim blocks, never edited in).
- **`projects/superbot-retro/` v1** — `meta.md` (repo-less seat: verbatim
  absence evidence — exhaustive `superbot*` search, 6 repos,
  `incomplete_results: false`; drives gba-homebrew + pokemon-mod-lab;
  founding-text POINTER to superbot `10a7486`, deliberately no
  instructions/coordinator copies since no committed deployed twin exists),
  `failsafe-prompt.md` (VERBATIM), `triggers.md` (both hourly child-lane
  wakes VERBATIM: gba `trig_0137SkvhXEJvwepX8aVNkcSn` `0 * * * *` ·
  pokemon `trig_01BTJjkMVMKtWPjuYe7643Hi` `30 * * * *`).
- **`projects/README.md`** — matrix rows for both seats (first repo-less
  row in the matrix).
- **`docs/owner-queue.md` item 17** — six-field, click-level: re-paste the
  consolidated env setup scripts (PR #73 → `cf2c4ee`), coordinator env
  FIRST (superbot-next→python3.11 fix inert until pasted); raw URLs per
  archetype.
- **`control/status.md`** — heartbeat slice record + the superbot-games
  nudge note (idle 02:15Z→13:00Z, 12 silent wakes; direct task list
  delivered; escalation = rebuild from registry package after 2 more idle
  wakes) as the deliberate last content change.

## 💡 Session idea

**A `regen-due` marker line in every `projects/*/meta.md`** — this slice
found the gba/pokemon packages confidently asserting the OPPOSITE of live
registry state ("NOT armed" vs armed-and-firing hourly since 01:36Z) with
nothing machine-checkable to catch it. A one-line, greppable
`regen-due-when:` field (e.g. "a trigger naming this repo appears/changes in
the registry sweep") would let the roster generator (`scripts/gen_roster.py`
already ingests the full trigger export) diff registry reality against each
meta's recorded cadence and emit a `package-stale` advisory — turning
package drift from a lucky catch into a standing check.

## ⟲ Previous-session review

The ORDER 018 env-consolidation slice (PR #73) was exemplary on
root-causing (two latent bugs fixed, why-nots recorded) and its heartbeat
explicitly named the "thin configs inert until owner paste" caveat — but it
stopped short of FILING the owner ask that caveat implies, leaving the
python3.11 fix live-on-main yet inert in every running environment with no
queue item pointing at it. This slice filed it (item 17). Improvement to
the system: when a slice's own status text contains "until next owner
paste / owner re-pastes", that phrase should trigger filing (or updating)
an owner-queue item in the same slice — the caveat and the ask are one
unit; a caveat without a queue item is a stall waiting to be rediscovered.

## Walls / negative findings

- None hit this slice (no classifier denials, no scope denials; the PR was
  opened via MCP and the born-red gate held as designed).
- Negative findings recorded IN the packages: no paste receipts for any
  mineverse/retro console field; no superbot-retro repo; no retro chain-link
  one-shots in the 549-record sweep.
