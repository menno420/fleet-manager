# Problem census — core repos (2026-07-12)

**Date:** 2026-07-12 (overnight program of 2026-07-11).
**Purpose:** input for regression-proof startup prompts and custom instructions
per fleet Project — what each repo's sessions must know at minute 0, what lies
to them today, and what no prompt can fix (owner/tooling asks).
**Method:** 6 parallel read-only census agents, one per repo, each producing
STATE / KNOWN PROBLEMS / UNKNOWN PROBLEMS / EXPECTATIONS / PROMPT IMPLICATIONS
with file@sha / PR# / run-id citations; this document is the assembly.
**Scope:** superbot, superbot-next, websites, substrate-kit, fleet-manager,
product-forge. Parked PRs #88/#89/#91/#92 (fleet-manager restructure stack +
settings port) untouched throughout.

---

## Per-repo verdicts

| Repo | Verdict | Biggest problem |
|---|---|---|
| superbot | FRESH — hub healthy, zero open PRs, CI all green | Heartbeat asserts superseded facts without per-field `verified-against:` stamps; 79 KB orientation payload taxing every session |
| superbot-next | FRESH — active minutes before census, but wake loop disarmed | No `.claude/CLAUDE.md` at HEAD — a fresh session auto-loads *nothing*; STALE OWNER-ACTION 2 asks the owner to create a repo that has existed since 2026-07-10 |
| websites | STALE (mildly, deliberately parked) | review-bake fails every day at 05:23Z on the "Actions is not permitted to create PRs" wall; baked stats stranded on `bake/*` branches forever |
| substrate-kit | FRESH — heartbeat and tree agree to the minute | Adopter registry blind to ≥3 (likely 5) vendored adopters; "v1.12.1 distribution COMPLETE" is false fleet-wide, leaving the substrate-gate false-green bug live downstream |
| fleet-manager | FRESH-but-seat-in-handover | Roster-freshness time-bomb: gen #10 stuck on `bot/roster-regen` (Actions-PR wall) → 4h blocking bar reds every `claude/*` PR from ~2026-07-12T00:25Z and no agent can clear it |
| product-forge | FRESH but ARCHIVED/going-DARK | Working agreement doesn't exist at its advertised path (`.claude/CLAUDE.md` dead pointer, `.substrate/` copy unrendered); dark inbox — no trigger wakes the lane while the manager can still write ORDERs into it |

---

## Top 10 fleet-wide problems by regression risk

Ranked by how likely each is to make a *future session regress* — act on a lie,
re-break a fix, or stall on a wall it can't see.

**1. Missing / unrendered CLAUDE.md boot layer (4 of 6 repos + kit template root cause).**
fleet-manager has no CLAUDE.md and no `.claude/` on main at all (fm census §3.3;
the permission-rules port is parked in #92); superbot-next has no `.claude/` at
HEAD `249ecaa` — only `.substrate/claude/CLAUDE.md`, installed only if bootstrap
runs, and its identity slot reads "superbot-next is built in Python." (sn census
§3); product-forge's only copy (`.substrate/claude/CLAUDE.md@4fdfa8a`) still
carries the "⚠️ UNRENDERED SLOTS" banner with `${primary_language}` etc. unfilled
(pf census U1). Root cause is kit-side: `src/engine/templates/
AGENT_ORIENTATION.md.tmpl:10,:34` points step 1 at `.claude/CLAUDE.md`
unconditionally, and the kit repo itself has no `.claude/` either (sk census
§3-2/§3-3 — the defect class it flagged at venture-lab, unfiled against itself).
A fresh session in these repos gets **zero repo instructions at minute 0** —
the structural reason sessions keep re-hitting documented walls (fm census §3.3,
§3.7 draft-PR slip).

**2. "GitHub Actions is not permitted to create or approve pull requests" — fleet-wide scheduled-automation killer (owner-only fix).**
websites: review-bake run 29167034060 died on exactly this after the designed
direct-push fallback was ruleset-rejected — so the cron `23 5 * * *` fails
*every day forever*, the first-ever `review/data/stats.json` is stranded on
`bake/review-data-20260711-202653`, and each failure adds an undeletable `bake/*`
branch (403 wall) (ws census §3.1). fleet-manager: roster-regen schedule run
29172287288 (23:32Z) regenerated gen #10 and pushed `94cb773` to
`bot/roster-regen` but PR creation was denied verbatim (job 86595329797) —
feeding directly into problem 3's time-bomb. Filed as
`OQ-FM-ACTIONS-PR-PERMISSION` (fm owner-queue §B); the fix is a repo/org
Settings → Actions toggle only the owner can click.

**3. Roster-freshness time-bomb + substrate-gate inconsistency/loophole.**
Tonight's sharpest edge: roster on fleet-manager main = gen #9
(`generated-at 2026-07-11T20:25Z`, `docs/roster.md@e801da5`);
`check_roster_freshness.py` bar = 4h, **blocking on `claude/*` branches**
(`roster-freshness.yml@e801da5`) ⇒ from ~2026-07-12T00:25Z every `claude/*` PR
push here gets a blocking red no agent can clear — landing gen #10 needs a merge
agents are walled from (fm census §3.1). The gate layer is also inconsistent
across adopters: fleet-manager's substrate-gate holds ADDED born-red cards red,
but product-forge's gate applies the full locked-door check only to *modified*
cards — an added card takes the advisory path, so a forgotten complete-flip
merges green there, enforced by convention only (pf census U4). And ≥3 adopters
still run pre-v1.12.1 dists carrying the substrate-gate **false-green bug**
v1.12.1 exists to fix (sk census §3-1) — three different gate behaviors under
one name.

**4. substrate-kit adopter registry blind to ≥3 vendored adopters — "distribution COMPLETE" is false.**
`docs/fleet-repos.txt@4493251` lists 10 repos; status.md declares "v1.12.1
distribution COMPLETE — all 9 vendored adopters at v1.12.1". Ground truth:
idea-engine pins 1.10.0, superbot-mineverse 1.8.0, product-forge 1.7.0 — each
with a vendored root `bootstrap.py` at fetched origin/main, none in the roster
or registry (sim-lab 1.7.0, superbot-idle 1.7.1, local-clone evidence). The
`bootstrap.py currency` checker greens by omission — its verdict depends on a
hand-maintained roster nobody reconciles against the actual fleet (sk census
§3-1). Any prompt or plan trusting "COMPLETE" will skip repos still carrying
the false-green gate bug.

**5. Stale owner-queue / ORDER asks — the owner is being asked to do things that are already done.**
superbot-next OWNER-ACTION 2 (control/status.md@8062e83, updated 23:10Z Jul 11,
plus the archive-ready note) still asks the owner to *create*
`superbot-plugin-hello` — the repo has existed since 2026-07-10T16:03Z and
plugins.lock.json@249ecaa already pins the plugin; the ask has been dead ~31h
across multiple status overwrites (sn census §3). Same class elsewhere:
websites OWNER-ACTIONS item 1 still asks for the #141 merge click (#141 merged
at `0545906` 20:24Z) and its heartbeat names ~9 prune-candidate branches that no
longer exist (ws census §1/§3.4). Owner attention is the fleet's scarcest
resource; stale asks burn it and teach the owner to skim the queue.

