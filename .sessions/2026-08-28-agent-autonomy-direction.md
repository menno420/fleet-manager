# 2026-08-28 — record the owner's agent-autonomy and session-hygiene direction (second overnight sitting)

> **Status:** `complete` — the sitting's direction is recorded, every review
> finding is dispositioned, and the gate ran green on the completed card.

- **📊 Model:** fable-5 · high · docs-only
- **📍 Venue:** local-desktop

## Mission

The **second** overnight 2026-08-27→28 hub sitting (owner-live, on the laptop;
parallel to the local/cloud-sync sitting fm #954 recorded, and it is the
substrate-kit conversation that sitting said was *"still ahead"*) produced
owner direction that exists only in that chat — the loss mode this repo keeps
writing findings about. Land it:

- a dated verbatim owner-direction record
  (`docs/findings/2026-08-28-owner-direction-agent-autonomy.md`,
  provenance-labelled) + its index row and an **OD-24** program row;
- Layer-2: a new **owner-directed review round** thread on
  [`docs/repos/substrate-kit/README.md`](../docs/repos/substrate-kit/README.md);
- `docs/current-state.md`: the "parked for / comes first" substrate-kit-sitting
  lines amended to the sitting having happened — **execution stays held;
  nothing here GOs the packets**;
- the sitting's no-commit laptop work logged via `tools/estate_activity.py`.

Recording only — no mechanism is built here, per the promotion rule
(roadmap § 6) and the owner's own "*documented in fleet-manager so I can
continue this later*".

## Shipped

- `docs/findings/2026-08-28-owner-direction-agent-autonomy.md` — NEW: the
  second sitting's verbatim record (the hygiene mandate with his A–D answers ·
  the initiative duty · the freedom doctrine with the ratification correction ·
  the chain architecture · the stepping-back verdict · the review round's
  four-step method) — commit `50c097a`.
- `docs/findings/README.md` — index row.
- `docs/planning/2026-07-26-consolidation-program.md` — **OD-24** appended
  directly under OD-23.
- `docs/repos/substrate-kit/README.md` — Layer-2 thread *"the owner-directed
  review round"* added first; every other thread untouched.
- `docs/current-state.md` — the three lines parked on "the substrate-kit
  sitting" amended to the sitting having happened (**the hold is NOT
  lifted**), plus one new OD-24 bullet.
- `docs/activity/off-repo-log.md` — the laptop sitting's no-commit work
  (instant-search wiring, Start-menu web search off) logged,
  venue `local-desktop`.
- `.substrate/guard-fires.jsonl` — telemetry delta retained, per
  current-state's live-mechanisms note.

## 💡 Session idea

A `SessionStart`-moment injection that serves the booting venue's one-line
purpose from its own intent surface (a repo: `intent.md` § 1; the hub: its
boot file's owner-three-liner). It is the cheapest mechanical answer to
*"the agents forgot their purpose because I stopped reminding them of it"*
(OD-24 § 5), the natural first prototype of the § 4 cross-session chain, and
it is measurable against the drift-incident corpus the review round will
harvest — promote only if the incidents it would have caught are real
(roadmap § 6).

## ⟲ Previous-session review

fm #954 (the same night's first sitting): its queue actions verified at this
checkout — `OQ-FM-AGENTS-BOOT` ✅ ANSWERED and `OQ-ONEDRIVE-HUB` ✅ RESCOPED
both present in `docs/owner-queue.md` (lines 519, 496). Its card's *"the
substrate-kit discussion is still ahead"* was accurate at writing and is
superseded by this PR the same night — recorded here rather than edited
there, because a card is a dated record. Nothing in its shipped surfaces
needed correction during this pass.

Layer-2 handoff: docs/repos/substrate-kit/README.md — "the owner-directed
review round" thread added

## Verify

- `python tools/check_doc_routes.py --strict` — **71 routes · 36 docs routed
  · 0 errors · 4 notes** (the same four pre-existing unrouted-convention
  notes fm #954 reported).
- `python bootstrap.py check --strict` — pre-flip: exactly the designed
  born-red hold on this card and no other finding (verified against the CI
  job log too: both findings name the hold, *"designed hold, not a
  defect"*); re-run at the flip with the card complete: **green, real exit
  code 0** (`check: all checks passed`).
- Codex exact-head review on `50c097a`: **three P2 findings, 3/3 conceded
  and fixed** — (1) the A–D defaults table blurred `OWNER`/`DERIVED`
  (the defaults' wording is the session's accepted proposal, not his words —
  now labelled so, finding § 1); (2) the OD-24 row carried the agent-selected
  hook events and the four-step review method without their `DERIVED` marks
  (added); (3) two live surfaces (`docs/owner-queue.md`,
  the execution packets' PKT-B4 row) still parked the AGENTS.md
  plant-vs-hand question on *"the substrate-kit sitting"* — both amended to
  the review round, matching current-state. The catch class is exactly the
  provenance failure the finding itself warns about; conceded without
  reservation.

## Landing

- PR: `menno420/fleet-manager#955` — READY on protected `main`; born-red card
  first commit; Codex exact-head review dispositioned on the batch head
  before this flip; lands on `substrate-gate` green.
- No capability wall discovered. New owner-only asks: none — the queue was
  groomed by fm #954 hours earlier the same night; this session's 💡 idea is
  on this card.
