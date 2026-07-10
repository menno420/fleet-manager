# 2026-07-10 — package-centralization assembly (projects/ registry)

> **Status:** `complete`

📊 Model: fable family (assembly worker, coordinator-dispatched) · start 2026-07-10T21:30Z · end 2026-07-10T21:55Z (`date -u`)

## Declared at open (born-red)

Assembly worker for the coordinator's package-centralization dispatch (Phase C
— the deliverable). About to land, in this PR:

1. **`projects/<name>/`** — every package dir from the three-builder sweep
   committed verbatim (13 full seat packages: fleet-manager · substrate-kit ·
   superbot-next · idea-engine · product-forge · sim-lab · websites ·
   trading-strategy · venture-lab · superbot-games · pokemon-mod-lab ·
   gba-homebrew · superbot; 5 archive/pre-birth metas: codetool-lab-fable5 /
   -opus4.8 / -sonnet5 · mobile-lab · games-program). Content is
   builder-verified; assembler spot-fixes mechanical issues only.
2. **`projects/README.md`** — the registry index: what this is (source of
   truth for per-Project console pastes; regenerate-don't-fork), the
   per-Project MATRIX (seat status · cadence · per-part deployed-state · key
   flag), the paste-wave section (which packages need owner pastes NOW vs
   ride a seat's own boot), provenance.
3. **`docs/owner-queue.md`** — ONE consolidated "Project package paste wave"
   active item (click-level subitems: kit §2b + OA8 · forge §2b · sim-lab
   failsafe arm via Routines screen · websites v2 re-paste + optional cadence
   retune · trading re-paste · superbot optional); FIX the Parked mislabel
   (opus4.8's releases are LIVE — the un-released tags are fable5/envdrift's);
   ADD the trading-strategy PR #37 owner merge click.
4. **`control/status.md`** — heartbeat as last content step (package-
   centralization record + notable builder findings).
5. **This card**, flipped `complete` as the deliberate last commit.

Landing: born-red card holds the gate red; work commits next; gate run
(`python3 bootstrap.py check --strict`) before the flip; flip last; REST
squash-merge on the branch's substrate-gate run going green. Sequencing note:
PR #38 (chain slice: roster v1 + model matrix) is open in parallel — this
branch update-branches/rebases over it before merging if it lands first.

## Done (close-out)

All five items landed, with two ground-truth corrections found at assembly
time (declared item 3's third bullet changed shape — see below). Commits
behind this card: `5c0be19` projects/ registry (75 files: 18 package dirs +
`_inventory/` ×3 + README) · `8769580` owner-queue · `9e88e0c` heartbeat +
corrections. PR #38 merged mid-session (`b5ded26`); this branch rebased onto
it cleanly and the heartbeat was written on top of #38's status (not the
stale 0eaa668 base).

- **Ground-truth correction 1 — trading PR #37 was ALREADY MERGED** (by the
  owner, 20:56:34Z, API-verified `merged_by: menno420`) between the package
  builder's snapshot (@ `ffdd6f6`) and assembly. The dispatch's "add the PR
  #37 owner merge click" item was therefore NOT added as an open ask
  (assumption-based/stale asks are banned) — recorded in owner-queue
  § Resolved (later additions) with provenance instead; README matrix row
  updated to match. #38's roster corroborates (trading failsafe also
  re-armed seat-side 21:03Z — noted in the matrix as verify-at-next-contact).
- **Ground-truth correction 2 — websites' 20:00Z fire landed 3 slices**
  (roster/#38; silent-fire watch cleared) — v2-shaped behavior, so paste-wave
  item (d) carries a verify-first note (skip the trigger re-paste if v2 is
  already live; the instructions re-paste stands either way).
- Spot-fix scope was mechanical-only; **zero fixes needed** (no missing
  trailing newlines, no broken relative links, shebangs present). Builder
  content untouched byte-for-byte.
- Decide-and-flag: the three sweep inventories committed at
  `projects/_inventory/` (beyond the dispatch's letter) — the metas cite them
  as sources and the scratchpad copies are ephemeral; without this the
  registry's provenance chain dangled.
- Count note for the record: the dispatch said "14 package dirs"; the build
  tree holds **18** (13 full + 5 archive/pre-birth) — assembled all 18,
  recorded accurately everywhere.
- Gate `python3 bootstrap.py check --strict` red pre-flip ONLY on this card's
  hold (missing enders + in-progress badge) — the born-red design; the sole
  other output is the pre-existing advisory (owner-action-fields on the ⚑
  line, never exit-affecting).

## 💡 Session idea

The registry's MATRIX deployed-state column is hand-transcribed from 18
metas and will drift the way every hand-copied table here has (kit-version
drift class, fixed twice today alone). Idea: extend the R25 roster-generation
duty (or `tools/gen_roster.py` when it lands) to also emit the per-part
deployed-state columns by parsing `projects/*/meta.md` "Deployed-state"
tables — one generator, two tables, zero hand-copies. Dedup-checked: neither
`docs/ideas/` nor the roster proposal covers projects/-registry generation.

## ⟲ Previous-session review

Previous-session review (the #38 chain slice): strong — it fixed the kit-line
drift (v1.4.0→v1.7.0) on sight per Q-0166 and its roster made two of THIS
session's ground-truth corrections cheap (trading #37 merged; websites fire
landed work — both were one grep away instead of two API hunts). Miss worth
naming: #38's roster and this registry's matrix now BOTH carry per-lane
trigger/cadence state with no cross-pointer — the concrete improvement is the
session idea above (one generator feeding both) plus the cross-links this PR
added in README/owner-queue. Not filler: the two-tables-one-truth split is a
real drift seed.