**6. Inbox status-grammar trap — `status: new` forever on finished ORDERs.**
The one-writer/append-only bus means ORDER headers are never edited:
fleet-manager orders 015/016/018 keep `status: new` (inbox.md@e801da5 lines
405/463/595) with DONE only in later append-blocks, while control/README says
"execute any order whose status is `new`" — a literal-minded wake **re-executes
finished orders** (fm census §3.4). Identical shape in websites (11 orders,
completion truth only in status.md `done=001-011`, ws census §3.5) and
substrate-kit (13 ORDERs all `status: new`, sk census §3-6). Grammar and gate
are in tension fleet-wide; every wake prompt must carry the workaround.

**7. Checkers that lie (green by omission, red by design, chronic-noise masking).**
superbot `check_docs.py --strict` false-fails natural cross-repo references —
hit in ≥2 sessions the same day, idea filed but unfixed (sb census §2). The kit
currency checker greens while adopters are invisible (problem 4). substrate-kit's
adopter registry shows 9/10 rows ⚠️ DRIFT for the benign self-report-lag class —
real drift renders identically, so the signal is dead (sk census §3-4).
product-forge: `bootstrap.py check --strict` exits 0 while
`docs/current-state.md` is unfilled boilerplate after 23 PRs — checker-green ≠
docs-true (pf census U2); its kit session counter is stuck at 0 across 10
sessions, arming every count-keyed cadence against a needle that never moves
(pf census U5). The fleet's own doctrine (superbot Q-0120: a green that
contradicts visible evidence is a bug in the *check*) applies to its own tooling.

**8. Binding docs contradicting the tree.**
websites `.claude/CLAUDE.md@8f97654:40` says "Three independent … services"
while FOUR exist (`review/` since #132/#141), and its verify command runs 1 of
4 test suites vs CI's `pytest tests/ botsite/tests dashboard/tests review/tests`
(ws census §3.2) — a session following the binding doc verbatim under-tests and
mis-models the architecture. idea-engine's generated CLAUDE.md derives its
sections from superbot `docs/eap/fleet-manifest.md`, retired to a pointer stub
in superbot #1974 the same day (sb census §3). superbot's Q-0254 provenance
claim ("shipped in three templates") is 1-of-3 true — only
CONSTITUTION.md.tmpl:18-20 carries the doctrine (sk census §2). Related security
fold-in, same repo/class: **websites owner-panel CSRF** — POST
`/owner/actions/refresh` + `/owner/actions/rerun-ci` (app/owner.py@8f97654) are
protected only by HTTP Basic; browsers auto-attach cached Basic credentials to
cross-site form POSTs, no CSRF token / Origin check / rate-limit — the exact
analog of the mineverse OAuth CSRF, unfiled (ws census §3.3). Impact bounded
(reversible actions) so it ranks here rather than top-3, but it is a contained,
shippable fix a session CAN land.

**9. Normalized-red CI — superbot-next golden-parity fails by design on every main push.**
The `golden-parity` workflow concluded **failure ×5** on the last 5 main pushes
(`f71d60b`→`249ecaa`) because the `report` leg is red-by-design; the required
`gate` job inside is green (sn census §1, docs/status/README-first.md@249ecaa).
Anyone — human, tool, or fresh session — reading workflow conclusions sees a
repo that has "failed CI" forever, and sessions are being *trained to ignore
red* (the E4 red-numbers misread class already cost time, sn census §4). Not
fixable by docs alone; every prompt must say "judge by the named gate job".

**10. Un-stamped heartbeat/status assertions + dark inboxes.**
superbot `control/status.md` (19:45Z) states "next recon at #2010" as
present-tense truth 4h after that pass merged — the "irregular cadence by
design" caveat covers update *frequency*, not assertion staleness; no
`verified-against: <sha>` stamps anywhere (sb census §3). fleet-manager's
heartbeat truth is forked three ways across main + parked #97 + parked #91
(fm census §3.8). product-forge is ARCHIVED with **no trigger armed** while the
fleet-manager failsafe wake IS armed and its protocol writes ORDERs into
product-forge's inbox — a new ORDER would sit unread indefinitely, and nothing
fleet-manager-side records "forge is dark — wake it first" (pf census U6).
Managers reading heartbeats get superseded facts; managers writing orders get
silence.

*Ranking notes:* the skeleton order survived verification against the census
files with one adjustment — the websites owner-panel CSRF is folded into #8
(binding-doc / same-repo class; bounded, reversible impact per ws census §3.3)
rather than ranked standalone. #2 and #3 are causally linked (the Actions-PR
wall is *why* the roster time-bomb exists) but kept separate: #2 is the
owner-only root cause, #3 is the regression-risk payload plus the independent
gate-loophole class.

---

## superbot — condensed census

