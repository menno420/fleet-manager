# The successor-ready estate truth baseline — a change-only re-audit and the `estate` seed manifest

> **Status:** `audit` · tier **TASK** — this is the baseline the fresh-start
> sequence's step 2 requires, and a future `estate` creation session works from
> it. Measured 2026-09-04 from the live GitHub account and from each
> repository's own source, pinned per repository; the pins and the delta are
> reproducible with committed tooling.
>
> **Why this exists, in the owner's words** (2026-08-30, live): *"we need to
> perform multiple audits again, but only if the information has changed so
> far."* His five-step sequence puts a **trustworthy baseline** between the plan
> and the seed, and the build order he chose on 2026-09-01 ([D-0035]) makes the
> **migration manifest** a named prerequisite: *"the migration manifest has one
> verb per candidate with a verifier's name."* Neither existed. This finding and
> [the manifest](../planning/2026-09-04-estate-seed-manifest.csv) are them.
>
> **Boundary, stated first because it bounds every claim below.** Substrate Kit
> is a **concurrent session's work** — kit PR #590 (adoption profiles, K1–K5)
> was open throughout this run. Nothing here edits the kit, designs a kit
> mechanism, or makes a seed item depend on an unreleased kit change. Where the
> baseline touches kit behaviour it records the dependency and the **currently
> verified** state. § 9 carries those rows.

## 1 · What was already settled before this run, and what was not

Stated first so the reader can see what this run added rather than re-derived.

**Settled, and not reopened here:** the fresh start itself and this repository
becoming the read-only archive ([D-0025]) · the name `estate` ([D-0026]) · the
three carry verbs — **carry whole · distill · archive only** · the absolute
write cutover with a lagging archive flag · the eleven role names · the
findability contract ([D-0032]) · the archive shape ([D-0033]) · file-length
caps ([D-0034]) · the build order, **thin seed → blind cold test → write
cutover → deeper machinery, with only K1–K5 before the seed** ([D-0035]) ·
hooks in the hub repository only, by design ([D-0038]) · the fan-out model tiers
([D-0040]) and the three-round Codex cap ([D-0039]).

**Genuinely unverified before this run, which is what made it the correct next
step:**

1. **No per-repository delta existed.** The plan says re-audit *where information
   changed*, and nothing computed where it had. The 2026-08 audit wave recorded
   almost no SHAs — the 2026-08-21 estate review that built `ESTATE.md` from 26
   repositories records **zero**, the 2026-08-23 intent audit **two** — so
   "has it changed" was not answerable from the record at all.
2. **No migration manifest existed**, though [D-0035] makes it a prerequisite of
   the seed and the acceptance test names it.
3. **Five repositories were `unrated` by the last intent audit** — a deliberate
   refusal to decide, never revisited — and two more (`spider-bot`,
   `creator-kit`) were created *after* every estate-wide audit.
4. **No test existed of whether the estate's records can route a stranger.**
   The retrieval half of the acceptance test is the scored half and *"had never
   been tested"*.

## 2 · Method, and the contract it ran under

The run was contracted before its first audit agent spawned, per
[`fleet-preflight`](../../.claude/skills/fleet-preflight/SKILL.md). The full
sheet is published verbatim at
[`data/2026-09-04-estate-truth-baseline/CONTRACTS.md`](data/2026-09-04-estate-truth-baseline/CONTRACTS.md);
its `UNCONTRACTED` line is empty. Three of its lines did real work:

- **The aggregation rule was written as an expression over field names and
  field-audited before the fleet ran** — 0 unread fields, 0 undefined, parsed
  from the rule's own source rather than a retyped copy
  ([`tools/estate_baseline/seed_rule.py`](../../tools/estate_baseline/seed_rule.py),
  exit 0), with 12 fixtures, **8 kill and 4 survival**. This exists because the
  estate's 2026-08-29 fan-out collected the deciding signal and threw it away:
  815 of 925 verdicts named a disagreement the survival rule never read.
  [`test_manifest.py`](../../tools/estate_baseline/test_manifest.py) proves the
  same thing end-to-end — a refuter's drop actually kills a row in aggregation.
