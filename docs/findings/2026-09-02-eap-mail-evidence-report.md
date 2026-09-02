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
  the two corpora are **not nested** (the full run cut the one superbot
  reader both depended on), so this is not clean evidence of scaling or
  verifier instability either way. Read § 3 and § 5 together before
  trusting any count here.
- **CUT: the 32 superbot `docs/eap` reader units** (of Fleet B's full 48-unit
  design) — dropped **before** any fleet-manager-side cut, exactly as the
  night brief's SIZE rule specifies ("drop Fleet B's satellite-heavy readers
  before dropping its fleet-manager readers"). The pilot's 1 superbot reader
  is the only superbot-side evidence in this pass; nothing else from that
  corpus was read tonight.
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

Each row is the surviving candidate's **id**, its **`corrected_claim`** as the
first verifier that supplied one wrote it (never the merge's original
wording), scope, and citations. Where the critic (§ 5) caught an error the
verifier itself did not fix in the payload, that is flagged inline as
**[UNFIXED]** — these numbers must be corrected before anything here goes
into a mail.

1. **A1-5+B10+B11** (finding, both) — *The delivery tier a rule sits in, not
   its wording, predicts whether agents follow it: where a rule is a
   required, exit-affecting check on a literal marker, compliance is
   near-total (335/335, 302/302, 503/503 session cards, three repositories);
   where the same class of rule is advisory prose that cannot fail a build,
   the same audit found decay (23 stale claim files untouched in one
   repository; a review protocol last run 46 days before its own census).*
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
   nothing.* **[UNFIXED]** the payload still states "7.0% of 925 verdicts,"
   which the verifier itself computed as 60/925 = **6.5%**, not 7.0% — fix
   before send. Also carries a citation the same verifier found supports
   none of its claims (`2026-08-24-e1-source-sweep.md:284-288`) and a "load-
   bearing correction" the verifier showed was already applied in the
   current draft on 2026-08-25 — this row is stale in two more places than
   its own corrected_claim admits.
3. **A1-7+A2-6+B2** (finding, both) — *A null or clean result is
   indistinguishable, in what an agent sees, from a check that never ran,
   never covered the case, or never executed as written — and the same
   collapse reaches the human reader.* Instances: a term-less 26-repo search
   returning 0 everywhere, caught only because a known-good control also
   came back empty; the CI gate collecting 73 of 121 tests with 48 invisible
   (superbot-games, 2026-07-10); the space-stripping phrase regex that ran
   under 986 agents and moved the corpus +127 sections once fixed
   (2026-08-29). Dropped from all three spines for budget, not weakness —
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
   not contain what is claimed (repo_count 10).* **[UNFIXED]** still carries
   a citation (`idea-engine docs/audits/eap-project-audit-2026-07-14.md:76`)
   its own verifier flagged as not resolving — the finding about unresolved
   references itself ships one.
9. **A2-4+A2-5** (finding, general) — *Delivering the rule at the moment of
   action has a measured ceiling and two silent failure modes: of 13 errors
   from one session scored against 116 committed statements, the statements
   caught 0.* Already substantially in the current draft (Finding 3);
   this row extends it with the ceiling/failure-mode framing.
10. **A1-6** (finding, both) — *A merge-blocking check that verifies a
    marker's presence, not its substance, reached full compliance while
    roughly one in nine marked sections carried no actual content* (161
    session cards at ~100% marker presence; a disjoint 27-card sample found
    ~1-in-9 empty underneath). Clean, well-cited, no critic flag.
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
    say 'I have this one.'"* The reachability/provenance material (74
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
- **L03** — superbot-games PR #16 asserted "substrate-gate now runs the
  suite"; the gate collected 73 of 121 tests (48 exploration tests
  invisible), and the session card's own arithmetic (62+11=73) papered over
  the gap. Graded "FALSE as stated" the same night; fixed the next day (PR
  #24), floor later raised 121→147→230.
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
not hold up); 0 already-covered.

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

- **FD-01** (merges 4 sub-rows) — superbot-games PR #16 asserted
  "substrate-gate now runs the suite," and the lane's close-out heartbeats
  reported "mining gen-1 complete green" on that gate. Actually: the gate
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
  finding, now also carrying the residue the pilot missed: even after the
  owner's API-verified flip, the repo's status file carried no
  `visibility: private — verified <ts>` line, so a standing guard had to be
  appended separately (ORDER 003, `a76ada7`).
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
tests inject synthetic events authored from memory," each dropped with the
reason "no earlier done-claim found in this corpus"). Both L02 and L08
drew their pilot-survival evidence from the one superbot reader unit the
pilot happened to read — the exact unit the full run's `skipSatellite: true`
cut. The two fleet-manager-sourced pilot survivors (L03 → FD-01, L04 →
FD-02) both held. The honest statement is narrower than "reversed at
scale": **removing the superbot lane removed the evidence those two rows
depended on**, which this pass cannot distinguish
from genuine verifier instability without a run that reads the same corpus
twice. Neither this report nor the underlying pass diagnoses which it is —
say so, don't imply causation either way.

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
| email-2 (scale-up) | **SENT** 2026-07-12 13:24:40Z (thread `19f41cd2e5380bb3`) — Fleet A's own critic found one candidate's overlap verdict treated this as an unconfirmed draft; that verdict is void, see § 5 | 10 | 10 |
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

- *"About the mail, that really is something to work on soon, and I think
  that all the audits I'm doing right now will provide valuable information,
  not only about the EAP itself but generally about how agents work, which
  would be a valuable addition to the mail."* (2026-08-28)
- *"I noticed that much of the work that was claimed to be complete was in
  fact not complete at all. Which is definitely something to review closely
  and mention in the final EAP mail, which I still haven't send."*
  (2026-09-01 — the direct mandate for Fleet B)
- *"I scaled it until I found the wall; the wall is human review, not agent
  capability; and that tells you exactly how close self-running AI actually
  is."* (2026-07-21 — the offered thesis line)
- *"less a coding tool, more a way for someone like me to run a software
  project by describing it"* (2026-07-21 — the offered throughline)
- **Rules for the mail, distilled:** it is owner-reserved (only he sends it);
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

**Every judge's pre-send mechanics warning, independent of spine choice:**
confirm every linked document is merged to `main` before sending (the
2026-08-29 audit and 2026-09-01 documents were on a feature branch, not
`main`, as of the judging pass — verify this is fixed before send); re-run
every stale count (the routes figure, 67→71→72 across three dates) the day
of sending and date it that day; state the reproducibility caveat (owner's
own credentials, private repos included, method reproducible, inputs not)
once for the whole mail rather than per finding.

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

This report is evidence, not a drafted mail — per the night brief and the
owner's own reservation, only he writes and sends Part 1, and no session
drafts Part 2 without him present. The next session should: (1) fix the
**[UNFIXED]** items in § 2 before quoting any of them; (2) **read
`docs/findings/night-review-2026-07-10.md` before using FD-01 or FD-02 in
the mail** — both critics independently name it as the original measured
source neither fan-out's readers opened, and its addition may also let
**L02's underlying claim (venture-lab's Stripe false-green) finally enter
the claim pool** — it never did in the full run, surviving only as
unmatched orphaned corrections — and may settle **L08's** (self-arming
routines) refuted status, which came from the same cut superbot lane; (3)
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
