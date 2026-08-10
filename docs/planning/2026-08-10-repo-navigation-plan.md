# The browsable repo — navigation, mandatory reading, and tier labels

> **Status:** `plan` — owner-directed 2026-08-10, live, during the full-read
> audit session (fm #839/#840). This file is the durable design so the work
> survives session compaction; execution starts the same day. Owner's words are
> marked `OWNER`; everything else is `DERIVED` design serving them.

## 1 · What the owner asked for

`OWNER`, distilled from the live directive:

- *"Think of this repo as a browsable application where the main feature is that
  everything is reachable in just a few taps/links. So no matter where you look
  in the repo you understand where you are and what that part is for."*
- A **mandatory reading order** whose requirements are explicit: any session
  understands **why this repo exists**, **how it came to existence**, that the
  **EAP happened and has now ended**, the **important goals**, and **what he is
  working on and why**. *"A fresh session should not read everything, but it has
  to understand the bigger picture."*
- *"Each section should be explained and easily found, so the problem that
  multiple sessions skipped an important document does not happen again."*
- *"Maybe we can use some kind of label system, where each part of the repo is
  either marked important or unimportant etc."*
- PR count is irrelevant: *"it does not matter if it happens in 1 PR or 100"* —
  the bar is **properly done**. (Verified the same day: no 1-PR limit exists
  anywhere in this repo; the constraint a session obeyed came from harness
  notification text.)

## 2 · Why this plan exists (the evidence base)

The full-read audit ([`../audits/2026-08-10-full-read/`](../audits/2026-08-10-full-read/README.md))
measured the failure this design answers: five consecutive sessions missed that
the owner's current plan was unreachable from the front door; 101 live-surface
defects survived adversarial refutation, and the dominant mechanism was **an
appended correction that never retracted what it corrected** — coherent documents
agreeing with each other and all wrong. Reachability ≠ being met: the E1 plan was
"reachable" at five hops and effectively invisible.

## 3 · The design

### 3.1 Three tiers, applied to areas (not to 833 files)

| tier | meaning | reader contract |
|---|---|---|
| **CORE** | mandatory orientation — the numbered reading order | read on every cold start; small enough that skipping is inexcusable |
| **TASK** | live surfaces read when the task touches them | routed by the boot table, the map, and doc-routes — never required for orientation |
| **RECORD** | historical/dated — the estate's memory | never required; explains provenance; a claim inside one is true *of its date* |

Tiers live in **the map** (§3.2) and in each area's README — not as 833 per-file
edits, which would go stale the way every frozen count has. Per-file `Status:`
badges already exist and keep their job; the tier answers the coarser question
"do I need this part at all?"

### 3.2 The map — `docs/MAP.md`

One page, linked from `README.md` and the boot file: every top-level directory
and every `docs/` subdirectory, one line each — what it is, its tier, live or
historical, where its README is. The browsable-app "few taps" property: README →
MAP → any area → any file, ≤3 links. The map is a *router*, not an encyclopedia;
one line per area, links carry the depth.

### 3.3 The mandatory reading order (CORE, in `README.md`)

Six reads, each with a one-line "what this gives you" so skipping is a choice,
not an accident:

1. `README.md` — what this repo is, **the story in 60 seconds** (new §: estate →
   EAP autonomous-Projects program → closed 2026-07-21 → consolidation era), and
   this list.
2. [`docs/intent.md`](../intent.md) — why it exists, what "working" means, who
   does what across providers (`OWNER`-labelled).
3. [`docs/current-state.md`](../current-state.md) — what is true now.
4. [the consolidation program](2026-07-26-consolidation-program.md) — the goals,
   the OD directives, the NOW pointer.
5. [`docs/fleet-account-2026-07-26.md`](../fleet-account-2026-07-26.md) — how it
   came to existence: the EAP story, what the program produced, its close.
6. [`docs/owner-reflection-2026-07-21.md`](../owner-reflection-2026-07-21.md) —
   how the owner thinks and decides.

This is the boot file's deep path made *mandatory and self-explaining* rather
than optional-looking. The boot file keeps its role for Claude Code; README
carries the surface-neutral copy (ChatGPT Work loads no boot file — measured).

### 3.4 The "you are here" contract (per-area READMEs)

Every directory a session can land in gets a README ≤15 lines stating: what this
area is · tier · live or historical · 3–5 key files · one link up (MAP). Areas
missing one today: `scripts/`, `tools/`, `environments/`, `templates/`,
`docs/conventions/`, `docs/retro/`, `docs/succession/`, `docs/audits/`.
Existing area READMEs get a tier line only — no rewrites of good content.

### 3.5 Repairs folded in (from the audit's defect list)

- `docs/findings/README.md` — regenerate the index complete (25 of 42 listed
  today), using the audit's per-file gists as row text.
- The two front-door contradictions already fixed this day (NOW pointer / OD-15;
  "Tier 1 filled" belongs to the next edit pass).
- The remaining ~100 defects stay in the audit's
  [`findings.md`](../audits/2026-08-10-full-read/findings.md) as the edit-pass
  worklist — this plan is navigation, not the whole cleanup.

## 4 · Execution order

1. ✅ Persist audit raw record + round-2 corrections + OD-15 (fm #840).
2. This plan, committed (fm #840).
3. `docs/MAP.md` + README rewrite (story, reading order, map link).
4. Missing area READMEs + tier lines on existing ones.
5. `docs/findings/README.md` regeneration from gists.
6. Boot-file sync (point at README's order + MAP; minimal words).

Steps 3–6 are one-or-more PRs; if a session dies mid-way, this file is the spec.

## 5 · Non-goals

Not a rewrite of any historical document (records may grow; instructions may
not). Not per-file tier stamps. Not a new checker — the existing `reachable`
check plus the map is the mechanism; a naive "every plan in the read path"
gate was measured to red on 7 files and stays rejected.
