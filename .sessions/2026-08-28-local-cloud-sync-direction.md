# 2026-08-28 — record the owner's local/cloud sync direction (2026-08-27→28)

> **Status:** `complete` — the sitting's decisions are recorded, every review
> finding is dispositioned, and the gate ran green on the completed card.

- **📊 Model:** fable-5 · high · docs-only
- **📍 Venue:** local-desktop

## Mission

The 2026-08-27→28 hub sitting (owner-live, on the laptop) produced owner
decisions on local↔cloud session sync that existed only in that chat — the
loss mode this repo keeps writing findings about. Land them:

- a dated owner-direction record (`docs/findings/2026-08-28-owner-direction.md`,
  verbatim, provenance-labelled) + its index row and OD row;
- `docs/owner-queue.md`: `OQ-FM-AGENTS-BOOT` answered **yes** ·
  `OQ-ONEDRIVE-HUB` rescoped (no longer sync-blocking);
- in-place amendments to `docs/activity/README.md`, the execution packets
  (PKT-B3 executor + step 3, PKT-B4 gate, OWN table) and the legibility plan
  § 7, plus `docs/current-state.md` and `docs/execution-surfaces.md` pointers.

Every removal was previewed to the owner in-chat and approved row by row
(six rows, 2026-08-28). **No packet executes here — recording only**; the
owner said "no execution yet" and the substrate-kit discussion is still ahead.

## Shipped

- `docs/findings/2026-08-28-owner-direction.md` — NEW: the sitting's verbatim
  record (handoff goal · lean-history pages · routing rule · full local
  discipline · PKT-B3 executor clarification · AGENTS.md yes · public fine ·
  honest nulls), + its `docs/findings/README.md` index row.
- `docs/planning/2026-07-26-consolidation-program.md` — OD-23 row (his words
  only; every mechanism stays `DERIVED` in the plans).
- `docs/owner-queue.md` — `OQ-FM-AGENTS-BOOT` ✅ ANSWERED yes ·
  `OQ-ONEDRIVE-HUB` ✅ RESCOPED (no letter owed), originals kept for
  provenance.
- `docs/planning/2026-08-26-estate-execution-packets.md` — PKT-B3 re-headed
  (hub-local session, held for GO; step 3 dropped as a step; hub hook wiring
  added to step 2; acceptance gains the handoff half) · PKT-B4 gate marked
  open · OWN-1/2/8 rows updated · § 9 OneDrive×git null rescoped.
- `docs/activity/README.md` — planned-pages spec sharpened (handoff test,
  lean history, public content rule), executor paragraph replaced,
  `OQ-ONEDRIVE-HUB` paragraph rescoped.
- `docs/planning/2026-08-26-legibility-and-intent-plan.md` § 7 +
  `docs/execution-surfaces.md` §§ 3–4b + `docs/current-state.md` — the
  AGENTS.md answer and the direction recorded where they were presented as
  open; `docs/findings/2026-08-26-owner-direction.md` §§ 1, 1b, 3 — dated
  clarify/supersede pointers, history untouched.
- `.substrate/guard-fires.jsonl` — the gate run's telemetry delta, committed
  per its own instruction.

## Review disposition

- Codex round 1 errored ("Failed to set up container") — retried per doctrine.
- Round 2 on `b3b2d09` returned two P2 findings, both **[conceded]**:
  (1) the two live ChatGPT project prompts still presented the AGENTS.md
  decision as open — both now carry the answered note ("do not re-ask");
  (2) the `OQ-ONEDRIVE-HUB` rescope read as if visibility solved transfer —
  the "pages give sight, not file access" residual is now named in the
  packets, the activity README, the queue row and the finding's § 7, with
  the a/b/c options kept as the recorded transfer candidates should a
  hub-only handoff ever arise.
- Round 3 on `cd039ec` returned one P2, **[conceded]**: the PKT-B3 hook-wiring
  clause had collapsed the three-way routing rule into two-way (all non-repo
  work → the public section); the spec now names all three branches, with
  machine/personal staying in the hub and only the lean public-safe account
  reaching the pages.
- Round 4 on `994bb8f` — the capped round (session-close: two re-review
  rounds, then land with findings named) — returned three findings. The P1 on
  this card's own `in-progress` badge is the designed born-red hold and
  resolves with the flip **[conceded-by-design]**. The P2 (PKT-B3 step 1 asked
  the public page for the hub's actual layout, conflicting with the no-paths
  content rule — now capability-level only) and the P1 (the GO hold was not
  propagated to the executable-route pointers: current-state's first-sitting
  line, the packets' § 6 first-sitting and § 7 paste-ready line — now gated)
  are both **[conceded]** and fixed. Per the cap, these fixes land without a
  further re-review round: reviewed SHA `994bb8f`, followed only by the fix
  commit and the flip commit.

## 💡 Session idea

A `🤝 Handoff:` card line (closed set: `expected-cloud` · `expected-local` ·
`null`) that `tools/estate_activity.py` surfaces as a "batons in flight"
section — the venue-handoff test (OD-23) becomes mechanical: a cloud session
opens the estate log and sees exactly which local tasks are waiting for it,
instead of inferring from prose.

## ⟲ Previous-session review

The 2026-08-27 owner-comments session (#952, chatgpt-work) landed the durable
comment contract this sitting leaned on: its "explicitly public" stance is now
owner-ratified (*"public is fine"*, OD-23 § 5), and nothing in its shipped
surfaces needed correction during this pass. The 2026-08-26 packets session's
PKT-B3/B4 rows are amended here by new owner direction, not as defects.

Layer-2 handoff: null (fleet-manager itself; no member repository attached).

## Verify

- `python tools/check_doc_routes.py --strict` — **71 routes · 36 docs routed ·
  0 errors · 4 notes** (all four pre-existing).
- `python bootstrap.py check --strict` — re-run at the flip with the card
  complete: the card hold cleared; the run stays red on **one pre-existing
  environment finding** — `tools/test_owner_comments.py` fails on this
  Windows venue **identically on a clean tree with this PR's changes stashed**
  (6 failures / 41 errors both ways; the parallel Codex workspace on this
  machine is claimed for exactly "owner-comments Windows portability").
  This PR's diff is markdown + this card + guard-fire telemetry only.
  **The binding predicate is the PR's required `substrate-gate` check
  (Linux), and this PR lands only on its green** — the venue block's own
  rule for a local gate that cannot answer.
- **Resolved before landing:** `main` moved mid-review (#953 — exactly that
  Windows portability fix, landed by the parallel Codex workspace); the one
  merge conflict was the append-only `guard-fires.jsonl` ledger, resolved as
  a union (both sides' records kept: 28,386 + 154). After the merge the full
  local gate runs **green, real exit code 0** — `check: all checks passed`,
  card reported complete.
- Removal preview: six rows presented to the owner in the hub chat
  2026-08-28; all six approved (rows 1–2 with the § 4 clarification).

## Landing

- PR: `menno420/fleet-manager#954` — READY on protected `main`; born-red card
  first commit; Codex review requested on the batch head before the flip.
- No capability wall discovered. New owner-only asks: none added — two
  resolved/rescoped.
