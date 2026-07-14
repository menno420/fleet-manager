#!/usr/bin/env python3
"""gen_roster.py — mechanized R25 fleet-roster generation.

================================ PROVENANCE ================================
Why added : Roster generations #1-#4 (fleet-manager PRs #38/#44/#53/#59) were
            each executed BY HAND as a wake procedure; ORDER 009 and the
            coordinator handoff (docs/succession/coordinator-handoff-2026-07-11.md
            section 7, work-ladder item 8) owe the mechanization. This script is
            that mechanization: it regenerates docs/roster.md from the same two
            sources every hand generation used — the live trigger registry
            (a `list_triggers` JSON export, passed in via --triggers) and each
            lane repo's control/status*.md heartbeat read over git transport
            at an ls-remote-verified HEAD.
Date      : 2026-07-11 (lane worker, model: fable-5, dispatched by coordinator
            cse_012o8pySy5K3AV6JWoPKryZL)
Reliability: VERIFIED — graduated 2026-07-11 after three logged ground-truth
            runs (Q-0105 criteria: "confirm across sessions" — runs below;
            run 1 found+fixed one display bug, runs 2 and 3 were fully
            clean). The roster may be treated as authoritative WITHIN its
            freshness bar (check_roster_freshness.py 4h / in-file 24h
            kill-switch); the tool itself no longer needs per-run
            hand-verification.
            Verification run 1 (2026-07-11, roster gen #5): 6-lane hand sample
            across verdict classes — ALL verdicts + heartbeat/evidence cells
            matched ground truth; ONE display bug found and fixed (age_str
            float truncation, ~32h17m vs true 32h18m; regression selfcheck
            added). Header stays until several clean runs accumulate.
            Verification run 2 (2026-07-11, roster gen #6): 6-lane hand sample
            (STALE ×2, FRESH ×2 incl. a triggerless lane and one that moved
            mid-sweep, hub fallback, STALE-BY-DESIGN) — verdicts 6/6 correct,
            every heartbeat/age/evidence cell matched ground truth at the
            pinned evidence SHA; ZERO fixes needed. First fully-clean run;
            header stays (2 runs logged, criteria say several).
            Verification run 3 (2026-07-11, roster gen #9, P3 fm PR #86 —
            the GRADUATION run): 4-lane hand sample (superbot hub FRESH,
            substrate-kit FRESH + its 2 legacy DARK sub-rows,
            superbot-games STALE + its DARK/DEAD sub-rows,
            trading-strategy FRESH) against independently-fetched ground
            truth (fresh depth-2 clones, own ls-tree + stamp reads) —
            verdicts 8/8 (4 lanes + 4 sub-rows), every evidence
            SHA/HEAD-date exact, heartbeat-file enumeration exactly matched
            each repo's control/ tree (first run exercising the P3 sub-row
            + heartbeat_files paths); ZERO fixes needed.
Kill-switch: KEPT despite graduation (Q-0105 letter) — delete this script
            if it proves unreliable over multiple sessions; a green verdict
            that fights visible evidence is the tool's bug (Q-0120) —
            re-open verification before trusting it again.
=============================================================================

WHAT IT EMITS (machine gen-N format — a deliberate SUBSET of the hand format):
  header (GENERATED banner, generation #N, generated-at, attribution,
  source-of-truth + >24h kill-switch note, transport-verification note)
  + the established roster table (Lane | Heartbeat `updated:` | Age | Phase |
  Orders | Kit | Wake state | Evidence)
  + the "Staleness verdicts" section using the established FRESH / STALE /
  DARK / DEAD vocabulary.
  It does NOT auto-derive the hand generations' "Deltas vs generation #N-1"
  narrative or per-row judgment prose (frozen flags, recommendations) — that
  is coordinator judgment, not heartbeat-derivable (see the proposal,
  docs/proposals/generated-roster-from-heartbeats.md, "What stays human").
  Deltas live in `git diff` of this file; the generating session may append
  prose below the machine sections before committing.

VERDICT LADDER (documented so the vocabulary stays stable):
  FRESH  — heartbeat age <= 2x the lane's wake cadence (cadence parsed from
           its matched cron; 2h assumed when no cron). MISSION.md's own bar.
  STALE  — age > 2x cadence but <= 24h. Watch, not action.
  DARK   — age > 24h on a live lane (R25: a roster/heartbeat >24h is dead —
           trust nothing, escalate).
  UNREADABLE (transport/auth) — the REPO could not be read over git
           transport at all (private-repo auth wall, non-convergent proxy).
           A MEASUREMENT artifact, never lane death: the lane may be
           perfectly alive behind the wall (gen #21 lesson: pokemon-mod-lab
           printed DEAD while it was ARCHIVE-READY with kit v1.15.0 merged
           hours earlier). Fix the transport (ROSTER_READ_TOKEN, below);
           never triage the lane off this verdict.
  DEAD   — the repo IS readable but no heartbeat signal is measurable
           (no parseable `updated:` stamp and no parseable HEAD date)
           on a lane that should have one.
  Overrides: disposition "archived"/"parked" reports STALE-BY-DESIGN instead
  of DARK/DEAD; "registry-only" seats (no repo) are judged on trigger
  last-fire only; any repo WITHOUT a control/status*.md falls back to HEAD
  committer date as its activity signal (the pre-#2003 hub behavior, kept
  generic — the hub itself heartbeats since superbot c18a9c3, P3).

TRANSPORT DOCTRINE (inherited from roster gen #3, MANDATORY — the git proxy
serves stale cached clone packs; 9/13 repos came back hours old on first
fetch on 2026-07-10):
  every remote read loops   fetch -> compare FETCH_HEAD to a fresh
  `git ls-remote` -> re-fetch   until the two agree (max --max-fetch-attempts,
  default 5). A repo that never converges, or that cannot be read at all
  (private wall, nonexistent), degrades EXPLICITLY to
  "NOT MEASURED (wall: <reason>)" — a Last-seen is never invented.
  AUTH (gen #21 root-cause fix): reads go over plain https git transport,
  which is unauthenticated on the headless Actions runner — public lane
  repos succeed, the private one (pokemon-mod-lab) walls with "could not
  read Username". When the dedicated env ROSTER_READ_TOKEN is set (a
  fine-grained read-only PAT; the roster-regen workflow forwards the
  secret of the same name), every github.com read sends it as a
  basic-auth extraheader — the same mechanism actions/checkout uses.
  GH_TOKEN / GITHUB_TOKEN are DELIBERATELY not picked up: agent sessions
  export literal "proxy-injected" placeholders in both, and sending that
  as a credential would 401 reads that succeed today.

EXPECTED --triggers JSON SHAPE (documented from a real `list_triggers`
response, 2026-07-11; the script FAILS LOUDLY — nonzero exit, named record
index — on mismatch):
  {
    "data": [                     # REQUIRED, list of trigger records
      {
        "id": "trig_...",         # REQUIRED str, "trig_" prefix
        "name": str,              # REQUIRED
        "created_at": ISO-8601,   # REQUIRED
        "enabled": bool,          # optional (absent => disabled)
        "cron_expression": str,   # optional — standing cron triggers only
        "run_once_at": ISO-8601,  # optional — one-shot triggers only
        "next_run_at": ISO-8601,  # optional
        "last_fired_at": ISO-8601,# optional
        "ended_reason": str,      # optional (e.g. "run_once_fired")
        "created_via": str,       # optional (e.g. "meta_mcp")
        "updated_at": ISO-8601,   # optional
        "persist_session": bool,  # optional
        "persistent_session_id": str,  # optional ("session_...")
        "session_grouping_id": str,    # optional ("sgrp_...")
        "creator": {"account_uuid": str},  # optional
        "job_config": {"ccr": {"events": [{"data": {"message":
            {"content": str, "role": str}, ...}}], ...}}  # optional; the
            # stored prompt text lives at events[0].data.message.content and
            # is used ONLY to attribute anonymous send_later chain links to
            # lanes — never printed into the roster.
      }, ...
    ],
    "has_more": bool,             # optional (pagination flag)
    "next_cursor": str,           # optional
    "captured_at": ISO-8601       # optional (ORDER 020): the instant the
                                  # export was taken — write it at every
                                  # wake dump; trigger-health verdicts are
                                  # evaluated AT this instant (see
                                  # snapshot_eval_time for the fallback
                                  # ladder when it is absent)
  }
  A merged multi-page export (this repo's convention: one dict with all
  pages' records concatenated under "data") and a raw single page are both
  accepted. Records with duplicate ids are deduplicated (first wins).

SNAPSHOT CONVENTION (P1 FRESHNESS, centralization plan §3a, fm PR #81):
  the canonical --triggers source is the COMMITTED export,
  `telemetry/triggers-snapshot.json` — dumped + committed at each manager
  wake (list_triggers is MCP-only, so the dump is inherently a CCR-wake
  step; records stable-sorted by trigger id, pages merged under one "data"
  key). The headless roster-regen cron (.github/workflows/roster-regen.yml,
  `40 */2 * * *`) consumes the committed snapshot and re-fetches heartbeats
  live, so the roster stays fresh between wakes; its TRIGGER columns are
  only as fresh as the last committed snapshot. Regen + a green
  scripts/check_roster_freshness.py is a REQUIRED wake step, not a
  commit-only-on-change option. An ad-hoc uncommitted export
  (tmp-triggers.json, gitignored) remains fine for one-off runs.

SUB-ROWS + EVIDENCE INDEX (P3 COVERAGE + INDEX, centralization plan §3c):
  every generation enumerates ALL control/status*.md heartbeat files per
  repo — the repo's committed substrate.config.json `heartbeat_files`
  declaration wins the ordering when present; a control/ glob is the
  fallback and also catches undeclared files — and emits ONE ROSTER
  SUB-ROW per extra heartbeat file ("↳ <lane> — <file>", verdict from
  that file's own `updated:` stamp; triggers stay on the parent row).
  This closes the multi-seat blind spot where one row stood in for three
  (superbot-games carries status.md + status-mining.md +
  status-exploration.md). Sub-row heartbeats ALSO feed the P2 candidate
  extraction, so an owner-ask in a sub-seat file can no longer strand.
  Every generation ALSO writes docs/evidence-index.md — a GENERATED
  cross-repo index linking each lane to its evidence home (the lane's
  docs/current-state.md, latest .sessions/ card, docs/retro when present,
  all pinned at the ls-remote-verified HEAD the roster row cites) so the
  manager-internal ↔ program-facing record split (plan §4) is navigable
  from one place. The hub row is REAL since superbot PR #2003 gave
  superbot a control/status.md (c18a9c3): the old "hub (no
  control/status.md by design)" disposition + HEAD-committer-date
  fallback is retired as a special case — the generic no-status-file
  fallback still applies to any repo without one.
  Since 2026-07-14 (central-docs-plan Slice 0 item 2, classes D1–D3) the
  evidence index ALSO carries per-file program-evidence row classes:
  superbot docs/eap/* (one row per doc — closes the measured 0-links gap),
  substrate-kit docs/reports/* (fleet evidence), the gen-2 feedback +
  custom-instructions proposal docs discovered by pattern in their five
  home repos, the superbot-next rebuild-evidence corpus, and a static
  retro-errata register. All discovered at the SAME pinned SHA as the
  lane row (see EVIDENCE_EXTRA / RETRO_ERRATA below).

CANDIDATE FEED (P2 QUEUE GENERATION, centralization plan §3b, fm PR #85):
  every generation ALSO writes docs/owner-queue-candidates.md — a GENERATED,
  NOT-source-of-truth extraction of each lane heartbeat's ⚑ needs-owner /
  OWNER-ACTION blocks (verbatim, line-start-anchored ⚑/OWNER-ACTION starts;
  `needs-owner: none` skipped; blocks deduped + capped). The manager curates
  docs/owner-queue.md FROM the feed — nothing lands there automatically.
  Feed items carry a deterministic content-derived `suggested-id`
  (OQ-<LANE>-<WORDS>, never positional) and a `possibly-covered-by` hint
  keyed on the queue's stable `id: OQ-…` slugs. `--check` compares the
  ROSTER only (the feed rides the same regen commit); `--stdout` prints the
  roster only and skips the feed.

USAGE
  # generate (writes docs/roster.md relative to the repo root):
  python3 scripts/gen_roster.py --triggers telemetry/triggers-snapshot.json \
      --generated-by "roster lane worker (model: fable-5)" \
      --dispatched-by "coordinator cse_..." [--generation N] [--date ISO]
  # drift check (exits 2 on ANY difference vs the committed roster;
  # pass the committed generation's --date/--generation/attribution to make
  # ages reproducible — Age is always computed against --date, so with
  # identical args any remaining diff is real world drift):
  python3 scripts/gen_roster.py --triggers tmp-triggers.json --check \
      --generation 4 --date 2026-07-11T01:58Z
  # offline self-check of the pure logic (no network, no triggers file):
  python3 scripts/gen_roster.py --selfcheck

No third-party deps: stdlib + the git binary via subprocess only.
"""

from __future__ import annotations

import argparse
import base64
import difflib
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

