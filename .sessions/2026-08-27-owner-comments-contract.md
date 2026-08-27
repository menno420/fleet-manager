# 2026-08-27 — durable owner-comment contract

> **Status:** `complete` — implementation, adversarial verification, and exact
> remote-head review are complete in `menno420/fleet-manager#952`.

- **📊 Model:** GPT-5 family · high · feature build
- **📍 Venue:** chatgpt-work

## Mission

Make repository-specific owner feedback a Fleet Manager-owned public record:
deterministic JSON records, stable per-repository and root indexes, a
never-delete consume transition, and a literal route a future session can read.
This is the Fleet Manager half only; the website UI and writeback client remain
owned by `websites`.

## 💡 Session idea

Add a bounded `owner_comments.py show <repo>` view that prints only active
comment identifiers, timestamps, source contexts, and paths. The stable README
already gives agents the route; a deterministic terminal view would make the
common read-and-consume loop easier without creating another projection or
copying comment text into member repositories.

## ⟲ Previous-session review

The 2026-08-26 estate-execution session specified the durable-record shape and
left the comments merge path, index update, and consume mechanics as named-open
findings. This session implements only that bounded contract; it does not
execute the other estate packets.

Layer-2 handoff: null (Fleet Manager itself; no member repository is being
modified).

## Shipped

- `docs/owner-comments/` — public v1 JSON schema, root projection, privacy and
  storage contract, and one stable generated README for every `docs/ESTATE.md`
  repository.
- `tools/owner_comments.py` — strict init/check/reindex/add/consume lifecycle;
  consumption is an atomic move into preserved history with both indexes
  updated in the same transaction. Recovery is pinned to symbolic HEAD, OID,
  index identity, exact target bytes, and crash-durable backups; mismatches are
  quarantined instead of overwritten.
- `.claude/hooks/route_docs.py`, `.claude/hooks/doc-routes.json`, and the live
  boot/router docs — repository work receives its literal active-comment index
  without an estate-wide search, including the documented Creator Kit aliases.
- `scripts/preflight.py` and `tools/test_owner_comments.py` — the storage,
  projection, staged-candidate, routing, never-delete, and crash-recovery
  contracts are part of the repository gate.
- Decision `[D-0018]` and `docs/current-state.md` record the public/durable
  boundary and the split from the separately owned `websites` UI/writeback.

## Review disposition

- Codex review of `b9fb8fb581` raised three findings: post-crash edit loss
  (P1), incomplete staged-tree validation (P2), and missing Creator Kit aliases
  (P2). **[conceded]** All three were fixed, replied to with exact evidence, and
  their threads were resolved.
- Subsequent exact-head reviews found and closed the remaining Windows
  read-only/hard-link, stale-mode, symlink/junction/reparse, transaction-root,
  file-mode phase, `.git` URL, and over-broad routing cases. **[conceded]** Each
  valid finding received a regression, exact-head reply, and resolved thread.
- Final product head `fde8a854c2783cbf321d249be24bc4fcb846b1cd`
  received a clean Codex review with no major issues. Independent adversarial
  passes over recovery, mixed modes, scratch windows, containment, and routing
  found no remaining P0/P1/P2.
- Remote-integrity audit caught connector truncation of generated
  `.substrate/guard-fires.jsonl` and a lost executable bit before merge. The
  final remote product tree keeps the telemetry path byte-identical to `main`
  and preserves the router hook as `100755`.

## Verify

- `python3 tools/test_owner_comments.py -q` — **89/89 passed**.
- `python3 tools/owner_comments.py check` — **CLEAN**, 28 repositories, 0
  active and 0 consumed records.
- `python3 tools/check_doc_routes.py --strict` — **71 routes**, 36 docs, 0
  errors, 0 notes.
- `git diff --check` — clean locally and on the corrected remote PR diff.
- `python3 bootstrap.py check --strict` — green after this deliberate final
  completion flip.

## Landing

- PR: `menno420/fleet-manager#952` — READY on protected `main`; the exact
  product head is reviewed and the repository gate is green.
- No capability wall and no new owner-only decision were discovered.
