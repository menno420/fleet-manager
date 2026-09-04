# 2026-09-04 — the `estate` seed's own prerequisites: row-level source drift, a provenance validator, the canonical-state column

> **Status:** `in-progress` — **What is about to happen:** the merged estate truth
> baseline (fm #1020, verdict `PARTIAL`) is re-read at HEAD and the seed-time
> requirements its § 11/§ 12 name are worked inside fleet-manager — not the
> seed itself (gated on the kit release cut, [D-0025] + the build order), not
> substrate-kit (another session's K1–K5), not E1 (the program's NOW pointer,
> the owner's). First step, already run: the delta against `anchors.tsv`; the
> moved set is the same four repositories the handoff named (couch-legend,
> fleet-manager, spider-swing, substrate-kit) — and by 19:02Z a fifth,
> spider-bot, had joined it (finding § 1). Next: a row-level instrument
> that says for each manifest row whether the FILE it cites moved since the SHA
> it was verified at (the handoff's "every carry row's source SHA" re-check,
> made mechanical), which doubles as the path/instant provenance validator
> § 12 item 10 says is missing; the `canonical_state_source` column § 12 item
> 11b names as a seed-time requirement, added through the generator and the
> manifest REGENERATED; the refute lane's overclaim schema given a consumer
> that joins on a named subject (§ 12 item 11).

- **📊 Model:** withheld · xhigh · feature build
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01DwEAXW4q4eT8v4nPqJbTq6](https://claude.ai/code/session_01DwEAXW4q4eT8v4nPqJbTq6) · "Estate truth baseline review"

## What shipped

All in PR fm #1036, commits `dd9defa` (the work), `8d5f8b7` and `bbda8ce` (inferred
sentences in the finding replaced by measured ones), the Codex round-1 fixes, and the
merge of `origin/main` at `17a532b` (`1081f53`, `.substrate/guard-fires.jsonl` resolved
as the deduplicated chronological union: 46,719 ours · 46,833 theirs · 47,037 union);
this card born-red at `9a2fcb0`.

- **`tools/estate_baseline/row_delta.py`** — the ROW-level drift instrument: for every
  manifest row, the git object at each cited path at the row's verification SHA versus the
  live default-branch tip; provenance it cannot resolve is published `UNCHECKABLE:<reason>`,
  which is the path/instant validator the baseline's § 12 item 10 lacked. Reads the
  ` + `-joined, repository-qualified and API-reference forms the corpus actually holds
  (round 1). Plus **`test_row_delta.py`**: 17 provenance shapes, 10 verification forms, 5
  path cases, 6 precedence cases, and 9 live controls (3 positive, 4 negative — three of
  them unmoved files inside MOVED repositories — 1 uncheckable, 1 api-reference).
- **`tools/estate_baseline/build_manifest.py`** — the `canonical_state_source` column
  (appended; from the reading that PRODUCED the row — its origin lane, never its
  `source_repo` — the hub from the file that declares itself the ledger); a
  consumer for the subject-bearing overclaim schema (exact join, in the docstring as the
  next run's contract; a malformed object with no subject is counted and refuses the
  strict build); the overclaim residual decomposed (59 reach no row · 4 reach rows
  outside MEASURED/OWNER · 10 applied). **`fixtures/journal-aggregation.jsonl` +
  `test_manifest.py`** extended for all of it, including a cross-source row with a
  ledger the hub cannot share.
- **`docs/planning/2026-09-04-estate-seed-manifest.csv`** — REGENERATED, not edited: 183
  rows, 22 prior columns byte-identical cell-for-cell, 183/183 carry the new column.
- **Evidence** — `docs/findings/data/2026-09-04-estate-truth-baseline/row-delta.tsv` (the
  row-level snapshot, 2026-09-04T18:59Z) and `delta-rerun-2026-09-04.tsv` (the delta re-run
  at 19:02Z; fleet-manager and spider-bot each took one commit in the three minutes between).
- **[The follow-on finding](../docs/findings/2026-09-04-estate-seed-prerequisites.md)** —
  what moved at row level (18 of 119 survivors — 17 fleet-manager rows over ten files, one
  spider-bot `distill`; two `carry`; the three satellite survivors' files unmoved although
  their repositories moved; 3 survivors UNCHECKABLE, named; 84 of 119 verification SHAs are
  fm #1020 PR-branch commits not on `main`), the column, the schema consumer, and § 5's
  exact list of what the seed session still owes — spider-bot's six rows now first on it.
- **The baseline finding annotated** where this changes what it says: § 8 (the column
  sentence made count-free — it read "twenty-one" over a 22-column file), § 11's re-check
  table (the `carry`-SHA row now names the command), § 12 items 10 / 11 / 11b (validator
  half done · consumer built · column added) and 13 ("123 survivors" → 119).
- **Index rows** — `docs/findings/README.md` regenerated (`gen_findings_index.py`, 78 listed)
  with the two owed descriptions authored (fm #1020's and this one's); `tools/README.md`
  and `docs/planning/README.md` rows updated.

Layer-2 handoff: null (fleet-manager itself; the four moved satellites were read through
the API only — compare and contents endpoints — and no repository's own thread state changed).

## Verify

Real exit codes, each read directly (never after a pipe):

```
python3 tools/estate_baseline/delta.py --anchors …/anchors.tsv --out <tsv>      exit 0 · 28 rows · 4 CHANGED at ≈18:27Z, 5 at 19:02Z (spider-bot joined)
python3 tools/estate_baseline/test_delta.py <tsv>                                exit 0 · 11/11 controls
python3 tools/estate_baseline/build_manifest.py --journal ×3 … --out <manifest>  exit 0 · 183 rows · 119 / 64 · 22 prior columns: 0 differing cells
python3 tools/estate_baseline/row_delta.py … --out data/…/row-delta.tsv          exit 0 · 337 API calls · 98 / 18 / 3 over the 119 survivors (18:59Z)
python3 tools/estate_baseline/test_row_delta.py                                  exit 0 · 9/9 controls, snapshot-relative · 17 provenance shapes
python3 tools/estate_baseline/test_manifest.py                                   exit 0 · 4 cases, 3 kill / 1 survival · strict build refused over the malformed object
python3 tools/estate_baseline/seed_rule.py                                       exit 0 · 0 unread / 0 undefined · 14 fixtures
python3 tools/gen_findings_index.py --check                                      exit 0 · 78 listed, current
python3 bootstrap.py check --strict --added-card <this card>                     exit 1 · sole findings: this card's born-red hold (+ the preflight lane echoing it)
```

The `stamp` checker caught one real finding before commit — this finding cited decisions
as `D-00NN` tokens, which stamps each at a second home; rewritten as
`decision NN in docs/decisions.md`, 0 tokens remain.

## Review

**Codex round 1 (on `b4fc8fe`): 5 findings — 5 conceded (2 P1, 3 P2), 0 refuted, 0 open.**
Each verified against the committed files before acting, each fixed and re-measured:
`[conceded]` P1 a subject-form overclaim object with no subject was dropped silently → counted,
printed, strict build refuses · `[conceded]` P1 the column was keyed by `source_repo`, stamping
the hub ledger on 12 rows (8 masked by a shared filename, 4 changed value) → keyed by the
producing reading, fixture with a ledger the hub cannot share · `[conceded]` P2 header
validation skipped on an empty manifest → validated from `fieldnames`, empty manifest refused ·
`[conceded]` P2 fresh-file negative controls accepted `UNCHECKABLE` → they fail it ·
`[conceded]` P2 the parser read ` + `-joined, repo-qualified and API-reference cells as
narration or not-found (7 killed cells) → parsed, qualified, named; snapshot re-taken.
Round 2 requested on the head carrying these fixes; the flip waits for its answer.

## ⚑ Decide-and-flag

- **⚑ The seed still waits on the kit release cut** — `OQ-KIT-V1-21-RELEASE` in
  `docs/owner-queue.md` is unchanged by this session; K1–K5 are on kit `main`, v1.21.0 is
  still the newest published release (re-read at HEAD). Nothing here changes that gate.
- **⚑ 84 of 119 surviving verification SHAs are squash-merged PR-branch commits** — they
  resolve today, are not ancestors of `main`, and GitHub does not promise to keep them.
  The re-anchor to `049b112` is mechanical and per-row verifiable (finding § 2) but edits
  journal inputs, so it is left for the seed session to do in one regeneration with the
  three uncheckable re-reads. Decision needed from nobody — it is a sequencing choice; flagged
  so it is not lost.

## 💡 Session idea

Move the shape check to where the shape is written: the reader schema's `source_path` and
`verification_point` should be two STRUCTURED fields (a list of paths; `sha@instant`)
validated at collection time by `row_delta.paths_of` / `shas_of`, so a narration such as
`(live PR list)` is refused by the agent's own output contract instead of surviving the
rule and being repaired one layer down. Same shape as the overclaim-subject fix in this PR:
the aggregation defect keeps being a schema defect one field earlier.

## ⟲ Previous-session review

`.sessions/2026-09-04-estate-truth-baseline.md` (fm #1020). Its handoff prompt was
accurate where it could be checked: the first command ran as written and returned the
same four moved repositories; every path it named existed at HEAD; the verdict and the
DECIDED / REJECTED lists matched the finding. Three things it got wrong, all counts, all
small, all now fixed in place: § 8 said "twenty-one columns" over a 22-column file, § 12
item 13 said "123 survivors" beside a § 8 table that said 119, and its own card says
"21 columns". The lesson it recorded — a value nobody retypes cannot be mistyped — is the
one this session applied by reading every number off the committed files, and the two
sentences this session still got wrong were the two it inferred from a heading list and a
mental tally rather than measured (finding § 2, both corrected in `8d5f8b7`). Its most
useful design choice was publishing killed rows with the branch that fired: the
row-level instrument could classify all 183 rows, killed included, because of it.