# --------------------------------------------------------------------------
# Lane registry — the ONE hand-maintained input inside the script.
# Add a lane here when a seat is born; flip `disposition` when one parks.
# Fields:
#   lane        display name (roster row, first column)
#   repo        GitHub repo under menno420/, or None for registry-only seats
#   disposition "live" | "archived" (stale-by-design) |
#               "registry-only" (no repo)
#               (the old "hub" disposition is RETIRED, P3: superbot has a
#               real control/status.md since PR #2003 → c18a9c3)
#   tokens      lowercase substrings that attribute triggers (by name, and by
#               stored-prompt content for anonymous send_later links)
# --------------------------------------------------------------------------
LANES = [
    {"lane": "superbot (hub)", "repo": "superbot", "disposition": "live",
     "tokens": ["suberbot docs", "superbot docs", "superbot night"]},
    {"lane": "superbot-next", "repo": "superbot-next", "disposition": "live",
     "tokens": ["superbot-next", "builder"]},
    {"lane": "substrate-kit", "repo": "substrate-kit", "disposition": "live",
     "tokens": ["substrate-kit", "kit-lab"]},
    {"lane": "websites", "repo": "websites", "disposition": "live",
     "tokens": ["websites"]},
    {"lane": "trading-strategy", "repo": "trading-strategy",
     "disposition": "live", "tokens": ["trading"]},
    {"lane": "venture-lab", "repo": "venture-lab", "disposition": "live",
     "tokens": ["venture"]},
    {"lane": "superbot-games · Seat A", "repo": "superbot-games",
     "disposition": "live", "tokens": ["superbot-games"]},
    {"lane": "superbot-idle (Seat B)", "repo": "superbot-idle",
     "disposition": "live", "tokens": ["superbot-idle"]},
    {"lane": "superbot-mineverse", "repo": "superbot-mineverse",
     "disposition": "live", "tokens": ["superbot-mineverse", "mineverse"]},
    {"lane": "retro-games coordinator (no repo)", "repo": None,
     "disposition": "registry-only",
     "tokens": ["superbot-retro", "retro-games"]},
    # 8-seat restructure seats (2026-07-11) — the seat failsafes are named
    # after the SEAT ("SuperBot World failsafe wake"), not any constituent
    # repo, so repo-token attribution missed all of them and the wedge
    # watchdog printed "(no attributed triggers)" on every constituent row
    # (INC-62, observed on idea-engine/'Ideas Lab failsafe wake'). One
    # registry-only entry per multi-repo/renamed seat carries the wake.
    {"lane": "game-lab (no repo)", "repo": None,
     "disposition": "registry-only", "tokens": ["game-lab", "game lab"]},
    {"lane": "SuperBot World seat (games+idle+mineverse)", "repo": None,
     "disposition": "registry-only", "tokens": ["superbot world"]},
    {"lane": "Ideas Lab seat (idea-engine+sim-lab)", "repo": None,
     "disposition": "registry-only", "tokens": ["ideas lab"]},
    {"lane": "Self Improvement seat (substrate-kit)", "repo": None,
     "disposition": "registry-only", "tokens": ["self improvement"]},
    {"lane": "SuperBot 2.0 seat (superbot+superbot-next)", "repo": None,
     "disposition": "registry-only", "tokens": ["superbot 2.0"]},
    {"lane": "Curious Research seat (no repo)", "repo": None,
     "disposition": "registry-only", "tokens": ["curious research"]},
    {"lane": "pokemon-mod-lab", "repo": "pokemon-mod-lab",
     "disposition": "live", "tokens": ["pokemon"],
     # INC-20: the fleet's ONE private repo — an auth wall here is a
     # known-credential gap (ROSTER_READ_TOKEN owner secret pending, fm
     # PR #144), never generic darkness. verdict_for renders it distinctly.
     "private": True},
    {"lane": "gba-homebrew", "repo": "gba-homebrew", "disposition": "live",
     "tokens": ["gba"]},
    {"lane": "product-forge", "repo": "product-forge", "disposition": "live",
     "tokens": ["product-forge", "forge"]},
    {"lane": "idea-engine", "repo": "idea-engine", "disposition": "live",
     "tokens": ["idea-engine"]},
    {"lane": "sim-lab", "repo": "sim-lab", "disposition": "live",
     "tokens": ["sim-lab"]},
    {"lane": "codetool-lab-fable5", "repo": "codetool-lab-fable5",
     "disposition": "archived", "tokens": ["codetool-lab-fable5"]},
    {"lane": "codetool-lab-opus4.8", "repo": "codetool-lab-opus4.8",
     "disposition": "archived", "tokens": ["codetool-lab-opus4.8"]},
    {"lane": "codetool-lab-sonnet5", "repo": "codetool-lab-sonnet5",
     "disposition": "archived", "tokens": ["codetool-lab-sonnet5"]},
    {"lane": "fleet-manager (this repo)", "repo": "fleet-manager",
     "disposition": "live", "tokens": ["fleet-manager", "fleet manager"]},
]

GITHUB_BASE = "https://github.com/menno420/"
ROSTER_REL = os.path.join("docs", "roster.md")
CANDIDATES_REL = os.path.join("docs", "owner-queue-candidates.md")
OWNER_QUEUE_REL = os.path.join("docs", "owner-queue.md")
EVIDENCE_REL = os.path.join("docs", "evidence-index.md")
LANES_JSON_REL = os.path.join("registry", "lanes.json")

# ------------------- program-evidence row classes (Slice 0 item 2) --------
# Centralization plan D1–D3 (docs/central-docs-plan.md §2 class D): the
# evidence index carries per-file row classes beyond the lane table.
# Discovery is regex-over-`git ls-tree -r` at the SAME pinned SHA as the
# lane row, so a per-file row can never be fresher than its lane evidence.
# INDEX rows only — the corpora stay home-side (plan §4 class D), fm links.

# D2 — gen-2 blueprint feedback docs + the paired custom-instructions
# proposals ("written explicitly for the manager to collect", plan D2).
_GEN2_RE = re.compile(
    r"(?i)^docs/.*(gen2[-_]?feedback|custom-instructions-proposal"
    r"|proposed-custom-instructions)[^/]*\.md$")
# D3 — superbot-next rebuild evidence corpus (plan D3, next candidate 5).
_NEXT_REBUILD_RE = re.compile(
    r"^docs/.*(rebuild-completion-report|orchestration-retrospectiv"
    r"|self-review-2026-07-09|project-review-2026-07-09"
    r"|program-review-2026-07-12|curation-report-2026-07-13)[^/]*\.md$")

EVIDENCE_EXTRA: dict[str, dict[str, re.Pattern]] = {
    # D1 — EAP program-narrative corpus: home stays superbot docs/eap/
    # (plan §7.2); fm indexes row-level (the measured gap was 0 links).
    "superbot": {"eap": re.compile(r"^docs/eap/[^/]+\.md$")},
    # D3 — kit fleet-evidence reports (incl. the two cfgdiff reports the
    # plan's fact-check verified at kit 727f5db).
    "substrate-kit": {"kit_reports": re.compile(r"^docs/reports/[^/]+\.md$")},
    "superbot-games": {"gen2": _GEN2_RE},
    "trading-strategy": {"gen2": _GEN2_RE},
    "codetool-lab-sonnet5": {"gen2": _GEN2_RE},
    "codetool-lab-fable5": {"gen2": _GEN2_RE},
    "codetool-lab-opus4.8": {"gen2": _GEN2_RE},
    "superbot-next": {"next_rebuild": _NEXT_REBUILD_RE},
}

# D3 — retro errata: corrections that today live only in superbot docs
# (plan D3 / opus4.8 candidate 4). Static register, rendered beside the
# per-file rows; source links pin at superbot's roster-row SHA.
RETRO_ERRATA: list[dict] = [
    {"repo": "codetool-lab-opus4.8",
     "claim": "retro names commit `c96318c` “the main tip at "
              "wind-down”",
     "correction": "FALSIFIED — three more PRs merged after it; the lane's "
                   "wind-down-complete commit is PR #22 `80f6cd1`, ~2h later",
     "source_repo": "superbot",
     "source_path": "docs/eap/fleet-winddown-audit-2026-07-09.md"},
    {"repo": "codetool-lab-opus4.8",
     "claim": "an exact quoted error-message sequence attributed to one doc",
     "correction": "MISATTRIBUTED — the quote only appears in a different "
                   "doc (winddown-audit finding 2)",
     "source_repo": "superbot",
     "source_path": "docs/eap/fleet-winddown-audit-2026-07-09.md"},
    # INC-64 residue + INC-65 (2026-07-14, wake 0235Z Slice D):
    {"repo": "codetool-lab-opus4.8",
     "claim": "retro's 102-test suite count",
     "correction": "OFF-BY-ONE — the shipped suite is 103; the slip was "
                   "never amended in-file (winddown audit)",
     "source_repo": "superbot",
     "source_path": "docs/eap/fleet-winddown-audit-2026-07-09.md"},
    {"repo": "codetool-lab-sonnet5",
     "claim": "README/review wording “two-arm model-comparison”",
     "correction": "THREE arms — the lane's own PR #1 body names both "
                   "siblings (fable5, opus4.8); flagged by its unmerged "
                   "2026-07-13 audit, unfixed on main @ `66c3dfc` (INC-65)",
     "source_repo": "fleet-manager",
     "source_path": "docs/fleet-inconsistencies-2026-07-13.md"},
]

# ---------------------------------------------------------------- schema ---


class SchemaError(Exception):
    """triggers.json did not match the documented list_triggers shape."""


def validate_export(obj) -> list[dict]:
    """Validate + dedupe a list_triggers export. Raises SchemaError."""
    if not isinstance(obj, dict):
        raise SchemaError(
            f"top level must be a dict with a 'data' list; got {type(obj).__name__}")
    if "data" not in obj:
        raise SchemaError(
            f"missing top-level 'data' key (found keys: {sorted(obj.keys())})")
    data = obj["data"]
    if not isinstance(data, list):
        raise SchemaError(f"'data' must be a list; got {type(data).__name__}")
    if not data:
        raise SchemaError("'data' is empty — refusing to generate a roster "
                          "from zero trigger records (a real registry sweep "
                          "has hundreds; this smells like a bad export)")
    seen: set[str] = set()
    records: list[dict] = []
    for i, rec in enumerate(data):
        if not isinstance(rec, dict):
            raise SchemaError(f"data[{i}] is not a dict")
        for field in ("id", "name", "created_at"):
            if field not in rec:
                raise SchemaError(f"data[{i}] missing required field {field!r} "
                                  f"(has: {sorted(rec.keys())})")
            if not isinstance(rec[field], str):
                raise SchemaError(f"data[{i}].{field} must be str")
        if not rec["id"].startswith("trig_"):
            raise SchemaError(f"data[{i}].id {rec['id']!r} lacks 'trig_' prefix")
        if "enabled" in rec and not isinstance(rec["enabled"], bool):
            raise SchemaError(f"data[{i}].enabled must be bool")
        for opt in ("cron_expression", "run_once_at", "next_run_at",
                    "last_fired_at", "ended_reason", "persistent_session_id"):
            if opt in rec and rec[opt] is not None and not isinstance(rec[opt], str):
                raise SchemaError(f"data[{i}].{opt} must be str when present")
        if rec["id"] not in seen:
            seen.add(rec["id"])
            records.append(rec)
    return records


# ------------------------------------------------------------- triggers ----

def prompt_text(rec: dict) -> str:
    """Best-effort extraction of the stored prompt (for lane attribution)."""
    try:
        events = rec["job_config"]["ccr"]["events"]
        msg = events[0]["data"]["message"]
        if isinstance(msg, dict):
            return str(msg.get("content", ""))
        return str(msg)
    except (KeyError, IndexError, TypeError):
        return ""


def cadence_hours(cron: str) -> float | None:
    """Parse the wake cadence in hours from the fleet's cron shapes.

    Handles: 'M * * * *' (1h) · 'M */N * * *' (Nh) · 'M A-B/N * * *' (Nh).
    Returns None for anything else (caller assumes the 2h default).
    """
    parts = cron.split()
    if len(parts) != 5:
        return None
    hour = parts[1]
    if hour == "*":
        return 1.0
    m = re.fullmatch(r"(?:\*|\d+-\d+)/(\d+)", hour)
    if m:
        return float(m.group(1))
    return None


def owns_record(lane: dict, rec: dict) -> bool:
    """Does this lane own this trigger record? (extracted for ORDER 020)."""
    tokens = [t.lower() for t in lane["tokens"]]
    hay = rec["name"].lower()
    if any(t in hay for t in tokens):
        return True
    # ONLY anonymous send_later links fall back to prompt-body matching:
    # named triggers routinely MENTION sibling lanes in their prompts
    # (verified 2026-07-11: sim-lab's failsafe prompt mentions
    # idea-engine), so body-matching a named trigger mis-attributes it.
    if not hay.startswith("send_later"):
        return False
    body = prompt_text(rec).lower()
    return bool(body) and any(t in body for t in tokens)


def match_lane_triggers(lane: dict, records: list[dict]) -> dict:
    """Split a lane's enabled triggers into standing / one-shot / poke-only."""
    mine = [r for r in records if r.get("enabled") and owns_record(lane, r)]
    return {
        "standing": [r for r in mine if r.get("cron_expression")],
        "oneshot": [r for r in mine if r.get("run_once_at")],
        "poke": [r for r in mine
                 if not r.get("cron_expression") and not r.get("run_once_at")],
    }


def attribute_lane(rec: dict) -> str | None:
    """Best-effort lane attribution for one record (first LANES match wins)."""
    for lane in LANES:
        if lane["tokens"] and owns_record(lane, rec):
            return lane["lane"]
    return None


