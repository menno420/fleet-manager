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
