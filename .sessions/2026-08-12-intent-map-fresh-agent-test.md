# 2026-08-12 · hub — run roadmap § 4.8's fresh-agent test of the Phase 2 intent map

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · review/verify — run the prescribed § 4.8
  fresh-agent test of the Phase 2 intent map: fresh subagents produce maps over
  the committed corpus against contamination-pinned historical snapshots; score
  against a rubric registered before any output is read; land the finding and
  the surface updates it obligates

Time: 2026-08-12 · venue: owner-live hub chat · branch
`claude/fleet-manager-review-nkpno9` (started at `1b10af1` = `origin/main`
after fm #850 merged)

## Previous-session review

⟲ fm #849/#850 (card `.sessions/2026-08-11-audit-defect-sweep.md`) closed 64 of
the 67 remaining full-read-audit defects with proving commands, leaving
D44/D45/D47 honestly OPEN and kit-side (v1.21.0 track). Card checked against
`main`: the tally matches findings.md, and its three ⚑ kit-side routes are
recorded where the v1.21.0 session will look. Nothing for this session to
repair.

## What is about to happen

1. **The owner ask:** *"Review the fleet manager and explain what you think is
   the most valuable next step. Then start working on it."* Review ran the
   README six-read order plus the entry-2b supersession docs. The pick:
   **roadmap § 4.8's fresh-agent test** — the one named outstanding item on the
   owner's current plan (OD-13 → Phase 2), flagged as outstanding in the boot
   file, the roadmap's § 2 table and § 8 honest nulls, `docs/current-state.md`,
   the replay finding, and the `intake` skill itself. Phase 2's mechanism claim
   is explicitly **not earned** until it runs (Codex, fm #830: disclosing the
   author-bias does not substitute), and the promotion rule (§ 6) blocks Phase 3
   sitting on an untested Phase 2.
2. **Method:** fresh subagents (no session context; model cutoff predates the
   corpus events) produce intent maps over the committed ten-ask corpus — the
   nine-fragment instruction from
   `docs/findings/2026-08-05-handoff-fidelity-and-boot-path.md` § 1 and the
   OD-6 correction — with retrieval against `git archive` snapshots pinned to
   the ask-time trees (case A: `7fbc065` = parent of fm #761; case B:
   `f53d7ea` = parent of fm #827), both probed clean of the answer key. The
   handed procedure is the live `intake` skill minus its replay section (the
   tally would leak outcomes). 3 independent agents on case A, 2 on case B.
3. **Scoring:** rubric committed BEFORE any agent output is read (commit order
   is the proof); § 4.8's two dimensions — column placement (citation-verified
   ESTABLISHED, no fused inference, no invented OPEN) and no silently resolved
   HIGH — plus per-case comparators from the committed record. Results in
   `docs/findings/2026-08-12-intent-map-fresh-agent-test.md`.
4. **Surface updates the result obligates:** roadmap § 2 status table + § 8
   honest nulls, boot-file read-path entry 1b, `intake` SKILL.md replay section,
   `docs/current-state.md`, program § 7 row.
5. Land on green: `check --strict` with real exit codes, telemetry delta
   retained, `@codex review` before the flip, flip last.