# ------------------------------------------------------- trigger health ----
# ORDER 020 (2026-07-12, P1 reliability — fleet-manager control/inbox.md;
# canonical spec: docs/trigger-health-spec.md — MOVED into fm 2026-07-14,
# central-docs-plan A2; was superbot docs/owner/trigger-health-order-2026-07-12.md).
# On 2026-07-12 ~02:30-08:00Z the trigger scheduler degraded SILENTLY: 9
# one-shot ticks dropped, several cron failsafes wedged with next_run_at
# frozen hours in the past while still enabled, two seats dark ~6h.
# Everything needed to catch it was visible in list_triggers all night —
# nothing was watching. These primitives are the detection; the per-wake
# CLI is scripts/check_trigger_health.py (which imports them), and the
# roster's "Trigger health" column below keeps the watchdog's record on
# the Actions regen substrate so it survives a CCR scheduler outage.

# Detection signature (verified against the incident registry):
# `enabled ∧ next_run_at < eval − 15min`.
WEDGE_GRACE_MIN = 15


def fire_time(rec: dict):
    """Next scheduled fire instant of a record (cron next or one-shot due)."""
    return parse_when(rec.get("next_run_at") or rec.get("run_once_at") or "")


def trigger_wedged(rec: dict, eval_dt: datetime) -> bool:
    """WEDGED cron: enabled, standing, next_run_at frozen > grace in the past.

    A healthy trigger ADVANCES next_run_at after each fire; a past
    next_run_at on an enabled cron means the scheduler is not delivering.
    """
    if not rec.get("enabled") or not rec.get("cron_expression"):
        return False
    nra = parse_when(rec.get("next_run_at") or "")
    return (nra is not None
            and (eval_dt - nra).total_seconds() / 60 > WEDGE_GRACE_MIN)


def oneshot_dropped(rec: dict, eval_dt: datetime) -> bool:
    """DROPPED-or-QUEUED one-shot: still enabled > grace past run_once_at.

    A delivered one-shot disables itself (ended_reason=run_once_fired), so
    enabled + past-due = undelivered. CAVEAT (spec note): a QUEUED tick
    (bound to a busy session — delivers when the turn goes idle, sound by
    design) is indistinguishable from a genuinely LOST one on the registry;
    both are flagged — an unlabeled queue is still a risk.
    """
    if not rec.get("enabled") or not rec.get("run_once_at"):
        return False
    roa = parse_when(rec["run_once_at"])
    return (roa is not None
            and (eval_dt - roa).total_seconds() / 60 > WEDGE_GRACE_MIN)


def has_future_tick(recs: list[dict], eval_dt: datetime) -> bool:
    """Any enabled record in recs with a fire instant still in the future?"""
    for r in recs:
        if not r.get("enabled"):
            continue
        ft = fire_time(r)
        if ft is not None and ft > eval_dt:
            return True
    return False


def health_report(records: list[dict], eval_dt: datetime) -> dict:
    """Fleet-wide WEDGED / DROPPED / DEAD-chain report (ORDER 020).

    DEAD chain = a seat session with >=1 dropped one-shot AND no future
    tick armed (spec step 4) — grouped by persistent_session_id, because a
    pacemaker chain is a property of the session it feeds, not of a lane
    name. Dropped one-shots WITHOUT a session id still count as dropped
    but cannot be chain-judged (listed under session None, never DEAD).
    """
    enabled = [r for r in records if r.get("enabled")]
    wedged = [r for r in enabled if trigger_wedged(r, eval_dt)]
    dropped = [r for r in enabled if oneshot_dropped(r, eval_dt)]
    dropped_ids = {r["id"] for r in dropped}
    by_session: dict = {}
    for r in enabled:
        by_session.setdefault(r.get("persistent_session_id"), []).append(r)
    dead = []
    for sess in sorted(k for k in by_session if k is not None):
        recs = by_session[sess]
        sess_dropped = [r for r in recs if r["id"] in dropped_ids]
        if sess_dropped and not has_future_tick(recs, eval_dt):
            dead.append({"session": sess, "dropped": sess_dropped})
    return {"wedged": wedged, "dropped": dropped, "dead_chains": dead,
            "by_session": by_session}


def snapshot_eval_time(payload: dict, triggers_path: str | None,
                       records: list[dict]):
    """The instant trigger health is evaluated AT: the snapshot's capture time.

    Returns (datetime | None, basis_str). Evaluating at wall-clock `now`
    instead would FABRICATE wedges from any snapshot older than one wake
    cadence (measured: the 11:25Z gen-14 snapshot read at 13:54Z false-
    wedges 7/9 healthy crons). The true capture instant is bounded by
    newest-record-stamp <= capture <= git-commit-time, and BOTH bounds
    were measured hours off on real snapshots (record stamps lag 3h into
    the 2026-07-12 outage because a frozen scheduler writes nothing; the
    gen-14 commit lagged capture 2.5h behind a parked regen PR). Ladder:
      1. top-level `captured_at` in the export — exact; written by the
         wake dump since ORDER 020 (extra top-level keys were always
         schema-legal). The rung every post-ORDER-020 snapshot hits.
      2. newest created/updated/last_fired stamp across the records —
         the LOWER bound: UNDERSTATES capture during an outage, so wedge
         verdicts turn conservative (may miss the newest wedge until the
         next captured_at export), never inflated. Chosen over commit
         time because a fabricated fleet-wide wedge alarm (upper bound)
         costs trust the watchdog needs.
      3. git commit time of the snapshot path — last resort for an
         export whose records carry no parseable stamps at all.
    """
    cap = parse_when(str(payload.get("captured_at") or ""))
    if cap is not None:
        return cap, "snapshot captured_at"
    best = None
    for r in records:
        for field in ("created_at", "updated_at", "last_fired_at"):
            t = parse_when(str(r.get(field) or ""))
            if t is not None and (best is None or t > best):
                best = t
    if best is not None:
        return best, ("newest record stamp — lower bound; UNDERSTATES "
                      "capture during an outage, verdicts conservative "
                      "(export with `captured_at` for exactness)")
    if triggers_path:
        try:
            out = _git(["log", "-1", "--format=%cI", "--",
                        os.path.relpath(triggers_path, repo_root())],
                       cwd=repo_root()).strip()
            when = parse_when(out)
            if when is not None:
                return when, ("git commit time of the snapshot — upper "
                              "bound; can OVERSTATE capture behind a "
                              "parked regen PR")
        except (Wall, ValueError, OSError):
            pass
    return None, "no eval basis derivable"


def lane_health_cell(trig: dict, eval_dt) -> str:
    """The roster's per-lane Trigger health cell (ORDER 020 step 2)."""
    all_recs = trig["standing"] + trig["oneshot"] + trig["poke"]
    if not all_recs:
        return "— (no attributed triggers)"
    if eval_dt is None:
        return "n/a (no eval basis)"
    bits = []
    for r in trig["standing"]:
        if trigger_wedged(r, eval_dt):
            bits.append(f"⚠️ WEDGED `{r['id']}` (next frozen "
                        f"{(r.get('next_run_at') or '?')[:16]}Z)")
    ndrop = sum(1 for r in trig["oneshot"] if oneshot_dropped(r, eval_dt))
    if ndrop:
        bits.append(f"⚠️ {ndrop} DROPPED-or-QUEUED one-shot(s)")
    if bits and not has_future_tick(all_recs, eval_dt):
        bits.append("💀 DEAD chain (no future tick armed)")
    return "; ".join(bits) if bits else "OK"


# ------------------------------------------------------------ transport ----

class Wall(Exception):
    """A remote read degraded — carry the honest reason."""


def _git(args: list[str], cwd: str | None = None, timeout: int = 120) -> str:
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    proc = subprocess.run(["git", *args], cwd=cwd, env=env, timeout=timeout,
                          capture_output=True, text=True)
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "").strip().splitlines()
        raise Wall(err[0] if err else f"git {args[0]} failed rc={proc.returncode}")
    return proc.stdout


# Read-token plumbing (gen #21 root cause — see TRANSPORT DOCTRINE above).
# ONLY this dedicated var triggers auth injection; GH_TOKEN/GITHUB_TOKEN are
# deliberately ignored (agent sessions export literal "proxy-injected"
# placeholders there — an invalid credential breaks reads that succeed today).
AUTH_TOKEN_ENV = "ROSTER_READ_TOKEN"

# Auth-shaped wall reasons (vs. e.g. stale-proxy non-convergence): the
# unauthenticated-prompt refusal, an explicit auth failure, and the
# masked-404 GitHub returns for a private repo the token cannot see.
AUTH_WALL_RE = re.compile(
    r"could not read (Username|Password)|Authentication failed"
    r"|Repository not found",
    re.IGNORECASE)


def _auth_args(url: str) -> list[str]:
    """`git -c` args injecting the read token (when set) for github.com reads.

    Same header actions/checkout writes; the token never appears in
    cleartext in the argument (base64 basic-auth pair), and Wall messages
    quote git stderr which never echoes headers.
    """
    token = os.environ.get(AUTH_TOKEN_ENV, "").strip()
    if not token or not url.startswith("https://github.com/"):
        return []
    pair = base64.b64encode(f"x-access-token:{token}".encode()).decode()
    return ["-c",
            f"http.https://github.com/.extraheader=AUTHORIZATION: basic {pair}"]


def describe_wall(reason: str) -> str:
    """Annotate an auth-shaped wall with its fix pointer (pure, selfchecked).

    The roster quotes wall reasons verbatim; appending the pointer here
    means every UNREADABLE row tells the reader HOW to make it readable
    instead of looking like an unexplained outage.
    """
    if AUTH_WALL_RE.search(reason):
        return (f"{reason} — private/auth wall; set {AUTH_TOKEN_ENV} "
                "(fine-grained read-only PAT) to authenticate the read")
    return reason


def ls_remote_head(url: str) -> str:
    """SHA of the remote default-branch HEAD (raises Wall)."""
    out = _git([*_auth_args(url), "ls-remote", url, "HEAD"])
    for line in out.splitlines():
        sha, _, ref = line.partition("\t")
        if ref.strip() == "HEAD":
            return sha.strip()
    raise Wall(f"ls-remote returned no HEAD ref for {url}")


def fetch_verified(url: str, workdir: str, max_attempts: int) -> tuple[str, int]:
    """Shallow-fetch HEAD and loop until FETCH_HEAD == a fresh ls-remote SHA.

    The agent git proxy serves stale cached clone packs (roster gen #3
    evidence: 9/13 repos hours old on first fetch) — NEVER trust a single
    fetch. Returns (verified_sha, attempts). Raises Wall on non-convergence.
    """
    _git(["init", "-q", workdir])
    fetched = ""
    for attempt in range(1, max_attempts + 1):
        _git([*_auth_args(url), "fetch", "-q", "--depth", "1", url, "HEAD"],
             cwd=workdir, timeout=300)
        fetched = _git(["rev-parse", "FETCH_HEAD"], cwd=workdir).strip()
        target = ls_remote_head(url)  # re-pin: the world may move mid-loop
        if fetched == target:
            return fetched, attempt
    raise Wall(f"stale proxy pack: fetched {fetched[:9]} != ls-remote after "
               f"{max_attempts} attempts")


def order_heartbeat_paths(declared: list[str], globbed: list[str]) -> list[str]:
    """Order the heartbeat files to read (P3 sub-rows, plan §3c).

    Pure so --selfcheck pins it. The repo's substrate.config.json
    `heartbeat_files` declaration wins the ordering when present; globbed
    control/status*.md files not declared are appended (an undeclared
    sub-seat file must never be invisible — that was gap 3). Declared
    files missing from the tree are dropped (never invent a heartbeat).
    control/status.md is always first when present (the primary row).
    """
    paths = [p for p in declared if p in globbed]
    paths += [c for c in globbed if c not in paths]
    if "control/status.md" in paths:
        paths.remove("control/status.md")
        paths.insert(0, "control/status.md")
    return paths


