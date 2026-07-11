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
Reliability: unverified — confirm its output against ground truth a few times
            across sessions before trusting it.
            Verification run 1 (2026-07-11, roster gen #5): 6-lane hand sample
            across verdict classes — ALL verdicts + heartbeat/evidence cells
            matched ground truth; ONE display bug found and fixed (age_str
            float truncation, ~32h17m vs true 32h18m; regression selfcheck
            added). Header stays until several clean runs accumulate.
Kill-switch: delete this if it proves unreliable over multiple sessions.
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
  DEAD   — heartbeat NOT MEASURABLE at all (repo/branch/status unreadable)
           on a lane that should have one.
  Overrides: disposition "archived"/"parked" reports STALE-BY-DESIGN instead
  of DARK/DEAD; "registry-only" seats (no repo) are judged on trigger
  last-fire only; the hub (no control/status.md by design) falls back to HEAD
  committer date as its activity signal, as gens #1-#4 did.

TRANSPORT DOCTRINE (inherited from roster gen #3, MANDATORY — the git proxy
serves stale cached clone packs; 9/13 repos came back hours old on first
fetch on 2026-07-10):
  every remote read loops   fetch -> compare FETCH_HEAD to a fresh
  `git ls-remote` -> re-fetch   until the two agree (max --max-fetch-attempts,
  default 5). A repo that never converges, or that cannot be read at all
  (private wall, nonexistent), degrades EXPLICITLY to
  "NOT MEASURED (wall: <reason>)" — a Last-seen is never invented.

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
    "next_cursor": str            # optional
  }
  A merged multi-page export (this repo's convention: one dict with all
  pages' records concatenated under "data") and a raw single page are both
  accepted. Records with duplicate ids are deduplicated (first wins).

USAGE
  # generate (writes docs/roster.md relative to the repo root):
  python3 scripts/gen_roster.py --triggers tmp-triggers.json \
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
#   disposition "live" | "hub" (no control/status.md by design) |
#               "archived" (stale-by-design) | "registry-only" (no repo)
#   tokens      lowercase substrings that attribute triggers (by name, and by
#               stored-prompt content for anonymous send_later links)
# --------------------------------------------------------------------------
LANES = [
    {"lane": "superbot (hub)", "repo": "superbot", "disposition": "hub",
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
    {"lane": "pokemon-mod-lab", "repo": "pokemon-mod-lab",
     "disposition": "live", "tokens": ["pokemon"]},
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


def match_lane_triggers(lane: dict, records: list[dict]) -> dict:
    """Split a lane's enabled triggers into standing / one-shot / poke-only."""
    tokens = [t.lower() for t in lane["tokens"]]

    def owns(rec: dict) -> bool:
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

    mine = [r for r in records if r.get("enabled") and owns(r)]
    return {
        "standing": [r for r in mine if r.get("cron_expression")],
        "oneshot": [r for r in mine if r.get("run_once_at")],
        "poke": [r for r in mine
                 if not r.get("cron_expression") and not r.get("run_once_at")],
    }


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


def ls_remote_head(url: str) -> str:
    """SHA of the remote default-branch HEAD (raises Wall)."""
    out = _git(["ls-remote", url, "HEAD"])
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
        _git(["fetch", "-q", "--depth", "1", url, "HEAD"], cwd=workdir,
             timeout=300)
        fetched = _git(["rev-parse", "FETCH_HEAD"], cwd=workdir).strip()
        target = ls_remote_head(url)  # re-pin: the world may move mid-loop
        if fetched == target:
            return fetched, attempt
    raise Wall(f"stale proxy pack: fetched {fetched[:9]} != ls-remote after "
               f"{max_attempts} attempts")


def read_heartbeat(url: str, max_attempts: int) -> dict:
    """Fetch a repo's HEAD + control/status*.md over verified git transport."""
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
        status_text = None
        status_path = None
        try:
            listing = _git(["ls-tree", "--name-only", "FETCH_HEAD", "control/"],
                           cwd=tmp)
            candidates = [ln for ln in listing.splitlines()
                          if re.fullmatch(r"control/status[^/]*\.md", ln)]
            preferred = [c for c in candidates if c == "control/status.md"]
            for path in preferred + [c for c in candidates if c not in preferred]:
                status_text = _git(["show", f"FETCH_HEAD:{path}"], cwd=tmp)
                status_path = path
                break
        except Wall:
            pass  # no control/ tree — hub-style repo; HEAD date is the signal
        return {"sha": sha, "attempts": attempts, "head_date": head_date,
                "status_text": status_text, "status_path": status_path}


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
    return text if len(text) <= limit else text[: limit - 1] + "…"


# --------------------------------------------------------------- verdict ---

def verdict_for(disposition: str, age_h: float | None, cadence_h: float,
                walled: bool) -> str:
    if disposition == "archived":
        return "STALE-BY-DESIGN"
    if disposition == "registry-only":
        return "n/a (registry-only seat)"
    if walled or age_h is None:
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
        if lane["repo"]:
            url = GITHUB_BASE + lane["repo"]
            try:
                hb = read_heartbeat(url, max_attempts)
                row["hb"] = hb
                if hb["status_text"]:
                    row["fields"] = parse_status(hb["status_text"])
                stamp = row["fields"].get("updated") or hb["head_date"]
                when = parse_when(stamp)
                if when:
                    row["age_h"] = (now - when).total_seconds() / 3600
            except Wall as exc:
                row["wall"] = str(exc)
        row["verdict"] = verdict_for(lane["disposition"], row["age_h"],
                                     row["cadence"], row["wall"] is not None)
        rows.append(row)
    return rows


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
           now: datetime, generated_by: str, dispatched_by: str) -> str:
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
               "with the verbatim wall reason — never guessed.\n>")
    out.append(f"> **Trigger evidence:** {len(records)}-record export, "
               f"**{len(enabled)} enabled**: {len(crons)} standing crons + "
               f"{len(pokes)} poke-only + {len(ones)} one-shots.\n")
    out.append("| Lane | Heartbeat `updated:` | Age | Verdict | Phase (machine-truncated) | Orders | Kit | Wake state (trigger · cron · last fire) | Evidence (repo @ HEAD) |")
    out.append("|---|---|---|---|---|---|---|---|---|")

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
                   "| {kit} | {wake} | {evidence} |".format(
                       lane=lane["lane"], hb=hb_cell, age=age,
                       verdict=row["verdict"],
                       phase=truncate(f.get("phase", "—"), 160),
                       orders=truncate(f.get("orders", "—"), 100),
                       kit=truncate(f.get("kit", "—"), 40),
                       wake=render_wake(row["trig"]),
                       evidence=evidence))

    out.append(f"\n## Staleness verdicts (generation #{generation})\n")
    order = ["DARK", "DEAD (not measurable)", "STALE", "FRESH",
             "STALE-BY-DESIGN", "n/a (registry-only seat)"]
    for v in order:
        lanes = [r["lane"]["lane"] for r in rows if r["verdict"] == v]
        if lanes:
            out.append(f"- **{v}:** " + ", ".join(lanes))
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
    ok(verdict_for("live", None, 2.0, True).startswith("DEAD"),
       "wall -> DEAD")
    ok(verdict_for("archived", 900.0, 2.0, False) == "STALE-BY-DESIGN",
       "archived override")
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
    # pipe escaping (markdown table safety)
    ok("\\|" in truncate("a|b", 50), "pipes escaped in cells")

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
    text = render(rows, records, generation, now,
                  args.generated_by, args.dispatched_by)

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
    else:
        with open(roster_path, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"gen_roster: wrote generation #{generation} to {roster_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