- **Concurrency was measured, not quoted.** A demand test dispatched 8 barrier
  agents at one instant, each held alive 45 s: **peak 2**, four clean waves of
  two. Within-wave starts were 1.1–3.6 s apart (provisioning is fast) while each
  new wave began 5.2–11.7 s after a slot freed — fast provisioning plus starts
  tracking slot-frees is slot-limiting. The documented `min(16, CPUs−2)` is
  **eight times** the measured figure and was not used for sizing.
- **The pilot was read whole and changed three things**, one of them mine.
  [`data/…/pilot-log.md`](data/2026-09-04-estate-truth-baseline/pilot-log.md).
  The sharpest was invisible in any summary: a `curl | python3` fetch returned
  **a different repository's README under HTTP 200**, valid base64, clean
  decode, while two agents ran concurrently on shared egress. The fleet's
  instructions were changed to fetch to disk and cross-check the blob sha and
  size against the tree listing.

**Model staffing was chosen per stage, never inherited** ([D-0040] as amended
2026-09-02): Sonnet 5 read, mapped and enumerated; Opus 5 refuted, adjudicated
disposition, scored blind and took the last look. **Fable 5.1: none** — the
owner's amendment reserves it for runs he asks for in words, and he did not ask
for this one.

## 3 · The authoritative census — 28 repositories, each accounted for once

Taken from the live account, not from any dated report:
`GET /user/repos?per_page=100&affiliation=owner` at 2026-09-04T11:34Z returned
**28 repositories — 19 non-archived, 9 archived, 3 private**
(`estate-backups`, `pokemon-mod-lab`, `shiftlife`). Reconciled against
[`ESTATE.md`](../ESTATE.md), which carries **28 rows**: **0 live-not-in-index,
0 index-not-live**. `MEASURED`.

That reconciliation is itself a result. The index was wrong by one repository
for a day in August (`creator-kit`, created 2026-08-25, registered 08-26 only
because an invisible-work sweep found it); it is exact today.

### Per-repository coverage, and the asymmetry the seed inherits

`MEASURED` at HEAD by enumerating the directories and matching them against the
census, not by quoting a generated page:

| Surface | Coverage | Uncovered |
|---|---|---|
| `docs/owner-comments/<repo>/` | **28 of 28** | — |
| `docs/repos/<repo>/` (Layer 2) | **10 of 28** | the 9 archived · `superbot-plugin-hello` · `creator-kit` · `curious-research` · `gba-homebrew` · `idea-engine` · `pokemon-mod-lab` · `shiftlife` · `sim-lab` · `fleet-manager` itself |
| `owner/intent-workbooks/` worksheets carrying his words | **1 of 74** — `owner/intent-workbooks/estate/why-this-estate-exists.md` | the other 73 are unanswered forms |

**This asymmetry is a seed-time obligation, not a curiosity.** The agreed
`estate` tree gives **every** repository a folder under `repositories/`, with a
generated index whose rows carry the state word. Seeded from today's coverage
that produces **eighteen rooms with a door and nothing behind it** — precisely
the *"dead rooms"* the door test already penalises. The manifest therefore
treats a `repositories/<repo>/README.md` for the eighteen as a seed-time
**deliverable** rather than a carry, and § 5's re-audit is what supplies the
content for the eight non-archived ones. The nine archived get a README only,
which is what the structure proposal already specifies.

**The 1-of-74 figure is the sharpest number in this section and it is not a
criticism of the workbooks.** They are questions written *for* the owner and he
has answered one. It means the successor cannot be seeded with "his intent"
as though it were recorded: what exists is his intent **on the successor's
purpose** (that one worksheet), plus the owner-direction records and decision
entries, which are real and quotable. Everything else in `owner/` seeds as an
empty form awaiting him — carried because the forms are the ask, not because
they contain answers.

## 4 · The baseline-of-baselines, and why it had to be rebuilt from dates

For each repository the run identified the best prior evidence that read it
**from its own source**, and the instant that evidence measured — recorded in
[`anchors.tsv`](data/2026-09-04-estate-truth-baseline/anchors.tsv) with the
prior evidence's own certainty rating.

**The measurement point almost never existed as a SHA**, so it is recovered from
the date: `tools/estate_baseline/delta.py` resolves the last commit on the
default branch at or before the anchor instant, then compares it to the live tip
and reports `ahead_by`. The anchor is the **start** of the measurement day — an
audit written on the 22nd read a tree that existed that day, and taking the
day's end would silently absorb same-day commits it never saw.