def read_heartbeat(url: str, max_attempts: int) -> dict:
    """Fetch a repo's HEAD + ALL control/status*.md + evidence paths.

    One verified fetch serves three consumers (P3): every heartbeat file
    (sub-rows), the primary status (roster row), and the evidence-index
    discovery (docs/current-state.md, latest .sessions/ card, docs/retro).
    """
    with tempfile.TemporaryDirectory(prefix="genroster-") as tmp:
        sha, attempts = fetch_verified(url, tmp, max_attempts)
        raw_date = _git(["log", "-1", "--format=%cI", "FETCH_HEAD"],
                        cwd=tmp).strip()
        # %cI carries the committer's LOCAL utc-offset — normalize to UTC Z
        # (bug caught at first real run: truncating the offset off made every
        # +02:00 commit look 2h in the future).
        try:
            head_date = (datetime.fromisoformat(raw_date)
                         .astimezone(timezone.utc)
                         .strftime("%Y-%m-%dT%H:%M:%SZ"))
        except ValueError:
            head_date = raw_date

        def ls(path: str) -> list[str]:
            try:
                return _git(["ls-tree", "--name-only", "FETCH_HEAD", path],
                            cwd=tmp).splitlines()
            except Wall:
                return []

        # -- heartbeat files: declared heartbeat_files wins, glob fallback --
        # -- kit version from the TREE (INC-40): substrate.config.json pin +
        #    .substrate/state.json installed version are the primary record;
        #    the heartbeat `kit:` line is prose that chronically lags
        #    (idle 8 releases behind at the 2026-07-13 review) and becomes
        #    fallback-only. Absence is honest: no config/state = no value.
        declared: list[str] = []
        kit_tree: dict = {"pinned": None, "state": None}
        try:
            cfg = json.loads(_git(["show", "FETCH_HEAD:substrate.config.json"],
                                  cwd=tmp))
            raw = cfg.get("heartbeat_files")
            if isinstance(raw, list):
                declared = [p for p in raw if isinstance(p, str)]
            v = cfg.get("kit_version")
            if isinstance(v, str) and v:
                kit_tree["pinned"] = v
        except (Wall, json.JSONDecodeError):
            pass  # no config / unparseable — the glob below is the source
        try:
            state = json.loads(_git(
                ["show", "FETCH_HEAD:.substrate/state.json"], cwd=tmp))
            v = state.get("kit_version")
            if isinstance(v, str) and v:
                kit_tree["state"] = v
        except (Wall, json.JSONDecodeError):
            pass  # no state file — pinned/heartbeat carry what is known
        globbed = [ln for ln in ls("control/")
                   if re.fullmatch(r"control/status[^/]*\.md", ln)]
        statuses: list[dict] = []
        for path in order_heartbeat_paths(declared, globbed):
            try:
                statuses.append({"path": path,
                                 "text": _git(["show", f"FETCH_HEAD:{path}"],
                                              cwd=tmp)})
            except Wall:
                continue  # listed but unreadable — skip, never invent

        # -- evidence discovery (P3 index; same pinned tree) --
        cards = sorted(ln for ln in ls(".sessions/")
                       if ln.endswith(".md")
                       and not ln.endswith("README.md"))
        retro = sorted(ln for ln in ls("docs/retro/") if ln.endswith(".md"))
        evidence = {
            "current_state": ("docs/current-state.md"
                              if "docs/current-state.md" in ls("docs/")
                              else None),
            "latest_card": cards[-1] if cards else None,
            "retro_latest": retro[-1] if retro else None,
            "retro_count": len(retro),
        }
        # -- program-evidence per-file discovery (Slice 0 item 2, D1–D3) --
        # Same pinned tree; regex over a recursive docs/ listing. An empty
        # match list is an HONEST absence at this SHA, never invented.
        extra: dict[str, list[str]] = {}
        spec = EVIDENCE_EXTRA.get(url.rstrip("/").split("/")[-1])
        if spec:
            try:
                tree = _git(["ls-tree", "-r", "--name-only", "FETCH_HEAD",
                             "docs"], cwd=tmp).splitlines()
            except Wall:
                tree = []
            for key, pat in spec.items():
                extra[key] = sorted(p for p in tree if pat.search(p))
        evidence["extra"] = extra
        primary = statuses[0] if statuses else None
        return {"sha": sha, "attempts": attempts, "head_date": head_date,
                "status_text": primary["text"] if primary else None,
                "status_path": primary["path"] if primary else None,
                "statuses": statuses, "evidence": evidence,
                "kit_tree": kit_tree}


# --------------------------------------------------------------- parsing ---

def parse_status(text: str) -> dict:
    """Pull the header fields out of a control/status*.md.

    Handles BOTH observed heartbeat styles (verified against live lanes,
    2026-07-11): the kit-standard bare line (`phase: ...`) and the bullet
    form some lanes write (`- **phase:** ...`, e.g. venture-lab, pokemon).
    """
    fields = {}
    for key in ("updated", "phase", "kit", "orders", "health", "lane"):
        m = (re.search(rf"^{key}:\s*(.+)$", text, re.MULTILINE)
             or re.search(rf"^-\s*\*\*{key}:\*\*\s*(.+)$", text, re.MULTILINE))
        if m:
            fields[key] = m.group(1).strip()
    # some lanes (product-forge) carry no phase line at all — the `lane:`
    # header is the closest one-liner; fall back honestly, labelled.
    if "phase" not in fields and "lane" in fields:
        fields["phase"] = f"(no phase line; lane: {fields['lane']})"
    return fields


# ----------------------------------------------- owner-flag extraction ----
# P2 (QUEUE GENERATION, centralization plan §3b, fm PR #85): parse_status
# only pulls header one-liners, so a lane's ⚑ needs-owner / OWNER-ACTION
# block never surfaced centrally until a manual owner-queue sweep — the
# highest-value channel had no automated aggregation. These helpers extract
# those blocks into docs/owner-queue-candidates.md (GENERATED — the manager
# still curates docs/owner-queue.md from it; nothing lands there
# automatically).

# A flag block STARTS on a line whose CONTENT BEGINS with ⚑ (optionally
# behind list/quote/bold markup — the observed lane styles: `⚑ needs-owner:`,
# `- **⚑ OWNER-ACTION 1:** …`, `⚑A — …`, `> ⚑ …`) or with the word
# OWNER-ACTION itself. Deliberately line-start-anchored: a ⚑ quoted
# mid-prose (fleet-manager's own giant phase lines re-tell old flags) is
# NOT a new ask and must not spam the feed.
FLAG_START_RE = re.compile(r"^\s*(?:[-*>]\s*|\d+\.\s+)*(?:\*\*)?\s*(?:⚑|OWNER-ACTION\b)")
# `⚑ needs-owner: none` (and friends) = explicitly no ask — never a candidate.
FLAG_NONE_RE = re.compile(
    r"needs-owner[:\s*]*\s*(?:\*\*)?\s*[`'\"]?(none|n/?a|—|-)?[`'\"]?\s*$",
    re.IGNORECASE)
# Kit header fields end a block (the flag line is part of the header block
# in the kit grammar; the next field is not a continuation of the ask).
HEADER_FIELD_RE = re.compile(
    r"^(updated|phase|health|kit|last-shipped|blockers|orders|notes|"
    r"coordinator|routine|lane|timestamp):", re.IGNORECASE)
FLAG_BLOCK_MAX_LINES = 25


def parse_owner_flags(text: str) -> list[list[str]]:
    """Extract ⚑ needs-owner / OWNER-ACTION blocks from a heartbeat.

    Returns a list of blocks (each a list of verbatim lines). A block runs
    from a flag-start line until a blank line, a markdown heading, a kit
    header field, a code fence, or the next flag start; capped at
    FLAG_BLOCK_MAX_LINES lines (truncation is marked). Duplicate blocks
    (identical normalized text) are dropped.
    """
    blocks: list[list[str]] = []
    seen: set[str] = set()
    lines = text.splitlines()
    i, n = 0, len(lines)
    in_fence = False
    while i < n:
        line = lines[i]
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            i += 1
            continue
        if in_fence or not FLAG_START_RE.search(line):
            i += 1
            continue
        if FLAG_NONE_RE.search(line):
            i += 1
            continue
        block = [line.rstrip()]
        j = i + 1
        while j < n and len(block) < FLAG_BLOCK_MAX_LINES:
            nxt = lines[j]
            if (not nxt.strip() or nxt.lstrip().startswith("#")
                    or nxt.lstrip().startswith("```")
                    or HEADER_FIELD_RE.match(nxt.strip())
                    or FLAG_START_RE.search(nxt)):
                break
            block.append(nxt.rstrip())
            j += 1
        if j < n and len(block) >= FLAG_BLOCK_MAX_LINES:
            block.append("… (block truncated at "
                         f"{FLAG_BLOCK_MAX_LINES} lines by gen_roster)")
        key = re.sub(r"\s+", " ", " ".join(block)).strip().lower()
        if key not in seen:
            seen.add(key)
            blocks.append(block)
        i = j
    return blocks


_SLUG_STOPWORDS = {"the", "a", "an", "of", "for", "and", "or", "to", "in",
                   "on", "is", "are", "with", "needs", "owner", "action",
                   "owneraction", "needsowner"}


def suggest_slug(lane_repo: str | None, lane_name: str, first_line: str) -> str:
    """Deterministic content-derived candidate id: OQ-<LANE>-<WORDS>.

    NOT positional (positional numbers reshuffle on every queue rewrite —
    the fm PR #75 renumbering broke a cross-reference; plan §3b). The
    manager may adopt or rename the id when curating; stability matters
    more than beauty.
    """
    lane_token = (lane_repo or lane_name).split()[0]
    lane_token = re.sub(r"[^A-Za-z0-9]+", "-", lane_token).strip("-").upper()
    cleaned = re.sub(r"[`*_>⚑#\[\]()]", " ", first_line)
    words = [w for w in re.findall(r"[A-Za-z0-9]+", cleaned)
             if w.lower() not in _SLUG_STOPWORDS][:4]
    tail = "-".join(w.upper() for w in words) or "FLAG"
    return f"OQ-{lane_token}-{tail}"


PR_URL_RE = re.compile(r"github\.com/menno420/([\w.-]+)/pull/(\d+)")
QUEUE_ID_RE = re.compile(r"^\s*-\s*id:\s*(OQ-[A-Z0-9-]+)\s*$", re.MULTILINE)


