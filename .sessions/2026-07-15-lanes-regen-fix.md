# 2026-07-15 — lanes-regen-fix (fm slice: lanes.json generation-counter lag under automated regen)

> **Status:** `complete`

- **📊 Model:** Claude Fable (Claude 5 family) · high · tooling+docs
- **⚑ Self-initiated:** yes — grooming slice promoted from the follow-up flagged
  on the roster-regen-0810 card (drift-on-sight: generated artifact lagging its
  generator under the automated regen path). Contained + reversible.

## What happened

- **Root cause confirmed:** `scripts/gen_roster.py` unconditionally re-emits
  `registry/lanes.json` with every roster generation (C3 emission, ~line 2110),
  but `.github/workflows/roster-regen.yml`'s commit step diff-checked and
  `git add`-ed only docs/roster.md + docs/owner-queue-candidates.md +
  docs/evidence-index.md — so every cron regen (#224 Gen #57, #226 Gen #58)
  advanced the docs while lanes.json stayed at generation 56 on main. Lane
  *content* never drifted (the LANES constant is unchanged); counter lag only.
- **Workflow fix (minimal diff, existing style):** added `registry/lanes.json`
  to the diff-quiet check, the `git add` line, the regen step name, and the
  bot-PR body file list in roster-regen.yml.
- **lanes.json brought current without desync:** ran the exact regen the cron
  runs, pinned to the committed generation —
  `python3 scripts/gen_roster.py --triggers telemetry/triggers-snapshot.json
  --generation 58 --date 2026-07-15T08:57Z --generated-by "roster-regen
  workflow (GitHub Actions, headless)" --dispatched-by "cron 40 */2 * * *
  (...)"` — then `git checkout --` the three docs (heartbeats moved since
  08:57Z, so re-emitting the docs would have desynced them from the committed
  Gen #58) and kept only registry/lanes.json, whose payload is a deterministic
  function of LANES + generation + date. Result: lanes.json generation 58,
  generated_at 2026-07-15T08:57:00Z, matching the committed roster header.
- **Heartbeat** stamped 09:18:03Z: #225 merged 08:20Z; lanes.json lag
  root-caused + workflow fixed this PR; backlog otherwise DRY; no owner replies
  yet to the ~07:10Z summary; seat picture unchanged (idea-engine⇄sim-lab
  cycling; 9 un-rebooted).
- **Landing state (verified live):** substrate-gate GREEN on the final head
  `be3988f` (the earlier red was the designed born-red hold), but merge-on-green
  **skipped #227 by design** — its owner-merge-only rail parks any PR whose diff
  touches `.github/workflows/**` (verbatim sweep log, run 29404130566: `skipped
  PR #227: .github/workflows/** in diff — owner-merge-only`). So this PR waits
  for the owner/coordinator merge click; it will never auto-land, and that is
  the rail working, not a defect.
- **Checkers:** check_owner_queue CLEAN; roster freshness OK (Gen #58, 0.4h);
  `bootstrap.py check --strict` clean apart from the designed born-red hold and
  4 pre-existing model-line advisories on 07-14 cards (advisory-only, not this
  slice's).

## Session enders

- **💡 Session idea:** generation-parity guard — teach
  `scripts/check_roster_freshness.py` (or the strict gate) to assert
  `registry/lanes.json`'s `generation` equals the roster header's
  `Generation #N`. This slice's drift class (one generated artifact lagging a
  sibling from the same generator because a staging list went stale) is purely
  mechanical and machine-checkable; the freshness checker already parses the
  roster header, so the parity assert is ~5 lines and turns the next staging
  omission into a red instead of an eyeball catch. (Friction → guard, Q-0194
  class; checker-tier, free to ship in a follow-up slice.)
- **⟲ Previous-session review (roster-regen-0810):** strong slice — it caught
  the lanes.json lag while verifying freshness, named the likely root cause
  (workflow stages docs only) in one line, and flagged it honestly instead of
  silently ignoring the mismatch; that precision made this fix slice cheap.
  Miss: with the root cause already named and the fix a two-line staging edit,
  drift-on-sight arguably wanted it fixed in the same slice rather than
  deferred a cycle. Workflow improvement: the generation-parity check above —
  it converts this whole drift class from "hope the next reader notices" into
  an enforcing guard, which is the Q-0194 pattern this repo is supposed to
  apply on every friction.
