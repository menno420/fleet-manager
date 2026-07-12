# 2026-07-12 — consolidation plan + prompt v3.4 restamp (phase B)

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-12 ·
synthesis session (consolidation plan + prompt v3.4)

## Declared at open (born-red)

This PR delivers (1) `docs/planning/2026-07-12-repo-consolidation-plan.md` —
the finalized owner-facing consolidation plan built from the phase-A census
(`docs/research/2026-07-12-repo-consolidation-census.md` @ `6ac4352`, PR #119)
reconciled with the game-lab-seat proposal (PR #121, which this plan cites and
supersedes); (2) the 16 v3.4 deltas applied to `docs/prompts/v3/` with regen +
registry re-sync; (3) owner-queue updates folding the plan's Phase 2/3 asks
(supersedes E#37 OQ-FORGE-DISPOSITION). Owner reviews personally — **no
auto-merge armed**. Deliverables 2–3 follow on this branch after the plan doc.

## Close-out

- **D1 — plan doc** `docs/planning/2026-07-12-repo-consolidation-plan.md`:
  census (PR #119 @ `6ac4352`) + game-lab proposal (PR #121) reconciled;
  the plan **cites and supersedes #121** and supersedes owner-queue E#37
  (OQ-FORGE-DISPOSITION).
- **D2 — prompt v3.4 restamp**: 16 deltas — 13 applied · 1 blocked on kit
  #279 · 1 half-pending kit #287 · 1 watch; +1 adopted #121 candidate,
  3 duplicates, 4 deferred. All 8 custom-instruction files under the
  8,000 char+byte gate; registry `--check-registry` OK
  (`regen_b_files.py` sources → `projects/<seat>/` copies re-synced).
- **D3 — owner-queue**: B#40–43 + E#44–48 added (opened as B#38–41 +
  E#42–46; renumbered in the origin/main merge — main's owner-live session
  took 38/39 for OQ-RAILWAY-APP-MINEVERSE / OQ-RAILWAY-PROJECT-SPLIT; ids
  unchanged); E#37 superseded; E#28 folded to 5 decisions.
- **Codex outcome**: usage-limited on this PR #122 (comment 4951946498) —
  no review will come until limits reset; coordinator re-pokes. The 3 P2
  findings from its review of superseded #121 (review 4680334132 on
  `9a5075a`) were verified and folded here instead: (1) product-forge
  DARK / never-ORDER lane gate added to Phase 1 (specs already named
  non-forge executors — clarifying gate line + provenance added);
  (2) trigger id `trig_015aNMg5ncoSE2Roe4MKjQnr` verified exact at every
  occurrence on this branch — the `ncoSe2` typo does not exist here,
  already-satisfied; (3) provenance line now states explicitly that
  #121's v1.1 deltas targeted the `docs/prompts/v3/` sources + regen,
  never the generated copies — already the v3.4 method.
- **Codex round 2** (on `b3a38ba`): 5/5 findings verified real and
  applied — fm CI intake path `docs/` prefix restored, wall-staleness
  exception mirrored into all 8 startups, B#40–42 range fixed,
  seat-digest re-synced, registry restamped to the true source commit.

💡 Session idea: **codex re-poke queue** — fleet-manager should keep a
small "codex re-request when usage resets" list (PR + date) in
`control/status.md` or a routine, so usage-limited reviews aren't
silently lost. Today both #121's request path and #122 hit the limit
window; without a queue those reviews just evaporate.

⟲ Previous-session review: the census session (phase A) — strong verdict
discipline and negative-findings-first reporting. But it missed that
game-lab was concurrently producing overlapping proposal #121 (landed the
same day), found only via coordinator relay. Improvement: phase-A style
sweeps should include a fleet-wide open-PR **title scan** for same-topic
work before writing, so parallel proposals merge at draft time instead of
post-hoc reconciliation.
