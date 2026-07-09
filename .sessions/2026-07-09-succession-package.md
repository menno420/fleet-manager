# 2026-07-09 — succession package (manager chat archiving)

> **Status:** `complete`

- **📊 Model:** unrecorded-by-policy · standard · docs-only
  (fleet program policy: no model identifiers in committed files)

## Goal

Commit the manager's full succession package before the owner archives this
chat: every deployed prompt verbatim (`docs/prompts/`), the uncommitted
evening findings (`docs/findings/`), the gen-2 blueprint draft, the successor
handoff doc, playbook R19, the yt-dlp capability recipe, dispatch-log evening
entries, and a heartbeat refresh. Nothing in the manager's context may be lost.

## What happened

- **`docs/prompts/`** — verbatim ledger: README index + universal init prompt,
  trading-lab, codetool arms (identical-by-design ×3), game-mining,
  game-exploration, universal wake-up, external-campaign meta-prompt
  (reconstructed structure, marked as such), and the NOT-YET-DEPLOYED
  venture-lab draft (`plan`, gen-2 born-right pilot candidate).
- **`docs/findings/`** — five previously chat-only worker reports distilled
  and committed: the full 10-lane retro synthesis (substance kept complete —
  the gen-2 blueprint's primary input), GPT-5.6 report (Codex-arm
  recommendation + METR eval-gaming caution), venture shortlist, the two
  UI-visibility screen-recording analyses (merged into one doc), and the
  ping-test dispatch/latency table (ack sweep flagged as pending for the
  successor).
- **`docs/gen2-blueprint.md`** — DRAFT seed standard: seed-state checklist,
  instruction-template deltas vs gen-1, owner setup checklist
  (routines = highest-value click), migration policy, successor open items.
- **`docs/handoff-2026-07-09.md`** — successor first-read: read order, per-lane
  fleet state, in-flight items (ping-ack, external campaign, venture-lab,
  Codex arm, kit orders, superbot-next ORDER 004 P0, websites ORDER 005, email
  addendum, EAP window closing 2026-07-10), standing rules.
- Housekeeping: playbook **R19** (serialize same-inbox appends), capabilities
  yt-dlp recipe, dispatch-log evening entries, `control/status.md` heartbeat,
  orientation router links for all new docs (reachability).
- Two stamp-discipline findings fixed pre-push (D-0007/D-0031 each de-cited to
  a single home); `bootstrap.py check --strict` green apart from this card's
  deliberate born-red hold.

## Guard recipe

The ping-ack sweep result was in-flight at handoff: successor collects the
observation worker's output or re-sweeps the 9 `control/status*` files
directly — anchor: `docs/findings/ping-test-2026-07-09.md` § Successor
follow-ups.

## 💡 Session idea

The succession package proves the manager's context is reconstructable only
because tonight someone manually swept chat-only artifacts into the repo. Make
it structural: a standing manager rule (candidate R20) — *every dispatched
worker's final report is committed to `docs/findings/` (or the dispatch-log
line links its committed home) in the same session that received it*. A
report that exists only in chat is a report the next manager never saw; this
package took hours precisely because that rule didn't exist yet.

## ⟲ Previous-session review

The housekeeping-verification session (#6) did exactly what its R-series asks:
verified every afternoon dispatch against live GitHub and caught three
unlanded/stale items reports had claimed. Miss it surfaced but didn't close:
it *observed* that order-append PRs race the inbox (kit#56 collision) and
proposed a template line, but shipped no rule — the same race then bit the
ping test hours later (PR #62 → #64). Improvement, applied this session: the
lesson is now enforcing as playbook R19 rather than advisory prose in a
session card — friction → rule, same day it was re-learned.
