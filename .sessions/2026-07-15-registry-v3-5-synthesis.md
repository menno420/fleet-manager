# 2026-07-15 — registry v3.5 synthesis verification + paste-ready per-seat index (ORDER 040 T1)

> **Status:** `in-progress`

Intent: verify ORDER 040 TASK 1's registry synthesis is complete at the current
generation (diff hub prompt artifacts vs the shipped bodies; fold real drift
only), ship the paste-ready per-seat starting-prompt index the owner asked for
live this session (2026-07-15), and note both in docs/current-state.md.

- **📊 Model:** Fable · high · docs-only

## What happened

- **ORDER 040 T1 verified complete at v3.6** (no restamp needed): the v3.5
  generation shipped 2026-07-13 (stage-1 PR #151 = v3.5; stage-2 = v3.6 per
  the registry's own bump rule — a body-changing re-sync takes the next
  number). This pass diffed the hub artifacts ORDER 040 names against the
  shipped bodies: all folds present in all 9 startups (grep: Q-0271 rider,
  chase-references + prep-owner-steps, OPEN-PRs-STAY-OPEN standing sentence,
  Q-0272 fleet-read paragraph, VENUE:hub, Q-0274 grounding route);
  `regen_b_files.py` exit 0 (all drift checks, 9/9 seats clean);
  `--check-registry` exit 0 (27/27 `projects/<seat>/` copies match). **No
  real body drift → no body edits, no version bump** (registry convention:
  no body change = no bump; restamping backwards to "v3.5" would break the
  DRIFT-CHECK grammar).
- **Paste-ready per-seat index shipped:** `docs/prompts/v3/README.md`
  (Status `audit`) — one row per seat (all 9 registry seats, covering every
  Gen #63 live lane): seat → exact CI file + startup file → kept/changed
  note (v3.5/v3.6), plus the founding procedure and the verification record.
  Linked from `docs/prompts/README.md` and `docs/current-state.md`.
- **current-state note** added under Recently shipped (fm #248).
- **Owner-queue A#63 merged-citation flag cleared** (visible drift on the
  close path): the `PR #246` citation reworded history-as-context
  ("landed via fm #246 — since merged"), same pattern the previous session
  used for #245; `check_owner_queue` back to CLEAN.
- **Close checks:** check_roster_freshness OK (Gen #64, 1.0h) ·
  check_owner_queue CLEAN · check_trigger_health PASS 9/9 (committed
  snapshot, captured 21:48:44Z) · `bootstrap.py check --strict` exit 0 (red
  only on this card's designed born-red hold). Seat-digest ADVISORY drift on
  3 seats (fleet-manager · game-lab · venture-lab) is pre-existing,
  advisory-only — left for the `--sync` lane (guard recipe:
  `docs/prompts/tools/seat_digest_sync.py --sync`, gate is
  `seat_digest_sync.py --check`).
- **Dispatch note (factual):** the coordinator's standing-authorization
  prompt block for this task was platform-denied 3× at dispatch (classifier:
  fabricated-authorization content in prompt templates, all phrasings) and
  was rerouted to owner-held text delivered in chat; this PR therefore
  carries no authorization/pre-authorization content — file map,
  verification record, and session mechanics only.

## Files touched

- `docs/prompts/v3/README.md` (new — the per-seat index)
- `docs/prompts/README.md` (pointer)
- `docs/current-state.md` (Recently shipped note)
- `docs/owner-queue.md` (A#63 citation reword)
- `.sessions/2026-07-15-registry-v3-5-synthesis.md` (this card)
- `control/claims/claude-registry-v3-5-synthesis.md` (claim, deleted at close)
- `control/status.md` (heartbeat)
- `.substrate/guard-fires.jsonl` (kit telemetry delta, committed not reverted)

## Enders

- 💡 **Session idea:** an **index-generation sync guard** in
  `docs/prompts/v3/tools/regen_b_files.py`: the new per-seat index
  (`docs/prompts/v3/README.md`) states the registry generation ("v3.6") in
  prose; when a future fold bumps the per-project stamps, nothing forces the
  index's generation line + kept/changed column to restamp, so the owner's
  paste map can silently go stale. One extra drift check — extract the
  index's stated generation and compare to the per-project stamp lines, fail
  on mismatch — makes the paste map mechanically current. Dedup: grepped
  `docs/ideas/` + `per-project/README.md` (no existing index/generation sync
  guard idea).
- ⟲ **Previous-session review** (owner-no-review-order, PR #246): strong
  slice — the ORDER 047 record kept owner verbatim primary + context quotes
  separate, and the A#63 landing path was recorded honestly (workflow-file
  rail named as a technical carve-out, not re-framed). One workflow
  improvement it surfaces: its heartbeat baton named "fan-out delivery of
  ORDER 047" as next task but left no per-lane checklist (which 8 lanes,
  which inbox paths), so the next wake re-derives the roster mapping; batons
  that name a fan-out should carry the target list inline — one line, eight
  slugs — to make the next wake paste-ready.
- **Next 2 tasks (baton):** (1) fan-out delivery of ORDER 047's paste block
  to the live lanes (superbot hub · substrate-kit · websites · idea-engine ·
  sim-lab · venture-lab · trading-strategy · gba-homebrew — owner/hub paste
  or next manager wake relays into lane inboxes); (2) after the owner's
  A#63 click lands #227, verify the merge and sweep A#63 to Resolved.
