# 2026-08-14 — gba unblock: migration test, owner bypass, phase 3 completes 5/5

> **Status:** `complete` — branch `claude/gba-bypass-s7-row`, records-only:
> this §7 row and this card. The work it records happened on gba #215/#216
> and kit #585 and is complete at this card's birth (the kit #584 precedent
> for a small records PR carrying its card complete).

- **📊 Model:** fable-5 · high · docs-only

## previous-session review

Same session, previous turn: the phase-3 card parked gba on the toolchain
fork with the probe record. All of it held; two of its claims were
superseded by better measurement this turn — "Wayback rate-limited" resolved
to "no capture exists", and my report's "nothing in CI executes the NDS
titles" was WRONG: `rom-builds.yml` boot-runs every NDS title under
py-desmume with telemetry watch-asserts (the very harness that caught the
regression). The correction is on gba #216.

## Shipped (records only — the work lives on the PRs)

- gba #216: mirror release + re-pin to 1.22.3; migration verdict measured
  (Underroot half-rate, slope 0.5; +1 boot-frame on the other two); holds
  open, carded and `do-not-automerge`, as the migration vehicle.
  **⟲ Superseded ~25 minutes after this card merged (owner, live,
  2026-08-14):** *"Why would any PR need to be open? I can't use the things
  that are in an open PR."* #216 was **closed unmerged at 06:41:13Z** — an
  open PR is never a vehicle; future work lives in records and branches. The
  branch `claude/nds-toolchain-1-22-3` is retained with the re-pin, the card
  and the measured verdict. Ruling captured as `[D-0017]`
  (`docs/decisions.md`); review evidence:
  `docs/findings/2026-08-14-v1210-phase3-review.md`.
- gba #215: merged `7a4977bb0` under the owner's one-time bypass — window
  05:58:13Z→05:58:16Z, `ROM builds` honored green first, ruleset restored
  and verified; tree-verified at main (dist `8807a00e…`, pin 1.21.0).
- kit #585: registry regen — 9 current · 3 honestly stale.

## Verify

- Every claim above cites its PR record; gba main read back raw
  (KIT_VERSION 1.21.0 · sha256 `8807a00e…` · pin 1.21.0).

Layer-2 handoff: null (no docs/repos/ folder exists for gba-homebrew;
its PRs #215/#216 carry the handoff)

💡 The bypass pattern that made this safe is reusable: honor every required
check the diff CAN satisfy, lift only the measured-broken one, merge, restore
within seconds, verify from the effective-rules endpoint, and leave the
timestamps on the PR. Worth one line in the playbook if it ever recurs.
