# Launch-package inventory — game lanes, codetool archives, new core seats

> Worker slice of the PROJECT-PACKAGE CENTRALIZATION inventory (owner dispatch
> 2026-07-10 ~20:50Z). READ-ONLY pass; all citations are `file @ repo-HEAD-SHA`
> at inventory time (2026-07-10 ~21:0xZ). The four-part package being
> centralized in fleet-manager: (1) Custom Instructions for dispatched working
> agents, (2) coordinator/startup prompt (continuous loop, Q-0265), (3) env
> setup script, (4) failsafe cron text.

## Repo discovery result

- `menno420/idea-engine` — **EXISTS** (pushed 2026-07-10T20:43Z). Added via
  `add_repo`, cloned to `/workspace/idea-engine`, HEAD `3d654f249de8a20eb673b0a0fefdc5c8124ce348`.
- `menno420/sim-lab` — **EXISTS** (pushed 2026-07-10T20:36Z). Added via
  `add_repo`, cloned to `/workspace/sim-lab`, HEAD `8b8075dba79474df5e99e01e66fbd4877f2b4da3`.
  (The seed commit the dispatch mentioned — 32dc75d — is in this repo's history;
  shallow clone at HEAD, seed confirmed via `.sessions/2026-07-10-seed.md` +
  `control/status.md` "seeded 2026-07-10 by the dispatch copilot".)
- `menno420/product-forge` — already in session scope; clone at
  `/workspace/product-forge`, HEAD `c93c0e321007d2133b9f301c0ee4f2b127efd272`.
- No other similarly-named repos under menno420 (full `list_repos` sweep, 17 repos).

HEAD SHAs used throughout:

| repo | HEAD |
|---|---|
| pokemon-mod-lab | `a76ada70cb0b` |
| gba-homebrew | `bc73da7` (fast-forwarded local from b607365; delta was PR #26 kit v1.7.0 upgrade only) |
| codetool-lab-fable5 | `a6cf1a9d5e8b` |
| codetool-lab-opus4.8 | `80f6cd102ef6` |
| codetool-lab-sonnet5 | `66c3dfc79735` |
| product-forge | `c93c0e32` |
| sim-lab | `8b8075db` |
| idea-engine | `3d654f24` |

---

## 1. pokemon-mod-lab (game-lab Track A) @ a76ada7

**Project state:** LIVE-PARKED. `control/status.md @ a76ada7`: "LANE PARKED —
overnight run complete: sessions 001–008, PRs #2–#10 all merged on green;
ORDER 001 done… awaiting owner direction." 3 ⚑ owner asks carried (required-check
click, concept pick, playtest).

**Artifacts found:**
- `CONSTITUTION.md @ a76ada7` — kit-generated working agreement + autonomy rails
  (binding; carries Understand-and-reflect, decide-and-flag, etc.). Kit v1.6.0
  vintage (`control/status.md` kit line: v1.6.0).
- `.substrate/claude/CLAUDE.md @ a76ada7` — **UNRENDERED template** (banner:
  "UNRENDERED SLOTS BELOW — run bootstrap.py ask"; `${primary_language}` etc.
  unfilled). Staged, never installed as `.claude/CLAUDE.md` (no `.claude/` dir
  in repo).
- `control/README.md @ a76ada7` — the manager↔lane protocol **including "The
  standing ritual (every session, every wake)"** — this is the closest thing to
  a committed coordinator-loop prompt for the lane (inbox-at-HEAD first,
  heartbeat-before-work, status-last with re-read). But it is the *ritual*, not
  the deployed Project instruction text.
- `control/inbox.md @ a76ada7` — ORDER 002 (status: new, P1) "SELF-ARM YOUR WAKE
  ROUTINE… cadence hourly, prompt: 'Read control/inbox.md at HEAD and run the
  standing ritual from your instructions.'" — **a de-facto wake-prompt text
  recorded in-repo, but UNEXECUTED**: `status.md` orders line = "ORDER 001 —
  DONE… no [other] order consumed". ORDER 003 (visibility=private verify) also
  unexecuted.
