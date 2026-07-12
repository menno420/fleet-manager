#!/usr/bin/env python3
"""Regenerate the 8 per-project startup files (artifact B) from universal-startup.md (A).

v3.1 regen discipline (QA PR #100, drift class D-1): every byte of a B file
outside the slot fills + the FIRST WORK ORDERS insert is A-verbatim. Never
hand-edit a B file — edit A or the SEAT config below, then rerun:

    python3 docs/prompts/v3/tools/regen_b_files.py

The script fills {{SLOT ...}} tokens (key = first word inside the braces),
inserts the seat's FIRST WORK ORDERS block before the WORK LOOP paragraph,
writes each per-project/<seat>-startup.md with a stamped header carrying the
real wc -c of the paste body, and prints the budget table for
per-project/README.md. Fitted target 7,500 / hard cap 8,000 per file.

Provenance: prompts v3.1 build (fleet-manager PR #103); A commit stamped in
A_COMMIT below — update it when A changes.
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V3 = HERE.parent
A_COMMIT = "08c86fa"  # universal-startup.md (A v3.1) source commit — update on every A edit
DATE = "2026-07-12"

FITTED = 7500
HARD = 8000


def a_body() -> str:
    text = (V3 / "universal-startup.md").read_text()
    m = re.search(r"^v3\.1 · 2026-07-12 · universal startup.*", text, re.M)
    return text[m.start():].rstrip("\n") + "\n"


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
    n = len(body.encode("utf-8")) if False else len(body)
    status = "fitted" if n <= FITTED else (f"over fitted by {n - FITTED}, under hard — flagged" if n <= HARD else f"OVER HARD by {n - HARD} — MUST TRIM")
    header = (
        "> **Status:** `reference`\n\n"
        f"<!-- v3.1 · {DATE} · GENERATED from ../universal-startup.md (A v3.1 @ {A_COMMIT}) by tools/regen_b_files.py — every byte outside the slot fills + the FIRST WORK ORDERS insert is A-verbatim; hand-edits are FORBIDDEN (drift class D-1, PR #100): edit A or the seat config, then regenerate. Canonical FAILSAFE WAKE + PACEMAKER text: A steps 3a/3b (D-2/D-3). Cron slot: per-project/README.md stagger table (D-7). -->\n"
        f"<!-- char-count: {n:,} chars = the paste body below this comment block (headers excluded; computed by the regen script) · budget ≤7,500 fitted / 8,000 hard · {status} -->\n"
        f"<!-- provenance: v3.0 seat draft (research PRs #93/#95 + census PRs #94/#96 + owner baseline 2026-07-11) + QA fixes applied from PRs #100/#101/#102: {seat['fixes']} -->\n\n"
    )
    return header + body, n, status


SEATS = [
    # ------------------------------------------------------------------ fleet-manager
    dict(
        file="fleet-manager-startup.md",
        fixes="boot-sim FM-1..FM-4; replay C-7/C-9 (cutover ids reconciled vs the armed registry; retro-games id ceded to Game Lab); question-rounds P0 regen set",
        slots=dict(
            SEAT_NAME="Fleet Manager",
            REPOS="menno420/fleet-manager (+ fleet READ)",
            HEARTBEAT_REPO="fleet-manager",
            MISSION=(
                "fleet oversight, NOT lane work — keep the records true: roster (docs/roster.md, the ONLY live one), owner-queue, "
                "fleet-triage, ORDERs + fan-in (Q-0264). Each wake: roster ≤4h; queue re-verified; sweep recorded"
            ),
            HARD_RAILS=(
                "⚠ HARD RAILS: (1) OVERSIGHT ONLY — never build a lane's slice: ORDER its inbox; product-forge is DARK — "
                "don't ORDER it, owner-queue its disposition (not a seat). (2) PARKED STACK #88/#89/#91/#92 — never "
                "merge/rebase/edit; expect parked, or later. (3) Newest heartbeat wins across main + open PRs (#97)."
            ),
            ORIENTATION_PATH=(
                "CONSTITUTION.md → control/status+inbox → docs/{roster,owner-queue,playbook}.md (no CLAUDE.md — expected, "
                "#92 parked); verify = check_roster_freshness.py + check_owner_queue.py"
            ),
            EXPECTED_RED=(
                "substrate-gate (born-red HOLD) · roster-freshness red on a >4h roster (regen in your OWN PR; root = "
                "Actions-PR wall, ⚑ OQ-FM-ACTIONS-PR-PERMISSION)"
            ),
            ORDER_GRAMMAR="append-only headers keep `status: new` after DONE-flips",
            CRON_STAGGER="30 */2 * * *",
            OLD_TRIGGER_IDS=(
                "the live prior failsafe (heartbeat/#97: trig_01F9UdoUtLy8oknBPBkHLshS; census: trig_01BKpsyoBzp1K1ob9H3iu1gM) "
                "— verify each; retro-games trig_01Y99uDKNtKTz2EtRYPWZkGY is GAME LAB's, not yours"
            ),
        ),
        orders="""FIRST WORK ORDERS (each: verify at boot — expected as of 2026-07-12, or later; one PR each):
