# The `estate` seed's own prerequisites — what moved at row level, a provenance validator, the canonical-state column

> **Status:** `reference` · tier **RECORD** · written 2026-09-04, fm #1036
>
> Follow-on to [`2026-09-04-estate-truth-baseline.md`](2026-09-04-estate-truth-baseline.md)
> (fm #1020, verdict `PARTIAL`). That finding's § 11 hands a future `estate`
> seed session a re-check list and its § 12 names what the run did not
> establish. This record works the items on both lists that live inside
> fleet-manager and need no agent fleet: the delta re-run, a row-level
> instrument for the *"every `carry` row's source SHA"* re-check, the
> path/instant provenance validator (§ 12 item 10), the
> `canonical_state_source` column (§ 12 item 11b), and a consumer for the
> subject-bearing overclaim schema (§ 12 item 11). **Not** the seed — the
> build order gates it on a kit release that is still uncut (v1.21.0 is the
> newest published release; K1–K5 sit on kit `main` unreleased, per the
> baseline's § 9 as re-read at HEAD). Not substrate-kit. Not E1.
>
> Certainty legend as in
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
> Every count below is read from a committed file named beside it; the live
> reads are direct-egress GitHub API calls made at the instants stated.

## 1 · The delta, re-run

`MEASURED` 2026-09-04T19:02Z — `delta.py` against the committed `anchors.tsv`
(run twice: at ≈18:27Z, and again at 19:02Z after the review round, because the
estate moved in between), output of the second run retained as
[`data/2026-09-04-estate-truth-baseline/delta-rerun-2026-09-04.tsv`](data/2026-09-04-estate-truth-baseline/delta-rerun-2026-09-04.tsv);
`test_delta.py` over that file: 7 unit cases, 11 of 11 live controls readable,
exit 0.

**The moved set grew by one during this session.** At ≈18:27Z four
repositories read `CHANGED_REAUDIT` — the handoff's couch-legend, fleet-manager,
spider-swing, substrate-kit. At 19:02Z **five** do: **spider-bot** joined when
its AI-operations tranche merged (`5a7f8a2`, 18:42Z) and two deployment-record
PRs followed. The other twenty-three read exactly as the audit left them (9
`ARCHIVED_OR_NONACTIVE`, 14 `UNCHANGED_REUSABLE`). Commits since the SHA each
audit read, at 19:02Z: spider-bot 27, fleet-manager 20, couch-legend 4,
substrate-kit 2, spider-swing 1. The handoff said that if this set grew, the
new repository's manifest rows were the first thing to re-check; § 2 does that
with an instrument rather than a reading.

What those commits touched, from `GET …/compare/{base}...{head}` per repository:

| repo | commits (first run → 19:02Z) | files at the first run | touches a file a surviving manifest row cites? |
|---|--:|--:|---|
| spider-bot | 0 → 27 | — | **yes** — every one of its six rows, one a survivor; see § 2 |
| fleet-manager | 16 → 20 | 90 | **yes** — see § 2 |
| couch-legend | 3 → 4 | 88 | no — `README.md` (the one surviving row's source) is not among them |
| substrate-kit | 2 | 31 | no — `docs/NEXT-TASKS.md` is not among them |
| spider-swing | 1 | 6 | no — `docs/current-state.md` is not among them |

A repository-level delta says "re-audit"; the file-level answer for three of the
five is "nothing this manifest relies on moved", and for the other two it is a
list of files. That gap is the reason for § 2.

## 2 · What moved at ROW level — the instrument, and what it says

**The instrument.** `tools/estate_baseline/row_delta.py` takes the manifest and,
for every row, (a) classifies the SHAPE of its provenance, (b) resolves the SHA(s)
in `verification_point` against the row's source repository, taking the
latest-dated one where a row names a reading and a later re-read — and only when
every candidate resolved, because falling back to the earlier reading when the
re-read is unknown would measure drift from a point the reader had superseded
(Codex round 2; such a row is `UNCHECKABLE` with the candidate named) — and (c)
compares the git object at each cited path — a blob for a file, the listing for
a directory, the matching entries for a single-level wildcard such as
`tests/*.py` — at that SHA against the same path at the live default-branch tip.
Identical objects mean the content the reader verified is the content that is
live. The row status vocabulary is in the script's docstring; the rule of
precedence is that one moved path outranks any number of unchanged ones,
because a `carry` copies bytes.

Fixtures: `tools/estate_baseline/test_row_delta.py` — the counts below are what
the suite prints, and the suite is the record: **18 provenance shapes** and
**10 verification-point forms** taken from live cells, **5 binding cases** (which
SHA binds, and the unresolved re-read that must not fall back), **5 path cases**
(4 kill / 1 survival) including the branch that must not fire, **8
row-precedence cases**, and live controls: 3 positives (fleet-manager rows citing
`docs/current-state.md`, `docs/ESTATE.md`, `docs/decisions.md` — all modified
in the first sixteen commits), 4 negatives (the three satellite survivors above
plus shiftlife, which has not moved since 2026-07-27), 1 uncheckable control and
1 api-reference control. **9 of 9 controls correct, exit 0** against the
committed snapshot. The three satellite negatives are the discriminating case:
their repositories moved, their files did not. (An earlier draft of this
paragraph carried the round-1 counts beside a round-2 suite; Codex round 2.)

**The snapshot.** `MEASURED` 2026-09-04T19:18Z — fleet-manager tip `17a532b`,
spider-bot tip `ee243fd`, the same tips the delta re-run in § 1 saw — 339 API
calls, exit 0 (taken three times during the session as the instrument was
corrected and the estate moved; only the last is committed) —
[`data/2026-09-04-estate-truth-baseline/row-delta.tsv`](data/2026-09-04-estate-truth-baseline/row-delta.tsv),
183 rows. Read from the file with `csv.DictReader`:

| | all 183 rows | the 119 survivors |
|---|--:|--:|
| `SOURCE_UNCHANGED` | 125 | **98** |
| `SOURCE_MOVED` | 25 | **18** |
| `SOURCE_UNVERIFIED_CROSS_REPO` | 2 | 0 |
| `UNCHECKABLE` | 31 | **3** |

**Of the 18 survivors whose source moved, 17 are fleet-manager rows and one is
spider-bot's** — *Railway build system is RAILPACK, not NIXPACKS* (`distill`,
`.railway/railway.ts`, rewritten by the AI-operations tranche; the distillation
must be redone from the live file). spider-bot's five killed rows moved too
(`README.md`, `CLAUDE.md`, `docs/extraction-ledger.md`). The fleet-manager files
behind the other 17 are ten:

`docs/current-state.md` · `docs/ESTATE.md` · `docs/decisions.md` ·
`docs/owner-queue.md` · `docs/CAPABILITIES.md` · `docs/traps.md` ·
`docs/planning/2026-07-26-consolidation-program.md` ·
`docs/planning/2026-09-01-estate-structure-proposal/` ·
`docs/planning/2026-08-21-game-community-bot/` · `tools/estate_baseline/seed_rule.py`

By disposition: 6 `archive_only` (the copy in the archive would be of an older
version — acceptable by that verb's own meaning, and the seed should copy at
seed time, not from the audit), 10 `distill` (the distillation must be written
from the live file, which is what `distill` already means), and **2 `carry`**,
which are the ones that matter:

| `carry` row | file | what moved since verification |
|---|---|---|
| *The decision ledger's own specification for how `estate` must be built* (OWNER) | `docs/decisions.md` | one entry appended since `14ea77e`: decision 42 in `docs/decisions.md` (Spider Bot), 59 lines, 1,222 → 1,281 — measured by diffing the file at both refs; an earlier draft of this cell said "decisions 40, 41 and 42" from the ledger's tail, which was an inference |
| *`tools/estate_baseline/` — this seeding run's own tooling* (MEASURED) | `tools/estate_baseline/seed_rule.py` | verified at the PR-branch head `7ccc88a`; the Codex round-3 fixes and this PR's own changes came after |

Neither is a surprise and neither invalidates the row — a `carry` of a file that
moved simply has to be a carry of the file **as it is at seed time**. What the
instrument adds is that this is now a fact the seed session reads off a column
rather than an instruction it has to remember.

**The 3 survivors the instrument cannot check** are the concrete form of the
baseline's § 12 item 10:

| row | why |
|---|---|
| *Owner-gated resume/archive decision* (fleet-manager, MEASURED-PRIOR) | its verification point names `33d9064b376f…`, which is **shiftlife's** tip, not a fleet-manager commit (HTTP 422 in fleet-manager) — the row's `source_repo` and its verification SHA disagree |
| *Cross-repo dependency: Android release signing* (fleet-manager, MEASURED-PRIOR) | `live-api@2026-09-04 (…)` — an instant with no commit |
| *sim-lab's canonical entry points are README.md + CONVENTIONS* (fleet-manager, MEASURED) | `local-read@2026-09-04` — an instant with no commit |

All three are rows a satellite's reading emitted about a hub file — the same
rows whose `canonical_state_source` § 3's re-keying corrected.

The 28 uncheckable killed rows split 10 with no path in `source_path` — 9 the
disposition judges' synthesised `(killed before a source was recorded)` and one
reader's `(live PR list)` — 14 with no SHA in `verification_point`
(`live-api@…`, `live-file@…`, `live-repo-tree@…`, `local-read@…`), and **4 API
references named as such** (`git/trees (harness/*)`, `live API:
pulls?state=open`, `live-api:pulls?state=open`, `releases API (tag …)`). The
two `SOURCE_UNVERIFIED_CROSS_REPO` rows cite a second path qualified with
`fleet-manager`; the row's SHA belongs to its own repository, so that path has
no verification point to compare and is named rather than compared at a SHA it
never had. **The first cut of the parser got eight of these wrong** — it read
three `+`-joined cells as narration, the four API references as narration or,
for `git/trees`, as a file not found, and dropped the wildcard in spider-bot's
`README.md, tests/*.py` as annotation so that row was judged on `README.md`
alone — Codex rounds 1 and 2 caught them; the parser now splits on ` + `,
honours a repository named before a path or as the first word of the
parenthetical after it (only when the census knows the name), names API
references, and expands a single-level wildcard against the directory listing at
both points (that row reads `SOURCE_MOVED` on both its paths). Counted from the
snapshot joined to the manifest on (subject, source_repo).

**A fact about the survivors' verification points the audit did not state.**
`sha_on_default_branch` is `no` for **84 of 119 survivors**: their SHAs
(`06dbbfe`, `14ea77e`, `7ccc88a`, `21b19be`, `50c1b1e`) are commits on the
fm #1020 PR branch, which was squash-merged as `049b112`. They resolve today
because the PR keeps them reachable, and the object comparison is exact
regardless. But they are not ancestors of `main`, so a later delta that starts
from `main`'s history will not find them, and GitHub does not promise to keep
unreachable commits forever. The safe re-anchor is mechanical and verifiable
per row — for each such row, if the object at the cited path is identical at
`049b112` and at the recorded SHA, the row may be re-anchored to `049b112` with
no loss — but it changes `verification_point` values, which live in the
journals the manifest is generated from. **Not done here**: that is a
regeneration from edited inputs, and the seed session should do it in one
step with the re-read of the three uncheckable rows.

## 3 · The `canonical_state_source` column

Added to `build_manifest.py::COLUMNS`, last, so the 22 pre-existing columns
keep their positions. Stamped per row from the `canonical_state_source` field of
the reading that **produced** the row — its origin lane — never from its
`source_repo`: a repository reading that cites a hub file leaves `source_repo ==
fleet-manager` while the truth is the satellite's. The first cut keyed on
`source_repo` and stamped the hub ledger on 12 of 183 rows (Codex round 1);
8 of the 12 were masked because both ledgers happen to be named
`docs/current-state.md`, and 4 changed value on the fix (two substrate-kit rows
→ `control/status.md`, one estate-backups row, one shiftlife row). Area lanes
are the hub's own reading, and for fleet-manager — read by five area lanes that
record no such field — the value is the file that declares itself the ledger
(a reading's JSON `null` stays an empty, reportable cell — round 2 caught the
first cut turning it into the word `None`): `docs/current-state.md` opens
with `Status: living-ledger` and *"It carries live hub state"*, and the boot
file's deep read path calls it *"the living ledger"*. The constant and its
citation are in the generator, not in prose here.

`MEASURED`: the regenerated manifest has **183 of 183 rows carrying a value**,
and a cell-by-cell comparison of the 22 pre-existing columns against the
committed file before regeneration finds **0 differing cells** (`git diff
--stat` shows every line changed because every line gained a column). Values
are the readers' verbatim text — `docs/current-state.md` plain for 5 repositories
(couch-legend, creator-kit, sim-lab, spider-swing, websites) and the hub, `control/status.md` for substrate-kit and product-forge,
`README.md (Status section); CLAUDE.md for the 12 invariants` for spider-bot,
`docs/repos/estate-backups/README.md (in fleet-manager; …)` for estate-backups,
and annotated `current-state.md` pointers for 4 (idea-engine, shiftlife, superbot, superbot-next) —
5 + 2 + 1 + 1 + 4 = 13 readings. (An earlier draft said "eight" plain, a tally error.) Fixture: `test_manifest.py` asserts the column, its
value for a reading that names one, the empty cell for a reading that does not,
and — with a fixture ledger the hub cannot share (`STATUS.md`) — that a row a
reading emitted about a hub file carries the reading's ledger.

## 4 · The overclaim schema — a consumer, and the residual decomposed

The baseline's § 12 item 11 says the 63 unmatched certainty overclaims are a
schema defect: free text with no subject. Two things done here, neither of which
changes the committed manifest (the retained journals hold only the free-text
form, and the builder still applies it exactly as before — 10 rows):

1. **The next run's schema has a consumer.** `build_manifest.py` reads
   `overclaimed_certainty` entries of the form `{"subject": …, "reason": …}` and
   joins them **exactly** on the case-folded subject within the audited reading —
   no threshold, no heuristic — publishing the refuter's reason in `blocker` as
   `adversary (by subject): …`. The module docstring states the required shape.
   An object with a missing or blank subject — the schema defect the object form
   exists to expose — is counted and printed as malformed, and so is an object
   whose subject reaches **no row of its reading** (a typo, a stale subject): both
   are a lost dissent, and the builder refuses success over either unless
   `--allow-partial` is passed (the first cut dropped the blank case silently,
   Codex round 1; the second covered only the blank case, round 2). Fixture: the
   aggregation journal carries one subject-form overclaim on a `MEASURED` item
   (killed through the rule's overclaim branch, asserted), one free-text flag that
   names nothing (counted, never applied, asserted), one object with no subject
   and one with a typo'd subject (each counted, neither reaching the near-miss
   row, and the strict build refused — all asserted).
2. **"63 of 73" was two numbers.** The builder now prints the split, read from
   the same data: **59 flags reach no row** by any join — the schema defect —
   and **4 reach only rows whose certainty is not `MEASURED`/`OWNER`**, where the
   rule declining to kill is the design, not a miss. The residual to fix by
   schema is 59, not 63.

The refute lane's *prompt* lives in the workflow script of whichever session
runs the next fleet, not in this tree; the consumer and the docstring are the
committed half. `fleet-preflight` § 1's aggregate contract already requires that
every collected field be read by the rule or declared report-only, which is the
check that would have caught the free-text form — this is that rule applied one
field earlier.

## 5 · What this leaves for the seed session, exactly

- **Re-read spider-bot's six rows** — its repository took 27 commits after the
  audit (the AI-operations tranche) and every row it contributed cites a file
  that changed; the one survivor is a `distill` of `.railway/railway.ts`.
- **Re-read the three uncheckable survivors** (§ 2) with a path and a commit
  each; regenerate.
- **Re-anchor the 84 PR-branch verification points** to `049b112` where the
  object comparison permits (§ 2) — one edit pass over the journals, one
  regeneration, `row_delta.py` before and after as the proof.
- **Read the two moved `carry` rows' files at seed time**, not from the audit.
  `row_delta.py --out` at launch is the command; the handoff table in the
  baseline's § 11 now names it.
- **The kit release cut** is still the gate on the seed itself (`OQ-KIT-V1-21-RELEASE`
  in `docs/owner-queue.md`, owner-paced) — untouched here, as scoped.
- **Untouched and still as the baseline states them:** the cold-session test's
  leak (§ 10), the manifest covering 13 repositories plus the hub (§ 12 item 12),
  the `only_source_is_hub_summary` flag being near-inert on live data (item 13),
  and `carry` rows over the successor's length cap (item 14).

## 6 · Verify

Every command below was run at the head this record was written at; exit codes
are the process's own, never read after a pipe.

```
python3 tools/estate_baseline/delta.py --anchors docs/findings/data/2026-09-04-estate-truth-baseline/anchors.tsv --out <tsv>   → exit 0, 28 rows, 5 CHANGED_REAUDIT at 19:02Z
python3 tools/estate_baseline/test_delta.py <that tsv>                                                                    → exit 0, 11/11
python3 tools/estate_baseline/build_manifest.py --journal run1 --journal run2 --journal run3-repos --classification … --out docs/planning/2026-09-04-estate-seed-manifest.csv
                                                                                                                          → exit 0, 183 rows, 119 / 64
python3 tools/estate_baseline/row_delta.py --manifest … --classification … --delta <tsv> --out data/…/row-delta.tsv        → exit 0, 339 calls, 98 / 18 / 3 over the 119 survivors
python3 tools/estate_baseline/test_row_delta.py                                                                           → exit 0, 9/9 live controls, 18 provenance shapes, 5 binding cases
python3 tools/estate_baseline/test_manifest.py                                                                            → exit 0, 4 cases; the strict build refused over the malformed object
python3 tools/estate_baseline/seed_rule.py                                                                                → exit 0, 0 unread / 0 undefined, 14 fixtures
```

The tools remain advisory — wired into no gate — as `tools/README.md` says; a
seed session runs them at launch.
