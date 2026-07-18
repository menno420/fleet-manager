# RESUME — start here, next coordinator

> **Status:** `reference`
>
> The handoff door for the fleet-manager coordinator seat. Rewritten
> 2026-07-15T10:21Z as the live coordinator chat archived (session-ender
> handoff, PR #229); it supersedes the 2026-07-14 dormancy edition — the
> fleet is **LIVE** again, not dormant. Everything below was verified
> against the tree at write time; per the truth bar, files and sibling
> HEADs win over this doc wherever they have since moved.

## 1 · What this repo is

fleet-manager is the fleet's source of truth and coordination hub: the
manager seat that steers the ~13-seat / ~19-repo agent fleet through
`control/` (owner-written `inbox.md` orders → manager-written `status.md`
heartbeat) and holds the cross-repo ledgers (roster, owner-queue, triage,
capabilities, dispatch log).

## 2 · Current state (as of 2026-07-15T10:21Z)

- **Fleet is LIVE** — the owner's v3.6 reboot wave ran overnight
  2026-07-15.
- The previous coordinator session ran the overnight ledger **fm PRs
  #215–#228** (all merged on green except **#227**, parked
  owner-merge-only — workflow-file diff). Its final heartbeat is
  `control/status.md` (phase: COORDINATOR SESSION ENDED).
- **Live lanes**: substrate-kit · gba · the idea-engine⇄sim-lab proposal
  loop (cycling fast). 9 seats remain un-rebooted **by owner choice**
  (hub, trading, games, idle, mineverse, forge, labs ×3) — neutral, no
  action owed until the owner sends their v3.6 prompts.

## 3 · Boot path for a fresh coordinator session (unchanged)

**HARD-SYNC first**: `git fetch origin main && git reset --hard
origin/main` on a clean tree (a dirty tree is a predecessor's work —
rescue-branch + push, never reset over it). Then read, in order:

1. `CONSTITUTION.md` (repo root) — the binding working agreement.
2. `control/status.md` — the last coordinator heartbeat.
3. `control/inbox.md` **at HEAD** — owner orders (newest at bottom).
4. [docs/roster.md](roster.md) + [docs/owner-queue.md](owner-queue.md) +
   [docs/playbook.md](playbook.md) (R1–R25 operating rules).

Verify: `check_roster_freshness.py` + `check_owner_queue.py` +
`check_trigger_health.py` (R26). Full boot text: the stored prompt in
[docs/prompts/v3/per-project/fleet-manager-startup.md](prompts/v3/per-project/fleet-manager-startup.md).

## 4 · Re-arm the wake chain (the outgoing session's triggers are GONE)

The outgoing coordinator retired its own triggers at close — the failsafe
`trig_012QyaM9wybnThRv8psNibve` and its pacemaker chain were deleted and
verified gone via `list_triggers`. **Nothing wakes this seat until you
re-arm it:**

1. **Failsafe cron** — name `Fleet Manager failsafe wake`, cron
   `30 */2 * * *` (the seat's slot in the stagger table,
   [docs/prompts/v3/per-project/README.md](prompts/v3/per-project/README.md)
   § "Failsafe cron stagger table"; a foreign trigger in the slot →
   report, never re-slot), prompt = the stored startup prompt (§3 link).
   Create fresh, then verify via `list_triggers` (paginate fully).
2. **Pacemaker** — ~15–30 min `send_later` continuation per working turn
   (Q-0265 pattern: ONE send_later per working turn, never stacked; the
   session ender arms nothing). Doctrine:
   [docs/prompts/v3/per-project/fleet-manager-custom-instructions.md](prompts/v3/per-project/fleet-manager-custom-instructions.md)
   and `docs/ROUTINES.md`.

## 5 · Open batons (waiting at handoff)

- **fm PR #227** — lanes.json regen fix, GREEN but parked
  **owner-merge-only** (workflow-file diff); needs one owner merge click
  (owner-queue **A#63**).
- **codetool-lab-fable5 PR #16** — owner merge click (owner-queue
  **A#62**).
- **superbot-next STALE** — its coordinator rebooted 04:20Z, stalled
  mid-close ~04:58Z; PR #490 sits born-red (card unflipped, auto-merge
  armed but held). Owner was advised live (~10:1xZ) to reply "continue"
  in that chat or boot a fresh v3.6 session. Verify at HEAD before
  acting; triage entry: [docs/fleet-triage.md](fleet-triage.md).
- **curious-research PARKED by owner** — no reboot; it gets a new
  mission later. Do not wake it.
- **ORDERs 023/024 owner-gated** — pending the owner-queue **E#44**
  consolidation-plan disposition; do not execute until the owner
  approves. (ORDERs 030–044 are lane-owned.)
- **9 seats un-rebooted by owner choice** (§2) — neutral; not a
  coordinator task.

## 6 · Older reference (archived program docs)

Still where they were: worklists
[docs/eap-final-night-worklists-2026-07-13.md](eap-final-night-worklists-2026-07-13.md),
audits [docs/eap-audit-collection.md](eap-audit-collection.md),
retrospective [docs/eap-retrospective.md](eap-retrospective.md) + story
[docs/eap-story.md](eap-story.md) + recon
[docs/eap-final-recon-2026-07-14.md](eap-final-recon-2026-07-14.md),
owner checklist (~47 rows open)
[docs/eap-owner-checklist-2026-07-14.md](eap-owner-checklist-2026-07-14.md),
email draft
[docs/eap-final-email-draft-2026-07-14.md](eap-final-email-draft-2026-07-14.md).
Reboot-night context: [docs/pre-reboot-review-2026-07-15.md](pre-reboot-review-2026-07-15.md).
central-docs-plan Phases 2–5 remain open
([docs/planning/2026-07-14-central-docs-plan.md](planning/2026-07-14-central-docs-plan.md)).