- Founding package: **pointer only** — inbox ORDER 001 cites
  `menno420/fleet-manager docs/prompts/game-lab-founding.md § ORDER 001` as the
  verbatim source. No founding-package copy committed in-repo.
- Custom Instructions (the actual Project paste): **NOT committed anywhere**
  in-repo. `docs/retro/QUESTIONS.md` references them; `docs/CAPABILITIES.md @
  a76ada7` line 54 records only "Environment / routine / Project creation:
  owner-click actions" (a wall, not the text).
- Env setup: **no repo-level env setup script.** Vendored build scripts only
  (`agbcc/build.sh`, `pokeemerald/build_tools.sh` — toolchain build, not session
  setup). `.substrate/hooks/settings.template.json` + README = kit hook template
  (advisory hooks; not installed — no `.claude/settings.json`).
- Failsafe cron: **none** recorded.

**Classification:** TYPE = kit CONSTITUTION + control protocol + unexecuted
wake-order text. CURRENT-vs-OUTDATED = **OUTDATED vs Q-0265**: ORDER 002's
hourly discrete-wake prompt is the pre-continuous-mode model; kit still v1.6.0;
staged CLAUDE.md unrendered. DEPLOYED-STATE = **unknown** (no trigger-recorded
routine; ORDER 002 never acked; whatever Custom Instructions the live Project
has are not in git).

**Missing for the four-part package:** all four. (1) working-agent Custom
Instructions not committed, (2) coordinator/continuous-loop prompt absent
(only the per-wake ritual + a stale hourly-wake ORDER text), (3) no env setup
script, (4) no failsafe cron text.

---

## 2. gba-homebrew (game-lab Track B) @ bc73da7

**Project state:** LIVE-PARKED (same shared game-lab lane, per-repo inbox).
`control/status.md @ bc73da7`: session 7 complete, Lumen Drift SCOPE-COMPLETE,
ORDER 001 done, ⚑ concept pick pending. Kit **v1.7.0** (PR #26 upgrade, merged
after the status write).

