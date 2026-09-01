# fleet-manager measured at `cb3fc9a` (2026-09-01)

> **Status:** `audit` · tier **RECORD** · `MEASURED` 2026-09-01 on a fresh clone at
> `cb3fc9a` by the first Fable 5.1 session, on the owner's laptop. Every number
> came from a command run that session; percentages are of tracked files unless
> stated. Written as evidence for the successor proposal
> ([`../planning/2026-09-01-estate-structure-proposal/`](../planning/2026-09-01-estate-structure-proposal/README.md)).

## Size and speed

| Measure | Value |
|---|---|
| Tracked files | 1,246 (1,083 Markdown) |
| Markdown volume | 142,984 lines · 10.3 MB |
| Commits since the first one (2026-07-09) | 1,036 |
| PRs merged since 2026-08-01 | 347 — about eleven a day |
| Merged PRs per day, last five days | 11 · 16 · 12 · 13 · 12 |

A repo that moves eleven PRs a day cannot be read from a clone that is a few
hours old. That is the stale-clone incident in one number.

## Where the files are

| Area | Files | Tier by `docs/MAP.md` |
|---|---|---|
| `.sessions/` | 472 | record |
| `docs/` | 403 | mixed — 111 findings · 48 prompts · 35 planning · 32 owner-comments · 65 loose files at the top |
| `owner/` | 93 | core (the intent workbooks, 86) |
| `projects/` + `control/` + `telemetry/` + `registry/` + `templates/` | 91 | record, seat-era |
| `.claude/` + `.substrate/` + `scripts/` + `tools/` | 153 | apparatus |

By a path-based split of the MAP tiers: **record ≈ 832 files (67 %)**,
apparatus 163 (13 %), owner 93 (7 %), live documents 158 (13 %). The living
core is roughly 250 files. The other thousand are memory.

## The long files

| Lines | Markdown files |
|---|---|
| ≤ 50 | 299 |
| 51–150 | 550 |
| 151–300 | 140 |
| 301–600 | 67 |
| 601–1,200 | 20 |
| > 1,200 | 7 |

The seven over 1,200: `owner/intent-workbooks/ALL-IN-ONE.md` (2,932, a
generated bundle), `docs/owner-queue.md` (2,161), `docs/CAPABILITIES.md`
(2,136), `docs/fleet-triage.md` (1,823), the full-read audit (1,785), the
2026-07-10 night review (1,597), `control/inbox.md` (1,595). Two of those
seven are live surfaces an agent is told to "read whole".

## What the mandatory reading order costs

The README names six reads. Read four is three documents. Measured bytes:

| Read | Bytes |
|---|---|
| `README.md` + `.claude/CLAUDE.md` | 6,927 + 28,456 |
| `docs/intent.md` | 12,902 |
| `docs/current-state.md` | 35,026 |
| consolidation program | **160,880** |
| roadmap + fresh-start redirect | 32,821 + 40,825 |
| `docs/fleet-account-2026-07-26.md` | 20,238 |
| `docs/owner-reflection-2026-07-21.md` | 14,210 |
| **Total** | **≈ 352 KB ≈ 88,000 tokens** |

Nearly half of a 200k context window goes to orientation before the first
task step. The consolidation program alone is about 40,000 tokens; it holds
71 lines over 400 characters and one of 7,393 (its §7 ledger is an
append-only table). This is the "immensely long files" complaint made exact,
and it is the single strongest argument for the successor's boot-path budget
in file 03.

## Two hygiene facts worth knowing

- `.substrate/guard-fires.jsonl`, the kit's telemetry ledger, is **24 MB and
  37,499 lines, committed in the tree**, touched by 250 commits since
  2026-08-01. It is 40 % of the 59 MB working tree. Every clone carries it.
- The doc-routing hook table (`doc-routes.json`, 72 routes) and the eight hook
  scripts exist in **one repository of twenty**. The kit ships no routing.

## Where the mistakes come from — the record already says

The estate has measured its own errors more carefully than most teams do.
The three sources that matter for the successor design:

1. **`docs/traps.md`** — eight registered traps, seven delivered by a route,
   one with a deterministic checker. The newest, TRAP-008 (a label read as its
   contents), had six instances in one session yesterday, one of them inside
   the document describing the trap.
2. **`docs/findings/2026-08-29-estate-agent-error-audit.md`** — 328 prose-only
   rules against 172 mechanical enforcers across 20 repos; seven error classes
   found independently by session cards and by external review: a guard never
   seen red · a correction that leaves copies standing · green read as
   verification · a verdict about a file never re-opened · a count from
   memory · enforcement words for nothing implemented · the companion record
   the diff owes. Widest of all (13 repos): the missing companion record.
3. **`docs/findings/2026-08-08-why-rules-dont-bind.md`** — 116 statements of
   the verify-first rule across 66 files caught 0 of 16 incidents. The owner
   asking a question caught 5.

And the finding that redirects effort: **nothing in yesterday's six misses was
unfindable.** The name of the successor sat in three places; the misread cell
was found on the first grep. Structure fixes the "never opened" half and the
"read past the qualifier" half only when it also shortens what is opened.
That is why file 03 caps file length instead of only naming folders.

## What already works, and must be kept

The areas that grew against a declared contract stayed navigable: `.sessions/`
(dated cards, a grammar README), `docs/repos/<name>/` (one folder per repo,
fixed filenames), `docs/owner-comments/<repo>/{unconsumed,consumed}/` (state
in the path, moved by a tool, red if folder and header disagree),
`docs/planning/` (dated, indexed), the generated `owner/README.md`. The
successor generalises those four patterns; it does not start from zero.

## The owner-profile duplication, measured across the estate

The 2026-09-01 duplication-map record on the laptop hub said `docs/owner-profile.md`
is "copied near-verbatim into essentially every one of the 27 other repos".
Measured by git blob SHA and byte size across all 28 repositories the same day
(`gh api repos/menno420/<repo>/contents/docs/owner-profile.md --jq '.sha, .size'`):

| What is there | Repositories |
|---|---|
| fleet-manager's own 5,922-byte file | 1 |
| A substrate-kit generated stub, 723–1,948 bytes, two repo-specific slots filled | 17 |
| No `docs/owner-profile.md` at all | 10 |
| A copy of fleet-manager's file | **0** |

So the duplication is the kit's `adopt` template, and the fix is one template
change — a pointer to the hub plus the repo's own two slots — not 26 edits.