Ground truth: origin/main @ `1ecc211` (2026-07-11 23:32Z, merge PR #2014).

### STATE — verdict: FRESH
- Hub with **no standing seat** (Q-0264); product runtime work moved lane-side
  (superbot-next rebuild). 8-seat structure recorded in
  `docs/owner/fleet-8seat-structure-2026-07-11.md`; 44th recon pass done
  (band-#2010, next at #2040, `f0444c2`).
- Heartbeat `control/status.md` updated 19:45Z vs last commits 23:24–23:32Z —
  FRESH by cadence, but *content* already lags (says "next recon at #2010"
  while #2010 merged 23:24Z; rebuild counts stale).
- **Zero open PRs** (Q-0103 discipline holding). CI on main **all green**
  (12/12 runs). Local checkers at `1ecc211`: ledger `--strict` clean,
  `check_docs --strict` exit 0, recon not due.

### KNOWN PROBLEMS
- codex-final-review CI lane was born-broken ~22 days (2026-06-19 → fixed
  PR #1995 @ `8214200`, invalid YAML) — a review lane silently dead 3 weeks.
- fleet-manifest went ~33.5h stale before retirement to a pointer stub
  (PR #1974); `check_manifest_freshness.py` deleted per its Q-0105 kill-switch.
- **check_docs cross-repo false positives** — recurring, hit ≥2 sessions the
  same day; idea filed (`docs/ideas/check-docs-cross-repo-path-awareness-2026-07-11.md`)
  but the checker still lies. 5 supersede-banner soft warnings carried
  (cross-repo successors unresolvable). `check_loop_health.py` = SKIP in recon
  sessions (no `gh` token).
- Codex usage cap fleet-wide (owner click to raise). Owner-action queue
  outstanding (`.sessions/2026-07-11-env-grant-and-relaunch-handoff.md`):
  Anthropic email before Tue 7/14, Codex reports review, Stripe keys, plugin
  seed push, env decision (websites #143), relaunch routines.
- Negative findings: router 274 Q-blocks all answered; review-inbox has zero
  live REV entries; no material contradictions among binding docs.

### UNKNOWN PROBLEMS
- **Cross-repo stale derivation:** idea-engine's binding CLAUDE.md derives from
  the retired fleet-manifest — sibling sessions land on a tombstone. Unfiled in
  either repo.
- **Heartbeat asserts stale facts without per-field stamps** — no
  `verified-against: <sha>`; manager sweeps read superseded claims (top-10 #10).
- **Hermes surface half-alive:** dispatch bridge doc still `living-ledger`,
  `scripts/hermes/` shipped, review-merge gate retired (Q-0197); whether the
  seat exists under the 8-seat structure is stated nowhere. `needs-hermes-review`
  residue is comment-only (clean retirement — negative finding).
- ORDER-done spot-checks PASS (001/#1977, 002/#2003 — no phantom deliverables).
  Checkers verified honest today (#763 false-green class fixed).
- **Orientation payload is the biggest unfiled cost:** current-state.md 684
  lines / 79 KB (header lines >4,000 chars); journal 792 lines one day behind;
  boot set = 5 documents. Sessions already pay a manual bypass tax (ad-hoc
  "don't re-derive" handoffs). **Three coexisting "START HERE" briefs** — a
  minute-0 reader can't tell which is authoritative.
- Routines: no superbot-hub cron (consistent with Q-0264); ~20 spent one-shot
  send_later triggers linger disabled (clutter). No security TODOs (grep clean).

### EXPECTATIONS
Claim lane → born-red PR + `.sessions/` card in first commit within ~2 min
(Q-0133/Q-0189) → goal-complete work → `python3.10 scripts/check_quality.py
--full` (Python 3.10 only) → flip card last → auto-merge on green (merge=deploy
Q-0193) → four mandatory enders (Q-0015/Q-0089/Q-0102/Q-0104) + friction→guard
(Q-0194). Decide-and-flag, never wait (Q-0240/Q-0241); CLAUDE.md propose-only
(Q-0106); recon only via routine (Q-0124). Evidence of waste: repeated
"don't re-derive" enumerations, a founding prompt gone stale between write and
boot (part-4h), two sessions burned on the same check_docs false positives.

### PROMPT IMPLICATIONS
- Must say: superbot = fleet hub, NO standing seat (Q-0264) — product work goes
  lane-side unless owner-directed.
- Must name THE single authoritative brief file + SHA (not three START-HEREs).
- Must carry the check_docs cross-repo workaround (prefix repo names in prose);
  root fix is tooling.
- Encode `verified-against: <sha>` on status assertions — durable fix is a
  kit-template change (owner/tooling). idea-engine derivation fix is not
  superbot-promptable.
- Hermes: "legacy — do not extend without owner word." Owner-click queue items
  (Codex cap, 7/14 email, plugin seed, Stripe): "don't re-verify; queued."
- Front-load the ~6 minute-0 facts verbatim instead of pointing at 79 KB of
  ledger; compressed hub boot pack is tooling worth proposing.

---

## superbot-next — condensed census

Read at origin/main `249ecaa` (2026-07-11T23:44Z, PR #218); some cites at
`8062e83` (heartbeat commit).

### STATE — verdict: FRESH (wake loop disarmed)
- Manifest-driven kernel rebuild ("sb/"); all seven port bands built; boots to
  RUNNING on real Postgres ("CUT-1 smoke PASS"); ~1,125+ unit tests; 22-checker
  fleet + six required named gates green; golden-parity `report` leg
  red-by-design.
- Heartbeat 23:10Z vs newest main 23:44Z — FRESH (benign lag); live branch
  `wave6/inventory-flip` committed 23:46Z.
- Open PRs: #217 (farm/mining money races, born-red); #206 + #196 (codex
  docs-only reviews, deliberately PARKED per
  control/claims/codex-risk-review-prs-196-206.md@249ecaa).
- CI last 5 main pushes: `ci` ✅×5, `named-gates` ✅×5, `golden-parity`
  workflow **failure ×5** (designed; required `gate` job green).

### KNOWN PROBLEMS
- Parked #196/#206 await verify-then-supersede-and-close (partially discharged
  by merged #213 `f71d60b` + open #217).
- Documented walls: `setup` PARKED (create-channel wall, playbook trap 17),
  `quicksetup` BLOCKED (D-0030), band-7 live-NL owner-key-gated (OWNER-ACTION 5),
  ~120–182 `_unmapped` goldens to re-home.
- ⚑ OWNER-ACTIONs open: 2 (hello-plugin — STALE, see below), 3 (require-up-to-date
  "update-branch dance" stranding PR tails #86/#87, admin-only), 5 (AI key),
  6 (fleet routines auto-disabled by the 16:31Z env teardown).
- Archive/active contradiction: archive-ready note written at `0e7cacd` (37/49)
  then ~10 more PRs merged (39/50) — repo not archived but wake routine
  DISARMED (q0265 retro) → progress depends on externally-fired sessions only.
- Codex reviewer **phantom commits ×3** (#144/#160/#178); Q-0120 guard held.
- Gen-1 self-review remediation never built: `tools/live_drive.py`,
  `docs/dev-environment.md`, red-class table — none exist ~130 PRs later.
- Cross-repo pointer lag: superbot's plan-of-record + ledger pin 37/49 /
  #111–#191 vs actual 39/50 / #218. Count drift across 4 sources (41 vs 47 vs
  50 subsystems); only CI checker output is live. current-state.md "In flight"
  is 2 days ≈ 120 PRs stale.

### UNKNOWN PROBLEMS
- **STALE OWNER-ACTION 2 / ORDER 002:** still instructs the owner to create
  `superbot-plugin-hello` — repo exists since 2026-07-10T16:03Z;
  plugins.lock.json@249ecaa already pins it. Dead ask ~31h (top-10 #5).
- **Boot pointer targets a non-existent file:** AGENT_ORIENTATION says boot set
  lives in `.claude/CLAUDE.md` — **no `.claude/` at HEAD**; tracked copy only at
  `.substrate/claude/CLAUDE.md`; identity slot reads "superbot-next is built in
  Python." A fresh session auto-loads nothing (top-10 #1).
- `.session-journal.md` is an empty template; real memory scattered across 69
  session cards + a 42 KB status.md. **Flip-playbook traps have no durable
  home** — "playbook trap N" cited across 20+ cards, no index anywhere.
- README-first.md stale: still gates the first flip on cleared OWNER-ACTION 1;
  counts "0/465 · 0/49" vs 39 flips landed.
- Permanent workflow-level red (top-10 #9). Auto-merge enabler exists only as
  an uninstalled `.substrate/ci/` template; ruleset blocks direct pushes +
  requires up-to-date branches → per-PR MCP arming.
- ORDER spot-checks (003/005/006/007) all ✓ — defect runs the other way (002
  done-when met but unmarked). Duplicate-looking parity rows are deliberate
  alias keys but foot-gun external tallies. No security TODOs; router empty.

### EXPECTATIONS
Boot order (working agreement → HANDOFF.md → current-state.md); one-writer
control bus; born-red card with 4 byte-markers; PRs READY, auto-merge on six
named gates, never-wait/silence=consent (PL-002); CAPABILITIES discovery rule;
cite PL-IDs; @codex question per substantive PR (ORDER 010). Minute-0: **red ≠
broken** (gate job is the signal); A-16 one-way parity door; grep status.md
(42 KB), don't read it; flip playbook lives in wave cards. Measured waste:
orientation ≈ **25% of session time** (self-review-2026-07-09 §C1); ~50-min MCP
events stall (trap 13a); oracle full-file MCP reads denied while a full local
superbot clone sat unused.

### PROMPT IMPLICATIONS
- Verify each OWNER-ACTION against live GitHub before relaying;
  superbot-plugin-hello exists — close/advance ORDER 002.
- Inject the boot set explicitly (CONSTITUTION.md + control/status.md +
  README-first) — nothing auto-loads; durable fix needs tooling/owner.
- Judge CI by named `gate`/required jobs, never golden-parity's conclusion.
- Name 2–3 wave cards as the porting manual; order a session to promote the
  trap index into docs/. Read the oracle from the LOCAL /home/user/superbot
  clone, never GitHub MCP full-file fetches.
- Trust check_parity_depth CI output for counts; fix stale pointers on sight
  (Q-0166 analog). Finish the #196/#206 claim next-step. Write the journal
  Quick-reference on first derivation. Restate Q-0120 for codex phantoms.
- Not promptable: re-arming the wake loop + fleet routines (OWNER-ACTION 6),
  update-branch ruleset (OWNER-ACTION 3).

---

## websites — condensed census

HEAD at census: `8f97654` (2026-07-11 22:33Z, merge PR #156).

### STATE — verdict: STALE (mildly, deliberately parked)
- Four FastAPI services — control-plane (`app/`), botsite, dashboard live on
  Railway; `review/` built + expanded (#141) but NOT deployed (Railway service
  = queued owner ask). Kit v1.12.1; `quality` REQUIRED on main; merge = deploy.
- Heartbeat 19:49Z, `phase: CLOSING — chain PARKED`, "main HEAD 345b5ce" —
  actual main advanced 6 commits to `8f97654` (22:33Z). Superseded facts a fresh
  session would act on: "#141 awaiting owner squash-merge" (merged `0545906`
  20:24Z); "kit: v1.12.0" (v1.12.1 since `93ad6cd`/#155); prune list names ~9
  ghost branches (7 heads remain + one NEW stranded
  `bake/review-data-20260711-202653`). Park was an explicit owner order.
- Open PRs: none. CI last ~12 runs: `quality` green except one expected
  born-red hold; **one real failure: review-bake run 29167034060** (§ below).

### KNOWN PROBLEMS
- Owner queue = `docs/owner/OWNER-ACTIONS.md` (7 ⚑ asks): #141 click (**done,
  entry stale**); botsite DATABASE_URL; control-plane GITHUB_TOKEN PAT (fleet
  walks 18 lanes on the anonymous 60 req/h ceiling); review/ Railway service;
  Q-0004 live-bot-control (blocking · open); Discord OAuth app; scoped
  control-API token.
- Walls (CAPABILITIES): branch deletion 403; tag push 403; direct
  api.github.com blocked; routine-fired sessions can lack push credential
  (rescue PR #59); "never record pushed without ls-remote proof".
- Documented recurring failures: gate leak PR #19; silent routine fires (2/4);
  the 5× cron-correction saga; wall-clock time-bomb tests (defused #111/#114/#130,
  AST guard + `app/clock.py`); truth sweep PR #111 found current-state.md
  carrying **4 stale claims**.
- Kit-version drift: none at HEAD (bootstrap.py = 1.12.1); quality.yml gate
  flags all exist in bootstrap.py (grep-verified). Unfinished lanes: dashboard
  `/admin` dry-run stub (Q-0004), botsite `/submit` stub, backlog
  "buildable-now empty".

### UNKNOWN PROBLEMS
1. **review-bake broken end-to-end, fails EVERY day 05:23Z** (top-10 #2):
   direct push ruleset-rejected → `gh pr create` → "GitHub Actions is not
   permitted to create or approve pull requests"; fallback steps 2–3 of
   review-bake.yml can never happen. First-ever `review/data/stats.json`
   stranded (ABSENT at HEAD — review-site stats show "no data yet"
   indefinitely); each run adds an undeletable `bake/*` branch. Nothing filed.
2. **Binding CLAUDE.md contradicts the tree** (top-10 #8): "Three … services"
   vs FOUR; verify command = `pytest tests/ -q` vs CI's four-suite line.
   Kit-generated, never re-rendered after review/ landed.
3. **CSRF in app/owner.py** (top-10 #8 fold-in): POST refresh/rerun-ci on
   Basic auth only — cached credentials auto-attach cross-site; no token /
   Origin check / rate-limit. Bounded impact, contained fix a session CAN ship.
4. Heartbeat + owner-queue entries superseded on main; `/fleet` / `/queue`
   render stale facts until the next 4-hourly fire.
5. Every ORDER says `status: new` forever (completion truth only in status.md
   `done=001-011`; spot-checks 004/009/011 clean) — top-10 #6.
6. Armed 4-hourly wake over a parked chain + dry backlog — live spend at a
   closed program; no disarm/retarget ask filed.
7. healthcheck covers 3 services; review/ needs adding at deploy — easy to forget.
- Negative findings: no secrets in tree; claims dir empty; settings.json pure
  kit-hook wiring.

### EXPECTATIONS
Boot: CLAUDE.md → HANDOFF.md (untracked, never commit) → current-state.md;
CAPABILITIES before declaring any wall. Landing: born-red card → READY PR →
required `quality` green → squash-merge → merge IS deploy; control-only diffs
ride the fast lane; `📊 Model:` line required (ORDER 010). One-writer status;
never edit inbox; claim first; ls-remote proof. Search hygiene: exclude
bootstrap.py + .substrate/. Waste evidence: truth-sweep #111 (4 stale claims a
fresh session "would trust"); ORDER 004 existed because a gate change
red-flagged 18 old cards.

### PROMPT IMPLICATIONS
- review-bake: not promptable (owner Actions setting) — but check the latest
  bake run + stranded `bake/*` before trusting review stats; file the owner ask.
- Treat review/ as first-class fourth service; run the FULL four-suite pytest
  line; queue a kit re-render of CLAUDE.md.
- Any new state-changing route needs CSRF protection — Basic auth is not a
  CSRF defense; fixing the two /owner actions is shippable now.
- Reconcile status.md + OWNER-ACTIONS against live GitHub before relaying;
  order truth = status.md `done=` line, never inbox `status:` fields.
- Fired sessions: check backlog-dry + parked state first; file disarm/retarget
  ask. Branch litter: not promptable (403s; owner enables auto-delete).
- current-state.md is a dated snapshot — verify in-flight claims live (bit twice).

---

## substrate-kit — condensed census

HEAD = `4493251` (2026-07-11T23:34Z); downstream pins read at each repo's
fetched origin/main unless marked local-only.

### STATE — verdict: FRESH
- Engine "finished + enforced" (1057 tests green per status); KL-0…KL-4 DONE;
  v1.0.0→v1.12.1 release discipline live; kit is consumer #0. current-state.md
  stability section dated 2026-07-09 (2 days behind; live truth migrated into
  control/status.md).
- Heartbeat 23:40:00Z vs last commit 23:34:13Z (#253) — agree to the minute.
- Open PRs: exactly 2, both **parked by design** (owner ratification,
  do-not-automerge): #220 (T5 v2 align) + #238 (T5 v3 probe re-shape) =
  OWNER-ACTIONs 14/15. A third PR event fired 23:46Z on branch
  `order-prompt-hardening-input` — enabler run 29172639139 **skipped**
  (non-`claude/*`).
- CI last ~10 runs green; the two `failure` conclusions are designed born-red
  gate holds. Latest release v1.12.1 three-way-verified (run 29170017074,
  asset sha256 1055ca2c…16e4aa).
- Downstream pins: websites 1.12.1 ✓; **idea-engine 1.10.0, superbot-mineverse
  1.8.0, product-forge 1.7.0 — none in the registry**; sim-lab 1.7.0 +
  superbot-idle 1.7.1 (local clones, lower confidence).

### KNOWN PROBLEMS
- Chronic heartbeat `kit:`-line self-report lag — 9/10 registry rows ⚠️ DRIFT
  (docs/adopters.md, generated 22:36:49Z); bump ownership is an open manager
  question. Parked #220/#238 block B1 run-10.
- **B1 cold-start bench: 1 PASS / 7 FAIL** — kit-planted repos mostly fail the
  kit's own cold-start bar (ruling ORDER 011, f5-ruling-order-011.md).
- Routine registry instability: the daily kit-lab trigger **vanished** from a
  718-trigger scan, re-armed as trig_01Jm57… (#253); an "already deleted"
  failsafe found still armed (#252) — records repeatedly diverge from the live
  registry.
- ~48 stale merged-PR branches (OA-10; deletion is a 403 wall). venture-lab
  AGENT_ORIENTATION points at nonexistent `.claude/CLAUDE.md` — flagged 2
  consecutive waves, template fix still pending. fleet-manager has no live root
  CLAUDE.md (staged only). pokemon-mod-lab `automerge.required_context` says
  "substrate-gate" but the real required check is "ROM builds".
- Kit tree-internal pin drift deliberate (config 1.0.0 vs dist 1.12.1).
  superbot-next origin/main force-pushed mid-wave (lane owns reconcile).
- **Q-0254 template claim PARTIALLY FALSE:** doctrine present in
  CONSTITUTION.md.tmpl:18-20 only; collaboration-model.md.tmpl +
  question-router.md.tmpl have zero hits. Generated repos carry the effect via
  the owner-profile slot; superbot's provenance claim is 1-of-3 true.

### UNKNOWN PROBLEMS
1. **HEADLINE — adopter registry blind to ≥3 (likely 5) vendored adopters;
   "v1.12.1 distribution COMPLETE" false fleet-wide** (top-10 #4). The invisible
   repos still run dists carrying the substrate-gate false-green bug v1.12.1
   fixes (#228 payload). Currency checker lies by omission.
2. **Kit's own orientation pointer is dead; nothing auto-loads:**
   AGENT_ORIENTATION.md:10 → `.claude/CLAUDE.md`; no `.claude/` and no root
   CLAUDE.md in the kit repo. Real agreement = root CONSTITUTION.md (not
   harness-loaded). Manually-started sessions start blind.
3. **The dead pointer ships in the template** — AGENT_ORIENTATION.md.tmpl:10,:34
   reference `.claude/CLAUDE.md` unconditionally; every staged-only adopter
   inherits it; no release since carries the fix (top-10 #1 root cause).
4. DRIFT-row noise desensitization — chronic benign red renders identically to
   real drift; no severity tiering (top-10 #7).
5. Auto-merge gap for non-`claude/*` branches (enabler arms only
   `startsWith(head_ref, 'claude/')` — the 23:46Z PR will sit unmerged on green).
6. Inbox `status: new` ×13 vs status.md done=001…013 (top-10 #6). DONE
   spot-checks 003/005/011/012/013 all ✓ — no false DONEs (negative finding).
7. Two "what is true now" surfaces with different freshness and no ranking
   (current-state.md 2 days stale vs status.md live).

### EXPECTATIONS
CONSTITUTION → control/inbox.md at HEAD → control/status.md; claim via
control/claims/; born-red card first commit, flip last; card markers incl.
`📊 Model:` + `Run type: routine · lab`; overwrite status.md as deliberate last
step; lane-repo writes are KIT DISTRIBUTION ONLY (Q-0261.3); never merge own
changes to the bench oracle. Cadence: daily lab loop 06:00Z + 2-hourly failsafe,
both re-armed 07-11T23:0x–2xZ, first-fire confirmation owed. Orientation waste
is literally benchmarked here (B1 1/8 PASS; PR #236 shipped to cut footprint;
the multi-KB single-line phase field is itself a parse cost).

### PROMPT IMPLICATIONS
- Registry incomplete — verify against the actual fleet before claiming
  distribution complete; root fix = roster reconciliation + discovery-based
  checker (tooling).
- "The kit's working agreement is root CONSTITUTION.md (no .claude/CLAUDE.md);
  read it first"; template fix + live pointer-target check = kit tooling work.
- Never assert the Q-0254 doctrine lives in all three templates; superbot
  CLAUDE.md correction is owner-gated (DISCUSS Q).
- DRIFT ≠ ignore — classify each row (severity tiers = tooling). Always branch
  `claude/*` or auto-merge never arms. Verify routine state by live
  list_triggers probe, never status prose. ORDER status lives in status.md.
  control/status.md outranks current-state.md for freshness. Minute-0 set =
  CONSTITUTION → inbox → status ONLY (ON-T2 fast path).
- Confidence notes: sim-lab/superbot-idle pins unfetched; the 23:46Z PR content
  unexamined; `bootstrap.py check` not run locally (CI green on #244/#250 heads
  is ground truth); branch-protection contexts inferred, not queried.

---

## fleet-manager — condensed census

All reads at HEAD `e801da5` (2026-07-11T22:29Z, kit v1.12.1 upgrade #90).

### STATE — verdict: FRESH-but-seat-in-handover
- Records custodian (Option A custodian-primary, owner decision 2026-07-11):
  canonical roster, owner queue + candidate feed, evidence index, fleet-triage;
  `control/` ORDER-relay secondary. Baseline = P1–P3 toolchain (fm #81–#86):
  roster regen cron `40 */2`, `check_roster_freshness.py` (4h bar, blocking on
  `claude/*`), `check_owner_queue.py`, substrate-gate CI.
- Heartbeat 21:50:00Z vs HEAD 22:29Z (heartbeat-exempt upgrade) ≈ 39m — FRESH.
  BUT the stamp records the coordinator seat ARCHIVED; the successor heartbeat
  exists only as parked **#97** (23:47Z: new failsafe trig_01BKpsyoBzp1K1ob9H3iu1gM
  armed, old trig_01F9UdoUtLy8oknBPBkHLshS deleted). Main is one generation behind.
- Open PRs (9): **#88→#89→#91** parked restructure stack (stacked bases, DO NOT
  TOUCH); **#92** parked settings port (repo has NO `.claude/`); #93/#94/#96
  tonight's census PRs (born-red by design); **#95 opened DRAFT** (violates
  playbook R6); #97 successor heartbeat (supersedes the status copy inside #91 —
  union-resolve landmine at rebase).
- CI last ~12: substrate-gate FAILURE on all 4 research branches ~23:44Z
  (expected holds); roster-freshness SUCCESS at that moment; **roster-regen
  schedule run 29172287288 (23:32:30Z) FAILURE** — gen #10 pushed to
  `bot/roster-regen` (`94cb773`) but PR creation denied verbatim (job
  86595329797).

### KNOWN PROBLEMS
1. **Actions-can't-create-PRs wall** — OQ-FM-ACTIONS-PR-PERMISSION
   (owner-queue §B); attempted twice live (runs 29164975251 GH013, 29165152964),
   verbatim walls recorded; still un-clicked.
2. **Classifier merge wall, 4 shapes** (seat retro §2): self-approval, relayed
   authorization, shared-token-no-APPROVE, content-correlation (fm #68 parked
   while identical #69/#70 merged). Doctrine: park READY+green.
3. Born-red arming wall — playbook R21 (PR #10 burned 3 attempts); superseded
   by UNIVERSAL v4 §2.4 (merged `e1848ff`, #76): never merge/arm own PRs.
4. **No auto-merge enabler here (and 10 of 13 lanes)** — enabler only in
   substrate-kit/superbot/idea-engine (docs/findings/enabler-install-verification-2026-07-11.md);
   combined with #2, agent PRs can only park.
5. **9 lane failsafes auto-disabled** (`auto_disabled_env_deleted`,
   14:45–16:16Z; handoff §3.2); owner never answered deliberate-or-incident;
   8 of 11 disabled records vanished from list_triggers by 21:3xZ (cause unknown).
6. PR #47 empty-vehicle lesson (retro §4): merged PR carried only its card;
   payload rebuilt in #76/#77. 7. Inbox ORDER-number race (R19, cost 2 PRs).
8. games-mining heartbeat unparseable → roster verdict DEAD; never routed as an
   order. 9. Paste-wave / env-repaste pending on owner (OQ-PASTE-WAVE,
   OQ-ENV-SETUP-REPASTE) — deployed Project instructions drifted v1 vs main
   v2/v3. 10. Roster ↔ superbot fleet-manifest ↔ idea-engine CLAUDE.md — three
   sources, one truth claim.

### UNKNOWN PROBLEMS
1. **⏰ Freshness time-bomb tonight (highest regression risk):** roster = gen #9
   (20:25Z); 4h blocking bar ⇒ from ~00:25Z every `claude/*` PR (including all
   5 overnight research PRs) reds on push and **no agent can clear it** (gen #10
   needs a walled merge). Nobody flagged the collision with the overnight program.
2. Regen "honest degrade" contradicts observed behavior — handoff §3.1 says v3
   "degrades honestly instead of failing red" but the 23:32Z run exited 1.
3. **No CLAUDE.md and no `.claude/` on main at all** — agreement lives in
   CONSTITUTION.md + docs/playbook.md, neither auto-loads; the structural reason
   sessions keep hitting the classifier walls (top-10 #1).
4. **Stale `status: new` headers** on orders 015/016/018 (lines 405/463/595)
   while control/README says "execute any order whose status is `new`" — a
   literal wake re-executes finished orders; append-only gate forbids the header
   flip (top-10 #6).
5. Retired-seat trigger still firing: "retro-games coordinator (no repo)"
   failsafe trig_01Y99uDKNtKTz2EtRYPWZkGY cron `50 */2`; retire parked with the
   stack. 6. Duplicate capabilities ledgers (docs/CAPABILITIES.md kit-planted vs
   docs/capabilities.md fleet master — case-distinguished only). 7. **PR #95
   opened DRAFT against R6** — evidence overnight sessions aren't reading the
   playbook (consistent with #3). 8. Heartbeat truth forked across main + #97 +
   #91 (top-10 #10). 9. DONE-order spot-checks clean (001–004 + universal
   prompt all exist — negative finding). 10. Branch protection: main PR-only
   (GH013 verbatim); substrate-gate holds born-red ADDED cards;
   `allow_auto_merge` setting not measured. 11. Security-adjacent residue:
   read-only PAT suggestion unactioned; OQ-VENTURE-STRIPE-KEYS / mineverse
   OAuth-CSRF ride the parked stack; no secret values in any file read.

### EXPECTATIONS
Custody first: regenerate roster every wake (R25); owner-queue curated
(R16/R17 — click-level, attempted-or-exact-wall evidence, assumption-based asks
banned); evidence index + fleet-triage current. Bus discipline: inbox FIRST,
execute `new` P0→P1; overwrite own status LAST; never edit inbox; serialize
appends (R19). Verify against repos, never agent reports (R2); match merge
events to the right PR (R3); capabilities discovered not assumed (R18).
Merge doctrine: UNIVERSAL v4 §2.4. Minute-0 kit: CONSTITUTION → status/inbox →
roster → owner-queue → playbook — **none auto-loads**; the prompt must carry
the boot list. Documented waste: 3× re-teaching of worker-prompt rules, 3
burned arm attempts (#10), 2 PRs lost to the ORDER race, a full round-trip
wasted on a dispatch-only session.

### PROMPT IMPLICATIONS
- Freshness bomb: "if roster-freshness reds your PR, it's the stale-roster
  class — do NOT chase it; note and continue; landing bot/roster-regen is a
  coordinator/owner action." Root fix not promptable.
- Actions-PR wall: owner click only; prompts should stop re-probing. Classifier
  wall: restate "park READY+green, never merge/arm own PR, never retry a denial"
  verbatim.
- Carry the boot list until #92 + a future CLAUDE.md land. ORDER-DONE rule:
  "an ORDER is DONE if ANY later update-block marks it DONE — scan the whole
  inbox." Restate R6 READY-never-draft. "Trust the newest heartbeat across
  main + open PRs (#97), not main alone."
- Not promptable: retired-seat trigger deletion (MCP/owner, rides the stack);
  failsafe env-deletion mystery (owner answer). Cross-repo: superbot/idea-engine
  prompts must name fleet-manager `docs/roster.md` as the only live roster.
- Empty-vehicle: "verify the payload landed — diff the merge." ORDER race:
  "next free ORDER at HEAD, never a concrete number." Restructure stack
  #88/#89/#91(+#92): "parked — never merge, rebase, or edit their branches."

---

## product-forge — condensed census

All reads via `git show origin/main` at HEAD `4fdfa8a` (2026-07-11T19:49Z, #23);
checker runs on a scratch `git archive` copy.

### STATE — verdict: FRESH but ARCHIVED/going-DARK
- Product-build seat: ORDERs 001–004 all done; games-web phase-1 COMPLETE
  (run.sh, fixtures, contract v1.0.1, tests, SVG art, a11y, Pages deploy
  prepped); archive-ready declared (docs/retro/archive-ready-2026-07-11.md).
  **docs/current-state.md is unfilled kit boilerplate** — real state lives in
  control/status.md + the retro.
- Heartbeat 19:39:50Z vs last commit 19:49Z — FRESH; lane deliberately
  archived: "NO trigger remains armed" — **verified true** (300-routine scan:
  zero enabled routines reference product-forge).
- Open PRs: ZERO (#1–#23 all merged). CI last 12 runs all success; only
  historical failures are deploy-pages runs 29126980391/29128667052 ("Get Pages
  site … Not Found"), expected until Pages is enabled (OA-003).

### KNOWN PROBLEMS
- ⚑ OA-003 open (owner click): GitHub Pages not enabled → site 404.
- External waits: superbot read-only API for games-web phase-2 (proposal at
  products/games-web/docs/phase2-data-api-proposal.md, no reply); inbox dry
  since ORDER 004 (~9h of 15-min ticks, honesty guard held, no filler).
- Merge classifier seat-variance: arming denied on #8/#12/#13/#14/#15/#17/#19,
  succeeded on #6/#7/#9/#10/#11/#21; self/peer merge denied on #4 ("permission
  laundering") — recipe in PLATFORM-LIMITS.md.
- Concurrency overlap #4/#5; the one-writer-per-product fix is still only a
  PROPOSAL in review-queue.md — never ratified, and the repo is archived, so it
  will rot.
- Past incidents guarded: future-dated heartbeat (~7.5h ahead, hand-typed) →
  check-heartbeat.py + heartbeat-guard.yml (024fccd); PR #3 red on `updated:`
  regex.
- Platform walls: failing check_run output can be EMPTY over the API (diagnose
  locally); ruleset contents unreadable (verify functionally).
- **Kit drift: pinned 1.7.0 vs kit HEAD 1.12.1 — 5 minors behind** (and
  invisible to the kit registry, sk census §3-1).

### UNKNOWN PROBLEMS
- **U1 — working agreement doesn't exist at its advertised path:** no
  `.claude/CLAUDE.md`, no root CLAUDE.md; only `.substrate/claude/CLAUDE.md`
  with the "⚠️ UNRENDERED SLOTS" banner (`${primary_language}`,
  `${architecture_layers}`, `${verify_command}`, `${owner_profile}` unfilled);
  AGENT_ORIENTATION step 1 is a dead pointer (top-10 #1).
- **U2 — orientation step 2 points at an empty ledger:** current-state.md is
  boilerplate after 23 PRs, yet `bootstrap.py check --strict` is GREEN (exit 0
  verified) — checker validates markers/reachability, not filledness (top-10 #7).
- **U3** — .session-journal.md all placeholders after 10 sessions; knowledge
  scattered in cards + PLATFORM-LIMITS.
- **U4 — substrate-gate completeness hole:** full locked-door check only on
  *modified* cards; ADDED cards get the advisory sentinel — but every forge
  session adds its card in its own PR, so the forgotten-flip gate never engages
  (guard-fire 2026-07-11T05:14:25Z came from a LOCAL check, not CI) (top-10 #3).
- **U5 — kit session counter stuck at 0** (state.json, kit 1.7.0) despite 10
  cards — every count-keyed cadence (compaction@20, reconciliation@20,
  graduation@50) armed against a needle that never moves. Whether 1.12.1 fixes
  it: not measured.
- **U6 — archived lane + live manager = dark inbox:** no trigger wakes forge,
  but the fleet-manager failsafe (trig_01BKpsyoBzp1K1ob9H3iu1gM, `30 */2`) is
  armed and writes ORDERs into control/inbox.md — a new ORDER sits unread
  indefinitely; nothing fleet-manager-side records "forge is dark" (top-10 #10).
- **U7** — two similarly-named claim mechanisms (root claims/ vs control/claims/);
  AGENT_ORIENTATION names only one.
- Spot-check of done ORDERs 001–004: all deliverables EXIST ✓ (negative
  finding). Also negative: heartbeat checker verified honest; no control/outbox.md
  (correct per protocol); no .claude/settings.json at all (only the never-
  installed .substrate/hooks template); no security TODOs in games-web (mock
  data only).

### EXPECTATIONS
FIRST: pull → read control/inbox.md → claim + execute `new` ORDERs by priority;
empty inbox → polish the newest product's roughest edge + flag `inbox empty` —
never invent product intent. Heartbeat-before-work; born-red card first commit,
flip last; overwrite status LAST with `updated:` pasted from `date -u` (never
typed). READY never draft; land your own PR (arm in the ~5–7s gate-pending
window or REST merge-on-green; on classifier denial flag "awaiting owner
click"). Verify: `bootstrap.py check --strict` + product tests. Money/external
spend: NEVER execute — six-field OWNER-ACTION plan only (Q-0259 r.4). Waste
evidence: a read pass burned enumerating gate needles; a whole hygiene PR (#22)
to un-flag a wrong-path error; red substrate-gate undiagnosable via API.

### PROMPT IMPLICATIONS
- U1: state the working agreement inline or point to
  README/CONSTITUTION/CONVENTIONS — never `.claude/CLAUDE.md`; rendering needs
  owner/tooling. U2: "truth = control/status.md + the archive-ready retro;
  IGNORE current-state.md (unfilled)" — filling it is a cheap first fix.
  U3: don't say "read the journal"; recipes live in PLATFORM-LIMITS + cards.
- U4: "flip the card complete before the final push — CI will NOT catch a
  forgotten flip on an added card"; CI fix needs kit upgrade. U5: not
  promptable (kit/tooling). U6: fleet-manager prompts must encode
  "product-forge is DARK — arm a wake before routing an ORDER"; resume recipe
  in the archive-ready retro. U7: name which claim mechanism applies.
- Seat-variance: carry the landing recipe; permanent fix = owner settings.
  OA-003: owner click (Settings → Pages). Phase-2: a superbot session must
  answer the API proposal. One-writer-per-product until ratified. Kit
  1.7.0→1.12.1: needs a deliberate upgrade session. Heartbeat: `date -u` +
  check-heartbeat.py before push.

---

## Prompt implications — consolidated

Union of the per-repo implication lines, deduplicated and grouped.

### (a) Every-Project boilerplate (goes in ALL fleet Project instructions)

1. **Boot-set injection:** name the repo's real working-agreement files inline
   (CONSTITUTION.md / playbook / README set) — never rely on `.claude/CLAUDE.md`
   auto-load; in 4 of 6 repos it doesn't exist or isn't rendered.
2. **Verify before relaying:** check every OWNER-ACTION / owner-queue ask /
   heartbeat claim against live GitHub before acting on or relaying it — git
   wins over heartbeat; heartbeats state superseded facts (superbot,
   superbot-next, websites, fleet-manager all evidenced).
3. **ORDER-completion rule:** an ORDER's truth is the status.md `orders:/done=`
   line or ANY later append-block marking it DONE — never the inbox header's
   `status: new` (append-only grammar; identical trap in fleet-manager,
   websites, substrate-kit).
4. **CI-reading rule:** judge CI by the named required/gate jobs, never the
   workflow-level conclusion (superbot-next golden-parity red-by-design; kit
   born-red holds); a green check that contradicts visible evidence is a bug in
   the *check* (Q-0120) — and a green checker does not prove the docs it
   validates were ever filled (product-forge U2).
5. **Session-card mechanics:** born-red card in the FIRST commit, flip
   `complete` as the deliberate LAST step — and know CI will NOT catch a
   forgotten flip everywhere (added-card advisory path, product-forge U4);
   `📊 Model:` family-level line required.
6. **Merge doctrine:** open READY, never draft; never merge/arm your own PR
   where the classifier wall applies — park READY+green and never retry a
   denial; always branch `claude/*` or auto-merge never arms.
7. **Ledger freshness ranking:** control/status.md outranks docs/current-state.md;
   current-state.md is a dated snapshot — verify in-flight claims live.
8. **Routine truth:** verify routine/trigger state by live list_triggers probe,
   never by status prose (kit's vanished-trigger evidence).
9. **Wall discipline:** capabilities are discovered, not assumed (check
   CAPABILITIES file → env → attempt once → record); never record "pushed"
   without ls-remote proof; don't re-probe documented owner-only walls.
10. **Cross-repo naming:** the only live fleet roster is fleet-manager
    `docs/roster.md` (fleet-manifest is a tombstone); prefix cross-repo file
    mentions with the repo name in prose (superbot check_docs trap).
11. **Security floor for new code:** any new state-changing HTTP route needs
    CSRF protection (token or Origin check) — Basic auth / OAuth session alone
    is not a CSRF defense (websites owner.py + mineverse precedent).

### (b) Per-Project specifics

- **superbot:** hub only, NO standing seat (Q-0264) — product work goes
  lane-side. Name THE single authoritative brief + SHA (three START-HEREs
  coexist). Front-load the minute-0 facts, don't point at the 79 KB ledger.
  Hermes surface is legacy — don't extend without owner word. Owner-click queue
  (Codex cap, 7/14 email, plugin seed, Stripe): don't re-verify. Python 3.10
  only: `python3.10 scripts/check_quality.py --full`.
- **superbot-next:** boot set = CONSTITUTION.md + control/status.md +
  README-first (nothing auto-loads). OWNER-ACTION 2 is stale —
  superbot-plugin-hello exists; close/advance ORDER 002. Red ≠ broken (gate
  job). Porting manual = named wave session cards (promote a trap index to
  docs/). Read the oracle from the LOCAL /home/user/superbot clone, never MCP
  full-file fetches. Counts: trust check_parity_depth output. Finish the
  #196/#206 claim next-step. Q-0120 on codex phantom commits.
- **websites:** treat review/ as the fourth service; run CI's full four-suite
  pytest line, not CLAUDE.md's snippet; queue a kit re-render. Check the latest
  review-bake run + stranded `bake/*` before trusting review stats. Fix the two
  /owner CSRF actions (shippable now). Fired sessions: check parked-chain +
  dry-backlog first; file a disarm/retarget ask.
- **substrate-kit:** working agreement = root CONSTITUTION.md. Registry roster
  is incomplete — verify against the actual fleet before claiming distribution
  complete. #220/#238 park open BY DESIGN — never arm, never close. DRIFT ≠
  ignore — classify each row. Never assert Q-0254 lives in all three templates.
  Minute-0 = CONSTITUTION → inbox → status ONLY.
- **fleet-manager:** roster-freshness red on `claude/*` = the stale-roster
  class — do NOT chase it; landing bot/roster-regen is coordinator/owner work.
  Boot list = CONSTITUTION → status/inbox → roster → owner-queue → playbook.
  Restructure stack #88/#89/#91 (+#92): parked — never merge/rebase/edit.
  Trust the newest heartbeat across main + open PRs (#97). Verify the payload
  landed — diff the merge (#47 lesson). Next free ORDER at HEAD, never a
  concrete number.
- **product-forge:** DARK — arm a wake before routing an ORDER (fleet-manager
  side must encode this). Truth = control/status.md + the archive-ready retro;
  IGNORE current-state.md; don't cite the journal. Landing recipe: arm in the
  gate-pending window / REST merge-on-green / flag on denial. One session per
  products/<slug>/ subtree. Heartbeat `updated:` from `date -u` +
  check-heartbeat.py. A superbot session must answer the phase-2 API proposal.

### (c) Not fixable by prompt — owner / tooling asks

**Owner clicks (settings/credentials):**
- Repo/org Settings → Actions → "Allow GitHub Actions to create and approve
  pull requests" — unblocks websites review-bake AND fleet-manager roster-regen
  (the roster time-bomb's root). Single highest-leverage click.
- product-forge Pages enable (OA-003). websites: botsite DATABASE_URL,
  control-plane GITHUB_TOKEN PAT (60 req/h ceiling), review/ Railway service,
  Discord OAuth app, scoped control-API token, Q-0004 ruling. superbot queue:
  Anthropic email by 7/14, Codex cap raise, Codex report reviews, Stripe keys,
  plugin-seed push (note: verify against the already-existing
  superbot-plugin-hello first), routine relaunch. superbot-next: AI key
  (OWNER-ACTION 5), update-branch ruleset (OWNER-ACTION 3), re-arm wake loop +
  fleet routines (OWNER-ACTION 6). Branch litter pruning / auto-delete head
  branches (403 walls everywhere). Answer: was the env teardown that
  auto-disabled 9 failsafes deliberate? (fm handoff §3.2). substrate-kit parked
  #220/#238 ratification.

**Kit/tooling work (buildable by sessions, mostly kit-side):**
- Fix `AGENT_ORIENTATION.md.tmpl` dead `.claude/CLAUDE.md` pointer + add a
  "pointer target exists live" check; render/install CLAUDE.md in
  superbot-next / product-forge / fleet-manager (fm's rides parked #92); a root
  CLAUDE.md for the kit repo itself.
- Adopter discovery: reconcile docs/fleet-repos.txt against the actual fleet;
  make the currency checker discover adopters instead of trusting the roster;
  severity-tier the DRIFT column.
- Close the added-card advisory loophole in substrate-gate (kit release);
  upgrade the 5-versions-behind adopters (product-forge 1.7.0, mineverse 1.8.0,
  idea-engine 1.10.0 → 1.12.1) so the false-green gate bug dies fleet-wide;
  fix the stuck session counter (verify whether 1.12.1 already does).
- Inbox grammar: an ORDER-status convention/checker that append-only doesn't
  break (fm §3.4). `verified-against: <sha>` stamps on heartbeat assertions
  (kit template change). check_docs cross-repo path awareness (superbot idea
  already filed). Re-tune or re-scope the fleet-manager 4h blocking
  roster-freshness policy. superbot compressed hub boot pack. idea-engine
  CLAUDE.md derivation fix (generated file — owner-gated there). superbot
  CLAUDE.md Q-0254 provenance correction (owner-gated — DISCUSS Q).
- Trigger hygiene: delete the retired-seat trigger (rides the parked stack);
  disarm-or-retarget the websites 4-hourly wake; reconcile routine-state
  records against the live registry.

---

*No secret values appear in this document. Model references are family-level
only. Census source files: 6 scratchpad census reports (superbot,
superbot-next, websites, substrate-kit, fleet-manager, product-forge),
2026-07-11/12 overnight program.*