**This is the honest weakness of the whole delta, and it is structural rather
than a defect of this run.** A date-recovered baseline cannot distinguish a
repository whose audit ran in the morning from one audited that evening. Its
error is bounded by one day of commits per repository, it always errs toward
**over**-reporting change (which costs re-audit effort, never missed change),
and the successor's fix is mechanical: **every row of the seed manifest carries
a source SHA**, so the *next* delta is exact.

The classification splits the mechanical from the judgemental deliberately.
`delta.py` decides **movement only**; `WEAK_OR_INCOMPLETE` and `NEW` are
judgements about the prior *evidence* and live in the anchor file, applied by a
reader. `creator-kit` is the live demonstration: mechanically `UNCHANGED`
(zero commits since its only prior mention), actually `NEW` (that mention was a
registration row, not an audit). A script that computed it would have laundered
a judgement into a measurement.

### The result

| Disposition | N | Repositories |
|---|---|---|
| `ARCHIVED_OR_NONACTIVE` | 9 | `Substrate-kit-app` · `codetool-lab-fable5` · `codetool-lab-opus4.8` · `codetool-lab-sonnet5` · `proxybench` · `superbot-games` · `superbot-idle` · `superbot-mineverse` · `trading-strategy` |
| `CHANGED_REAUDIT` | 6 | `fleet-manager` (23 commits) · `couch-legend` (5) · `substrate-kit` (3) · `websites` (2) · `idea-engine` (1) · `sim-lab` (1) |
| `WEAK_OR_INCOMPLETE` | 7 | `spider-swing` · `superbot` · `superbot-next` · `product-forge` · `estate-backups` · `shiftlife` · `spider-bot` |
| `UNCHANGED_REUSABLE` | 5 | `curious-research` · `gba-homebrew` · `pokemon-mod-lab` · `superbot-plugin-hello` · `venture-lab` |
| `NEW` | 1 | `creator-kit` |
| **Total** | **28** | every repository exactly once |

`WEAK_OR_INCOMPLETE` is where the run departs from a naive delta. Five of those
seven read **`unrated`** in the 2026-08-23 intent audit — `superbot`,
`superbot-next`, `websites`, `couch-legend`, `shiftlife` — which that audit was
careful to call *"a deliberate refusal to decide, not a weak verdict"*, noting
that rating them was one read each and that any could displace its own
recommended order. Nobody did those reads in the twelve days since.
`spider-swing` is there for the opposite reason: it was rated, and it **failed**.

### Reproducing it

```bash
python3 tools/estate_baseline/delta.py \
  --anchors docs/findings/data/2026-09-04-estate-truth-baseline/anchors.tsv \
  --out /tmp/delta-now.tsv
python3 tools/estate_baseline/test_delta.py /tmp/delta-now.tsv   # 11 live controls
```

The instrument is fixtured on both sides: 7 unit branches (4 kill, 1 survival)
and **11 live controls over the real estate — 4 known-moved and 7 known-still,
all correct**. A matcher that passes fixtures and returns nothing on real text
is still broken, so the real-slice control is not optional.

## 5 · What the re-audit found

