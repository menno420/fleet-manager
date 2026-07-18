# 2026-07-18 · fleet-manager owner-steps revise to corrected doctrine (#308/#309/#311)

> **Status:** `complete`

About to happen: revise `docs/owner-steps-2026-07-18.md` to the corrected doctrine
(owner #308/#309/#311) — split it into three clear sections: ✅ done by agents,
→ handled in the hub chat (agent-doable, not owner clicks), and 👤 genuine owner-only
(external accounts + money, secret values, product/intent decisions). Reflect this
session's sweep results.

- **📊 Model:** Opus 4.8 · medium · docs-only

## What shipped (Did)
- **docs/owner-steps-2026-07-18.md — restructured into three top sections** (badge
  kept `audit`; filename unchanged so `current-state.md` line 117 still reaches it):
  1. **✅ Done by agents (no owner action):** gba #177/#178 flipped Ready (auto-land
     on green), gba #165 merged (Underroot v1.0, by owner), fleet-manager #313
     doctrine reconciliation — each linked.
  2. **→ Handled in the hub chat (agent-doable, not owner clicks):** the
     settings/rulesets/required-checks list (gba ruleset, pokemon-mod-lab
     protect-main + `ROM builds`, substrate-kit → `kit-quality`, superbot-idle
     `pytest`, superbot-next retention 400d + merge-queue, product-forge Pages),
     releases/tags (gba Lumen-Drift v1.3; cfgdiff/envdrift parked on delete-vs-archive),
     and the fleet-wide stale-branch deletes — each with target + full URL, plus the
     one-line venue note (this Projects session's platform layer declined the direct
     settings/release calls; routed to the hub session, which has full ability — not a
     standing limit).
  3. **👤 Genuine owner-only steps:** external accounts + money (Gumroad/KDP/Stripe,
     PayPal), secret VALUES (websites PAT, Railway Postgres, mineverse/next env,
     ROSTER_READ_TOKEN — names only), and product/intent decisions
     (delete-vs-archive rec A, apparatus-sizing, kit/games rulings, venture
     money/D1–D19, trading go/defer, idea-engine #481, curious slicer/drybox,
     websites bot-control). Time-gated + optional/veto tails preserved. Exact URLs
     and paste-blocks retained.
- **Appendix preserved** and extended with this session's newly-done items.
- **Manual false-wall scan of the rewritten doc: CLEAN** — no banned present-tense
  wall phrasing. (The `tools/check_no_false_walls.py` guard #309/`.claude/CLAUDE.md`
  reference as a required check is still **not planted** in this repo and no workflow
  invokes it — same gap the prior session flagged; scanned manually instead.)
- **Verify:** `check_owner_queue` EXIT=0 · `check_docs_links` CLEAN (256 files) ·
  `bootstrap check --strict` EXIT=0 (born-red HOLD by design until this flip).

## 💡 Session idea
Add a `--owner-only` lint mode to the owner-steps aggregator (or `check_owner_queue.py`)
that flags any queued item whose verb is *merge / ready-flip / change setting / cut
release / delete branch* against a mergeable-green or agent-doable target — i.e. the
exact class this session had to hand-move out of the owner list. It is the queue-side
twin of the still-missing `check_no_false_walls.py`: false walls in prose red the PR,
false owner-steps in the queue would red it too, so the roll-up can't silently re-over-route
agent work to the owner next time.

## ⟲ Previous-session review
PR #313 (`docs/current-state.md` + `owner-queue.md` doctrine sync) did the doctrine
correction cleanly at the *living-ledger* layer and honestly flagged both the
CONSTITUTION branch-deletion tension and the absent guard — good, disciplined scoping.
What it left for a follow-up (this session): the **owner-steps roll-up itself** still
carried the pre-correction routing, so a reader hitting `owner-steps-2026-07-18.md` from
current-state's link still saw agent-doable work filed as owner clicks. **System
improvement:** doctrine corrections should sweep *all* docs reachable from the changed
one in the same pass (current-state → owner-steps is a one-hop link), not just the
directly-edited ledgers — otherwise the corrected ledger points at an uncorrected
downstream doc. The `--owner-only` lint idea above is the enforcing version of that.

## ⚑ Self-initiated
None beyond the assigned rewrite. Flagged (did not fix, out of scope, carried from #313):
the absent `tools/check_no_false_walls.py` guard (session idea proposes its queue-side
twin); the pre-existing `seat-digest-stale` advisory (regen via `python3 bootstrap.py
seat-digest`, pulls in #308/#311 bytes I didn't author — left for a follow-up).
