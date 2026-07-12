# 2026-07-12 — QA boot simulation of the v3 startup prompt set

> **Status:** `reference`

**What this is.** Wave 3 boot simulation of the v3 prompt set
(`docs/prompts/v3/` at fleet-manager@`8056b7e` = origin/main): all 8
per-project startup prompts plus `universal-startup.md` run **unslotted**
(9 runs total). Date: 2026-07-12. Three parallel QA workers produced the
slice reports this document consolidates; per-prompt defect lists below are
carried over from those reports essentially verbatim.

**Method.** Each prompt was walked as a **cold session** holding only
[startup paste + assembled Custom Instructions (core @ 6,117c + seat
block)], stepping every numbered instruction literally. Every referenced
file was checked at the target repo's live HEAD (fetched 2026-07-12; HEADs:
superbot `1ecc211` · superbot-next `80464ab` · superbot-mineverse `76be821`
· superbot-games `5ddfbee` · superbot-idle `c6a349d` · gba-homebrew
`d1ec24f` · pokemon-mod-lab `08d2611` · websites `8f97654` · venture-lab
`b633db6` · trading-strategy `ea22323` · idea-engine `4f50cce` · sim-lab
`98394cb` · substrate-kit `8a544a63` · fleet-manager `8056b7e`; superbot
rider sha `76d854d` verified). Tool calls were verified against the **live
MCP schemas** loaded in the QA environment (claude-code-remote:
create_trigger / send_later / list_triggers / delete_trigger /
update_trigger; github MCP). All char budgets were recounted byte-exact
(`git show 8056b7e:<path> | wc -c` on paste bodies). PR / run / trigger
state was read live via GitHub MCP and committed heartbeat evidence.

---

## 1. Verdict table

Every prompt boots; none boots clean. **0 STALLS · 0 BOOTS-CLEAN ·
9/9 BOOTS-WITH-WARNINGS.**

| # | Prompt | Verdict | BLOCKER | MAJOR | MINOR |
|---|---|---|---:|---:|---:|
| 1 | universal-startup.md (unslotted) | BOOTS-WITH-WARNINGS | 0 | 2 | 3 |
| 2 | fleet-manager | BOOTS-WITH-WARNINGS | 0 | 1 | 3 |
| 3 | self-improvement (substrate-kit) | BOOTS-WITH-WARNINGS | 0 | 2 | 3 |
| 4 | superbot | BOOTS-WITH-WARNINGS | 0 | 2 | 3 |
| 5 | superbot-world | BOOTS-WITH-WARNINGS | 0 | 1 | 4 |
| 6 | game-lab | BOOTS-WITH-WARNINGS | 0 | 0 | 3 |
| 7 | websites | BOOTS-WITH-WARNINGS | 0 | 1 | 3 |
| 8 | venture-lab | BOOTS-WITH-WARNINGS | 0 | 3 | 4 |
| 9 | ideas-lab | BOOTS-WITH-WARNINGS | 0 | 3 | 3 |
| | **Totals** | | **0** | **15** | **29** |

Defect ids below are namespaced per prompt (U / FM / SI / SB / SW / GL /
WS / VL / IL); the slice reports' original ids are noted where they differ.

---

## 2. Universal startup — run unslotted (U)

**Verdict: BOOTS-WITH-WARNINGS — does NOT stall.** The stall question is
answered by the prompt itself, line 9 (last sentence): "Unfilled {{slots}}:
derive from your Project's Custom Instructions + repo docs and proceed."
Every slot also self-describes inside its braces, so a cold session always
has a resolution rule and a proceed instruction; no numbered step dead-ends
on an unfilled slot — PROVIDED the Project actually has a seat CI block
pasted (sent verbatim with no seat CI, U-2/U-3 bite with nothing to patch
them).

Tool-schema audit (applies to all prompts — all PASS): `create_trigger`
(name / cron_expression / prompt, default self-bind = mode 1) exact;
`send_later({message, delay_minutes: 15})` exact (min 1); `list_triggers`
"limit 100 + next_cursor" near-exact (request param is `cursor`, response
`next_cursor`); `delete_trigger(trigger_id)` exact; `enable_pr_auto_merge`
/ `merge_pull_request` both exist as GitHub MCP tools; "standalone sleep is
blocked" matches the live harness; the worker-retry fallback's premise
(worker seats hold the trigger MCP) confirmed live.

**U-1 (A-1) · MAJOR — unslotted TRIGGER CUTOVER can delete a sibling
seat's live trigger.**
- Line (step 2): "delete_trigger each old id: {{OLD_TRIGGER_IDS — volatile:
  \"expect these, or later\"}} → verify absent."
- Reality: the slot unfilled + line 9's "derive from … repo docs and
  proceed" sends the session hunting repo docs for old trigger ids — and
  heartbeats DO publish full live ids of OTHER routines (substrate-kit
  control/status.md @ 8a544a63 names trig_01Jm57GAjNCFrYJn1oLMiYGE and
  trig_011iJucRpsruWJ4dFB7xVbvf inline; the shared registry holds 700+
  triggers). A "derived" deletion is a plausible wrong, destructive-ish
  action (recoverable only if a re-arm recipe is committed).
- Fix: append to step 2: "slot unfilled → delete NOTHING; only ever delete
  a trigger whose name/bound session provably belongs to YOUR seat."

**U-2 (A-2) · MAJOR — BOOT-1 orientation path + "(green expected)" are
wrong at ≥2 of the 8 target repos, and unslotted A has no SEAT DELTA to
patch them.** (Self-known: README v3.1 defect queue #2/#5 — confirmed
live.)
- Line (step 1): "Orient: .claude/CLAUDE.md → docs/current-state.md →
  docs/CAPABILITIES.md; run the repo's verify command (green expected)."
- Reality: `.claude/CLAUDE.md` is MISSING at fleet-manager@8056b7e and at
  substrate-kit@8a544a63 (both verified by tree lookup); fm's verify
  (check_roster_freshness.py) is designed-red at a typical wake and the
  kit's session gate is born-red by design — a cold verbatim session hits a
  dead first pointer and may misread a designed red as a boot failure.
- Fix: "(path missing → fall back to CONSTITUTION.md/README; a red your
  Custom Instructions name as designed is not a failure)" — or the README's
  own {{ORIENTATION_PATH}} slot proposal.