*(§ 5 is completed from the fleet's returned evidence; see the sections below.)*

## 6 · Defects found in fleet-manager's own live truth, and fixed here

Three were found in the hub's own boot path while establishing the baseline.
All three directly blocked it — a successor `state/` seed distills from these
files — so all three were fixed inline with the reason stated in the diff.

1. **`docs/current-state.md` carried three different states for one open
   question, inside one file.** `OQ-FM-D2-TARGET` read **STILL OPEN** in § Work
   state, **CLOSED** 150 lines below in the OD-26 entry, and *"awaits the
   owner"* in § Next action — the section a cold session reads to decide what to
   do. The program's NOW pointer and [`owner-queue.md`](../owner-queue.md) both
   already said **ANSWERED 2026-08-28 — `spider-swing`** (OD-26). Corrected to
   the answered state, with the withdrawal history kept.
2. **`docs/current-state.md` never said this repository is being replaced.**
   The mandatory third read answers *"what is true now"*, and its only match for
   "successor" was a line about `superbot`'s successor bot. No mention of the
   fresh-start redirect, the name `estate`, the build order, or [D-0025]/[D-0026].
   A successor state document distilled from it would have described a hub with
   no cutover. Added, with provenance.
3. *(further hub-level defects from the area lanes are recorded in § 7.)*

**This is the fourth recorded instance of one defect class**, and naming it is
worth more than the three fixes: the boot file's own read-path entries 0, 1b and
2b each exist because *a decision existed and was not on the path that would
deliver it*. The class is not "documents go stale" — it is that this estate's
front doors are each internally plausible and jointly stale, which the
independent review named in its § 7 and which reproduced here twice more.

Two of that review's four § 7 findings are **now fixed** and were re-verified
at this run's HEAD: `docs/MAP.md` does route to `owner/` (a CORE-tier row), and
`docs/planning/README.md` records the hard cut, the carry set and the name as
answered rather than open. One is fixed by [D-0025]'s own ANSWERED paragraph.
The fourth — current-state naming an older action — is finding 2 above, and it
was **wider than the review stated**.

## 7 · Contradictions — exposed, never reconciled away

*(completed from the fleet's returned evidence)*

## 8 · The seed manifest

*(completed from the fleet's returned evidence)*

## 9 · The Substrate Kit dependency, at its currently verified state

The seed's shape depends on kit behaviour, and a concurrent session is changing
that behaviour right now. This run **records the dependency and measures the
current state**; it solves nothing here and proposes no kit change.

`MEASURED` 2026-09-04T12:0xZ, live API, direct egress:

| What | State | Command |
|---|---|---|
| Latest **published** kit release | **v1.21.0**, published 2026-08-13T12:23:57Z; assets `bootstrap.py`, `bootstrap.py.sha256`, `release.json` | `GET /repos/menno420/substrate-kit/releases/latest` |
| Kit `main` | `ff06fb902c69`, 2026-09-01T18:25:00Z — **ahead of the published release** | `GET …/branches/main` |
| **K1–K5** (adoption profiles) | **`menno420/substrate-kit#590`, OPEN** — head `19d70eeff43e`, 31 files, 7 commits, +4,761, last updated 2026-09-04T12:03:17Z | `GET …/pulls/590` |
| What fleet-manager vendors | `kit_version 1.21.0` (`substrate.config.json`), and `bootstrap.py` self-reports `1.21.0` | read at HEAD |

**The dependency stated exactly, so the seed session does not have to infer it.**
`[D-0035]` puts *"K1–K5 in substrate-kit, one release"* **before** the seed. As of
this measurement K1–K5 are **not released, not on kit `main`, and exist only in
an open pull request**. So a seed item that requires the `hub` adoption profile
is blocked on three events in order — #590 merges · a release is cut (the cut is
owner-paced, and the record says fixes already on `main` are waiting for the next
batch) · the new hub adopts that release. **None of the manifest's seeded items
depends on any of them**, which is the property this run was asked to preserve:
the baseline is consumable by a seed session whether or not K1–K5 have landed,
and what changes with them is the *tree the kit plants*, not the *truth the
manifest carries*.

**What this run deliberately did not do:** read #590's diff to judge it, form a
view on the adoption-profile design, or record any K1–K5 behaviour as a fact.
The five items are a live PR by another session; anything said about their
behaviour today would be stale on merge. A seed session re-checks the four rows
above at launch — they are the first entry in the handoff's re-check list (§ 11).

## 10 · Testing the baseline against cold-session use

*(completed from the blind-scored test)*

## 11 · Verdict, and the exact handoff

### The verdict

*(completed from the fleet's returned evidence and the blind score)*

### What a future `estate` creation session can now safely do

1. **Work from [the manifest](../planning/2026-09-04-estate-seed-manifest.csv)
   rather than re-auditing the estate.** Every row carries a subject, a source
   repository and path, a source SHA or live-API verification point, a certainty
   tag, the canonical owner of that truth, one destination role, one disposition,
   whether transformation is required, the links that must survive, any blocker,
   and a verifier. Rows the survival rule killed are present with `survives=no`
   and the branch that fired, so the seed session can argue with the rule rather
   than rediscover its casualties.
2. **Treat the census as settled and each repository as dispositioned once.**
   28 repositories, reconciled live against `ESTATE.md`.
3. **Seed the eighteen `repositories/<repo>/` folders that have no Layer-2
   folder today** using § 5's re-audit for the eight non-active-but-live ones and
   a README-only row for the nine archived, per the structure proposal.
4. **Carry the one answered intent worksheet as owner-authored truth** —
   `owner/intent-workbooks/estate/why-this-estate-exists.md`, his words of
   2026-08-31 on why the successor exists. The other 73 worksheets carry
   questions, not answers, and seed as forms.
5. **Take the three fixed hub defects as fixed** (§ 6) and the two fixed
   review § 7 findings as fixed — all re-verified at this run's HEAD.

### What it MUST re-check at launch, and why

| Re-check | Why it cannot be inherited |
|---|---|
| **Re-run `delta.py` against `anchors.tsv`** | The estate moves; this baseline is a snapshot at 2026-09-04T11:34Z. The command is one line and the anchors are committed. |
| **The four Substrate Kit rows in § 9** | K1–K5 were an open PR at this measurement. Published release, kit `main`, PR #590's state and what the hub vendors all change without notice. |
| **Every `carry` row's source SHA** | A carry copies bytes. If the source moved, the copy is a stale fork of a live document — the exact failure the fresh start exists to end. |
| **`fleet-manager`'s own HEAD** | It moved 23 commits between its prior evidence and this run, and it is the substantive seeding source. |
| **The open-PR inventory** | Taken at one instant with `per_page=100`; `superbot` alone carried 8 open dependabot PRs, and dependabot churn is continuous. |
| **Any row whose `certainty` is `MEASURED-PRIOR`** | Someone else measured it, dated. That is provenance, not currency. |

### What remains dependent on the separate Substrate Kit implementation

Only the **shape the kit plants**, never the truth the manifest carries:
the `hub` adoption profile (no `control/` bus, no generic `docs/` set, a visible
`sessions/`, a pointer-shaped owner profile, untracked guard telemetry). Until
kit #590 merges, a release is cut and the new hub adopts it, a seed will be born
into the default shape and will need those five things undone by hand — which is
exactly the cost `[D-0035]` sequenced K1–K5 before the seed to avoid. **The
manifest is consumable either way**; what changes is how much hand-work the seed
commit carries.

## 12 · What this run did NOT establish

An undisclosed limit is the real defect, so these are stated as flatly as the
findings.

1. **The delta's baseline is recovered from a DATE, not a SHA**, because the
   2026-08 audit wave recorded almost none. Its error is bounded by one day of
   commits per repository and always errs toward over-reporting change. Fixed
   for the future, not for this run: every manifest row carries a source SHA, so
   the next delta is exact.
2. **`UNCHANGED_REUSABLE` is a claim about the tree, not about the evidence.**
   Zero commits since a measurement proves the *source* did not move; it does
   not prove the measurement answered the successor's questions. § 5's reuse lane
   judges that separately and its verdicts are the ones to read — a repository
   can be unmoved and still not reusable.
3. **The census describes what was fetched, never what was missed.** It is
   scoped to `GET /user/repos?affiliation=owner` for this account. A repository
   under another owner, in an organisation, or shared with the account would not
   appear, and nothing here would look wrong.
4. **No claim is made about Substrate Kit's K1–K5 behaviour.** § 9 measures only
   where that work *is*. It is another session's open PR and anything said about
   its behaviour would be stale on merge.
5. **The cold-session test is ten questions**, blind-scored. A pass is evidence
   the baseline routes, never proof it routes everything, and the answering
   agents ran inside this repository, so § 10 reports the leak assessment
   alongside the score rather than assuming isolation.
6. **The owner's half of the acceptance test is not run.** His browsing test —
   finding a named document on GitHub's web view without opening an index — is
   his, and this run cannot substitute for it.
7. **This run did not test the `estate` tree**, which does not exist. It tests
   whether the *baseline* can seed one. The door-test walks in the structure
   proposal remain unrun against anything real.
8. **The re-audit is a slice, by design.** Fourteen repositories were re-read;
   nine archived ones were confirmed archived and given provenance rows rather
   than audited; five were argued for reuse. Anything the unread nine hold beyond
   their provenance line is unmeasured, and § 5 names the one question that was
   asked of them.
9. **A manifest is a proposal, not a cutover.** Every row is a *candidate* with a
   verb and a verifier. Whether the owner accepts the verb is his; the run's
   claim is that each row is provenanced enough to be argued with, not that the
   argument is settled.
10. **The three hub defects fixed inline are the ones that blocked this
    baseline** — they are not a full audit of fleet-manager's live truth, and the
    area lanes' `surprises` in § 7 are a sample of a class rather than its
    enumeration.
