# 2026-07-10 — Fable-5 fleet review: synthesis landing (findings + proposals + ideas)

> **Status:** `complete`

📊 Model: withheld per session policy (Fable-5 review wave, synthesis + landing agent) · night (~01:45Z)

## Declared at open (born-red)

Synthesis + landing session for tonight's Fable-5 ultracode fleet review.
About to land, in this ONE PR (new files only, plus the ideas/findings
indexes, a dispatch-log line, and the handoff in-flight note + F15 websites
drift fix — gen2-blueprint.md / playbook.md / owner-queue.md deliberately
NOT touched; the next blueprint edit is owned by the CI-tier sim session):

1. `docs/findings/fable5-review-2026-07-09.md` — 30/30 adversarially
   confirmed findings: owner exec summary, per-dimension dispositions,
   blueprint amendment PROPOSALS P1–P11, drift-fix list D1–D6.
2. `docs/proposals/instructions/` — README + 10 gen-2 founding instruction
   packages, ALL marked PROPOSED (not deployed).
3. `docs/ideas/` — 3 verified new ideas (review-queue drainer, lane-seeder
   automation, fleet economics ledger), state `captured` + README cohort.
4. `docs/dispatch-log.md` line + `docs/handoff-2026-07-09.md` in-flight note
   and websites-line drift fix (F15/D3).

Landing: born-red card holds the gate red; flips `complete` as the last
commit; REST merge-on-green (R21 — born-red shape, no arm attempt).

## Done (close-out)

- **Findings synthesis** — `docs/findings/fable5-review-2026-07-09.md`
  landed: exec summary for the owner (6 plain-language priorities: hold the
  venture-lab paste for D1, refusal branch for the self-merge law, review
  queue drainer, fleet cost ledger, seed-lane automation, 10 packages
  ready); five dimension tables (instructions ×9, goals ×6,
  feedback-synthesis ×9, consistency ×3, new-ideas ×3) each with
  per-finding disposition; blueprint amendment PROPOSALS P1–P11 held for
  the CI-tier sim session's blueprint pass; drift-fix list D1–D6 with D3
  executed here and D1/D2 flagged as pre-paste blockers. Findings README
  index row added.
- **Proposals** — 10 packages copied to `docs/proposals/instructions/` with
  a README index marking all PROPOSED (not deployed) + the paste-time
  delta-8 lint; badge lines normalized to the kit taxonomy (`plan`, with
  "PROPOSED, not deployed" preserved in prose) so the substrate gate stays
  green — content otherwise verbatim from the review drafts.
- **Ideas** — 3 files at `captured` (review-queue-drainer,
  lane-seeder-automation, fleet-economics-ledger, all `-2026-07-10.md`)
  following the frontmatter format; ideas README 2026-07-10 cohort section.
- **Ledgers** — dispatch-log 2026-07-10 night section; handoff in-flight
  note + the two websites ORDER-005 lines corrected (F15/D3, drift fixed on
  sight).
- **Rails held** — no edits to gen2-blueprint.md, playbook.md,
  owner-queue.md, or any prompt/founding text; fleet-manager writes only;
  amendments shipped as proposals, not applied.
- ⚑ Self-initiated beyond the strict brief: D3 handoff websites fix (the
  brief allowed a handoff in-flight note; the same file carried confirmed
  F15 drift) + the findings-README index row (repo convention: every
  findings doc is linked from the index).

## 💡 Session idea

**Confirmed-findings JSON as a committed artifact class:** this review's 30
verdicts lived in a session scratchpad and survive only as prose synthesis.
If review waves committed their machine-readable findings array (claim +
recommendation + verdict.notes per entry) under `docs/findings/data/`, the
next blueprint editor could lint amendments P1–P11 against the verdict
evidence mechanically instead of re-reading prose — and later sessions could
re-verify individual findings at HEAD by id. One directory + one README
line; pairs with the review-queue drainer idea.

## ⟲ Previous-session review

The ultracode-verification session (PR #16) set the pattern this session
leaned on — verdict tables committed to `docs/findings/`, born-red card,
REST merge-on-green — and its card's honest "permission-blocked from
merging" line is exactly the refusal-transparency the blueprint still lacks
(finding F6). One improvement it surfaces: it recorded the merge block only
in its card, where no fleet process looks; had it also appended the one-line
refusal to `docs/review-queue.md` (or a walls doc), tonight's F6 amendment
proposal would have had a fourth first-hand specimen in this very repo. The
generalization is P3's refusal script: record the denial where the fleet
reads, not just where the session writes.
