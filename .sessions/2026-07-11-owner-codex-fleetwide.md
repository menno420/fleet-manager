# 2026-07-11 — owner update: Codex fleet-wide enablement + superbot-idle verdict

> **Status:** `complete`

📊 Model: Claude Fable 5 (claude-fable-5) · owner-update propagation slice · night (~00:4xZ)

## Declared at open (born-red)

Owner update (2026-07-11 ~00:2xZ): Codex environments now exist for ALL 12
active fleet repos; stale envs for dead repos deleted. This session propagates
that fact in ONE PR:

1. `projects/` metas — every Codex-status line → ENABLED (owner, 2026-07-11);
   codetool ×3 archive metas note envs deleted; quota caveat centralized in
   `projects/README.md`; new `projects/superbot-idle/meta.md` stub (repo
   verified to EXIST — the games-mapping react-by-action).
2. `docs/capabilities.md` — retire the fleet-manager no-Codex-env wall
   (dated, owner provenance); add the fleet-wide enablement fact + quota
   caveat (quota refusals = RETRY-LATER, never a wall).
3. `docs/review-queue.md` — @codex now PRIMARY drain path on all 12 active
   repos; open rows' drain paths annotated; ORDER 007 relay unblocked for
   fleet-manager PRs (header note).
4. `docs/owner-queue.md` — sim-lab OA-002 → Resolved; item 14 Seat B
   repo-creation click DONE (superbot-idle exists, cited); react line
   reworded to "§5 veto window open, prep proceeding decide-and-flag".
5. `control/inbox.md` — append ORDER 014 (this owner update, ✅ DONE here)
   + ORDER 015 (Seat A + Seat B founding-package prep; status: new).
6. Heartbeat last (00:3xZ stamp; games-mapping flag downgraded to "§5 veto
   window open").

superbot-idle verdict (verified this session, pre-card): **EXISTS** —
menno420/superbot-idle, public, pushed 2026-07-11T00:15:40Z, SEEDED (binding
lane-contract README live on main: idle-engine + theme packs, seeded per
superbot Q-0267 founding package). Landing: born-red card → flip `complete`
last → REST squash on green (R21).

## Done (all six change sets, this PR — #54)

- **superbot-idle verdict: EXISTS + SEEDED** — `list_repos`: public, pushed
  2026-07-11T00:15:40Z, `can_push: true`; raw README probe (200): binding
  lane-contract README on main (idle-engine + theme packs, Q-0267 founding
  package). MCP repo scope + api.github.com are walled for it from this seat
  (recorded walls — verdict built from the two working channels, not guessed).
- **projects/ metas** — 11 active metas' Codex lines → **ENABLED (owner,
  2026-07-11)** with the old verdicts superseded in place; codetool ×3 archive
  metas note stale envs DELETED; **new `projects/superbot-idle/meta.md`**
  (PRE-PACKAGE stub: existence verdict, Seat B frame, ORDER 015 pointer);
  `projects/README.md` gains § Codex fleet-wide enablement (the ONE central
  quota-caveat home: refusals = RETRY-LATER, never a wall — superbot#1920
  22:03Z cited) + matrix fleet-manager/superbot-idle rows updated.
- **docs/capabilities.md** — fm no-Codex-env wall RETIRED (dated 2026-07-11,
  owner provenance, old recording sites named); enablement fact + quota
  caveat added as a CAN entry.
- **docs/review-queue.md** — standing drainer re-primaried: @codex PRIMARY on
  all 12 active repos, fallback tier = quota windows + archives/non-enabled;
  ORDER 007 relay UNBLOCKED for fm PRs (header note); all 8 open rows'
  drain paths annotated (codex? → codex ×4; sb#1920 quota = retry-later;
  pokemon#8/gba#12 re-affirmed manager-batch — outside the 12).
- **docs/owner-queue.md** — new § Resolved 2026-07-11: sim-lab OA-002
  RESOLVED, fm PR-#26 env ask RESOLVED, Seat B repo click DONE; item 14
  reworded to "react-by-action received for repo name; §5 veto points remain
  open for objection, founding-package prep proceeding decide-and-flag".
- **control/inbox.md** — ORDER 014 appended near-verbatim + ✅ DONE (executed
  here); **ORDER 015 appended (status: new)** — Seat A + Seat B founding
  packages, next chain slices execute it.
- **Heartbeat last** — 00:35Z stamp; games-mapping flag DOWNGRADED to
  "§5 veto window open"; permissions re-land state carried as found
  (grant landed owner-authored `c23223f`; v2 fold re-land still rides the
  work ladder); propagation record section added — the deliberate final step
  before this card flipped `complete`.

`bootstrap.py check --strict` (with inbox-base simulation): green except the
expected born-red card hold + the pre-existing advisory owner-action warning.

💡 **Session idea:** add a `codex-status` line to `bootstrap.py check`'s
advisory tier (or a tiny fm checker) that greps `projects/*/meta.md` for
Codex verdicts older than the newest fleet-wide ruling in
`projects/README.md` — this session found 11 metas + 2 ledgers + 1 queue all
carrying the same stale fact; a one-line drift probe would have named the
full correction set mechanically (and will again at the NEXT fleet-wide
platform change, which this program generates monthly).

⟲ **Previous-session review:** chain slice #6 (PR #52) was a model lean
slice — it scoped superbot-games#5's residual risk with a file-level coverage
map instead of a vague "looks fine", and its honest "reactions are not
agent-visible from this seat" line is exactly what kept THIS session from
misreading the owner's silence: the react arrived by action (repo creation),
not by comment. Improvement it surfaces: owner reacts increasingly arrive
**by action** (repo created, commit landed, PR merged) rather than by text —
the wake prompt's owner-signal probe should name "check for react-by-action
artifacts (new repos via list_repos, owner-authored commits)" as a standing
probe step, not rely on comment threads.