1. ROSTER — regen docs/roster.md (R25) in your session PR whenever generated-at >4h (gen #10 expected on main, PR #99). Done-when: roster-freshness green.
2. QUEUE SWEEP — re-verify every owner-queue ask + heartbeat claim on live GitHub; close satisfied ones. Done-when: zero stale asks.
3. STALENESS SWEEP — stamp vs git log -1 + live PRs per lane; verdicts to fleet-triage; a DEAD verdict becomes a routed ORDER or ⚑, never just a report. Done-when: dated verdicts.""",
    ),
    # ------------------------------------------------------------------ self-improvement
    dict(
        file="self-improvement-startup.md",
        fixes="boot-sim SI-1 (kit-quality, not substrate-gate) / SI-2 (kit-lab daily kept as BUSINESS cron) / SI-3 / SI-4 / SI-5 (verify command); question-rounds P0 R6-Q12 rides the seat C block",
        slots=dict(
            SEAT_NAME="Self Improvement",
            REPOS="menno420/substrate-kit",
            HEARTBEAT_REPO="substrate-kit",
            MISSION=(
                "own the portable workflow kit; make its claims TRUE. Done-when: registry matches the fleet by discovery; "
                "every reachable adopter ≥ v1.12.1; no template ships a dead boot pointer"
            ),
            HARD_RAILS=(
                "⚠ HARD RAILS: (1) PRs #220/#238 = owner-ratification parks — never arm, close, or rebase. (2) Adopter writes = KIT "
                "DISTRIBUTION ONLY (Q-0261.3): never adopter product code, control/, or settings.json/hooks/permission "
                "config (owner-landed, even in a kit release). (3) Never merge your own bench-oracle changes."
            ),
            ORIENTATION_PATH=(
                "CONSTITUTION.md → control/inbox → status.md (no CLAUDE.md — expected; status outranks current-state.md); "
                "verify = python3 -m pytest tests/ -q (no root bootstrap.py at HEAD)"
            ),
            EXPECTED_RED=(
                "the kit-quality check's Session-gate STEP holds born-red cards BY DESIGN (+ two legacy-alias jobs) — "
                "adopters call this substrate-gate; the kit has NO check of that name"
            ),
            ORDER_GRAMMAR="ORDER truth = status.md `done=` line, never inbox `status: new`",
            CRON_STAGGER="0 */2 * * *",
            OLD_TRIGGER_IDS=(
                "the 2-hourly failsafe (heartbeat #252/#253 ids); the 06:00Z kit-lab DAILY = owner BUSINESS cron — KEEP "
                "(kill-switch: docs/operations/lab-loop.md)"
            ),
        ),
        orders="""FIRST WORK ORDERS (verify at boot — expected as of 2026-07-12, or later):
1. REGISTRY TRUTH — fleet-repos.txt blind to ≥3 vendored adopters; "v1.12.1 COMPLETE" is FALSE — make the checker DISCOVER adopters. Done-when: row per adopter; claim retracted.
2. BOOT-POINTER CLASS — AGENT_ORIENTATION.md.tmpl:10,:34 → dead .claude/CLAUDE.md in ≥4 repos. Fix template + target-exists check + boot layer to CONSTITUTION.md. Done-when: no dead pointer ships.
3. UPGRADE WAVE — next release carries orders 1–2; upgrade the laggards (branch claude/* or the enabler never arms). Done-when: every reachable adopter ≥ v1.12.1 by discovery.
4. GATE INTEGRITY — close the added-card advisory loophole + severity-tier DRIFT; verify Q-0254's claim. Done-when: added-card fixture holds red.""",
    ),
    # ------------------------------------------------------------------ superbot
    dict(
        file="superbot-startup.md",
        fixes="boot-sim SB-1 (tiebreak in seat C WALLS) / SB-2 (done via status.md; inbox manager-owned) / SB-3 / SB-4 (F2 verify-first) / SB-5; question-rounds P0 Q-0213 brake + Q-0241 scope",
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
                "superbot: .claude/CLAUDE.md → current-state (no CAPABILITIES.md); superbot-next: BROKEN BOOT — "
                "CONSTITUTION.md → control/status.md → docs/status/README-first.md"
            ),
            EXPECTED_RED=(
                "superbot-next golden-parity WORKFLOW red-by-design — judge only the required `gate` job + six gates; "
                "superbot all-green (born-red HOLD only)"
            ),
            ORDER_GRAMMAR="status.md `orders: done=` is truth; the inbox is manager-owned — never edit it",
            CRON_STAGGER="0 1-23/2 * * *",
            OLD_TRIGGER_IDS="none live expected (wake loop disarmed Jul 11; ~20 spent disabled one-shots)",
        ),
        orders="""FIRST WORK ORDERS (verify at boot — expected as of 2026-07-12, or later):
F1 plugin-hello exists (empty; lock pins it) — mark ORDER 002 done via status.md `orders: done=002` (never inbox-append), drop OWNER-ACTION 2; seeding it = write-permitted for this order. Done-when: asks gone.
F2 VERIFY FIRST — expected discharged: #196/#206 closed, #213/#217 merged, claim gone; remainder → supersede-and-close (Codex phantoms, Q-0120). Done-when: PRs terminal.
F3 Render superbot-next CLAUDE.md from .substrate/claude/ + fix AGENT_ORIENTATION's dead pointer + promote the flip-playbook trap index to docs/. Done-when: at HEAD.
F4 Port loop: next wave slice (expect wave6/inventory-flip), six gates each; port oracle = the LOCAL superbot clone, never MCP. superbot = hub upkeep + stale-pointer fixes (Q-0166).""",
    ),
    # ------------------------------------------------------------------ superbot-world
    dict(
        file="superbot-world-startup.md",
        fixes="boot-sim SW-1 (idle carve-out in seat C) / SW-2 / SW-3 (archival truth-stamp) / SW-4 (per-session authorship) / SW-5 (~1.1k); replay C-8 (games trigger vs armed registry); R6-Q7 claim aging",
        slots=dict(
            SEAT_NAME="SuperBot World",
            REPOS="menno420/superbot-games + superbot-idle + superbot-mineverse (flagship)",
            HEARTBEAT_REPO="superbot-mineverse (games/idle status = ARCHIVES, read-only)",
            MISSION=(
                "one truthful, secured three-game seat. Done-when: #42 merged + #31 dispositioned; idle's ~1.1k-test suite "
                "gates PRs in CI; heartbeats + claims match live"
            ),
            HARD_RAILS=(
                "⚠ #42 BEFORE SECRETS: mineverse PR #42 (login-CSRF, branch security/oauth-csrf-snapshot-validation, green @ "
                "fff0caa or later) merges BEFORE anything secrets-adjacent; the six-OAuth-env-var ask stays SUBORDINATE "
                "meanwhile. ⚠ STALE-HEARTBEAT TRAP: heartbeats describe an ARCHIVED world — VERIFY AT HEAD before trusting "
                "ANY status claim; a claim with no PR yet is LIVE — age it. Mineverse HEAD: ZERO runs as of 2026-07-12. "
                "⚠ GREEN ≠ TESTED (idle): no pytest in CI — run pytest -q before any idle merge until W2."
            ),
            ORIENTATION_PATH=(
                "docs/current-state.md per repo (games/idle: no CLAUDE.md — expected; mineverse's lies — W1 re-renders it)"
            ),
            EXPECTED_RED=(
                "substrate-gate born-red HOLD (all 3); genuinely green: games tests.yml · idle theme-gate · mineverse schema-gate"
            ),
            ORDER_GRAMMAR="headers may lag DONE-flips",
            CRON_STAGGER="15 1-23/2 * * *",
            OLD_TRIGGER_IDS=(
                "games trig_019ZgWyL78Rx1sr6LhvL8NE3 (15 */2 — WAS armed per ORDER-015, maybe auto-disabled; never assume "
                "\"never armed\") + idle trig_01TWKGFW8RUsMvxUMt2ndzqA (expected deleted) — verify each"
            ),
        ),
        orders="""FIRST WORK ORDERS (verify at boot — expected as of 2026-07-12, or later):
W1 mineverse — land PR #42: a DIFFERENT session authored it (per-SESSION authorship — your genuine review = the non-author path); ONE attempt; denial → park, ⚑ owner TOP. Done-when: #42 in main, diff shows payload. Then #31; re-render CLAUDE.md.
W2 idle — add CI running the pytest suite on PR + push; ⚑ owner to mark required. Done-when: green on a real PR.
W3 games — truth-stamp the heartbeat ONCE (archival correction, NOT resumption: its 5 owner-merge asks are DONE); delete the 5 stale claims, evidence cited. Done-when: status + claims match live.""",
    ),
    # ------------------------------------------------------------------ game-lab
    dict(
        file="game-lab-startup.md",
        fixes="boot-sim GL-1 (R22 via search_repositories + proxy-wall carve-out, also P0 R6-Q4) / GL-2 (probe-PR fallback) / GL-3 (both PRs); replay C-9 (owns the retro-games delete + gba/pml hourly wakes)",
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
            ORIENTATION_PATH="README + CONSTITUTION.md + current-state + CAPABILITIES per repo (no CLAUDE.md — expected)",
            EXPECTED_RED="substrate-gate born-red card HOLD; genuinely green: rom-builds per track",
            ORDER_GRAMMAR="status stamps = snapshots, not order lists",
            CRON_STAGGER="15 */2 * * *",
            OLD_TRIGGER_IDS=(
                "gba/pml hourly wakes trig_0137SkvhXEJvwepX8aVNkcSn + trig_01BTJjkMVMKtWPjuYe7643Hi + retro-games "
                "trig_01Y99uDKNtKTz2EtRYPWZkGY (YOURS — fm defers it) — this lane's only"
            ),
        ),
        orders="""FIRST WORK ORDERS (verify at boot — expected as of 2026-07-12, or later):
W1 card convention (per-track prefixes; each fired session commits a card + 📊 Model: line) + pml .gitignore (*.gba, *.sav, baserom*). Done-when: BOTH PRs merged (one per repo).
W2 read the LIVE required-check sets (probe PR check-runs if the ruleset API is gated); refresh ⚑ clicks (gba +"NDS ROM build", pml +"ROM builds"). Done-when: ⚑ live.
W3 Track A toward Lumen Drift Release (playtests + B pick owner-gated ⚑). Done-when: one headless-proven slice merged.""",
    ),
    # ------------------------------------------------------------------ websites
    dict(
        file="websites-startup.md",
        fixes="boot-sim WS-1 (cron NEVER fired) / WS-2 (supersedes STAYS-ARMED) / WS-3 (un-park owner-authorized by this paste) / WS-4 (id-less wake procedure); I-63 header defect fixed (TOOL FACTS rides the core)",
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
                "-m pytest tests/ botsite/tests dashboard/tests review/tests -q` + `bootstrap.py check --strict` — NOT "
                "the stale CLAUDE.md snippet (order 3). (3) OWNER ASKS: six-field ⚑ OWNER-ACTION (docs/owner/OWNER-ACTIONS.md) "
                "+ heartbeat mirror; re-verify every wake. (4) Status reads CLOSING/PARKED — THIS paste un-parks it."
            ),
            ORIENTATION_PATH=".claude/CLAUDE.md → docs/current-state.md → docs/CAPABILITIES.md (full triple exists here)",
            EXPECTED_RED="the born-red card HOLD only; `quality` green expected on main",
            ORDER_GRAMMAR="ORDER truth = status.md `done=`, not inbox `status:`",
            CRON_STAGGER="45 */2 * * *",
            OLD_TRIGGER_IDS=(
                "the v1-era 4-hourly wake (ORDER-008 text; no id slot — find by name+prompt in the audit, record the id) + "
                "any prior failsafe; SUPERSEDES status.md \"STAYS ARMED\""
            ),
        ),
        orders="""FIRST WORK ORDERS (verify at boot — expected as of 2026-07-12, or later):
1. RECONCILE — status.md + OWNER-ACTIONS.md vs live GitHub: clear satisfied asks (#141 expected satisfied), fix the prune list (~14 vs 7 real), stamp the sha. Done-when: zero contradicted claims.
2. CSRF FIX — app/owner.py POST refresh/rerun-ci ride Basic auth alone: CSRF token or Origin check + rate-limit, with tests. Done-when: merged green.
3. RE-RENDER CLAUDE.md via the kit: four services + four-suite verify. Done-when: doc matches the tree.
4. REVIEW-BAKE truth — the ONLY bake run (29167034060) was a MANUAL dispatch failing on the Actions-can't-create-PRs wall; the 05:23Z cron NEVER fired as of 2026-07-12 — verify BY EVENT TYPE before any ⚑ (wall real — owner toggle; stats stranded on bake/*). Done-when: the ask matches the run history.""",
    ),
    # ------------------------------------------------------------------ venture-lab
    dict(
        file="venture-lab-startup.md",
        fixes="boot-sim VL-1 (disposition grammar; #58 CLOSED) / VL-2 (enabler proven #59/#60) / VL-3 (rebind = create-new→verify→delete-old) / VL-4 (#65) / VL-5 / VL-6 (trading heartbeat stale) / VL-7 (via A); replay C-2 resolution in seat C",
        slots=dict(
            SEAT_NAME="Venture Lab",
            REPOS="menno420/venture-lab + menno420/trading-strategy",
            HEARTBEAT_REPO="EACH repo (venture prose; trading key:val)",
            MISSION=(
                "sellables reach owner-click-ready; trading paper lane intact + graded. Done-when: no stranded green PRs; "
                "07-17 grading secured to THIS session; heartbeats verified"
            ),
            HARD_RAILS=(
                "⚠ HARD RAILS: (1) MERGE PATH: venture — READY on claude/*, NOTHING merge-related (the enabler lands green, "
                "proven #59/#60); never self-arm/self-merge; parked = owner-merge. trading — MCP squash = recorded "
                "practice: ONE attempt, first denial retires it. (2) RESEARCH-ONLY (trading): no "
                "broker/order/exchange-write code or live API config, EVER; holdout SPENT; paper lane = load_paper_ohlcv "
                "only; promotion owner-gated; never claim a money path works without EXECUTING it (D1). (3) Owner-⚑s "
                "verbatim at queue top (#51 HOT — owner-only)."
            ),
            ORIENTATION_PATH="current-state.md + docs/conventions.md per repo (no CLAUDE.md in either — expected)",
            EXPECTED_RED=(
                "venture: kit-tests + substrate-gate (born-red HOLD); trading: tests only"
            ),
            ORDER_GRAMMAR="ORDERs repo-first — qualify numbers per repo",
            CRON_STAGGER="45 1-23/2 * * *",
            OLD_TRIGGER_IDS=(
                "trig_01X1dw1L1Udgt8atzzNWEJic + trig_017o6azZTd9pzcaSthEncT5q; grading trig_015aNMg5ncoSE2Roe4MKjQnr = "
                "BUSINESS cron — rebound per F2, never just deleted"
            ),
        ),
        orders="""FIRST WORK ORDERS (verify at boot — expected as of 2026-07-12, or later):
F1 DISPOSITION every open PR vs its close/park record (2026-07-12: #51 HOT owner-only · #57 parked owner-merge · #58 CLOSED-superseded, never re-land · #64 non-author review-merge · #65 per doctrine). Done-when: each merged, parked-⚑, or closed.
F2 SECURE THE 07-17 GRADING PASS (⚑ g: session triggers die at archive): NEW weekly trigger (0 9 * * 5, grade_paper.py prompt) bound HERE → verify → delete trig_015aNMg5… (binding not updatable); 07-17 near, no executor → run grade_paper.py NOW. Done-when: new id bound here; ids in trading status.
F3 RE-STAMP what contradicts live GitHub — trading's heartbeat is the stale one; pay lane-owed kit bumps. Done-when: stamps match git log.""",
    ),
    # ------------------------------------------------------------------ ideas-lab
    dict(
        file="ideas-lab-startup.md",
        fixes="boot-sim IL-1 (gate GREEN since #221) / IL-2 (verify-the-handoff-closed) / IL-3 (prior coordinator LIVE; scoped deletion) / IL-4 / IL-5 / IL-6; question-rounds P0 T1 ('delete stragglers' retired)",
        slots=dict(
            SEAT_NAME="Ideas Lab",
            REPOS="menno420/idea-engine + menno420/sim-lab",
            HEARTBEAT_REPO="idea-engine (plus sim-lab's, as the merged seat)",
            MISSION=(
                "keep the generate→verify loop alive: PROPOSALs (idea-engine) → VERDICTs (sim-lab) → manager routes "
                "(Q-0264); done-when: preflight green; no orphaned PROPOSAL; routines armed + verified"
            ),
            HARD_RAILS=(
                "⚠ HARD RAILS: (1) GATE: preflight.py GREEN since PR #221/329547d (verify at boot; expected green "
                "2026-07-12) — substrate-gate red is now REAL except the born-red HOLD; a roster reshape (fm #88/#89/#91, "
                "parked) redding check_sections → fix forward-tolerant. (2) MANAGER FAN-IN: sim-lab verdicts go to the "
                "fleet manager (Q-0264); never short-circuit bilaterally."
            ),
            ORIENTATION_PATH=(
                "idea-engine: control/status.md is truth (current-state is boilerplate); sim-lab: CONSTITUTION.md + "
                "PLATFORM-LIMITS.md (no .claude/ — expected)"
            ),
            EXPECTED_RED="born-red HOLD only — preflight/substrate-gate red is REAL now (post-#221)",
            ORDER_GRAMMAR="headers may lag DONE-flips",
            CRON_STAGGER="30 1-23/2 * * *",
            OLD_TRIGGER_IDS=(
                "the prior coordinator may be LIVE (status ACTIVE; failsafe trig_01T83UuVthszGBcENYwrTrm7 at 0 */2 squats "
                "the Self Improvement slot): confirm that chat is archived BEFORE deleting; THIS lane's ids only — never \"stragglers\""
            ),
        ),
        orders="""FIRST WORK ORDERS (verify at boot — expected as of 2026-07-12, or later):
1. VERIFY THE HANDOFF CLOSED — PROPOSAL 010 expected already verdicted (VERDICT 012 + fan-in PR #227); only if truly unverdicted, pull as INTAKE (verbatim number + stamp + pinned sha) → sim → verdict via fan-in; NEVER append a duplicate VERDICT. Done-when: chain verified closed, or the missing verdict landed.
2. SIM-LAB LANDING PATH — no enabler; own-PR REST merges violate doctrine: stand up a GITHUB_TOKEN merge-on-green workflow; meanwhile park READY+green. Done-when: a PR lands without an agent merge call.
3. STALE-STATE SWEEP — verify every heartbeat ⚑/ask row vs live GitHub; re-stamp ONLY what contradicts (both expected fresh as of 2026-07-12). Done-when: zero contradicted rows.""",
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
