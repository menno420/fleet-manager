# What changed in your seat prompts: v3.4 → v3.5 → v3.6 (one page)

> **Status:** `reference` — owner-skimmable summary of the 2026-07-13 night's
> two prompt folds (v3.5 = PR #151 stage-1; v3.6 = stage-2, this doc's PR).
> Full detail per version: [`per-project/README.md`](per-project/README.md)
> changelog sections. Nothing here changes mechanics — the v3.3
> one-file-per-seat composition is untouched; these folds add doctrine your
> orders already imposed and one new seat.

## The one-line version

Your seats now carry, baked into every startup + Custom Instructions: **never
wait for you** (Q-0271), **open PRs stay open** (your 2026-07-13 standing
order), **they may read the whole fleet** (Q-0272), **they know what the hub
chat is for** (Q-0273 `VENUE:hub`), **they boot-read the grounding file**
(Q-0274) — and **Curious Research is seat 9** with registry-grade prompts.

## v3.5 (stage-1, PR #151) — rider + skills

| What | Where it landed |
|---|---|
| **AUTONOMY RIDER (Q-0271):** owner absent = normal; silence = consent = done; the OWNER-ONLY list is the sole park class (queue-and-continue); uncertainty → SIM-REQUEST; never-wait ≠ bypass CI | shared DOCTRINE section, all startups |
| **Seed skills (Q-0273):** chase-references (resolve every reference before acting) + prep-owner-steps (deep link first, paste-ready blobs, one sitting) | shared DOCTRINE + CI `skills` entry |

## v3.6 (stage-2, this PR) — the completion fold + seat 9

| What | Where it landed |
|---|---|
| **OPEN PRs STAY OPEN — now the STANDING default** (was night-only in your direct orders): land on green, never merge-chase, stack follow-ons on the open head (base noted in the PR body); you sweep open PRs from the hub | AUTONOMY RIDER sentence + CI BOOT TRIAD entry |
| **FLEET READ (Q-0272):** every repo read-only standing (pml DARK); route = superbot `docs/fleet-reading-path.md`; live state = `fleet_status.py` | new shared DOCTRINE paragraph + CI Routes footer |
| **VENUE MODEL (Q-0273):** hub chat ≠ PM seat ≠ Project seats; merge/destructive-shaped asks tagged `VENUE:hub` for you to run in the hub | new shared DOCTRINE paragraph + CI six-field-ask line |
| **GROUNDING (Q-0274):** every seat boot-reads superbot `docs/owner/fleet-grounding.md` §0–§1 + its own § + §10 | shared DOCTRINE + each seat's Orientation route |
| **NINTH SEAT — Curious Research:** your founding pair conformed to registry format (stateless; the night program was not baked in); failsafe `20 */2`; registry dir at v1 | `per-project/curious-research-*.md` + `projects/curious-research/` |

## Why "v3.6", not "v3.5 stage-2"

The stamp line is the drift check — a body-changing re-sync must bump the
generation so a stale paste is detectable by quoting it. Stage-2 changed
every body → next number. The kit-fence wiring formerly penciled as v3.6
becomes the v3.7 pending item (still blocked on an unreleased kit).

## What you may want to do (all optional — nothing blocks)

- **Re-paste when convenient:** each seat's Custom Instructions + startup
  from `projects/<seat>/{instructions,coordinator-prompt}.md` (v3.6 bodies).
  Seats keep working on v3.5 pastes; the folds ride ORDERs meanwhile.
- **Curious Research:** its registry prompts are ready at
  `projects/curious-research/` whenever you re-paste that Project.

All CI pastes verified ≤ 8,000 chars AND bytes (worst seat: 7,999 bytes);
checker green: `python3 docs/prompts/v3/tools/regen_b_files.py`.
