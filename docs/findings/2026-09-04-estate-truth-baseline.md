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
> and the seed, and the build order he chose on 2026-09-01 (decision 35 in `docs/decisions.md`) makes the
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
becoming the read-only archive (decision 25 in `docs/decisions.md`) · the name `estate` (decision 26 in `docs/decisions.md`) · the
three carry verbs — **carry whole · distill · archive only** · the absolute
write cutover with a lagging archive flag · the eleven role names · the
findability contract (decision 32 in `docs/decisions.md`) · the archive shape (decision 33 in `docs/decisions.md`) · file-length
caps (decision 34 in `docs/decisions.md`) · the build order, **thin seed → blind cold test → write
cutover → deeper machinery, with only K1–K5 before the seed** (decision 35 in `docs/decisions.md`) ·
hooks in the hub repository only, by design (decision 38 in `docs/decisions.md`) · the fan-out model tiers
(decision 40 in `docs/decisions.md`) and the three-round Codex cap (decision 39 in `docs/decisions.md`).

**Genuinely unverified before this run, which is what made it the correct next
step:**

1. **No per-repository delta existed.** The plan says re-audit *where information
   changed*, and nothing computed where it had. The 2026-08 audit wave recorded
   almost no SHAs — the 2026-08-21 estate review that built `ESTATE.md` from 26
   repositories records **zero**, the 2026-08-23 intent audit **two** — so
   "has it changed" was not answerable from the record at all.
2. **No migration manifest existed**, though decision 35 in `docs/decisions.md` makes it a prerequisite of
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
  The sharpest was invisible in any summary: one agent read **a different
  repository's README** while two ran concurrently. Its own wall blamed the
  network — *"apparent proxy/cache anomaly on this environment's egress path"* —
  and that is **wrong**: `creator-kit`'s README is 2,112 bytes, the agent
  received 2,113 (one trailing newline from the decode), and both transcripts
  show the two agents reading the same `$OUT/README.md` in a shared scratchpad.
  Nothing came from the network that should not have; two processes shared a
  filename. Corrected in the pilot log, which had repeated the agent's
  attribution. The instruction it produced — cross-check every fetched file's
  blob sha and size against the tree listing — is kept, because it catches
  either cause and would have caught this one at the moment it happened.

