# 2026-07-12 — Prompts v3 draft: universal startup + ender + CI core + per-project plan

> **Status:** `complete`

📊 Model: fable-5 · setup worker dispatched by coordinator · start 2026-07-12 (born-red at open) · phase-2 integration close-out by integrator worker

## Declared at open (born-red)

Synthesis session: prompts v3 draft — universal startup, session ender, custom-instructions core, per-project plan. Inputs: research PRs #93/#95 + owner-pasted baseline 2026-07-11.

## Shipped (close-out)

- **4 universal artifacts** (`docs/prompts/v3/`): `universal-startup.md` (A,
  body 5,868c after the 2026-07-12 integrator LANDING addition — the
  founding-brief-vs-relay dispatch rule, fm PR #99 evidence),
  `session-ender.md` (D, 1,896c, never-re-arms per owner spec delta
  2026-07-11T23:47Z), `custom-instructions-core.md` (universal core paste
  block 6,117c between CORE-START/END), `per-project/README.md` (phase-2
  plan + status + stagger table + v3.1 defect queue).
- **16 per-seat files** (`docs/prompts/v3/per-project/`, commit `b80b8e0`):
  8 seats × (startup B + custom-instructions C seat block), drafted by 8
  seat drafters against census PRs #94/#96 + the owner baseline
  `docs/prompts/baseline-2026-07-11/`, then integrator-audited: char counts
  (all 16 verified real `wc -c`, all within 8,000 hard; 7/8 startups +
  7/8 seat blocks within fitted), ARM-JSON byte-shape uniform (create_trigger
  name/cron/"firing into THIS session"/prompt EXACTLY + send_later unquoted-key
  shape + verify-after-arm + never-route-to-owner + worker-retry — 8/8),
  cron stagger collision-free (table in per-project/README.md; game-lab +
  websites baseline-kept, fleet-manager census-verified, 5 proposed),
  version headers 16/16.
- **Integrator fixes:** venture-lab trim pass 7,986 → 7,398 (fitted) +
  seat block 1,664 → 1,607 (over fitted by 224, flagged in-file; every
  census mandate retained); superbot-world inline STAGGER-SLOT comment
  removed from paste body (7,499 → 7,431); fleet-manager declared counts
  corrected −1 (7,497/1,382); superbot seat slug reconciled README-side
  (`superbot-*`, drafter's simpler form).
- **Defect queue:** 10 consolidated v3.1 items in
  `docs/prompts/v3/per-project/README.md` § "KNOWN DEFECTS → v3.1 queue"
  (A over budget; BOOT-1 orientation path should be a slot; missing
  {{FIRST_WORK_ORDERS}} slot; per-repo inbox read; "(green expected)" vs
  expected-red seats; PACEMAKER-vs-ender wording; pokemon-mod-lab census
  conflict resolution; stale enabler count; superbot settings-grant
  HYPOTHESIS; trading squash-on-green = precedent not guarantee).

## Walls hit

None in integration. Pre-existing repo wall unchanged: roster-freshness 4h
bar + Actions-PR permission (OQ-FM-ACTIONS-PR-PERMISSION) — main's roster
gen #10 (PR #99) was merged into this branch to keep `freshness` green.

💡 Session idea: the char-count header lines were hand-maintained by 8
drafters and 2 of 16 drifted (fleet-manager −1 twice, superbot-world went
stale after an edit). A 20-line `scripts/check_prompt_counts.py` that parses
each `docs/prompts/v3/**` header convention (body-below-comments / fenced /
marker-pair) and diffs declared vs real `wc -c` would make the budget audit
mechanical and CI-able.

⟲ Previous-session review: the phase-1 draft session (universal artifacts)
declared its scope cleanly at open and its A/C/D artifacts needed zero
structural rework at integration — the slot convention held across 8
independent drafters. One improvement it surfaces: A shipped at 5,467c
against its own ~5,000 budget with no in-file overrun flag, and that single
overrun forced per-seat compression work in at least 3 of 8 B files; a
budget check at artifact-A time would have been 8× cheaper than at seat time.
