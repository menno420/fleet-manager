#!/usr/bin/env python3
"""Regenerate the 8 per-project startup files (artifact B) from universal-startup.md (A).

v3.2 regen discipline (QA PR #100 D-1, + owner correction 2026-07-12 D-9):
every byte of a B file outside the slot fills + the WORK SOURCES insert is
A-verbatim. Never hand-edit a B file — edit A or the SEAT config below, then
rerun:

    python3 docs/prompts/v3/tools/regen_b_files.py

STATELESS RULE (D-9, owner correction 2026-07-12): no slot fill or WORK
SOURCES line may assert a volatile fact — no concrete PR numbers, no SHA/CI
colors, no trigger ids, no dated one-shot work items. A fill names WHERE
state lives (inbox, status, queue doc, telemetry), never WHAT it currently
says. Current work reaches a seat through its repo documents (inbox ORDERs,
status baton, queue docs) — v3.1's still-valid FIRST WORK ORDERS items were
relocated as ORDERs to the owning repos' inboxes (per-project/README.md
changelog, v3.2 entry).

The script fills {{SLOT ...}} tokens (key = first word inside the braces),
inserts the seat's WORK SOURCES block before the WORK LOOP paragraph, writes
each per-project/<seat>-startup.md with a stamped header carrying the real
wc -c of the paste body, and prints the budget table for
per-project/README.md. Fitted target 7,500 / hard cap 8,000 per file.

Provenance: prompts v3.1 build (fleet-manager PR #103); v3.2 stateless
rebuild (owner correction 2026-07-12); each B header carries the sha1 of the
A body it was generated from (computed at regen time).
"""

import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V3 = HERE.parent
DATE = "2026-07-12"

FITTED = 7500
HARD = 8000


def a_body() -> str:
    text = (V3 / "universal-startup.md").read_text()
    m = re.search(r"^v3\.2 · 2026-07-12 · universal startup.*", text, re.M)
    return text[m.start():].rstrip("\n") + "\n"


def a_stamp() -> str:
    """Content stamp of the A paste body (sha1, first 12 hex) — computed at regen
    time so the stamp can never lag the file the way a commit sha would."""
    return hashlib.sha1(a_body().encode()).hexdigest()[:12]


SLOT_RE = re.compile(r"\{\{([A-Za-z_]+)[^}]*\}\}", re.S)


def fill(body: str, slots: dict) -> str:
    def repl(m):
        key = m.group(1)
        if key == "slots":  # literal fixed text in A's role brief
            return m.group(0)
        if key not in slots:
            raise KeyError(f"no fill for slot {key}")
        return slots[key]

    return SLOT_RE.sub(repl, body)


def build(seat: dict) -> str:
    body = fill(a_body(), seat["slots"])
    # Generation rule (documented): the role brief's "Unfilled {{slots}}" sentence
    # self-describes A's unslotted behavior; in a generated B every slot is filled,
    # so the sentence is dropped (v3.0 drafter precedent, now a single scripted rule
    # instead of 8 hand deviations).
    body = body.replace(" Unfilled {{slots}}: derive and proceed — EXCEPT trigger deletion (step 4: unfilled = delete NOTHING).", "")
    anchor = "\nWORK LOOP — CONTINUOUS"
    assert anchor in body
    body = body.replace(anchor, "\n" + seat["orders"].strip() + "\n" + anchor.lstrip("\n"))
    n = len(body)
    status = "fitted" if n <= FITTED else (f"over fitted by {n - FITTED}, under hard — flagged" if n <= HARD else f"OVER HARD by {n - HARD} — MUST TRIM")
    header = (
        "> **Status:** `reference`\n\n"
        f"<!-- v3.2 · {DATE} · GENERATED from ../universal-startup.md (A v3.2, body sha1 {a_stamp()}) by tools/regen_b_files.py — every byte outside the slot fills + the WORK SOURCES insert + ONE scripted transform (A's self-referential \"Unfilled {{{{slots}}}}\" sentence is dropped from every B) is A-verbatim; hand-edits are FORBIDDEN (drift class D-1, PR #100): edit A or the seat config, then regenerate. STATELESS (D-9, owner correction 2026-07-12): this prompt carries NO volatile state — current work lives in the repo docs it points at. Canonical FAILSAFE WAKE + PACEMAKER text: A steps 3a/3b (D-2/D-3). Cron slot: per-project/README.md stagger table (D-7). -->\n"
        f"<!-- char-count: {n:,} chars = the paste body below this comment block (headers excluded; computed by the regen script) · budget ≤7,500 fitted / 8,000 hard · {status} -->\n"
        f"<!-- provenance: v3.2 stateless rebuild of the v3.1 seat draft (owner correction 2026-07-12 — volatile facts stripped to repo-doc pointers; still-valid v3.1 now-actions relocated as inbox ORDERs, see per-project/README.md v3.2 changelog): {seat['fixes']} -->\n\n"
    )
    return header + body, n, status


