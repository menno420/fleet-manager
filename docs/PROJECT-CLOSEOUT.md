# fleet-manager — project closeout (fleet master document)

> **Status:** `audit`
>
> Written 2026-07-21 at the close of the autonomous session period (sessions
> became read-only 2026-07-22T00:00Z). This is the fleet-manager (hub) seat's
> final handover — and because this repo is the fleet's records custodian, it
> doubles as the **fleet-level master closeout**: the one document that maps
> every repo, every record surface, and every open thread. Written for two
> readers who know nothing about these sessions: the owner, and a fresh
> future Claude session. Facts marked "verified live" were checked against
> GitHub/the committed snapshot at write time (2026-07-21 ~17:0xZ), not from
> memory.

---

## 1 · What this project is & what was accomplished

### The role

fleet-manager is the **hub of a ~19-repo agent fleet**. During the autonomous
session period, each repo ("lane") had its own agent seat doing product work
— a Discord bot, four websites, a GBA game, research engines, a portable
project-bootstrap kit — while this repo's coordinator seat did the
**oversight**: it kept the canonical fleet records (who is alive, what waits
on the owner, what happened), watched every lane's wake-up scheduling for
silent failures, landed or routed stray PRs anywhere in the fleet, and
consolidated everything the owner ever needed to see into a small set of
documents in this repo.

### The record surfaces (the custodian mission)

- **`docs/roster.md`** — the generated fleet snapshot: every lane, its
  heartbeat age, verdict (FRESH/STALE/DARK), kit version, wake triggers, and
  trigger health, regenerated every ~2h by GitHub Actions
  (`scripts/gen_roster.py` + `.github/workflows/roster-regen.yml`). 145
  generations by close. Companion: `docs/evidence-index.md` (per-lane
  evidence pins) and `registry/lanes.json`.
- **`docs/owner-queue.md`** — the single deduplicated list of things only the
  owner can do, each item self-contained with paste-ready steps (84 stable
  `OQ-` ids through its history; drift probed by `scripts/check_owner_queue.py`).
- **`docs/fleet-triage.md`** — the dated event log: every oversight cycle,
  incident, escalation, and disposition, with verbatim evidence.
- **`docs/prompts/v3/`** — the seat prompt registry (startup / continue /
  session-ender / final-closer): the paste artifacts that founded and closed
  every seat.
- **`control/`** — the historical ORDER-relay bus (inbox/outbox/status/claims);
  `control/status.md` is this seat's heartbeat.

### The oversight tooling suite (all in `scripts/`, stdlib-only)

Built across the seat's run, mostly in the final four days (~35 PRs, #332
boot through #425), each answering a real incident:

- **Trigger snapshots + health invariants** — `assemble_triggers_snapshot.py`
  (paged `list_triggers` export → `telemetry/triggers-snapshot.json`) +
  `check_trigger_health.py` with invariants **I1–I8** (wedged crons, dropped
  one-shots, dead chains, manager failsafe, snapshot freshness, tick
  pile-up, duplicate crons). Born from the 2026-07-12 silent scheduler
  degradation (9 dropped one-shots, two seats dark ~6h, nothing watching).
  Spec: `docs/trigger-health-spec.md`; seat-provenance-aware I8 remedy PR #353.
- **Routine-state proof pair** — `verify_routine_state.py` (PR #335; diffs
  the heartbeat's machine-readable routine-claims fence against any export;
  volatile-field drift check PR #365) + `emit_routine_claims.py` (PR #357;
  write-side fence updater, round-trip-validated). The fence itself: PR #339.
