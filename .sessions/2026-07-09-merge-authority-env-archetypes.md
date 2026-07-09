# 2026-07-09 — merge-authority policy + env archetypes + merge-queue verification

> **Status:** `complete`

📊 Model: Claude Fable 5 (claude-fable-5) · worker session · docs/policy/environments

## Declared at open (born-red)

Three owner directives (2026-07-09), one PR:

1. **Merge-authority policy** — gen-2 lanes ALWAYS land their own PRs
   (auto-merge armed at creation = the sanctioned self-merge path; REST
   merge-on-green R8 fallback). No PR waits for review: merge anyway + flag
   in a committed `docs/review-queue.md` ledger and/or @-mention Codex;
   review is post-merge, veto = revert. Kill do-not-automerge/owner-gated
   merge for gen-2 lanes. Folds into gen2-blueprint §1 + §2 and the
   venture-lab founding text; seed `docs/review-queue.md`.
2. **Environment consolidation** — ≤4 archetypes covering all current +
   planned projects; one TESTED defensive setup script + env var NAME union
   each; `environments/archetypes.md` mapping table + scripts; two-source
   layout test (the trading-strategy provision killer) demonstrated.
3. **Merge queue** — re-verify the open-PR sweep at live HEAD; commit
   `docs/merge-queue-2026-07-09.md` for the owner's merge session.

Then: owner-queue consolidation (one click-level environments item + merge-
queue pointer), handoff in-flight update, card flip, auto-merge verification.

## Done (all three directives, PR #10)

1. **Policy shipped:** gen2-blueprint §1 conventions bullet + §2 delta 2
   rewritten (provenance: owner directive 2026-07-09, on each edit);
   venture-lab MERGE AUTHORITY block upgraded (launches with it);
   `docs/review-queue.md` seeded (append-only ledger, R9; post-merge review,
   veto = revert).
2. **Archetypes shipped:** `environments/archetypes.md` (11 project rows +
   the live coordinator env → 4 archetypes; var-NAME unions; 3.10/3.11
   wrinkle; owner paste-steps) + 4 scripts, all `bash -n` clean and run
   clean in-container across 6 layouts — incl. the bare two-source checkout
   that killed 2 trading sessions (exit 0, per-repo installs) and a
   broken-child non-fatality demo. Transcripts in PR #10's body.
3. **Merge queue shipped:** `docs/merge-queue-2026-07-09.md`, every row
   re-verified at live HEAD 22:41Z. Material delta vs the draft:
   superbot-next #95 is now `mergeable_state: dirty` (main moved) — MERGE
   after a lane-side conflict fix; kit #49/#26 resolved to `behind`
   (benign); games #14/#5 clean; zero-PR repos reconfirmed.
4. Owner-queue item 1 → the ONE "create the ≤4 environments" click item
   (trading first); item 16 → merge-session pointer; venture-lab launch
   step 4 now points at the python-lab archetype. Handoff in-flight updated.

Friction (R8 realized again): `enable_pr_auto_merge` refused while the
born-red gate was the last-reported state ("unstable status") — re-armed in
the fresh pending window after the flip push; REST merge-on-green stood by
as the fallback.

## 💡 Session idea

**Archetype drift check:** the 4 archetype scripts + `archetypes.md` will
drift as lanes add manifests/vars (the exact drift class that made the old
per-lane specs scatter). A tiny stdlib checker (`tools/check_archetypes.py`
or a kit check) that greps each mapped repo at HEAD for
`scripts/env-setup.sh` / `requirements*.txt` / `requirements.lock` /
`pyproject.toml` and diffs reality against each project's mapping row would
catch a stale row at CI time instead of at the next provision death — the
cheapest possible guard on the fleet's most blood-paid failure class.

## ⟲ Previous-session review

The gen-1 wind-down session (PR #9) executed a clean template-reuse play
(venture-lab voice → universal prompt) and shipped R20 with real provenance
— its "unacknowledged = undelivered" rule is already earning its keep. One
genuine gap this session inherited: its owner-queue asks still pointed env
setup at the retro-synthesis pack in ANOTHER repo (superbot `docs/eap/`)
for "exact scripts" — a scattered pointer this session's archetype
consolidation retires. Workflow improvement shipped here: environments are
now ONE owner item backed by tested, in-repo scripts instead of four
cross-repo scavenger hunts.
