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

`MEASURED` 2026-09-04 ≈ 18:27Z — `delta.py` against the committed
`anchors.tsv`, output retained as
[`data/2026-09-04-estate-truth-baseline/delta-rerun-2026-09-04.tsv`](data/2026-09-04-estate-truth-baseline/delta-rerun-2026-09-04.tsv);
`test_delta.py` over that file: 7 unit cases, 11 of 11 live controls readable,
exit 0.

**The moved set is unchanged from the handoff:** four repositories read
`CHANGED_REAUDIT` — couch-legend, fleet-manager, spider-swing, substrate-kit —
and the other twenty-four read exactly as the audit left them (9
`ARCHIVED_OR_NONACTIVE`, 15 `UNCHANGED_REUSABLE`). Commits since the SHA each
audit read: fleet-manager 16, couch-legend 3, substrate-kit 2, spider-swing 1
(couch-legend took a fourth, `254531ba`, at 18:36:58Z — after this file was
written and before the row-level snapshot in § 2 was taken, which is why the
two committed files name different couch-legend tips).

What those commits touched, from `GET …/compare/{base}...{head}` per repository:

| repo | commits | files | touches a file a surviving manifest row cites? |
|---|--:|--:|---|
| fleet-manager | 16 | 90 | **yes** — see § 2 |
| couch-legend | 3 | 88 | no — `README.md` (the one surviving row's source) is not among them |
| substrate-kit | 2 | 31 | no — `docs/NEXT-TASKS.md` is not among them |
| spider-swing | 1 | 6 | no — `docs/current-state.md` is not among them |

A repository-level delta says "re-audit"; the file-level answer for three of the
four is "nothing this manifest relies on moved". That gap is the reason for § 2.

## 2 · What moved at ROW level — the instrument, and what it says

**The instrument.** `tools/estate_baseline/row_delta.py` takes the manifest and,
for every row, (a) classifies the SHAPE of its provenance, (b) resolves the SHA(s)
in `verification_point` against the row's source repository, taking the
latest-dated one where a row names a reading and a later re-read, and (c)
compares the git object at each cited path — a blob for a file, the listing for
a directory — at that SHA against the same path at the live default-branch tip.
Identical objects mean the content the reader verified is the content that is
live. The row status vocabulary is in the script's docstring; the rule of
precedence is that one moved path outranks any number of unchanged ones,
because a `carry` copies bytes.

Fixtures: `tools/estate_baseline/test_row_delta.py` — 9 provenance shapes and
10 verification-point forms taken from live cells, 5 path cases (4 kill /
1 survival) including the branch that must not fire, 6 row-precedence cases,
and live controls: 3 positives (fleet-manager rows citing `docs/current-state.md`,
`docs/ESTATE.md`, `docs/decisions.md` — all modified in the sixteen commits),
4 negatives (the three satellite survivors above plus shiftlife, which has not
moved since 2026-07-27) and 1 uncheckable control. **8 of 8 controls correct,
exit 0** against the committed snapshot. The three satellite negatives are the
discriminating case: their repositories moved, their files did not.

**The snapshot.** `MEASURED` 2026-09-04T18:38Z, 331 API calls, exit 0 —
[`data/2026-09-04-estate-truth-baseline/row-delta.tsv`](data/2026-09-04-estate-truth-baseline/row-delta.tsv),
183 rows. Read from the file with `csv.DictReader`:

| | all 183 rows | the 119 survivors |
|---|--:|--:|
| `SOURCE_UNCHANGED` | 130 | **99** |
| `SOURCE_MOVED` | 19 | **17** |
| `SOURCE_NOT_FOUND` | 1 | 0 |
| `UNCHECKABLE` | 33 | **3** |

**The 17 survivors whose source moved are all fleet-manager rows**, and the
files behind them are ten:

`docs/current-state.md` · `docs/ESTATE.md` · `docs/decisions.md` ·
`docs/owner-queue.md` · `docs/CAPABILITIES.md` · `docs/traps.md` ·
`docs/planning/2026-07-26-consolidation-program.md` ·
`docs/planning/2026-09-01-estate-structure-proposal/` ·
`docs/planning/2026-08-21-game-community-bot/` · `tools/estate_baseline/seed_rule.py`

By disposition: 6 `archive_only` (the copy in the archive would be of an older
version — acceptable by that verb's own meaning, and the seed should copy at
seed time, not from the audit), 9 `distill` (the distillation must be written
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

The 30 uncheckable killed rows split 17 with no path in `source_path` — 9 the
disposition judges' synthesised `(killed before a source was recorded)` and 8
readers' narration (`(live PR list)`, `live API: pulls?state=open`,
`releases API (tag …)`, `docs/repos/ (absence) + …`) — and 13 with no SHA in
`verification_point` (`live-api@…`, `live-file@…`, `live-repo-tree@…`,
`local-read@…`). The one `SOURCE_NOT_FOUND` is a killed sim-lab row whose
`source_path` reads `git/trees`. Counted from the snapshot joined to the
manifest on (subject, source_repo).

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
the reading that audited the row's `source_repo` (13 repositories), and for
fleet-manager — which was read by five area lanes that record no such field —
from the file that declares itself the ledger: `docs/current-state.md` opens
with `Status: living-ledger` and *"It carries live hub state"*, and the boot
file's deep read path calls it *"the living ledger"*. The constant and its
citation are in the generator, not in prose here.

`MEASURED`: the regenerated manifest has **183 of 183 rows carrying a value**,
and a cell-by-cell comparison of the 22 pre-existing columns against the
committed file before regeneration finds **0 differing cells** (`git diff
--stat` shows every line changed because every line gained a column). Values
are the readers' verbatim text — `docs/current-state.md` for eight repositories
and the hub, `control/status.md` for substrate-kit and product-forge,
`README.md (Status section); CLAUDE.md for the 12 invariants` for spider-bot,
`docs/repos/estate-backups/README.md (in fleet-manager; …)` for estate-backups,
and annotated `current-state.md` pointers for superbot, superbot-next,
shiftlife and idea-engine. Fixture: `test_manifest.py` asserts the column, its
value for a reading that names one, and the empty cell for a reading that does
not.

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
   Fixture: the aggregation journal now carries one subject-form overclaim on a
   `MEASURED` item (killed through the rule's overclaim branch, asserted) and one
   free-text flag that names nothing (counted, never applied, asserted).
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
python3 tools/estate_baseline/delta.py --anchors docs/findings/data/2026-09-04-estate-truth-baseline/anchors.tsv --out <tsv>   → exit 0, 28 rows
python3 tools/estate_baseline/test_delta.py <that tsv>                                                                    → exit 0, 11/11
python3 tools/estate_baseline/build_manifest.py --journal run1 --journal run2 --journal run3-repos --classification … --out docs/planning/2026-09-04-estate-seed-manifest.csv
                                                                                                                          → exit 0, 183 rows, 119 / 64
python3 tools/estate_baseline/row_delta.py --manifest … --classification … --delta <tsv> --out data/…/row-delta.tsv        → exit 0, 331 calls
python3 tools/estate_baseline/test_row_delta.py                                                                           → exit 0, 8/8
python3 tools/estate_baseline/test_manifest.py                                                                            → exit 0, 4 cases
python3 tools/estate_baseline/seed_rule.py                                                                                → exit 0, 0 unread / 0 undefined, 14 fixtures
```

The tools remain advisory — wired into no gate — as `tools/README.md` says; a
seed session runs them at launch.
