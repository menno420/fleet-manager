# EAP mail evidence report — night fleet, 2026-09-01/02

> **Status:** `reference` · produced by two verified, novelty-checked fan-outs
> run overnight (fleet-preflight sheet: `docs/findings/data/workflows/05-CONTRACTS-night.md`,
> scripts beside it) while the owner slept. Every finding below draws on a
> **verifier's `corrected_claim`** — quoted directly where one lens supplied
> usable text; synthesized from the row plus both lenses' records where the
> two lenses' corrections needed combining (FD-02); quoted directly from the
> **retained original candidate** where a `corrected_claim` was itself
> unusable and the candidate wording survived intact elsewhere in the raw
> JSON (B5) — but never the raw candidate or merge-stage wording taken alone
> *without* checking it against the verifiers first, per the night brief's
> own rule. Fleet A's non-survivors are
> listed with their individual reason (§ 2); **Fleet B's 25 non-survivors are
> not** — this report has only the aggregate "refuted," a known gap named in
> § 3 and § 5 (the individual reasons exist in each row's raw verifier record
> under `docs/findings/data/2026-09-02-eap-mail-evidence/`, just not pulled
> into this document). **Read the "What was not read, and what
> the critics found wrong" section before using anything here for the mail** —
> both critics found real, unfixed defects in what survived, and the owner's
> own stated top priority for this mail (the false-done pattern) is under-
> represented in Fleet A's three spines.

## 0 · What ran, what was cut, and why (the OPEN item this report closes)

- **Venue:** cloud container, this session. **Concurrency measured 2** (demand
  test, `05-CONTRACTS-night.md`) — not the pilot's 6, not the "4" seen on
  another container. Every size below follows from that number.
