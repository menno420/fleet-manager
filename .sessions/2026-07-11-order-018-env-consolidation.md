# 2026-07-11 — ORDER 018: environment/setup-script consolidation (audit R2/R3/R4/R6)

> **Status:** `in-progress`

📊 Model: Claude (Fable family, fable-5) · lane worker dispatched by
coordinator cse_012o8pySy5K3AV6JWoPKryZL

## Declared at open (born-red)

Scope: execute ORDER 018 (control/inbox.md, filed 2026-07-11T11:52Z) — the
env-consolidation lane from the 2026-07-11 instruction-and-env audit §4:
**R2** collapse the 4 Python archetype scripts into ONE base shim
(`environments/setup-base.sh`) + knob table in `environments/archetypes.md`,
with the four archetype files as thin configs (filenames stable) and the
missing `superbot-next→python3.11` `pick_python` case fixed in the
consolidated table; **R3** gba-lab stays separate — disposition its two lane
gaps (xdelta3/flips patch tooling; devkitARM Track-B pull gated behind
homebrew detection); **R4** retire the 13 `projects/*/setup-script.sh` probe
variants to the one `environments/` lineage (tombstones, filenames kept);
**R6** record the mobile-lab node-lab-knob-vs-escape-hatch decision in
`environments/archetypes.md` (decide-and-flag ⚑). Bookkeeping: inbox DONE
block + status heartbeat; flip this card `complete` as the final commit; REST
squash-merge on green (R21).
