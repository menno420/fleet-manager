# 2026-07-11 — fleet instruction + environment audit (owner-directed, cross-repo)

> **Status:** `complete`

📊 Model: Claude Opus 4.8 · owner-directed cross-repo audit landed from a superbot session · night

## What this is (not a fleet-manager seat wake)

The owner, running the live fleet from claude.ai, asked a superbot session to
"compare all the projects' instructions to each other and find out if they can be
improved, same with the env/startup scripts, find which projects can reuse the
same scripts." This card records the artifact that session landed into
fleet-manager (via `add_repo` + a normal branch/PR). It is **not** a
fleet-manager coordinator wake — the manager's own routine still owns the repo;
this is an owner-relayed audit + ORDER.

## Landed this PR

1. `docs/findings/instruction-and-env-audit-2026-07-11.md` — the full synthesis
   from two read-only mapping agents (instructions comparison + env-script
   consolidation), every claim `file:line`-cited.
2. `docs/findings/README.md` — index row for the audit.
3. `control/inbox.md` — **ORDER 016 (P0)** directing the manager to act:
   route the merge-authority UNIVERSAL fix to the owner (owner-provenance),
   re-issue the walled lane instructions after it lands, and execute env R1/R5
   now + track R2/R3/R4/R6.

## Headline finding

The owner-landed `UNIVERSAL.md` merge clause ("arm auto-merge at creation / REST-
merge on green") prescribes the exact actions the auto-mode classifier terminally
denies — so **12 of 13 lanes carry the walled merge path as PRIMARY; only
substrate-kit is correct.** The kit's own `CAPABILITIES.md` already documents the
working recipe (open READY → the `auto-merge-enabler.yml` workflow lands it
server-side). Root fix = correct the UNIVERSAL block (owner lands it) → propagates
to every lane. Second finding: the 5 env archetypes are ~4-into-1 consolidatable
(one base shim + 3 knobs) and 5 live lanes are unregistered in `archetypes.md`.

## Boundaries respected

- Did NOT edit the owner-provenance `UNIVERSAL.md` block — §2.4 is a proposal for
  the owner to land (instruction-poisoning guard).
- Did NOT rewrite lane `instructions.md` (they derive from UNIVERSAL; re-issuing
  them before the owner lands the corrected block would create drift).
- No destructive actions; no merges attempted inside any Project session.

## 💡 Session idea

**A one-line CI guard that fails when a lane `instructions.md` contains an
agent-side merge verb.** The whole 12/13-walled problem would have been caught at
authoring time by a checker that greps each `projects/*/instructions.md` for
`enable_pr_auto_merge` / `merge_pull_request` / "REST merge-on-green" / "arm
auto-merge yourself" and reds if the enabler-only pattern isn't the one in force.
"Enforce, don't exhort" — the doctrine already lives in CAPABILITIES; a grep-gate
stops the wrong wording from being re-pasted into a new seat. Home: a
`scripts/check_merge_doctrine.py` in fleet-manager, advisory first.

## ⟲ Previous-session review

The gen-3 founding standard (`superbot docs/planning/gen3-deployment-standard`)
did a lot right — born-continuous seats, worker-seat scheduling fallback, the
calibration gate — but it inherited the walled merge wording from UNIVERSAL
without cross-checking it against the kit's *own* CAPABILITIES discovery from the
same day, so every new seat it founded was born with the classifier-walled merge
instruction. The system-level improvement: when a founding standard and a
capability ledger are edited the same day, the later edit should reconcile
against the other (a "same-day doctrine cross-check"), or a checker like the
session idea above should enforce it — otherwise a known wall gets re-encoded into
every downstream seat.
