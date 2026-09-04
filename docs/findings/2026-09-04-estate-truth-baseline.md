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

## 11 · Verdict

*(completed)*

## 12 · What this run did NOT establish

*(completed)*
