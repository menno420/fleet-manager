# 2026-08-13 · substrate-kit v1.21.0 — the cut, and fleet-manager's adoption

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · mechanical refactor
- ⚑ Self-initiated: no — the owner's 2026-08-09 *"both, in order"* ruling,
  second half; re-confirmed live 2026-08-13. The kit-side cut ran first in
  this same session (kit #581, merged; v1.21.0 published run `31699815412`).

💡 Session idea: **the harness that proves a fix can silently stop being able
to see the defect it guards.** Two instruments failed the same way today: the
A/B harness's defect-5 claim counter used a raw substring count that the
HONEST fix also satisfies (the corrected template legitimately shows the
command inside the copy-loop recipe), and my first context-aware replacement
used `[^.]` in its gap — which the period in "bootstrap.py" blocks, so it
counted 0 on the very dist that HAS the claim. An instrument's positive
control (does it fire on the known-bad input?) is as load-bearing as its fix
verification — `capability-probe` step 3b generalises further than absences.

## previous-session review

fm #852 (fresh-scorer half of § 4.8) checks out against the tree: the finding
(`docs/findings/2026-08-13-intent-map-fresh-scorer.md`) exists and the
program §7 row, roadmap § 4.8/§ 8 and `current-state.md` all carry the
PARTIAL-confirmed-3/3 result consistently; the permissions allowlist it
bundled is live in `.claude/settings.json` (this session ran under it —
few prompts, as intended). No claims found overstated.

## What this session did (kit side — recorded here because the owner reads fm)

Cut and published **substrate-kit v1.21.0** closing the seven-defect worklist
(`docs/findings/2026-08-09-substrate-kit-defects.md`, defect 7 first), the
three substrate-gate hardenings fm re-applied by hand each upgrade, and the
capability-seed retraction of the three route-quirk walls (+ the same wall in
the `enforcement-required-unverified` NOTE and the branch-sweep template).
Kit #581: born-red, **two Codex rounds — R1 6 findings (4 conceded+fixed,
2 partial with evidence), R2 3 findings (all conceded+fixed; final commit
dispositioned under the two-round cap, stated not inferred)** — merged
`0021adc`; publish `workflow_dispatch` run `31699815412` success.

**Release record:** v1.21.0 · bump PR kit#581 merged @ `0021adc` · release
run `31699815412` · tag v1.21.0 @ `0021adc` · sha256
`8807a00e0e7f14f61f37f2afb48bcb38e4b7247b10741761ff99630bf9cc7356`
(downloaded asset = release.json field = .sha256 asset = committed dist at
the bump SHA — four-way ✔).

**Fresh 12-adopter `--gate-preview` sweep with the new dist** (the DECIDED
prerequisite for shipping the promotion): the six promoted sites carry **0
findings on 12/12 trees**; every would-red row belongs to a deliberately
un-promoted site (`boot_path` on 10 trees, `automerge_preflight` on 2).

**The intake-graduation call (the prompt's OPEN item) — DEFERRED**, stated
per instruction: (1) a defect-fix release reaching twelve adopters should not
also carry a feature graduation; (2) fm #852 made the checker-side needle
rule a hard prerequisite (imprecision counts scorer-relative, 4–11) and it is
not pinned yet; (3) the hazard the ride would close fires on the hand-run
copy loop, not the upgrade (fm #833 measured), and the loop's template now
warns diff-before-copy. The graduation is its own session.

## This PR (fm side)

Adopt v1.21.0: `bootstrap.py` 1.20.2 → 1.21.0 (banked rollback), the host
half of the new repo-checkers extension point (`scripts/repo_checks.sh`),
the A/B harness's context-aware defect-5 claim counter (with the `[^.]`-gap
fix above), the SKILLS-local re-apply-table trim to what genuinely remains,
and the program §7 / current-state ledger updates.

## Verification (each box checked only when its command has run)

- [x] sha256 four-way on the published asset (values above)
- [x] `tools/ab_kit_scan.py` old=vendored 1.20.2, new=PUBLISHED asset —
      **all seven rows in the wanted direction**: defects 1/2/3/4/7 flag
      (0→1 each, defect 7's row green), defect 6 clears (1→0) with the
      quote-only improvement kept (0→0), defect 5 claim 1→0 with staging
      behaviour unchanged (build 0, staged 14→15, live 0 by design)
- [ ] `python3 bootstrap.py.new upgrade` — bank verified
- [ ] carve-out scan (`.substrate/upgrade-report.md`) — listed in PR body
- [ ] regenerated substrate-gate carries the three upstreamed fixes (env
      block · repo-checkers step · sentinel) — diffed, not assumed
- [ ] capability-seed fence carries the retraction rows after refresh
- [ ] `python3 bootstrap.py check --strict` exit 0 (designed hold excepted)
      + `python3 tools/check_no_false_walls.py --strict` exit 0
- [ ] Codex review at the exact head; dispositions recorded here

Layer-2 handoff: null (fleet-manager itself; substrate-kit has no Layer-2
folder — `docs/repos/` coverage note stands)