**Model staffing was chosen per stage, never inherited** (decision 40 in `docs/decisions.md` as amended
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
the *"dead rooms"* the door test already penalises.

**Where that obligation lives, stated exactly, because an earlier draft of this
paragraph said something the artifact contradicts.** It is **not** a manifest
row. An enumerator proposed one (*"the 18 of 28 repositories with no Layer-2
folder need a `repositories/<repo>/README.md` authored fresh at seed time"*) and
**the survival rule killed it** — `survives=no`, on `not source_path`, because a
thing that must be *written* has no source to cite. That is the rule behaving
correctly: a manifest row is a claim about existing truth, and future work is
not that. The obligation is therefore carried in **§ 11's handoff**, where work
belongs, and the arithmetic there is stated per repository rather than as one
number. Found by the independent completeness critic, which read the row and the
paragraph and reported that they disagreed.

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

## 4b · What moved during the run — and a correction to the estate's own activity tool

The `BASE` contract schedules a re-read before publication. Running
`python3 tools/estate_activity.py refresh` mid-run (exit 0) surfaced two things
the 11:34Z snapshot could not have held, one of them material.

### Two other sessions started while this one was auditing

| repo | PR | opened | what it is |
|---|---|---|---|
| `fleet-manager` | [#1021](https://github.com/menno420/fleet-manager/pull/1021) | 2026-09-04T12:18:24Z | *"Spider Bot's purpose, recorded"* — 6 files |
| `spider-bot` | [menno420/spider-bot#3](https://github.com/menno420/spider-bot/pull/3) | 2026-09-04T12:19:06Z | *"AI operations: one intake path, one moderation path…"* — 2 files |

Both carry the **same owner-live direction of 2026-09-04**, and their own PR
bodies say it is *"newer than every record in this repo"*:

> *"Spider Bot exists to manage the Slingy Spider server and help during testing
> of the game. It should become a reliable automoderator with heavy AI
> integration. People should be able to talk naturally to it for guidance,
> complaints, bugs, feedback and improvement ideas."*

**This is material, not incidental.** `spider-bot` is one of the thirteen
repositories in this run's re-audit slice, and its purpose was being **restated
by the owner while an agent of this run was reading it at a SHA pinned before
that**. So this baseline's `spider-bot` row is **superseded on its purpose field
at the moment of writing**, and the seed manifest carries that as a blocker
rather than as a fact: the successor's `repositories/spider-bot/intent.md` must
be written from fm #1021 and spider-bot #3, not from this run's reading.
`WEAK_OR_INCOMPLETE` was the right classification for it and remains right for a
different reason than the one that earned it.

It is also the second concurrent session this run has had to work around — the
first being Substrate Kit's kit #590 (§ 9). Two independent sessions moving
estate state during a three-hour audit is not an anomaly to note once; it is the
**operating condition** a seed session will also be in, which is why the handoff
in § 11 makes re-running the delta the first launch step rather than an optional
freshness check.

### The activity tool over-reports "invisible work", and the cause is `pushed_at`

The same run flagged two repositories under *"Invisible work — repositories that
moved without a card to explain it"*:

| repo | flagged because | `pushed_at` | what that push actually was |
|---|---|---|---|
| `superbot` | *"newest card is 2026-08-13 — pushed 18 days later with no card"* | `2026-08-31T18:38:08Z` | PR **#2453**, `dependabot[bot]`, created **`2026-08-31T18:38:08Z`** — the same second. Default branch `5e3a667b` is from 2026-08-20T23:17:52Z and did not move. All 8 open PRs are dependabot's; **zero distinct non-bot authors**. |
| `spider-swing` | same wording | `2026-08-31T04:26:56Z` | PR **#180**, `dependabot[bot]`, created **`2026-08-31T04:26:57Z`** — one second later, which is the branch push followed by the PR. Default branch `fc64a3fb` is from 2026-08-23T20:17:00Z and did not move. |

The attribution is a match to the second, not an inference: `pushed_at` advances
on **any** ref, so a bot opening a branch reads identically to an unrecorded
human or agent session. Both rows are false positives.

The log's own framing is what makes this worth writing down rather than a nit:
it calls that section *"the section the log exists for"* and says a row means
*"nothing in the estate's records says who did that work or why."* Here the
records say precisely who did it, with a timestamp that matches exactly — and
the tool did not look.

**Scoped honestly:** both repositories do also carry stale non-dependabot
branches (`superbot` has 46 branches including several `claude/*` and `codex/*`;
`spider-swing` has 5). None of those is what `pushed_at` is reporting — the
newest push in each case is the dependabot one — so the false positive is
specifically about *which* ref moved most recently, not a claim that these
repositories have no unrecorded history anywhere.

**Recorded, not fixed.** The fix is a real change to a generator that this run
did not set out to touch, and the honest scope note is that `estate_activity.py`
is advisory and wired into no gate, so a false positive costs an investigation
rather than a red build. It is carried into the seed manifest as a **known
defect of a carried tool**, which is the disposition the successor needs: the
tool is worth carrying, and it is worth carrying with this written down.

## 5 · What the re-audit found

Thirteen repositories re-read from their own source at pinned SHAs, each then
attacked by an Opus adversary told to kill it. **26 agents, 26 returned, 0
errors.** Raw evidence: [`repo-readings.json`](data/2026-09-04-estate-truth-baseline/repo-readings.json)
and [`refutations.json`](data/2026-09-04-estate-truth-baseline/refutations.json).

| repo | state | docs vs source | front door | hub agrees | prior evidence |
|---|---|---|---|---|---|
| `spider-swing` | active | **DISAGREE** | **NO** | PARTIAL | STILL_HOLDS |
| `product-forge` | active | **DISAGREE** | **NO** | **DISAGREE** | STILL_HOLDS |
| `estate-backups` | dormant | PARTIAL | **NO** | AGREE | STILL_HOLDS |
| `couch-legend` | active | PARTIAL | YES | PARTIAL | STILL_HOLDS |
| `spider-bot` | active | PARTIAL | PARTIAL | PARTIAL | **PARTIAL** |
| `websites` | active | PARTIAL | PARTIAL | PARTIAL | **SUPERSEDED** |
| `creator-kit` | dormant | PARTIAL | PARTIAL | AGREE | STILL_HOLDS |
| `idea-engine` | dormant | PARTIAL | PARTIAL | PARTIAL | STILL_HOLDS |
| `sim-lab` | dormant | PARTIAL | PARTIAL | AGREE | STILL_HOLDS |
| `superbot-next` | parked | PARTIAL | PARTIAL | AGREE | STILL_HOLDS |
| `shiftlife` | paused | AGREE | YES | AGREE | STILL_HOLDS |
| `substrate-kit` | infrastructure | AGREE | YES | AGREE | STILL_HOLDS |
| `superbot` | frozen | AGREE | YES | AGREE | STILL_HOLDS |

**Only two walls in thirteen repositories**, both recorded with exact error text.
Private repositories read as cleanly as public ones on the direct-PAT path.

**Two of these readings were cross-checked by hand rather than trusted** —
[`spot-checks.md`](data/2026-09-04-estate-truth-baseline/spot-checks.md) carries
the session's own live-API verification of `superbot`'s missing root README and
`product-forge`'s four seat-era ORDERs still reading `status: new`. Both prior
claims held exactly; the first needed its wording corrected (the repository has a
front door, it is simply not at root), which is the kind of imprecision a seed row
would have propagated.

### The three findings that matter for the seed

1. **Three front doors are inadequate and two of them are actively wrong.**
   `spider-swing`'s README still says naming is *"still open"*, *"No release
   signing exists"* and store publishing *"remain[s] absent"* — all three false
   against the repository's own ledger, which records the name decided
   2026-08-05, a signing workflow run through version code 66, and a signed
   build on Play's internal-testing track. `product-forge` routes a cold session
   to a seat retired 2026-07-21. Both were known; **neither has been fixed**, and
   the turnkey fix briefs written 2026-08-23 are still unapplied.
2. **`websites` is the one repository whose prior evidence is SUPERSEDED** —
   the only `CHANGED_REAUDIT` row where re-reading changed the answer rather
   than confirming it. `spider-bot`'s reads PARTIAL for a different reason: its
   purpose was restated by the owner *during this run* (§ 4b).
3. **`prior_evidence_verdict` is `STILL_HOLDS` in 11 of 13.** The 2026-08 audit
   wave was accurate. What it lacked was not correctness but **scope** — which
   is exactly what the unchanged-reuse lane found on the other five
   repositories, and it is the finding that should shape the seed: this estate's
   records are trustworthy about what they measured and silent about what the
   successor needs.

### The unchanged five: zero movement is not reusability

The [reuse lane](data/2026-09-04-estate-truth-baseline/unchanged-reuse.md)
re-verified all five tips independently (5 of 5 byte-identical to the pinned
SHAs) and then judged the evidence rather than the tree:

| repo | verdict |
|---|---|
| `venture-lab` | **REUSABLE** |
| `superbot-plugin-hello` | split — reusable for *"is it a build input?"* (no, measured from the host's own boot test), not for purpose |
| `curious-research` · `gba-homebrew` · `pokemon-mod-lab` | **NOT_REUSABLE** |

Four of the five anchor to `2026-08-22-repo-dispositions.md`, whose own header
says it is *"**Not canonical for** any repo's internal state."* It measured
*should this be archived*, never *what is this repo for, where does its truth
live, what must a fresh agent not trust*. **Zero commits proves the source did
not move; it cannot make evidence reusable that never asked the question.**
`curious-research` is the sharpest case — its row rests on the owner's *"gets a
new mission later"*, a claim about **intent**, for which commit count is not
even the right freshness instrument.

**This overturns the mechanical classification for four repositories**, and it is
the single most important correction this run makes to its own delta.

### The nine archived

The [provenance lane](data/2026-09-04-estate-truth-baseline/archived-provenance.md)
confirmed the archived flag live on all nine and answered the one question that
could change a disposition — *does anything live still depend on one?* —
with **None**, from six targeted checks (the one real pin read at its source;
the live successor `spider-bot`'s own docs, 0 hits in 4 of 4 files; the one cron;
serving surfaces; forks and issues; the hub's records). It states its own limit:
`search/code` indexes a minority of this account, so this is **not** an
account-wide completeness claim, and closing it would need a clone-and-grep of
the keeps, which was not run.

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
   fresh-start redirect, the name `estate`, the build order, or decision 25 in `docs/decisions.md`/decision 26 in `docs/decisions.md`.
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
answered rather than open. One is fixed by decision 25 in `docs/decisions.md`'s own ANSWERED paragraph.
The fourth — current-state naming an older action — is finding 2 above, and it
was **wider than the review stated**.

## 7 · Contradictions — exposed, never reconciled away

**Readers reported 13. Their adversaries found 38 more they had missed** — the
refute stage nearly quadrupled the count, which is the clearest evidence in the
run that a single-pass audit under-reports disagreement. It also killed **58
claims** and flagged **73 certainty overclaims** (`MEASURED` where the basis was
a document describing a live surface — the estate's own TRAP-001). **Every one of
the 13 verdicts is `PARTIAL`:** no reading was fully confirmed, and none was
wholly refuted.

**One contradiction is `UNRESOLVED` by design** — `spider-bot`'s status, where
the repository's README Status and Threads sections disagree with each other and
with the hub's Layer-2 folder, and the owner restated the repository's purpose
mid-run. Two authoritative sources disagreeing is a contradiction requiring
resolution, not a tie to be broken by whichever is easier, so the manifest kills
the affected seed row rather than picking one.

### Hub-versus-repository, resolved in the repository's favour

`product-forge` is the only outright `DISAGREE` on the hub axis, and
`spider-swing`, `couch-legend`, `spider-bot`, `websites` and `idea-engine` are
`PARTIAL`. The pattern is consistent and worth stating because it shapes the
seed: **where the hub and a repository disagree, the hub is usually right about
the resolved state and the repository's own front door is stale.** `spider-swing`
is the clean case — `ESTATE.md` correctly records the name, the Play track and
the signing, while the repository's README denies all three.

That inverts the naive rule *"the repository always wins"*. The repository wins
on **what is true**; it does not follow that its **README** wins, and a seed
built by copying front doors would import the errors. The manifest's
`canonical_state_source` column exists for this: it points at the repository's
ledger, not its README.

### Contradictions found inside single hub documents

Three, all fixed or withdrawn in this PR, and all of the same class — *"several
polished front doors, each internally plausible and jointly stale"*, here
occurring **within one file**:

- `docs/current-state.md` held three different states for `OQ-FM-D2-TARGET` (§ 6).
- `docs/current-state.md` never mentioned that this repository is being replaced (§ 6).
- `docs/ESTATE.md` carried a `search/code` sweep presented as having *"removed
  the stated blocker on the deletion question"*, 83 lines below its own section
  headed *"`search/code` does NOT cover this account — dependency sweeps are
  unreliable."* Withdrawn; the disposition is unaffected because it rests on
  value, but **deletion is irreversible** and that clearance was not earned.

## 8 · The seed manifest

[`../planning/2026-09-04-estate-seed-manifest.csv`](../planning/2026-09-04-estate-seed-manifest.csv)
— **generated**, never hand-edited, by
`python3 tools/estate_baseline/build_manifest.py` from the fleet's retained
journals. Re-running it reproduces the file; re-running it against a fresh fleet
at seed time shows what moved.

**Twenty-one columns per row**, which is what `decision 35 in `docs/decisions.md``'s acceptance test asks
for (*"one verb per candidate with a verifier's name"*) plus the provenance the
fresh-start directive requires (*no certainty tag, no seed*): subject · source
repository · source path · verification point · certainty · canonical owner ·
destination role · disposition · transformation required · links that must
survive · blocker · verifier · the four dissent fields · fact · origin lane ·
`survives` · `killed_by`.

### The shape of the cut

| | N |
|---|--:|
| rows | 183 |
| **live in `estate`** | **68** — 18 `carry`, 50 `distill` |
| `archive_only` (stays in fleet-manager, reachable by link) | 55 |
| killed by the survival rule, published with the branch that fired | 60 |

**68 live items against ~1,300 tracked files** is the thin seed the plan asks
for, and the ratio is the point rather than the count: the fresh start exists
because *"a growing archive nobody reads"* is a named non-goal, and a manifest
that seeded three hundred items would have reproduced it.

Destination roles of the 68: `practices/` 14 · `repositories/` 14 · `owner/` 11 ·
`tools/` 9 · `plans/` 6 · `state/` 6 · `decisions/` 3 · `root` 3 · `evidence/` 1 ·
`ideas/` 1.

> **Every number in this section was wrong until the external round, and the
> paragraph below it said the opposite of what the artifact showed.** The
> section was written when the manifest held 109 rows — the fleet-manager half
> alone — and was never regenerated after the repository lane folded in. All
> three independent critics opened the CSV, counted, and reported it as a P1;
> two of them reproduced the manifest with its own generator first to prove the
> artifact was not the stale half. **This is the run's own TRAP-001 — a dated
> reading presented as current — committed inside a document that names
> TRAP-001 twice.** Corrected here from `csv.DictReader` over the committed
> file, and the same numbers are what the generator prints.

### What the rule killed, and what the external round changed about that claim

Sixty rows died across **30 distinct branch strings**. The split by origin:
**51 kills the rule made itself · 9 echoed from a disposition judge.**

**The earlier draft of this paragraph said the reverse** — *"all nine were
already killed by a judge, and the rule independently overturned zero"* — which
was true of the 109-row half and false of the artifact it was printed beside.
The builder prints the split on every run (`kill origin : …`); the sentence was
carried forward from the earlier state instead of read off the output. The
provenance critic called this *"the run's central methodological self-criticism,
inverted against its own artifact"*, and it was right.

**Two aggregation defects the external round found, both now fixed, both
measured before and after:**

- **The drop join lost 19 of 44 adversary verdicts.** `build_manifest.py` joined
  a refuter's `seed_items_to_drop[].subject` to a reader's item by exact
  case-folded equality; adversaries write qualified subjects (*"identity and
  live status — the 'live in production on Railway' clause"*) where the reader
  wrote the bare noun. **This is the 2026-08-29 defect reproduced by the run
  built to avoid it** — a dissent collected and then lost, one layer further
  down than where that run lost it. Replaced with a content-word overlap join;
  **34 of 44 now apply**, and the residual 10 are disclosed in § 12 rather than
  smoothed.
- **73 certainty overclaims were collected and read by nothing.** The refute
  schema gathered them; `SCHEMA_FIELDS` had no such field and the rule no such
  branch. Now a field the rule reads — `certainty_overclaimed and certainty in
  ('MEASURED','OWNER')` — with the field audit still clean (0 unread, 0
  undefined) and the fixtures at 14 cases, 9 kill / 5 survival. **8 of 73
  applied**, because an overclaim names a claim rather than a seed subject and
  only some resolve to one; the other 65 are disclosed, not discarded.

**A third defect the fixtures caught while fixing the first.** Scoping the drops
per refuter is required — a drop written about `spider-swing` was reaching a
`superbot` row — and the giveaway was arithmetic: **49 applied against 44 that
exist**. The fixture now has a cross-repository case that fires when the scoping
is removed, verified by removing it.

### Coverage

The `origin_lane` column carries which agent produced each row, so coverage is
readable from the artifact rather than asserted here. The builder also prints a
`NOTE` naming any repository in the re-audit slice with no reading in the
journals it was given — a deliberate loud null rather than a silently short
manifest.

## 9 · The Substrate Kit dependency, at its currently verified state

The seed's shape depends on kit behaviour, and a concurrent session is changing
that behaviour right now. This run **records the dependency and measures the
current state**; it solves nothing here and proposes no kit change.

`MEASURED` 2026-09-04, live API, direct egress, **re-read at publication**:

| What | State | Command |
|---|---|---|
| Latest **published** kit release | **v1.21.0**, 2026-08-13T12:23:57Z — unchanged | `GET …/releases/latest` |
| Kit `main` | **`6a82288e9e81`, 2026-09-04T12:30:02Z** | `GET …/branches/main` |
| **K1–K5** (adoption profiles) | **`menno420/substrate-kit#590` MERGED 2026-09-04T12:15:39Z**, merge commit `8a83c733eded` | `GET …/pulls/590` |
| What fleet-manager vendors | `kit_version 1.21.0`; `bootstrap.py` self-reports `1.21.0` | read at HEAD |

> **This section said `OPEN` until the external round.** It was measured at
> 12:0xZ, the PR merged at **12:15:39Z**, and the finding kept being edited for
> four more hours without the row being re-read. **The BASE contract required
> exactly this re-read before publishing and it was not run against the kit** —
> so the run failed its own § 6 contract on the one repository it had declared
> out of scope but depended on. All three critics caught it independently.

**What the merge does and does not change.** K1–K5 are now on kit `main` but
**not in a published release** — v1.21.0 still is, from 2026-08-13 — and
fleet-manager still vendors 1.21.0. So the ordering the build order requires
(*"K1–K5 in substrate-kit, one release"* before the seed) is **one step further
along and still not satisfied**: what remains is the cut, which is owner-paced,
and then the new hub adopting it. The property this run was asked to preserve
holds unchanged: **no seeded item depends on any of it.**

**What this run deliberately did not do:** read #590's diff to judge it, form a
view on the adoption-profile design, or record any K1–K5 behaviour as a fact.
The five items are a live PR by another session; anything said about their
behaviour today would be stale on merge. A seed session re-checks the four rows
above at launch — they are the first entry in the handoff's re-check list (§ 11).

## 10 · Testing the baseline against cold-session use

Three cold agents answered [the ten pre-registered questions](data/2026-09-04-estate-truth-baseline/cold-session-rubric.md)
from the baseline artifacts **alone**; an independent Opus scorer, which had not
seen this synthesis, applied the rubric committed **before any answer existed**.

**Result: PASS — mean 2.0, all ten questions at 2, zero at 0, zero
`right_for_wrong_reason`, and every cited artifact verified by the scorer as
actually supporting its answer.** No question was reported unanswerable.

**And the result is heavily qualified, by the scorer, in two ways the rubric
asked for and one it did not anticipate.**

1. **The agents were not cold.** All three ran with
   `/home/user/fleet-manager/.claude/CLAUDE.md` auto-loaded, and **all three
   self-disclosed it unprompted and specifically** in the `leaks` field. Its
   load-bearing overlap is Q4 (the successor's name and build order), which the
   boot file states independently. The scorer checked whether the permitted
   artifacts carry Q4 on their own and found they do — § 1 and a manifest row —
   *"so the baseline does route Q4; these three agents are simply not clean
   evidence that it does."* That distinction is the honest reading of the whole
   PASS.
2. **The rubric leaked into the corpus.** `unchanged-reuse.md` quotes Q1, Q2, Q3
   and Q7 **with their pass criteria**, and it was in the permitted artifact set,
   so the agents could read the marking scheme for four of ten questions. The
   scorer found this; the rubric's own "what this does not establish" did not
   anticipate it. **Neither did I** — the lane was told the rubric's questions
   were the bar it should judge prior evidence against, which is why they are
   quoted there, and nobody noticed that made the file an answer key.
3. **A mean of 2.0 across ten questions is itself a signal to distrust.** A
   perfect score on a test whose corpus contains part of its own marking scheme
   and whose agents had the boot file loaded is weak evidence of routing and
   strong evidence that the test was too easy. It is reported as PASS because
   that is what the pre-registered bar says; it is **not** treated as
   establishing the retrieval half of the acceptance test, and § 11 does not
   rest on it.

**What the scorer said the baseline should have carried**, all now either fixed
or recorded: §8's regenerated counts (fixed) · a `supersedes` field per
repository (recorded) · a reconciliation of §5's `hub agrees` column with the
manifest's resolution fields (recorded) · a **state-word column in the
manifest**, because today every state word lives only in §5's prose table, which
forces a machine-readable question back into narrative (recorded) · the rubric
kept out of the artifact set (recorded).

## 11 · Verdict, and the exact handoff

### The verdict

# `PARTIAL`

Not `READY_FOR_THIN_SEED`, and the external round is why. Three independent
critics attacked the synthesis on separate lenses and returned
**PARTIAL · BLOCKED · BLOCKED** with 35 findings between them, of which **eleven
were P1 and every P1 was correct.** A verdict of READY written over that would
be exactly the failure the owner's own EAP account names as what killed the last
rebuild — *"work that was claimed to be complete was in fact not complete at
all."*

**What the PARTIAL rests on — the parts that survived attack:**

- **The census.** The completeness critic re-ran `GET /user/repos` itself and
  reproduced 28 / 9 archived / 3 private and the `ESTATE.md` reconciliation.
- **The delta instrument.** Reproduced from its own commands; 11 of 11 live
  controls correct.
- **The manifest's reproducibility.** Two critics regenerated the CSV
  byte-identical from the committed journals.
- **The raw evidence.** *"The run's raw evidence is unusually good"* — the
  provenance critic, which opened 12 rows' `source_path` at their stated
  verification points, 7 locally and 5 cross-repo.
- **The reuse finding**, which is the run's most consequential correction to
  itself and drew no P1.

**What keeps it from READY — the defects that were real, in the order they
matter:**

1. **§ 8 described a manifest that was not the committed one**, and inverted the
   run's own central self-criticism. Both fixed; both were the run committing
   TRAP-001 inside a document that cites TRAP-001.
2. **The aggregation lost 19 of 44 adversary drops and read 0 of 73 certainty
   overclaims** — the 2026-08-29 defect, reproduced one layer down by the run
   built to prevent it. Fixed and re-measured (34 of 44; 8 of 73), with the
   residual disclosed rather than closed.
3. **§ 9 said the kit PR was open four hours after it merged**, which is the
   BASE contract's own re-read not being run. Fixed.
4. **Provenance is string-non-emptiness, not path-shape.** Rows survive with
   `source_path` values like `(live PR list)`. The rule tests that the field is
   filled, not that it points anywhere. **Not fixed** — it needs a validator and
   a re-run of the readings, which is more than a correction.
5. **The manifest is not estate-wide.** Fourteen of 28 repositories contribute
   zero rows: the nine archived (by design) and the five unmoved (because their
   evidence is not reusable, which the run proved). Honest, and it means the
   artifact is a migration manifest **for fleet-manager plus thirteen
   repositories**, not for the estate.
6. **Several `carry` rows would fail `estate`'s own preflight on day one** —
   `docs/decisions.md` is 1,222 lines against a 200-line cap, and one row's
   blocker concedes the split *"must actually be done"*.

**A `PARTIAL` here is worth more than a manufactured `READY`.** The seed session
can work from this: the census is settled, the delta is reproducible, 68 live
items are provenanced, and the six items above are named with what each needs.
What it must not do is treat the manifest as final — it is a reviewed proposal
with known holes, which is what the acceptance test asked for.

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
exactly the cost `decision 35 in `docs/decisions.md`` sequenced K1–K5 before the seed to avoid. **The
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
8. **The re-audit is a slice, by design.** Thirteen repositories were re-read by
   the repository lane (fleet-manager was read by the five area lanes instead);
   nine archived ones were confirmed archived and given provenance rows rather
   than audited; five were argued for reuse. Anything the unread nine hold beyond
   their provenance line is unmeasured, and § 5 names the one question that was
   asked of them.
9. **A manifest is a proposal, not a cutover.** Every row is a *candidate* with a
   verb and a verifier. Whether the owner accepts the verb is his; the run's
   claim is that each row is provenanced enough to be argued with, not that the
   argument is settled.
10. **Provenance is tested for non-emptiness, not for shape.** `source_path`
    and `verification_point` are checked as filled strings, so a narration like
    `(live PR list)` passes as provenance. Three surviving `MEASURED` rows carry
    one. Fixing it needs a path/instant validator and a re-run of the readings.
11. **10 of 44 adversary drops and 65 of 73 certainty overclaims still reach no
    row.** The join is content-word overlap; an overclaim names a claim rather
    than a seed subject, and only some resolve to one. Better than the 19 and 73
    that were lost before the external round, and not zero.
12. **The manifest covers 13 of 28 repositories plus fleet-manager.** The nine
    archived contribute provenance prose and no rows, by design; the five unmoved
    contribute none because their prior evidence is not reusable. Anyone reading
    the CSV as *the estate's* migration manifest will be wrong.
13. **`only_source_is_hub_summary` is set on 7 of 183 rows and 0 of 123
    survivors**, while ~30 survivors are sourced from a hub index or README. The
    flag is agent-set and under-used, so that branch of the rule is close to
    inert on live data — it fires in fixtures, not here.
14. **Several `carry` rows exceed the successor's own file-length cap**
    (`docs/decisions.md` 1,222 lines against 200). `carry` was judged on whether
    the truth belongs live, never on whether the file can land as-is.
15. **The counts of what was re-audited disagreed between § 5 and § 12** — 13
    versus 14 — on whether `fleet-manager` counts as re-read. It is 13
    repositories by the repository lane plus fleet-manager by the five area
    lanes; the population is now named wherever a number appears.
16. **The three hub defects fixed inline are the ones that blocked this
    baseline** — they are not a full audit of fleet-manager's live truth, and the
    area lanes' `surprises` in § 7 are a sample of a class rather than its
    enumeration.
