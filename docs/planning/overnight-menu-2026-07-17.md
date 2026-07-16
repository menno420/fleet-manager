# Overnight Planning Menu — 2026-07-17

> **Status:** `audit`
>
> A veto-ready menu of concrete fleet-manager seat proposals, generated
> overnight for the owner's morning filter-by-veto pass. Nothing here is
> built unless separately landed. Small ✅ items may ship as normal slices.

**Generated:** 2026-07-16 (overnight autonomous run, coordinator directive
2026-07-16 ~21:45Z — silence = consent, planning-mode fan-out).
**Scope:** the `fleet-manager` repo / seat — oversight machinery, checkers,
ORDER + roster + owner-queue tooling, telemetry. **Not** new product lanes
(those live in `docs/ideas/`).

## How to use this

Each proposal is independent and reversible-on-paper. Read the pitch, then
**veto what you don't want** — the survivors become `docs/planning/` plans
or `docs/ideas/` files in a later session. Effort is complexity, not time:
**S** = one checker/doc, **M** = a tool + wiring, **L** = a subsystem.
Risk: **✅** trivial · **↩️** reversible · **⚠** needs care.

Deduped against the 15 files in `docs/ideas/` and the 5 in `docs/planning/`
as of HEAD `68f7994` (roster Gen #74). Items that extend an existing idea
are marked **[extends …]**; everything else is new.

---

## Small (✅ / S) — checker, doc-drift, snapshot tooling

### S1 · Roster verdict-legend consistency checker
Every roster generation hand-uses the FRESH/STALE/DARK/DEAD/STALE-BY-DESIGN
legend; a typo'd or dropped verdict silently mis-classifies a seat. A tiny
`scripts/check_roster_legend.py` asserts every seat row carries exactly one
known verdict token and the legend block matches the rows used.
- **Effort:** S · **Risk:** ✅ · **Unblocks:** trustworthy roster reads; feeds S10/M12.

### S2 · Owner-queue slug + format linter [extends `check_owner_queue.py`]
The existing check verifies citations and slugs-intact; add format assertions:
every `OQ-` slug unique, uppercase-kebab, present in exactly one section, and
carrying the six-field grammar (or a `note:` explaining why not).
- **Effort:** S · **Risk:** ✅ · **Unblocks:** clean owner-queue at every read; prereq for M13 aging alarms.

### S3 · fleet-triage staleness advisory
`docs/fleet-triage.md` verdicts are dated 2026-07-11 (the 19-agent review) and
have not been re-verdicted since. A `scripts/check_triage_age.py` prints a WARN
line when any verdict block is older than N days (default 14), so stale keep/
archive calls surface instead of rotting.
- **Effort:** S · **Risk:** ✅ · **Unblocks:** the "verdicts as of 2026-07-11" drift the recon flagged tonight.

### S4 · Snapshot-freshness auto-note in the heartbeat
I6 SNAPSHOT-FRESH fails on a clock, not an event (tonight: 6.3h vs 4h bar), and
each session re-discovers it. Have `check_trigger_health.py` emit a one-line,
paste-ready status.md note ("trigger export N.Nh stale — refresh before acting")
so the heartbeat writer copies it instead of re-deriving.
- **Effort:** S · **Risk:** ✅ · **Unblocks:** the recurring I6-rediscovery tax every wake pays.

### S5 · Docs link-drift sweep
A stdlib `scripts/check_doc_links.py` walks `docs/**`, resolves every relative
markdown link, and reports dead targets + orphaned files (reachable from no
README). Catches the reachability class the substrate docs-gate only checks for
*new* files, across the *whole* tree.
- **Effort:** S · **Risk:** ✅ · **Unblocks:** doc-drift-you-can-see (bugs-first); complements the kit docs-gate.

### S6 · ORDER ledger auto-index
`control/inbox.md` is now 48 append-only ORDER blocks; finding "open at HEAD"
means grepping. A generator writes/refreshes a top-of-file TOC (order #, ISO
date, status, one-line title) so open vs done is readable at a glance without
scrolling 48 blocks.
- **Effort:** S · **Risk:** ↩️ (touches inbox — writer-owned; generate into a fenced managed block only) · **Unblocks:** faster inbox@HEAD reads; prereq for L21 lifecycle tooling.

### S7 · Claim-file format linter
`control/claims/*.md` must each carry `branch · scope · date`. A linter asserts
the shape and flags a claim whose branch has no live PR and is >N hours old
(stale-claim candidate), matching the GIT-HYGIENE stale rule.
- **Effort:** S · **Risk:** ✅ · **Unblocks:** collision detection; fewer orphaned claims.

### S8 · Trigger-health WARN digest line
`check_trigger_health.py` currently prints I1–I8 verbatim; the I8 duplicate-cron
WARN ×4 repeats every run. Collapse repeated WARNs into one digest line with a
count + the disposition owner ("keep-OLDEST is a sibling-lane call") so the
signal doesn't drown the PASS lines.
- **Effort:** S · **Risk:** ✅ · **Unblocks:** readable trigger-health output; less alarm fatigue.

### S9 · CAPABILITIES wall-age flagger
`docs/CAPABILITIES.md` walls carry a "re-verify >14d" rule that nothing enforces.
A checker flags any wall entry whose last-verified date is older than 14d, so a
stale "walled" claim gets re-probed instead of blocking work indefinitely.
- **Effort:** S · **Risk:** ✅ · **Unblocks:** the classifier-wall claims (ORDER 047/048 fan-out) going silently permanent.

### S10 · `fleet_status.py` delta column
`scripts/fleet_status.py` shows a per-seat snapshot; add a `--since <gen>` flag
that diffs against a prior roster generation and marks each seat ↑/↓/= (verdict
moved this run). One glance shows what changed overnight.
- **Effort:** S · **Risk:** ✅ · **Unblocks:** the morning "what moved while I slept" question this menu itself answers by hand.

---

## Medium (↩️ / M) — a tool + wiring

### M11 · Denial-corpus analytics from telemetry
Denial-routing records ("a declined call: record verbatim…") are scattered across
session cards and status blocks. Parse them into a structured corpus, cluster by
*shape* (classifier-wall / permission-prompt / scope-403 / quota-429), and rank
the top recurring walls. Turns "3× same shape = WALLS + flag" from a per-session
memory into a fleet-wide, queryable ledger.
- **Effort:** M · **Risk:** ↩️ · **Unblocks:** the ORDER 047/048 classifier-wall pattern is currently re-litigated every session with no aggregate view.

### M12 · Roster verdict automation
Today FRESH/STALE/DARK/DEAD is computed by hand each regen from heartbeat age +
commit age. Encode the rules (heartbeat<Nh → FRESH; heartbeat stale but commits
fresh → ACTIVE/INC; no signal + no orders → DARK; terminated → DEAD) in the
regen script so verdicts are derived, not typed — with a manual-override lane for
judgment cases (the superbot INC-16 "DARK-but-committing" class).
- **Effort:** M · **Risk:** ↩️ · **Unblocks:** removes the top roster-error source; makes S1's legend check load-bearing.

### M13 · Owner-queue aging alarms [extends S2]
The owner-queue has 60 active `OQ-` slugs; some (repo-admin, decisions/veto) sit
for weeks. Add age tracking (first-seen date per slug), sort each section
oldest-first, and emit escalation tiers (>7d note, >21d WARN, >45d "stale — close
or escalate"). The morning owner pass sees the oldest asks first.
- **Effort:** M · **Risk:** ↩️ · **Unblocks:** owner-queue items aging silently past usefulness.

### M14 · Landing-workflow presence auditor
ORDER 048 asks the manager to verify every repo has a server-side landing
workflow (superbot-next, superbot-games, gba-homebrew, pokemon-mod-lab named as
gaps). A checker reads each seat's `.github/workflows/` over raw-content and
reports which repos lack a merge-on-green equivalent — turning a manual
per-repo check into one command.
- **Effort:** M · **Risk:** ↩️ · **Unblocks:** ORDER 048 follow-up (4); recurring "does repo X auto-land?" question.

### M15 · Cross-session pacemaker / chain-death monitor
The wake-chain relies on one `send_later` pacemaker per turn; a dropped
pacemaker silently ends the chain (the WAKE-DEAD class). A monitor compares the
last failsafe-cron fire against expected cadence (`30 */2 * * *`) and flags a
missed window, so chain-death is detected instead of discovered hours later.
- **Effort:** M · **Risk:** ⚠ (touches trigger enumeration — coordinator-session bound; read-only audit only) · **Unblocks:** silent chain death between failsafe wakes.

### M16 · ORDER fan-out completion tracker
ORDER 047 and 048 are both `new` with their fan-out leg incomplete ("0 lane
inboxes cite them"). A tracker cross-references each open ORDER's done-when
against live lane inboxes (raw-content reads) and reports which fan-out targets
still lack the block — a standing "what's actually unfinished" board.
- **Effort:** M · **Risk:** ↩️ · **Unblocks:** the exact ORDER 047/048 blind spot the recon surfaced tonight.

### M17 · Roster heartbeat-vs-commit reconciler
The superbot hub is DARK on heartbeat (~3.2d) but FRESH on commits (~16m) →
manually re-classified ACTIVE (INC-16). Automate the reconciliation: when
heartbeat and commit-age disagree by a threshold, auto-tag the seat with the
INC class and the evidence, instead of a human noticing.
- **Effort:** M · **Risk:** ↩️ · **Unblocks:** false-DARK seats (active but quiet heartbeat) being mis-triaged.

### M18 · Nightly owner-digest generator
This menu was assembled by hand tonight. A generator that emits a single
morning digest — roster deltas (S10), owner-queue oldest items (M13), open
ORDERs + fan-out gaps (M16), trigger-health one-liner (S4/S8), PRs merged
overnight — gives the owner a one-screen "state of the fleet" for the veto pass.
- **Effort:** M · **Risk:** ↩️ · **Unblocks:** the owner's morning cold-scan; composes S4/S8/S10/M13/M16.

---

## Ambitious (⚠ / L) — a subsystem

### L19 · Cross-lane dependency tracking
Model which lanes block which (e.g. substrate-kit release → seat re-render;
fleet-manager ORDER → lane execution) as an explicit DAG in a machine-readable
file, and surface it in the roster so a blocked-upstream seat is flagged before
it stalls. Today dependencies live only in prose across ORDERs and status blocks.
- **Effort:** L · **Risk:** ⚠ (new model to keep in sync with reality) · **Unblocks:** invisible upstream blocks; smarter dispatch ordering.

### L20 · Recreated-projects A/B instrumentation
The EAP wind-down recreates every seat (cutover 2026-07-21). Instrument the
experiment: record per-seat baseline metrics pre-cutover (PR velocity, CI
green-rate, roster freshness, denial count) and the same post-recreation, so the
owner can *measure* whether recreation improved seat performance instead of
guessing.
- **Effort:** L · **Risk:** ⚠ (needs a stable metric definition before cutover — time-boxed by the 07-21 deadline) · **Unblocks:** an evidence answer to "did recreation help?"; feeds the whole wind-down retro.

### L21 · ORDER lifecycle state-machine tooling
Formalize ORDER states (new → dispatched → fanned-out → verified → done) with a
tool that validates transitions, blocks a "done" flip while fan-out targets are
unmet (M16), and renders the ledger as a live board. Turns the append-only
prose ledger into a tracked workflow without losing the append-only truth.
- **Effort:** L · **Risk:** ⚠ (must not fight the "FULL thread = truth" rule — state derived, never overwriting the prose) · **Unblocks:** ORDER 047/048-class "new but half-done" ambiguity; composes S6 + M16.

### L22 · Fleet telemetry warehouse
Unify the per-seat signals (heartbeats, denials, PR events, CI outcomes,
trigger fires) into one committed, append-only event store the manager reads
instead of scraping N repos over raw-content each wake. The single source that
S10/M11/M13/M16/M18 all currently reconstruct independently.
- **Effort:** L · **Risk:** ⚠ (schema + freshness discipline; forward-only) · **Unblocks:** every analytics proposal above stops re-deriving the same data.

### L23 · Automated staleness-sweep → ORDER pipeline
Close the loop: when the roster produces a DEAD/DARK verdict or a DARK seat with
no orders, auto-draft a candidate ORDER (or flag) into a review queue for the
manager to approve rather than hand-authoring each sweep disposition. The sweep
stops being a manual write.
- **Effort:** L · **Risk:** ⚠ (auto-drafting ORDERs — must stay a *proposal* queue, never auto-append to inbox) · **Unblocks:** the manual DEAD/DARK→ORDER routing step every sweep repeats.

### L24 · Self-auditing verdict loop
The manager makes roster/triage verdicts but never checks them against what
actually happened. A periodic auditor re-reads prior sweeps against subsequent
seat activity and scores accuracy (was a DARK seat actually dead? did a KEEP
seat produce anything?), feeding corrections back — the internal mirror of the
independent-reviewer idea, applied to the manager's own judgments.
- **Effort:** L · **Risk:** ⚠ (needs a fair scoring definition) · **Unblocks:** unmeasured manager-judgment drift; a quality signal on oversight itself.

### L25 · Owner-queue → paste-ready-console pipeline
Many owner-queue items are console/settings actions the owner must perform by
hand (repo admin, secrets, Railway splits). Extend the queue tooling to render
each such item as a fully paste-ready block (exact URL, exact clicks, exact
values) grouped by venue (GitHub / Railway / Claude console), so the owner's
session is copy-paste, never derive. Builds on the six-field + prep-owner-steps skill.
- **Effort:** L · **Risk:** ⚠ (must never embed secrets — reference env/vault only) · **Unblocks:** owner console-time friction; composes M13 + the prep-owner-steps skill.

---

## Summary table

| # | Proposal | Effort | Risk | New/Extends |
|---|---|---|---|---|
| S1 | Roster verdict-legend checker | S | ✅ | new |
| S2 | Owner-queue slug/format linter | S | ✅ | extends |
| S3 | fleet-triage staleness advisory | S | ✅ | new |
| S4 | Snapshot-freshness auto-note | S | ✅ | new |
| S5 | Docs link-drift sweep | S | ✅ | new |
| S6 | ORDER ledger auto-index | S | ↩️ | new |
| S7 | Claim-file format linter | S | ✅ | new |
| S8 | Trigger-health WARN digest | S | ✅ | new |
| S9 | CAPABILITIES wall-age flagger | S | ✅ | new |
| S10 | `fleet_status.py` delta column | S | ✅ | new |
| M11 | Denial-corpus analytics | M | ↩️ | new |
| M12 | Roster verdict automation | M | ↩️ | new |
| M13 | Owner-queue aging alarms | M | ↩️ | extends |
| M14 | Landing-workflow presence auditor | M | ↩️ | new |
| M15 | Pacemaker/chain-death monitor | M | ⚠ | new |
| M16 | ORDER fan-out completion tracker | M | ↩️ | new |
| M17 | Heartbeat-vs-commit reconciler | M | ↩️ | new |
| M18 | Nightly owner-digest generator | M | ↩️ | new |
| L19 | Cross-lane dependency tracking | L | ⚠ | new |
| L20 | Recreated-projects A/B instrumentation | L | ⚠ | new |
| L21 | ORDER lifecycle state-machine | L | ⚠ | new |
| L22 | Fleet telemetry warehouse | L | ⚠ | new |
| L23 | Staleness-sweep → ORDER pipeline | L | ⚠ | new |
| L24 | Self-auditing verdict loop | L | ⚠ | new |
| L25 | Owner-queue → paste-ready-console | L | ⚠ | extends |

**25 proposals — 10 S / 8 M / 7 L.** Several compose (M18 ← S4/S8/S10/M13/M16;
L22 ← M11/M13/M16; L21 ← S6/M16), so vetoing a foundation naturally prunes its
dependents. Recommended first-build set if the owner wants momentum without a
decision: **S3, S5, S9** (pure drift/staleness catchers, ✅, zero coupling).
