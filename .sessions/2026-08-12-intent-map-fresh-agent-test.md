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

## Close-out

**Shipped (PR #851): the producer half of the § 4.8 fresh-agent test, verdict
PARTIAL — Phase 2's mechanism claim earned producer-side; the fresh-scorer
half the record requires (replay finding § 4, fm #830 disposition) stays
open.** *(This block first claimed "run in its prescribed form, near-PASS";
Codex round 1 refuted both halves from the record — conceded, reframed.)*

- The finding: `docs/findings/2026-08-12-intent-map-fresh-agent-test.md` —
  design § 1 (pins `7fbc065`/`f53d7ea`, contamination probes, procedure
  redaction), rubric § 2 (committed at `a7b1a5f`, before any agent output
  existed), results § 3, verdict § 4, honest nulls § 5.
- The evidence folder beside it: five verbatim agent reports, both prompt
  templates, the citation checker + four TSVs, and the adjudication of every
  non-PASS row (`docs/findings/2026-08-12-intent-map-fresh-agent-test/`).
- Measured (post-round-1 recount): **222 checked citations (188 ESTABLISHED ·
  34 other) · 221 substance-correct (ESTABLISHED subset 187/188) · 11
  exact-range attribution imprecisions · 1 citation-overreach · 1 ESTABLISHED
  miscount · 0 fabricated facts · 0 invented OPEN · 0 silent HIGHs · 0 false
  alarms**; the walkthrough's one HIGH dissolved under fresh retrieval (the
  ask-time tree already carried operational content for *"genuinely better
  built"*); both case-B agents converged on the actual fm #827 repair
  sight-unseen.
- Surfaces updated so nothing keeps calling the test outstanding: roadmap § 2
  row + § 4.8 second-live-run paragraph + § 8 bullets 1 and 3 (amendment
  trail preserved); boot file entry 1b; `intake` replay section (kit-named —
  SKILLS-local ⚠ re-apply entry extended to cover it); `current-state.md`
  Recently-shipped entry + in-place supersede of the fm #830 clause; program
  § 7 row (NOW unchanged); findings index row.
- `.substrate/check-exceptions.yml`: 3 reason-carrying entries for the raw
  folder's verbatim-quote fires (2× stamp, 1× false-wall) — the reports are
  the measurement; rewording them would corrupt it.

**Verify (run this session, tails verbatim):**

- `python3 scripts/check_docs_links.py` →
  `CLEAN — every intra-repo link in 378 file(s) resolves` · exit 0
- `python3 bootstrap.py check --strict` → exit 1 with exactly one finding:
  `[preflight-script] … born-red HOLD` naming this card (the designed pre-flip
  state; the 7 raw-folder findings resolved by badges + reasons, suppressions
  fire with verdicts recorded)
- `python3 verify_citations.py <pin> <tsv>` (substance, ±3) → A1 47/51 ·
  A2 53/55 · A3 50/54 · B1+B2 59/62 machine-PASS; every non-PASS row opened
  and adjudicated in the evidence folder's README (needle/harness artifacts
  separated from real imprecisions)
- `python3 verify_citations.py <pin> <tsv> --exact` (attribution, round 1) →
  A1 46/51 · A2 51/55 · A3 50/54 · B1+B2 57/62; the five rows passing ±3 but
  failing exact + the six substance-adjudicated ones = the 11 attribution
  imprecisions
- CI red on PR #851 verified against the job log: 3 findings = the born-red
  hold ×2 + the `[reachable]` orphan, discharged by this batch's index/links

⚑ Flags (MEDIUM, decided per intake step 7): pin choice = parent of the
receiving session's first landed PR (exact boot minute unknowable); the one
citation-overreach adjudicated as attribution-family, not fabrication (raw
data committed for re-adjudication); scale 3+2 agents (counts, not rates).
⚑ Owner-queue: unchanged — no owner ask touched (OQ-FM-D2-TARGET stands).
💡 Session idea: **a cite-check pass for intent maps** — all 7 D1 defects are
one class (a cited range not carrying the quoted content), the exact class
`tools/gemini_delegate.py` already verifies for delegated reads; measured need
7/222. Promotion-rule gated: flagged, deliberately not built after one run.
⟲ Previous-session review: in the header section above — fm #849/#850's card
checked against `main`, accurate, nothing to repair.

**Codex round 1 (head `6b7a3f6`; review ~6.5 min after the literal
`@codex review` comment): 6 inline findings — 2 P1 · 4 P2; 5 `[conceded]` ·
1 `[partial]`, each verified against source before acting:**

1. `[conceded]` P1 — "the prescribed test has run" overclaimed: the recorded
   bar is a fresh agent that produces **and scores** (verified at
   `2026-08-09-intent-map-replay.md:166` and the fm #830 disposition card,
   round-1 row 3). Every surface reframed to producer-half-run /
   scorer-half-outstanding; the mechanism claim scoped producer-side.
2. `[conceded]` P1 — the "221/222 ESTABLISHED citations" metric mislabeled
   its denominator: the TSVs encode citations from the whole reports.
   Relabeled as an all-report check with the ESTABLISHED subset (188 rows,
   187/188) partitioned per agent in the evidence folder README.
3. `[conceded]` P2 — the ±3 tolerance converted small wrong ranges into
   machine-PASSes that never reached adjudication. `--exact` mode added, both
   passes reported; attribution imprecisions 6 → **11** (the five predicted
   rows all reproduced).
4. `[conceded]` P2 — the finding described pin A's `SKILLS-local.md` as
   absent; it exists (87 lines) and lacks only the "All 27" section. Both
   sites corrected with the error named — a scorer error the agents did not
   make.
5. `[conceded]` P2 — A3's "26 installed entries" was acknowledged but not
   counted; now an ESTABLISHED factual defect in the tally and verdict.
6. `[partial]` P2 — OPEN-column discipline was outside the pre-registered
   rubric: conceded that the gap is real and counted the instances (A1 ×2,
   A2 ×3, A3 ×3, B2 dispositions-inline, B1 strict); kept as `[partial]`
   because the entries also follow the procedure's own step 4 ambiguity
   ("every unresolved item gets a class" with no home for decided items) —
   recorded as a procedure defect in § 4, with the one-line `intake` fix
   deliberately left to the round that next amends the skill.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached)

PR: menno420/fleet-manager#851 — ready, born-red hold until this badge flips.
