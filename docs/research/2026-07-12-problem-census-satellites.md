# Problem census — satellite repos (2026-07-12)

> **Status:** `historical` — dated snapshot (census night 2026-07-11→12); repos move on, verify against HEAD before acting.

> **Date:** 2026-07-12
> **Author:** fleet-manager research worker (overnight program: regression-proof startup prompts)
> **Scope:** superbot-games · superbot-idle · superbot-mineverse · gba-homebrew ·
> pokemon-mod-lab · venture-lab · trading-strategy · idea-engine · sim-lab ·
> superbot-plugin-hello · (one-paragraph checks) codetool-lab-opus4.8 ·
> codetool-lab-sonnet5 · codetool-lab-fable5
> **Method:** per-repo state / known problems / unknown problems / merge-readiness /
> prompt-implications, verified against git history (`origin/main` at HEAD) and CI
> runs at HEAD; PRs/Actions/repo metadata via GitHub MCP; read-only throughout.

Framing: the owner's 2026-07-11 restructure defines **8 standing seats** (Venture
Lab, SuperBot World, Game Lab, Ideas Lab, Self Improvement, SuperBot 2.0, Websites,
Fleet Manager — `projects/README.md` on `claude/restructure-roster`); the satellites
below fold into four of them. This census is the ground truth those new seat
prompts must be written against. The restructure PRs (#88–#91) are parked unmerged
at census time — that fact is itself ranked below.

## Executive summary

| Repo | Verdict | One-line why | Key citation |
|---|---|---|---|
| superbot-games | **STALE** | Heartbeat still instructs owner to merge 5 PRs already merged; 5 phantom claim files at HEAD | `control/status.md`@5ddfbee vs PRs #50–#55 merged 2026-07-11T20:25–20:43Z |
| superbot-idle | **FRESH** | Heartbeat (ARCHIVED-READY/dormant) matches reality; 0 open PRs, CI green | `control/status.md`@c6a349d; runs 29165729090/29165729081 |
| superbot-mineverse | **STALE** | Heartbeat says "IN FLIGHT: (none)" while green security PR #42 sits unmerged and nothing is armed to process it | `control/status.md`@76be821 vs PR #42 (head fff0caa, green) |
| venture-lab | **STALE** | Committed heartbeat declares ARCHIVE-READY at `e7e5c9f` while HEAD is `296a1a9` with 3 post-archive PRs (#56 merged, #57/#58 open) | `control/status.md@296a1a9` |
| trading-strategy | **FRESH (marginal)** | Heartbeat accurate at stamp; only benign lane-owed kit lag + open succession PR #64 | `control/status.md@ea22323` |
| gba-homebrew | **FRESH** | Heartbeat (session 23) matches git; only newer commit is declared-lane-owed kit bump | `control/status.md@d1ec24f` |
| pokemon-mod-lab | **FRESH** | Heartbeat matches git; ARCHIVE-READY / HONEST IDLE; R22 private-visibility check clean 20+ cycles | `control/status.md@08d2611` |
| idea-engine | **FRESH** | Heartbeat matches HEAD — but its CI gate exits 2 at HEAD (see rank 1) | `control/status.md@a9b41f6`; `scripts/preflight.py` exit 2 |
| sim-lab | **FRESH** | Heartbeat matches git (stamp future-dated ~27 min, minor); 11 verdicts finalized, CI green | `control/status.md@0622118`; run 29166034428 |
| superbot-plugin-hello | **DEAD (empty)** | Zero commits ever; owner created the repo 2026-07-10 and no agent noticed — the second leg of the handoff never fired | API `409 Git Repository is empty`; superbot-next `control/status.md:147-149@249ecaa` |
| codetool-lab-opus4.8 | **DARK** | Wound down 2026-07-09, not GitHub-archived (`archived: false`); salvage = succession pack + retro | last commit 80f6cd1 |
| codetool-lab-sonnet5 | **DARK** | Wound down 2026-07-09, not GitHub-archived; v0.1.1 tag/release never shipped | last commit 66c3dfc |
| codetool-lab-fable5 | **DARK** | Wound down 2026-07-09/10, not GitHub-archived; finished releases untagged (agents policy-blocked) | last commit a6cf1a9 |

**Headline negatives:** idea-engine's merge gate is broken at HEAD and nobody filed
it; the mineverse login-CSRF fix is green but parked with no merge path armed; the
idea-engine↔sim-lab generate→verify loop is fully stopped (PROPOSAL 010 sim-ready,
unpulled, both trigger sets dismantled); three of ten satellites boot on heartbeats
that contradict git; secrets hygiene is clean in all ten repos (verified negative);
none of the three "archived" labs is actually GitHub-archived.

## Top 10 satellite problems ranked by regression risk

Ranked by likelihood × blast radius **for the new seat prompts** — i.e. what will
actually bite a fresh seat booting on these repos.

**1. idea-engine's CI gate is broken at HEAD — every non-control PR opens permanently red.**
`python3 scripts/preflight.py` exits **2**: `check_sections` cannot parse fleet-manager
roster gen#9 `↳` sub-rows (introduced by fm PR #86/cddcb95, 25 minutes *after*
idea-engine archived). `substrate-gate.yml:96` runs exactly this preflight; heartbeat
and CI history still say green. Unfiled.
*Prompt implication:* Ideas Lab first wake runs preflight, expects the failure, and
fixes the parser (or pins `--file` to a saved roster copy) as PR #1, before any content work.

**2. Cross-track leak / public-exposure recurrence in Game Lab, plus R22 dilution.**
One merged seat holds Nintendo-derived content (pokemon-mod-lab, PRIVATE) and a
public repo (gba-homebrew) — one wrong-repo commit re-ships the 2026-07-10 incident
where the repo "has been PUBLIC the whole time" while 8 PR bodies asserted PRIVATE
(inbox ORDER 003 @08d2611). Guard today is prose + the per-session R22 API check,
which lives only in pml's inbox/status and dies if the merged prompt dilutes it.
*Prompt implication:* R22 verbatim — verify `visibility: private` via API every
session before ANY private-track work; never move Track A material (files, assets,
screenshots, hashes, PR-body descriptions) to any public surface.

**3. Mineverse login-CSRF fix (PR #42) parked while secrets provisioning could go first.**
The fix is green (runs 29172186988/29172187011) but the coordinator archived and
disarmed routines at 19:39Z, auto-merge-enabler **skipped** the `security/*` branch
(run 29172187017), and the heartbeat doesn't know the PR exists. The heartbeat's
top OWNER-ACTION is provisioning the six OAuth env vars — if the owner does that
first, sign-in goes live with a known login-CSRF hole (`server/auth.py`@76be821;
PR #42 body: "this PR GATES secret provisioning").
*Prompt implication:* SuperBot World's FIRST mineverse action = get #42 merged;
only then anything secrets-adjacent; then close-or-supersede #31.

**4. Trigger/wake succession dies at chat archive — fleet-wide class, already fatal twice.**
trading-strategy self-filed it ("both live triggers … DIE SILENTLY when that chat is
archived", `control/status.md@ea22323` ⚑ g); the fix PR #64 rebinds to a *new*
coordinator session — same fragility, fresher session, and its failsafe now "covers
both repos" (one archive kills both wake chains). Same class stopped the Ideas Lab
loop: PROPOSAL 010 sim-ready and unpulled, both coordinators archived, both trigger
sets dismantled (idea-engine ⚑ Q-0265; sim-lab `control/status.md@0622118`).
*Prompt implication:* every seat prompt carries its re-arm recipe (Q-0265 /
PLATFORM-LIMITS wake-recipe / status RE-ARM SPEC) and re-arms + records trigger IDs
at every coordinator handover; the 2026-07-17 grading pass must not be orphaned.

**5. Stale heartbeats + stale claims steer next wakes into an archived world.**
games: heartbeat instructs owner clicks already done + 5 phantom claim files;
venture-lab: committed heartbeat flatly wrong at HEAD (ARCHIVE-READY, wrong SHA,
wrong kit version); mineverse: heartbeat unaware of PR #42. The drift is structural
— kit-upgrade sessions may not touch status ("heartbeat bump is lane-owed"), so
every kit wave leaves the heartbeat lying until the next lane session.
*Prompt implication:* first action of any seat session = verify `control/status.md`
stamp against `git log origin/main -1` and live PR state; sweep terminal-state
claims on wake; heartbeat is a dated snapshot, never an order list.

**6. Venture-lab merge-authority split-brain strands green PRs.**
`docs/conventions.md@296a1a9` rule 2 says the lane "ALWAYS lands its own PRs" while
`docs/PLATFORM-LIMITS.md@296a1a9` documents 5+ verbatim classifier denials and the
proven working path (child builds to READY+green; coordinator merges under a genuine
owner turn). trading-strategy self-lands via MCP squash-on-green. Four green/open
PRs (#51, #57, #58, #64) already sit awaiting non-agent action; a merged Money-seat
prompt quoting either repo's convention verbatim breaks the other.
*Prompt implication:* per-repo merge-path table in the seat prompt — venture-lab:
never self-merge/arm, coordinator lands; trading-strategy: MCP squash-on-green is
the every-merge-to-date path.

**7. superbot-idle's 1131-test suite runs in no CI workflow.**
`grep pytest .github/workflows/*.yml` → no match; CI is kit gate + theme gate only.
`CONVENTIONS.md`@c6a349d makes pytest a *local* convention. Both siblings gate
merges on pytest; idle is the odd one out and nobody filed it — any future engine
regression merges green.
*Prompt implication:* before any merge in idle, run `python3 -m pytest -q` yourself;
better, first wake task = add a pytest gate workflow + ask owner to require it.

**8. Restructure PRs #88–#91 unmerged will re-break idea-engine's lane parser a second time.**
`check_sections.py` derives valid `ideas/<section>/` names from the live roster;
fm PR #88 folds the 12 lanes idea-engine's sections mirror into 8 seats. When
#88–#91 land, sections and parser both invalidate again (and `product-forge/` maps
to a seat awaiting owner disposition). A rank-1 fix that only patches the `↳` grammar
regresses at restructure-landing time.
*Prompt implication:* the parser fix must be written against the 8-seat roster
shape, and Ideas Lab's section list re-derived when #88–#91 merge — encode the
dependency, don't let two repos' schedules race silently.

**9. Venture-lab PR #51 photo exposure — 10 full-res sellable originals public (HOT, owner-only).**
Open since 2026-07-11T18:24Z on public branch `menno420-patch-1`; the archive-ready
retro flags "⚑ Close PR #51 + delete branch" (`docs/retro/archive-ready-2026-07-11.md@296a1a9`
line 22; originals "4080–11720px wide, up to ~10 MB", PR #52 body). Every day open
erodes the photo-packs product.
*Prompt implication:* not promptable (owner clicks) — but the seat prompt must keep
the ⚑ verbatim at top of queue and never invent a publish/fix path around it.

**10. superbot-plugin-hello is empty while superbot-next still lists its creation as *pending* — the stale-ask drift class.**
The owner clicked (repo created 2026-07-10T16:03Z, `409 Git Repository is empty`
ever since); the complete plugin package sits at superbot-next
`examples/superbot-plugin-hello/` "pending the owner-created repo"
(`docs/game-plugin-contract.md:9-10`), and superbot-next's OWNER-ACTION 2 was never
re-checked (~30h). Both Ideas Lab ledgers show one instance each of the same class.
*Prompt implication:* SuperBot 2.0 seat: move the example verbatim and clear
OWNER-ACTION 2. Fleet-wide: after filing an owner-click ask, re-check whether it
was satisfied at every wake.

---

## SuperBot World (superbot-games · superbot-idle · superbot-mineverse)

Method: local clones fetched (`git fetch origin`) and inspected at `origin/main`; PRs/CI via GitHub MCP. Read-only throughout — nothing committed, no comments, no PRs. All model names family-level. No secret values quoted anywhere.

### superbot-games
**Verdict: STALE** — heartbeat (`control/status.md`@5ddfbee, `updated: 2026-07-11T19:39:14Z`) still says "5 open PRs green+clean … the only gate is owner merge clicks", but all five (#50, #52, #53, #54, #55) were merged 2026-07-11T20:25–20:43Z, plus #58 at 22:29Z; open PRs today = 0.

#### State
- Default branch `main`, HEAD `5ddfbee` ("kit: upgrade substrate-kit v1.12.0 → v1.12.1 (#58)", merged 2026-07-11T22:29:02Z). Prior day: heavy burst — #49, #50, #51, #52, #53, #54, #55, #56, #57 all merged 2026-07-11.
- Heartbeat: `control/status.md` (phase "close-out + archive-prep"), plus two archived gen-1 lane heartbeats `control/status-mining.md` / `control/status-exploration.md` (both marked "⟵ GEN-1 HISTORY … do not resurrect the split").
- Drift specifics: the heartbeat's `⚑ OWNER-ACTION` block still instructs the owner to "Squash & merge the 5 open PRs (#50, #52, #53, #54, #55)" — all already merged. `control/claims/` still holds 5 claim files (`auto-balance-page.md`, `dnd-clamp-fuzz.md`, `dnd-scene-chaining.md`, `economy-cross-domain-sim.md`, `persistence-save-state-contract.md`) for those merged PRs — stale claims at HEAD 5ddfbee.
- Open PRs: **none** (list_pull_requests state=open → []).
- CI: healthy. Two workflows — `substrate-gate.yml` (kit gate, born-red session-card hold) + `tests.yml` (pytest, Python "3.x"). Latest main runs both success at HEAD 5ddfbee: run 29170576515 (substrate-gate), run 29170576518 (tests), 2026-07-11T22:29:05Z.

#### Known problems
- **Agent self-merge classifier-blocked; auto-merge deliberately NOT armed.** `control/status.md`@5ddfbee: "agent self-merge is platform-classifier-blocked; do NOT attempt". PR #51 body: "auto-merge deliberately NOT armed in this repo (#40 lesson)". Merge path = owner clicks. (Now cleared by the owner's merge sweep, but the mechanism stands for the next wake.)
- **Self-review (ORDER 004) central finding** — `.sessions/2026-07-11-order-004-self-review.md`@5ddfbee: "the merge-hold: five green PRs park ⚑ because the auto-mode classifier blocks agent self-merge…".
- **Open owner decision** — `control/status-mining.md`@5ddfbee: "⚑ OWNER-DECISION on the session-card model-line vs. no-id-in-artifacts conflict … only the formal ruling pending".
- **Open owner decision** — `control/status.md`@5ddfbee OWNER-ACTION item 2: transfer-policy source model (TRUE source-debit vs seeded-credit), `docs/design/persistence-design.md` §5, still undecided.
- **Wake routine not armed** — `control/status-mining.md`@5ddfbee: "routine: NOT ARMED — no scheduler tool available this session ('No such tool available: mcp__claude-code-remote__send_later')"; inbox ORDER 002 (arm hourly trigger) relies on seat-dependent tool availability.
- Parallel-PR floor-file churn: `tests/dnd/EXPECTED_MIN_TESTS.txt` collided across #50/#52 (both PR bodies document the rebase); heartbeat suggests a merge queue as optional owner action.

#### Unknown problems
- **Heartbeat + claims drift (headline, filed above as the verdict):** nothing in-repo records that the 5 PRs merged; a fresh session reading `control/status.md` at HEAD would re-ask the owner for clicks already done and see 5 phantom in-flight lanes in `control/claims/`.
- **No `.claude/` directory at all** (verified `git ls-tree -r origin/main`: only `.github/workflows/{substrate-gate,tests}.yml`) — no in-repo agent instructions or hooks; behavior depends entirely on external Project instructions + CONSTITUTION.md.
- `docs/current-state.md`@5ddfbee "Stability baseline" still cites "substrate-kit v1.2.0 engagement" while the repo is on v1.12.1 (baseline-section lag, minor).
- Spot-checks that PASSED: `games/shared/sim/economy_sim.py`, `docs/balance.md` + `tools/gen_balance.py`, `docs/design/persistence-design.md` all exist at HEAD as claimed by PRs #54/#55/#53.
- Secrets hygiene: clean — grep for token/key/secret/webhook patterns hits only test/game vocabulary and kit backup files (`.substrate/backup/bootstrap-*.py`, `.substrate/ci/auto-merge-enabler.yml` uses the standard GITHUB_TOKEN pattern). No hardcoded credential literals found.

#### Prompt implications
- Prompt must say: on wake, re-verify `control/status.md` open-PR/OWNER-ACTION claims against live GitHub before acting — the heartbeat is a dated snapshot that the owner's merge clicks outdate.
- Prompt must say: delete `control/claims/<branch>.md` files whose PRs are terminal (sweep on wake).
- Instructions must encode: merge path here is owner-click (self-merge classifier-blocked, auto-merge unarmed) — never burn turns retrying merges.
- Not promptable (needs owner/tooling): merge queue on main; scheduler-tool availability per seat; the model-line vs no-id-in-artifacts formal ruling.

### superbot-idle
**Verdict: FRESH** — heartbeat `control/status.md`@c6a349d (`updated: 2026-07-11T19:37:36Z`, "ARCHIVED-READY / dormant") matches reality: HEAD c6a349d is the heartbeat merge itself (PR #71, 2026-07-11), 0 open PRs, CI green.

#### State
- HEAD `c6a349d` "Merge pull request #71 … heartbeat: ARCHIVED-READY / dormant" (2026-07-11). 69+ lane PRs merged in ~2 days; suite grew 24 → 1131 tests (per heartbeat SHIPPED RECORD).
- Lane deliberately dormant: wake loop DISARMED (trigger `trig_01TWKGFW8RUsMvxUMt2ndzqA` deleted, with a written RE-ARM SPEC in the heartbeat); chat-only knowledge archived to `docs/retro/2026-07-11-lane-retro.md` + `docs/retro/2026-07-11-archive-ready.md` (PR #70).
- Open PRs: **none**.
- CI: latest main runs both success at HEAD c6a349d: run 29165729090 (substrate-gate), run 29165729081 (theme-gate), 2026-07-11T19:42:15Z. Auto-merge verified working here (heartbeat OA-001 "RESOLVED-VERIFIED": armed at creation, fired on green).

#### Known problems
- **PLATFORM-LIMITS.md@c6a349d is a whole catalogue of verified walls** (quotes): "Direct push to main post-seed: rejected"; "Auto-merge arming can fail BOTH ways on fast CI"; "Agent self-merge can be classifier-denied"; "403 on tag pushes / release creation / branch deletion"; "Toolsets are seat-dependent within one Project"; "Completed routine runs are not inspectable owner-side"; "PR can stall with ZERO check runs (mergeable_state: unknown …) — rebase, don't wait".
- Upstream blocks parked in heartbeat: SIM-001/Q-0264, PLUG-001 (plugin adapter evidence-blocked), KIT-001 — all external to this repo.
- ORDERs 000–002 all done (`orders: acked=000-002 done=000-002`).

#### Unknown problems
- **HEADLINE: the 1131-test suite is not run by any CI workflow.** `grep pytest .github/workflows/*.yml` → no match; CI = `substrate-gate.yml` (kit checks, system python3) + `theme-gate.yml` (`python tools/theme_gate.py themes` with pyyaml/jsonschema). `CONVENTIONS.md`@c6a349d line 17 makes pytest a *local* pre-push convention only. Its two siblings both gate merges on pytest (games `tests.yml`; mineverse `schema-gate.yml` required) — idle is the odd one out and nobody filed it.
- **No `.claude/` directory** at HEAD (same as games) — despite the system-prompt context in fleet sessions carrying an idle CLAUDE.md, none is committed in this repo (`git ls-tree -r origin/main` shows only the two workflows under `.github/`).
- Spot-checks that PASSED: `tools/simulate.py` exists; `tests/vectors/saves.v2.json` really contains 45 vectors (7 golden_v2 + 6 golden_v1_migration + 32 errors — matches the "45 vectors" claim); achievements layer exists as `idle_engine/achievements.py`.
- Python version pin is loose: substrate-gate uses system python3 + setup-python "3.x"; no interpreter pin anywhere for the (CI-absent) test suite.
- Secrets hygiene: clean — pattern hits are schema/theme vocabulary only; no credential literals.

#### Prompt implications
- Prompt must say: before any merge in idle, run `python3 -m pytest -q` yourself — CI will NOT catch test regressions (no pytest workflow); better: first task on wake is adding a pytest gate workflow + asking owner to require it.
- Prompt must say: treat PLATFORM-LIMITS.md as pre-verified walls — do not re-probe (its own header says so).
- Instructions must encode: the RE-ARM SPEC in `control/status.md` is the wake-loop recipe; verify via list_triggers after arming.
- Not promptable (needs owner/tooling): making a pytest check *required* on main is a repo-settings click.

### superbot-mineverse
**Verdict: STALE** — heartbeat `control/status.md`@76be821 (`updated: 2026-07-11T19:45:00Z`, "WRAPPED / ARCHIVED … IN FLIGHT: (none)") is contradicted by post-archive reality: security-fix PR #42 opened 2026-07-11T23:26Z (green, unmerged, and nothing is armed to process it — the coordinator's Routines were disarmed at 19:39Z per the same heartbeat).

#### State
- HEAD `76be821` "wrap-up: founding-day retro … final heartbeat (#41)", squash-merged by the owner 2026-07-11T19:46:19Z. Founding day: PRs #1–#40, 39 merged on green (heartbeat day-ledger).
- Open PRs (2):
  - **#31** "Add pre-provisioning security report (dormant OAuth + write path)" — owner's own Codex-generated report PR, opened 2026-07-11T16:41Z (~7h old), head 6e3d46a, base stale (4be012e, several merges behind).
  - **#42** "security: bind OAuth login to the browser (login-CSRF fix) + validate snapshots at ingestion" — opened 2026-07-11T23:26Z (<1h old at census time), branch `security/oauth-csrf-snapshot-validation`, head fff0caa, **green** (substrate-gate run 29172186988 success, schema-gate/pytest run 29172187011 success) — but auto-merge-enabler run 29172187017 **skipped** (the enabler only arms `claude/*` branches; a `security/*` branch will sit unmerged until someone clicks).
- CI: 3 workflows — `substrate-gate.yml`, `schema-gate.yml` (full pytest, Python **3.10** pinned, on PR + push to main), `auto-merge-enabler.yml`. **Anomaly: main HEAD 76be821 has ZERO workflow runs** — latest main-branch runs are at the previous commit a19e420 (runs 29165242207/29165242211, success, 19:25:54Z), and no run exists between 19:45:05Z and 23:26:32Z although both gates trigger `on: push: branches: [main]`. The PR head (b2b4f7b) was green at 19:45:05Z, so the content is almost certainly fine, but the merge commit itself is CI-unverified; cause not measured.
- Heartbeat quality otherwise high: structured ⚑ OWNER-ACTION (six env-var names), FLAG 1/FLAG 2 carry-verbatim specs for the bot lane, routines-disarm receipts with trigger IDs.

#### Known problems
- `control/status.md`@76be821: "⚑ needs-owner: 1 item — provision the six env vars to switch sign-in on … Also owner-side: review/merge your own open PR #31 (Codex security report); Builder-lane FLAGs 1+2 … stay informational until the manager picks them up; stage-5 live-prod flag remains owner-only."
- Everything remaining is externally blocked (bot-lane READ relay FLAG 1, WRITE endpoint FLAG 2, owner env vars) — by design, not by failure.
- `.sessions/2026-07-11-enforce-pytest-gate.md` + heartbeat line 5: pytest was made a required context on main and verified blocking on PRs #32–#35 (claim; branch-protection API not directly readable — PR #42 body says the same).

#### Unknown problems
- **`.claude/CLAUDE.md`@76be821 contradicts the code.** Its Architecture section still says "Three read-only layers … no database, no auth, no secrets anywhere in this repo" — while `server/auth.py` (OAuth, PR #11), `server/actions.py` (HMAC write path) and `docs/auth.md` all ship at HEAD. The kit banner says re-render after interview updates; nobody did. A fresh session booting on this file gets told auth doesn't exist.
- **Mineverse is the only repo of the three with `.claude/` at all** (CLAUDE.md + `settings.json` wiring 4 hooks to `/usr/bin/python3.10 bootstrap.py hook …`). Games/idle have none — hook behavior diverges silently across the future merged seat.
- Open PR #31's base is 4be012e (pre-#32 main) — its report doc `docs/pre-provisioning-security-report-2026-07-11.md` exists only on the Codex branch, not on main; if #42 merges first, #31 is historical and should be closed-or-rebased, but no doc says which.
- Spot-checks that PASSED: `docs/retro/archive-ready-2026-07-11.md`, `docs/ideas/founding-day-groomed-backlog-2026-07-11.md`, all three `schemas/*.v1.schema.json` exist at HEAD as the heartbeat claims.
- Secrets hygiene: clean — `server/auth.py`/`server/actions.py` reference env-var *names* only (e.g. lines `ENV_CLIENT_SECRET = "DISCORD_OAUTH_CLIENT_SECRET"`, `ENV_SECRET = "MINING_WRITE_SHARED_SECRET"`); the test shim's fallback literal is self-labelled `"shim-dev-secret-not-a-secret"` (`tests/shim/shim_bot.py` line 423). No real credential material committed.

#### OAuth login-CSRF (mandatory item)
- **Where:** `server/auth.py`@76be821 — `make_state` (lines 158–169) mints an HMAC-signed, 10-min-TTL, nonce-carrying state token; `verify_state` (lines 171–173) checks only signature+TTL+purpose. `build_authorize_url` (lines 209–216) passes it to Discord. `/auth/login` sets **no cookie**, and the callback in `server/app.py` trusts the bare state — so any valid state works from **any** browser (classic login-CSRF: attacker-initiated login can be completed in a victim's browser). `docs/auth.md`@76be821 even documents the design: "No server-side store — the signature is the state."
- **Documented?** Yes, twice: owner's Codex audit PR **#31** (finding: "OAuth `state` not bound to the initiating browser"), and the fix PR **#42** which cites it as "a login-CSRF hole". Also indirectly in `.sessions/2026-07-11-discord-oauth.md` (original design rationale, no vulnerability awareness).
- **Exploited/broken in practice?** No — OAuth is **dormant**: the six env vars are unprovisioned, the site runs degraded read-only/anonymous (heartbeat OWNER-ACTION 1), so there is no live attack surface yet.
- **"Fixed" means:** PR #42 (head fff0caa, both gates green) merges to main — `/auth/login` sets an HttpOnly+SameSite=Lax cookie carrying a keyed HMAC binding of the exact state, `/auth/callback` requires it and `hmac.compare_digest`-verifies before any Discord call — **before** the owner provisions the six OAuth/write secrets. PR #42's own body states this ordering ("this PR GATES secret provisioning"), matching the coordinator constraint: **fix lands before any secrets work in this repo.**
- **Operational catch:** the fix is parked — coordinator archived + Routines disarmed at 19:39Z, and auto-merge-enabler skipped the `security/*` branch (run 29172187017). Someone (owner or the merged seat) must merge #42 explicitly; the heartbeat doesn't know it exists.

#### Prompt implications
- Prompt must say: FIRST action in mineverse = get PR #42 merged (it is green; owner click or explicit merge turn), and only after that touch anything secrets-adjacent; then close-or-supersede #31.
- Prompt must say: re-render/fix `.claude/CLAUDE.md` (bootstrap render) so the architecture section stops denying auth exists.
- Prompt must say: treat main-HEAD CI absence as "verify before building on top" — check the last commit's check runs, don't assume push-runs exist.
- Not promptable (needs owner/tooling): provisioning the six env vars; the auto-merge-enabler's `claude/*`-only branch filter (workflow change, kit-owned).

#### Seat merge-readiness: SuperBot World
Concrete frictions the merged seat prompt must absorb:

1. **Three merge paths, all different.** games: auto-merge deliberately unarmed + agent self-merge classifier-blocked → owner-click only (status.md@5ddfbee, PR #51 body). idle: auto-merge armed-at-creation, verified firing (OA-001), with documented both-ways arming failures (PLATFORM-LIMITS.md). mineverse: `auto-merge-enabler.yml` workflow, but only for `claude/*` branches (PR #42 skipped). A single "open PR then X" instruction is wrong in at least two repos.
2. **Three CI shapes.** games: substrate-gate + tests.yml (pytest, "3.x"). idle: substrate-gate + theme-gate, **no pytest in CI**. mineverse: substrate-gate + schema-gate (pytest, pinned **3.10**) + enabler. "Green CI" means different assurance levels per repo.
3. **Heartbeat grammar diverges.** games `control/status.md` (+ two archived per-lane status files that must not be resurrected — status-mining.md header), idle single status.md with SHIPPED RECORD/ROUTINE RECORD/OA-blocks, mineverse status.md with kit/engaged fields + FLAG-carry-verbatim blocks. A merged seat needs one canonical heartbeat home and explicit "the other two are archives" language, or three writers will drift.
4. **`.claude/` asymmetry.** Only mineverse commits CLAUDE.md + settings.json hooks (pinned to `/usr/bin/python3.10`); games/idle have none. Session behavior (hooks, orientation) silently changes depending on which repo the seat cd's into — and mineverse's CLAUDE.md is factually wrong about its own architecture.
5. **Claims conventions.** games uses `control/claims/<branch>.md` (currently 5 stale post-merge), idle used control/claims (cleaned), mineverse "control/claims/ contains only its README". Merged seat needs one claims dir + a terminal-state sweep rule.
6. **Both dormant repos disarmed their wake loops with re-arm recipes in different places** (idle: status.md ROUTINE RECORD; mineverse: heartbeat notes + retro) — the merged seat prompt must point to both re-arm specs, or the seat wakes blind.
7. **Cross-repo dependency direction:** mineverse's FLAG 1/2 target the superbot bot lane, games' persistence waits on a superbot-next games-persistence decision (id stamped at its one fleet-manager home, the superbot-world custom instructions in `docs/prompts/v3/per-project/`) — the merged seat will carry inter-repo blocks it cannot clear itself; needs an explicit "externally-blocked ≠ actionable" list.

#### Top regression risks (this slice)
1. **Mineverse login-CSRF fix (PR #42) rots unmerged** — repo archived, routines disarmed, auto-merge skipped its branch, heartbeat unaware; if the owner provisions the six OAuth secrets first, sign-in goes live vulnerable.
2. **Idle's 1131 tests run in no CI workflow** — any future merge is gated only by kit/theme checks; a real engine regression lands green.
3. **Games heartbeat + 5 stale claim files instruct actions already done** — next wake re-asks for merged-PR clicks and sees phantom in-flight lanes (drift class the fleet's own Q-0166 calls fix-on-sight).
4. **Mineverse main HEAD (76be821) has zero workflow runs** — push-gates silently didn't fire on the merge commit; building on an unverified HEAD normalizes CI blind spots.
5. **Merged-seat convention collisions** (merge path, heartbeat grammar, .claude presence) — a single-prompt seat applying one repo's rules to another (e.g. arming auto-merge in games, trusting CI in idle) fails in ways each repo has already individually documented.

---

## Venture Lab (venture-lab · trading-strategy)

Method: local clones fetched (`git fetch origin`), all reads against `origin/main` (venture-lab HEAD `296a1a9`, trading-strategy HEAD `ea22323`) + GitHub MCP for PRs/Actions. READ-ONLY throughout. Important context discovered during the census: **the seat merge is not future — it already happened.** Both open heartbeat PRs record "the merged **Money seat** (venture-lab + trading-strategy, owner decision 2026-07-11)" (venture-lab PR #58 body; trading-strategy PR #64 body). The census prompt's "future seat" framing is one day behind the repos.

### venture-lab

**Verdict: STALE** — heartbeat at HEAD (`control/status.md@296a1a9`) declares "**ARCHIVE-READY, idle**" with "**HEAD at write:** `e7e5c9f`", but HEAD is `296a1a9` (PR #56, kit v1.12.1, merged 2026-07-11T22:29Z) and three post-archive PRs exist (#56 merged, #57 + #58 open). The correcting heartbeat is PR #58 (open, born-red, unmerged, opened 23:23Z) — until it lands, the committed heartbeat contradicts git history.

#### State
- Last commits on `origin/main`: `296a1a9` 2026-07-12 (merge of PR #56 kit v1.12.1) ← `2044dc6` (#55 archive close-out) ← `e7e5c9f` (#54) ← `389bb37` (#53) ← `dfe3332` (#52 photo previews), all 2026-07-11. High velocity: PRs #44–#56 all merged 2026-07-11.
- Heartbeat: `control/status.md` (lane-written, overwritten wholesale). Stamp `updated: 2026-07-11T19:37:09Z`, `status: green`. Stale in three specifics at HEAD: phase (ARCHIVE-READY vs. active Money seat), `kit heartbeat: kit: v1.10.1` (HEAD is v1.12.1 via #56), and the archive note saying failsafe cron `trig_01X1dw1L1Udgt8atzzNWEJic` is "pending deletion" (PR #58 body says the live triggers are now different ones).
- Open PRs (3): **#51** "Add files via upload" (owner-authored, opened 2026-07-11T18:24Z) — the ⚑ HOT photo-exposure branch, 10 full-res sellable originals public (see Known problems); **#57** OWNER LAUNCH HOUR packet (opened 22:30Z, READY + 3 checks green on head `ed6bbd6`, deliberately **PARKED — owner-merge only**); **#58** Money-seat heartbeat re-stamp (opened 23:23Z, born-red by design, awaiting flip/merge).
- CI: two workflows, `kit-tests` + `substrate-gate`. Latest main runs both **success** at HEAD `296a1a9` (runs 29170588402 / 29170588422, 2026-07-11T22:29Z). `substrate-gate` became a **required check** on 2026-07-11 (`docs/PLATFORM-LIMITS.md@296a1a9`, "Merge wall re-verified on PR #55 (substrate-gate now a REQUIRED check)").

#### Known problems
- **Photo exposure (HOT, unactioned):** `docs/retro/archive-ready-2026-07-11.md@296a1a9` line 22: "**⚑ Close PR #51 + delete branch `menno420-patch-1`** — photo exposure: 10 [full-res originals…]". PR #52 body confirms: originals "4080–11720px wide, up to ~10 MB" at repo root of a public repo — the sellable product itself. PR #51 is still open.
- **Token-budget misses, 3 of 4 metered builds** — `control/status.md@296a1a9` § NEGATIVES: "Stripe Webhook Test Kit: ~284k vs 120k cap (~2.3×)… Agent Fleet Field Manual: ~200k vs 90k cap (~2.2×)… photo-packs: ~93.8k vs 80k cap (~1.2×)… A cap that is silently exceeded three times out of four is not a cap." Forward rule already named: caps must include research + CI overhead; report metered usage.
- **Merge wall — self-merge classifier denials (recurring, 5+ verbatim captures):** `docs/PLATFORM-LIMITS.md@296a1a9` — "[Self-Approval]… Merge Without Review" walled PR #9 twice (2026-07-10), the ORDER 004 repair PR twice, and PR #15 three times (2026-07-11). "ROOT CAUSE: relayed authorization is never genuine in a child seat. WORKING PATH (proven): child builds PR to READY + CI-green; the coordinator seat executes the squash-merge under the owner's genuine-user turn." This **directly contradicts** `docs/conventions.md@296a1a9` rule 2 ("This lane ALWAYS lands its own PRs — written grant") — the binding conventions file encodes a path the platform demonstrably walls.
- **Owner-gated publish queue frozen on clicks:** all 4 sellable products UNPUBLISHED, sell-clicks are owner ⚑ (⚑B $49, ⚑D $19, ⚑E $29, ⚑F $39) plus ⚑A (Stripe test keys), ⚑G (GitHub Pages) — `docs/retro/archive-ready-2026-07-11.md@296a1a9` lines 22–35. Revenue base case in PR #57 body: "**BASE CASE = 0 sales** (no distribution channel wired) → payback **INDEFINITE**. Distribution is the real gap."
- **Stale codex PR disposition:** ⚑ "Disposition PR #38" (archive-ready line 24) — resolved: #38 closed unmerged 2026-07-11T19:58Z (superseded by merged #49 fail-closed hotfix, per PR #58 body). The archive-ready doc at HEAD still lists it as open owner work — minor doc drift.
- **Wake-chain not re-armed at archive:** `control/status.md@296a1a9` § Archive note — "Pacemaker wake chain is **NOT re-armed** at archive… a fresh session re-arms the wake chain per ORDER 002." PR #58 claims three live triggers now exist, but that record is unmerged.

#### Unknown problems
- **No root `CLAUDE.md`, no `.claude/settings.json`** at HEAD (`git ls-tree origin/main` — root has `CONSTITUTION.md`, kit template lives at `.substrate/claude/CLAUDE.md` only). Session behavior is steered entirely by kit files + inbox — nothing repo-committed configures the harness. Same in trading-strategy, so at least the gap is symmetric.
- **Heartbeat-vs-HEAD drift is structural**, not incidental: status is "overwritten wholesale each session" but kit-upgrade sessions are forbidden to touch it ("heartbeat bump is lane-owed", PR #56 body) — so every kit wave leaves the committed heartbeat lying about kit version until the next lane session. Observed twice (kit line stale at v1.10.1 now; trading-strategy's was "stale at v1.7.1 since PR #44", its status admits).
- **Secrets hygiene: CLEAN.** Grep at `origin/main` for Stripe/AWS/GitHub/Slack key patterns and private-key blocks found only clearly-fake test values (`candidates/membership-kit/server/test_http_realpath.py` — "whsec_ fake TEST value", "sk_test_ fake TEST value") and placeholder docs (`candidates/stripe-webhook-test-kit/README.md` — `whsec_your_signing_secret`). Env var **names** only, per the repo's own rule. Negative finding, verified.
- **DONE-claim spot-checks pass:** all four claimed dist artifacts exist at HEAD (`candidates/membership-kit/dist/membership-kit-v0.2.zip`, `candidates/stripe-webhook-test-kit/dist/…v0.1.zip`, `candidates/template-packs/dist/…v0.1.zip`, `candidates/agent-fleet-field-manual/dist/…v0.1.{html,zip}`). Non-author verification of the test kit is recorded in status ("Ran 14 tests in 3.033s / OK").
- **No telemetry ledger:** trading-strategy commits `telemetry/model-usage.jsonl`; venture-lab has none despite its heavier token-budget pain — the repo measuring budgets worst has no committed usage ledger.

#### Prompt implications
- Merge wall → **prompt must say: children never self-merge or arm auto-merge in venture-lab; land via the coordinator's squash-merge under a genuine owner turn (PLATFORM-LIMITS working path); PARK label = owner-merge only.**
- Heartbeat drift → **prompt must say: first action of any seat session is verify `control/status.md` stamp against `git log origin/main -1` and re-stamp if it lags; kit-upgrade sessions leave a lane-owed heartbeat debt — pay it.**
- Token budgets → **instructions must encode: intake caps include research + CI overhead; report metered usage; 3-of-4-over-cap is the base rate to plan against.**
- Photo exposure / publish clicks / Pages / Stripe keys → **not promptable (needs owner clicks); prompt must keep the six-field ⚑ queue verbatim and never invent a publish path.**
- Missing root CLAUDE.md/settings → **not promptable alone (owner/tooling: kit follow-up); prompt should note session config is kit+inbox only.**

### trading-strategy

**Verdict: FRESH (marginal)** — heartbeat `control/status.md@ea22323` stamped 2026-07-11T19:33:12Z is accurate against git history at its stamp; the only lag is benign newest-merge lag (kit line says v1.12.0, HEAD `ea22323` is PR #63's v1.12.1 — a merge type whose heartbeat bump is explicitly "lane-owed") plus one open succession PR (#64). No claim in it contradicts the tree.

#### State
- Last commits on `origin/main`: `ea22323` 2026-07-12 (#63 kit v1.12.1) ← `d3ae8f4` (#62 archive-ready close-out) ← `2dd955d` (#61 v1.12.0) ← `3172b43` (#60) ← `ed8add3` (#59 ORDER 010 self-review), all 2026-07-11. PRs #55–#63 merged same day.
- Heartbeat: `control/status.md` — dense key:value grammar (`updated:` / `phase:` / `health:` / `orders:` / `⚑ needs-owner` / `next-update-by:`). Claims verified: "health: green — full suite 223 passed"; "0 open PRs" was true at its stamp (PR #64 opened later, 23:15Z); "orders: acked=001–010, done=001–010" consistent with inbox (ORDER 010 is the newest); holdout SPENT with 13 rows.
- Open PRs (1): **#64** succession heartbeat (opened 2026-07-11T23:15Z) — re-arms the weekly grading cadence (new trigger `trig_015aNMg5ncoSE2Roe4MKjQnr`, cron `0 9 * * 5`, next 2026-07-17T09:05Z) and marks ⚑ (g) resolved. Body: "Merge is an owner/non-author action." Unmerged — the on-main record still says the grading pass has NO executor.
- CI: two workflows, `tests` + `substrate-gate`. Latest main runs both **success** at HEAD `ea22323` (runs 29170711495 / 29170711497, 2026-07-11T22:33Z).

#### Known problems
- **⚑ (g) trigger succession (top risk, self-filed):** `control/status.md@ea22323` routine-state: "⚠ SUCCESSION RISK — both live triggers are bound to the coordinator session session_01NwvvbgUVSdQvY8eYwtuEoo and DIE SILENTLY when that chat is archived… the 2026-07-17 grading pass and inbox watching then have NO executor." Fix is in open PR #64, but its replacement triggers are again bound to a (new) coordinator session — the fragility class is unchanged, only the session is fresher.
- **⚑ (c) auto-merge toggle OFF:** status — "auto-merge arm fails pending-side with 'unstable status' while the repo toggle is off, so every merge needs an agent to poll-and-merge (reconfirmed on PR #36)." Owner click never done; every merge to date is MCP squash-on-green.
- **⚑ (b) env setup script not saved:** "fresh-environment sessions die silently at provision without it" — owner paste of `environments/setup-universal.sh` into the environment config, still pending.
- **⚑ (f) post-2026 OOS protocol proposal** — decision-only owner item; 5 dev-candidates are dev-only forever without it. "flag-only, this item never self-executes."
- **⚑ (d) dead gen-1 session** still listed active in the project UI (cosmetic).
- **Direct push to main blocked by ruleset** (PR #56 body: "Direct push to main is blocked by repository rules, hence this micro-PR") — claims-release housekeeping costs a full PR cycle each time.

#### Unknown problems (incl. live-trading remnant inventory)
- **Live-trading remnants at HEAD: NONE — verified negative.** `requirements.txt@ea22323` line 1: "# Pinned research-lab dependencies… **Research only — no broker libs.**" (pandas, numpy, yfinance, requests, pytest only). Grep across `src/` + `scripts/` for `ccxt|binance|alpaca|coinbase|kraken|place_order|create_order|submit_order|live_trad|api_secret` → zero order/exchange-write code (sole hit: a comment in `src/trading_lab/data.py`; data flows read-only via yfinance). The "paper lane" is a **git-committed mock ledger** — `experiments/paper/ledger.md@ea22323`: "**No real money, no brokerage account, no order, no API — ever.**" — graded weekly by `scripts/grade_paper.py` at simulated t+1-open fills with costs. The research-only pivot is already **binding in-repo** (`docs/paper-lane-protocol.md` BINDING per status; holdout SPENT, promotion CLOSED, the only promotion path is owner-gated). The seat prompt fences a wall that is already built — it must keep it built.
- **Kit-version heartbeat drift (recurring class):** kit line at HEAD says v1.12.0; HEAD is v1.12.1 (#63). The same status line admits the same line "was stale at v1.7.1 since PR #44". The class recurs because kit sessions may not touch status.
- **Secrets hygiene: CLEAN.** Grep at `origin/main` (excluding kit machinery) for key patterns and `api_key|API_KEY` → zero hits. No exchange credentials exist because no exchange integration exists.
- **DONE-claim spot-checks pass:** `PAPER_LANE_START = "2026-07-11"` pinned in `src/trading_lab/config.py@ea22323` ("Do not change this constant") ✓; `HOLDOUT_START = "2025-01-09"` locked ✓; paper-0001 WATCH row present in `experiments/paper/ledger.md` ✓; 223-test suite + both workflows green at HEAD ✓.
- **Root `CLAUDE.md` missing — and self-known:** status notes: "kit lane-owed follow-ups (2) live root CLAUDE.md, (3) CAPABILITIES landing-constraints entry, (4) AGENT_ORIENTATION v1.12.0 manual merge remain PARKED." No `.claude/settings.json` either (`git ls-tree` empty).
- **Telemetry model-attribution drift (minor):** early `telemetry/model-usage.jsonl` rows say `"model": "claude-agent"` (pre-ORDER-009); newest rows are family-level (`fable-5`) — compliant going forward, historic rows unfixed.

#### Prompt implications
- Research-only rail → **prompt must say: no broker libs, no order/exchange-write code, no live API config — ever; holdout is SPENT (no re-runs, no new windows); paper lane touches only `load_paper_ohlcv`; the only promotion path is an owner-gated pre-registered protocol (⚑ f).**
- Trigger succession → **not promptable alone (needs owner/tooling: a session-independent Routine or owner-owned cron); prompt must still say: at every coordinator handover, re-arm the weekly grading trigger and record trigger IDs in `control/status.md`.**
- Weekly grading deadline → **prompt must say: `next-update-by` 2026-07-17T23:59Z grading pass via `scripts/grade_paper.py` per protocol §6–§7; late is tolerated, never is not.**
- Auto-merge OFF / push blocked → **prompt must say: land via MCP squash-on-green (the every-merge-to-date path); micro-PRs for claims housekeeping are normal.**
- Kit-heartbeat drift → **instructions must encode: kit upgrades leave a lane-owed status bump; pay it in the next lane session.**

#### Seat merge-readiness: Venture Lab (one seat, two repos)
The merge is already decided and partially executed (Money seat, owner decision 2026-07-11; PR #58 + #64 are its first artifacts, both open). Concrete friction the merged seat prompt must handle:
1. **Divergent merge paths (the sharpest edge):** trading-strategy lane self-lands via MCP squash-on-green (#55–#63 precedent, auto-merge toggle OFF, ⚑ c); venture-lab children are classifier-walled from any self-merge/auto-merge-arm (5+ verbatim denials, `docs/PLATFORM-LIMITS.md@296a1a9`) and land only via coordinator merge under a genuine owner turn — and venture-lab's own binding `conventions.md` rule 2 still asserts the opposite ("ALWAYS lands its own PRs"). A merged prompt quoting either repo's convention verbatim breaks the other repo.
2. **Divergent heartbeat grammars:** venture-lab `control/status.md` is section-prose (NEGATIVES / Ledger / Archive note / six-field ⚑); trading-strategy is strict key:value with `next-update-by` and orders acked/done lines. Two files, two grammars, one writer-seat — the prompt must name both formats or the seat homogenizes one and breaks its parser/reader expectations.
3. **Colliding ORDER namespaces:** both repos have independent `control/inbox.md` sequences (venture-lab ORDER 001–006; trading-strategy ORDER 001–010). "ORDER 005" is ambiguous in a merged seat — prompt must always qualify orders repo-first.
4. **Different CI/required checks:** venture-lab = `kit-tests` + `substrate-gate` (substrate-gate REQUIRED since 2026-07-11); trading-strategy = `tests` (pytest, 223) + `substrate-gate` (NOT a required check; merges happen on observed green, toggle OFF). Same gate name, different enforcement level.
5. **Different risk constitutions:** trading-strategy has hard scientific rails (holdout SPENT, paper-lane data rail, pre-registration, significance bar) where an eager venture-lab-style "build and ship" instinct is the threat; venture-lab has owner-click/publish/spend rails where a cautious trading-style "never act" instinct stalls revenue. One prompt, two opposite default postures — must be scoped per-repo, not per-seat.
6. **Different languages/tooling:** trading-strategy is a typed Python package (`src/trading_lab`, pyproject, pytest) with committed data + experiment artifacts; venture-lab is markdown-products + stdlib scripts + per-candidate unittest suites. Verification commands differ per repo (pytest -q + check --strict vs. per-candidate unittest + check --strict).
7. **Shared trigger budget:** both repos' cadences now hang off one Money-seat coordinator session's triggers (PR #64 body: failsafe `trig_017o6azZTd9pzcaSthEncT5q` "covers both repos") — a single archive event now kills BOTH repos' wake chains simultaneously. Higher blast radius than pre-merge.

#### Top regression risks (this slice)
1. **Trigger succession dies again:** all cadence triggers (incl. the 2026-07-17 grading pass executor) are bound to the current coordinator session; one chat archive silently kills both repos' wake chains — the exact failure both repos already documented once (status ⚑ g; venture-lab archive note).
2. **Merge-authority split-brain strands PRs:** a merged-seat agent following venture-lab `conventions.md` self-merge grant gets classifier-walled (or, worse, follows trading-strategy's self-land habit into a repo where it's denied), leaving green PRs open — #51, #57, #58, #64 are already 4 open PRs awaiting non-agent action tonight.
3. **PR #51 photo exposure remains public:** 10 full-res sellable originals on an open public branch since 2026-07-11T18:24Z, HOT ⚑, owner-only fix — every day open erodes the photo-packs product.
4. **Research-rail erosion under the merged seat:** venture-style throughput pressure in trading-strategy touching holdout/paper-lane files (holdout SPENT is irreversible; one wrong re-run invalidates the program's integrity claims).
5. **Heartbeat drift normalizes:** both status files structurally lag kit merges and seat pivots (venture-lab's is flatly wrong at HEAD right now); a seat prompt that trusts `control/status.md` over `git log` will act on an archived-world model.

---

## Game Lab (gba-homebrew · pokemon-mod-lab)

Read-only census, 2026-07-11 (local clones fetched; origin/main inspected). All citations are `file@sha` on origin/main, PR#, or CI run id.

### gba-homebrew

**Verdict: FRESH** — heartbeat `control/status.md@d1ec24f` stamped 2026-07-11T21:03:45Z (session 23) matches git reality: newest merge is PR #59 (kit v1.12.1) at `d1ec24f` 2026-07-12 00:29 (+0200), the only newer-than-stamp commits are that kit-upgrade PR (benign lag, explicitly declared lane-owed in PR #59 body).

#### State
- **Repo:** PUBLIC (`visibility":"public"`, GitHub API 2026-07-11). Default branch `main`; only branch on origin is `main` — zero stale refs.
- **Heartbeat:** `control/status.md@d1ec24f` — section-preserving lane write ("appends the shepherd section at file end only; every Gloamline/Brineward/Lumen-Drift section above remains session 20/21's record"). Phase: Gloamline slice 5 (barricades) SHIPPED + Brineward walking skeleton SHIPPED + owner archive-prep executed; durable hand-off = `docs/retro/archive-ready-2026-07-11.md` and `docs/retro/archive-ready-2026-07-11-brineward.md`.
- **History:** ~23 sessions in 2 days; last substantive game PRs #52–#56 (Gloamline skeleton/shove-waves/barricades, Brineward concept/skeleton) all merged 2026-07-11; then hourly-wake heartbeats #57, #58 and kit upgrade #59.
- **Open PRs:** zero (PRs #52–#59 all merged; last merged 2026-07-11T22:29Z).
- **CI:** two workflows on main — `ROM builds` (rom-builds.yml, builds all `games/*/Makefile` ROMs, devkitARM/BlocksDS) and `substrate-gate`. Latest main runs both **success** at HEAD `d1ec24f` (run 29170585644 ROM builds, 29170585659 substrate-gate, 2026-07-11T22:29Z). A third workflow `headless-boot.yml` exists in the tree.
- **Deliverables verified at HEAD:** `dist/gloamline.nds` sha256 recomputed from the blob = `25ae4f81…` and `dist/brineward.nds` = `89e68dc2…` — both **exactly match** the claims in `dist/README.md@d1ec24f` and PR #55/#56 bodies. Shipped-claim spot-check passes.

#### Known problems (filed by the lane itself)
- **Auto-merge fires before NDS builds are green:** required-check set is the GBA "ROM builds" job only, "so an armed auto-merge merges the moment that job goes green … footgun. Discipline until the owner adds `NDS ROM build` to the required checks (⚑ queued in `control/status.md`)" — `docs/PLATFORM-LIMITS.md@d1ec24f` (lines ~44–49). Owner-click pending.
- **Self-approval classifier wall:** arming auto-merge hits the "[Self-Approval]…Merge Without Review" classifier on some surfaces — `docs/PLATFORM-LIMITS.md@d1ec24f` line ~34.
- **External publishing owner-gated:** "External publishing of Track B (itch.io, forums, anywhere) still requires an owner action — queue it under ⚑ needs-owner, never perform it" — `README.md@d1ec24f`.
- Owner-gated queue (archive-ready retro): playtest verdicts on shipped slices; next-slice picks. Lane is otherwise in "expand the games" standing-directive mode (owner directive quoted verbatim in `control/status.md@d1ec24f`).

#### Unknown problems (nobody filed)
- **Session-card gaps:** `.sessions/` has sessions 1–11 and 15–21 but **no cards for 12–14, 22, 23** (`git ls-tree origin/main .sessions/`); sessions 22/23 exist only as PR bodies (#57, #58). The `📊 Model:` ground-truth order (inbox ORDER 003 @d1ec24f: "in its committed session card") is being satisfied in PR bodies instead of committed cards for wake sessions — nobody filed this mismatch.
- **Model-name format drift:** PR #57 body says `📊 Model: claude-sonnet-5`, PR #58 says `sonnet-5` — family-level rule (Q-0262) met, but grammar is inconsistent across sessions.
- **No `.claude/settings.json` / CLAUDE.md at repo root** — only `.substrate/claude/CLAUDE.md` and `.substrate/hooks/settings.template.json` exist at `d1ec24f`. Hooks are template-only, not installed; the merged seat cannot assume harness-enforced guards here.
- **Committed binaries in a public repo** (`dist/*.nds`, `dist/*.gba`) are declared publish-safe-by-construction (`dist/README.md@d1ec24f`) and are original homebrew — consistent, but this is exactly the pattern that must NEVER appear in the merged seat's private-track work, and the habit lives in the same lane brain.
- **Secrets:** grep for token/key patterns (ghp_/github_pat_/AKIA/PRIVATE KEY) over origin/main — zero hits. Clean.
- **Track-isolation exposure (public side):** `README.md@d1ec24f` lines 8–17 publicly names `menno420/pokemon-mod-lab` as "Track A, PRIVATE … contains Nintendo-copyrighted material"; `control/status.md@d1ec24f` and session cards 8/9/15 also reference the pokemon-mod-lab track by name. No Track A code/assets found in this tree (games/ are original C/C++; no pokeemerald/pret/baserom file paths), but the public repo **advertises the existence and nature of the private ROM-hack repo**.

#### Prompt implications
- Prompt must say: after any merge, verify the post-merge main `NDS ROM build`/full CI run green — auto-merge only waits on the GBA "ROM builds" required check (not promptable away: adding required checks is owner/ruleset tooling).
- Prompt must say: every fired session (including bare wakes) commits a session card with the `📊 Model:` family line — PR-body-only attribution is drift.
- Instructions must encode: dist ROM refresh = same-PR provenance row (size + sha256 + source-tree statement) in `dist/README.md`, byte-determinism double-build.
- Not promptable (needs owner): add `NDS ROM build` to required checks; external publishing of Track B.

### pokemon-mod-lab

**Verdict: FRESH** — heartbeat `control/status.md@08d2611` stamped 2026-07-11T21:03:45Z (session 044) matches git: newest merge PR #52 (kit v1.12.1) at `08d2611` 2026-07-12 00:29 (+0200); only-newer commit is that declared-lane-owed kit bump. Phase is explicitly **ARCHIVE-READY / HONEST IDLE** — all real work owner-gated.

#### State
- **Repo:** PRIVATE (`"private":true`, GitHub API 2026-07-11) — and the lane re-verifies this **every session** (R22 guard: "visibility: private — verified 2026-07-11T21:03Z via `list_repos`", `control/status.md@08d2611`).
- **Content:** full vendored **pret/pokeemerald decomp** (11,557 files under `pokeemerald/`, incl. 5,729 graphics + 1,303 sound files — extracted Nintendo-copyrighted assets) plus the `agbcc` compiler tree. No `baserom.*` committed; `pokeemerald/.gitignore` excludes `*.gba`; **no built ROM binaries anywhere** (only map `.bin` layout data). Hash epoch pinned in status: `VANILLA c42d284c…` byte-identical to the pre-QoL baseline anchor.
- **History:** 44 sessions; PRs #1–#52. Real mod work (16 QoL patches, ALL/VANILLA/PURIST_PLUS build presets, `docs/build-presets.md`) ended around session 020; sessions 021–044 are hourly-wake heartbeats ("honest idle").
- **Open PRs:** zero (`list_pull_requests`; status claims same). Stale remote branches: `track-a/session-019`, `track-a/session-024` (both ⚑ owner-click-delete — agent deletion was DENIED by the auto-mode git-destructive classifier, `control/status.md@08d2611` ⚑ 5), plus **`claude/eloquent-newton-qaf1ii`** (head of closed-unmerged PR #47) which is NOT in the ⚑ list.
- **CI:** `rom-builds` (builds agbcc + full pokeemerald ROM every push/PR; "asserted and hashed but NEVER uploaded (private-repo hard rail: no ROM artifacts)" — `.github/workflows/rom-builds.yml@08d2611`) and `substrate-gate`. Latest main runs both **success** at HEAD `08d2611` (runs 29170585254, 29170585220, 2026-07-11T22:29Z).

#### Known problems (filed)
- **THE incident (owner-queue class):** inbox ORDER 003 @`08d2611`: "this repo's README declares a 'no exceptions' PRIVATE hard rail, 8 PR bodies asserted 'this repo is PRIVATE,' and the repo has been **PUBLIC the whole time** — the vendored Nintendo decomp source was world-readable, and no session ever ran the one API call that checks" (fleet-manager night-review 2026-07-10 finding Q16). Remediated: owner flipped visibility; standing R22 verify-every-session rule now in force with 20+ consecutive clean cycles.
- **⚑ OWNER-ACTION 1** — "ROM builds" is **not in the required-check set** (only substrate-gate); owner must add it via ruleset UI ("No agent API surface for rulesets", `control/status.md@08d2611` ⚑ 1 + `docs/PLATFORM-LIMITS.md`). Until then auto-merge can land a PR that breaks the Nintendo-source build.
- **⚑ OWNER-ACTION 2/3** — next-arc concept pick + playtest verdict on 6 game-feel patches; hatch-128 stacking blocked on it (`control/status.md@08d2611`).
- **Toolchain-bearing container scarcity:** review-queue row #23 "needs a toolchain-bearing container; none seen since session 027's capability finding" (`control/status.md@08d2611`).
- **Classifier walls (resolved but recurrent class):** wake-env GitHub write tools + `add_repo` denials (OWNER-ACTION 4/5, RESOLVED after 20 clean cycles; reopen-on-regression).

#### Unknown problems (nobody filed)
- **PR-ledger drift, small:** status claims "PRs #1–#50 all merged or correctly closed-as-superseded (#19, #29)" (`control/status.md@08d2611`) — but **PR #47 is also closed-unmerged** (no merged_at; superseded by #48 the same session) and is absent from that list, and its branch is the unflagged stale ref above.
- **Session-card gaps:** `.sessions/` has track-a sessions 001–030 and 041 only — **no cards for 031–040 or 042–044** despite PRs #36–#51 existing for them; ORDER 004 done-when ("every fired session records … in its committed session card") is unmet by wake practice (model line lives in PR bodies).
- **No top-level `.gitignore`** at `08d2611` (only `pokeemerald/.gitignore`) — a built ROM at repo root (e.g. a copied `pokeemerald.gba`) would not be ignore-protected. Never-upload rail exists in CI comments only.
- **Secrets:** token/key-pattern grep over origin/main (excluding vendored trees) — zero hits. Clean.
- **Track-isolation cross-references:** `docs/conventions.md@08d2611` line 97 encodes the rail ("…Track A assets/code into `gba-homebrew` (Track B is publish-safe by…"); README hard rail is explicit and includes "no owner override assumed". No gba-homebrew code found here beyond process references — the risky direction is A→B, and today it is guarded only by prose + agent discipline, no tooling.

#### Prompt implications
- Prompt must say: R22 first — verify `visibility: private` via the API every session before ANY private-track work; never assert visibility from README/rails/prior PR bodies (the shipped-public bug class).
- Prompt must say: never move code, assets, screenshots, hashes-of-assets, or PR-body descriptions of Track A material to any public surface — including the merged seat's own public-track PRs and session cards.
- Instructions must encode: no ROM binaries or extracted-asset uploads ever (CI comment rail → seat rule); no `baserom` may be committed; owner provides base inputs into the private surface only.
- Not promptable (needs owner): add "ROM builds" to required checks; delete stale refs `track-a/session-019`, `track-a/session-024`, `claude/eloquent-newton-qaf1ii` (classifier denies agent deletion); concept pick + playtest verdicts.

#### Seat merge-readiness: Game Lab
- **The two repos are ALREADY one lane by design** ("game-lab is ONE lane running two GBA game tracks in two repos … per-repo inboxes", both READMEs @HEAD) — the merge formalizes an existing split-brain, which is the good news: control grammar (`control/inbox.md` manager-written append-only / `control/status.md` lane-written) is shared.
- **Heartbeat grammar diverges:** pml status is *wholesale overwrite* each session (`control/status.md@08d2611` header) vs gba's *section-preserving own-section writes* per parallel arc (`control/status.md@d1ec24f` header). A merged seat prompt must pick one grammar per repo and say so, or parallel sessions will clobber each other's sections (gba PR #53 already documents a status race + mechanical resolution).
- **Toolchains differ completely:** gba = devkitARM r68 + Butano 21.7.1 + BlocksDS 1.21.1, sha256-pinned mirror installs (`docs/current-state.md@d1ec24f`); pml = apt binutils-arm-none-eabi + vendored agbcc + pokeemerald make (`rom-builds.yml@08d2611`). Different setup scripts, different CI jobs, different "green" meanings. Seat prompt must route per-track, never share build dirs or caches.
- **CI/merge-path asymmetry:** both use substrate-gate + auto-merge, but the required-check sets differ AND both have a filed required-check hole (gba: NDS job not required; pml: ROM builds not required at all). Merged seat must treat "auto-merge armed" ≠ "build proven" on BOTH repos until the two owner clicks land.
- **The isolation rule must concretely forbid:** (1) any file, asset, screenshot-of-copyrighted-asset, or diff from `pokemon-mod-lab` appearing in `gba-homebrew` or any public PR/body/card — today the only guard is README prose in both repos + R22; (2) starting private-track work before the session's own visibility API check; (3) committing ROM binaries or base-ROM material anywhere in pml (contrast: gba *deliberately* commits dist ROMs — the seat carries two opposite binary policies and must never apply the gba habit to pml); (4) describing Track A mod content in the public repo beyond the existing lane-identity pointer. What makes it risky today: one brain, two policies, and a proven incident where the rail was asserted 8 times while false (ORDER 003 @08d2611).
- **Session numbering/card conventions differ** (gba plain "session N" vs pml "track-a-session-NNN"; both have undocumented card gaps) — merged seat needs one card convention with per-track prefixes, or provenance queries break.

#### Top regression risks (this slice)
1. **Cross-track leak by unified seat:** one merged context holding Nintendo-derived content and a public repo is one wrong-repo commit away from re-shipping the 2026-07-10 public-exposure incident (ORDER 003 @08d2611) — highest-severity, prose-only guard today.
2. **Visibility regress unnoticed:** R22 lives in pml's inbox/status only; a merged seat prompt that drops or dilutes the every-session API check recreates the "asserted PRIVATE while PUBLIC" bug class.
3. **Auto-merge through the required-check holes:** both repos can merge red-in-practice PRs (gba NDS jobs / pml ROM builds not required) — a broken Nintendo-source build or broken NDS ROM lands silently until the two owner ruleset clicks happen.
4. **Status-file clobber under the two heartbeat grammars** (wholesale-overwrite vs own-section) once one seat writes both repos, plus the already-observed status race (gba PR #53 note).
5. **Ledger/card erosion:** wake sessions already skip committed cards in both repos (pml 031–040/042–044, gba 12–14/22–23 missing) and pml's PR ledger misses #47 — the merged seat inherits and doubles the drift surface.

---

## Ideas Lab (idea-engine · sim-lab) + superbot-plugin-hello

Method: local clones fetched (`git fetch origin`) and inspected at `origin/main`; GitHub MCP for PRs/Actions/repo metadata. All READ-ONLY. Citations are `file@sha`, PR#, commit SHA, or Actions run id. Model names family-level only.

### idea-engine

**Verdict: FRESH** — heartbeat `updated: 2026-07-11T19:53:28Z` (`control/status.md@a9b41f6`) matches HEAD `a9b41f6` 2026-07-11T19:55Z ("archive-ready close-out … (#219)"); the lane is deliberately in phase **ARCHIVE-READY**, not abandoned.

#### State
- **Heartbeat**: `control/status.md@a9b41f6` — phase ARCHIVE-READY, `health: green`, `kit: v1.10.0`, `orders: acked=001-002 done=001-002`, `blockers: none`. Stamp discipline is explicit ("real wall-clock via date -u, per the control/README rule").
- **Git history agrees**: last 6 merges a9b41f6(#219) 19:55Z · c71710e(#218) 19:48Z · 49a70f5(#217) 19:43Z · 7992351(#216) 19:39Z · 4499d4c(#215) 19:28Z · 702c894(#214) 19:27Z — all 2026-07-11. 219 PRs merged since repo seed 2026-07-10 (~2 days).
- **Open PRs: 0** (`list_pull_requests state=open` → `[]`). Claims dir clean: `control/claims/` = `README.md` only (matches the heartbeat's claims-sweep claim).
- **CI**: two workflows, `substrate-gate.yml` + `auto-merge-enabler.yml`. All 30 most-recent main-branch `substrate-gate` runs **success** (newest: run 29165103800, sha 574ac37, 19:21:15Z). Caveat: **no main-push runs exist for the final ~5 merges** (newest main run 19:21Z vs HEAD merged 19:55Z) — PR-lane runs were green pre-merge; cause not measured.
- **~122 merged remote branches left in place** — heartbeat admits deletion is walled ("git push-delete → verbatim HTTP 403, GitHub MCP has no branch-delete tool", `control/status.md@a9b41f6` line 3; wall also at `docs/CAPABILITIES.md:51`). Confirmed: `git branch -r` shows ~125 refs.

#### Known problems (filed by the lane itself)
- **Telemetry-PR loop, ~40 PRs**: "end the self-feeding one-line telemetry-PR loop (#58..#100): exempt the three kit state anchors … from the HARNESS stop hook's git-cleanliness nag" — `ideas/fleet/README.md@a9b41f6` (fix shipped: `scripts/patch-stop-hook-git-check.sh`, SessionStart-wired in `.claude/settings.json`).
- **Auto-merge race classes** (`docs/current-state.md@a9b41f6` § Ops facts): arm-at-open squashes ~25s after open so heartbeat PR-number stamps must ride a follow-up PR (recipe PRs #198/#201/#206/#212); "**Already-clean PRs never arm** (race class, PR #209) … sat green ~4 minutes with auto-merge silently unarmed"; "**Dirty-PR zero-check-runs jam**"; enabler scope excludes `venture/*` branches.
- **Recurring stray local commit**: "local `main` in session checkouts recurringly diverges from `origin/main` with a stray seed commit `df64aab`" (`docs/current-state.md@a9b41f6`).
- **Coordinator triggers dismantled at archive** (Q-0265): "The archiving coordinator's failsafe cron trigger AND its 15-minute send_later chain are being DISMANTLED with the chat archive — a fresh coordinator MUST RE-ARM BOTH per Q-0265 at first wake" (`control/status.md@a9b41f6` ⚑ block).
- **Owner sitting bundle, deadline ≤2026-07-13**: FOUR bundled decisions (Lumen Drift itch.io go/no-go · pokemon playtest verdicts · gba concept pick · post-EAP routine posture) + the WEBSITES CUTOVER structured choice — all parked in the ⚑ needs-owner block (`control/status.md@a9b41f6`), unanswered at archive.
- **Verdict debt**: "PROPOSAL 009 and 010 verdicts owed by sim-lab (odd-hour pulls)" (`control/status.md@a9b41f6` notes). PROPOSAL 009's verdict actually exists (sim-lab VERDICT 010) — the heartbeat is slightly behind here; PROPOSAL 010 is genuinely unverdicted.
- Inbox: ORDER 001 + 002 both answered (`orders:` line + `docs/retro/self-review-2026-07-11.md` exists). No unanswered ORDERs.

#### Unknown problems (nobody filed)
- **HEADLINE — the CI gate is broken at HEAD**: `python3 scripts/preflight.py` exits **2** right now: `check_sections: cannot parse lane registry: unparseable roster lane cell '↳ substrate-kit — control/status-gba-homebrew-trackb.md' — roster format changed? update this parser, do not trust this run`. `substrate-gate.yml:96` runs exactly this preflight, so **the next non-control-only PR opens permanently red**. Cause: fleet-manager roster generation #9 (`docs/roster.md`, fm PR #86/cddcb95, generated 2026-07-11T20:25Z) introduced `↳` sub-rows — **25 minutes after idea-engine archived** (19:55Z). Nobody has filed this; both the heartbeat and CI history still say green.
- **Second-order: the 8-seat restructure will break the same checker again.** `check_sections.py` derives valid `ideas/<section>/` names from the live roster (docstring `scripts/check_sections.py:11-13`); the restructure (fleet-manager PR #88 "Ideas Lab (`ideas-lab/` — folds idea-engine + sim-lab)" — **parked unmerged**, base main@1dea86d) folds the 12 lanes idea-engine's sections mirror (`ideas/`: fleet + 12 lane dirs, verified at a9b41f6) into 8 seats. Sections and parser both invalidate when #88–#91 land. `product-forge/` section exists while product-forge "awaits owner disposition (not in the 8-seat list)" (fm `projects/README.md@claude/restructure-seats`).
- **CLAUDE.md drift**: `.claude/CLAUDE.md` architecture line still says sections are "derived from superbot docs/eap/fleet-manifest.md" — that manifest was flipped `historical`/SUPERSEDED 2026-07-11 (superbot `docs/eap/fleet-manifest.md@1ecc211` header); the checker was repointed to the roster but the working agreement wasn't.
- **`docs/current-state.md` skeleton unfilled**: "Stability baseline", "In flight", "Recently shipped" are still template placeholders at a9b41f6 — only the Ops-facts section is real. The heartbeat carries the true state instead (single point of failure for orientation).
- **Roster-vs-status trigger contradiction**: fm roster gen#9 shows idea-engine "+2 one-shot(s), next 2026-07-11T19:10" while the heartbeat says all coordinator triggers dismantled — which is live is **not measurable from this seat**.
- **Secrets**: pattern sweep (ghp_/github_pat_/sk-ant-api/AKIA/xox[bap]/BEGIN-PRIVATE, excluding bootstrap.py/.substrate) → **0 hits**. Clean.
- Spot-checks of shipped claims: `docs/retro/archive-ready-2026-07-11.md` ✓ exists, `docs/retro/self-review-2026-07-11.md` ✓, `scripts/patch-stop-hook-git-check.sh` ✓, claims dir clean ✓ — no missing-deliverable found.

#### Prompt implications
- Prompt must say: **at first wake run `python3 scripts/preflight.py`; expect check_sections to fail on roster `↳` sub-rows; fixing the parser (or pinning `--file` a saved roster copy) is the first PR, before any content work.**
- Prompt must say: re-arm BOTH the failsafe cron and the ~15-min send_later chain per Q-0265 at first wake (`control/status.md` ⚑ + `docs/retro/archive-ready-2026-07-11.md` are the boot documents).
- Instructions must encode: heartbeat-stamp discipline = real `date -u` wall-clock, never-guess PR numbers (stamp rides a follow-up PR — the #198/#201/#206/#212 recipe).
- Instructions must encode: when a green in-pattern PR sits unarmed >2 min, merge manually (PR #209 class); read `mergeable_state` before waiting on checks.
- Not promptable (needs owner/tooling): branch deletion (403 on every path — 122 stale branches stay); the ≤07-13 owner sitting bundle; roster format stability (fleet-manager-side).

### sim-lab

**Verdict: FRESH** — heartbeat `updated: 2026-07-11T20:20:00Z` (`control/status.md@0622118`), HEAD 0622118 (#43) 2026-07-11T19:52:49Z; phase **CLOSE-OUT / ARCHIVE-READY** by owner order, not abandonment. (Note the stamp is ~27 min *ahead of its own commit time* — see Unknown problems.)

#### State
- **Heartbeat**: `control/status.md@0622118` — "Sim-ready intake queue EMPTY (idea-engine outbox consumed through PROPOSAL 009 → VERDICT 010). 11 verdicts finalized (V001–011). No open PRs/branches/issues." `kit: v1.7.0 · check: green`, orders ORDER-001/002 both done.
- **Git history agrees**: 0622118(#43) 19:52Z · a8d901b(#42) 19:43Z · 4c74d7a(#41) 18:46Z · 45613e6(#40) · d461932(#39), all 2026-07-11. **Open PRs: 0** (verified). Remote branches: `main` + 2 stale `sim/owner-002-*` heads (minor, contradicts "no branches" only trivially).
- **CI**: one workflow, `substrate-gate.yml` (kit gate — runs `bootstrap.py check --strict`, **no roster coupling**). Latest main runs all **success**, including the final merge (run 29166034428, sha 0622118, 19:52:51Z). `bootstrap.py check --strict` re-run locally at HEAD: **exit 0**.
- **Deliverables verified on disk**: 11 verdict blocks V001–V011 in `control/outbox.md@0622118` (headers at lines 11–119); sims dirs exist for every verdict incl. `sims/verdict-010-settle-once-architecture-guard/` and the two owner-direct audits; `PLATFORM-LIMITS.md`, `docs/retro/self-review-2026-07-11.md`, `docs/retro/archive-ready-2026-07-11.md`, verdict-numbering map at `docs/current-state.md:74` — all present.

#### Known problems (filed)
- **OA-002 Codex usage cap**: "6+ @codex questions are pending; the Q-0264.4 review step draws no reply until the quota frees … reproduced on every verdict PR" (`control/status.md@0622118`; e.g. sim-lab PR #38 comment). Every verdict ships with `codex: … reply: pending`.
- **OA-003 review-site deploy**: VERDICT 011's `review` website "built for Anthropic reviewers but is currently unreachable" — owner click (`control/status.md@0622118`).
- **OA-004 tag-push 403**: `git push origin refs/tags/harness-v0.1.0` → 403; harness release un-versioned (`PLATFORM-LIMITS.md@0622118`).
- **Cross-session trigger binding org-walled**: verbatim "binding a trigger to another session is not enabled for this organization"; trigger tools absent from coordinator top-level toolset, present behind ToolSearch in worker seats (`PLATFORM-LIMITS.md@0622118` § Routine/wake arming).
- **Auto-merge squash race + GraphQL rate-limit**: "GraphQL auto-merge is intermittently rate-limited; REST merge-on-green is the PROVEN fallback"; squash out-races the trailing heartbeat commit ("Seen on #38/#39 and #40/#41") (`PLATFORM-LIMITS.md@0622118` § Merge path).
- **api.github.com 403 for non-scoped repos** — proven bypass: raw.githubusercontent.com + `git ls-remote` + shallow clones (`PLATFORM-LIMITS.md@0622118`).
- **Recurring evidence gap (structural)**: "No live fishing/mining earn-rate baseline exists in source, so reward-VALUE conclusions stayed provisional in VERDICTs 001 and 008 … owned upstream (idea-engine / the game repos), not fixable in sim-lab" (`docs/current-state.md:83-90@0622118`).
- OA-005 (dead-session trigger) — RESOLVED pre-archive, zero sim-lab triggers remain (`control/status.md@0622118` ⚑ OA-005).

#### Unknown problems (nobody filed)
- **Future-stamped heartbeat**: `updated: 2026-07-11T20:20:00Z` sits inside commit 0622118 authored 19:52:49Z — the stamp is ~27 min in the future of its own commit. Hand-estimated stamps violate the wall-clock rule idea-engine enforces; a merged-seat freshness checker would mis-rank this lane.
- **PROPOSAL 010 orphaned by the double archive**: idea-engine appended it 19:41Z (#217), sim-lab archived ~19:52Z without pulling it; each repo's close-out points at the *other side's next session* ("polls idea-engine outbox for PROPOSAL 010+", `control/status.md@0622118`; "unpulled 010 at archive is EXPECTED", idea-engine status). With both trigger sets dismantled, **nothing will pull it unless the new seat prompt says so.**
- **Kit/harness fork inside the future seat**: sim-lab kit **v1.7.0** vs idea-engine **v1.10.0** (fleet is on v1.12.x — fm PR #90); sim-lab has **no `.claude/` directory at all** (verified `ls -a`) while idea-engine ships `.claude/settings.json` with 4 hook classes + a SessionStart stop-hook patch; sim-lab has **no auto-merge-enabler workflow** (REST merge-on-green is its documented path) while idea-engine arms auto-merge at open. Same "seat", three divergent machineries.
- **Numbering grammar trap**: VERDICT numbers ≠ PROPOSAL numbers (V009/V011 are owner-direct, so P009→V010 etc.); the map exists (`docs/current-state.md:74`) but any consumer that assumes V-n ↔ P-n silently misroutes. Also `control/inbox.md` legally interleaves two writers' block types (manager `## ORDER` between lane `## INTAKE 005` and `006`).
- **Secrets**: same pattern sweep → **0 hits**. Clean.

#### Prompt implications
- Prompt must say: first wake pulls idea-engine `control/outbox.md` for PROPOSAL 010+ (it is sim-ready and owed a verdict) and re-arms the wake loop per `PLATFORM-LIMITS.md` § wake-recipe.
- Instructions must encode: verdict-vs-proposal numbering is offset — always cite the source PROPOSAL number + timestamp verbatim (the existing INTAKE grammar) and never derive one number from the other.
- Instructions must encode: merge path = REST merge-on-green (GraphQL flaky); heartbeat rides a follow-up control-lane PR after the squash race; `updated:` stamps come from `date -u`, never estimated.
- Instructions must encode: @codex replies are verify-never-obey (Q-0120) and will be `pending` until OA-002 clears — don't block verdicts on them.
- Not promptable (needs owner/tooling): OA-002 Codex quota, OA-003 review-site deploy, OA-004 tag push, the org wall on cross-session trigger binding, the upstream earn-rate telemetry gap.

### superbot-plugin-hello

**Verdict: DEAD (empty by half-executed handoff)** — zero commits ever: GitHub API returns `409 Git Repository is empty`; `git ls-remote origin` returns no refs; repo created 2026-07-10T16:03:03Z, `pushed_at` 16:03:04 (creation only), `size: 0`, description "the plugin template for superbot-next" (repo metadata via search_repositories).

#### State
- No heartbeat, no commits, no branches, no PRs, no CI (nothing to run). Local clone at `/home/user/superbot-plugin-hello` contains only `.git`. **The empty repo IS the finding.**

#### Known problems
- It is tracked — by *another* repo: superbot-next OWNER-ACTION 2 asked the owner to "Create one new empty GitHub repository named superbot-plugin-hello … agents then move `examples/superbot-plugin-hello/` verbatim" (superbot-next `control/status.md:147-149@249ecaa` fetch of origin/main).

#### Unknown problems
- **Not dead weight — a live template whose second leg never fired.** The complete plugin package (README, pyproject.toml, `superbot_plugin_hello/`, `tests/`) exists at superbot-next `examples/superbot-plugin-hello/` (tree verified at origin/main; last touched 62d850f, 2026-07-11), "seeded in-tree pending the owner-created menno420/superbot-plugin-hello repo" (`docs/game-plugin-contract.md:9-10`). The owner clicked (repo created 2026-07-10T16:03Z) — **and no agent has noticed since**: superbot-next `control/status.md@HEAD` still lists the repo creation as a *pending* owner action ~30h after it was done. Stale owner-queue row + unfired follow-through.
- Because it's empty there is no settings/branch-protection/secrets surface to audit — nothing measured, nothing to leak.

#### Prompt implications
- The SuperBot 2.0 seat prompt (not Ideas Lab) must say: **repo exists and is empty since 2026-07-10 — move `examples/superbot-plugin-hello/` verbatim and clear OWNER-ACTION 2 from the status ledger.**
- Instructions must encode (fleet-wide): after filing an owner-click ask, re-check whether it was satisfied at every wake — an owner click with no agent follow-through is silent drift.

#### Seat merge-readiness: Ideas Lab

The generate→verify handoff **exists and demonstrably worked**: PROPOSALs 001–009 (idea-engine `control/outbox.md@a9b41f6`) were each pulled as INTAKE 001–009 into sim-lab `control/inbox.md@0622118` with verbatim source citations (number + timestamp + pinned sha), and 11 verdicts (V001–V011, incl. 2 owner-direct) sit finalized in sim-lab `control/outbox.md@0622118`. Friction the merged seat prompt must handle:

1. **Verdict routing is triangular, not bilateral** — sim-lab's outbox is addressed to the **fleet manager**, which "owns all post-verdict routing" (`control/outbox.md@0622118` header; Q-0264); idea-engine only *tracks* verdicts. An internal loop must either keep the manager fan-in or explicitly re-rule it; silently short-circuiting it breaks the fleet's one-reviewer contract.
2. **PROPOSAL 010 is in flight across a double archive** — the loop is stopped right now; nothing pulls it without a prompt line.
3. **Two heartbeat files, two grammars** — same key set but idea-engine enforces `date -u` stamps + never-guess-PR-numbers while sim-lab's final stamp is future-dated; a merged seat needs ONE stamp rule and (open question) whether it keeps two `control/status.md` files or roster sub-rows.
4. **Two CIs**: idea-engine's gate runs `scripts/preflight.py` (roster-coupled, **currently exit 2** — see headline) vs sim-lab's kit-only gate (green). Merged seat inherits a broken gate on one half.
5. **Two merge paths**: enabler-armed auto-merge with documented race classes vs REST merge-on-green; and two kit versions (v1.10.0 / v1.7.0, fleet at v1.12.x) + hooks-vs-no-hooks `.claude/` split.
6. **Numbering**: PROPOSAL-n ↔ VERDICT-m offset with the map only in sim-lab `docs/current-state.md:74`.
7. **Cross-repo mechanics still needed post-merge**: even as one seat, the repos stay separate — raw-URL pulls, sha-pinned citations, append-only one-writer files (`control/README.md` both sides) must survive; the seat prompt should name which repo's clone is "home".

#### Top regression risks (this slice)

1. **idea-engine CI gate broken at HEAD** — `check_sections` can't parse fleet-manager roster gen#9 `↳` sub-rows; every non-control PR opens unmergeable-red until the parser is fixed (substrate-gate.yml:96 → preflight exit 2). Unfiled.
2. **Generate→verify loop is fully stopped** — PROPOSAL 010 sim-ready + unpulled, both coordinators archived, both trigger sets dismantled; resumption depends entirely on the new seat prompt encoding both wake/re-arm recipes (Q-0265 + PLATFORM-LIMITS wake-recipe).
3. **8-seat restructure not landed** (fm PRs #88–#91 parked unmerged) — when it lands, idea-engine's 12 lane-derived `ideas/` sections and the roster parser invalidate a second time; sections like `product-forge/` map to a seat that may be retired.
4. **Convention fork inside the single seat** (kit v1.7.0 vs v1.10.0, hooks vs none, auto-merge enabler vs REST merge, stamp discipline) — a prompt written for one half misfires on the other.
5. **Stale-ask drift class** (evidenced by plugin-hello): owner-click asks that were satisfied but never re-checked; both lanes' ⚑ ledgers (idea-engine's PROPOSAL-009-verdict-owed line, superbot-next's OWNER-ACTION 2) already show one instance each.

---

## Archived codetool labs (one-paragraph checks)

### codetool-lab-opus4.8 (mdverify)

Last commit `80f6cd102ef6850ca0570c3cd5cf5ec000c2264c` on main, 2026-07-09 ("control: wind-down complete — ready for archive + fresh session (#22)"). **Not GitHub-archived** — the API reports `archived: false`; it is inactive-by-declaration, not frozen (planning docs say "ARCHIVE after gen-3 succession settles", i.e. the archive click hasn't happened). Zero open PRs and zero open issues; one dangling unmerged branch `claude/status-heartbeat-001` (tip `ea1b23b`, a superseded status heartbeat — `control/status.md` itself flags it for owner deletion since agents 403 on ref deletes). No stale self-description: the README presents the mdverify tool as a product (with CI badge) but explicitly labels the repo a "throwaway eval repo", and `control/status.md` states wind-down complete. Live-fleet references are one-directional and terminal: superbot's fleet-consolidation plan (2026-07-11) lists it as "⚫ parked / ARCHIVE"; obvious salvage is the succession pack (`docs/succession/NEXT-BOOT.md`, gen-2 feedback, tested setup script) and the whole-life retro, which the fleet plans cite as reference material. Tags v0.1.0 + v0.2.0 with Releases are live. Verdict: **DARK** (wound down, not yet GitHub-archived).
Safe-to-delete: **no** — owner's own plan says archive (read-only), not delete; succession/retro docs are cited fleet reference material, and the pending owner action is the archive click + branch delete, not removal.

### codetool-lab-sonnet5 (cfgdiff)

Last commit `66c3dfc79735db55dc777854eda6087ff9c45e02` on main, 2026-07-09 ("status: wind-down complete — ready for archive + fresh session (#16)"). **Not GitHub-archived** (`archived: false`) — inactive since wind-down. Zero open PRs/issues; one leftover branch `test/push-check` that IS merged into main (a probe branch, flagged in `control/status.md` as cosmetic owner-delete). No stale self-description: README opens by calling it a "Throwaway EAP capability-evaluation repo" and honestly says cfgdiff is "Not yet on PyPI"; status file declares wind-down complete with a precise needs-owner list (PyPI trusted publisher, tag `v0.1.1` at `0b1eb60` — no tags exist yet, so the release never shipped). Fleet references: superbot fleet-consolidation plan lists it "⚫ parked / ARCHIVE — pending v0.1.1 tag"; salvage items are the succession pack (`docs/succession/`), the retro (`docs/retro/project-review-2026-07-09.md` with click-by-click release steps), and the cross-format diff tool itself if the owner ever wants it published. Verdict: **DARK**.
Safe-to-delete: **no** — the owner-planned disposition is archive, and it still holds an unshipped release recipe plus succession docs the fleet plans reference.

### codetool-lab-fable5 (envdrift)

Last commit `a6cf1a9d5e8b1082025e8a4c9abce9febd2aea92` on main, 2026-07-10 ("Succession-doc fix: release-wall is SEAT-DEPENDENT, not 'route closed' (#14)") — one day *after* its own wind-down commit `d7f46ea` (2026-07-09), a post-wind-down correction. **Not GitHub-archived** (`archived: false`). Zero open PRs/issues; no dangling branches (only `main` on origin) — the cleanest of the three. No stale self-description: README markets envdrift as a working tool (accurate) and explicitly notes `control/` is fleet metadata; `control/status.md` says wind-down complete, with needs-owner items (tags v0.1.0 at `73ef38d` / v0.2.0 at `13a84e5` + Releases — no tags pushed yet, agents policy-blocked; optional PyPI). Fleet references: listed "⚫ parked / ARCHIVE — pending tag/Release clicks" in the 2026-07-11 fleet-consolidation plan; salvage = succession pack (`docs/succession/` incl. PLATFORM-LIMITS + tested `environments/setup-universal.sh`) and envdrift 0.2.0 itself, a finished zero-dependency CLI. Verdict: **DARK**.
Safe-to-delete: **no** — archive is the planned terminal state; it carries untagged finished releases and the succession/platform-limits docs the fleet cites.

### Prompt implications

Exclude all three codetool-lab repos from every seat prompt (they are wound-down gen-1 eval arms, no live lane); do **not** list them as delete candidates — the owner's standing disposition is GitHub-archive (read-only) after gen-3 succession settles, with small pending owner clicks first (opus: delete `claude/status-heartbeat-001`; sonnet5: tag v0.1.1; fable5: tags v0.1.0/v0.2.0 + Releases). None of the three is actually GitHub-archived yet — the census term "archived" is currently aspirational.

---

## Prompt-implications rollup

Deduplicated across all five fragments, grouped per future seat, then cross-fleet.
"Prompt must say" = goes in the seat's coordinator/wake prompt; "instructions must
encode" = goes in the Project Custom Instructions / repo conventions; "not
promptable" = needs owner clicks or tooling and the prompt may only carry the ⚑.

### SuperBot World (superbot-games · superbot-idle · superbot-mineverse)

Prompt must say:
- On wake, re-verify `control/status.md` open-PR/OWNER-ACTION claims against live GitHub before acting; sweep terminal-state `control/claims/<branch>.md` files.
- Mineverse FIRST action = get PR #42 (login-CSRF fix) merged; only then anything secrets-adjacent; then close-or-supersede #31; re-render `.claude/CLAUDE.md` so it stops denying auth exists.
- Idle: before any merge, run `python3 -m pytest -q` yourself (no pytest in CI); first wake task = add a pytest gate workflow + ask owner to require it. Treat PLATFORM-LIMITS.md as pre-verified walls — do not re-probe.
- Treat main-HEAD CI absence (mineverse 76be821 class) as "verify before building on top" — check the last commit's check runs.
- Per-repo merge-path table: games = owner-click only (self-merge classifier-blocked, auto-merge deliberately unarmed); idle = auto-merge armed-at-creation (with both-ways arming failure classes); mineverse = enabler arms `claude/*` branches only.

Instructions must encode:
- One canonical heartbeat home per repo, with the archived per-lane status files explicitly marked history; one claims dir + terminal-state sweep rule.
- Both dormant repos' re-arm recipes (idle status.md RE-ARM SPEC; mineverse heartbeat/retro notes); verify via list_triggers after arming.
- An explicit "externally-blocked ≠ actionable" list (mineverse FLAGs 1/2 → superbot bot lane; games persistence → the superbot-next games-persistence decision, id at its stamp home in `docs/prompts/v3/per-project/superbot-world-custom-instructions.md`).

Not promptable (owner/tooling): six OAuth env vars; enabler's `claude/*`-only filter; merge queue; pytest-required repo-settings click; scheduler-tool seat availability; the model-line vs no-id-in-artifacts ruling; transfer-policy source model decision.

### Venture Lab / Money seat (venture-lab · trading-strategy)

Prompt must say:
- venture-lab: children never self-merge or arm auto-merge; land via coordinator squash-merge under a genuine owner turn; PARK label = owner-merge only. trading-strategy: land via MCP squash-on-green (the every-merge-to-date path); micro-PRs for claims housekeeping are normal.
- First action of any seat session = verify `control/status.md` stamp against `git log origin/main -1`; re-stamp if it lags.
- Research-only rail (trading-strategy): no broker libs, no order/exchange-write code, no live API config — ever; holdout SPENT; paper lane touches only `load_paper_ohlcv`; promotion only via owner-gated pre-registered protocol.
- Weekly grading: `next-update-by` 2026-07-17T23:59Z via `scripts/grade_paper.py` per protocol §6–§7; at every coordinator handover re-arm the grading trigger and record trigger IDs in `control/status.md`.
- Qualify ORDER numbers repo-first (colliding inbox namespaces); name both heartbeat grammars and keep them per-repo.

Instructions must encode:
- Intake token caps include research + CI overhead; report metered usage; 3-of-4-over-cap is the base rate.
- Kit upgrades leave a lane-owed heartbeat bump — pay it next lane session.
- Per-repo default posture: cautious in trading-strategy (scientific rails), shipping in venture-lab (owner-click rails) — scoped per-repo, never per-seat.

Not promptable (owner/tooling): PR #51 close + branch delete (photo exposure — keep the ⚑ verbatim, never invent a publish path); publish clicks / Stripe keys / GitHub Pages; auto-merge repo toggle; env setup-script console paste; session-independent trigger hosting; post-2026 OOS protocol decision.

### Game Lab (gba-homebrew · pokemon-mod-lab)

Prompt must say:
- R22 first — verify `visibility: private` via the API every session before ANY private-track work; never assert visibility from README/rails/prior PR bodies.
- Never move Track A material (code, assets, screenshots, hashes-of-assets, PR-body descriptions) to any public surface, including the seat's own public-track PRs and session cards.
- After any merge in gba, verify the post-merge main NDS/full CI run green (auto-merge waits only on the GBA "ROM builds" required check); treat "auto-merge armed" ≠ "build proven" in BOTH repos until the owner's two required-check clicks land.
- Every fired session (including bare wakes) commits a session card with the `📊 Model:` family line — PR-body-only attribution is drift.
- Route toolchains per-track (devkitARM/Butano/BlocksDS vs agbcc/pokeemerald make); never share build dirs or caches; per-repo heartbeat grammar (gba section-preserving vs pml wholesale-overwrite) named explicitly.

Instructions must encode:
- No ROM binaries or extracted-asset uploads ever in pml; no `baserom` committed; owner provides base inputs into the private surface only. (Contrast: gba deliberately commits dist ROMs — never apply that habit to pml.)
- dist ROM refresh = same-PR provenance row (size + sha256 + source-tree statement) in `dist/README.md`, byte-determinism double-build.
- One session-card convention with per-track prefixes.

Not promptable (owner/tooling): add "NDS ROM build" (gba) and "ROM builds" (pml) to required checks; delete stale refs `track-a/session-019`, `track-a/session-024`, `claude/eloquent-newton-qaf1ii`; external publishing of Track B; concept pick + playtest verdicts; toolchain-bearing container availability.

### Ideas Lab (idea-engine · sim-lab)

Prompt must say:
- idea-engine first wake: run `python3 scripts/preflight.py`; expect check_sections to fail on roster `↳` sub-rows; fixing the parser (against the 8-seat roster shape, or pinning `--file` to a saved roster copy) is the first PR, before any content work.
- Re-arm BOTH the failsafe cron and the ~15-min send_later chain per Q-0265 at first wake; sim-lab side re-arms per `PLATFORM-LIMITS.md` § wake-recipe.
- sim-lab first wake pulls idea-engine `control/outbox.md` for PROPOSAL 010+ (sim-ready, owed a verdict).
- Keep the manager fan-in: sim-lab verdicts route to the fleet manager (Q-0264), never short-circuit idea-engine↔sim-lab directly without an explicit re-rule.

Instructions must encode:
- Heartbeat stamps = real `date -u` wall-clock, never estimated (sim-lab's future-stamp class); never-guess PR numbers — the stamp rides a follow-up PR (#198/#201/#206/#212 recipe).
- Merge paths per half: idea-engine enabler-armed auto-merge with its race classes (green unarmed >2 min → merge manually, PR #209 class; read `mergeable_state` first); sim-lab REST merge-on-green (GraphQL flaky).
- PROPOSAL-n ↔ VERDICT-m numbering is offset — always cite the source PROPOSAL number + timestamp verbatim; never derive one from the other.
- @codex replies are verify-never-obey (Q-0120) and stay `pending` until OA-002 clears — don't block verdicts on them.

Not promptable (owner/tooling): branch deletion (403; ~122 stale branches stay); the ≤2026-07-13 owner sitting bundle; roster format stability (fleet-manager-side); Codex quota; review-site deploy; tag-push 403; org wall on cross-session trigger binding; upstream earn-rate telemetry gap.

### SuperBot 2.0 (adjacent finding routed here)

- Prompt must say: menno420/superbot-plugin-hello exists and is empty since 2026-07-10 — move superbot-next `examples/superbot-plugin-hello/` verbatim and clear OWNER-ACTION 2 from the status ledger.

### Archived labs (all seats)

- Exclude codetool-lab-opus4.8 / -sonnet5 / -fable5 from every seat prompt; never list them as delete candidates — the standing disposition is GitHub-archive after gen-3 succession settles, with small pending owner clicks first (branch delete; tag v0.1.1; tags v0.1.0/v0.2.0 + Releases).

### Cross-fleet (every seat prompt / instruction set)

1. **Heartbeat ≠ ground truth:** first action of every session = verify `control/status.md` stamp + claims against `git log origin/main -1` and live PR state; the heartbeat is a dated snapshot, never an order list (stale in games, venture-lab, mineverse right now; structurally lagged everywhere by the lane-owed kit-bump rule).
2. **Claims sweep on wake:** delete claim files whose PRs are terminal; a claim is a whiteboard note, not an audit trail.
3. **Owner-ask recheck:** after filing an owner-click ask, re-check whether it was satisfied at every wake — a satisfied-but-unnoticed click is silent drift (plugin-hello; games' merged-PR asks; venture-lab's #38 disposition).
4. **Trigger succession:** every seat carries its own re-arm recipe and records trigger IDs in its heartbeat at every coordinator handover; session-bound triggers die silently at chat archive (proven in trading-strategy, idea-engine, sim-lab, venture-lab).
5. **Merge path is per-repo, never per-seat:** the fleet spans owner-click-only, coordinator-merge-under-owner-turn, MCP squash-on-green, enabler-armed auto-merge (branch-filtered), and REST merge-on-green — a seat prompt must table them per repo; retrying a walled merge burns turns.
6. **"Green CI" assurance level varies per repo:** required-check holes (gba NDS, pml ROM builds, trading-strategy tests-not-required) and missing suites (idle pytest) mean the prompt must state what green actually proves in each repo.
7. **Family-level model names only** in every artifact (`📊 Model:` line), committed in session cards, not just PR bodies.
8. **Secrets discipline held everywhere** (10/10 satellites clean at HEAD — patterns/filenames only, env-var names only): the prompts should keep the rule that produced this, verbatim.
9. **Kit-version spread** (v1.7.0 → v1.12.1) and `.claude/` presence asymmetry across repos in the same seat: prompts must not assume hooks or kit behavior exist uniformly; a kit-upgrade wave is a known heartbeat-drift generator.
