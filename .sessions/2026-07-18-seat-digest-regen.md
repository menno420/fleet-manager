# Session — seat-digest-regen

> **Status:** `complete`

**Branch:** `claude/seat-digest-regen-2026-07-18`

📊 Model: Opus 4.8 · medium · docs-only (derived-artifact regen)

**What I set out to do:** regenerate stale `docs/seat-digest.md` flagged by
`bootstrap.py check --strict` (the `[seat-digest-stale]` advisory) via
`python3 bootstrap.py seat-digest` — a derived render only, never hand-edited.

**Did:**
- **Regenerated `docs/seat-digest.md`** with `python3 bootstrap.py seat-digest`.
  The fence-marked `substrate-kit:walls-digest` block re-rendered from current
  sources (the skill index + the capability ledger `docs/CAPABILITIES.md`): the
  `any`-venue "Merging own PRs is normal agent work" line and the
  `autonomous-project` "Self-scheduling the seat wake chain — WALL (verified
  2026-07-17)" line now match the ledger, and the "…plus N more" tail moved
  21 → 23. Derived artifact — **not hand-edited**; only the generator wrote it.
- **Committed only the derived render** (plus the heartbeat + this card).
  Verified `docs/seat-digest.md` alone clears the advisory with no integrity
  complaint — the strict check compares the committed render directly to a fresh
  render of sources, so `.substrate/state.json`'s tracked hash is not the gate;
  kept the PR to the digest bytes only.
- **Gates:**
  - `python3 bootstrap.py check --strict` → **`[seat-digest-stale]` advisory
    GONE**. Residual `exit=1` is the by-design born-red session-card HOLD
    (`check_session_gate` holds `substrate-gate` red until this card flips
    `complete`) — clears on this final push, not a defect.
  - `python3 tools/check_no_false_walls.py` → **EXIT 0** (`CLEAN — no
    present-tense standing capability-denial claim`). The regen carried a
    `— WALL`-labelled digest line, but it is a fenced derived quote of the
    ledger, not a fresh present-tense wall assertion in a living/binding doc, so
    the guard stays green.
- **Heartbeat** `control/status.md` refreshed (front-matter timestamp/wake +
  a new "This session" block); structure preserved, apparatus unchanged.

⚑ Self-initiated: None — directed deliverable (FM-seat drift-fix task, one
contained born-red PR). Docs/registry-only; no trigger created, modified, fired,
or deleted; no cross-repo write.

💡 Session idea: **A `seat-digest` freshness *pre-commit / born-red* nudge that
fires the instant a digest *source* (the skill index or the capability ledger)
is committed without a matching `bootstrap.py seat-digest` re-render in the same
change.** Today the drift is only caught *after the fact* by the strict
advisory, so a source edit lands and the digest silently lags until a later
session (this one) sweeps it — the exact lag that shipped stale walls/skills
downstream. A tiny checker diffing "did this commit touch `docs/SKILLS.md` or
`docs/CAPABILITIES.md` but leave `docs/seat-digest.md` byte-identical?" would
turn the reactive advisory into a same-commit prompt. Advisory-only with a
kill-switch (same disposable tier as the other convenience guards); dedup-check
against the existing strict advisory first — this is the *earlier* trip-wire,
not a duplicate of it.

⟲ Previous-session review: **`.sessions/2026-07-18-fm-meta-restamp-v37.md`** (the
registry `meta.md` restamp) was rigorous where it counted — it verified every
Class-A claim against the live websites parser and was scrupulously honest that
the v3.7 stamps were *inference, not repo-verified* (Q-0120 discipline held).
What it could have done better ties straight to this session: that pass touched
the *registry* docs but did not re-run `bootstrap.py seat-digest`, and the
digest was already lagging its sources — so the `[seat-digest-stale]` advisory
sat red through a docs-heavy session that was well-positioned to clear it.
Workflow improvement it surfaces: a docs-only session should end with a
"derived-artifact sweep" (regen the digest, contextpack, roster) as a checklist
line, so a session that edits sources doesn't leave their renders stale for the
next one — exactly what the session idea above would enforce mechanically.

📋 Doc-audit: nothing captured only in chat that belongs in a durable home — the
regen is self-documenting (the digest IS the derived home), the heartbeat +
this card record the action, and PR #323's body carries the before/after. No
owner decision, new doc, or ledger entry created that needs routing elsewhere.
