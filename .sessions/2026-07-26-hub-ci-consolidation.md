# 2026-07-26 · hub — CI consolidation: 97 workflow files measured, 44% is dead agent plumbing

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-07-26 · venue: owner-live hub chat · branch
`claude/repo-consolidation-plan-jl7z6x` (restarted from main after #540 merged)

💡 Session idea: the CI sprawl is the **same disease as the repo sprawl, with
the same cause** — both are load-bearing structures for autonomous agent seats
that no longer exist. Which means they have the same fix, and the ordering
matters a lot: **archiving a repo stops its scheduled workflows**, so doing the
repo consolidation first makes roughly two-thirds of the CI cleanup happen for
free. Hand-tuning 97 workflow files before archiving would be work done twice.

## previous-session review

Same session, one PR back: #540 landed the fleet consolidation plan (22 → 9,
product topology). Owner then asked whether the CI checks could be consolidated
too. This card answers that with measurement rather than impression.

## What this commit does (docs-only)

- **`docs/planning/2026-07-26-ci-consolidation.md`** (new) — the measurement and
  the target. Live over the direct-PAT path: `.github/workflows/` trees for all
  22 repos + the Actions runs API windowed to 24h.
- **`docs/planning/2026-07-26-fleet-consolidation-plan.md`** — W7 now carries the
  sequencing point and links the companion doc.
- **`docs/planning/README.md`** — index row.

## The numbers (measured 2026-07-26, not estimated)

- **97 workflow files** across 22 repos; **397 Actions runs/24h**, **46% cron**.
- **~43 files (44%) are autonomous-agent merge plumbing**: `auto-merge-enabler`
  ×14, `substrate-gate` ×14, `merge-on-green` ×7, plus `auto-merge-disarm`,
  `automerge-card-guard` ×2, `host-automerge-extras`, `ci-rerun-watchdog`,
  `pr-auto-update`, `pr-conflict-guard`, `heartbeat-guard`.
- **Real product testing is the smallest class at ~15 files.**
- `merge-on-green` fires **14×/day** on each of `codetool-lab-{fable5,opus4.8,sonnet5}`,
  `superbot-plugin-hello`, `pokemon-mod-lab`, `product-forge` — all with zero
  open PRs and zero commits since 2026-07-18. ~83 runs/day polling for PRs that
  will never arrive.
- **~175 of 185 daily cron runs serve the closed program.**
- Only `shiftlife` (100 runs, 1 cron) and `superbot` (100 runs, 24 cron) show
  healthy profiles.

## Self-implicating evidence worth keeping

PR #540 was **failed twice by `substrate-gate` on a documentation-only change**:
once because the supersession banner pushed `> **Status:**` past line 12, once
because `superseded` is not in the allowed badge vocabulary (`historical` is).
Neither finding protected anything. That gate holds *unattended* sessions to a
doc discipline; against a reviewed change on a frozen doc corpus it is pure
friction. Hence the recommendation to demote it to advisory everywhere except
`fleet-manager` and `substrate-kit`.

Second self-implicating note, kept because it will bite again: the first local
verification of #540 read `$?` **after a pipe into `tail`**, which reports
`tail`'s status (always 0) rather than the checker's — so a red gate looked
green. Verify by capturing the checker's own exit code directly, never through
a pipeline.

## Target

3 uniform checks per active repo (`test` / `build` / `deploy`) + a short
specialist list, of which `golden-parity` (superbot-next, 533 cases) is the most
valuable check in the fleet — it is what makes the W3 cutover decidable instead
of a leap of faith. End state: ~20 workflow files, <60 runs/24h, ~5 cron.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
