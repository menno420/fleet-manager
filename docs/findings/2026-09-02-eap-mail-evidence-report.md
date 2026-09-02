# EAP mail evidence report — night fleet, 2026-09-01/02

> **Status:** `reference` · produced by two verified, novelty-checked fan-outs
> run overnight (fleet-preflight sheet: `docs/findings/data/workflows/05-CONTRACTS-night.md`,
> scripts beside it) while the owner slept. Every finding below is quoted from
> a **verifier's `corrected_claim`**, never from the raw candidate or the merge
> stage's wording, per the night brief's own rule. Non-survivors are listed with
> their reason, not silently dropped. **Read the "What was not read, and what
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
  11 named EAP docs split over 400 lines) — see § 3 for its result, filled
  after this document's first commit once the run lands.
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
· prior mails from superbot@5e3a667 docs/eap: 7 files ≈160 KB (SHA unchanged
from the 2026-09-01 pilot).
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
   **[UNFIXED, per Fleet A's critic]** the payload still reads "10 of 20 rows
   report no `.claude/` directory" after its own verifier could reproduce
   only 9 on two independent regex passes and never fixed the number.
   **[CORRECTION, per the owner's 2026-09-01 sitting, unread by this
   reader]**: the "1 of 20 repos has hooks" framing is not a coverage gap —
   the owner states it is **deliberate** ([D-0038]): fleet-manager is always
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
   the judge panel's top-scored graft recommendation, unanimous across all
   three judges.
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
   nothing implements.* **[DATA DEFECT, per the critic]**: this row's
   surviving `claim` field is not the original candidate text — it is
   verifier meta-commentary ("Holds as written; the numbers 9, 7, 5 and 2 are
   exact repo_counts...") left in the payload where the claim should be nothing
   downstream can check what actually survived. **Do not quote this row's
   `claim` field verbatim; the pattern it describes is real (repo_counts 9,
   7, 5, 2 from the 284-pattern catalogue) but its wording must be
   reconstructed from the shard data before use.** This is also the row
   closest to the owner's own stated priority for this mail (§ 6) and it is
   in **none of the three spines** — see § 5.
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
12. **A3-1+A2-1+B13** (ask, both) — *A way for a session to see the other
    sessions — what they did, what they are touching now, and how many can
    actually run — because none of the three is currently retrievable.* The
    pass's only surviving **ask**-role candidate, and it is in **none of the
    three spines** (§ 5).

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
  ORDER 003. Citations (verifier-corrected): claim —
  `/tmp/eap-night/superbot-eap/fleet-overnight-review-2026-07-10.md:33,105`;
  found — `docs/findings/night-review-2026-07-10.md:31-33,118-140` (a file
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

**Full run (16 fleet-manager-only reader units, `skipSatellite: true`) —**
launched at 00:23Z after Fleet A landed; result not yet in at first commit of
this report. **[FILL AFTER NOTIFICATION — see run id in the commit that adds
this section's numbers.]**

## 4 · Prior-mail overlap map (6 readers, all 4 July mails + the 2 unsent drafts + the current draft)

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
  self-contradiction risk the winning spine (§ 6) was built to patch, but
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
- **No corpus census, no denominator, and no audit trail for refutations** —
  11 of 15 pilot candidates vanish with the single word "refuted" and
  nothing else; this is itself an instance of the append-without-retract
  pattern the estate's own audits name.
- **L07/L08/L12 same-mechanism split verdict** (§ 3) — unresolved.

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
**spine index 2** highest: **18/20, 19/20, 19/20** (vs. spine 0's 16/17/14 and
spine 1's 17/18/13).

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

**All three judges' unanimous top graft recommendation** (from the two
non-winning spines, into the winner): add the null-result-vs-check-that-
never-ran finding (#3 above) as a fourth addendum item if the owner will
spend ~100 more words — called "the single most product-actionable item in
any of the three spines... a concrete tool-result contract change, not a
process wish."

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
- `docs/findings/data/2026-09-02-eap-mail-evidence/fleet-b-full-*.json` —
  Fleet B's full scoped run, added once it lands.

## 10 · What tomorrow's session should do with this

This report is evidence, not a drafted mail — per the night brief and the
owner's own reservation, only he writes and sends Part 1, and no session
drafts Part 2 without him present. The next session should: (1) fix the
**[UNFIXED]** items in § 2 before quoting any of them; (2) resolve the
L07/L08/L12 contradiction in § 3 and decide whether Fleet B's full run
changes the ledger's survivor set; (3) decide, with the owner, whether B5
(the false-done substitution taxonomy — his own stated priority) gets a
fourth addendum slot or replaces one of the winning spine's three; (4)
re-verify every citation this report carries forward — the critic's spot
check found a 4-for-4 line-anchor drift rate, and nothing here should be
trusted to the line without a fresh open; (5) confirm every linked document
is on `main`, and re-run every stale count, on the day of sending.