- **Lane-liveness ledger** — `check_lane_liveness.py` (PR #350): scores every
  lane LIVE/QUIET/STALLED from commits vs wake fires; **WAKING-IDLE**
  detection (fires with zero landed output, PR #379); append-only ledger +
  transition diff (PR #386); **IDLE-DECLARED** (a declared, dated idle is not
  a stall — PR #400, from the `OQ-SI-CHAIN-DEAD` false escalation).
- **Regen-skip detector** — in `check_roster_freshness.py` (PR #352): names
  the exact missed cron window when a roster regen drops (the 3-night 00:40Z
  drop class that PR #344's odd-hours second cron fixed).
- **Routine-claims fence + emitter + verifier** — see the proof pair above;
  together they make every heartbeat's scheduling claims machine-checkable.
- **Label hygiene** — `check_label_hygiene.py` (PR #370): fleet-wide
  hold-label detector; its first ground-truth run (19/19 repos, 0 hold-class
  definitions) *was* the verification that retired `OQ-LABEL-DEFS-DELETE`.
- **R30 pre-merge verifier** — `r30_merge_check.py` (PR #372): mechanizes the
  3-point workflow-PR check (Codex-clean at exact head SHA · all checks
  green · whole-file secret+egress scan), PASS/REVIEW/STOP, fail-safe.
- **Idea-backlog harvester** — `gen_idea_backlog.py` (PR #377): harvests every
  session card's 💡 idea across the repo into
  `docs/planning/idea-backlog.md` with groomed-status detection.
- **Advisory drift checkers (S3/S5/S9 + grammar)** —
  `check_fleet_triage_staleness.py` (#299), `check_docs_links.py` (#293),
  `check_capabilities_wall_age.py` (#296), `check_capabilities_grammar.py`
  (#358); plus `tools/check_no_false_walls.py` (#316) — the CI linter that
  stops any doc from recording an agent-capability wall as permanent.

### The landing infrastructure

- **`merge-on-green.yml`** — server-side backstop lander (verify-then-merge)
  so a green PR never waits on anyone.
- **`roster-regen.yml`** — headless roster regeneration on **dual crons**
  (`40 */2 * * *` + `40 1-23/2 * * *`, PR #344 after the drop incidents —
  net hourly coverage; delivery proof gen #101).
- **`substrate-gate.yml` / `roster-freshness.yml`** — the kit merge gate
  (session-card discipline) and the stale-roster PR gate.

### Doctrine milestones (the working rules that made it run)

- **R29 (2026-07-15)** — the owner never reviews PRs: feature PRs flip ready
  and land on green; review is CI + cross-agent, never a human queue.
- **R30 (2026-07-19, PRs #367/#368/#372)** — even workflow-touching PRs are
  agent-merged after the 3-point head-SHA check; the owner's last standing
  merge class was retired.
- **Nothing-stuck directive (owner, 2026-07-19 ~08:00Z)** — executed same
  morning (PR #351): product-forge #29 merged by the hub, websites #434
  label-stripped + merged, a 9-repo hold-label sweep; the label
  *definitions* retirement was verified by the hygiene checker the same day.
- **Kit v1.20.x wave shepherding** — the fleet-wide substrate-kit
  v1.17.0→v1.20.x upgrade: 7 adopter legs tracked, nudged, fixed and landed
  by the hub to **5/7 merged** (idea-engine #740 · superbot-games #183 ·
  superbot-mineverse #138 · websites #452 · venture-lab #282), remnants
  trading-strategy #160 + superbot-next #602 (§3). The hub also drove the
  v1.20.2 checker-fix release into both remnants (re-vendored same day).
- **Prompt registry v3 → v3.8** — the per-seat startup/continue/ender prompt
  set, closed out by `docs/prompts/v3/final-closer.md` (PR #425), the
  artifact this very document follows.
- Earlier majors, still load-bearing: the centralization plan P1→P3 (PRs
  #81–#86: snapshot → headless regen → generated queue feed → evidence
  index), the project-recreation runbook (#271), the fleet-wide PR-landing
  audit (#265), the capabilities ledger correction ("agents can merge",
  #308/#309), and the fleet boot file for fresh hub sessions (#312).

---

## 2 · Current true state — verified live 2026-07-21 ~17:0xZ

- **Roster:** generation **#145**, generated-at 2026-07-21T16:58Z by the
  Actions cron — fresh at write time. Verdicts: 3 FRESH (websites,
  idea-engine, fleet-manager) · 4 STALE · 12 DARK/archived lanes · 1 PRIVATE
  (pokemon-mod-lab, auth wall — honest UNREADABLE, not dead). Note: most
  DARK lanes are *closed by design* (wound-down generations), not failures.
- **Trigger registry** (committed snapshot, captured 2026-07-21T16:00:18Z,
  26 pages to exhaustion): **2577 records, 17 enabled** — 10 standing crons +
  1 poke-only + 6 one-shots. `check_trigger_health.py`: **PASS, 8/9 green, 1
  WARN** — the standing I8 duplicate "SuperBot World failsafe wake" pair
  (§3). Every seat's closer wipes its own triggers at program end, so the
  enabled count should fall toward zero; this seat's own wipe result lands
  in `control/status.md` (Phase 2 of this close).
- **Open PRs fleet-wide** (live GitHub search, 17:07Z): **15** —
  fleet-manager #427 (this closeout, born-red by design) · trading-strategy
  #160 + superbot-next #602 (kit-wave remnants, both `blocked`, §3) ·
  superbot-next #576 (docs) · substrate-kit #552 (`do-not-automerge` BY
  DESIGN — owner bench pin) · superbot ×7 dependabot · websites #465 (bake) ·
  sim-lab #344 (proposal artifact).
- **Kit wave:** 5/7 merged (verified in §1). **#160** head `f1c5284`
  (v1.20.2 re-vendored), red = 3 resident doc lines
  (`docs/current-state.md:389` · `CONSTITUTION.md:166` ·
  `docs/review-queue.md:8`). **#602** head `2755fdb` (v1.20.2 re-vendored),
  red = 2 resident lines (`docs/current-state.md:101` + `:118`); all four
  red checks trace to that one `check --strict` step — no product failure
  (3647 tests pass).
- **Sibling closeouts:** raw-fetch probe of
  `docs/PROJECT-CLOSEOUT.md` across all 18 sibling repos at ~17:06Z — **none
  landed yet**; every seat writes one **today at the same path**
  (`docs/PROJECT-CLOSEOUT.md` in each repo) per the same final-closer
  prompt. (pokemon-mod-lab is private, so the anonymous probe cannot see it
  either way.) Check the links in §4 again after today.
- **This repo:** `main` at `4347658` (gen-#145 regen) at branch time;
  `bootstrap.py check --strict` green on the payload except the deliberate
  born-red session card (flips at Phase 2).

---

## 3 · Continuation — open threads, priority-ordered

Each item is self-contained: a fresh session (or the owner) can resume from
this section alone.

1. **trading-strategy #160 — kit upgrade, 3 doc lines from green.**
   The PR (head `f1c5284`, v1.20.2) is blocked only by 3 false-wall findings
   in *resident-owned* docs: `docs/current-state.md:389`,
   `CONSTITUTION.md:166`, `docs/review-queue.md:8`. Two are deliberate
   adopter governance (align to fleet doctrine or allowlist as
   `accepted_risk` in `.substrate/check-exceptions.yml`), one is a live queue
   note to reword/date-stamp. A hub-prepared fixed working tree existed at
   `/home/user/trading-strategy` (container-local; gone when the container
   is); the fix content is trivial to re-derive — the 3 target lines are
   unchanged on the branch. **Resume:** clone the repo, check out
   `claude/kit-upgrade-v1.20.1`, fix/allowlist the 3 lines (reason-carrying
   entries), push, merge on green.
2. **superbot-next #602 — kit upgrade, 2 lines from green (lane-owned).**
   Head `2755fdb` (v1.20.2). Fix is entirely `docs/current-state.md:101`
   (date-stamp/repudiate the momentary-refusal record in place, or
   allowlist) and `:118` (collapse the two-line quote to one line). That
   greens all four red checks at once. **Resume:** same recipe as #160, in
   superbot-next, per the PR body's STEP-2 analysis.
3. **`OQ-SBW-DUP-FAILSAFE` — duplicate "SuperBot World failsafe wake" crons.**
   Two enabled crons, same name + schedule (`15 1-23/2 * * *`):
   `trig_01XJJ88pQaQFRSpVAviCfAZe` (older) + `trig_01DbcKVWxn6RJPhfyRkgTg6m`
   (newer, live-seat-bound) — 12 recorded escalation cycles of double-fires.
   **Likely MOOT at close:** the SBW seat's own final-closer wipes both.
   **Check:** run `list_triggers` (paginate to exhaustion) after 2026-07-22;
   if either id survives, delete it — post-close, *any* surviving trigger is
   dead weight, so the old keep-the-newer nuance no longer applies.
4. **`OQ-WEBSITES-LABEL-MACHINERY` — remove the websites label re-creator.**
   `\.github/workflows/host-automerge-extras.yml` on websites main still
   auto-re-creates + auto-applies the retired `do-not-automerge` label on
   workflow-touching `claude/*` PRs. The edit dispatch wants the owner's live
   venue (two 2026-07-19 auto-mode denials recorded — transient venue state,
   not a wall); the resulting PR then lands normally.
   Tripwire: `python3 scripts/check_label_hygiene.py`.
5. **Post-close apparatus decision (was `OQ-FM-APPARATUS-SIZING`).**
   GitHub Actions keep running after the sessions end: `roster-regen.yml`
   fires ~hourly (dual crons) forever, regenerating the roster from
   heartbeats no seat updates anymore. Harmless, but noisy. Recommended when
   convenient: reduce to daily (`40 6 * * *`, keep `workflow_dispatch`) or
   disable the workflow; keep `merge-on-green.yml` + `substrate-gate.yml`.
   Full per-workflow verdicts: `docs/owner-queue.md` §(D).
6. **The future-work well.** `docs/planning/idea-backlog.md` (generated,
   46 harvested idea blocks with groom status) + `docs/planning/2026-07-19-next-slices.md`
   (ranked executable slices) + `docs/owner-queue.md` §§(B)–(G) (owner-only
   asks: secrets, settings, product publishes, standing decisions —
   each with paste-ready steps). Any fresh session looking for work starts
   in these three files.

---

## 4 · Owner walkthrough — what you have, in plain language

Everything below is a committed document or a live artifact; the sessions
that wrote them are gone, but nothing here depends on them.

### The three fleet records (all in this repo)

- **[The roster](roster.md)** — the fleet map. One row per repo/seat: when it
  last reported (heartbeat), whether it was active, what woke it, and a link
  to its evidence. It was regenerated every ~2 hours by GitHub Actions (and
  still is, until you slow that down — §3 item 5). Read it to see the whole
  fleet at a glance; after close, treat it as a historical snapshot.
- **[The owner queue](owner-queue.md)** — your to-do inbox. Only things that
  genuinely need *you* (secrets, account clicks, decisions). Every item says
  WHAT / WHERE (exact URL) / HOW (paste-ready steps) / WHY / how to VERIFY
  it worked — you never have to derive anything. Resolved items move down
  the file with the evidence that resolved them.
- **[The fleet-triage log](fleet-triage.md)** — the event log. Dated entries
  for every oversight cycle: what was checked, what broke, what was done
  about it, with verbatim evidence. When you wonder "what actually happened
  on the night of X", this is the file.

### The prompt registry — `docs/prompts/v3/`

The paste artifacts that ran the fleet. You paste one into a project chat;
it tells the session who it is and what to do:

- **[universal-startup.md](prompts/v3/universal-startup.md)** — founds a seat
  (paste once when creating a new project session). Per-seat variants:
  `prompts/v3/per-project/`.
- **[universal-continue.md](prompts/v3/universal-continue.md)** — resumes any
  seat mid-run ("pick up where the records say you left off").
- **[session-ender.md](prompts/v3/session-ender.md)** — closes a session
  cleanly (heartbeat + routine disposition).
- **[final-closer.md](prompts/v3/final-closer.md)** — the program-end close
  every seat ran today (closeout doc + records true-up + routine wipe).
  Post-close, **universal-continue** is the one to paste if you ever restart
  a seat in a fresh session.

### Tools an outside/fresh session can run (one line each)

From a clone of this repo (`python3 scripts/<name>` unless noted):

- `gen_roster.py` — rebuild the roster from live heartbeats ("is anything
  alive?").
- `check_trigger_health.py` — scan a triggers export for scheduling failures
  ("are any wake-ups broken/duplicated?").
- `assemble_triggers_snapshot.py` — turn paged `list_triggers` output into
  the committed snapshot the health check reads.
- `verify_routine_state.py` / `emit_routine_claims.py` — prove/update what
  the heartbeat *claims* about its scheduling vs what the registry *shows*.
- `check_lane_liveness.py` — per-lane LIVE/QUIET/STALLED verdicts ("who is
  actually landing work?").
- `check_owner_queue.py` — flag owner-queue drift (items citing merged/closed
  PRs).
- `check_roster_freshness.py` — is the roster stale; which regen window was
  missed.
- `check_label_hygiene.py` — fleet-wide scan for hold-labels that block
  merges.
- `check_docs_links.py` / `check_fleet_triage_staleness.py` /
  `check_capabilities_wall_age.py` / `check_capabilities_grammar.py` —
  advisory doc-drift sweeps (dead links · stale triage rows · aged
  capability walls · ledger format).
- `r30_merge_check.py --repo owner/name --pr N` — the 3-point safety check
  before merging a workflow-touching PR.
- `gen_idea_backlog.py` — re-harvest every session card's ideas into the
  backlog table.
- In superbot: `python3.10 scripts/fleet_status.py` — the one-command
  fleet heartbeat table from the hub side.

### The fleet — every repo, its closeout, its artifacts

Each repo's own closeout lands **today** at `docs/PROJECT-CLOSEOUT.md`
(none were up yet at this document's write time — follow
`https://github.com/menno420/<repo>/blob/main/docs/PROJECT-CLOSEOUT.md`).
Live artifacts listed are the ones this repo's records cite; each repo's own
closeout is the authority on its products.

| Repo | What it is | Known live artifacts (as recorded here) |
|---|---|---|
| [superbot](https://github.com/menno420/superbot) | The live Discord bot + the original workflow lab | Production bot on Railway (merge = deploy) |
| [superbot-next](https://github.com/menno420/superbot-next) | The bot's ground-up rebuild | — |
| [websites](https://github.com/menno420/websites) | Four server-rendered sites (control-plane · botsite · dashboard · review) | [control-plane](https://control-plane-production-abb0.up.railway.app) · [review](https://review-production-f027.up.railway.app) (Railway project `reliable-grace`) |
| [substrate-kit](https://github.com/menno420/substrate-kit) | The portable project-bootstrap kit every repo vendors | Releases through v1.20.2 |
| [superbot-mineverse](https://github.com/menno420/superbot-mineverse) | Mining-game web companion | [web app](https://web-production-97636.up.railway.app) |
| [superbot-games](https://github.com/menno420/superbot-games) / [superbot-idle](https://github.com/menno420/superbot-idle) | Bot game modes (Seat A / Seat B) | Ship inside the bot |
| [gba-homebrew](https://github.com/menno420/gba-homebrew) | Real GBA games | [Playable web builds](https://menno420.github.io/gba-homebrew/) · Lumen Drift ROM (Release pending — `OQ-GBA-LUMEN-RELEASE`) |
| [pokemon-mod-lab](https://github.com/menno420/pokemon-mod-lab) | ROM-hack lab (private) | ROM builds via Actions |
| [trading-strategy](https://github.com/menno420/trading-strategy) | Trading-strategy research (program terminal: 0/13 cleared significance — an honest null) | Final holdout report on main |
| [venture-lab](https://github.com/menno420/venture-lab) | Sellable-product experiments | 3 products publish-ready (owner clicks in queue §C) |
| [idea-engine](https://github.com/menno420/idea-engine) / [sim-lab](https://github.com/menno420/sim-lab) | Idea generation ↔ verification pair | Verdict ledgers (V237+/VERDICT 274) in-repo |
| [product-forge](https://github.com/menno420/product-forge) | Android/product experiments (archived-ready) | — |
| [codetool-lab-fable5](https://github.com/menno420/codetool-lab-fable5) / [-opus4.8](https://github.com/menno420/codetool-lab-opus4.8) / [-sonnet5](https://github.com/menno420/codetool-lab-sonnet5) | Same-task model comparison labs (wound down) | envdrift · mdverify (opus4.8 releases LIVE) · cfgdiff |
| [curious-research](https://github.com/menno420/curious-research) | Gift repo — maker research companion | Animated HTML guides in `guides/` |
| [fleet-manager](https://github.com/menno420/fleet-manager) | This repo — the hub | The records + tooling this document describes |

### Owner checklist (quickest first)

1. **Post-close trigger sweep (~2 min).** After 2026-07-22, run
   `list_triggers` in the hub chat, paginated to exhaustion. Expect zero
   enabled seat triggers (every closer wipes its own). Delete any survivor —
   they can only wake dead sessions. This also settles the old
   `OQ-SBW-DUP-FAILSAFE` pair for free.
2. **Slow or stop `roster-regen.yml` (~2 min).** It keeps firing ~hourly on
   GitHub's dime with no seats left to report. Repo → Actions →
   roster-regen → disable, or edit the two cron lines to `40 6 * * *`.
3. **Websites label machinery (~10 min, your venue).** Have a session remove
   the label re-creation block from websites
   `host-automerge-extras.yml` (§3 item 4) — the dispatch just needs you
   present.
4. **When you want the products:** the venture-lab publish clicks, websites
   Postgres/PAT, GBA release, and the other standing asks are all in
   [owner-queue.md](owner-queue.md) §§(B)–(D), each with paste-ready steps.
   None is urgent; none expires.

---

## 5 · Working this repo with a fresh session

- **Boot route (in order):** `CONSTITUTION.md` (the working agreement) →
  `control/status.md` (the seat's last heartbeat — first line says SEAT
  CLOSED) → `docs/roster.md` + `docs/owner-queue.md` + `docs/playbook.md`
  (fleet map · owner asks · the R1…R30 operating rules). Then this document.
- **Verify before any push:** `python3 bootstrap.py check --strict` — the
  kit gate that CI (`substrate-gate.yml`) also runs. Green locally = green
  in CI.
- **Landing mechanics:** claim your lane (`python3 bootstrap.py claim <slug>
  --scope "..."`), first commit = a **born-red session card**
  (`.sessions/<date>-<slug>.md` with `> **Status:** \`in-progress\``), open
  the PR READY immediately, do the work, write the card's close-out
  (Status badge · 💡 idea · previous-session review · 📊 Model line), **flip
  the badge to `complete` as the deliberate last push** → the gate goes
  green → merge it yourself or let `merge-on-green.yml` land it. Delete your
  claim at close (`bootstrap claim <slug> --delete`).
- **Gotchas a newcomer must know:**
  1. **Docs gate:** every new `docs/*.md` needs a `> **Status:** \`<token>\``
     badge (taxonomy in `bootstrap.py`) *and* a link from a read-path doc
     (`docs/current-state.md` / `AGENT_ORIENTATION.md` reachability roots)
     — an unlinked doc fails the gate as an orphan.
  2. **Guard-fires:** `check --strict` appends telemetry to
     `.substrate/guard-fires.jsonl` — in this repo you **commit** that delta
     (do-not-revert), unlike kit-distribution PRs in adopter repos.
  3. **Generated files:** never hand-edit `docs/roster.md`,
     `docs/evidence-index.md`, `docs/owner-queue-candidates.md`,
     `docs/planning/idea-backlog.md`, `docs/seat-digest.md`,
     `registry/lanes.json`, `telemetry/triggers-snapshot.json` — regenerate
     with their `gen_*`/`assemble_*` script.
  4. **False-wall discipline:** never write "agents cannot X" into any doc.
     A refusal is a transient, venue-specific event: attempt once, record
     the exact error + date, route around it. CI
     (`tools/check_no_false_walls.py`) reds a PR that documents a
     capability wall — and the phrasing rules are strict enough that even
     *quoting* a wall claim can trip it (allowlist via
     `.substrate/check-exceptions.yml` with a reason, as PR #424 did).
