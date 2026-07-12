# 2026-07-12 — ORDER 020 amendment: TICK PILE-UP signature + coordinator handover

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-12 ·
coordinator-dispatched build worker (successor coordinator's first slice)

## Declared at open (born-red)

Coordinator successor boot + ORDER 020 amendment (TICK PILE-UP signature).
Scope: I7 TICK-PILE-UP invariant in `scripts/check_trigger_health.py` + fresh
registry snapshot (`telemetry/triggers-snapshot.json`) + playbook R26
pacemaker-discipline note + CAPABILITIES send_message finding + inbox DONE
flip + coordinator heartbeat handover in `control/status.md`.

## Close-out

**Shipped (PR #142):**

- **I7 TICK-PILE-UP** in `scripts/check_trigger_health.py` (ORDER 020
  amendment 2026-07-12T19:20Z): FAIL when >1 PENDING (enabled, unfired)
  one-shot on one session carries near-identical normalized message text
  (ISO timestamps, `#hex` suffixes, digits stripped; stored prompt is the
  identity, name is the fallback). Long-fuse DISTINCT deliverables exempt.
  FAIL line names the session, tick ids oldest→newest, and the remedy:
  prune to the NEWEST tick; record the prune in the roster health column +
  control/status.md. Selfcheck extended (pile-up case, exempt long-fuse
  pair, fired-sibling case) — `--selfcheck` PASS.
- **Fresh snapshot** `telemetry/triggers-snapshot.json`: 945 records,
  captured_at 2026-07-12T20:41:13Z (trimmed 12-field re-export merged over
  the 18:25:51Z verbatim bodies; merge method, 7 created_at bounds, 3
  inter-capture deletions and the in-flight fm-failsafe cutover delta all
  documented in top-level `capture_notes`).
- **Check result: PASS 7/7** (evaluated 20:41Z capture instant). I7 first
  evaluation PASS — post-prune registry clean; the two same-session SWTK
  long-fuse checkpoints (T+7 / T+14) correctly exempted as distinct
  deliverables. **Replay proof:** the pre-prune 18:25:51Z snapshot reds I7
  on the incident's 4 stacked `session_01FMJoC5uC6WSUTosceTGcmo` pacemaker
  ticks (18:38/18:56/19:11/19:17Z, keep-newest named) — the amendment's
  done-when, evaluated on the real registry.
- **Playbook R26** extended with the pacemaker-discipline rule (one
  outstanding tick per session; re-arm only after consuming; silent
  nothing-to-do re-arms; I7 is the enforcement; prune-to-newest remedy).
- **docs/CAPABILITIES.md**: send_message to an INACTIVE session fails with
  `Cannot send events to inactive session (session_inactive)` — verified
  against 5 inactive seat sessions; only the mid-turn ACTIVE substrate-kit
  session accepted delivery. Cross-seat relay rides durable homes.
- **control/inbox.md**: append-only ORDER 020 amendment ✅ DONE flip
  (21:58Z). **control/status.md**: successor-coordinator heartbeat
  handover (seat ACTIVE, failsafe cutover, PASS 7/7, next-3, needs-owner).

**Verify:** `bootstrap.py check --strict` green except the designed born-red
session-gate hold on this card (flipped by this commit); roster-freshness OK
(0.5h); owner-queue CLEAN; trigger-health PASS 7/7 exit 0. Landing path:
park READY + green — owner-click / owner-provenance dispatch; no auto-merge
armed.

💡 Session idea: commit `scripts/gen_triggers_snapshot.py` — a transform
from a raw paginated list_triggers dump to the committed telemetry snapshot
schema (merge pages, dedupe, sort by id, stamp `captured_at`, carry verbatim
bodies forward when a re-export is trimmed), so every wake's R26
fresh-export stops being a hand-rolled transform — this session hand-built
it again (scratchpad `build_snapshot.py`), including a merge-over-prior-
bodies step the recipe in telemetry/README.md describes only as prose.
Dedup: grepped docs/ + scripts/ — no existing transform script; the recipe
exists only as README prose and ad-hoc session code.

⟲ Previous-session review: the predecessor coordinator's close-out was
exemplary — full 947-record routine disposition with verified terminal PR
states — but its final heartbeat listed #139/#140 as parked 8 minutes
before they merged (both MERGED 20:07Z), and it left send_message
reachability untested (this boot found the inactive-session wall).
Improvement: the session ender should re-check open-PR states one last time
before writing the heartbeat, or state "merge pending — verify at boot" so
the successor knows the line is a snapshot, not a fact.
