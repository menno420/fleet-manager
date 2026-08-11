# 2026-08-11 · hub — close the full-read audit's remaining open defects

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · mechanical refactor — sweep the 67 defects the
  verify-and-edit session left OPEN: record the already-discharged closures,
  fix the task-routed live surfaces, era-banner the retired apparatus, and
  record every closure in findings.md with the command that proves it

Time: 2026-08-11 · venue: scheduled continuation session · branch
`claude/fleet-manager-audit-defects-668i5n` (started at `9df0a55` =
`origin/main` after fm #848 merged)

## Previous-session review

⟲ fm #846/#847 (card `.sessions/2026-08-11-audit-verify-and-edit-pass.md`)
re-ran all seven headline re-checks before editing, closed 34 defects with
proving commands run after their fixes, survived two Codex rounds (11
findings, 11 conceded), and left 67 honestly OPEN. Its card's open-set
enumeration lists 66 ids — the 67th is **D4**, closed by fm #840 per the
headline table but never given a closure paragraph, which this session's
derivation (101 headers − 34 closure paragraphs) surfaced.

## What is about to happen

1. **Record-only closures first** — D4 (closed fm #840), D84 (carve-out landed
   fm #840, `d73d063`), D94 (discharged by fm #846's seat-digest regen; three
   RETRACTED rows verified at `9df0a55` before any edit).
2. **Task-routed fixes** — D86 (grok.md's false null), the
   AGENT_ORIENTATION-vouched family (D48/D51/D75) and its shared
   `.substrate/state.json` root (D41–D43, D53, D93), the D‑0015 family
   (D34/D35, D83, D99), the false-wall strikes (D31, D39, D49, D69, D88, D89).
3. **The mechanical sweep** — era banners on the retired generated files and
   seat-era docs, index completions, script self-description corrections.
4. **Not taken:** D44/D45 — `bootstrap.py` is GENERATED; kit-side, v1.21.0
   track. They stay OPEN with their entries untouched.
5. Every closure recorded in findings.md with the exact executed command; the
   whole proof battery re-runs after the session's last edit; land on green
   (ready PR, `@codex review` and wait, flip last).

## Close-out

**Shipped (PR #849): 65 of the 67 remaining defects closed — 99 of 101
audit entries now carry closure paragraphs; D44/D45 stay honestly OPEN**
(`bootstrap.py` is GENERATED; kit-side, v1.21.0 track).

- **59 fixed at their sites:** the `.substrate/state.json` slot family
  corrected through the kit's own API and the personas regenerated, never
  hand-edited (D41–D43 + the planted docs D48/D53/D75/D93); the [D‑0015]
  family's remedies now disable instead of delete, with the trigger-health
  selfcheck assertion updated to pin the new remedy (D34/D35, D51, D83,
  D99); six false walls struck with fresh measurements run this session
  (D31, D39, D49, D69, D88, D89); roster-style ⛔ banners on the three
  frozen generator outputs and era banners on ten missed seat-era docs; the
  research index completed; both generators' emitted headers made honest and
  `idea-backlog.md` regenerated from the corrected source (D36/D82); the
  one non-terminal card badge flipped (D40); claims/ contested status stated
  on both sides (D46); a do-not-restamp note planted at `control/status.md`
  after the config route proved a designed no-op — the kit falls back on an
  empty `heartbeat_files` and the allowlist never reaches the advisory
  stream, so the first version of that fix overclaimed and CI re-fired the
  advisory against it; caught, reverted, re-scoped (D47);
  `project.index.json`'s stale area values corrected (D98).
- **Six recorded as already discharged:** D4 + D84 (fm #840 — D4 surfaced by
  this session's derivation after the previous card's open-set enumeration
  listed 66 ids for "67 open"), D61/D62 (the findings index regenerated
  complete 2026-08-10), D94/D95 (fm #846's seat-digest regen and SKILLS.md
  re-scope) — each verified against the tree before recording.

**Verify (run this session, tails verbatim):**

- closure battery (86 assertions, one row per proving command, the same
  table that generated the recorded text): `86/86 PASS` — re-run after the
  session's last content edit
- `python3 scripts/check_trigger_health.py --selfcheck` →
  `selfcheck: PASS (0 failure(s))`
- `python3 scripts/gen_idea_backlog.py --selfcheck` →
  `selfcheck: OK — 6 harvest/format assertions + determinism`
- `python3 scripts/check_docs_links.py` →
  `CLEAN — every intra-repo link in 369 file(s) resolves`, exit 0
- `python3 scripts/preflight.py` → only red is this card's born-red hold;
  doc routes 0 errors; false walls CLEAN
- `python3 bootstrap.py check --strict` → exit 0 at close, after the flip

⚑ Three items route to the v1.21.0 kit session: two corrected strings still
live in kit templates inside `bootstrap.py` (the collaboration-model
canonical pointer; the D44/D45 branch-sweep/rules walls — GENERATED file),
and the `[status-stale]` advisory needs a kit-side off-switch for a retired
control bus (D47: fallback-on-empty is deliberate and the allowlist does not
reach the advisory stream, so no host-side disable exists) — alongside the
capability-seed rows already registered in SKILLS-local.md.
⚑ The gate's `--session-log` sentinel carve-out keeps a comment clause
("this repo still carries … an in-progress Status") that D40's flip made
historical; the sentinel itself stays correct and stays needed. Kit-side
absorb when the carve-out lands upstream.
⚑ `docs/current-state.md` deliberately untouched again (word budget) — the
session's record lives in findings.md and this card, same choice as fm #846.

💡 Session idea: **one table should drive both the execution and the record
of every proving command.** This session's battery holds (id, command,
expected) rows; the closure generator pulls commands from the same table, so
recorded-vs-executed gaps are impossible by construction — the class Codex
caught three times in fm #846 and the first battery run caught here again
(a grep re-matching its own retraction quote, two line-vs-occurrence count
errors). Candidate: promote the pattern into the audit conventions or a
small checker that re-runs recorded `Prove:` commands.

⟲ Previous-session review: fm #846/#847's card was accurate to the tree
with one countable defect — the open-set enumeration (66 ids for "67
open"), which its own 101−34 derivation exposes; recorded in D4's closure
rather than by editing the historical card.

**Codex round 1 (head `fab701e`; the draft→ready flip did not trigger a
review — 13 minutes of three-surface polling, zero events — so the literal
`@codex review` comment fired it): 2 inline P2 findings — 2 `[conceded]`,
both verified against source before acting, both fixed:**

1. The D46 claims note asserted "the `session-close` skill's claim step
   writes here" — **false**: the installed skill's step 1 says the claim is
   the born-red card + open PR, *not* a `control/claims/` file. Written
   from the skill's one-line description without opening its body — the
   exact unread-description class `read_before_write` exists for. All three
   carve-out sites and the D46 closure now carry the operative rule.
2. The slot fix stopped one short of its own principle: three MORE
   `.substrate/state.json` slots still fed corrected renders with seat-era
   text (`new_area_ownership`, `staleness_review`, `fleet_dark_repos`), so
   a `render` would have re-emitted the retracted doctrine. Verified, then
   **derived the full set instead of trusting the named three** — the sweep
   found six (`fleet_siblings`, `fleet_status_command`, `review_ritual`
   besides Codex's three); all six corrected via `bootstrap.py answer`,
   residual stale-live-clause sweep returns NONE.

Battery re-run after the round-1 fixes: **88/88 PASS**.

PR: menno420/fleet-manager#849 — ready, born-red hold until this badge flips.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached)
