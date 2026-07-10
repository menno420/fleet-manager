# 2026-07-10 — ORDER 003 (review-queue enforcement) + ORDER 007 (@codex relay rule) + ORDER 011 close-out

> **Status:** `complete`

📊 Model: fable-5 (family-level, per Q-0262 model-line policy) · start 2026-07-10T20:45Z

## Declared at open (born-red)

Q-0265 continuation-chain slice (fired 20:43Z — the chain's first fire, executed by
this worker on the coordinator's behalf). About to land, in this PR:

1. **`docs/review-queue.md`** — ORDER 003: the auto-append rule made BINDING in the
   header (>50 changed lines of runtime/product code OR any self-flagged risk → row,
   appended by the PR's own session before close; N=50 rationale documented,
   decide-and-flag), the standing drainer named two-tier (PRIMARY @codex post-merge
   review per Q-0258/Q-0259 r3 · FALLBACK manager failsafe-wake batches; 48h-unread
   escalation), and the FIRST DRAIN PASS backfilled — 8 rows for the highest-risk
   overnight/day PRs fleet-wide, each with why-risky + citation + drain path.
2. **`docs/gen2-blueprint.md`** — changelog entry making the same rule binding at the
   blueprint level (§1 review bullet amendment).
3. **`docs/playbook.md`** — ORDER 007: new REVIEW RELAY section (R24, the @codex
   relay rule — one specific question on the final head; Part C template pointer;
   Q-0120 return path; owner-queue is owner-only-items ONLY).
4. **`control/inbox.md`** — ORDERs 003 + 007 flipped ✅ DONE (this PR); ORDER 011
   flipped ✅ DONE (re-arm record verified live this session and landed verbatim in
   status.md per its done-when).
5. **`control/status.md`** — heartbeat as the deliberate last content step (chain-slice
   record, orders footer, next slice = ORDER 009).

## Close-out

All five landings shipped as declared (PR #37). Decisions taken decide-and-flag:

- **⚑ N=50** as the auto-append threshold (runtime/product code lines, excl. docs/,
  control/, .sessions/, pure test additions) — rationale in the review-queue header;
  owner may re-tune.
- **⚑ Two-tier drainer**: PRIMARY @codex (Q-0258/Q-0259 r3), FALLBACK manager
  failsafe-wake batches; 48h-unread escalation. Codex availability recorded per repo
  where cheaply visible (superbot LIVE via codex-labeled #1917; superbot-next LIVE per
  the ORDER 007 input line; fleet-manager NOT enabled — env ask on PR #26; all others
  "codex availability unknown" until probed).
- **Backfill = 8 rows** (aim was 6–10): venture-lab#9 · superbot-games#16 + #5 ·
  trading-strategy#21 + #36 · superbot#1920 · pokemon-mod-lab#8 · gba-homebrew#12.
  Honest finding recorded on the superbot row: the overnight band #1915–#1925 contained
  **zero disbot/ runtime PRs** (only #1917's one-line Codex docstring), so the band's
  max-risk item is the #1920 enforcement-surface tooling change, not a runtime PR.
- ORDER 011 done-when satisfied with **live re-verification**, not just transcription:
  new trigger present + enabled and old id absent in the full 88-record `list_triggers`
  output pulled this session.

💡 **Session idea:** wire the N=50 auto-append rule into the substrate-kit `check`
advisory set — a `review-queue-append` advisory that diffs the PR's changed runtime lines
against the threshold and warns when a row is missing. The rule is binding-by-doc today;
the kit advisory makes it self-enforcing fleet-wide at zero owner cost (enforce, don't
exhort — Q-0132 class), and the kit already has the owner-action-fields advisory as the
exact pattern to copy.

⟲ **Previous-session review:** the ~20:40Z doctrine-fold job (PR #36) landed clean folds
across three repos and correctly filed ORDER 011 as in-progress while a parallel worker
executed the re-arm — good decoupling. One improvement it surfaced: it wrote "the re-arm
record lands verbatim in this file per the proven cutover recipe" but left no pointer to
WHERE the executing worker would find the verbatim result values (trigger id, created-at)
— this slice had to re-derive them from a live `list_triggers` pull. That re-derivation
turned out to be the better practice anyway (verify > relay, R2/Q-0120), so the concrete
improvement is: make "re-verify live before recording DONE" the stated norm for any
cross-worker done-when hand-off, not an accident of a missing pointer.
