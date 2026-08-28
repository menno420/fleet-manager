# 2026-08-28 — substrate-kit review round, session 3 (the kit-tree truth pass + the two owed checks)

> **Status:** `in-progress` — born red; this hold token flips only as the
> session's last commit.

- **📊 Model:** fable-5 · high · review/verify
- **📍 Venue:** cloud-container

## Mission

The round's next audit, selected from the committed candidates in the round
thread: **(a) the kit-tree truth pass** — read substrate-kit's committed doc
surface in full at kit main `a9acc41`, including the nine docs subdirectories
the genesis dig's §9 names as skipped (audits, gen2, ideas, operations,
planning, recipes, reports, retro, reviews — plus succession, which the skip
list never even named), and record per-doc live/stale/superseded verdicts with
citations, the way the dig's §10 did for the fm/superbot sets; then reconcile
`kit:docs/current-state.md` (headline still v1.20.2 / "only open PR is #552")
in the kit's own venue through its full discipline. **(b) The two owed
checks** from the router band re-read §1: does the kit's PL-002
canonicalization preserve superbot:Q-0241's rebuild-only scope clause (§1.5),
and did the kit ship any of superbot:Q-0214's delete-with-tombstones retention
posture (§1.4) — both answered with evidence at a named SHA, never against a
doc's self-description.

Checked first, as ordered: the owner's letters (Move-1 GO · the journal
question · the §10 disposition confirmations) and the two new queued
one-liners (`OQ-KIT-PROMPT-DOCTRINE` · `OQ-EAP-SPEND-WINDOW-MOOT`) are
**unanswered** — no unconsumed owner comments for fleet-manager,
substrate-kit or superbot; no new fm commits past `ffe9a53`; nothing new in
the owner-queue. Everything owner-gated stays gated: no Move 1, no §10
disposition execution, no release, no worklist build rows (26/29/33/34/35
stay the build session's lead), fm #958 untouched.

State re-verified before branching: fm main `ffe9a53`, kit main `a9acc41`,
kit 0 open PRs, kit-quality green on kit #587's head `44b9847` (the merge
into `a9acc41`).

## Shipped

- **[The kit-tree truth pass](../docs/findings/2026-08-28-kit-tree-truth-pass.md)**
  (this PR): all **187** doc-surface files at kit `a9acc41` judged per-doc
  (104 historical-record · 23 stale · 20 live · 21 generated · 15 reference ·
  4 superseded — totals recomputed mechanically from the appendix after
  every correction), read by 19 workflow lanes with a code-checked
  whole-population coverage gate, every non-obvious verdict adversarially
  verified (31/36 upheld; the workflow's 5 corrections plus Codex fm #960's
  2 verdict overturns and 3 propagation fixes, all applied and named in §6);
  the 22-file wrong-action set catalogued as §5 recommendations (zero
  deletions; the economy-activation decision carved out of the sweep's
  blanket); the 1,165 unjudged tracked files named with reasons
  (code/harness/cards/boilerplate; 187+1,165=1,352 ✓).
- **Both owed checks answered** in the same finding: §2 — PL-002's
  canonicalization **preserves** superbot:Q-0241's rebuild-only scope at
  `kit:docs/program/rulings.md:66-68` (the expiry clause legitimately
  exercised by PL-012/Q-0271; the one drop a Q-0241-vs-Q-0271 provenance
  mislabel in three derived copies of one owner-profile sentence); §3 —
  superbot:Q-0214's delete-with-tombstones retention **substantially
  shipped** as the v1.0.0 economy engine (harvest-gated triple filter,
  tombstone shards, shadow→gated ladder), the `/updates` feed nowhere, and
  the mechanism unconfigured and trace-free on the kit's own 342-card
  corpus at HEAD. In-place
  answered-pointers added at the dig's §4/§8 claim sites and the re-read's
  §1.4/§1.5; findings-README row; round thread advanced to session 3 done;
  current-state OD-24 bullet extended.
