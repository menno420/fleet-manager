# 2026-07-26 · hub — fleet consolidation plan (product topology), 22 → 9

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-07-26 · venue: owner-live hub chat · branch
`claude/repo-consolidation-plan-jl7z6x`

💡 Session idea: the fleet's repo count is not a hygiene problem, it is a
**stale organizing principle**. "One agent seat = one repo" was correct while
the seats existed (ruling Q-0260 gave each seat an unambiguous write scope);
the program closed 2026-07-22 and the topology outlived it. Every visible
symptom — `phone-controller` buried in a seat-named repo, `botsite`/`dashboard`
duplicated across `superbot` and `websites`, four repos for one bot's games —
traces to that single cause. Consolidation is a translation, not a cleanup.

## previous-session review

Last hub work was 2026-07-23 (forge Slice-4 landing). Since then: the
autonomous program closed, `shiftlife` was founded 2026-07-24 and has taken all
37 of its commits inside a week. The 2026-07-12 consolidation plan (seat-based,
19 → 16) was never executed and its target end-state is no longer reachable —
superseded here rather than revived.

## What this commit does (docs-only)

- **`docs/planning/2026-07-26-fleet-consolidation-plan.md`** (new) — the plan.
  Census of all 22 repos taken live over the direct-PAT path (`curl --noproxy`,
  repos + trees + commits + releases APIs), not from the derived roster.
  Target: **22 → 9 active repos**, organized by product. Seven sequenced
  workstreams, W1 first (graduate `phone-controller` — smallest blast radius,
  proves the subtree-split + secrets recipe W2/W3 reuse).
- **`docs/planning/README.md`** — index row for the new plan.
- **`docs/planning/2026-07-12-repo-consolidation-plan.md`** — SUPERSEDED banner;
  status `plan` → `historical`. Its delete-vs-archive contradiction is recorded
  as resolved by OD-3.

## Owner decisions recorded (hub chat, 2026-07-26)

- **OD-1** — `superbot-next` is the destination ("the old superbot repo is
  filled with too much architectural debt"), but **live testing comes first**;
  the cutover is gated on it (W3).
- **OD-2** — `venture-lab` **stays a live repo** (19 publish-ready SKUs + the
  Night Kiln series are intended inventory), not archive material.
- **OD-3** — **archive, do not delete.** Resolves the standing contradiction
  between the 2026-07-10 "delete no repos" ruling and the 2026-07-12 "delete the
  test repos" ask.

## Findings worth keeping

- **Verified, and it corrects a natural assumption:** `superbot-idle` and
  `superbot-plugin-hello` are *already* installed plugins of `superbot-next` —
  pinned by manifest hash in `plugins.lock.json` (v0.1.0 each). But
  `superbot-games` is **not** plugin-packaged (no `pyproject.toml`, no
  `manifest.py`; 103 tests of pure domain only), so W2b is real build work —
  the host-facing adapters — not a file move. `superbot-mineverse` is a
  decoupled web app, not a plugin; its no-Postgres/no-token rail must survive
  the move as CI, not as a repo boundary.
- **Stranded assets, measured:** `superbot-next` at 533/533 golden parity never
  cut over · `phone-controller` (signed APK, owner-playtested) two directories
  deep in an "archive-ready" repo · `envdrift` and `cfgdiff` finished with **0
  releases each** · venture-lab 1 of ~20 SKUs live.
- **21 of 22 repos were created 2026-07-07 → 2026-07-24.** Only `superbot`
  (2025-08-10) predates the program. Fifteen have `PROJECT CLOSEOUT` as their
  newest commit.
- **`roster-regen.yml` still fires ~hourly** regenerating a roster of seats that
  no longer exist (W7).

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
