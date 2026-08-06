# 2026-08-06 · hub — telemetry delta from the 12-repo gate-preview sweep

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

💡 Session idea: **the guard-fire ledger records what fired but not what
produced it.** These 94 records came from the kit's *unreleased* build run
against this tree during a cross-repo sweep — findings under a gate this repo
does not itself run (fleet-manager vendors v1.20.1). The ledger has no field
for that, so the provenance survives only in a commit message, which is not
where a future reader will look. A `kit_version` on each record would make the
ledger self-describing and cost one key.

## previous-session review

`2026-08-06-foundation-verification.md` (#789) landed the checker
classification and the boot-path audit, and merged. This is the telemetry it
generated afterwards, while sweeping the other 10 adopter repos for kit #579 —
the known wart that `check --strict` appends to a tracked file, so verifying a
commit dirties the tree it just cleaned.

Opened on a **fresh branch off main**, not on the #789 branch: a merged PR is
finished and does not take follow-up commits.

## What landed

- `.substrate/guard-fires.jsonl` — 94 records. Kept rather than discarded
  because the standing rule is *commit the delta, never revert it*; a thinner
  ledger with a tidier story is exactly what that rule exists to prevent. The
  `blocking`/`stamp` rows are genuine and did happen here — the `D-0011` id
  collision #789 introduced and fixed.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**
- `python3 bootstrap.py check --strict` → **exit 0**
- Merge-conflict resolution validated structurally: every retained row parsed
  as JSON before the write (4,690 records), and `git diff --diff-filter=U`
  confirmed empty before committing.

⚠ **Checked deliberately against today's incident.**
`2026-08-06-broke-main-and-wired-the-gate.md` records a session committing
**conflict markers to `main`**: `git commit --no-edit 2>/dev/null` failed on a
conflicted merge, `2>/dev/null` swallowed the error, and the following `git add
-A && git commit` staged the markers. This session ran two merges with that
same shape. Both were verified: `git grep` for conflict markers across
`fleet-manager` main and `substrate-kit` main returns **nothing**, and both
merges checked `--diff-filter=U` was empty before committing rather than
trusting the commit's exit code.

**Honest null.** The provenance problem in the idea above is recorded, not
fixed — the ledger still cannot say which build wrote a row.