**Artifacts found:**
- `CONSTITUTION.md @ bc73da7` — same kit working agreement as Track A (binding).
- `.substrate/claude/CLAUDE.md @ bc73da7` — **RENDERED** by the v1.7.0 upgrade
  ("gba-homebrew — game-lab Track B: original GBA homebrew on Butano — agent
  working agreement", Status: binding). Still staged-only (no `.claude/` dir).
  Note the asymmetry with Track A's unrendered copy.
- `control/README.md @ bc73da7` — same protocol + standing ritual as Track A.
- `control/inbox.md @ bc73da7` — same ORDER 002 self-arm-hourly-wake text
  (status: new, issued 2026-07-10, **unexecuted** — status orders line:
  "acked=001 done=001 · no new orders at HEAD (inbox re-read 07:14Z)"; ORDER 002
  landed at the repo ~20:20Z, after that re-read — lane hasn't seen it). Also a
  committed "Standing default (between orders)" paragraph — a between-orders
  loop fragment usable as coordinator-prompt raw material.
- Founding package: **pointer only** → fleet-manager
  `docs/prompts/game-lab-founding.md` (via inbox ORDER 001).
- Env setup: **`tools/setup-toolchain.sh` @ bc73da7** — idempotent, PINNED
  toolchain installer (devkitARM r68 via leseratte10 mirror because devkitPro
  infra is Cloudflare-403 behind the fleet proxy — documented wall,
  `docs/PLATFORM-LIMITS.md`; Butano 21.7.1 pinned). This is the best
  environment-setup artifact in the games slice, but it is a *toolchain*
  installer, not the fleet defensive setup-universal shim.
- Failsafe cron: none recorded.

**Classification:** TYPE = kit CONSTITUTION (rendered staged CLAUDE.md) +
control protocol + toolchain setup script + unexecuted wake-order text.
CURRENT-vs-OUTDATED = **OUTDATED vs Q-0265** (same hourly-wake ORDER text;
standing-default is per-wake, not continuous-loop). DEPLOYED-STATE =
**unknown** (no trigger recorded; ORDER 002 unseen/unexecuted; Project Custom
Instructions not in git).

**Missing:** (1) Custom Instructions text, (2) coordinator/continuous prompt,
(4) failsafe cron. (3) partially present — `tools/setup-toolchain.sh` covers
the toolchain but there is no session-env setup-universal adoption.

---

## 3. codetool-lab-fable5 @ a6cf1a9 — ARCHIVE tier

**Project state:** NONE (wound down 2026-07-10; no active Project). Packages
are documentation for a hypothetical gen-3 successor only.

**Artifacts (the succession pack doubles as a future-seat package):**
- `docs/succession/NEXT-BOOT.md @ a6cf1a9` — full gen-2 boot sequence
  (heartbeat-before-work → read order → walking skeleton → work) = **de-facto
  future startup prompt**, discrete-session model.
- `docs/succession/custom-instructions-proposal.md @ a6cf1a9` — KEEP/DROP/ADD
  rewrite of the founding Custom Instructions, blueprint-aligned
  (READY-never-draft, merge authority written, walls up front, heartbeat).
  **Proposal, not deployed text.**
- `docs/succession/PLATFORM-LIMITS.md`, `ENVIRONMENT.md`, `gen2-feedback.md`
  @ a6cf1a9 — walls with exact error text + env spec.
- Env setup: `environments/setup-universal.sh @ a6cf1a9` (copy of fleet
  canonical `fleet-manager environments/templates/setup-universal.sh`, R15
  always-exit-0 contract) routing to `scripts/env-setup.sh` (repo-specific
  editable install, non-fatal). **The most complete env-setup pair in this
  slice.**
- `control/inbox.md @ a6cf1a9` line 14 (ORDER 002-ish ping) + line 26 (ORDER
  004 latency ping) record fleet conventions verbatim but no wake-routine
  prompt (this lane predates routine self-arming).
- Original founding Custom Instructions: **not committed** (the proposal quotes
  fragments; opus4.8's coordinator even notes it never saw the lane's full CI
  text).

**Classification:** TYPE = succession pack (NEXT-BOOT startup prompt + CI
proposal + env spec + setup scripts). CURRENT-vs-OUTDATED = **OUTDATED vs
Q-0265 by design** (discrete-session gen-2 model; predates continuous mode and
Q-0264 pipeline). DEPLOYED-STATE = n/a — nothing deployed; ARCHIVE.

**Missing (if ever revived):** (1) actual founding CI text never committed —
only the proposal; (2) coordinator prompt is discrete-wake NEXT-BOOT, needs
Q-0265 continuous rewrite; (4) no failsafe cron text. (3) env setup is DONE
(setup-universal.sh + env-setup.sh, tested contract).

---

## 4. codetool-lab-opus4.8 @ 80f6cd1 — ARCHIVE tier

**Project state:** NONE ("wind-down complete — ready for archive + fresh
session", control/status.md @ 80f6cd1).

**Artifacts:**
- `docs/succession/NEXT-BOOT.md @ 80f6cd1` — richest of the three (read order
  with per-line why, walking-skeleton check, merge-authority probe §5) =
  future-seat startup prompt, discrete model.
- `docs/succession/PROPOSED-CUSTOM-INSTRUCTIONS.md @ 80f6cd1` — KEEP/DROP/ADD;
  carries the honest caveat that the coordinator **never saw the build lane's
  actual Custom Instructions text** (critique of *inferred* instructions).
- `docs/succession/ENVIRONMENT.md`, `GEN2-FEEDBACK.md` @ 80f6cd1.
- Env setup: `environments/setup.sh @ 80f6cd1` — defensive, always-exit-0,
  cwd-detecting (written as the fix for the sibling-lane setup-death: a session
  that died 10s after spawn, unnoticed ~2.8h).
- `control/inbox.md @ 80f6cd1` ORDER 001 quotes the founding relationship
  ("Execute the task in your Project Custom Instructions") — confirms the CI
  text lived only in the Project surface, never in git.

**Classification:** TYPE = succession pack. OUTDATED vs Q-0265 (discrete).
DEPLOYED-STATE = n/a; ARCHIVE.

**Missing:** same shape as fable5 — (1) real deployed CI text absent from git,
(2) continuous-loop prompt absent, (4) no failsafe cron. (3) present.

---

## 5. codetool-lab-sonnet5 @ 66c3dfc — ARCHIVE tier

**Project state:** NONE ("wind-down complete — ready for archive", status @
66c3dfc).

**Artifacts:**
- `docs/succession/NEXT-BOOT.md @ 66c3dfc` — gen-2 boot sequence (read order,
  walking skeleton with READY-never-draft callout, known walls §3).
- `docs/succession/PROPOSED-CUSTOM-INSTRUCTIONS.md @ 66c3dfc` — table-form
  KEEP/DROP/ADD with per-row gen2-blueprint alignment column (the most
  blueprint-integrated of the three proposals).
- `docs/succession/README.md @ 66c3dfc` — succession queue state (DONE /
  IN-FLIGHT / NEXT).
- Env setup: `docs/succession/setup-universal.sh @ 66c3dfc` — fleet canonical
  template adapted (pyproject editable + [dev] extra). NOTE: lives under
  docs/succession/, **no environments/ dir** — a gen-3 reviver must know to
  look there.
- `docs/succession/ENVIRONMENT.md`, `GEN2-FEEDBACK.md` @ 66c3dfc.

**Classification:** TYPE = succession pack. OUTDATED vs Q-0265 (discrete).
DEPLOYED-STATE = n/a; ARCHIVE.

**Missing:** (1) deployed CI text not in git, (2) continuous prompt, (4)
failsafe cron. (3) present but in a non-standard location.

---

## 6. product-forge @ c93c0e3 — core seat (Q-0259 r.4 + Q-0264)

**Project state:** SEEDED, **coordinator NOT booted yet** (status @ c93c0e3:
"Coordinator seat NOT booted yet… Owner items pending: Project creation +
package §1/§2 pastes"). ORDER 001 (games-web phase-1 mock prototype) already in
the inbox from the manager; a later commit at HEAD ("ORDER 001: build
products/games-web/ phase-1 mock-data prototype", c93c0e3) shows work starting.

**Seed contents (born-right, kit v1.7.0):** CONSTITUTION.md, CONVENTIONS.md
(day-0 landing rules incl. written merge-authority grant, Q-0258 post-merge
review), PLATFORM-LIMITS.md, control/{README,inbox,status}.md, bootstrap.py +
substrate.config.json + `.github/workflows/substrate-gate.yml` (gate observed
in status), claims/, review-queue.md, products/ skeleton, telemetry/, docs/
(CAPABILITIES, AGENT_ORIENTATION, owner-profile, question-router, etc.),
`.substrate/claude/CLAUDE.md` (**unrendered** staged template),
`.sessions/2026-07-10-seed.md`.

**Founding package:** pointer — `README.md @ c93c0e3` line 4: "Founding design:
superbot `docs/planning/round3-founding-package-product-forge-2026-07-10.md`"
(package §1 = Custom Instructions paste, §2 = coordinator boot incl. step 5
routine arm — per status.md's routine line). Not re-read here (superbot is
another worker's slice).

**Routine:** `control/status.md @ c93c0e3` routine line: "NOT armed — the
coordinator arms 'product-forge 2-hourly standing wake' (cron `0 */2 * * *`)
at its first boot per the founding package §2 step 5."

**Classification:** TYPE = kit seed + founding-package pointers.
CURRENT-vs-OUTDATED = **PARTIALLY OUTDATED vs Q-0265**: the recorded plan is a
2-hourly *standing wake* (discrete wakes), not the Q-0265 continuous
send_later-chain + *failsafe* model that idea-engine already cut over to.
Seeded before/at the Q-0265 cutover; the founding package §2 text in superbot
is the thing to re-check. DEPLOYED-STATE = **NOT DEPLOYED** (no Project, no
trigger, CI pastes pending owner).

**Missing:** (1) CI text = pointer only (superbot planning doc, not
centralized); (2) coordinator prompt = pointer only + pre-Q-0265 shape; (3) no
env setup script in-repo (no environments/, no setup-universal copy); (4) no
failsafe cron text (only the standing-wake cron plan).

---

## 7. sim-lab @ 8b8075d — core seat (Q-0264 evidence lane)

**Project state:** LIVE — "BOOT COMPLETE — continuous mode" (status @ 8b8075d);
ORDER 000 walking skeleton + verdict exemplar shipped (PRs #2–#4); INTAKE queue
holds 3 proposals pulled from idea-engine's outbox.

**Seed contents (born-right, kit v1.7.0):** CONSTITUTION.md, CONVENTIONS.md
(incl. the lane-unique @codex-before-finalization rule, Q-0264.4),
PLATFORM-LIMITS.md, control/{README,inbox,outbox,status}.md (inbox has the
two-appender ORDER/INTAKE extension per founding package §2/Q-0264),
bootstrap.py, substrate-gate CI (observed enforcing on PRs #2–#4), harness/,
sims/ (README + REFERENCE.md with the gen3_deployment_sim precedent), claims/,
review-queue.md, docs/ set, `.substrate/claude/CLAUDE.md` (**unrendered**),
`.sessions/2026-07-10-seed.md`. Founding pointer: `README.md @ 8b8075d` line 4
→ superbot `docs/planning/round3-founding-package-simulator-2026-07-10.md`.

**Routine / failsafe — the critical finding:** `control/status.md @ 8b8075d`
OA-003: failsafe routine **'sim-lab failsafe wake' (cron `0 1-23/2 * * *`, ODD
hours, offset one hour after idea-engine's even-hour output) =
owner-manual-pending** — the coordinator session has **neither create_trigger
nor send_later** ("tool not present in session toolset", verbatim), so the
continuation chain is ALSO unavailable on that seat, and — worst for
centralization — **"exact prompt text is in the coordinator's first reply"**,
i.e. the failsafe prompt exists ONLY IN CHAT, not committed anywhere.

**Classification:** TYPE = kit seed + live continuous seat + committed
routine-*state* (but not routine-*text*). CURRENT vs Q-0265/Q-0264 = **CURRENT
in design** (continuous mode, Q-0264 pipeline wired, odd/even cadence
coupling), but the failsafe is UNARMED and its text uncommitted.
DEPLOYED-STATE = Project live and producing; **failsafe NOT deployed**
(owner-manual-pending); pacemaker chain unavailable on this seat (tool gap) —
so the lane currently advances only on manual/owner-driven wakes.

**Missing:** (1) CI text = pointer only; (2) coordinator prompt = pointer
only; (3) no env setup script in-repo; (4) failsafe cron **text lives only in
a chat reply** — highest-priority capture item for the centralization: the
fleet package must own this text, and the cadence coupling (sim-lab odd hours
↔ idea-engine even hours) must be centralized as a *pair*, or one side's
change silently breaks the pipeline rhythm.

---

## 8. idea-engine @ 3d654f2 — core seat (Q-0264 origin)

**Project state:** LIVE and the most advanced seat — "STEADY — eleventh slice
shipping (PR #14)… mode: continuous — slices chained back-to-back per Q-0265";
outbox depth 3 with backpressure held until sim-lab pulls.

**Seed contents:** CONSTITUTION.md, control/{README,inbox,outbox,status}.md,
bootstrap.py, kit v1.7.0, claims/, review-queue.md, ideas/ tree (253 files,
10 sections), scripts/check_sections.py + check_ideas.py (+ --outbox mode),
docs/ set, `.substrate/claude/CLAUDE.md` (**unrendered**),
`.sessions/2026-07-10-seed.md` + `-first-probe.md`. **NOTE: no root
CONVENTIONS.md and no PLATFORM-LIMITS.md** (unlike sim-lab/product-forge —
earlier seed, Q-0264 v2 package); landing conventions live in `README.md § 
Landing conventions (gen-3 standard, day-0)` @ 3d654f2 line 91.

**Routine — the ONLY fully trigger-recorded deployment in this slice:**
`control/status.md @ 3d654f2` routine line records the Q-0265 cutover
VERBATIM: old wake deleted (`delete_trigger trig_01KBoHPaquSCDHysip67PQBh` →
confirmed), new failsafe created with the full call —
`create_trigger {"name":"idea-engine failsafe wake","cron_expression":"0 */2 * * *","prompt":"FAILSAFE WAKE (idea-engine, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD → inbox → slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending."}`
→ `trig_0178q9Je2xRFJgthwamrg9Br`, enabled, self-bound to coordinator session
`session_01TwoaFmWeB8pYbHMyFYgjqJ`, verified via list_triggers. Continuation
chain armed and alive.

**Classification:** TYPE = kit seed + live continuous seat + **verbatim
deployed failsafe text committed**. CURRENT vs Q-0265 = **CURRENT — the Q-0265
reference implementation** (this status line is the template the fleet package
should generalize). DEPLOYED-STATE = **DEPLOYED + trigger-recorded** (the only
one in this slice).

**Missing:** (1) CI text = pointer only (superbot founding package v2 +
Q-0264 ruling); (2) coordinator continuous-loop prompt as such not committed —
the failsafe text *sketches* it ("sync HEAD → inbox → slice after slice, each
merged-on-green") but the full §2 boot/loop prompt lives in superbot planning;
(3) no env setup script; (4) failsafe = PRESENT (committed verbatim). Also
missing vs siblings: root CONVENTIONS.md / PLATFORM-LIMITS.md.

---

## Cross-cutting: what the centralization must fix (this slice's view)

1. **No repo in this slice commits its deployed working-agent Custom
   Instructions.** Best available: codetool KEEP/DROP/ADD proposals (advisory),
   kit CONSTITUTION/staged-CLAUDE.md (working agreement ≠ Project CI paste),
   founding-package pointers into superbot docs/planning/ (round3 packages for
   the 3 core seats) and fleet-manager docs/prompts/game-lab-founding.md (games).
2. **Coordinator/continuous-loop prompt (Q-0265)**: only idea-engine runs it,
   and only its *failsafe* text is committed. sim-lab's equivalent is
   chat-only. Games + codetools are pre-Q-0265 discrete-wake shapes (hourly
   ORDER 002 texts / NEXT-BOOT docs).
3. **Env setup scripts**: codetools have the mature defensive pattern
   (fleet-canonical setup-universal.sh + repo shim, R15 always-exit-0);
   gba has a pinned toolchain installer; **pokemon and all three core seats
   have NONE in-repo.**
4. **Failsafe cron texts**: committed verbatim only in idea-engine.
   sim-lab's = chat-only + owner-manual-pending (create_trigger absent on that
   seat — seat-dependent tool availability is itself a wall the package must
   plan around, recorded in sim-lab PLATFORM-LIMITS.md). product-forge's is a
   pre-Q-0265 standing-wake plan. Games/codetools: none.
5. **Games program mapping (Q-0259 r5 = 3 dedicated game Projects):** current
   deployed structure is ONE shared game-lab lane across two repos with
   per-repo inboxes (`control/README.md` in both). Neither game repo references
   Q-0259 r5 yet (last substantive status writes 07:14/07:49Z predate it). The
   centralized package set must therefore plan **3 new per-game-project
   packages** (instructions + loop prompt + env + failsafe each), not a port of
   the single game-lab-founding.md prompt; the concept-pick ⚑s in both lanes'
   status files are the natural fork point. Track A additionally carries the
   visibility=private hard-rail order (ORDER 003) any new package must inherit.
6. **Cadence coupling**: idea-engine even-hour output ↔ sim-lab odd-hour pull
   (OA-003 text) is an inter-Project contract; centralize the pair, not two
   independent crons.
7. **Unexecuted self-arm orders**: both game lanes' ORDER 002 (self-arm hourly
   wake) is status:new and unexecuted — if fleet-manager centralizes routine
   texts, those orders are superseded and should be reconciled (they encode the
   OLD hourly model).
