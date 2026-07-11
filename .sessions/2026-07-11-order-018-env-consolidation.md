# 2026-07-11 — ORDER 018: environment/setup-script consolidation (audit R2/R3/R4/R6)

> **Status:** `complete`

📊 Model: Claude (Fable family, fable-5) · lane worker dispatched by
coordinator cse_012o8pySy5K3AV6JWoPKryZL · PR #73

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

## Shipped (close-out)

- **R2** — `environments/setup-base.sh` (new): ALL shared setup logic — the
  byte-identical multi/single-repo detection block, the coordinator-superset
  manifest ladder (`env-setup.sh`|`setup-env.sh` → `requirements.lock` →
  `requirements*.txt` depth-2 each-individually → `pyproject.toml` `[dev]`
  then `-e .` → skip), the data-driven `pick_python` pin table, git-state
  triage, env presence report — behind knobs `ARCH_NAME` / `BASELINE_PIP` /
  `PICK_PYTHON_TABLE` / `ENV_REPORT` / `ENV_REPORT_HINT` / `GIT_TRIAGE`.
  The 4 Python-family archetype scripts are now ~25-line thin configs that
  set knobs and source the base (resolution: `$FLEET_SETUP_BASE` → repo-local
  → workspace child → alongside-file → raw fetch; base-unavailable degrades
  to a warning + exit 0, R15). Knob table + notes:
  `environments/archetypes.md` § "The base shim + knob table".
- **Two latent bugs fixed by the consolidation:** (1) the audit §4.2 bug —
  coordinator's `pick_python` had no `superbot-next→python3.11` case (the
  live multi-repo env installed superbot-next under bare `python3`, correct
  only by luck); the shared pin table now carries it. (2) Found in-flight:
  `pick_python`'s missing-interpreter WARNING was logged to stdout inside a
  command substitution — it would have been captured INTO `$py` and corrupted
  the interpreter name in every pre-consolidation copy; now stderr
  (sandbox-proven: captured `py='python3'`, warning still visible).
- **R3** — gba-lab stays a separate full script; both gaps FIXED IN-SCRIPT:
  (a) `xdelta3` added to the apt baseline (patch-distribution tooling;
  `flips` deliberately NOT added — not in the Ubuntu apt archive, an unsigned
  source build would re-add the surface R3b removes; why-not recorded in
  archetypes.md § "R3 disposition"); (b) the Block-3 unsigned
  leseratte10-mirror devkitARM pull is gated behind homebrew detection
  (pokeemerald-only env skips it; bare/unknown layout keeps the proven
  default; `GBA_TRACK_B=force`/`skip` overrides) and the DEVKITPRO
  export/persist only fires when the toolchain is actually on disk.
- **R4** — all 13 `projects/*/setup-script.sh` probe variants retired to
  short exit-0 tombstones pointing at the lane's archetype in the one
  `environments/` lineage (filenames stable — meta.md pointers resolve).
- **R6 ⚑** — decision recorded in archetypes.md: mobile-lab keeps the repo
  `scripts/env-setup.sh` escape-hatch (the fleet's only JS lane — a knob
  today would be speculative surface); the named promotion path is a
  `node-lab` knob on `setup-base.sh` the moment a SECOND JS lane appears.
- **Verification:** `bash -n` clean on all 19 touched/created scripts;
  sandbox runs with stubbed apt/curl/python covered multi-repo + single-repo
  detection, the 3.11/3.10 pin paths, the fallback WARN, the base-unavailable
  fail-soft path, and the Track-B gate (skip / attempt / override) — every
  scenario exited 0. Thin configs remain **unverified-as-thin-configs** until
  the next owner paste / lane boot (Q-0105 posture, noted in archetypes.md).
- **Bookkeeping:** inbox ORDER 018 `✅ DONE` update block (append-only,
  13:06Z real UTC); status heartbeat prepended with the R2/R3/R4/R6 slice,
  the ⚑ R6 flag, and the three lane-side follow-ups (trading-strategy
  `environments/setup-universal.sh` drift · websites triple lineage ·
  superbot-games `environment/` vs `environments/` split).

⚑ Self-initiated: none beyond ORDER scope (the stderr `pick_python` fix and
the DEVKITPRO-persist guard are in-scope root-cause fixes discovered while
consolidating the files the ORDER names).

## 💡 Session idea

The R2 thin configs depend on `environments/setup-base.sh` staying
knob-compatible, but nothing enforces it: add a tiny CI selfcheck (rides
substrate-gate's full lane) that runs each archetype thin config in a stub
sandbox — exactly the stubbed-apt/curl/python harness this session used,
~30 lines — asserting exit 0 + the expected interpreter pin lines. That turns
"unverified-as-thin-configs" into a per-PR regression guard instead of a
wait-for-next-boot posture, and would have caught both latent `pick_python`
bugs years earlier. (Dedup-checked: no `docs/ideas/` dir in this repo; no
existing selfcheck covers `environments/`.)

## ⟲ Previous-session review

The previous slice (PR #71, catch-up heartbeat + ORDERs 017/018 filing) did
the filing cleanly — ORDER 018's do:/done-when: were specific enough that
this session needed zero owner round-trips, which is exactly what a good
ORDER buys. One improvement it surfaces: the filed ORDER text said "pick one
lineage" for R4 without naming the tombstone-vs-delete disposition, and the
dispatcher had to supply that interpretation downstream; ORDERs that retire
files should state the artifact's end-state (tombstone / delete / redirect)
explicitly so the executing worker never has to guess a reversibility
posture. Workflow improvement: add an "end-state:" line to the order grammar
for retirement/deprecation ORDERs.