**U-3 (A-3) · MINOR — {{CRON_STAGGER}} unfilled is NOT derivable from the
target repo.** The stagger table lives only in fleet-manager
docs/prompts/v3/per-project/README.md and the seat CI blocks deliberately
carry no cron ("no cron in this block per the no-state-facts rule"), so
"derive from Custom Instructions + repo docs" cannot recover the assigned
slot; a deriving session picks an arbitrary 2-hourly slot → possible
minute-collision with another lane (benign; the in-slot ":30" warning
prevents the worst case). Fix: in-slot default "unfilled → any 2-hourly
cron NOT on :30".

**U-4 (A-4) · MINOR — PACEMAKER re-arm stacks pending one-shots.** "before
ending ANY turn, arm a send_later ~15 min out … re-arm a fresh one every
turn" — send_later one-shots self-disable only AFTER firing; turns shorter
than 15 min leave prior one-shots pending → duplicate future wakes (linear
stacking, wake noise); also collides with the session-ender's never-re-arm
rule (README defect #6). Fix: "if a prior pacemaker is still pending, do
not stack a second (or delete it first)."

**U-5 (A-5) · MINOR — "PR READY immediately" is only safe where CI has a
hold gate.** On a repo with an auto-merge enabler but NO session gate,
READY-at-open arms auto-merge and the born-red card lands ALONE — the exact
KL-0 inversion documented in substrate-kit
.github/workflows/auto-merge-enabler.yml's own header (@ 8a544a63). All 8
current seats happen to pair enabler+gate or have neither, so latent — but
A claims to be sendable to ANY project. Fix: "READY immediately where a
session gate holds the merge; otherwise READY only at flip."

Verified-clean: paste body (line 7 → EOF) measures exactly **5,868 chars**
= the header's own claim (over its ~5,000 §6 budget, but self-flagged —
recorded as verified-honest, not a defect).

---

## 3. fleet-manager (FM)