- **Fleet A** (`04-eap-mail-evidence-pass.js`, unchanged except args) ran to
  completion: **84 agents, 7.84M tokens, 156.5 min** (run `wf_bda232c1-cf5`).
  Floor was 2.1h; actual 2.6h — the floor's own caveat (phase barriers, `effort:
  'high'` stages) held.
- **Fleet B** (`05-eap-false-done-ledger.js`, authored tonight) ran a **3-unit
  pilot** concurrently with Fleet A (a sizing mistake — it cost Fleet A wall-
  clock by sharing the same 2 slots) — **37 agents, 2.66M tokens, 38.4 min**
  (run `wf_d0348386-8b6`) — then, once Fleet A landed, a **full run scoped to
  the fleet-manager-only lane** (`skipSatellite: true` — 16 reader units, the
  11 named EAP docs split over 400 lines) — **83 agents, 7.11M tokens, 146.7
  min** (run `wf_fb35b278-362`). See § 3 for the result: 3 survivors, not the
  pilot's 4 — two of the pilot's survivors did not survive the full run, but
  the two corpora are **not nested**, and the two losses have different
  mechanisms, not one shared cause **[CORRECTED, Codex review round 15:
  this summary previously said both lost the same cut superbot reader —
  only one did]**. Read § 3 in full before trusting any count or causal
  claim here; this summary intentionally does not restate the mechanism.
- **CUT: the 32 superbot `docs/eap` reader units** (of Fleet B's full 48-unit
  design) — dropped **before** any fleet-manager-side cut, exactly as the
  night brief's SIZE rule specifies ("drop Fleet B's satellite-heavy readers
  before dropping its fleet-manager readers"). The pilot's 1 superbot reader
  is the only superbot-side evidence **Fleet B's false-done pass** read
  tonight — **[SCOPED, Codex review round 11]** not "in this pass" overall:
  Fleet A separately and systematically read 5 superbot prior-mail files
  (§ 1, § 4), which is unaffected by this cut.
- **CUT: Fleet C** (the 19-repo EAP-birth closeout audit) — not attempted.
  Fleet A alone took 2.6h against a measured concurrency of 2; there was no
  wall-clock left to fit a third fleet before 05:00 Europe/Amsterdam, let
  alone 04:00.
- **Stop rule that fired:** the night brief's own conditional — "if A alone
  would run past 04:00, drop Fleet B's satellite-heavy readers" — fired
  before Fleet A even finished, once the demand test returned concurrency 2
  instead of the pilot's 6.

## 1 · Corpus census (pasted from `05-CONTRACTS-night.md`, not recomposed)

**Fleet A** — fleet-manager@fa9a391: 20 synthesis/record documents ≈590 KB
(15 doc readers + 5 owner-word readers) · 284-pattern catalogue (1.47 MB)
resharded into 12 files (161684+136817+130276+123659+119956+129328+120359+
125216+127275+123470+117583+93707 bytes; high-severity&repo_count≥3: 118;
no covering mechanism named: 51; panel-killed: 7) + 20 repo censuses (395 KB)
· prior mails: **[CORRECTED, Codex review round 8]** the retained result
carries **6** `prior_mails` entries, not the 7-file design the pilot's own
CONTRACTS sheet named — 5 superbot files (`anthropic-email-2/3/4`,
`gen1-wrapup-email-final-candidate`, `2026-07-18-followup-email-draft`) plus
the current fleet-manager draft; `permission-classifier-findings-consolidated-2026-07-16.md`
is missing from the executed **prior-mail extraction readers** despite
being cited as `covered_by` for non-survivor A3-7 in § 2 — **[CORRECTED,
Codex review rounds 9-10]** A3-7's coverage verdict is not unsupported:
its verifiers list this file in `what_i_opened` and cite its contents
directly, so the gap is narrower than "never opened by this pass" for A3-7
— it was opened by verifiers checking overlap, just never fed to the
systematic prior-mail extraction stage. **B14 is a different case, checked
directly and NOT the same gap**: its fit-lens verifier's `already_covered_by`
names `anthropic-email-4-classifier-regression-sent-2026-07-16.md`, a file
that WAS in the executed 6-file extraction corpus — B14's overlap
verdict rests on a file this pass did read, not the missing one (SHA unchanged
from the 2026-09-01 pilot, 5e3a667, for the files that did run).
**Gap the corpus does NOT cover, named by Fleet A's own critic:** `fa9a391`
added `docs/findings/2026-09-01-owner-direction.md`,
`docs/findings/2026-09-01-fleet-manager-measured.md` and the successor-
structure proposal after the pilot's base SHA — none are in Fleet A's fixed
reader list (the script ran "unchanged except args," per the night brief), so
none of tonight's Fleet A readers opened the owner's own most recent sitting
about this very mail. See § 5.

**Fleet B** — superbot@5e3a667 docs/eap: 30 files, 6,192 lines, 507,874 bytes
(fetched 2026-09-01T21:40Z) · fleet-manager@fa9a391: 11 named EAP docs,
343,739 bytes, split into 16 reader units at the 400-line threshold. Combined
design corpus 41 files / 851,613 bytes / 48 units; **tonight's actual read is
smaller** — pilot read 2 fm units + 1 sb unit; the full scoped run read the
16 fm units and **0 of the 32 sb units** (cut, see § 0).

## 2 · Fleet A — verified findings surviving both lenses (12 of 16 verified, 27 ranked, 44 pooled, 284 pattern rows read)

Each row is the surviving candidate's **id**, its wording, scope, and
citations. Wording is the first verifier's **`corrected_claim`** for every
row except **B5**, whose text is instead the **retained original candidate
quotation** (its `corrected_claim` field is itself corrupted — see item 6);
never the merge stage's wording taken alone without checking it against a
verifier. Where the critic (§ 5) caught an error the verifier itself did
not fix in the payload, that is flagged inline as **[UNFIXED]** — these
numbers must be corrected before anything here goes into a mail.

1. **A1-5+B10+B11** (finding, both) — *The delivery tier a rule sits in, not
   its wording, predicts whether agents follow it: where a rule is a
   required, exit-affecting check on a literal marker, compliance is
   near-total (335/335, 302/302, 503/503 session cards, three repositories);
   where the same class of rule is advisory prose that cannot fail a build,
   the same audit found decay (23 stale claim files untouched in one
   repository; a review protocol last run 46 days before its own census).*
   **[CORRECTED, Codex review round 14: the headline overclaims.]** The
   fit-lens verifier rejects "predicts whether agents follow it" as written:
   the 335/335, 302/302 and 503/503 figures measure presence of a literal
   marker, not adherence to the rule the marker stands for. The websites
   row is its own counterexample in the same source — 302/302 cards are
   "structurally perfect" on marker presence, but of those same 302 cards
   only **~10% name any skill** and **5/302 (≈1.7%) use the estate's own
   disposition vocabulary**. The narrower, source-supported claim: a
   binary exit-affecting check on a literal marker gets near-total
   adherence *to the marker*; the reasoning the marker exists to represent
   is not carried across by the same mechanism, and this report's own
   framing had promoted byte-form compliance into behavioral compliance.
   Citations: `docs/findings/2026-08-28-substrate-kit-genesis-dig.md`,
   `docs/findings/2026-08-29-estate-agent-error-audit.md`.
   **[DISPUTED, not "unfixed" — corrected, Codex review round 7]** the
   payload reads "10 of 20 rows report no `.claude/` directory," and this
   is NOT a clean error: the original census reader's count, AND the
   holds-lens verifier's own independent recount, both land on **10**
   (holds-lens: *"I counted the rows myself: exactly 10... the candidate's
   10 is right"*); only the fit-lens verifier's separate recount reports
   **9** (two regex passes, omitting `sim-lab`). This report previously
   presented the fit-lens's 9 as the correction and the payload's 10 as
   unfixed — reversed: it is an unresolved 9-vs-10 split between the two
   lenses, 2 of 3 counts (census + holds-lens) favoring 10. Needs a fresh
   recount to settle, not a silent pick of either lens.
   **[CORRECTION, per the owner's 2026-09-01 sitting, unread by this
   reader]**: the "1 of 20 repos has hooks" framing is not a coverage gap —
   the owner states it is **deliberate** (owner ruling recorded in
   `docs/decisions.md` and `docs/findings/2026-09-01-owner-direction.md` § 4):
   fleet-manager is always
   the cloud-session root by design, so its hooks apply to every session that
   roots there regardless of how many other repos load no `.claude/` of
   their own. State this finding with that correction attached, or drop the
   hook-coverage half entirely.
2. **A1-2+A2-2+A3-9** (finding, both) — *Same-family adversarial self-review,
   in the two designs this estate measured, discriminated only where the
   decision rule let a single skeptic win and the refuters were independent
   of the author; where it did not, it looked rigorous and refuted almost
   nothing.* **[REVERSED, Codex review round 11 — "7.0%" is right, not
   wrong]** this report previously flagged "7.0% of 925 verdicts" as an
   error needing correction to "6.5% (60/925)" — backwards. Checked
   directly: summing `refuter_count` across all 284 rows of
   `docs/findings/data/2026-08-29-agent-error-patterns.jsonl` gives **65**,
   and 65/925 = 7.03% ≈ **7.0%, matching the payload as written**. The
   verifier's own discrepancy note says exactly this ("i.e. the 7.0% is
   right") — "60" is the mismatched figure (the source's own 293
   CONFIRMED + 572 PARTIAL + 60 REFUTED pattern-level tally, a different
   count from the 65 refuting lens-verdicts), not "7.0%". Do not change
   this row's percentage before send. Also carries a citation the same
   verifier found supports none of its claims
   (`2026-08-24-e1-source-sweep.md:284-288`) and a "load-bearing
   correction" the verifier showed was already applied in the current
   draft on 2026-08-25 — this row is stale in two other places than its
   own corrected_claim admits, just not the percentage.
3. **A1-7+A2-6+B2** (finding, both) — *A null or clean result is
   indistinguishable, in what an agent sees, from a check that never ran,
   never covered the case, or never executed as written — and the same
   collapse reaches the human reader.* Instances: a term-less 26-repo search
   returning 0 everywhere, caught only because a known-good control also
   came back empty; the CI gate collecting 73 of 121 tests with 48 invisible
   (superbot-games, 2026-07-10); the space-stripping phrase regex that ran
   under 986 agents and moved the corpus +127 sections (+1%) once fixed
   (2026-08-29) — small in scale, real in kind: a regex silently
   under-counting is the same failure class as a null result read as
   clean. Dropped from all three spines for budget, not weakness —
   the top graft recommendation from 2 of the 3 judges (product-lens and
   evidence-lens; the owner-rules judge recommends the concurrency finding
   instead, see § 7 — not unanimous, corrected per Codex review, fm #1010).
4. **A2-3+B1** (finding, general) — *Agent-authored checks are landed and
   counted as coverage after a single green run, with no run in which they
   were ever shown to fail; when the instrument is broken, its silence is
   read as a measurement.* Citation: an independent guard review's "nine
   findings, seven real defects" is cited only second-hand
   (`2026-08-09-error-to-mechanism.md:331-341`) — **[UNVERIFIED, per the
   critic]** the primary record (`2026-08-09-independent-guard-review.md`)
   was never opened by this pass.
5. **A1-1+B8** (finding, both) — *On the GitHub surfaces measured, human and
   agent authorship are not distinguishable, and the error runs in both
   directions.* Of 155 PR-review comments posted under the owner's own
   identity across **all 12 of the 28 repositories that have any review
   comments**, 135 (87%) carry a literal agent marker and the remaining 20
   read identically on inspection; of 564 issue comments enumerated in **the
   6 busiest of 28**, 562 are agent-attributable, 2 indeterminate, 0 read as
   his own voice — one narrates him in the third person from his own
   account. Keep the exact denominators ("12 of 28," "6 of 28") — collapsing
   either to a bare "of 28" was the precise overclaim the source itself
   corrects. State the cause plainly: agents authenticate with his own
   shared credential — this estate's own choice, not a platform defect.
6. **B5** (finding, both) — *The evidence cited for a done/verified claim
   routinely establishes something narrower than the claim: a green suite
   standing for the shipped path, one enforcement claim naming a mechanism
   nothing implements.* *"The evidence cited for a done or verified claim
   routinely establishes something narrower or different from the claim it
   is cited for: a green suite standing for the shipped path (repo_count
   9), one environment or viewport standing for the whole surface (7), a
   call's success standing for the state it was meant to produce (5), and a
   proxy signal standing for the property it approximates (2)."* **[DATA
   DEFECT, per the critic — CORRECTED, Codex review round 8]**: the
   downstream `verified[].row.claim` field this pass's spine/critic stages
   were shown is verifier meta-commentary ("Holds as written; the numbers
   9, 7, 5 and 2 are exact repo_counts...") instead of the claim — but the
   text above is **not lost or reconstructed**; it is the original
   candidate wording, retained intact at
   `result.verified[].candidate.claim` (id `B5`) in
   `fleet-a-full-wf_bda232c1-cf5.json`, quoted directly. The defect is in
   the prompt construction that built the downstream `survivorBrief` passed
   to spine/critic agents, not in what was measured or retained. This is
   also the row closest to the owner's own stated priority for this mail
   (§ 6) and it is in **none of the three spines** — see § 5.
7. **A1-9+B3** (finding, general) — *The change lands correctly and
   everything the change obligates elsewhere does not: a companion artifact
   owed by the same diff (a derived file, a ledger row, an index link, a
   committed binary) goes unshipped.* **[PROVENANCE FLAG, per the critic]**
   the row survived only after its central sentence was inverted mid-pass —
   the scope qualifier was preserved at source and dropped in the copies,
   not the reverse as the row's own "why" field still narrates. Rewrite
   before use.
8. **A2-7+B6** (finding, both) — *Claims about a named artifact are written
   without the artifact being resolved: references that do not exist or do
   not contain what is claimed (repo_count 10).* **[CORRECTED, review pass
   2026-09-02 (fm #1010's landing session)]** this row shipped, until the
   flip, a citation its own verifier flagged as not resolving
   (`idea-engine docs/audits/eap-project-audit-2026-07-14.md:76` — "at line
   76, a time-to-land PR sampling table... the fabrication material is at
   lines 151 and 165. Either the repo attribution or the line number is
   wrong") — the finding about unresolved references itself shipped one.
   Resolved against this repository's own copy, opened at the flip head:
   `docs/audits/eap-project-audit-2026-07-14.md:151` (the Codex-relay row —
   "Cost arrived as fabrication — #4... the VERDICT 016 gate (3/3
   fabrications caught, 0/24 false alarms)") and `:165` (the gate ordered
   fleet-wide MANDATORY), with the suspension itself at
   `docs/fleet-inconsistencies-2026-07-13.md:147` (INC-43: the `@codex`
   verdict-review step SUSPENDED at `dedc12e` "after 3/3 verified fabricated
   reviews (incidents #1–#3)"). The idea-engine copy was not opened (that
   repository was not attached); cite the fleet-manager lines.
9. **A2-4+A2-5 — CORRECTED (Codex review round 11): wrong method/denominator
   in the original text.** *Delivering the rule at the moment of action has
   a measured ceiling and two silent failure modes: of 13 errors from one
   session, scored against a two-part test (does an actionable moment exist,
   and is the error decidable there from the text alone) — 8 were
   machine-decidable (4 already watched, 2 built, 2 buildable but
   deliberately declined), 3 needed a human procedure, 1 had no moment, 1
   remains an open design question; in the register of 8 recurring failure
   patterns, 7 are delivered by a reminder route and exactly 1 has a
   deterministic checker.* This report previously stated the 13 errors were
   "scored against 116 committed statements, the statements caught 0" — that
   116-statements/0-caught pair is a **different** measurement, already in
   the current draft's own Finding 3; conflating the two invented a method
   and denominator for this row. The two-part-test scoring above is the
   row's real, distinct basis — **[CERTAINTY, Codex review round 12]**
   labeled `REASONED` at source (`docs/findings/2026-08-09-error-to-mechanism.md:14-17`),
   not `MEASURED` — only the detector/check replays this candidate also
   cites are measured. Do not upgrade this scoring's certainty when using
   it.
10. **A1-6** (finding, both) — *A merge-blocking check that verifies a
    marker's presence, not its substance, reached full compliance while a
    sampled slot the check never covers held nothing about 1 in 9 times.*
    **[CORRECTED, Codex review round 13: these are two different checks
    over two different fields, not one result at two sample sizes.]** Over
    fleet-manager's full 161 August session cards, the 💡 idea marker was
    present 161/161 and a mechanical detector found **zero** empty review
    sections — the gate held everywhere it actually checked. A separate,
    disjoint 27-card sample checked idea-slot *content* (a field the
    mechanical detector does not cover) and found ~11% (~1-in-9) holding no
    actual idea — dispatch text or a mission restatement, not leftover
    template text (an adversarial probe over all 161 cards found zero
    surviving auto-drafted hint strings, so the empty slots were authored,
    not template residue). Clean, well-cited, no critic flag.
11. **B4** (finding, general) — *Values an available command or the
    environment would supply are written from recall or composition instead:
    counts and figures in 12 repositories, time values in 8.* **[WORDING
    RISK, per the critic]** the "no ambient clock" framing is refutable as
    written (a date *is* in the session's own context) — reword to "not
    re-checked against the clock at the moment of writing" before use.
12. **A3-1+A2-1+B13 — NARROWED (Codex review round 4, fm #1010): the
    fit-lens verifier explicitly drops the row's first leg.** The merge
    stage's original wording (a broad "see the other sessions" ask covering
    reachability, provenance, reservation and concurrency) is what this
    report originally quoted; the fit-lens `corrected_claim` instead says
    *"Drop leg 1 entirely (it is draft ask 3 and July ask (d)7 restated)"*
    and narrows the row to two legs the current draft does NOT already
    carry: **(a)** a shared-namespace reservation primitive — this estate's
    parallel lanes built the same artefact twice for want of one
    (substrate-kit PRs #362/#363 built the same ORDER independently; two
    lanes adopted the identical kit 7 minutes apart, ~19 min of one lane's
    work wasted; three subagents independently minted the identical
    identifier "G-7" for three different primitives); **(b)** a per-launch
    concurrency figure an agent can read — one 1,063-agent run showed
    observed concurrency of peak 4, median 4, mean 3.43 across 4,097
    samples against a documented 10–16, "per-container and cannot be
    inherited." Its own proposed ask line: *"A concurrency figure and a
    shared-namespace reservation primitive an agent can read at launch —
    because a fan-out plan sized from the documented 10-16 against an
    observed 4 gets its wall clock wrong by more than 3×, and four separate
    lanes in this estate built the same artefact twice for want of a way to
    say 'I have this one.'"* **[CAVEAT, Codex review round 11]** the "more
    than 3×" figure in that quoted ask line is not unconditionally true —
    documented-10 against observed-4 is 2.5×, documented-mean-3.43 is
    ~2.9×; only the top of the documented 10–16 range clears 3×. Quoted
    here verbatim as the verifier wrote it; if this line goes into the
    actual mail, bound it ("up to 4×") or name which documented figure it
    compares against, rather than sending "more than 3×" unconditionally.
    The reachability/provenance material (74
    session records, 54 reachable, 0-of-418 carrying a machine field), if
    used at all, belongs as one clause under the current draft's existing
    ask 3, not as a second ask. This is the pass's only surviving
    **ask**-role candidate, and it is in **none of the three spines** (§ 5)
    — meaning none of the three even carries the narrowed version.

**4 non-survivors, with reason** (not silently dropped):

| id | reason | covered_by |
|---|---|---|
| A1-3+A3-10 | refuted — already argued | the blind-scored eval and its thesis are already in the current draft (lines 172-196, 246-257); only the PARTIAL/3-of-3 verdict was genuinely new and is worth folding into the existing paragraph, not a new finding |
| A3-6 | refuted — already argued | `anthropic-email-4-classifier-regression-sent-2026-07-16.md` (SENT mail) |
| A3-7 | refuted — partly argued | `permission-classifier-findings-consolidated-2026-07-16.md` (SENT superbot mail) — the ask half is already sent; only the evidence half (three-settings test, ~1,900 orphans) is genuinely new |
| B14 | refuted — already argued | `anthropic-email-4-classifier-regression-sent-2026-07-16.md` — "some denials were correct" is already in the July mails' balance paragraph |

## 3 · Fleet B — the false-done ledger

**Pilot (3 reader units, run `wf_d0348386-8b6`):** 59 claims, 35 corrections
extracted → 18 merged rows → 16 ranked → 15 verified → **4 survivors**:

- **L02** — venture-lab's membership-kit product was listed ready-to-sell
  ("Stripe Checkout + webhook, pre-wired," 13/13 tests green) on or before
  2026-07-10; the headline Stripe path had never executed against real
  Stripe — the tests injected synthetic events from a hand-rolled helper that
  always set `customer_email`, while the live path had `customer_email: null`
  on real events plus an invalid success-URL placeholder. Found the same
  night by the fleet-manager night review (R23); fix issued as venture-lab
  ORDER 003. Citations (verifier-corrected): claim — **[PATH FIXED, Codex
  review round 3, fm #1010]** `superbot:docs/eap/fleet-overnight-review-2026-07-10.md:33,105`
  at pinned SHA `5e3a667` (the verifier's original citation used this
  session's `/tmp/eap-night/...` scratch fetch, an uncommitted container
  path that will not survive this session — replaced with the pinned repo
  path so the citation stays independently verifiable); found —
  `docs/findings/night-review-2026-07-10.md:31-33,118-140` (a file
  **outside** tonight's fixed reader list, opened by the verifier directly —
  see § 5).
- **L03** — superbot-games PR #16 asserted that the substrate-gate CI step
  now ran the test suite (fleet-manager's rendering — no file here
  reproduces the PR body itself, see FD-01's correction in § 2); the gate
  collected 73 of 121 tests (48 exploration tests invisible), and the
  session card's own arithmetic (62+11=73) papered over the gap. Graded
  "FALSE as stated" the same night (a direct quote of the night review's
  own verdict word, `docs/findings/night-review-2026-07-10.md:330-334`);
  fixed the next day (PR #24), floor later raised 121→147→230.
- **L04** — pokemon-mod-lab declared itself PRIVATE "no exceptions" in its
  README and 8 PR bodies while world-readable the whole time, with vendored
  Nintendo source shipped publicly; caught by the same night review (Q16);
  owner flipped it private; became live rule R22 VISIBILITY GUARD.
- **L08** — "agent self-arming routines WORK," with four lanes cited as
  first-fire evidence — true for arming/firing, but a project-created
  routine carries no repo scope, so the woken session arrives with nothing
  attached; the owner later put the failure rate at "about 1 in 3" on one
  lane (2026-07-26). **Contradiction, unresolved:** the same underlying claim
  appears as **L07** and **L12** in this same pilot, both refuted — the
  dedupe pass did not merge L07/L08/L12 into one row with one verdict. The
  ledger simultaneously publishes and retracts the same false-done; treat
  L08 as provisional until reconciled.

11 refuted (routine plan-evolution, not false-dones, or citations that did
not hold up); **0 rows killed by both-lenses coverage agreement**
(**[CORRECTED, Codex review round 11]** not "0 already-covered" as
originally written — `already_covered_by` is populated on multiple
fit-lens verdicts in the raw pilot JSON, including L01, L02, L05, L06 and
L15 with real citations (`docs/planning/2026-08-30-fresh-start-redirect.md`,
`docs/fleet-account-2026-07-26.md`, `docs/traps.md` TRAP-001), the same
distinction § 3's full-run text already makes — applied here too).

**Full run (16 fleet-manager-only reader units, `skipSatellite: true`, run
`wf_fb35b278-362`):** 505 claims, 332 corrections extracted → 150 merged rows
→ 30 ranked → 28 verified → **3 survivors**, 25 refuted. **Correction (Codex
review, fm #1010): `already_covered_by` was NOT left empty on 0 rows** — it
is populated on several lenses, including two of the three survivors below
(FD-02's fit lens names `docs/playbook.md` R22; FD-17's fit lens names
`docs/traps.md` TRAP-006/007). No row was *killed* by the both-lenses-covered
path (the aggregation rule requires both lenses to agree, and none did), but
"0 already-covered" as originally written implied the field went unused,
which is false — it shows real, if split, coverage verdicts the ledger
should have surfaced rather than this report erasing. `docs/traps.md` itself
still was never in the reader corpus, which is the more precise version of
the original claim (see § 5).

- **FD-01** (merges 4 sub-rows) — superbot-games PR #16 asserted that the
  substrate-gate CI step now ran the test suite, and the lane's close-out
  heartbeats reported clean status ("mining gen-1 complete green") on that
  gate. **CORRECTED (Codex review round 13): both wordings — "substrate-gate
  now runs the suite" and "mining gen-1 complete green" — are
  fleet-manager's own renderings, not verbatim quotes; no file readable
  from this repo reproduces PR #16's body or the heartbeat text itself
  (both verifiers flag this: certainty is high on the measured 73/121
  substance, one notch lower on "quoted verbatim").** Actually: the gate
  collected 73 of 121 tests — `games/exploration/tests/` (48 tests) was
  invisible, and neither close-out heartbeat acknowledged the fix order.
  This is the pilot's **L03**, now cited from two fleet-manager documents
  (`docs/eap-story.md`, `docs/launch-readiness-2026-07-10.md`) instead of
  one — **CORRECTED (Codex review, fm #1010): these are two corroborating
  retellings of the same primary measurement, not independent evidence.**
  Both are fleet-manager renderings of `docs/findings/night-review-2026-07-10.md`
  (§ 5's "single most damaging omission"), which no reader in this pass
  opened. A second layer the pilot didn't catch: the close-out heartbeats
  that *kept reporting green* after the gap was found.
- **FD-02** (merges 5 sub-rows) — pokemon-mod-lab's README declared PRIVATE
  "no exceptions" and 8 PR bodies repeated it, while the repo was
  world-readable with vendored Nintendo source, matching all 13 account
  repos being public at the time. This is the pilot's **L04** — same
  finding, now also carrying the residue the pilot missed:
  `docs/launch-readiness-2026-07-10.md:551-554` records ORDER 003 (the
  standing R22 guard) appended at `a76ada7` 12:56Z, while the same
  document's own API check confirming `private:true` is timestamped
  ~15:12Z (line 545) — the guard-append precedes the cited
  API-verification by ~2h16m, an ordering the source document leaves
  unreconciled itself. **CORRECTED (Codex review round 13): this report
  previously stated the guard was appended *after* the verified flip,
  which reverses the source's own two timestamps.** Either ordering, the
  residue holds: the status file still lacked the
  `visibility: private — verified <ts> via <surface>` line the guard
  exists to add.
- **FD-17 — CORRECTED (Codex review, fm #1010): narrow to one sub-claim, not
  six.** The merge stage grouped six disposition-stamp sub-rows into one
  row, but the fit-lens verifier's `corrected_claim` explicitly narrows it:
  *"fleet-manager stamped sim-lab's OA-002 struck-through as resolved
  ('~~Owner: enable Codex (OA-002)~~ resolved — Codex envs exist for all 12
  repos') while sim-lab held OA-002 open with 6+ @codex questions pending;
  the 2026-07-13/14 fleet review found the stamp conflated
  integration-ENABLED with usage-QUOTA-capped."* The other five sub-claims
  the merge bundled in do **not** hold as false-dones per the same verifier:
  the INC-40/INC-41 "✅ RESOLVED" stamps name their own residue in the same
  table cell (honestly scoped, not a later correction); the ORDER 002/014
  "done" stamp is independently corroborated (`bbaccec`); the inbox-vs-
  status.md lag (INC-73) is filed by the ledger itself as by-design under a
  documented one-writer convention; and the "~65 of 82 items never retired"
  figure is quoted from `docs/audits/2026-08-10-full-read/findings.md`, a
  document **outside both this pass's corpus and the EAP fortnight the
  ledger covers** — it is queue decay against dispositions that document's
  own § 12 calls "recommendations... not completed work," not a false-done.
  This report originally stated all six as one surviving row, which
  contradicted the verifier's own correction; the row above is the corrected
  version. Coverage: TRAP-006/007-family per the fit lens, "a variant
  instrument... not a duplicate" (registry/queue disposition stamps, not
  session-card status flips).

**Two of the pilot's four survivors did not survive the full run — CORRECTED
framing (Codex review, fm #1010): the two corpora are not nested, so this is
not clean evidence of scaling or verifier instability.** L08 (self-arming
routines) reappears as **FD-13**, refuted. **L02 (venture-lab's Stripe
false-green) does NOT map to FD-09** — **[CORRECTED, Codex review round 9]**
FD-09 is an unrelated $29 Gumroad-product claim; the actual fate of L02's
underlying claim, checked directly against the raw JSON, is that it **never
entered the full run's claim pool at all** — its refutation survives only
as four unmatched `orphaned_corrections` entries (the false-done itself:
"the headline claim has never executed against real Stripe... 13 green
tests inject synthetic events authored from memory," each dropped because
no matching done-claim exists in the pool — four differently worded
`reason` fields, one of them verbatim "No earlier done-claim found in this
corpus for venture-lab's Stripe integration being green/verified before
2026-07-10"; the pool's only venture-lab Stripe done-claims are the $29
Gumroad kit of 2026-07-12 and PR #9 of 2026-07-10, a different product
**[PRECISION, review pass 2026-09-02: this sentence previously presented
one paraphrase as the quoted reason of all four]**).

**L02 and L08 lost their pilot-survival evidence for two different reasons
— [CORRECTED, Codex review round 14, then corrected again round 15: round
14 misdiagnosed L02's mechanism].** L08's correction cited
`anthropic-email-2-draft-2026-07-11.md` — the one superbot file the pilot
happened to read, the exact file `skipSatellite: true` removed from the
full run; that loss is real and mechanical. **L02's correction cited
`docs/eap-story.md` throughout, in both runs — a fleet-manager file that
was never cut**, so its loss cannot be a satellite-cut effect either way.
**What actually happened to L02, per round 15's correction: the READERS
did not disagree.** Both the pilot's `docs/eap-story.md` reader (lines
1-300, citing the correction at `:229-233`) and the full run's equivalent
reader (citing it at `:241-245`, the file having shifted) extracted the
correction and **no matching claim** — checked directly:
`result.readers[0].claims` in the retained pilot JSON (21 entries) has no
venture-lab/Stripe/membership-kit claim, the same as the full run. The
actual divergence is in the **merge stage**, not the readers: the merge
contract is explicit ("a ledger ROW requires BOTH a claim ... AND a
correction ... do not manufacture" a row when no matching claim exists,
`05-eap-false-done-ledger.js:182`) — but L02's own `certainty` field
admits the pilot's merge violated exactly that rule: "the claim side is
reconstructed from the correction record, which is the only place the
13-green-tests status is quoted." The pilot's merge stage invented a
claim from an orphaned correction; the full run's merge stage correctly
left the same correction unmatched, in `orphaned_corrections`. Only
L03 → FD-01 and L04 → FD-02, the two fleet-manager-sourced pilot
survivors, held cleanly in both runs. The honest statement: **one row
(L08) lost its evidence to the satellite cut; the other (L02) never had a
matching claim in either run — the pilot's own merge stage should not
have produced it, and the full run correctly declined to** — different
mechanisms, and a rerun proposing to recover L02 by re-adding the
superbot lane, or by fixing reader coverage, would not fix the actual
cause; the fix belongs in the merge stage's own contract enforcement.

**25 non-survivors carry only the word "refuted" IN THIS REPORT** — not in
the raw output. **[CORRECTED, Codex review, fm #1010]** every non-survivor's
full verifier records (both lenses' `what_i_opened`, `discrepancies`,
`corrected_claim`, `already_covered_by`) are retained in
`docs/findings/data/2026-09-02-eap-mail-evidence/fleet-b-full-wf_fb35b278-362.json`
— the evidence is not lost or unauditable, it simply was not pulled into
this Markdown document. The CONTRACTS sheet's pilot note flagged this exact
gap and named the fix (pull a reason from each verifier's `discrepancies`
field into the report); that pull is next-session work, not done here.

## 4 · Prior-mail overlap map (6 readers — 5 superbot prior-mail files + the current fleet-manager draft; **[CORRECTED, Codex review round 9]** not 7 — see § 1's corrected corpus census)

| source | status | topics | asks | good-parts |
|---|---|---|---|---|
| email-4 (classifier regression) | **SENT** 2026-07-16 ~21:12Z | coordinator/worker trust boundary, model-independence, coordinator-merge-freedom proposal, "can't use the product to debug the product," settable permission scope | 13 | 5 |
| email-2 (scale-up) | **SENT** 2026-07-12 13:24:40Z (thread `19f41cd2e5380bb3`) — Fleet A's own critic found one candidate's overlap verdict treated this as an unconfirmed draft; that verdict is void, see § 5 | scale arc 1-3→15→8 repos, shared memory as standout win, durable-state recoverability, born-red+auto-merge composition, agent-armed Routines, mechanical-vs-social-layer trust, merge-authority root cause, Routine model drift, Routines spawning repo-less, owner-click gating, two-vantage permission split, Routine observability, trigger-scheduler incident, carryover from July 8, hand-built compensating patterns, shipped-work roundup, public review website, self-wake wobble + 3-option proposal, ranked "what would help" list — **[CORRECTED, Codex review round 14: this cell was missing, shifting 10 (asks) into the topics column and leaving good-parts blank; 19 topics, 10 asks, 10 good-parts per the retained reader record]** | 10 | 10 |
| email-3 | send-ready 2026-07-13; sent status unverified from this source | Projects hallucinate capability limits, anti-stall doctrine, hub/Project venue split, "one-word dream," doctrine as versioned artifacts | 4 | 6 |
| gen1 wrap-up (final candidate) | send-candidate 2026-07-10; no sent confirmation in this source | large single-session PRs, honesty at 10x parallelism, durable-state recovery, permission-classifier coherence | 10 | 9 |
| 07-18 follow-up | **NOT SENT — free material** | venue-scoped denial (same authority, denied inside a Project, unrestricted outside), two-layer necessity, PR-backlog disposition numbers | 2 | 3 |
| current draft (2026-08-24, rev. 08-25) | unsent, Part 2 1,686 words, this pass's baseline | scale figures, Finding 1 (forgetting/false-done), Finding 2 (append-without-retract), Finding 3 (116 statements caught 0 of 16), outside-vendor review, 5 asks | 6 | 6 |

**Correction the critic caught that this table must carry forward:** email-2
**was sent** (2026-07-12, thread `19f41cd2e5380bb3` — correspondence record
line 101; also confirmed by `superbot docs/eap/NEXT-SESSION-finalize-email.md`).
At least one Fleet A survivor's already-argued verdict rests on treating it
as an unconfirmed draft; that reasoning is void and needs re-checking before
the survivor's novelty claim is trusted (§ 5).

## 5 · What the critics found wrong — read this before drafting anything

Both fan-outs ran a completeness critic; both found real defects in their own
survivors, not just gaps in coverage.

**Fleet A's critic** (full detail in `docs/findings/data/2026-09-02-eap-mail-evidence/fleet-a-full-wf_bda232c1-cf5.json`):

- **Citations were never resolved at source.** Two lenses declined to check
  citations into other repositories on the stated premise that "superbot /
  sim-lab / idea-engine / substrate-kit are not cloned in this session" —
  false: `menno420` is the clone parent and contains all four. The critic
  resolved four disputed citations in seconds. This is the exact failure
  mode A2-7+B6 itself reports.
- **Every corpus line-anchor the critic spot-checked was wrong** — all four
  landed on section headings instead of the quoted text (e.g.
  `sim-lab/control/outbox-archive-2026-07.md:164` is a VERDICT header; the
  actual fabrication is at line 172). Content is real; anchors are
  systematically drifted. **No citation in this report should be trusted to
  the line without a fresh open.**
- **The owner's own stated top priority for this mail is unrepresented.**
  His 2026-09-01 sitting: *"much of the work that was claimed to be complete
  was in fact not complete at all... definitely something to review closely
  and mention in the final EAP mail."* The nearest survivor is B5
  (FALSE-DONE, § 2.6) — corrupted in the payload — and **it is in none of
  the three spines**. Neither is the pass's only ask-role survivor
  (A3-1+A2-1+B13). Five of twelve survivors are used by zero spines.
- **No spine reconciles the estate's own unresolved numbers**: two different
  "116"s, two different "127"s, "67 vs 71 vs 72" doc-routes counts with no
  reconciling date, the draft's "21/21 zero fabrication" sitting beside this
  pass's own Finding 6-equivalent (Fleet A survivor evidence of citations
  that don't resolve) with no clause holding the two apart — the exact
  self-contradiction risk the winning spine (§ 7) was built to patch, but
  only for the two required edits it names, not for the wider set the critic
  found.
- **Nothing was checked against the live Gmail thread** — the correspondence
  record is three weeks stale and the connector was available this session.
- **Missing sources named by the critic, most load-bearing:**
  `docs/findings/2026-09-01-owner-direction.md` (his sitting about this exact
  mail, one day before this pass, unread by any Fleet A reader — see § 1),
  `docs/planning/2026-09-01-estate-structure-proposal/` (the same
  failure-to-mechanism exercise run one day earlier), `docs/findings/2026-09-01-fleet-manager-measured.md`
  (a current-SHA reconciliation of the stale census figures this pass's
  survivors still carry), `docs/findings/2026-08-06-provenance-mechanism-measured.md`
  (the estate's only controlled experiment on same-family review — directly
  bears on survivor #2's whole thesis).

**Fleet B's pilot critic** (full detail in
`docs/findings/data/2026-09-02-eap-mail-evidence/fleet-b-pilot-wf_d0348386-8b6.json`):

- The **decided reader corpus is once-removed from the primary source** for
  3 of the 4 survivors — `docs/findings/night-review-2026-07-10.md` carries
  the primary record nearly verbatim for L02, L03 and L04, and was never in
  the fixed reader list (out of scope to relitigate mid-run, per the night
  brief). Verifiers sometimes opened it anyway (not restricted the way
  readers are) and corrected citations accordingly; this is inconsistent
  across rows, not a rule.
- **No corpus census, no denominator, and no audit trail in what the critic
  itself was shown** — 11 of 15 pilot candidates reached the pilot's critic
  as the single word "refuted" and nothing else (its prompt was fixed for
  the full run, see § 3's script fixes, but not retroactively for the
  pilot). The raw pilot JSON does retain each row's full verifier records —
  this is a gap in what the critic saw and in what this report pulls
  forward, not in what was measured.
- **L07/L08/L12 same-mechanism split verdict** (§ 3) — unresolved (and, per
  the full-run critic below, L08 itself did not survive the larger corpus).

**Fleet B's full-run critic** (full detail in
`docs/findings/data/2026-09-02-eap-mail-evidence/fleet-b-full-wf_fb35b278-362.json`)
— the same corpus-distance defect, now sharper, plus new ones the larger run
exposed:

- **`docs/findings/night-review-2026-07-10.md` is "the single most damaging
  omission"** (the critic's own words) — it is the *original* measured
  source for **both** FD-01 and FD-02, the pass's two strongest survivors,
  and was named as a known gap by the pilot's own CONTRACTS note and still
  not added to the 16-file corpus. Both survivors' "actually" halves rest on
  a document no reader unit opened — only verifiers reached it, inconsistently.
- **Yield collapsed, not scaled: 3 readers → 4 survivors; 16 readers → 3
  survivors.** **[CORRECTED, Codex review, fm #1010]** the executed
  full run read 16 fleet-manager units, not the unexecuted 48-unit combined
  design — the corpus grew ~5.3×, not 16×, and (per the corrected framing
  above) even that comparison isn't clean since the pilot's superbot unit
  was cut, not merely outweighed. What still stands: a larger read produced
  *fewer* absolute survivors in raw terms (4 → 3), and neither
  over-collapsing in the merge (FD-17 originally absorbed 6 sub-rows before
  its own verifier narrowed it to 1; FD-13 absorbs 7) nor tightening in the
  verify lenses is diagnosed as the cause.
- **`docs/traps.md` was never in the READER corpus** (the extraction phase
  that produces claims and corrections) — **CORRECTED (Codex review, fm
  #1010): verifiers did open it directly.** Both verifier prompts instruct
  checking coverage against `docs/traps.md`, and FD-17's holds-lens
  `what_i_opened` lists it by section (TRAP-006 §207ff, TRAP-007 §292ff),
  with its fit-lens `already_covered_by` naming TRAP-006/007 explicitly —
  this is real, verified overlap, not a guess from general knowledge. The
  more precise limitation: no READER read `docs/traps.md` as a corpus item
  to extract from, so any false-done whose only trace is in the trap
  register itself (rather than in a document a reader happened to open)
  would never enter the claims/corrections pool at all — a coverage gap in
  extraction, not in verification. FD-17 also resembles TRAP-008 ("a label
  read as its contents"); FD-01 (CI green over an uncollected third of a
  suite) resembles TRAP-003 and TRAP-004, neither cross-checked. Neither
  pattern-catalogue register
  (`docs/findings/data/2026-08-29-agent-error-patterns.jsonl`, the very
  corpus Fleet A read the same night) was cross-checked either.
- **A single systematic misclassification dominates the 182 orphaned
  corrections** — roughly 40 are dropped as "corrects a wall/status/stale-count,
  not a done-claim," which is schema-correct but means the ledger's
  corrections side is mostly measuring a *different* phenomenon (false
  walls, stale status) than its claims side. Several other orphans look like
  genuine merge misses rather than absences — e.g. one dedupe reason
  literally states the counterpart "is the same statement split onto the
  claims side, so pairing would be circular," which describes a merge
  failure, not a justification.
- **The corpus was DECIDED at 11 fleet-manager files against roughly 30
  EAP-era documents this repository actually holds** — a deliberate,
  documented choice (not relitigated mid-run, per the night brief), but it
  means this ledger is a **sample of the EAP record, not the EAP record**,
  and its survivor count should never be read as exhaustive.
- **Fixed line-count file splits bisect live evidence records — [Codex
  review round 15, confirmed real not hypothetical].** Five of the
  fleet-manager and superbot files over 400 lines were split at fixed line
  counts, not paragraph or section boundaries (`05-eap-false-done-ledger.js`,
  `FM_FILES`/`SB_FILES`). Checked directly against the retained readers: at
  `docs/eap-story.md`'s 300/301 split, the trigger-scheduler incident bullet
  (line 300: "9 dropped send_later one-shots, 2 wedged crons..."; lines
  301-303: the completing "damning line" quote) fell across both readers —
  reader 1 (lines 1-300) extracted nothing for it, reader 2 (lines 301-580)
  extracted only the completing quote, and the measured 9/2 counts never
  entered the claims/corrections pool at all. `eap-retrospective.md:220-221`
  and `launch-readiness-2026-07-10.md:360-361` cut mid-paragraph the same
  way (not individually checked for lost content the way this instance
  was). This is a corpus-coverage gap distinct from the ones above:
  content that was read by no reader, in full, because it straddled a
  boundary chosen by line count rather than structure.

**Third check: Codex review of this PR (fm #1010), multiple rounds, all
findings addressed or explicitly disclosed** (current round/finding tally:
`docs/findings/data/workflows/05-CONTRACTS-night.md` EXTERNAL line — the
one place that live count is kept, per Codex review round 7/8: restating it
here too created a second copy that went stale every single round) — the
drafted version of this report itself had
errors, caught by exactly the external adversarial round the night brief's
DECIDED section requires. Round 1 (10 findings) is summarized above where
this note originally stood; round 2 (10 more, on the round-1 fix commit)
caught residue round 1 missed: FD-17's citation independence overstated —
`docs/eap-story.md` and `docs/launch-readiness-2026-07-10.md` are two
corroborating retellings of one primary source, not two independent paths
(§ 2, FD-01); the "never against `docs/traps.md`" line was itself wrong —
verifiers DID open it directly (FD-17's `what_i_opened` cites it by
section) — the real gap is narrower: no READER read it as a corpus item
(§ 5); the executive summary and § 5 still said "reversed... on the larger
corpus" after the body text was corrected — fixed for consistency; the
judge score table transcribed spine 0 and spine 1's per-judge totals in the
wrong order (§ 7); the "unanimous" graft recommendation was 2 of 3 judges,
not 3 — the owner-rules judge recommends a different reserve ask (§ 7); the
front-matter banner claimed every non-survivor carries a reason, true for
Fleet A, false for Fleet B's 25 — narrowed. Script fixes from round 2: the
negative-coverage regex missed `"n/a — ..."`, a form the actual full-run
output used; the critic's `READ` list used the model-authored `source`
field, which a split reader can render as a bare path missing its range —
switched to the deterministic unit labels; the merge stage's per-group row
cap (25) was tighter than its input size (`CHUNK`=40), so a group with more
than 25 genuine matches would silently lose the excess — the cap now equals
`CHUNK`. Not fixed, disclosed: the dedupe stage's silent loss of rows
beyond its own output cap (150 merged → at most 45 returned) is logged but
not batched like the merge stage — next-session work.

**Round 3 (8 more findings, on the round-2 fix commit):** the session card
still called both critics "reproduced in full" after the README's wording
was already softened — fixed there too; the CONTRACTS sheet's AGGREGATE
line for Fleet B described the pre-round-1 `dies()` expression and fixture
tally, no longer what the script asserts — updated; two more "unanimous"/
"unauditable beyond refuted" claims survived from the pre-round-2 wording
in §§ 2 and § 3's "25 non-survivors" line — both corrected to distinguish
"not pulled into this report" from "absent from the raw output" (which the
raw output is not: every non-survivor retains full verifier records,
confirmed by direct check of the committed pilot JSON). Two real defects:
**the merge stage's `filter(Boolean)` silently dropped an entire failed
group's corrections** (up to `CHUNK`=40 at a time) with no log, no
`orphaned_corrections` entry, and no critic visibility — fixed to log
failed groups and pass their raw corrections to the critic as
`unprocessedCorrections` (**[CORRECTED, round 4]** checked directly against
this run's own numbers rather than assumed: `merged` (150) + `orphaned`
(182) = 332 = `corrections` exactly, so this actual run had zero merge-group
failures — the fix guards a real risk the code had, not a defect this run
hit); **L02's claim citation pointed at this
session's `/tmp/eap-night/...` scratch fetch**, a path that will not
survive the container — replaced with the pinned `superbot:...@5e3a667`
repository path (§ 3). **Disclosed, not fixed:** the survival rule requires
BOTH lenses to populate `already_covered_by` before killing a row as
already-covered, but only the fit-lens prompt searches broadly for
coverage — the holds-lens prompt checks only two named sources. FD-02
survives as a "fresh finding" even though its own fit-lens calls it
"already-known plumbing" (naming `docs/playbook.md` R22), because the
holds-lens left the field empty. Recorded in the CONTRACTS sheet; a real
fix needs symmetric lens scope or a single aggregated coverage verdict.

**Round 5** (1 finding): this closing note's own round tally had already
gone stale by the push that fixed round 4 — corrected, and corrected again
after round 5 for the same reason (a tally naming "N rounds" is stale the
moment the commit fixing round N's own finding is what round N+1 reviews;
readers should treat this count as accurate as of this exact head, not as
self-maintaining). **Round 6** (3 findings): the front-matter's
`corrected_claim`-only guarantee overstated itself — B5's own
`corrected_claim` is corrupted (§ 2.6) and FD-02's paragraph synthesizes
both lenses rather than quoting one, so the banner now describes both
paths; **a real, verified defect** — the reader prompt never bounded CLAIMS
to the EAP fortnight, and checking this run's own claim pool directly found
30 of 505 claims (5.9%) dated 2026-07-22 or later, consuming capacity in
the capped merge/verify stages — reader prompt fixed for future runs;
checked directly (not assumed) that all 3 of this run's actual survivors
have in-window `claimed_when` dates, so the pool dilution did not
contaminate the survivor set, though it may have silently displaced an
in-window candidate — unknowable without a re-run (§ 3, CONTRACTS sheet).

**Round 7** (6 findings): the round-6 date fix only bounded the upper end
of the EAP window; the run's own claim pool already had 3 pre-window June
claims, so the reader prompt now bounds both 07-07 and 07-21 (CONTRACTS
sheet). **A real correction to this report's own earlier correction:** § 2
finding #1's "10 of 20" figure was flagged **[UNFIXED]** as if the
payload's own verifier disproved it — checked directly against the raw
verdicts, the holds-lens verifier independently recounted and got **10**
("the candidate's 10 is right"), the same as the original census reader;
only the fit-lens verifier's separate recount got 9. This is an unresolved
2-of-3 split, not a clean correction, and the finding above now says so.
Index/wording sync: `docs/findings/README.md`'s row for this report is
changed to describe review rounds without a hardcoded number (a specific
count in a second file goes stale the instant the next round lands — this
closing note, updated each round in place, is the one place a round count
belongs); the CONTRACTS sheet's RETAIN line dropped an overpromised
follow-up query ("which claims were never refuted") the retained output
cannot actually answer. Disclosed, not fixed: the completeness critic sees
only the ≤30 claims attached to verified rows, not the full 505-claim pool,
so it cannot check an orphaned correction against a claim that was matched
then cut by the ranking cap, or against a claim never selected at all.

## 6 · The owner's words on this mail, collected (5 readers, 25 quotes kept)

- **`OWNER`**, verbatim including the source's own typo — **[CORRECTED,
  Codex review round 12]** this report previously silently normalized
  "whih" to "which" and added a closing period; restored to the source
  exactly: *"About the mail, that really is something to work on soon, and
  I think that all the audits I'm doing right now will provide valuable
  information, not only about the EAP itself but generally about how
  agents work, whih would be a valuable addition to the mail"*
  (2026-08-28, `docs/findings/2026-08-28-od24-sitting-answers.md:642-645`)
- **`OWNER`** — *"I noticed that much of the work that was claimed to be
  complete was in fact not complete at all. Which is definitely something
  to review closely and mention in the final EAP mail, which I still
  haven't send."* (2026-09-01, the direct mandate for Fleet B —
  **[CORRECTED, Codex review round 14]** this report previously said the
  quote had no in-repo citation and pointed only at this session's own
  originating brief; it is in fact already reproduced verbatim at
  `docs/findings/2026-09-01-owner-direction.md:73-75`, present at the
  audited base SHA)
- **`DERIVED`** — *"I scaled it until I found the wall; the wall is human
  review, not agent capability; and that tells you exactly how close
  self-running AI actually is."* (2026-07-21, the offered thesis line —
  `docs/owner-reflection-2026-07-21.md:189-191`). **[CORRECTED, Codex
  review round 14: mislabeled OWNER in round 13.]** The retained
  `owner_words.rules_for_the_mail` record and the source document's own
  §-opening line (`docs/owner-reflection-2026-07-21.md:163-165`, "Guidance
  distilled from the whole email exchange") both flag this as distilled
  guidance for a future drafting session, not the owner's own verbatim
  wording — first-person phrasing notwithstanding.
- **`DERIVED`** — *"less a coding tool, more a way for someone like me to
  run a software project by describing it"* (2026-07-21, the offered
  throughline — `docs/owner-reflection-2026-07-21.md:191-193`). Same
  correction and same source caveat as the thesis line above.
- **`DERIVED` — rules for the mail, distilled** (Codex review round 12:
  the raw record itself flags several of these as distilled guidance and
  at least one reading as "not itself a verbatim rule" — labeled here so
  it isn't mistaken for settled owner instruction; the owner can replace
  any of it): it is owner-reserved (only he sends it);
  don't re-argue permission/coordinator-trust material already covered
  exhaustively; net-new content in priority order (capability feedback,
  a week-over-week scorecard, the "what I had to build myself" teardown,
  usage-economics, a standing offer to run structured probes, the
  consolidation number); form should read as a fan's critique, tight not
  dense.
- **Length is explicitly unsettled** — his 2026-08-28 widening reopened it;
  no source since fixes a word count for the combined mail.
- Agent roster: only `docs/intent.md` § 7 (2026-08-08, self-flagged
  unbenchmarked except the Codex row) states one — Claude is "the main
  agent," holding the widest credentials, preferred for documentation work.

## 7 · The three spines and their judge scores (all three judges agree on the winner)

All three lenses (product-team, evidence, owner-rules) independently scored
**spine index 2** highest: **18/20, 19/20, 19/20** (vs. spine 0's 16/14/17 and
spine 1's 17/16/13, judge-1/judge-2/judge-3 order — corrected per judge
transcript, Codex review fm #1010: no judge gave spine 1 an 18).

**Winner — "Part 2 Addendum — General Agent-Behavior Findings (≤450 words) +
Required Part 2 Patches."** Keeps the current 1,686-word Part 2 intact, adds
one ≤450-word addendum (Findings 4-6, 3 new asks, a sources block) plus two
required one-clause patches to existing draft sentences so they don't read as
self-contradicting once the addendum ships beside them. Full structure,
word budgets, and both required patches (verbatim original + minimal patch
text) are in the raw JSON — reproduced in full because they are close to
send-ready text:
`docs/findings/data/2026-09-02-eap-mail-evidence/fleet-a-full-wf_bda232c1-cf5.json`
→ `result.spines[2]`.

**⚠ DO NOT COPY THIS SPINE VERBATIM — [Codex review round 14]:** the spine
text (both its finding-6 body and its patch wording) still carries the
uncorrected A1-6 framing this report fixes in § 2 above — "a disjoint
27-card sample found about one in nine marked sections held no real
content," treating the full-161-card zero-empty-review-sections result and
the disjoint 27-card ~1-in-9-empty-*idea-slot* sample as one measurement.
The spine JSON is retained verbatim as the agent produced it and is not
edited here; whoever drafts from it must patch this exact clause to match
§ 2's corrected wording before it reaches the mail, or it reintroduces the
error this report exists to catch.

**What it deliberately drops, and why** (its own field, not this report's
gloss): the self-review survival-rule finding (#2 above) — arithmetic needs a
fix first and a second collision-patch the budget can't afford; the
null-vs-untested-check finding (#3) — same shape as the draft's existing
Finding 2, shares an incident with the draft's Finding 3; the FALSE-DONE
substitution taxonomy (B5) — the owner's own stated priority (§ 6), held out
for a *future* revision on the reasoning that it "sharpens" an existing ask,
which is exactly the gap the critic (§ 5) flags as unaddressed.

**Two of three judges' top graft recommendation — CORRECTED (Codex review,
fm #1010): not unanimous.** The product-lens and evidence-lens judges both
recommend adding the null-result-vs-check-that-never-ran finding (#3 above)
as a fourth addendum item if the owner will spend ~100 more words — the
evidence-lens judge calls it "the single most product-actionable item in
any of the three spines... a concrete tool-result contract change, not a
process wish." **The owner-rules judge recommends a different reserve
fourth ask instead** — the measured concurrency leg (fan-out concurrency
held at 4, median 4/mean 3.43 across 4,097 samples, against a documented
10–16), calling it "clean, product-legible, absent from the four July mails
and from the current draft." Both are live options if the owner grants more
words; this report originally claimed all three judges agreed, which they
did not.

**Pre-send mechanics warnings, independent of spine choice —
**[CORRECTED, Codex review round 11]** not unanimous across all three:**
all three judges warn to confirm every linked document is merged to `main`
before sending (the 2026-08-29 audit and 2026-09-01 documents were on a
feature branch, not `main`, as of the judging pass) and to re-run every
stale count (the routes figure, 67→71→72 across three dates) the day of
sending, dated that day. The reproducibility caveat (owner's own
credentials, private repos included, method reproducible, inputs not),
stated once for the whole mail rather than per finding, is raised by the
**product and owner-rules judges only** — the evidence judge does not
request it.

## 8 · Contract sheets (quoted, not summarized)

Both fleets' fleet-preflight sheets are committed in full beside their
scripts and are the source of every SIZE/PILOT/CORPUS number in this report:
`docs/findings/data/workflows/05-CONTRACTS-night.md` (this run) and
`docs/findings/data/workflows/04-CONTRACTS.md` (the 2026-09-01 pilot Fleet A
reused unchanged).

## 9 · Raw data retained

- `docs/findings/data/2026-09-02-eap-mail-evidence/fleet-a-full-wf_bda232c1-cf5.json`
  — Fleet A's complete return value (readers, patterns, owner words, ranked
  candidates, all 16 verify pairs, all 3 spines, all 3 judges, the critic).
- `docs/findings/data/2026-09-02-eap-mail-evidence/fleet-b-pilot-wf_d0348386-8b6.json`
  — Fleet B's pilot return value.
- `docs/findings/data/2026-09-02-eap-mail-evidence/fleet-b-full-wf_fb35b278-362.json`
  — Fleet B's full scoped run (16 fleet-manager-only reader units).

## 10 · What tomorrow's session should do with this

> **Owner, 2026-09-02 (the review sitting), on the sentence below:** *"I
> would like a proper draft created which I can read and edit."* A session
> drafts the mail from this report; he reads, edits and sends. The rest of
> this section is that draft's precondition list, unchanged. Record:
> [`2026-09-02-owner-direction.md`](2026-09-02-owner-direction.md) § 5b.

This report is evidence, not a drafted mail — per the night brief and the
owner's own reservation, only he writes and sends Part 1, and no session
drafts Part 2 without him present. The next session should: (1) resolve the
flagged items in § 2 before quoting any of them — **[UNVERIFIED]** (#4),
**[PROVENANCE FLAG]** (#7), **[WORDING RISK]** (#11) and the unresolved
9-vs-10 split in #1; the one **[UNFIXED]** citation (#8) was resolved at
the flip; (2) **read
`docs/findings/night-review-2026-07-10.md` before using FD-01 or FD-02 in
the mail** — both critics independently name it as the original measured
source neither fan-out's readers opened, and its addition may also give
**L02's underlying claim (venture-lab's Stripe false-green)** a fresh claim
source to enter the pool through. **Read this precisely, per round 15's
correction (round 14's own diagnosis was itself wrong): L02's problem was
never a missing corpus, and it was not a reader inconsistency either** —
its correction sits in `docs/eap-story.md`, a fleet-manager file read in
both runs, and **both runs' readers agreed**: neither extracted a matching
claim (checked directly against `result.readers[0].claims` in the
retained pilot JSON). **The actual fault is in the merge stage**: the
pilot's merge invented a claim from the orphaned correction alone, which
its own contract explicitly forbids ("do not manufacture" a row,
`05-eap-false-done-ledger.js:182`); the full run's merge correctly left
it unmatched. Adding night-review as a source may supply an independent
claim, but the more direct fix is enforcing the merge stage's own
no-manufacture rule (or accepting the row only ever existed via a
contract violation); do not re-add the superbot lane expecting that alone
to recover L02 — it never depended on
it. **L08** (self-arming routines), unlike L02, genuinely did draw its
refuted status from the cut superbot lane
(`anthropic-email-2-draft-2026-07-11.md`) and may be settled by restoring
that source; (3)
decide, with the owner, whether the false-done
substitution taxonomy (B5, Fleet A) or the false-done ledger itself (Fleet
B, his own directly-stated priority for this mail) gets a slot in the mail
— neither is in any of Fleet A's three spines; (4) fill in the 25 non-survivor
reasons Fleet B's full run left as bare "refuted" (pull from each verifier's
`discrepancies` field, per the CONTRACTS sheet's own pilot note); (5)
re-verify every citation this report carries forward — Fleet A's critic
spot-check found a 4-for-4 citation line-anchor drift rate, and nothing here
should be trusted to the line without a fresh open; (6) confirm every linked
document is on `main`, and re-run every stale count, on the day of sending.