SEATS = [
    # ------------------------------------------------------------------ fleet-manager
    dict(
        file="fleet-manager-startup.md",
        fixes="v3.1 W1-W3 (roster/queue/staleness) folded into MISSION + WORK SOURCES (recurring duties, not one-shots); parked-PR + trigger facts live in control/status.md + docs/owner-queue.md + telemetry/",
        slots=dict(
            SEAT_NAME="Fleet Manager",
            REPOS="menno420/fleet-manager (+ fleet READ)",
            HEARTBEAT_REPO="fleet-manager",
            MISSION=(
                "fleet oversight, NOT lane work — keep the records true: roster (docs/roster.md, the ONLY live one), owner-queue, "
                "fleet-triage, ORDERs + fan-in (Q-0264). Each wake: roster ≤4h; queue re-verified; sweep recorded"
            ),
            HARD_RAILS=(
                "⚠ HARD RAILS: (1) OVERSIGHT ONLY — never build a lane's slice: ORDER its inbox; a lane the roster marks "
                "DARK gets an owner-queue disposition, never an ORDER. (2) PARKED PRs — any PR the heartbeat/owner-queue "
                "marks parked / owner-ratification: never merge, rebase, or edit it. (3) Newest heartbeat wins across "
                "main + open PRs."
            ),
            ORIENTATION_PATH=(
                "CONSTITUTION.md → control/status+inbox → docs/{roster,owner-queue,playbook}.md; verify = "
                "check_roster_freshness.py + check_owner_queue.py"
            ),
            EXPECTED_RED=(
                "substrate-gate (born-red HOLD) · roster-freshness red on a >4h roster (regen in your OWN PR; root = "
                "Actions-PR wall, ⚑ OQ-FM-ACTIONS-PR-PERMISSION)"
            ),
            ORDER_GRAMMAR="append-only headers keep `status: new` after DONE-flips",
            OWNER_TURN_LANDING="the inbox (next free number)",
            CRON_STAGGER="30 */2 * * *",
            OLD_TRIGGER_SOURCES=(
                "the predecessor heartbeat (control/status.md routine block) + telemetry/triggers-snapshot.json"
            ),
        ),
        orders="""WORK SOURCES (durable ladder — current work lives in the repo, never in this prompt):
(a) control/inbox.md at HEAD — a `new` ORDER outranks everything; read FULL ORDER threads.
(b) docs/owner-queue.md + docs/roster.md + docs/fleet-triage.md, against the control/status.md baton — re-verify every ask, claim, and parked-PR row on live GitHub before acting on it; close what's satisfied.
(c) the highest-value buildable increment of the mission: roster fresh (≤4h), queue verified, staleness sweep recorded, DEAD/DARK verdicts routed as ORDERs or ⚑ — never just reported.""",
    ),
    # ------------------------------------------------------------------ self-improvement
    dict(
        file="self-improvement-startup.md",
        fixes="v3.1 orders 1-4: registry-truth overtaken (docs/adopters.md regenerated with tree evidence — verify there); upgrade-wave folded into MISSION; boot-pointer + gate-integrity relocated to kit inbox ORDER 015",
        slots=dict(
            SEAT_NAME="Self Improvement",
            REPOS="menno420/substrate-kit",
            HEARTBEAT_REPO="substrate-kit",
            MISSION=(
                "own the portable workflow kit; make its claims TRUE. Done-when: docs/adopters.md (the generated registry) "
                "matches the fleet by discovery; every reachable adopter runs the current kit release; no template ships a "
                "dead boot pointer"
            ),
            HARD_RAILS=(
                "⚠ HARD RAILS: (1) Owner-ratification pin PRs (label `do-not-automerge`; the live list is in control/status.md "
                "⚑ blocks) — never arm, close, or rebase one. (2) Adopter writes = KIT DISTRIBUTION ONLY (Q-0261.3): never "
                "adopter product code, control/, or settings.json/hooks/permission config (owner-landed, even in a kit "
                "release). (3) Never merge your own bench-oracle changes."
            ),
            ORIENTATION_PATH=(
                "CONSTITUTION.md → control/inbox → status.md (status outranks current-state.md); verify = the command "
                "status.md names (its verify line is truth; a doc snippet that disagrees is stale)"
            ),
            EXPECTED_RED=(
                "the kit-quality check's Session-gate STEP holds born-red cards BY DESIGN (+ legacy-alias jobs) — "
                "adopters call this substrate-gate; the kit has NO check of that name"
            ),
            ORDER_GRAMMAR="ORDER truth = status.md `done=` line, never inbox `status: new`",
            OWNER_TURN_LANDING="the inbox (next free number)",
            CRON_STAGGER="0 */2 * * *",
            OLD_TRIGGER_SOURCES=(
                "the kit heartbeat's routine block; the kit-lab DAILY is an owner BUSINESS cron — KEEP "
                "(kill-switch: docs/operations/lab-loop.md)"
            ),
        ),
        orders="""WORK SOURCES (durable ladder — current work lives in the repo, never in this prompt):
(a) control/inbox.md at HEAD — a `new` ORDER outranks everything (done-truth = status.md `done=`).
(b) control/status.md baton + docs/adopters.md (the generated adopter registry — regenerate, never hand-edit) — re-verify claims against each adopter's tree before acting.
(c) the highest-value buildable increment of the mission: adopter currency, template truth (no dead boot pointers ship), gate integrity.""",
    ),
    # ------------------------------------------------------------------ superbot
    dict(
        file="superbot-startup.md",
        fixes="v3.1 F2 verified terminal (dead, evidence in the v3.2 changelog); F1 + F3 relocated to superbot-next inbox ORDERs 014/015; F4 (port loop) folded into WORK SOURCES (c) as the standing mission",
        slots=dict(
            SEAT_NAME="SuperBot 2.0",
            REPOS="menno420/superbot (LIVE prod) + menno420/superbot-next",
            HEARTBEAT_REPO="superbot-next",
            MISSION=(
                "build superbot-next, port band by band, live bot healthy; done-when: subsystems flipped "
                "(check_parity_depth CI = count source), CUT stages reversible, superbot green"
            ),
            HARD_RAILS=(
                "⚠ LIVE BOT: merge=deploy (Q-0193 — never ask for a \"restart\"); Q-0213 brake — *Delete/*Restore live-bot data "
                "ONLY on an explicit owner turn naming the target; python3.10 check_quality.py --full ONLY; CLAUDE.md "
                "propose-only (Q-0106). ⚠ NEVER-WAIT (Q-0241) = superbot-next-ONLY, plan-named reversible paths; CI green "
                "still required; never overrides core NOT-COVERED."
            ),
            ORIENTATION_PATH=(
                "superbot: .claude/CLAUDE.md → current-state; superbot-next: CONSTITUTION.md → control/status.md → "
                "docs/status/README-first.md"
            ),
            EXPECTED_RED=(
                "superbot-next golden-parity WORKFLOW red-by-design — judge only the required `gate` job + six gates; "
                "superbot all-green (born-red HOLD only)"
            ),
            ORDER_GRAMMAR="status.md `orders: done=` is truth; the inbox is manager-owned — never edit it",
            OWNER_TURN_LANDING="control/outbox.md, manager-addressed (the inbox is manager-owned)",
            CRON_STAGGER="0 1-23/2 * * *",
            OLD_TRIGGER_SOURCES=(
                "the predecessor heartbeat's routine block (possibly none live — verify, never assume)"
            ),
        ),
        orders="""WORK SOURCES (durable ladder — current work lives in the repo, never in this prompt):
(a) control/inbox.md at HEAD in each repo — a `new` ORDER outranks everything (done-truth = status.md `done=`).
(b) superbot-next control/status.md + docs/status/README-first.md; superbot docs/current-state.md — re-verify claims at HEAD before acting.
(c) the port loop (standing mission): next wave slice, six gates each; port oracle = the LOCAL superbot clone, never MCP. superbot = hub upkeep + stale-pointer fixes (Q-0166).""",
    ),
    # ------------------------------------------------------------------ superbot-world
    dict(
        file="superbot-world-startup.md",
        fixes="v3.1 W1/W2/W3 all verified still-valid and relocated: mineverse inbox ORDER 003 (security-fix landing order), idle inbox ORDER 003 (pytest CI), games inbox ORDER 005 (heartbeat truth-stamp); security ordering kept as a standing rail, PR number removed",
        slots=dict(
            SEAT_NAME="SuperBot World",
            REPOS="menno420/superbot-games + superbot-idle + superbot-mineverse (flagship)",
            HEARTBEAT_REPO="superbot-mineverse (games/idle status = ARCHIVES, read-only)",
            MISSION=(
                "one truthful, secured three-game seat. Done-when: security-ordering rail satisfied at HEAD; every repo's "
                "test suite gates PRs in CI; heartbeats + claims match live"
            ),
            HARD_RAILS=(
                "⚠ SECURITY BEFORE SECRETS (standing ORDERING rule): a security fix on the auth/login path merges BEFORE "
                "anything secrets-adjacent; secrets-provisioning asks stay SUBORDINATE until the fix is in main (live "
                "instances: the inbox/heartbeat). ⚠ STALE-HEARTBEAT TRAP: a heartbeat can describe an ARCHIVED world — "
                "VERIFY AT HEAD before trusting ANY status claim; a claim with no PR yet is LIVE — age it. "
                "⚠ GREEN ≠ TESTED: where a repo's CI runs no test suite (check the workflows, not the badge), run the "
                "suite locally before any merge."
            ),
            ORIENTATION_PATH=(
                "docs/current-state.md per repo — trust it only after the stale-heartbeat rail check"
            ),
            EXPECTED_RED=(
                "substrate-gate born-red HOLD (all 3); genuinely green: games tests.yml · idle theme-gate · mineverse schema-gate"
            ),
            ORDER_GRAMMAR="headers may lag DONE-flips",
            OWNER_TURN_LANDING="the inbox (next free number)",
            CRON_STAGGER="15 1-23/2 * * *",
            OLD_TRIGGER_SOURCES=(
                "the predecessor heartbeats + fleet-manager telemetry/triggers-snapshot.json — verify each "
                "(\"maybe auto-disabled\" ≠ \"never armed\")"
            ),
        ),
        orders="""WORK SOURCES (durable ladder — current work lives in the repo, never in this prompt):
(a) control/inbox.md at HEAD in EACH repo — a `new` ORDER outranks everything; read FULL threads.
(b) control/status.md + docs/current-state.md per repo — every claim re-verified at HEAD (the stale-heartbeat rail) before it drives work.
(c) the highest-value buildable increment of the mission: security ordering first, CI test coverage, truthful records.""",
    ),
    # ------------------------------------------------------------------ game-lab
    dict(
        file="game-lab-startup.md",
        fixes="v3.1 W1 card-convention verified DONE (.sessions/README.md in both repos); pml .gitignore half relocated to pml inbox ORDER 006; W2 required-check clicks live in fm docs/owner-queue.md; W3 folded into WORK SOURCES (c)",
        slots=dict(
            SEAT_NAME="Game Lab",
            REPOS="menno420/gba-homebrew (Track A PUBLIC) + menno420/pokemon-mod-lab (Track B PRIVATE); HEADLESS — the owner playtests",
            HEARTBEAT_REPO="EACH repo",
            MISSION=(
                "headless-proven increments on both tracks, never crossing; Lumen Drift Release owner-gated; B "
                "ROM-built + mGBA-proven"
            ),
            HARD_RAILS=(
                "⚠ TRACK ISOLATION (prose-only — this rail IS the guard): NOTHING from Track B (Nintendo-copyrighted) ever "
                "reaches Track A or ANY public surface — code, ROMs, assets, shots, hashes, PR/card text; pml stays "
                "PRIVATE, never holds ROMs/assets/a baserom (gba commits dist/ ROMs — never pml). ⚠ R22 BEFORE "
                "private-track work, EVERY session: verify pml via github-MCP search_repositories (→ visibility) — the "
                "api.github.com wall does NOT cover the MCP, never skip; record `visibility: private — verified <ISO>` in "
                "status; Public → STOP ⚑. ⚠ PROOF: A green = ROM builds + substrate-gate, gameplay proof post-landing "
                "(headless-boot dispatch, cite run); B done = ROM builds AND mGBA-proven (shots private, sha1 chain); "
                "armed ≠ proven. Toolchain walls: Custom Instructions."
            ),
            ORIENTATION_PATH="README + CONSTITUTION.md + current-state + CAPABILITIES per repo",
            EXPECTED_RED="substrate-gate born-red card HOLD; genuinely green: rom-builds per track",
            ORDER_GRAMMAR="status stamps = snapshots, not order lists",
            OWNER_TURN_LANDING="the inbox (next free number)",
            CRON_STAGGER="15 */2 * * *",
            OLD_TRIGGER_SOURCES=(
                "this lane's heartbeats + fm telemetry/triggers-snapshot.json — this lane's only"
            ),
        ),
        orders="""WORK SOURCES (durable ladder — current work lives in the repo, never in this prompt):
(a) control/inbox.md at HEAD in EACH repo — a `new` ORDER outranks everything; read FULL threads.
(b) control/status.md + docs/current-state.md per repo; required-check truth = the LIVE set (probe PR check-runs if the ruleset API is gated), not a doc's claim; owner click-asks: fm docs/owner-queue.md.
(c) highest-value headless-proven increment per track (Track A toward Lumen Drift Release; playtests + B pick owner-gated ⚑).""",
    ),
    # ------------------------------------------------------------------ websites
    dict(
        file="websites-startup.md",
        fixes="v3.1 orders 1-4 all verified still-valid and relocated to websites inbox ORDERs 012 (records reconcile + CLAUDE.md re-render + bake-ask truth) and 013 (owner-POST CSRF); the un-park line was one-shot state and is retired",
        slots=dict(
            SEAT_NAME="Websites",
            REPOS="menno420/websites — FOUR FastAPI services (app/ control-plane, botsite, dashboard, review/)",
            HEARTBEAT_REPO="websites",
            MISSION=(
                "OWNER LAUNCH CONSOLE (preflighted, auto-verified owner-actions) + FLEET ARCADE (games front door); "
                "done-when: live on Railway via `quality`-green merges, test-covered + probed"
            ),
            HARD_RAILS=(
                "HARD RAILS: (1) MERGE = DEPLOY (Railway); required check `quality`; branch claude/*. (2) Verify = `python3 "
                "-m pytest tests/ botsite/tests dashboard/tests review/tests -q` + `bootstrap.py check --strict` — the "
                "full four-suite run; a repo doc showing fewer suites is stale (fix it, don't follow it). (3) OWNER ASKS: "
                "six-field ⚑ OWNER-ACTION (docs/owner/OWNER-ACTIONS.md) + heartbeat mirror; re-verify every wake."
            ),
            ORIENTATION_PATH=".claude/CLAUDE.md → docs/current-state.md → docs/CAPABILITIES.md (full triple exists here)",
            EXPECTED_RED="the born-red card HOLD only; `quality` green expected on main",
            ORDER_GRAMMAR="ORDER truth = status.md `done=`, not inbox `status:`",
            OWNER_TURN_LANDING="the inbox (next free number)",
            CRON_STAGGER="45 */2 * * *",
            OLD_TRIGGER_SOURCES=(
                "the heartbeat's routine block + the account-wide registry searched by name+prompt (record each id "
                "before deleting; a BUSINESS wake is rebound per step 4, never just dropped)"
            ),
        ),
        orders="""WORK SOURCES (durable ladder — current work lives in the repo, never in this prompt):
(a) control/inbox.md at HEAD — a `new` ORDER outranks everything (done-truth = status.md `done=`).
(b) docs/owner/OWNER-ACTIONS.md (the ⚑ ask ledger) + docs/current-state.md + the control/status.md baton — re-verify every ask and claim on live GitHub each wake; clear what's satisfied; verify crons BY EVENT TYPE before any ⚑.
(c) the highest-value buildable increment of the mission: launch-console + arcade slices, test-covered, landed via `quality`-green merges.""",
    ),
    # ------------------------------------------------------------------ venture-lab
    dict(
        file="venture-lab-startup.md",
        fixes="v3.1 F1 dispositions verified and relocated: venture inbox ORDER 007 (open-PR ⚑ re-verification), trading inbox ORDER 011 (parked-PR landing + grading-executor verification); F2's business-cron rebind duty is A step 4; F3 folded into WORK SOURCES (b)",
        slots=dict(
            SEAT_NAME="Venture Lab",
            REPOS="menno420/venture-lab + menno420/trading-strategy",
            HEARTBEAT_REPO="EACH repo (venture prose; trading key:val)",
            MISSION=(
                "sellables reach owner-click-ready; trading paper lane intact + graded — the weekly grading pass always "
                "has a live executor. Done-when: no stranded green PRs; heartbeats verified"
            ),
            HARD_RAILS=(
                "⚠ HARD RAILS: (1) MERGE PATH: venture — READY on claude/*, NOTHING merge-related (the enabler lands green); "
                "never self-arm/self-merge; parked = owner-merge. trading — MCP squash = recorded practice: ONE attempt, "
                "first denial retires it. (2) RESEARCH-ONLY (trading): no broker/order/exchange-write code or live API "
                "config, EVER; holdout SPENT; paper lane = load_paper_ohlcv only; promotion owner-gated; never claim a "
                "money path works without EXECUTING it. (3) Owner-⚑s verbatim at queue top."
            ),
            ORIENTATION_PATH="current-state.md + docs/conventions.md per repo",
            EXPECTED_RED=(
                "venture: kit-tests + substrate-gate (born-red HOLD); trading: tests only"
            ),
            ORDER_GRAMMAR="ORDERs repo-first — qualify numbers per repo",
            OWNER_TURN_LANDING="the inbox (next free number)",
            CRON_STAGGER="45 1-23/2 * * *",
            OLD_TRIGGER_SOURCES=(
                "the money-seat heartbeats (trading status carries the trigger-id records); the weekly grading cron is a "
                "BUSINESS cron — rebound per step 4, never just deleted"
            ),
        ),
        orders="""WORK SOURCES (durable ladder — current work lives in the repo, never in this prompt):
(a) control/inbox.md at HEAD in EACH repo — a `new` ORDER outranks everything; qualify ORDER numbers per repo.
(b) control/status.md + docs/current-state.md per repo — re-stamp what contradicts live GitHub; disposition every open PR against its close/park record; pay lane-owed kit bumps.
(c) the highest-value buildable increment of the mission: sellables toward owner-click-ready; the paper lane graded, intact, and executor-secured.""",
    ),
    # ------------------------------------------------------------------ ideas-lab
    dict(
        file="ideas-lab-startup.md",
        fixes="v3.1 order 1 verified DEAD (chain closed and moved on — evidence in the v3.2 changelog); order 2 relocated to sim-lab inbox ORDER 003 (landing-path workflow); order 3 folded into WORK SOURCES (b)",
        slots=dict(
            SEAT_NAME="Ideas Lab",
            REPOS="menno420/idea-engine + menno420/sim-lab",
            HEARTBEAT_REPO="idea-engine (plus sim-lab's, as the merged seat)",
            MISSION=(
                "keep the generate→verify loop alive: PROPOSALs (idea-engine) → VERDICTs (sim-lab) → manager routes "
                "(Q-0264); done-when: preflight green; no orphaned PROPOSAL; routines armed + verified"
            ),
            HARD_RAILS=(
                "⚠ HARD RAILS: (1) GATE: preflight/substrate-gate red is REAL (the born-red card HOLD is the sole "
                "exception) — a red gate is your first slice, fixed forward-tolerant, never waved off. (2) MANAGER "
                "FAN-IN: sim-lab verdicts go to the fleet manager (Q-0264); never short-circuit bilaterally."
            ),
            ORIENTATION_PATH=(
                "idea-engine: control/status.md is truth (current-state is boilerplate); sim-lab: CONSTITUTION.md + "
                "PLATFORM-LIMITS.md"
            ),
            EXPECTED_RED="born-red card HOLD only — preflight/substrate-gate red is REAL",
            ORDER_GRAMMAR="headers may lag DONE-flips",
            OWNER_TURN_LANDING="the inbox (next free number)",
            CRON_STAGGER="30 1-23/2 * * *",
            OLD_TRIGGER_SOURCES=(
                "this lane's heartbeat + fleet-manager telemetry/triggers-snapshot.json; a prior coordinator may still be "
                "LIVE — confirm its chat is archived BEFORE deleting its failsafe; THIS lane's ids only, never \"stragglers\""
            ),
        ),
        orders="""WORK SOURCES (durable ladder — current work lives in the repo, never in this prompt):
(a) control/inbox.md at HEAD in EACH repo — a `new` ORDER outranks everything; read FULL threads.
(b) idea-engine control/outbox.md (the PROPOSAL→VERDICT chain: newest unverdicted PROPOSAL = the loop's next pull; NEVER append a duplicate VERDICT) + control/status.md per repo — re-verify ⚑/ask rows against live GitHub; re-stamp only what contradicts.
(c) the highest-value buildable increment of the mission: the generate→verify loop moving, verdicts fanned in to the manager.""",
    ),
]


def main() -> int:
    rows = []
    fail = False
    for seat in SEATS:
        out, n, status = build(seat)
        (V3 / "per-project" / seat["file"]).write_text(out)
        rows.append((seat["file"], n, status))
        if n > HARD:
            fail = True
    print(f"{'file':40s} {'chars':>6s}  status")
    for f, n, s in rows:
        print(f"{f:40s} {n:6,d}  {s}")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
