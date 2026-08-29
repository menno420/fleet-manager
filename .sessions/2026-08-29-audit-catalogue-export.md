# 2026-08-29 — the fleet's unread output, rescued before the container took it

> **Status:** `in-progress` — born-red. Exporting the 284 candidate patterns and
> 20 repository censuses the audit harvested and never used.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** harness policy forbids a model identifier in a pushed
  artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container

## Mission

Owner ask, live, with the session near compaction: *"review what your fleet has
produced and if there's anything else there that we could use… I want to make
sure that the valuable parts of this session are not lost."*

**There was, and it was about to be.** The audit
([fm #967](../docs/findings/2026-08-29-estate-agent-error-audit.md)) used
roughly **ten** patterns. The fleet produced **284**, plus **20 per-repo
instruction censuses** and 2,875 classified incidents — all sitting in
`harvest-cache.json` in a container-local scratchpad, referenced by no committed
artifact. The retrospective already records that this container is the **third**
of the session and that the earlier runs' transcripts are gone; the same fate
was queued for this.

## Shipped

- `docs/findings/data/2026-08-29-agent-error-patterns.jsonl` — **284 rows**,
  one per candidate pattern, with cites, counts, gap class, fix family and
  proposed fix. **118 are `high` severity across ≥3 repositories.**
- `docs/findings/data/2026-08-29-repo-instruction-census.jsonl` — **20 rows**,
  one per repository: instructions, enforcement by kind, prose-only rules, kit
  divergences, biggest gap, portable lesson.
- `docs/findings/data/README.md` — how to read them, `jq` cuts that work, and
  **the loud caveat that these are candidates**: the panel rejected 7 of 284, so
  a row here has survived almost nothing.

## Why this is data, not a finding

Every limit the retrospective records applies to every row: the panel's 97.5 %
pass rate, the 89/10 corpus composition, the ≤5 % cross-corpus contamination,
counts as observed mentions with no dedup measured. The README says so before it
says anything else, because the risk of a committed catalogue is that its rows
get quoted as established.

## Codex round 1 — 7 P2 findings, all `[conceded]`

Requested on `5111dd4a`; the review landed as an **issue comment**, not inline
review comments. My first check read `reviews=0 inline=0` and concluded nothing
had arrived — the third mis-scoped-matcher false null of the day, and the reason
[fm #976](https://github.com/menno420/fleet-manager/pull/976) exists.

| # | finding | disposition | fix |
|---|---|---|---|
| 1 | Pattern rows drop the panel outcome, so the 7 rejected candidates are unfindable | `[conceded]` | Recovered `survives` · `refuter_count` · `already_covered_by` · `panel_run` from the retained run JSON and joined onto all 284 rows (284/284 matched by name). Tally `MEASURED`: refuters 0 on 226 · 1 on 51 · 2 on 7. |
| 2 | Census `repo` field carries paths and caveats, so `select(.repo=="websites")` silently misses rows | `[conceded]` | Split into canonical `repo` + `full_name` + `aliases` + `scope_notes` on 3 rows; all 20 ids now canonical and unique. |
| 3 | L116 records `repo_count: 4` against 5 listed repos | `[conceded]` | Corrected to 5 in both the field and `date_span`. Swept all 284 — it was the only such row. |
| 4 | The owner-attribution lane's premise is void and propagates into 24 rows | `[conceded]` | Archival correction at the head of `02-…js` (script left verbatim), `owner_flagged_premise: "VOID"` on every row carrying the key, and a README paragraph. |
| 5 | Census sampling limits absent from the data README | `[conceded]` | New section: one reader per repo, filtered snapshots where `scope_notes` says so, some mechanisms inferred from docs. `enforcement` reads as a floor. |
| 6 | Judge verdicts carry no link to the draft they judged | `[conceded]` | Reconstructed from the run ranking and **proved unique** by exhaustive search over partitions matching per-draft mean, catches and verdict multiset. `draft_name`/`draft_index`/`draft_mean_score`/`association_note` on all 9. |
| 7 | The judges' `MEASURED TELEMETRY` block overstates concurrency | `[conceded]` | Archival correction at the head of `03-…js`. This is the sharpest of the seven: the skill those judges were shaping exists to stop a figure entering a record as measured with its scope stripped, and it reached them inside the skill's own design prompt. |

**Zero `[survived]`.** Every finding was checked against the data before it was
accepted; none needed arguing.

### Two things the fixes turned up that Codex did not raise

- **`instance_count` ≠ `instances | length` on 32 rows** (row 1: 28 claimed, 16
  listed). The count is the lane's shard tally, the array is what it quoted.
  Only the array is checkable; documented in the data README with a `jq` cut.
- **The workflows README's "`preflight` angle 6.5" was one judge's individual
  score**, not the draft's mean (6.83). Found by the F6 reconstruction.

### One near-miss worth recording

Writing up F1 I typed a refuter tally of 155/122/7 — extrapolated from the
second run's numbers without reading the first. The measured tally is
**226/51/7**. It was caught by verifying before commit, which is the right
order, but it is the fourth instance today of *asserting a count from a subset*.
The number would have shipped inside the very PR whose subject is unverified
counts.

## Verify

- Row counts re-derived at export (284 / 20), not carried from the chat.
- `python3 bootstrap.py check --strict` → real exit code, no pipe.

## ⟲ Previous-session review

Previous card: [`2026-08-29-fleet-orchestration-retro.md`](2026-08-29-fleet-orchestration-retro.md)
(fm #971, merged).

**Held up** — its measurements were re-derived rather than recalled, and its one
`[partial]` was closed by testing the assumption underneath it.

**What it missed, which this card closes:** it recorded how the fleet ran and
what it cost, and never asked what the fleet had *produced* that nobody read.
The retrospective's §5 says "the fan-out produces raw material" — and the raw
material was left in a directory the same document notes is already-gone for
earlier runs. **A session can measure its own waste precisely and still not
notice the unread output beside it.**

## 💡 Session idea

**A close-time check for unreferenced fan-out output.** The journals and task
outputs of any workflow are enumerable, and so is whether the session's diff
cites them. A session that ran a fleet and committed nothing pointing at its
results is discarding work it paid for — mechanically detectable, no judgement
needed.

**Why an idea and not an action:** it is a new gate lane in every adopter, which
OD-24 §3 reserves to the owner, and OD-26 §13 puts mechanisms behind the revised
plan. It also belongs with `fleet-preflight` as its close-time sibling — the
skill covers the hour *before* launch and nothing yet covers the hour after.
