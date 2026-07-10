<!-- v1 · 2026-07-10 · fleet-manager projects registry -->
# superbot — manual session kickoff prompt (NOT a standing seat)

> Part 2 of the superbot package. **superbot has NO standing Project seat by
> design** (owner directive Q-0264, 2026-07-10: the Q-0262.8 hub-executor pick
> was vetoed; hub games-finishing routes to the games program / owner-started
> superbot sessions; the Idea Engine harvests the hub's `docs/ideas/` by
> link). So this file is NOT a coordinator seat brief — it is the **manual
> session kickoff prompt** the owner (or a dispatcher acting for him) pastes
> as the first message when starting a superbot session at will. Provenance:
> `.claude/CLAUDE.md` session workflow + `docs/current-state.md` per-sector
> queues + Q-0259/Q-0264 rulings, verified against superbot origin/main
> `dc19b1e8`, 2026-07-10.

```
v1 · 2026-07-10 · superbot coordinator-prompt

Owner-started superbot session. Work this repo per its own working agreement
— .claude/CLAUDE.md is binding and auto-loaded; this message only sets the
boot order and the lane. There is no standing seat here (Q-0264): you are a
one-session agent; finish what you start.

BOOT (in order, before any edit):
1. Land on origin/main HEAD (persistent workspaces inherit a stale branch —
   `git checkout main && git pull --ff-only` if the residue advisory fires).
2. Read .claude/CLAUDE.md → docs/collaboration-model.md →
   docs/current-state.md (per-sector ▶ queues) → .session-journal.md
   ⚡ Quick reference → docs/AGENT_ORIENTATION.md route for your task.
3. Scan docs/owner/claims/ + open PRs for lane overlap before claiming.

PICK YOUR LANE (first match wins):
a. The owner's stated focus in this chat — it outranks everything below.
b. The GAMES COMPLETION WAVE (Q-0259 r.5 / Q-0264.8 priority): finish and
   deepen the hub's live games (mining/gear/skills/structures, fishing,
   creature game, casino) toward owner-playable completeness — the S1 sector
   file (docs/current-state/S1-bot.md) and the games folio carry the ▶
   startable items and turn-key plan slices.
c. A ▶ startable item from your sector's docs/current-state/ file, or a
   docs/ideas/ promotion (Q-0172 — ideas exist to be built; flag it on the
   ⚑ Self-initiated line).
Do NOT run the Q-0107 reconciliation pass — the routine does that itself
(Q-0124) — but fix any docs/ledger drift you can see (Q-0166).

EXECUTE per CLAUDE.md — the non-negotiables:
- Claim file first (docs/owner/claims/<branch>.md), delete at close.
- Born-red session card (.sessions/<date>-<slug>.md, Status: in-progress) as
  the FIRST commit; open the PR READY immediately (first ~2 minutes); flip
  the badge to complete as the deliberate LAST commit.
- If you open the PR via the GitHub MCP, call enable_pr_auto_merge right
  after (Q-0127) — the enabler workflow doesn't fire on app tokens.
- python3.10 everywhere; `python3.10 scripts/check_quality.py --full` +
  `check_architecture.py --mode strict` green before every push; batch pushes.
- Hard rails: services never import views; DB only via utils.db.*; writes
  through *_mutation.py services + emit_audit_action.
- Merging IS deploying (Q-0193) — never tell the owner to restart/deploy;
  DO tell him any per-PR data step (seed commands, operator buttons).

SESSION ENDERS (mandatory, in the session card, before flipping green):
- One backlog-grooming move: advance ONE docs/ideas/ item down its lifecycle
  (Q-0015).
- 💡 One NEW idea you genuinely believe in, dedup-grepped (Q-0089) — the
  Idea Engine harvests docs/ideas/, so a substantial one gets an idea file.
- ⟲ Previous-session review: one genuine remark + one concrete workflow
  improvement (Q-0102); never filler.
- Documentation audit (Q-0104): `python3.10 scripts/check_current_state_ledger.py
  --strict` + check_docs --strict + "is anything from this session not in its
  durable home?" — the /session-close skill drives the automated half.
- Sim-worthy questions and non-kit fleet needs: flag them for the fleet
  manager (route to sim-lab per Q-0264.7), don't build one-off harnesses here.

TERMINAL-STATE DISCIPLINE (Q-0103): the session is not done until the PR is
merged (auto-merge on green Code Quality) or closed with a one-line reason.
Never leave the session PR open. Delete your claim file, flip the card green,
and confirm in your final message: PR number, merge state, what shipped, what
you flagged.
```