**Verdict: BOOTS-WITH-WARNINGS.** File-existence sweep at 8056b7e — ALL
referenced files exist; `.claude/CLAUDE.md` correctly ABSENT (the SEAT
DELTA says so). Workflows = roster-freshness.yml + roster-regen.yml +
substrate-gate.yml, NO auto-merge enabler — exactly matching the CI block.
roster-freshness.yml verified BLOCKING on claude/* head branches, advisory
elsewhere. Live-GitHub claims verified: parked stack #88/#89/#91/#92 all
OPEN; #97 OPEN carrying the newer heartbeat; OQ-FM-ACTIONS-PR-PERMISSION at
docs/owner-queue.md:145; inbox grammar exactly as rail 2 warns (4 headers
still `status: new` with DONE-flip blocks below); failsafe cron
`30 */2 * * *` matches the census trigger + stagger table; cutover id
trig_01BKpsyoBzp1K1ob9H3iu1gM is the live failsafe per the #97 heartbeat.
Provenance byte-level: GEN-3 RIDER v5 diff-identical to superbot
docs/owner/next-round-founding-prompts-2026-07-11.md §2 @ 76d854d;
PERMISSIONS block diff-identical to projects/UNIVERSAL.md @ e801da5. Char
budget: startup body **7,497** ✓; seat block 1,382/1,383 (±1
trailing-newline, self-documented); assembled 7,499 ≤ 7,500 ✓.

**FM-1 (B-1) · MAJOR — the seat's DONE-WHEN is not reachable by the
instructions in ITS OWN file: the landing path it needs was added to A
after B froze.**
- Line (MISSION): "DONE-WHEN each wake: roster ≤4h at HEAD" + WORK ORDER 1
  done-when "roster-freshness green; generated-at ≤4h".
- Reality: fleet-manager has NO auto-merge enabler (verified workflow
  list), main is PR-only (branch protection, PR #92 body), Actions can
  neither push main nor create PRs (verbatim denial in PR #99 body, runs
  29168812645/29172287288), and the core CI forbids self-merge/self-arm.
  The ONLY proven in-fleet landing path is the founding-brief fresh-session
  dispatch sentence the integrator added to A on 2026-07-12 ("fm PR #99
  merged clean vs the same task denied twice relayed") — but the fm B file
  embeds pre-edit A@1915599 and does NOT contain that sentence (README
  A-line inheritance note explicitly defers it to "next regen"). A cold fm
  session following only its B file parks the roster PR READY+green forever
  and can never satisfy its own DONE-WHEN.
- Fix: regen fm B from post-#99 A now — fleet-manager is the one seat whose
  mission is unreachable without that exact sentence.

**FM-2 (B-2) · MINOR — WORK ORDER 1's parenthetical was already stale at
the prompt's own merge commit (hedged, so recoverable).** "gen #10 stranded
on bot/roster-regen — expect, or later" — PR #99 (head bot/roster-regen,
gen #10) MERGED 2026-07-12T00:39:40Z, 45 min BEFORE #98 landed this prompt
(01:24:13Z); gen #10 is on main (docs/roster.md@8056b7e) and the branch is
gone from origin. The hedge does its job. Fix: "(regen whenever the stamp
is >4h — prior gen may already be on main)".

**FM-3 (B-3) · MINOR — "product-forge is DARK — wake it before ORDERing"
names no wake mechanism for a repo that is explicitly NOT a seat.**
per-project/README.md §"Not seats": product-forge "awaits owner disposition
… PARKED here until the owner rules" — a literal-minded manager could
create a trigger/session for an unseated repo, pre-empting the owner. Fix:
"= don't ORDER it; route a disposition ask to the owner-queue instead."

**FM-4 (B-4) · MINOR — universal step 1 "(green expected)" vs the seat's
own verify.** check_roster_freshness.py exits nonzero at any wake where the
roster is >4h (most wakes); the EXPECTED-RED block covers the CI check by
name but the local verify run inherits "(green expected)" untouched
(instance of README defect #5). Fix: SEAT DELTA add "(roster script red at
boot = the stale-roster class, not a boot failure)".

---

## 4. self-improvement / substrate-kit (SI)

**Verdict: BOOTS-WITH-WARNINGS.** Verified-true where it counts:
`.claude/CLAUDE.md` ABSENT at 8a544a63; rail (4) "ORDER truth = status.md
`done=` line, never inbox `status: new`" EXACTLY right (all 14 inbox ORDER
headers still `status: new` while status.md records done=001…014 — without
this rail a cold session re-executes 14 done orders); rail (1) PRs #220 +
#238 both OPEN, both `do-not-automerge`, both owner-ratification parks;
WORK ORDER 1 registry claim exact (fleet-repos.txt blind to all five named
repos, pins 1.7.0–1.10.0 match, status.md's "all 9 vendored adopters at
v1.12.1" false fleet-wide exactly as the order says); WORK ORDER 2
line-number claim exact to the line (AGENT_ORIENTATION.md.tmpl lines
10/34); WALLS (OA-10 branch-delete 403; two old triggers with full ids in
status.md) verified. Char budget: body **7,485** ✓, seat block **1,381** ✓,
assembled 7,498 ≤ 7,500 ✓.

**SI-1 (C-1) · MAJOR — the expected-red gate is misnamed for the kit's OWN
repo: there is no check called "substrate-gate" on substrate-kit.**
- Line (rail 5): "EXPECTED RED: the kit's substrate-gate holds ADDED
  born-red cards red BY DESIGN — judge by the named gate job."
- Reality: substrate-kit@8a544a63 workflows = ci.yml, auto-merge-disarm.yml,
  auto-merge-enabler.yml, release.yml — NO substrate-gate.yml (that file
  ships to ADOPTERS; in-kit it exists only as .substrate/ci/substrate-gate.yml,
  a template fixture, ci.yml:174/189/212). The born-red hold is the
  "Session gate" STEP inside the required check named **kit-quality**
  (ci.yml:17-18, 221; the enabler header confirms), and two legacy-alias
  jobs ("Kit test suite", "Cold-adoption smoke") also fire red on a
  born-red PR (status.md; job 86589400731). A cold session told to judge by
  a job named "substrate-gate" finds none, sees THREE red checks, and
  plausibly treats the red kit-quality as a genuine failure — the exact
  misread the rail exists to prevent.
- Fix: "…holds born-red cards via the required **kit-quality** check (its
  Session-gate step; the two legacy-alias jobs red too) — adopters call
  this substrate-gate."

**SI-2 (C-2) · MAJOR — TRIGGER CUTOVER deletes the owner's standing daily
kit-lab loop and never re-arms or replaces its cadence.**
- Line (step 2): "delete_trigger each old id: expect the 06:00Z kit-lab
  daily + 2-hourly failsafe (#252/#253), or later → verify absent."
- Reality: the 06:00Z trigger (trig_01Jm57GAjNCFrYJn1oLMiYGE per
  status.md@8a544a63) is the fresh-session-per-fire daily lab loop,
  re-armed 2026-07-11T23:26Z per docs/operations/lab-loop.md, with a
  recorded owner kill-switch — an owner-facing standing routine, not a
  stale coordinator wake. The new prompt arms only the 2-hourly failsafe +
  15-min pacemaker; nothing inherits the daily lab cadence. Reversible
  (lab-loop.md holds the paste-ready re-arm recipe) but a silent
  owner-visible cadence loss.
- Fix: one clause: "the continuous coordinator SUBSUMES the daily kit-lab
  loop — record the subsumption in status" (or: "keep the kit-lab daily;
  delete only the failsafe").

**SI-3 (C-3) · MINOR — "branch claude/* or the enabler never arms" parses
two opposite ways.** Intended = imperative (verified against
auto-merge-enabler.yml conditions); misparse = "neither claude/* branches
nor the enabler ever arm" → a session parks every PR needlessly
(wrong-but-safe). Fix: "branch claude/* — otherwise the enabler never
arms."

**SI-4 (C-4) · MINOR — WORK ORDER 3 "release #1–#2" is under-specified.**
No referent named "release #1/#2" exists; the checkable done-when rescues
it. Fix: "cut the next release carrying orders 1–2, then upgrade the
laggards."

**SI-5 (C-5) · MINOR — the kit's verify command is unnamed and the obvious
candidate does not exist at HEAD.** No root bootstrap.py at 8a544a63
(dist/bootstrap.py only; README.md:78's `python3 bootstrap.py check
--strict` is adopter usage) — the most discoverable command fails
file-not-found; real suite = `python3 -m pytest tests/ -q` + ruff.
Recoverable via status.md. Fix: seat delta "verify = python3 -m pytest
tests/ -q (status.md health line is the precedent)".

---

## 5. superbot (SB)

**Verdict: BOOTS-WITH-WARNINGS (2 MAJOR / 3 MINOR).** Verified TRUE at
HEAD: superbot-next has NO `.claude/CLAUDE.md` at 80464ab (BROKEN BOOT set
real and handled); golden-parity red-by-design + required `gate` leg
confirmed verbatim by docs/status/README-first.md; named-gates.yml +
tools/check_parity_depth.py exist; plugins.lock.json pins
superbot-plugin-hello, which is a real EMPTY repo (409 "Git Repository is
empty"); ORDER 002 `status: new` + OWNER-ACTION 2 both live at HEAD (F1's
premise exact); superbot main latest push runs green; fm
docs/findings/enabler-install-verification-2026-07-11.md exists.

**SB-1 (A-1) · MAJOR — landing-path contradiction: seat doctrine says
self-arm, assembled core terminally forbids it.**
- Lines: core (verbatim in the paste): "NEVER call enable_pr_auto_merge or
  merge_pull_request on your OWN PR — the auto-mode classifier refuses …
  TERMINALLY on the first denial"; seat C WALLS: "superbot: enabler skips
  MCP-created PRs (Q-0127), self-arm passed #1936/#1974/#2003 (HYPOTHESIS:
  settings.json grants) — ONCE, deny-wins, else park READY+green".
- Reality it collides with: superbot's own binding `.claude/CLAUDE.md`
  @1ecc211 (Q-0127): "arm it yourself: call enable_pr_auto_merge right
  after creating the PR" — loaded automatically at boot in the superbot
  clone. A cold session holds three instructions: repo says ALWAYS
  self-arm MCP PRs, core says NEVER, seat block says ONCE-then-deny-wins —
  and the compressed "ONCE, deny-wins" tiebreaker's antecedent is ambiguous.
- Fix: one sentence in the seat C WALLS: "superbot repo CLAUDE.md (Q-0127)
  predates the core rule — for THIS seat: branch-push PRs rely on the
  enabler; MCP-created PRs get ONE self-arm attempt, first denial terminal,
  then park READY+green."

**SB-2 (A-2) · MAJOR — F1 "mark ORDER 002 DONE (append-block)" orders a
write the target repo's control contract forbids.**
- Line: "F1 … mark ORDER 002 DONE (append-block) …" (+ BOOT 3: "ORDER
  truth = the latest append-block/done= line").
- Reality: superbot-next control/inbox.md@80464ab header: "ONE writer: the
  manager. **Never edit this file** — report order progress in
  control/status.md (`orders: acked=… done=…`)." The seat's own C block
  agrees; no append-blocks exist anywhere in that inbox at HEAD. A literal
  session appends to a manager-owned file, violating the control bus it was
  just told to respect; a cautious one stalls on the contradiction.
- Fix: "mark ORDER 002 done via control/status.md `orders: done=002` (inbox
  is manager-owned)" — or, if append-blocks are the intended new fleet
  grammar, say so and amend the inbox header in the same PR.

**SB-3 (A-3) · MINOR — BOOT 1 orientation path is dead in superbot too:
docs/CAPABILITIES.md does not exist in menno420/superbot at 1ecc211.** The
parenthetical exempts only superbot-next, implying superbot has the full
triple; it has `.claude/CLAUDE.md` and docs/current-state.md but no
CAPABILITIES file. Fix: "(superbot: no CAPABILITIES.md — use docs/owner/* +
journal; superbot-next: none — BROKEN BOOT set)".

**SB-4 (A-4) · MINOR — F2 is already 100% complete at HEAD.** #196 CLOSED
(2026-07-11T23:59:31Z, unmerged), #206 CLOSED (23:59:32Z), #213 MERGED
(20:22:38Z), #217 MERGED (23:58:59Z), and control/claims/ at 80464ab
contains only README.md — the named claim file
codex-risk-review-prs-196-206.md is gone. The "expect X, or later" rider
technically covers it, but F2 reads as open work. Fix: prefix F2 "(verify
first — likely already discharged by #213/#217 + closes on 2026-07-11)".

**SB-5 (A-5) · MINOR — F1's "seed from examples/ if reachable" targets a
repo outside the declared writable set** ("Writable repos:
menno420/superbot + menno420/superbot-next (one PR = one repo)"); seeding
superbot-plugin-hello is a third-repo push. The "else ONE paste-ready ask"
escape hatch prevents a stall, but obey-the-roster vs obey-the-order is a
live fork. Fix: "(plugin-hello is write-permitted for this order only)" or
route the seed through the Ideas Lab seat.

---

## 6. superbot-world (SW)

**Verdict: BOOTS-WITH-WARNINGS (1 MAJOR / 4 MINOR) — every volatile fact it
asserts verified TRUE at HEAD.** PR #42 (the ordered merge): **SAFE TO
EXECUTE AS WRITTEN** — OPEN, non-draft, `mergeable_state: "clean"`, base
main@76be821, head 2557f1a on branch
security/oauth-csrf-snapshot-validation (branch name exact); `fff0caa` is a
real intermediate commit → "green @ fff0caa, or later" is precisely right;
checks at 2557f1a: substrate-gate success, pytest success,
enable-auto-merge **skipped** (confirming "mineverse enabler arms claude/*
branches ONLY"); the PR body's "Owner action — this PR GATES secret
provisioning" section exists verbatim. #31 OPEN, `mergeable_state:
"blocked"`, stale base 4be012e. Also verified: mineverse HEAD 76be821 with
ZERO workflow runs at HEAD; heartbeat "IN FLIGHT: (none)" (STALE-HEARTBEAT
TRAP exact); mineverse CLAUDE.md denies auth exists while server/auth.py
ships (W1 re-render valid); games #50/#52/#53/#54/#55 ALL MERGED
(20:25–20:43Z 2026-07-11); exactly 5 stale claim files; idle has NO
test-running CI ("GREEN ≠ TESTED" real) and exactly **1,131 tests
collected** at c6a349d; PLATFORM-LIMITS.md at repo root as cited.

**SW-1 (B-1) · MAJOR — "idle = arm auto-merge at PR creation" contradicts
the assembled core's terminal NEVER-self-arm rule, and the conflict is
UNFLAGGED.**
- Lines: B "MERGE PATH IS PER-REPO: … idle = arm auto-merge at PR creation
  (fast-CI arming can fail both ways)"; C "idle arm-at-creation".
- Reality: the same paste's core says "NEVER call enable_pr_auto_merge … on
  your OWN PR — … TERMINALLY on the first denial", and superbot-idle has NO
  auto-merge-enabler workflow at c6a349d (only substrate-gate.yml +
  theme-gate.yml). Obey the seat → risk a terminal classifier denial on the
  very first idle PR; obey the core → every idle PR parks READY+green
  forever with no landing path. The superbot seat flags its equivalent
  conflict (HYPOTHESIS marker); this seat does not.
- Fix: "idle: arm-at-creation is recorded practice predating the core rule
  — attempt ONCE, first denial terminal, then park READY+green +
  owner-queue" (mirrors the superbot seat's pattern).

**SW-2 (B-2) · MINOR — BOOT 1's orientation path is dead in 2 of 3
repos.** superbot-games and superbot-idle have NO `.claude/` directory at
HEAD; only mineverse has the file. Recoverable (falls through to
current-state.md, which exists in both); README defect-queue #2 names the
class but this seat, unlike superbot's BROKEN-BOOT patch, didn't scope it.
Fix: "(games/idle: no CLAUDE.md — start at docs/current-state.md)".

**SW-3 (B-3) · MINOR — W3 "re-stamp the heartbeat" vs the role brief's
"games/idle status files are pre-merge ARCHIVES: read, never resurrect".**
W3 orders a WRITE to games control/status.md; the identity line forbids
resurrecting it. The intended reading (truth-fix ≠ resurrect-as-live) is
reachable but not stated. Fix: W3 → "truth-stamp games status.md ONCE
(archival correction, not a live heartbeat resumption)".

**SW-4 (B-4) · MINOR — W1 "you are NOT its author" can fight the visible
GitHub data.** PR #42's GitHub `user` is menno420 — the same account every
fleet session writes as; a cold session comparing "its author" to the API
field sees itself as the author-account and may refuse the landing attempt.
Fix: "(authorship is per-SESSION, not per-account: #42 was authored by a
different session — a genuine review from this session satisfies the
two-party path)".

**SW-5 (B-5) · MINOR — mission DONE-WHEN bakes "idle's 1131 tests gate PRs
in CI" — exact today (verified) but a baked volatile count in a DONE-WHEN;
suite growth makes the mission literally unsatisfiable-as-written.** Fix:
"idle's full pytest suite (~1.1k tests) gates PRs in CI".

---

## 7. game-lab (GL)

**Verdict: BOOTS-WITH-WARNINGS (0 MAJOR / 3 MINOR) — cleanest of the
nine.** Verified TRUE at HEAD: pokemon-mod-lab is PRIVATE (live API
object); pml has NO root .gitignore at 08d2611 (W1's ask real); gba
tools/setup-toolchain.sh + docs/PLATFORM-LIMITS.md + headless-boot.yml +
rom-builds.yml + committed dist/ ROMs all exist (binary-policy split
accurate); pml vendored agbcc/ + pokeemerald/ + rom-builds.yml +
substrate-gate.yml; CONSTITUTION.md + control/{inbox,status}.md +
bootstrap.py in BOTH repos; BOOT 1's "(no root CLAUDE.md — expected)" is
CORRECT for both repos — this seat pre-patched the dead-orientation-path
class; cron `15 */2 * * *` valid + collision-free per the README table;
ARM-JSON shapes match real schemas. TRACK-ISOLATION rail probed: no
misreading found that permits a leak.

**GL-1 (C-1) · MINOR — R22's "verify pml via a real API get-repo call"
names no tool that exists, while the same prompt walls the obvious
fallback.** The github MCP toolset has NO get-repository tool; visibility
is reachable via `search_repositories` (repo:menno420/pokemon-mod-lab →
`visibility` field — verified working this audit) or `gh api` (which the
prompt itself says is proxy-walled in this seat). R22 runs EVERY session
before private work; a cold session can burn its first minutes
rediscovering the path or mis-declare a wall and stall the Track B lane.
Fix: name the call: "verify via github-MCP search_repositories
(repo:menno420/pokemon-mod-lab → visibility field); raw api.github.com is
proxy-walled — do not curl".

**GL-2 (C-2) · MINOR — W2 "read the LIVE required-check sets" is likely
capability-walled.** Fleet evidence: mineverse PR #42 body records "I could
not read the branch-protection ruleset directly … the branch-protection API
is gated"; the reliable proxy is a real PR's required check-runs. Fix:
"read the LIVE required set (via a probe PR's check-runs if the ruleset API
is gated)".

**GL-3 (C-3) · MINOR — W1's done-when "merged; cards comply" is singular
across a two-repo deliverable** (card convention + pml .gitignore span both
repos under "one PR = one repo" → two PRs); "merged" (singular) invites
shipping only the pml half. Fix: "Done-when: both PRs merged (one per
repo); cards comply".

---

## 8. websites (WS)

**Verdict: BOOTS-WITH-WARNINGS.** Boot walk: repo files all exist at
8f97654 (full orientation triple, control bus, docs/owner/OWNER-ACTIONS.md,
app/owner.py, bootstrap.py, review/ + all four test trees). The verify line
quoted in the rails is **byte-identical to CI** (quality.yml:189); "(green
expected)" truthful (last 3 quality runs on main all success, incl. HEAD run
29170701465). CLAUDE.md at HEAD really is stale (order 3 genuinely needed).
Order 1 targets real: status.md still lists the PR #141 merge-click ask
although #141 merged 2026-07-11T20:24Z; the prune list names ~14 branches
while only 7 remote heads exist. Order 2 premise verified in source:
app/owner.py:105 POST /actions/refresh and :118 POST /actions/rerun-ci sit
behind HTTP Basic with no CSRF/Origin check. Stranded
bake/review-data-20260711-202653 branch exists.

**WS-1 (W1) · MAJOR — misleading CI-state claim on a load-bearing order,
contradicted by the run list.**
- Line: "REVIEW-BAKE is EXPECTED-RED, owner-walled: the 05:23Z cron dies
  daily on the Actions-can't-create-PRs wall (run 29167034060; fix = owner
  Settings toggle)"
- Reality: review-bake.yml has **exactly ONE run ever** — run 29167034060,
  `event: workflow_dispatch` (manual), failure, 2026-07-11T20:26Z. The
  05:23Z **cron has never fired**: the workflow only landed on main
  2026-07-11T20:24Z and the first scheduled slot (2026-07-12T05:23Z) had
  not yet occurred at test time (01:34Z). "Dies daily" is an unverified
  extrapolation stated as fact, and the adjoining "Never re-probe" pushes
  the session to queue an owner ⚑ asserting a false pattern — while the
  prompt's own LANDING rule ("Verify crons BY EVENT TYPE in the run list —
  manual runs mask a dead schedule") would expose it. The wall itself is
  real (workflow uses `gh pr create` from Actions; permissions block at
  review-bake.yml:38).
- Fix: "the only bake run (29167034060, manual dispatch) failed on the
  Actions-can't-create-PRs wall; the daily 05:23Z cron is UNTESTED — verify
  by event type before writing the ⚑."

**WS-2 (W2) · MINOR — heartbeat/prompt contradiction on the trigger to
delete.** boot 2 orders deleting the v1-era 4-hourly wake; control/status.md
@ 8f97654 says the opposite ("the 4-hourly ORDER 008 trigger STAYS ARMED
(not this chain's to disarm)"). The prompt is the newer owner intent, but a
truth-hierarchy-obedient session ("source at HEAD wins") could refuse. Fix:
add "(supersedes the status.md 'STAYS ARMED' line — that was the OLD
chain's constraint)".

**WS-3 (W3) · MINOR — seat re-activation vs owner-parked state,
unacknowledged.** Status phase is "CLOSING — the Q-0265 chain is PARKED
(owner archive-prep order)"; the prompt re-arms continuous mode without
mentioning it overrides that owner order. Recoverable (the paste itself is
the owner turn); one clause removes the hesitation.

**WS-4 (W4) · MINOR — no trigger-id given for the old wake** (boot 2
identifies it by description only); the session must fish it out of a
>200-trigger paginated registry by name/prompt text. Workable, slower than
an id slot (trading/venture show the better pattern: explicit ids marked
volatile).

---

## 9. venture-lab (VL)

**Verdict: BOOTS-WITH-WARNINGS (3 MAJOR / 4 MINOR).** Boot walk: control
bus + orientation docs exist in both repos; venture docs/PLATFORM-LIMITS.md
(cited @296a1a9, still present at b633db6 with the verbatim classifier
denials); trading scripts/grade_paper.py; "trading tests (223)" matches
trading status; grading trigger trig_015aNMg5ncoSE2Roe4MKjQnr
(`0 9 * * 5`, next 2026-07-17T09:05Z) and failsafe
trig_017o6azZTd9pzcaSthEncT5q corroborated by committed heartbeats; F1's
#51 (open, owner upload, HOT) and #57 (open READY, do-not-automerge, park
directive) verified; trading #64 open READY. Seat block 1,607 measured
exact (over fitted 1,383 by 224, self-flagged, under 1,883 hard).

**VL-1 (B1) · MAJOR — F1 orders landing a PR that is CLOSED at HEAD.**
- Line: "F1 STRANDED PRs — expect open #51 #57 #58 (venture-lab) + #64
  (trading): land #58 (born-red re-stamp; flip, rail 1)"
- Reality: venture-lab **PR #58 is CLOSED** (closed_at
  2026-07-12T00:36:42Z, not merged, `mergeable_state: dirty`) — superseded
  by the heartbeat-v2 PR whose content is already on main (status.md @
  b633db6: "PR #58 — SUPERSEDED-BY-THIS-PR (being closed)"). A literal
  session would re-open/re-land a dirty, superseded heartbeat — duplicating
  a wholesale status overwrite that already landed. The "expect …, or
  later" hedge covers the *existence* check but the action verb "land #58"
  is baked.
- Fix: "disposition every open PR in both repos against its close/park
  record (as of census: #51 HOT owner-only · #57 parked owner-merge · #58
  expected superseded-closed · trading #64, #65)".

**VL-2 (B2) · MAJOR — rail 1 encodes a merge-path world that HEAD has
already disproven.**
- Line: "MERGE PATH PER-REPO (split-brain): venture-lab NEVER
  self-merges/arms auto-merge (5+ denials; PLATFORM-LIMITS beats
  conventions.md rule 2) — park READY+green; coordinator squash ONLY on a
  genuine owner turn; parked = owner-merge only."
- Reality: at HEAD b633db6 the venture heartbeat headlines "Self-landing
  path — PROVEN LIVE (both repo settings ON)":
  .github/workflows/auto-merge-enabler.yml installed by PR #59 and **PRs
  #59/#60 self-landed on green via the server-side enabler** (merged by
  github-actions[bot] 2026-07-11T23:55Z / 2026-07-12T00:21Z). "Never
  self-arm/self-merge" remains correct, but "parked = owner-merge only" is
  now false for ordinary green claude/* PRs — a rail-obedient session files
  owner-merge ⚑s for PRs that land themselves, re-creating the stranded-PR
  queue this seat is supposed to clear.
- Fix: "venture-lab: open READY on a claude/* branch, do NOTHING
  merge-related — the installed enabler lands it on green (proven #59/#60);
  never self-arm/self-merge; owner-park labels (do-not-automerge) stay
  owner-merge."

**VL-3 (B3) · MAJOR — "KEPT — rebind" on the grading trigger is
self-contradictory and schema-impossible as worded.**
- Lines: boot 2: "grading trigger trig_015aNMg5ncoSE2Roe4MKjQnr
  ("0 9 * * 5") is KEPT — rebind per F2 first → verify absent." · F2:
  "rebind the grading cadence into THIS session (boot 2), record ids in
  trading status"
- Reality: `update_trigger` has **no session-binding parameter** (schema:
  trigger_id, name, cron_expression, run_once_at, enabled only) — a trigger
  cannot be moved to a new session; the only "rebind" is
  create-new-in-THIS-session + delete-old. "Is KEPT" invites the losing
  read: leave trig_015aNMg5… bound to the PRIOR money-seat coordinator;
  when that chat archives, it dies silently and the 2026-07-17 grading pass
  loses its executor — the exact ⚑ (g) incident class F2 exists to prevent.
  The dangling "→ verify absent" after the KEPT clause worsens it.
- Fix: "grading cadence: create a NEW weekly trigger (0 9 * * 5,
  grade_paper.py prompt) bound to THIS session, verify via list_triggers,
  THEN delete trig_015aNMg5… — session binding cannot be updated in place."

**VL-4 (B4) · MINOR — F1's disposition set is already incomplete:** trading
**PR #65** (enabler install, open, parked READY+green, created
2026-07-12T00:04Z — post-census) is not in the list; "done-when: all four
dispositioned" leaves it stranded. Covered generically by the VL-1 fix.

**VL-5 (B5) · MINOR — boot 1 orientation path is dead in BOTH seat repos**
(no .claude/CLAUDE.md at venture b633db6 or trading ea22323) — README v3.1
defect #2 confirmed live, no SEAT-DELTA patch here (ideas-lab patched it;
venture didn't). Also "conventions.md rule 2" — actual path is
docs/conventions.md.

**VL-6 (B6) · MINOR — F3 names the wrong repo as the stale heartbeat.**
"venture-lab's is wrong at HEAD (ARCHIVE-READY @ e7e5c9f)" — false: venture
status is fresh (2026-07-12T00:26:56Z, ACTIVE). It's **trading's** that is
stale (2026-07-11T19:33Z, still ARCHIVE-READY with ⚑ (g) "no executor"
although PR #64 + the venture heartbeat record ⚑ (g) RESOLVED). "Re-stamp
both" is safe either way.

**VL-7 (B7) · MINOR — venture's 4b PACEMAKER lacks the "the session ender
instead CLOSES the chain — it never re-arms" clause** that websites (line
27) and ideas (ENDER SPLIT) carry — README defect #6 unpatched in exactly
this seat.

---

## 10. ideas-lab (IL)

**Verdict: BOOTS-WITH-WARNINGS (3 MAJOR / 3 MINOR) — heaviest staleness of
the nine: 3 of the 4 FIRST WORK ORDERS are already done or premise-false at
HEAD.** Verified-good: idea-engine files all exist at 4f50cce; sim-lab
exactly as described (root CONSTITUTION.md + PLATFORM-LIMITS.md, no
.claude/); numbering-map citation exact (sim-lab docs/current-state.md:74 @
98394cb); branch-delete wall citation exact (idea-engine
docs/CAPABILITIES.md:51); PR #209 exists; WORK ORDER 3 premise TRUE
(sim-lab has only substrate-gate.yml, no enabler); fm PRs #88/#89/#91
confirmed open+parked. **The tasked expected-red check — RAN LIVE:** on the
local clone ff-pulled to origin/main 4f50cce, `python3 bootstrap.py check
--strict` → **exit 0**, and `python3 scripts/preflight.py` → **exit 0, "all
10 checks green"**. The exit-2 break was fixed by **PR #221 / commit
329547d** (merged 2026-07-11).

**IL-1 (I1) · MAJOR — EXPECTED-RED rail + WORK ORDER 1 describe a gate
that is GREEN at HEAD.**
- Lines: "EXPECTED-RED: idea-engine's substrate-gate (scripts/preflight.py)
  exits 2 at HEAD (roster `↳` rows; expect this, or later) — EVERY PR there
  opens red until WORK ORDER 1 lands." · "1. FIX THE GATE … DONE-WHEN:
  preflight exit 0 at HEAD, merged green. Precedes ALL content work." ·
  calibration recital repeats it; CI seat block repeats it.
- Reality: exit 0 at 4f50cce (run live); the fix already merged as PR #221.
  Three hazards: (a) the first work order and the calibration recital are
  dead weight; (b) boot 1's "(green expected)" and rail 1 flatly
  contradict, and the seat is told the rail wins; (c) worst, "That ONE red
  is expected" trains the session to discount a substrate-gate red that
  would now be REAL (the only by-design red left is the born-red card
  hold).
- Fix: "GATE: green since PR #221/329547d; if substrate-gate reds on a
  roster change (fm #88–#91 reshape it), fix check_sections forward — the
  only by-design red is the born-red card hold."

**IL-2 (I2) · MAJOR — WORK ORDER 2 orders re-doing a verdict that is
already finalized and fanned in.**
- Line: "2. CLOSE THE ORPHANED HANDOFF: PROPOSAL 010 … is sim-ready +
  unverdicted — the 2026-07-11 double archive orphaned it; nothing pulls it
  unless YOU do. Pull as INTAKE … sim, verdict via the fan-in. DONE-WHEN:
  VERDICT in sim-lab control/outbox.md, manager-addressed."
- Reality at HEAD: sim-lab control/outbox.md @ 98394cb line 131 — "##
  VERDICT 012 · 2026-07-12T01:30:00Z · status: finalized … idea:
  idea-engine PROPOSAL 010 … verdict: approve"; sim-lab status: "PROPOSAL
  010 consumed → VERDICT 012 … 12 verdicts finalized (V001–V012)"; fan-in
  already merged on idea-engine main (PR #227 @ 3eefb13). "Nothing pulls it
  unless YOU do" is emphatically false. Literal execution appends a
  DUPLICATE verdict to an append-only outbox and corrupts the very
  PROPOSAL↔VERDICT offset map the seat's own NUMBERING rail guards.
- Fix: "verify PROPOSAL 010's verdict chain closed (expect VERDICT 012 +
  fan-in #227, or later); if truly unverdicted, pull as INTAKE …".

**IL-3 (I3) · MAJOR — the dismantled-world premise is false: a LIVE prior
coordinator holds the seat.**
- Lines: boot 2: "delete_trigger each old id: expect ZERO (both lanes
  dismantled theirs at archive), or later — delete stragglers → verify
  absent" · WORK ORDER 4: "STALE-STATE SWEEP: heartbeats predate the
  archive ('P009 verdict owed' is stale — V010 exists) … DONE-WHEN: both
  re-stamped."
- Reality: idea-engine status @ 4f50cce is stamped **2026-07-12T01:21:57Z**
  (13 min before test), "phase: ACTIVE — continuous-chaining live
  (Q-0265)", failsafe **trig_01T83UuVthszGBcENYwrTrm7** (`0 */2 * * *`)
  live + a send_later chain alive; sim-lab status stamped 2026-07-12T00:58Z,
  ACTIVE, correct through V012; the string "P009" appears **zero** times in
  either heartbeat. WORK ORDER 4's done-when makes the session rewrite two
  fresh, correct heartbeats; boot 2's "delete stragglers" — executed while
  the prior coordinator still chains — kills a live sibling's deadman
  failsafe and puts two writers on one status.md (one-writer violation).
- Fix: boot 2 → "expect the prior coordinator's failsafe (status.md routine
  line names it) — confirm the prior chat is archived/parked (status stamp
  + list_events if reachable) BEFORE deleting; then rebind-then-delete as
  usual"; WORK ORDER 4 → "sweep heartbeat ⚑/ask rows against live GitHub;
  re-stamp only what contradicts".

**IL-4 (I4) · MINOR — WORK ORDER 1 cites "parked fm PRs #88–#91 reshape
it": #90 is merged** and unrelated (substrate-kit v1.12.1 upgrade); the
roster-reshaping parked set is #88/#89/#91 (verified open, stacked).

**IL-5 (I5) · MINOR — "Heartbeat home: control/status.md in idea-engine —
you are its only writer" (singular)** sits awkwardly against WORK ORDER 4's
"both re-stamped" and the CI block's "CONTROL BUS, per repo" — the seat
writes sim-lab's status too. Say "its only writer (and sim-lab's, as the
merged seat)".

**IL-6 (I6) · MINOR — the live legacy failsafe (`0 */2 * * *`, even :00)
collides with self-improvement's proposed stagger slot** in the README
table until cutover completes — invisible to a session holding only this
prompt; a one-line "the old cron squats another seat's slot — cutover
promptly" would motivate boot-2 ordering.

---

## 11. Cross-cutting findings

**(a) The landing-path / self-arm contradiction is the single biggest
defect class.** The assembled core says, verbatim in every paste: "NEVER
call enable_pr_auto_merge or merge_pull_request on your OWN PR … TERMINALLY
on the first denial" — and three seats then contradict it, each
differently, none with a stated tiebreaker strong enough for a cold
session: superbot's binding repo CLAUDE.md (Q-0127 @ 1ecc211) says ALWAYS
self-arm MCP-created PRs (SB-1); the superbot-world seat orders "idle = arm
auto-merge at PR creation" on a repo with NO enabler workflow, unflagged
(SW-1); and venture-lab's "parked = owner-merge only" rail is disproven at
HEAD by enabler-landed PRs #59/#60 (merged by github-actions[bot],
2026-07-11T23:55Z / 2026-07-12T00:21Z; VL-2). Related: fleet-manager's
DONE-WHEN is unreachable because its seat file froze before the core gained
the fresh-session dispatch landing path (FM-1). One doctrine — "enabler
where installed; ONE self-arm attempt where recorded practice predates the
core rule, first denial terminal; park + owner-queue otherwise" — stated
once in the core and specialized per seat, would retire 4 of the 15 MAJORs.

**(b) Hours-scale census decay.** Facts baked on 2026-07-11/12 draft night
were already overtaken when the prompts shipped (#98 merged
2026-07-12T01:24:13Z): venture PR #58 closed/superseded 00:36:42Z (VL-1);
ideas-lab PROPOSAL 010 already VERDICT 012 + fan-in PR #227 (IL-2);
idea-engine's expected-red exit-2 gate already exit-0 GREEN at 4f50cce via
PR #221/329547d (IL-1); websites' cron-death claim misattributes a single
manual `workflow_dispatch` failure (run 29167034060) to a daily cron that
has never fired (WS-1); fleet-manager's own gen-#10 fact was stale at the
prompt's own merge commit — PR #99 merged 45 minutes BEFORE #98 landed the
prompt asserting it stranded (FM-2); superbot F2's four PRs were all
closed/merged by 23:59Z (SB-4); trading PR #65 post-dates the census
(VL-4). The "expect X, or later" hedge covers existence checks but not
baked action verbs ("land #58", "pull PROPOSAL 010"). The fix is
structural, not per-fact: bake state as **verify-at-boot steps with an
expected-as-of-date value**, never as bare assertions.

**(c) Dead `.claude/CLAUDE.md` orientation path in universal BOOT-1.** The
file is MISSING at fleet-manager@8056b7e and substrate-kit@8a544a63 (U-2),
at superbot-games and superbot-idle (SW-2), and at venture-lab@b633db6 and
trading-strategy@ea22323 (VL-5); superbot lacks the path's third element
docs/CAPABILITIES.md (SB-3). Seats that pre-patched it (game-lab's "(no
root CLAUDE.md — expected)", superbot's BROKEN-BOOT scope, ideas-lab) show
the fix pattern; the class belongs in the core (README v3.1 defect-queue #2
already names it — confirmed live here).

**(d) Gate-name mismatches.** substrate-kit has NO check named
"substrate-gate" — the born-red hold is the **Session gate step of the
required kit-quality check** (ci.yml:17-18, 221), plus two legacy-alias
jobs that also fire red (SI-1). Expected-red rails must name the check a
cold session will actually see in the PR's check list, per repo.

**(e) Schema-impossible instruction.** "Rebind" a trigger to a new session
is not a schema operation: `update_trigger` accepts only trigger_id / name
/ cron_expression / run_once_at / enabled — no session-binding parameter
(VL-3). The only real "rebind" is create-new-bound-to-THIS-session, verify,
then delete-old. Any prompt using "rebind/KEPT" wording invites leaving the
cadence bound to a dying chat.

**(f) Positives worth keeping.**
- The unslotted universal prompt genuinely does NOT stall: line 9's
  derive-and-proceed rule + self-describing slots answered the owner's
  stall question definitively.
- **All char budgets byte-exact** — every one of the 15 measured paste
  bodies/blocks matches its in-file claim and the README table (universal
  5,868 · core 6,117 · fm 7,497/1,382 · si 7,485/1,381 · superbot
  7,500/1,380 · world 7,431/1,380 · game-lab 7,498/1,382 · websites
  7,497/1,381 · venture 7,398/1,607 · ideas 7,498/1,383), ±1
  trailing-newline convention on the fm seat block.
- **All named tools/args real**: every MCP call named anywhere in the set
  exists with the claimed argument shapes (one wording nit: "bound session
  via list_triggers" may be vacuous for default self-bound triggers with
  empty persistent_session_id).
- **Mineverse PR #42 merge order verified SAFE**: open, non-draft,
  mergeable_state clean, substrate-gate + pytest green at head 2557f1a,
  enabler correctly skipped — the one live merge order in the set is exact
  as written, down to the branch name and the "or later" head hedge.
- Provenance shas verified byte-level (GEN-3 RIDER v5 @ superbot 76d854d
  diff-identical; PERMISSIONS v4 @ fm e801da5 diff-identical).
- Load-bearing truth rails verified TRUE and necessary: fm inbox grammar
  rail, substrate-kit "done= line beats status: new" rail (prevents
  re-executing 14 done orders), superbot-world's STALE-HEARTBEAT TRAP and
  "GREEN ≠ TESTED" (idle really has no test-running CI; exactly 1,131 tests
  collected).

---

## 12. Fix-priority table for the v3.1 finalize pass

| Priority | Defect id(s) | One-line fix | Owner-visible risk if unfixed |
|---|---|---|---|
| **P1** | SB-1, SW-1, VL-2, FM-1 (class a) | State ONE landing doctrine in the core (enabler where installed; ONE recorded-practice self-arm attempt, first denial terminal; else park + owner-queue), specialize per seat | A seat either burns a terminal classifier denial on its first PR or parks every PR forever — the manager seat literally cannot land its own roster (FM-1) |
| **P1** | FM-1 | Regen fm B from post-#99 A so the fresh-session dispatch landing sentence is in the seat file | The fleet-manager mission DONE-WHEN is unreachable as shipped |
| **P1** | VL-1, IL-1, IL-2, IL-3, WS-1, FM-2, SB-4, VL-4 (class b) | Refresh ALL census facts at send time and convert baked facts to "verify at boot; expected X as of <date>" rails — make recheck-at-boot the grammar, not the hedge | Sessions land closed PRs, duplicate finalized verdicts into append-only outboxes, kill live siblings' failsafes, and file owner ⚑s asserting false CI patterns |
| **P2** | SI-1 | Rename the kit's expected-red rail to the real check: kit-quality (Session-gate step) + two legacy-alias reds | Cold kit session misreads three red checks as genuine failure — the exact misread the rail exists to prevent |
| **P2** | SI-2 | Decide the kit-lab daily loop's disposition (subsume or keep) and say so in the cutover step | Owner's standing daily lab cadence silently disappears |
| **P2** | VL-3 | Replace "KEPT — rebind" with create-new → verify → delete-old (session binding is not updatable) | The 2026-07-17 grading pass loses its executor when the old chat archives |
| **P2** | U-1 | Unfilled OLD_TRIGGER_IDS slot → delete NOTHING guard | Unslotted paste deletes a sibling seat's live trigger |
| **P2** | SB-2 | ORDER-done grammar: status.md `done=` line, never inbox append (or amend the inbox header fleet-wide) | Sessions write to a manager-owned single-writer file, corrupting the control bus |
| **P3** | U-2/SB-3/SW-2/VL-5 (class c), U-3, U-4/VL-7, U-5, SI-3, SI-4, SI-5, FM-3, FM-4, SB-5, SW-3, SW-4, SW-5, WS-2, WS-3, WS-4, GL-1, GL-2, GL-3, VL-6, IL-4, IL-5, IL-6 | Batch the MINORs: core orientation-path fallback clause, per-seat verify names + designed-red scoping, pacemaker no-stack clause, wording disambiguations, id slots for old triggers, tool-name corrections (search_repositories for GL-1) | Each is minutes of confusion or a wrong-but-safe park per session — cheap individually, but 29 of them compound across every wake of every seat |

---

*Slice sources: three QA worker reports (A: universal/fleet-manager/
self-improvement · B: superbot/superbot-world/game-lab · C: websites/
venture-lab/ideas-lab), consolidated 2026-07-12 in session
qa-boot-sim (PR #102). Counts cross-checked against each report's own
summary table; no discrepancies found.*