- **kit #588 MERGED on green** (squash `7f58f0e`, kit venue, its own
  discipline): `docs/current-state.md` reconciled (a dated current-truth
  block; the v1.20.2/#552 headline corrected in place; the 07-17 block
  demoted; Next-action routed to the live worklist) + `control/status.md`'s
  false #552 line and stale adopters clause + `docs/NEXT-TASKS.md` row 4
  flipped to reconciled. Three Codex rounds: R1 2 P2 + R2 1 P2
  conceded-and-fixed (release-trigger precision — ported into this PR's
  finding too; #588 named as latest-unreleased in both ledgers); R3's 1 P1
  was the born-red hold itself, consumed by the flip.
- **`OQ-KIT-P10-REQUIRED-CHECKS` retired by a live read**
  (`GET /repos/menno420/substrate-kit/rules/branches/main`: exactly
  `kit-quality`, strict-up-to-date false) — queue entry marked ✅ RESOLVED
  (overtaken); residue named as agent work (the ci.yml legacy-alias
  deletion, a build-session item).

Checked and re-checked: the owner's letters (Move-1 GO · journal · §10
confirmations) and both new OQ one-liners remain **unanswered**; everything
owner-gated stayed gated. superbot stayed frozen (one raw API fetch of the
router, 668,746 bytes — size-identical to the re-read's recorded fetch; no
clone, no write).

## Verify

- Workflow: 57 agents (19 readers + 2 owed + 32 verdict verifiers + 4 owed
  lenses), ~4.5M subagent tokens, 0 errors; coverage assigned=returned=187
  checked in code.
- fm venue: `python3 bootstrap.py check --strict` — the mid-session run
  surfaced a real `[stamp]` finding (D-0015 cited by token in the new
  finding), fixed in place; the pre-flip run's only finding is the designed
  born-red hold naming this card (real exit codes, no pipes).
- Kit venue: `python3 scripts/preflight.py` OK — 9 legs green (real exit 0,
  three runs); kit-quality green at the flip; merged by the armed enabler
  (squash).
- The P10 claim: live rules endpoint, not a doc echo (TRAP-001 honoured).

⚑ Owner decisions needed: none new. The round's standing letters (Move-1
GO · journal · §10 confirmations) and the two queued one-liners
(`OQ-KIT-PROMPT-DOCTRINE` · `OQ-EAP-SPEND-WINDOW-MOOT`) remain open;
`OQ-KIT-P10-REQUIRED-CHECKS` closed as overtaken (no click needed).

💡 **Session idea:** the truth pass's sharpest structural result is that the
kit's own retention machinery (shipped v1.0.0, tested, shadow-gated) is
unconfigured and trace-free on the kit's own 342-card corpus —
`economy.classes: []`, no prune artifact at HEAD — while the estate
separately worries about corpus growth. A one-session
build-track item "kit dogfoods its own economy in shadow mode" would
produce the first real census of what delete-with-tombstones would do,
purely report-only, and turn the §5 disposition row into measured evidence
for the owner's Move-2 thinking.

## ⟲ previous-session review

Session 2's two committed exits both worked as designed here: the
two-re-review cap's "land with findings named-and-routed" exit absorbed a
non-converging reviewer again (this time R3's finding was the designed hold
itself — named, consumed by the flip, nothing routed), and its worklist
row-35 pattern gave this session the shape for §5's
recommendations-not-executions table. One narrowing of session 2's records:
kit #587's NEXT-TASKS release line ("cut only via workflow_dispatch")
lacked the agent-runnable qualifier — release.yml's own header names tag
push as a second, owner-side canonical trigger; Codex R1 on kit #588 caught
this PR inheriting the imprecision, and both kit files plus this repo's
round-thread trap line and the truth-pass rows now carry the precise form.

Layer-2 handoff: docs/repos/substrate-kit/README.md — review-round thread
advanced to "session 3 done"; the one-paragraph answer's stale
current-state clause closed; the traps section's release + required-check
lines made precise.