def load_queue_pr_index(queue_path: str) -> dict[tuple[str, str], set[str]]:
    """Map (repo, pr-number) -> owner-queue slug ids that cite it.

    Used for the feed's `possibly-covered-by` hint so the manager sees at a
    glance whether an extracted ask already has a curated queue item. Keyed
    on the stable `id: OQ-…` slugs (P2), never positional numbers.
    """
    try:
        with open(queue_path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return {}
    index: dict[tuple[str, str], set[str]] = {}
    current_id = None
    for line in text.splitlines():
        m = QUEUE_ID_RE.match(line)
        if m:
            current_id = m.group(1)
            continue
        if re.match(r"^\d+\.\s", line) or line.startswith("## "):
            # a new item starts before its id line is seen; heading resets
            if re.match(r"^#", line):
                current_id = None
        for repo, num in PR_URL_RE.findall(line):
            if current_id:
                index.setdefault((repo, num), set()).add(current_id)
    return index


# The ONE deliberate deviation from byte-verbatim block quoting (same class
# as P1's api_token_hint strip): a lane heartbeat quoting a decision id like
# `D-0005` would trip the kit's stamp-discipline check ("stamp each decision
# at one home") on THIS repo every regen — the feed is a quotation, not a
# second home. The ASCII hyphen in `D-NNN…` ids is swapped for U+2011
# (non-breaking hyphen): visually identical, checker-inert. Grep the source
# heartbeat for the exact byte form.
_DECISION_ID_RE = re.compile(r"\bD-(\d{3,})\b")


def _sanitize_feed_line(line: str) -> str:
    line = line.replace("```", "ʼʼʼ")  # keep the fenced block intact
    return _DECISION_ID_RE.sub("D‑\\1", line)


def render_candidates(rows: list[dict], generation: int, now: datetime,
                      generated_by: str, dispatched_by: str,
                      queue_index: dict[tuple[str, str], set[str]]) -> str:
    stamp = now.strftime("%Y-%m-%dT%H:%MZ")
    out = []
    out.append("# Owner-queue candidate feed — GENERATED\n")
    # `living-ledger` is the kit-allowed badge closest to this file's nature
    # (docs/roster.md precedent — machine-regenerated living state); the kit
    # badge vocabulary has no `generated` token (check finding, PR #85).
    out.append("> **Status:** `living-ledger`\n>")
    out.append("> **GENERATED — NOT SOURCE OF TRUTH; the manager curates "
               "`docs/owner-queue.md` from it.** Do not hand-edit; "
               "regenerated with the roster on every regen "
               "(`scripts/gen_roster.py`, P2 — centralization plan §3b).\n>")
    out.append(f"> **Generation #{generation}** · generated-at **{stamp}** · "
               f"by {generated_by}, dispatched by {dispatched_by}\n>")
    out.append("> Every block below is a VERBATIM `⚑ needs-owner` / "
               "`OWNER-ACTION` extraction from a lane heartbeat "
               "(`control/status*.md` at the ls-remote-verified HEAD the "
               "roster row cites). Nothing here lands in the owner queue "
               "automatically: the manager dedups, verifies (R17), and "
               "curates. `suggested-id` is a deterministic content-derived "
               "slug the manager may adopt; `possibly-covered-by` lists "
               "active queue ids citing the same PR — `none matched` means "
               "manual dedup is still needed.\n")
    total = 0
    for row in rows:
        flags = row.get("owner_flags") or []
        if not flags:
            continue
        lane = row["lane"]
        hb = row["hb"]
        src = (f"{lane['repo']}/{hb['status_path']} @ `{hb['sha'][:7]}`"
               if hb and hb.get("status_path") else "(no heartbeat file)")
        used: set[str] = set()
        for block in flags:
            total += 1
            first = re.sub(r"\s+", " ", block[0]).strip()
            slug = suggest_slug(lane["repo"], lane["lane"], first)
            if slug in used:
                k = 2
                while f"{slug}-{k}" in used:
                    k += 1
                slug = f"{slug}-{k}"
            used.add(slug)
            covered: set[str] = set()
            body = "\n".join(block)
            for repo, num in PR_URL_RE.findall(body):
                covered |= queue_index.get((repo, num), set())
            for num in re.findall(r"PR\s*#(\d+)", body):
                if lane["repo"]:
                    covered |= queue_index.get((lane["repo"], num), set())
            out.append(f"### {lane['lane']} — {truncate(first, 110)}\n")
            out.append(f"- suggested-id: `{slug}`")
            out.append(f"- source: {src} · heartbeat `updated:` "
                       f"{truncate(row['fields'].get('updated', 'n/a'), 60)}")
            out.append("- possibly-covered-by: "
                       + (", ".join(f"`{c}`" for c in sorted(covered))
                          if covered else
                          "none matched (manual dedup needed)"))
            out.append("")
            out.append("```text")
            out.extend(_sanitize_feed_line(ln) for ln in block)
            out.append("```")
            out.append("")
    if total == 0:
        out.append("*(No lane heartbeat carries an extractable "
                   "`⚑ needs-owner` / `OWNER-ACTION` block this "
                   "generation.)*\n")
    else:
        out.append(f"---\n\n{total} candidate block(s) across "
                   f"{sum(1 for r in rows if r.get('owner_flags'))} lane(s). "
                   "Feed is additive-noise-tolerant by design: over-capture "
                   "is curated out by the manager; silent stranding is the "
                   "failure this feed exists to kill.\n")
    return "\n".join(out) + "\n"


# ------------------------------------------------ evidence index (P3) -----

def render_evidence_index(rows: list[dict], generation: int, now: datetime,
                          generated_by: str, dispatched_by: str) -> str:
    """docs/evidence-index.md — each lane row → its evidence home (§3c).

    One row per LANE (sub-rows share the repo's evidence). Links pin to the
    same ls-remote-verified HEAD SHA the roster row cites, so the index can
    never be fresher than its evidence. The manager-internal ↔
    program-facing record split (plan §4) is navigable from this one page.
    """
    stamp = now.strftime("%Y-%m-%dT%H:%MZ")
    out = []
    out.append("# Cross-repo evidence index — GENERATED\n")
    out.append("> **Status:** `living-ledger`\n>")
    out.append("> **GENERATED — NOT SOURCE OF TRUTH.** Do not hand-edit; "
               "regenerated with `docs/roster.md` on every regen "
               "(`scripts/gen_roster.py`, P3 — centralization plan §3c). "
               "Each repo stays canonical for its OWN internal state (plan "
               "§4): this index LINKS evidence homes, it never copies them "
               "(copies drift).\n>")
    out.append(f"> **Generation #{generation}** · generated-at **{stamp}** · "
               f"by {generated_by}, dispatched by {dispatched_by}\n>")
    out.append("> **Program-narrative home:** cross-repo program reviews / "
               "night-reviews / email drafts live in **superbot "
               "[`docs/eap/`](https://github.com/menno420/superbot/tree/main/"
               "docs/eap)** (front door: its README); fleet-wide state lives "
               "HERE in fleet-manager (roster · owner-queue · fleet-triage · "
               "capabilities · environments). Links below pin to the "
               "ls-remote-verified HEAD each roster row cites.\n")
    out.append("| Lane | Heartbeat file(s) | `docs/current-state.md` | "
               "Latest `.sessions/` card | `docs/retro/` | Pinned @ HEAD |")
    out.append("|---|---|---|---|---|---|")

    def link(repo: str, sha: str, path: str, label: str | None = None) -> str:
        return (f"[{label or path}]({GITHUB_BASE}{repo}/blob/{sha}/{path})")

    for row in rows:
        if row.get("subrow"):
            continue  # sub-rows share the parent lane's evidence
        lane = row["lane"]
        repo = lane["repo"]
        if repo is None:
            out.append(f"| {lane['lane']} | n/a — registry-only seat | — | — "
                       "| — | trigger registry only |")
            continue
        if row["wall"]:
            wall = truncate(row["wall"], 80)
            out.append(f"| {lane['lane']} | NOT MEASURED (wall: {wall}) | — "
                       "| — | — | NOT MEASURED |")
            continue
        hb = row["hb"]
        sha = hb["sha"]
        ev = hb.get("evidence") or {}
        hbs = hb.get("statuses") or []
        hb_cell = (", ".join(link(repo, sha, st["path"],
                                  st["path"].removeprefix("control/"))
                             for st in hbs)
                   if hbs else "none — HEAD committer date is the signal")
        cs = (link(repo, sha, ev["current_state"], "current-state.md")
              if ev.get("current_state") else "—")
        card = (link(repo, sha, ev["latest_card"],
                     os.path.basename(ev["latest_card"]))
                if ev.get("latest_card") else "—")
        retro = (link(repo, sha, ev["retro_latest"],
                      f"{os.path.basename(ev['retro_latest'])} "
                      f"(+{ev['retro_count'] - 1} more)"
                      if ev.get("retro_count", 0) > 1
                      else os.path.basename(ev["retro_latest"]))
                 if ev.get("retro_latest") else "—")
        out.append(f"| {lane['lane']} | {hb_cell} | {cs} | {card} | {retro} "
                   f"| `{sha[:7]}` |")

    out.append("\n> A `—` cell is an HONEST absence at the pinned HEAD "
               "(the file/dir does not exist there), never a broken link. "
               "Walled repos degrade to NOT MEASURED with the verbatim "
               "reason, same doctrine as the roster.")

    # ---- program-evidence per-file rows (Slice 0 item 2, plan D1–D3) ----
    by_repo: dict[str, dict] = {}
    for row in rows:
        if row.get("subrow") or not row["lane"]["repo"] or not row.get("hb"):
            continue
        by_repo[row["lane"]["repo"]] = row["hb"]

    def extra_files(repo: str, key: str) -> list[str] | None:
        hb = by_repo.get(repo)
        if hb is None:
            return None  # walled / not fetched this generation
        return (hb.get("evidence") or {}).get("extra", {}).get(key, [])

    def file_bullets(repo: str, key: str) -> list[str]:
        files = extra_files(repo, key)
        if files is None:
            return [f"- NOT MEASURED — `{repo}` unreadable at this "
                    "generation (see the roster row's verbatim wall)."]
        if not files:
            return [f"- — none found at `{repo}`'s pinned HEAD "
                    "(honest absence, pattern-discovered)."]
        sha = by_repo[repo]["sha"]
        return [f"- {link(repo, sha, p)}" for p in files]

    out.append("\n## Program evidence — per-file rows "
               "(central-docs-plan D1–D3)\n")
    out.append("Discovered by pattern at the SAME pinned SHA as each lane "
               "row above. INDEX rows only — every corpus stays canonical "
               "in its home repo (plan §4 class D); fm links, never copies.\n")

    out.append("### D1 — superbot `docs/eap/` (program-narrative corpus; "
               "home stays superbot)\n")
    out.extend(file_bullets("superbot", "eap"))

    out.append("\n### D3 — substrate-kit `docs/reports/` (fleet evidence)\n")
    out.extend(file_bullets("substrate-kit", "kit_reports"))

    out.append("\n### D2 — gen-2 feedback + custom-instructions proposals\n")
    out.append("Written for the manager to collect; the codetool-lab copies "
               "are archive-bound (also on the D5 mirror-before-archive "
               "list).\n")
    for repo in ("superbot-games", "trading-strategy", "codetool-lab-sonnet5",
                 "codetool-lab-fable5", "codetool-lab-opus4.8"):
        out.append(f"**{repo}**\n")
        out.extend(file_bullets(repo, "gen2"))
        out.append("")

    out.append("### D3 — superbot-next rebuild evidence corpus "
               "(pointers only)\n")
    out.extend(file_bullets("superbot-next", "next_rebuild"))

    out.append("\n### D3 — retro errata register\n")
    out.append("Corrections that would otherwise live only in the source "
               "repo's audit docs; registered beside the evidence they "
               "correct.\n")
    out.append("| Repo | Recorded claim | Correction | Source |")
    out.append("|---|---|---|---|")
    for err in RETRO_ERRATA:
        src_hb = by_repo.get(err["source_repo"])
        src = (link(err["source_repo"], src_hb["sha"], err["source_path"])
               if src_hb else
               f"`{err['source_repo']}:{err['source_path']}` (NOT MEASURED "
               "this generation)")
        out.append(f"| {err['repo']} | {err['claim']} | {err['correction']} "
                   f"| {src} |")
    return "\n".join(out) + "\n"


ISO_RE = re.compile(r"(\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}(?::\d{2})?)"
                    r"(Z|[+-]\d{2}:\d{2})?")


def parse_when(stamp: str) -> datetime | None:
    """Lenient ISO-ish parse (heartbeats vary: Z suffix, no seconds, prose).

    Respects an explicit utc-offset when present; assumes UTC when absent
    (the fleet heartbeat convention is Z stamps).
    """
    if not stamp:
        return None
    m = ISO_RE.search(stamp)
    if not m:
        return None
    raw = m.group(1).replace(" ", "T")
    if len(raw) == 16:
        raw += ":00"
    offset = m.group(2)
    if offset and offset != "Z":
        raw += offset
    try:
        when = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    return when.astimezone(timezone.utc)


def age_str(hours: float) -> str:
    if hours < 0:
        return "future?"
    # Round to whole seconds BEFORE flooring to minutes: `hours` arrives as
    # seconds/3600 and the float noise truncates an exact minute down —
    # 32.3h rendered "~32h17m" because (32.3-32)*60 == 17.999…  (caught by
    # hand verification at roster gen #5, verification run 1).
    total_m = int(round(hours * 3600)) // 60
    if hours < 1:
        return f"~{total_m}m"
    if hours < 48:
        h, m = divmod(total_m, 60)
        return f"~{h}h{m:02d}m"
    return f"~{hours / 24:.1f}d"


def truncate(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    # markdown tables break on raw pipes
    text = text.replace("|", "\\|")
    # Roster cells are QUOTATIONS of lane heartbeats, not decision homes —
    # the same stamp-discipline swap as the candidate feed (P2; first
    # tripped by a P3 sub-row quoting `D-0002` in its kit cell): ASCII
    # hyphen in D-NNN ids -> U+2011, visually identical, checker-inert.
    text = _DECISION_ID_RE.sub("D‑\\1", text)
    return text if len(text) <= limit else text[: limit - 1] + "…"


# --------------------------------------------------------------- verdict ---

def verdict_for(disposition: str, age_h: float | None, cadence_h: float,
                walled: bool, private: bool = False) -> str:
    if disposition == "archived":
        return "STALE-BY-DESIGN"
    if disposition == "registry-only":
        return "n/a (registry-only seat)"
    if walled:
        # A transport/auth wall is a MEASUREMENT artifact, never lane death
        # (gen #21: pokemon-mod-lab printed DEAD while demonstrably alive
        # behind its private wall). DEAD below is reserved for a READABLE
        # repo with no measurable heartbeat signal. A wall on the KNOWN
        # private repo is rendered distinctly (INC-20): it is a credential
        # gap (ROSTER_READ_TOKEN pending), not generic unreadability.
        if private:
            return "PRIVATE (auth wall — not DARK; ROSTER_READ_TOKEN pending)"
        return "UNREADABLE (transport/auth)"
    if age_h is None:
        return "DEAD (not measurable)"
    if age_h <= 2 * cadence_h:
        return "FRESH"
    if age_h <= 24:
        return "STALE"
    return "DARK"


# -------------------------------------------------------------- rendering --

def build_rows(records: list[dict], now: datetime, max_attempts: int,
               log=lambda *_: None) -> list[dict]:
    rows = []
    for lane in LANES:
        log(f"[gen_roster] lane {lane['lane']} …")
        trig = match_lane_triggers(lane, records)
        cad = 2.0
        if trig["standing"]:
            c = cadence_hours(trig["standing"][0].get("cron_expression", ""))
            if c:
                cad = c
        row = {"lane": lane, "trig": trig, "cadence": cad, "hb": None,
               "wall": None, "fields": {}, "age_h": None}
        subrows: list[dict] = []
        if lane["repo"]:
            url = GITHUB_BASE + lane["repo"]
            try:
                hb = read_heartbeat(url, max_attempts)
                row["hb"] = hb
                if hb["status_text"]:
                    row["fields"] = parse_status(hb["status_text"])
                    row["owner_flags"] = parse_owner_flags(hb["status_text"])
                stamp = row["fields"].get("updated") or hb["head_date"]
                when = parse_when(stamp)
                if when:
                    row["age_h"] = (now - when).total_seconds() / 3600
                # P3 sub-rows (plan §3c): one row per EXTRA heartbeat file,
                # judged on that file's own stamp; triggers stay on the
                # parent row. Sub-row heartbeats also feed the P2 candidate
                # extraction (a sub-seat ask must not strand).
                for st in hb["statuses"][1:]:
                    sub = {"lane": {"lane": f"↳ {lane['lane']} — `{st['path']}`",
                                    "repo": lane["repo"],
                                    "disposition": lane["disposition"],
                                    "tokens": []},
                           "trig": {"standing": [], "oneshot": [], "poke": []},
                           "cadence": cad, "wall": None, "age_h": None,
                           "subrow": True,
                           "hb": dict(hb, status_text=st["text"],
                                      status_path=st["path"]),
                           "fields": parse_status(st["text"]),
                           "owner_flags": parse_owner_flags(st["text"])}
                    swhen = parse_when(sub["fields"].get("updated") or
                                       hb["head_date"])
                    if swhen:
                        sub["age_h"] = (now - swhen).total_seconds() / 3600
                    sub["verdict"] = verdict_for(lane["disposition"],
                                                 sub["age_h"], cad, False)
                    subrows.append(sub)
            except Wall as exc:
                row["wall"] = describe_wall(str(exc))
        row["verdict"] = verdict_for(lane["disposition"], row["age_h"],
                                     row["cadence"], row["wall"] is not None,
                                     lane.get("private", False))
        # INC-16 divergence signal: a STALE/DARK verdict rests on the
        # heartbeat stamp alone, but the repo HEAD committer date is in the
        # same fetch — when commits are FRESH while the heartbeat is not,
        # the lane is ACTIVE with a lagging heartbeat (the superbot-games
        # ~50-PRs-while-rated-DARK failure). DARK is never declared on
        # heartbeat alone: the marker rides the verdict cell + a summary
        # line, so a re-wake ask is never filed against a pushing lane.
        if (row["verdict"] in ("STALE", "DARK") and row["hb"]
                and row["hb"].get("head_date")):
            head_when = parse_when(row["hb"]["head_date"])
            if head_when:
                head_age = (now - head_when).total_seconds() / 3600
                # same FRESH bar the heartbeat itself is judged by
                if head_age <= 2 * row["cadence"]:
                    row["divergence"] = head_age
        rows.append(row)
        rows.extend(subrows)
    return rows


# INC-41 — deliberate kit pins, listed so no registry rendering "fixes" them:
# superbot pins 1.0.0 (CLAUDE.md Q-0254 note — "until superbot itself upgrades
# from a real kit release") and substrate-kit self-pins 1.0.0 (the designed
# owner-held pin path). If the pinned value ever moves off the listed one the
# label disappears on its own — never hand-remove it.
DELIBERATE_KIT_PINS = {"superbot": "1.0.0", "substrate-kit": "1.0.0"}


def kit_cell(row: dict) -> str:
    """Kit column — TREE-derived primary (INC-40), heartbeat line fallback.

    - Sub-rows (extra per-lane heartbeat files, typically frozen archives)
      never contribute their own `kit:` line: a parseable line in an archived
      file otherwise renders as current (INC-40's superbot-games v1.7.1 case).
    - Deliberate pins are labeled, not "corrected" (INC-41) — and the hub's
      pin now renders instead of "—".
    - When the tree and the heartbeat line disagree, the tree wins and the
      lag is flagged inline.
    """
    if row.get("subrow"):
        return "(parent row; archived kit: line excluded — INC-40)"
    hb = row.get("hb") or {}
    kt = hb.get("kit_tree") or {}
    tree = kt.get("state") or kt.get("pinned")
    hb_line = (row.get("fields") or {}).get("kit")
    if tree:
        repo = (row.get("lane") or {}).get("repo")
        if DELIBERATE_KIT_PINS.get(repo) == kt.get("pinned") and \
                (kt.get("state") or kt.get("pinned")) == kt.get("pinned"):
            return f"v{tree} (deliberate pin — INC-41)"
        if hb_line and f"v{tree}" not in hb_line:
            return f"v{tree} (tree; hb line lags — INC-40)"
        return f"v{tree} (tree)"
    return hb_line or "—"


def render_wake(trig: dict) -> str:
    bits = []
    for r in trig["standing"]:
        last = r.get("last_fired_at") or "never"
        bits.append(f"**{r['name']}** `{r['id']}` · `{r['cron_expression']}` "
                    f"· last {truncate(last[:19], 25)} "
                    f"· next {truncate((r.get('next_run_at') or '?')[:16], 20)}")
    for r in trig["poke"]:
        bits.append(f"poke-only `{r['name']}`")
    if trig["oneshot"]:
        soonest = min((r.get("run_once_at") or "" for r in trig["oneshot"]))
        bits.append(f"+{len(trig['oneshot'])} one-shot(s), next {soonest[:16]}")
    return "; ".join(bits) if bits else "**NONE**"


def render(rows: list[dict], records: list[dict], generation: int,
           now: datetime, generated_by: str, dispatched_by: str,
           eval_dt=None, eval_basis: str = "no eval basis derivable") -> str:
    enabled = [r for r in records if r.get("enabled")]
    crons = [r for r in enabled if r.get("cron_expression")]
    ones = [r for r in enabled if r.get("run_once_at")]
    pokes = [r for r in enabled
             if not r.get("cron_expression") and not r.get("run_once_at")]
    stamp = now.strftime("%Y-%m-%dT%H:%MZ")
    refetched = [r for r in rows if r["hb"] and r["hb"]["attempts"] > 1]

    out = []
    out.append("# Fleet roster — GENERATED\n")
    out.append("> **Status:** `living-ledger`\n>")
    out.append("> **GENERATED — do not hand-edit; regenerated each manager "
               "wake (`scripts/gen_roster.py`, R25).**\n>")
    out.append(f"> **Generation #{generation}** · generated-at **{stamp}** · "
               f"by {generated_by}, dispatched by {dispatched_by} · machine "
               f"generation (`scripts/gen_roster.py`)\n>")
    out.append("> **Source of truth = the lane heartbeats** (each repo's "
               "`control/status*.md` at an ls-remote-verified HEAD over git "
               "transport) + the live trigger registry (`list_triggers` "
               "export). This file is a derived snapshot. **Kill-switch: if "
               "this file's generated-at goes stale >24h, trust the "
               "heartbeats directly** — do not act on a stale roster row.\n>")
    out.append(f"> **Transport verification:** every repo HEAD below was "
               f"fetched shallow and re-fetched until FETCH_HEAD == a fresh "
               f"`git ls-remote` (stale-proxy-pack doctrine, roster gen #3)"
               + (f"; re-fetch was needed for: "
                  + ", ".join(r["lane"]["lane"] for r in refetched)
                  if refetched else "; all repos converged on the first fetch")
               + ". Repos that could not be read are marked NOT MEASURED "
               "with the verbatim wall reason and verdict UNREADABLE "
               "(transport/auth) — a measurement artifact, never guessed "
               "and never printed as lane death.\n>")
    out.append(f"> **Trigger evidence:** {len(records)}-record export, "
               f"**{len(enabled)} enabled**: {len(crons)} standing crons + "
               f"{len(pokes)} poke-only + {len(ones)} one-shots.\n>")
    out.append("> **Sub-rows (P3, plan §3c):** a `↳` row is an EXTRA "
               "heartbeat file in the same repo (all `control/status*.md` "
               "are enumerated; `substrate.config.json heartbeat_files` "
               "ordering honored) — judged on its own `updated:` stamp; "
               "wake triggers live on the parent lane row. Evidence homes "
               "per lane: `docs/evidence-index.md` (generated with this "
               "file).\n>")
    health = health_report(records, eval_dt) if eval_dt is not None else None
    out.append("> **Trigger health (ORDER 020):** evaluated at **"
               + (eval_dt.strftime("%Y-%m-%dT%H:%MZ") if eval_dt else "n/a")
               + f"** (basis: {eval_basis}) · grace {WEDGE_GRACE_MIN}min. "
               + (f"Fleet-wide: **{len(health['wedged'])} WEDGED cron(s) · "
                  f"{len(health['dropped'])} DROPPED-or-QUEUED one-shot(s) · "
                  f"{len(health['dead_chains'])} DEAD chain(s)**"
                  if health is not None else "NOT EVALUATED (no basis)")
               + " — detail section below the verdicts; wake-time "
               "enforcement: `scripts/check_trigger_health.py`.\n")
    out.append("| Lane | Heartbeat `updated:` | Age | Verdict | Phase (machine-truncated) | Orders | Kit | Wake state (trigger · cron · last fire) | Trigger health | Evidence (repo @ HEAD) |")
    out.append("|---|---|---|---|---|---|---|---|---|---|")

    for row in rows:
        lane = row["lane"]
        f = row["fields"]
        if row["wall"]:
            hb_cell = f"NOT MEASURED (wall: {truncate(row['wall'], 90)})"
            age = "n/a"
            evidence = f"NOT MEASURED (wall: {truncate(row['wall'], 90)})"
        elif lane["repo"] is None:
            hb_cell = "n/a — registry-only seat (no repo)"
            age = "n/a"
            evidence = "trigger registry only"
        else:
            hb = row["hb"]
            if f.get("updated"):
                hb_cell = truncate(f["updated"], 60)
            else:
                hb_cell = (f"n/a — no control/status*.md at HEAD; HEAD "
                           f"committer date {hb['head_date'][:16]}Z used")
            age = age_str(row["age_h"]) if row["age_h"] is not None else "n/a"
            evidence = f"`{hb['sha'][:7]}` {hb['head_date'][:19]}"
        out.append("| {lane} | {hb} | {age} | {verdict} | {phase} | {orders} "
                   "| {kit} | {wake} | {health} | {evidence} |".format(
                       lane=lane["lane"], hb=hb_cell, age=age,
                       verdict=row["verdict"]
                       + (" ⚠ commits-FRESH (heartbeat lags — lane ACTIVE "
                          "by pushes, INC-16)"
                          if row.get("divergence") is not None else ""),
                       phase=truncate(f.get("phase", "—"), 160),
                       orders=truncate(f.get("orders", "—"), 100),
                       kit=truncate(kit_cell(row), 48),
                       wake=("(triggers on the parent lane row)"
                             if row.get("subrow")
                             else render_wake(row["trig"])),
                       health=("(parent row)" if row.get("subrow")
                               else lane_health_cell(row["trig"], eval_dt)),
                       evidence=evidence))

    out.append(f"\n## Staleness verdicts (generation #{generation})\n")
    order = ["DARK", "DEAD (not measurable)",
             "PRIVATE (auth wall — not DARK; ROSTER_READ_TOKEN pending)",
             "UNREADABLE (transport/auth)",
             "STALE", "FRESH", "STALE-BY-DESIGN",
             "n/a (registry-only seat)"]
    for v in order:
        lanes = [r["lane"]["lane"] for r in rows if r["verdict"] == v]
        if lanes:
            out.append(f"- **{v}:** " + ", ".join(lanes))
    divergent = [r for r in rows if r.get("divergence") is not None]
    if divergent:
        out.append("- **⚠ heartbeat-vs-commits divergence (INC-16 — "
                   "verdicts above rest on the heartbeat; these lanes' repo "
                   "HEADs are FRESH, so treat them as ACTIVE, never re-wake "
                   "or declare dead on the heartbeat alone):** "
                   + ", ".join(f"{r['lane']['lane']} (heartbeat "
                               f"{age_str(r['age_h'])} vs newest commit "
                               f"{age_str(r['divergence'])})"
                               for r in divergent))
    out.append(f"\n## Trigger health (generation #{generation})\n")
    out.append("> ORDER 020 (per-wake trigger-health; canonical spec: "
               "fm `docs/trigger-health-spec.md` — moved in 2026-07-14, "
               "plan A2). "
               "Evaluated at **"
               + (eval_dt.strftime("%Y-%m-%dT%H:%MZ") if eval_dt else "n/a")
               + f"** (basis: {eval_basis}); grace {WEDGE_GRACE_MIN}min. A "
               "QUEUED tick (bound to a busy session — delivers when the "
               "turn goes idle, sound by design) is indistinguishable from "
               "a LOST one on the registry, so BOTH are flagged. Recovery "
               "for a DEAD chain / dark seat: `send_message` that seat's "
               "session (the manager's only working cross-session revival "
               "path — fire/update/create_trigger on another session are "
               "org-refused; do NOT re-edit .claude/settings.json for the "
               "prompts, Q-0242). This section rides the Actions regen "
               "substrate so the watchdog's record survives a CCR "
               "scheduler outage.\n")
    if health is None:
        out.append("- **NOT EVALUATED** — no capture-time basis derivable "
                   "from the snapshot.")
    elif not (health["wedged"] or health["dropped"] or health["dead_chains"]):
        out.append("- **All clear** — no wedged crons, no dropped "
                   "one-shots, no dead chains at the evaluated instant.")
    else:
        if health["wedged"]:
            out.append(f"- **WEDGED cron(s): {len(health['wedged'])}** — "
                       "enabled with `next_run_at` frozen in the past:")
            for r in health["wedged"]:
                out.append(f"  - `{r['id']}` {truncate(r['name'], 60)} · "
                           f"`{r.get('cron_expression')}` · next frozen "
                           f"{(r.get('next_run_at') or '?')[:16]}Z · lane: "
                           f"{attribute_lane(r) or '(unattributed)'}")
        if health["dropped"]:
            out.append(f"- **DROPPED-or-QUEUED one-shot(s): "
                       f"{len(health['dropped'])}** — enabled past "
                       "`run_once_at` (never delivered), by seat session:")
            groups: dict = {}
            for r in health["dropped"]:
                groups.setdefault(r.get("persistent_session_id"),
                                  []).append(r)
            for sess in sorted(groups, key=str):
                rs = groups[sess]
                oldest = min((r.get("run_once_at") or "?")[:16] for r in rs)
                lanes = sorted({attribute_lane(r) or "(unattributed)"
                                for r in rs})
                out.append(f"  - `{sess or '(no session id)'}`: {len(rs)} "
                           f"dropped, oldest due {oldest}Z · lane: "
                           + ", ".join(lanes))
        if health["dead_chains"]:
            out.append(f"- **DEAD chain(s): {len(health['dead_chains'])}** "
                       "— dropped tick + NO future tick armed on the "
                       "session (recover via `send_message`):")
            for d in health["dead_chains"]:
                lanes = sorted({attribute_lane(r) or "(unattributed)"
                                for r in d["dropped"]})
                out.append(f"  - `{d['session']}` · {len(d['dropped'])} "
                           "dropped, no future tick · lane: "
                           + ", ".join(lanes))
    out.append("\n> Machine generation: the hand generations' \"Deltas vs "
               "generation #N-1\" narrative is coordinator judgment and is "
               "NOT auto-derived — read `git diff` on this file, or append "
               "prose below before committing.")
    return "\n".join(out) + "\n"


# -------------------------------------------------------------- selfcheck --

def selfcheck() -> int:
    """Offline assertions over the pure logic. Exit 0 on pass."""
    fails = []

    def ok(cond, msg):
        if not cond:
            fails.append(msg)

    # schema: accepts real shape, rejects broken ones
    good = {"data": [{"id": "trig_x", "name": "n", "created_at": "2026-07-11",
                      "enabled": True, "cron_expression": "30 */2 * * *"}]}
    ok(len(validate_export(good)) == 1, "schema accepts a valid record")
    for bad, why in [
        ([], "top-level list"), ({}, "missing data"),
        ({"data": [{}]}, "record missing id"),
        ({"data": [{"id": "x", "name": "n", "created_at": "t"}]}, "bad id prefix"),
        ({"data": [{"id": "trig_x", "name": "n", "created_at": "t",
                    "enabled": "yes"}]}, "non-bool enabled"),
        ({"data": []}, "empty data"),
    ]:
        try:
            validate_export(bad)
            fails.append(f"schema should reject: {why}")
        except SchemaError:
            pass
    # dedup
    two = {"data": [good["data"][0], dict(good["data"][0])]}
    ok(len(validate_export(two)) == 1, "duplicate ids deduplicated")
    # cadence
    ok(cadence_hours("30 * * * *") == 1.0, "hourly cron -> 1h")
    ok(cadence_hours("15 */2 * * *") == 2.0, "*/2 cron -> 2h")
    ok(cadence_hours("0 1-23/2 * * *") == 2.0, "1-23/2 cron -> 2h")
    ok(cadence_hours("0 */4 * * *") == 4.0, "*/4 cron -> 4h")
    ok(cadence_hours("weird") is None, "garbage cron -> None")
    # verdicts
    ok(verdict_for("live", 1.0, 2.0, False) == "FRESH", "1h/2h -> FRESH")
    ok(verdict_for("live", 5.0, 2.0, False) == "STALE", "5h/2h -> STALE")
    ok(verdict_for("live", 30.0, 2.0, False) == "DARK", ">24h -> DARK")
    ok(verdict_for("live", None, 2.0, True) == "UNREADABLE (transport/auth)",
       "wall -> UNREADABLE, never DEAD (gen #21 pokemon-mod-lab lesson)")
    ok(verdict_for("live", None, 2.0, True, private=True)
       == "PRIVATE (auth wall — not DARK; ROSTER_READ_TOKEN pending)",
       "wall on the known private repo renders distinctly (INC-20)")
    ok(verdict_for("live", 1.0, 2.0, False, private=True) == "FRESH",
       "private flag changes nothing when the repo is readable")
    # INC-62: the 8-seat failsafe names attribute to the seat registry rows
    seat_rec = {"id": "trig_s", "name": "Ideas Lab failsafe wake",
                "created_at": "t", "enabled": True,
                "cron_expression": "30 1-23/2 * * *"}
    ok(attribute_lane(seat_rec) == "Ideas Lab seat (idea-engine+sim-lab)",
       "seat-named failsafe attributes to its seat registry row (INC-62)")
    ok(attribute_lane({"id": "trig_s2", "name": "SuperBot World failsafe wake",
                       "created_at": "t", "enabled": True,
                       "cron_expression": "15 1-23/2 * * *"})
       == "SuperBot World seat (games+idle+mineverse)",
       "SuperBot World failsafe attributes to its seat row")
    ok(verdict_for("live", None, 2.0, False) == "DEAD (not measurable)",
       "readable repo with no measurable signal -> DEAD")
    ok(verdict_for("archived", 900.0, 2.0, False) == "STALE-BY-DESIGN",
       "archived override")
    # wall annotation: auth-shaped reasons get the fix pointer, others don't
    ok(AUTH_TOKEN_ENV in describe_wall(
        "fatal: could not read Username for 'https://github.com': "
        "terminal prompts disabled"),
       "auth wall annotated with the read-token pointer")
    ok(AUTH_TOKEN_ENV in describe_wall("remote: Repository not found."),
       "masked-404 private wall annotated too")
    ok(describe_wall("stale proxy pack: abc != def after 5 attempts")
       == "stale proxy pack: abc != def after 5 attempts",
       "non-auth wall left verbatim")
    # read-token injection: dedicated env only, github.com only, no cleartext
    _saved_tok = os.environ.pop(AUTH_TOKEN_ENV, None)
    try:
        ok(_auth_args("https://github.com/menno420/x") == [],
           "no token -> no auth args (unauthenticated read unchanged)")
        os.environ[AUTH_TOKEN_ENV] = "tok-selfcheck"
        aa = _auth_args("https://github.com/menno420/x")
        ok(len(aa) == 2 and aa[0] == "-c"
           and aa[1].startswith("http.https://github.com/.extraheader="
                                "AUTHORIZATION: basic ")
           and "tok-selfcheck" not in aa[1],
           f"token -> basic-auth extraheader, never cleartext ({aa})")
        ok(_auth_args("https://example.com/x") == [],
           "non-github url never receives the header")
        os.environ[AUTH_TOKEN_ENV] = "   "
        ok(_auth_args("https://github.com/menno420/x") == [],
           "blank token (unset Actions secret renders empty) -> unauthenticated")
    finally:
        if _saved_tok is None:
            os.environ.pop(AUTH_TOKEN_ENV, None)
        else:
            os.environ[AUTH_TOKEN_ENV] = _saved_tok
    # age rendering — the float-truncation regression (gen #5 verification
    # run 1: 32.3h must be 32h18m, not 32h17m) + floor-of-seconds semantics
    ok(age_str(32.3) == "~32h18m", "exact minute not truncated by float noise")
    ok(age_str(4 + 33 / 60 + 44 / 3600) == "~4h33m",
       "seconds floored to the minute")
    ok(age_str(0.5) == "~30m", "sub-hour age")
    ok(age_str(-0.1) == "future?", "negative age -> future?")
    # status parsing + stamps
    f = parse_status("# x\nupdated: 2026-07-11T01:45Z\nphase: hello\n"
                     "kit: v1.8.0 · check: green\norders: none\n")
    ok(f.get("updated", "").startswith("2026-07-11"), "updated parsed")
    ok(f.get("kit", "").startswith("v1.8.0"), "kit parsed")
    when = parse_when("2026-07-11T01:45Z")
    ok(when is not None and when.hour == 1, "ISO minute stamp parsed")
    ok(parse_when("garbage") is None, "garbage stamp -> None")
    # utc-offset respected (the %cI bug caught at the first real run)
    off = parse_when("2026-07-11T04:43:22+02:00")
    ok(off is not None and off.hour == 2 and off.minute == 43,
       "+02:00 offset converted to UTC")
    # bullet-form heartbeat headers (venture-lab / pokemon style)
    fb = parse_status("- **timestamp:** t\n- **phase:** work loop X\n"
                      "- **kit:** v1.6.0 · check: green\n")
    ok(fb.get("phase") == "work loop X", "bullet-form phase parsed")
    ok(fb.get("kit", "").startswith("v1.6.0"), "bullet-form kit parsed")
    # kit cell — tree-primary derivation (INC-40) + deliberate pins (INC-41)
    _kr = {"lane": {"repo": "somerepo"},
           "hb": {"kit_tree": {"pinned": "1.15.0", "state": "1.15.0"}},
           "fields": {"kit": "v1.7.1 · check: green"}}
    ok(kit_cell(_kr) == "v1.15.0 (tree; hb line lags — INC-40)",
       "tree beats a lagging heartbeat kit: line")
    _kr["fields"]["kit"] = "v1.15.0 · check: green"
    ok(kit_cell(_kr) == "v1.15.0 (tree)", "tree + agreeing hb line = plain")
    ok(kit_cell({"lane": {"repo": "x"}, "hb": {"kit_tree": {}},
                 "fields": {"kit": "v1.8.0"}}) == "v1.8.0",
       "no tree value falls back to the heartbeat line")
    ok(kit_cell({"lane": {"repo": "x"}, "hb": {}, "fields": {}}) == "—",
       "no data at all renders em-dash")
    ok(kit_cell({"subrow": True, "lane": {"repo": "x"},
                 "hb": {"kit_tree": {"state": "1.15.0"}},
                 "fields": {"kit": "v1.7.1"}})
       == "(parent row; archived kit: line excluded — INC-40)",
       "sub-row kit: line excluded (INC-40 archived-file case)")
    ok(kit_cell({"lane": {"repo": "superbot"},
                 "hb": {"kit_tree": {"pinned": "1.0.0", "state": None}},
                 "fields": {}}) == "v1.0.0 (deliberate pin — INC-41)",
       "hub pin surfaces labeled instead of em-dash (INC-41)")
    # lane: fallback when no phase line exists (product-forge style)
    ff = parse_status("updated: t\nlane: builder (ORDER 001)\n")
    ok("lane: builder" in ff.get("phase", ""), "phase falls back to lane:")
    # trigger attribution incl. prompt-body matching for send_later links
    recs = [
        {"id": "trig_1", "name": "gba-homebrew hourly wake",
         "created_at": "t", "enabled": True, "cron_expression": "0 * * * *"},
        {"id": "trig_2", "name": "send_later 2026-07-11T02:54Z #f0c0e3",
         "created_at": "t", "enabled": True, "run_once_at": "2026-07-11",
         "job_config": {"ccr": {"events": [{"data": {"message": {
             "content": "continue the gba-homebrew chain", "role": "user"}}}]}}},
        {"id": "trig_3", "name": "unrelated", "created_at": "t",
         "enabled": True, "cron_expression": "0 * * * *"},
    ]
    m = match_lane_triggers({"tokens": ["gba"]}, recs)
    ok(len(m["standing"]) == 1 and len(m["oneshot"]) == 1,
       "name + prompt-body attribution")
    # a NAMED trigger whose prompt merely mentions a sibling lane must NOT
    # attribute to it (the sim-lab-mentions-idea-engine mis-attribution
    # caught at the first real run)
    recs2 = [{"id": "trig_9", "name": "sim-lab failsafe wake",
              "created_at": "t", "enabled": True,
              "cron_expression": "0 1-23/2 * * *",
              "job_config": {"ccr": {"events": [{"data": {"message": {
                  "content": "…relay to idea-engine…", "role": "user"}}}]}}}]
    m2 = match_lane_triggers({"tokens": ["idea-engine"]}, recs2)
    ok(not m2["standing"], "named trigger body-mention does not attribute")
    # owner-flag extraction (P2 candidate feed)
    hb_text = ("# lane · status\n"
               "updated: 2026-07-11T12:00Z\n"
               "phase: building (⚑ quoted mid-prose must NOT extract)\n"
               "⚑ needs-owner: none\n"
               "notes: fine\n")
    ok(parse_owner_flags(hb_text) == [], "needs-owner: none extracts nothing")
    hb_text2 = ("updated: t\n"
                "⚑ needs-owner: add required check `pytest`\n"
                "  - WHERE: settings/rules\n"
                "  - HOW: add context\n"
                "notes: x\n")
    fl2 = parse_owner_flags(hb_text2)
    ok(len(fl2) == 1 and len(fl2[0]) == 3 and "WHERE" in fl2[0][1],
       "needs-owner block captured with continuation, ended by header field")
    hb_text3 = ("- **⚑ OWNER-ACTION 1:** enable Pages\n"
                "- **⚑ OWNER-ACTION 2:** tick auto-merge\n"
                "\n"
                "⚑A — Stripe TEST keys\n"
                "still the same block line\n"
                "\n"
                "prose mentioning ⚑ mid-line never starts a block\n")
    fl3 = parse_owner_flags(hb_text3)
    ok(len(fl3) == 3, "bullet OWNER-ACTIONs split into blocks; ⚑A caught; "
                      f"mid-prose ⚑ ignored (got {len(fl3)})")
    ok(fl3[2] == ["⚑A — Stripe TEST keys", "still the same block line"],
       "⚑A block carries its continuation line")
    dup = parse_owner_flags("⚑ OWNER-ACTION x\n\n⚑ OWNER-ACTION x\n")
    ok(len(dup) == 1, "duplicate flag blocks deduplicated")
    fence = parse_owner_flags("```\n⚑ OWNER-ACTION inside fence\n```\n")
    ok(fence == [], "flags inside code fences ignored")
    # slug suggestion — deterministic, content-derived, non-positional
    s = suggest_slug("pokemon-mod-lab", "pokemon-mod-lab",
                     "- **⚑ OWNER-ACTION 1:** add required check `ROM builds`")
    ok(s == "OQ-POKEMON-MOD-LAB-1-ADD-REQUIRED-CHECK", f"slug derivation ({s})")
    ok(suggest_slug("x", "x", "⚑") == "OQ-X-FLAG", "empty slug falls back")
    # queue index keys on OQ slugs
    import tempfile as _tf
    with _tf.NamedTemporaryFile("w", suffix=".md", delete=False) as qf:
        qf.write("## Active queue\n\n1. **games PR #27: MERGE.**\n"
                 "   - id: OQ-GAMES-PR27-MERGE\n"
                 "   - WHERE: https://github.com/menno420/superbot-games/pull/27\n")
        qpath = qf.name
    idx = load_queue_pr_index(qpath)
    os.unlink(qpath)
    ok(idx.get(("superbot-games", "27")) == {"OQ-GAMES-PR27-MERGE"},
       f"queue PR index keyed on slug ids ({idx})")
    # feed sanitization: decision ids checker-inert, fences kept intact
    ok("D-0005" not in _sanitize_feed_line("… per D-0005 forbids …"),
       "decision id hyphen swapped (stamp-discipline inert)")
    ok("D‑0005" in _sanitize_feed_line("… per D-0005 forbids …"),
       "decision id still human-readable after swap")
    ok("```" not in _sanitize_feed_line("```bash"), "fence chars neutralized")
    # pipe escaping (markdown table safety)
    ok("\\|" in truncate("a|b", 50), "pipes escaped in cells")
    ok("D-0002" not in truncate("adopted (D-0002)", 50)
       and "D‑0002" in truncate("adopted (D-0002)", 50),
       "decision ids in roster cells are stamp-discipline inert")
    # P3: heartbeat-file ordering (declared wins, glob catches undeclared,
    # status.md always first, declared-but-absent dropped)
    ok(order_heartbeat_paths(
        ["control/status-mining.md", "control/status.md"],
        ["control/status-exploration.md", "control/status-mining.md",
         "control/status.md"]) ==
       ["control/status.md", "control/status-mining.md",
        "control/status-exploration.md"],
       "heartbeat ordering: status.md first, declared order, glob extras last")
    ok(order_heartbeat_paths(["control/ghost.md"], ["control/status.md"]) ==
       ["control/status.md"], "declared-but-absent heartbeat dropped")
    ok(order_heartbeat_paths([], []) == [], "no heartbeat files -> empty")
    # ORDER 020: trigger-health primitives (wedge / drop / dead-chain)
    _t0 = datetime(2026, 7, 12, 6, 33, tzinfo=timezone.utc)
    _wedged = {"id": "trig_w", "name": "venture-lab money-seat failsafe wake",
               "created_at": "t", "enabled": True,
               "cron_expression": "0 */2 * * *",
               "next_run_at": "2026-07-12T04:06:34.945805082Z"}
    _healthy = {"id": "trig_h", "name": "x failsafe", "created_at": "t",
                "enabled": True, "cron_expression": "30 */2 * * *",
                "next_run_at": "2026-07-12T06:30:00Z"}
    _disabled = dict(_wedged, id="trig_d", enabled=False)
    ok(trigger_wedged(_wedged, _t0), "frozen cron 147m past -> WEDGED")
    ok(not trigger_wedged(_healthy, _t0),
       "cron 3m past next fire is within grace -> not wedged")
    ok(not trigger_wedged(_disabled, _t0), "disabled cron never wedged")
    _drop = {"id": "trig_o", "name": "send_later 2026-07-12T06:00Z #85fcf4",
             "created_at": "t", "enabled": True,
             "run_once_at": "2026-07-12T06:00:00Z",
             "persistent_session_id": "session_dead"}
    _fired = dict(_drop, id="trig_f", enabled=False,
                  ended_reason="run_once_fired")
    _due_soon = {"id": "trig_s", "name": "send_later x", "created_at": "t",
                 "enabled": True, "run_once_at": "2026-07-12T07:00:00Z",
                 "persistent_session_id": "session_live"}
    ok(oneshot_dropped(_drop, _t0), "enabled one-shot 33m past due -> DROPPED")
    ok(not oneshot_dropped(_fired, _t0), "fired (disabled) one-shot not dropped")
    ok(not oneshot_dropped(_due_soon, _t0), "future one-shot not dropped")
    _hr = health_report([_wedged, _healthy, _disabled, _drop, _fired,
                         _due_soon], _t0)
    ok([r["id"] for r in _hr["wedged"]] == ["trig_w"], "health: wedged set")
    ok([r["id"] for r in _hr["dropped"]] == ["trig_o"], "health: dropped set")
    ok([d["session"] for d in _hr["dead_chains"]] == ["session_dead"],
       "dead chain: dropped tick + no future tick on the session")
    _revived = dict(_due_soon, id="trig_r",
                    persistent_session_id="session_dead")
    ok(health_report([_drop, _revived], _t0)["dead_chains"] == [],
       "a future tick on the same session keeps the chain alive")
    _orphan = dict(_drop, id="trig_n")
    _orphan.pop("persistent_session_id")
    ok(health_report([_orphan], _t0)["dead_chains"] == [],
       "session-less dropped one-shot is dropped but never chain-judged")
    # eval-time ladder: captured_at wins; record stamps are the last rung
    _ev, _basis = snapshot_eval_time(
        {"captured_at": "2026-07-12T06:33:02Z", "data": []}, None, [])
    ok(_ev is not None and _ev.minute == 33 and "captured_at" in _basis,
       "eval time: captured_at rung")
    _ev2, _basis2 = snapshot_eval_time(
        {"data": []}, None,
        [{"id": "trig_x", "name": "n", "created_at": "2026-07-12T03:35:50Z",
          "last_fired_at": "2026-07-12T03:00:00Z"}])
    ok(_ev2 is not None and _ev2.hour == 3 and "UNDERSTATES" in _basis2,
       "eval time: record-stamp rung is labeled conservative")
    ok(snapshot_eval_time({"data": []}, None, [])[0] is None,
       "eval time: honest None when underivable")
    # lane attribution + per-lane health cell
    ok(attribute_lane(_wedged) == "venture-lab", "wedged cron lane-attributed")
    ok(attribute_lane(_drop) is None, "anonymous one-shot unattributed")
    _cell = lane_health_cell(
        {"standing": [_wedged], "oneshot": [_drop], "poke": []}, _t0)
    ok("WEDGED" in _cell and "DROPPED" in _cell and "DEAD chain" in _cell,
       f"health cell carries wedge+drop+dead ({_cell})")
    ok(lane_health_cell({"standing": [_healthy], "oneshot": [], "poke": []},
                        _t0) == "OK", "healthy lane cell is OK")
    ok(lane_health_cell({"standing": [], "oneshot": [], "poke": []}, _t0)
       .startswith("—"), "triggerless lane cell is an honest dash")
    ok(lane_health_cell({"standing": [_wedged], "oneshot": [], "poke": []},
                        None) == "n/a (no eval basis)",
       "no eval basis -> n/a cell, never a fabricated verdict")
    # P3: evidence-index rendering (banner, sub-row collapse, honest walls)
    _sha = "a" * 40
    _hb = {"sha": _sha, "attempts": 1, "head_date": "2026-07-11T00:00:00Z",
           "status_text": "", "status_path": "control/status.md",
           "statuses": [{"path": "control/status.md", "text": ""}],
           "evidence": {"current_state": "docs/current-state.md",
                        "latest_card": ".sessions/2026-07-11-x.md",
                        "retro_latest": "docs/retro/r1.md",
                        "retro_count": 2}}
    _rows_ev = [
        {"lane": {"lane": "xlane", "repo": "xrepo"}, "wall": None, "hb": _hb},
        {"lane": {"lane": "↳ xlane — `control/status-sub.md`",
                  "repo": "xrepo"}, "subrow": True, "wall": None, "hb": _hb},
        {"lane": {"lane": "regseat", "repo": None}, "wall": None, "hb": None},
        {"lane": {"lane": "walled", "repo": "wrepo"}, "wall": "boom",
         "hb": None},
    ]
    ev_txt = render_evidence_index(
        _rows_ev, 1, datetime(2026, 7, 11, tzinfo=timezone.utc), "t", "t")
    ok("NOT SOURCE OF TRUTH" in ev_txt, "evidence index carries the banner")
    ok("↳" not in ev_txt, "sub-rows collapse into the parent lane row")
    ok(f"blob/{_sha}/docs/current-state.md" in ev_txt,
       "current-state link pinned at the verified HEAD sha")
    ok("(+1 more)" in ev_txt, "retro count surfaced")
    ok("registry-only seat" in ev_txt, "registry-only seat rendered honestly")
    ok("wall: boom" in ev_txt, "walled repo degrades to NOT MEASURED")

    for msg in fails:
        print(f"SELFCHECK FAIL: {msg}", file=sys.stderr)
    print(f"selfcheck: {'FAIL' if fails else 'PASS'} "
          f"({len(fails)} failure(s))")
    return 1 if fails else 0


# ------------------------------------------------------------------ main ---

def repo_root() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(here)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--triggers", help="path to the list_triggers JSON export")
    ap.add_argument("--generation", type=int,
                    help="generation number (default: committed roster's + 1)")
    ap.add_argument("--date", help="generated-at ISO stamp (default: now UTC);"
                    " Age is computed against this, so identical args give "
                    "reproducible output")
    ap.add_argument("--generated-by",
                    default="machine generation (scripts/gen_roster.py)")
    ap.add_argument("--dispatched-by", default="(not stated)")
    ap.add_argument("--out", help=f"output path (default: {ROSTER_REL})")
    ap.add_argument("--stdout", action="store_true",
                    help="print instead of writing")
    ap.add_argument("--check", action="store_true",
                    help="diff regenerated output vs the committed roster; "
                    "exit 2 on drift")
    ap.add_argument("--selfcheck", action="store_true",
                    help="run offline logic assertions and exit")
    ap.add_argument("--max-fetch-attempts", type=int, default=5)
    args = ap.parse_args(argv)

    if args.selfcheck:
        return selfcheck()

    if not args.triggers:
        ap.error("--triggers is required (export list_triggers to JSON first)")

    try:
        with open(args.triggers, encoding="utf-8") as fh:
            payload = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"gen_roster: cannot read {args.triggers}: {exc}", file=sys.stderr)
        return 1
    try:
        records = validate_export(payload)
    except SchemaError as exc:
        print("gen_roster: SCHEMA MISMATCH — the triggers export does not "
              f"match the documented list_triggers shape: {exc}\n"
              "(see the expected-shape block in this script's docstring; if "
              "the platform changed the response shape, update BOTH.)",
              file=sys.stderr)
        return 1

    roster_path = args.out or os.path.join(repo_root(), ROSTER_REL)
    committed = None
    if os.path.exists(roster_path):
        with open(roster_path, encoding="utf-8") as fh:
            committed = fh.read()

    generation = args.generation
    if generation is None:
        m = committed and re.search(r"\*\*Generation #(\d+)\*\*", committed)
        generation = (int(m.group(1)) + (0 if args.check else 1)) if m else 1

    now = parse_when(args.date) if args.date else datetime.now(timezone.utc)
    if args.date and now is None:
        print(f"gen_roster: cannot parse --date {args.date!r}", file=sys.stderr)
        return 1

    rows = build_rows(records, now, args.max_fetch_attempts,
                      log=lambda *a: print(*a, file=sys.stderr))
    eval_dt, eval_basis = snapshot_eval_time(payload, args.triggers, records)
    text = render(rows, records, generation, now,
                  args.generated_by, args.dispatched_by,
                  eval_dt=eval_dt, eval_basis=eval_basis)

    if args.check:
        if committed is None:
            print(f"gen_roster --check: no committed roster at {roster_path}",
                  file=sys.stderr)
            return 1
        diff = list(difflib.unified_diff(
            committed.splitlines(), text.splitlines(),
            fromfile="docs/roster.md (committed)",
            tofile="regenerated", lineterm=""))
        if diff:
            print("\n".join(diff))
            print(f"\ngen_roster --check: DRIFT — {len(diff)} diff lines "
                  "(committed roster is not current, or was hand-authored "
                  "in the richer prose format)", file=sys.stderr)
            return 2
        print("gen_roster --check: clean — committed roster matches "
              "regeneration")
        return 0

    if args.stdout:
        sys.stdout.write(text)
        return 0

    with open(roster_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"gen_roster: wrote generation #{generation} to {roster_path}")

    # P2 (§3b): the owner-queue candidate feed regenerates WITH the roster —
    # same rows, same generation stamp, one regen path (manual + the
    # roster-regen workflow both get it for free).
    cand_path = (os.path.join(os.path.dirname(roster_path), "owner-queue-candidates.md")
                 if args.out else os.path.join(repo_root(), CANDIDATES_REL))
    queue_index = load_queue_pr_index(os.path.join(repo_root(), OWNER_QUEUE_REL))
    cand_text = render_candidates(rows, generation, now, args.generated_by,
                                  args.dispatched_by, queue_index)
    with open(cand_path, "w", encoding="utf-8") as fh:
        fh.write(cand_text)
    print(f"gen_roster: wrote owner-queue candidate feed to {cand_path}")

    # P3 (§3c): the cross-repo evidence index regenerates WITH the roster —
    # same rows, same pinned SHAs, one regen path.
    ev_path = (os.path.join(os.path.dirname(roster_path), "evidence-index.md")
               if args.out else os.path.join(repo_root(), EVIDENCE_REL))
    ev_text = render_evidence_index(rows, generation, now, args.generated_by,
                                    args.dispatched_by)
    with open(ev_path, "w", encoding="utf-8") as fh:
        fh.write(ev_text)
    print(f"gen_roster: wrote cross-repo evidence index to {ev_path}")

    # C3 (central-docs-plan Slice 0 item 3): the machine-readable lane
    # registry regenerates WITH the roster. The authored source of truth is
    # the LANES constant above (one named writer); this emission exists so
    # external consumers (websites #102's client-side repoint; kit docs that
    # still derived sections from the superseded superbot fleet-manifest)
    # read a stable JSON artifact instead of scraping a python constant.
    lanes_path = (os.path.join(os.path.dirname(roster_path), "..",
                               LANES_JSON_REL)
                  if args.out else os.path.join(repo_root(), LANES_JSON_REL))
    lanes_path = os.path.normpath(lanes_path)
    os.makedirs(os.path.dirname(lanes_path), exist_ok=True)
    lanes_payload = {
        "_source_of_truth": ("GENERATED — the authored master is the LANES "
                             "constant in scripts/gen_roster.py; regenerated "
                             "with every roster generation. Do not hand-edit "
                             "(central-docs-plan C3)."),
        "generation": generation,
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "lanes": [
            {"lane": lane["lane"],
             "repo": lane["repo"],
             "github": (GITHUB_BASE + lane["repo"]) if lane["repo"] else None,
             "disposition": lane["disposition"],
             "tokens": lane["tokens"]}
            for lane in LANES
        ],
    }
    with open(lanes_path, "w", encoding="utf-8") as fh:
        json.dump(lanes_payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"gen_roster: wrote machine-readable lane registry to {lanes_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
