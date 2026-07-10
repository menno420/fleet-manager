# Gen-2 PROPOSED founding package — websites

> **Status:** `plan` — **PROPOSED, not deployed** — drafted 2026-07-10 from the binding gen-2 blueprint (fleet-manager
> `docs/gen2-blueprint.md` §1–§2 + §2a, read at HEAD), playbook R21, the lane's OWN succession
> pack (`docs/succession/proposed-custom-instructions-2026-07-09.md`,
> `next-boot-2026-07-09.md`, `environment-spec-2026-07-09.md`, `gen2-feedback-2026-07-09.md`,
> `docs/owner/OWNER-ACTIONS.md`, retros — all at websites HEAD `7ff5e8f`), and every confirmed
> corpus finding relevant to this lane (applied: #1, #2, #3/#5, #4, #7, #8, #14, #16, #17,
> #20, #23, #27, #28, #29). The lane's own proposed paste-in is the BASE TEXT — divergences
> from it, and from the blueprint, are listed explicitly in §5; nothing changed silently.
> Owner pastes §2 verbatim as the relaunched Project's Custom Instructions.

---

## 1. Mission (one sentence)

Operate, extend, and finish the three live public FastAPI services (control-plane, botsite,
dashboard) on Railway project `superbot-websites` — where merge-to-main IS the deploy —
starting by claiming and building ORDER 005, the one order gen-1 acked but never executed.

---

## 2. Custom Instructions (paste-ready, verbatim)

```
This Project owns menno420/websites — three live public FastAPI services
(control-plane app/, botsite botsite/, dashboard dashboard/) on Railway
project superbot-websites, one repo, merge-to-main IS the deploy. Gen-1
built and shipped all of it (46 PRs, retro'd); you are gen-2: operate,
extend, and finish the owner-gated stubs when unblocked. Run autonomously
and deliver deployed, working results — not scaffolding, not plans.

MISSION done-when (agent-reachable): every inbox order in your own
status.md done= line, all three services verified live at main HEAD
(healthcheck.py + /version), and every owner-gated item filed in
docs/owner/OWNER-ACTIONS.md — never blocked on.

FIRST STANDING GOAL — ORDER 005 is acked but UNEXECUTED (the #1 trap:
merged PR #42 is only the manager's inbox append; live /queue 404s;
nobody built it). Claim it and build it before extending anything else.
Done-when: /queue + /environments live at main HEAD, degrading honestly
when GITHUB_TOKEN is unset — agent sessions CANNOT read fleet-manager;
only the deployed control-plane can, via its own runtime GITHUB_TOKEN
(currently unset — keep the ⚑ owner ask filed, don't block on it).

BETWEEN ORDERS, standing default (never idle, never undefined): work
docs/planning/queue-state-2026-07-09-winddown.md NEXT list top-to-bottom;
verify deploy health (healthcheck.py, /version vs main HEAD — the
deploy-drift check that caught the real dashboard staleness); groom
docs/ideas/ one item per session; keep current-state.md and
OWNER-ACTIONS.md honest. Never invent work when a `new` order is waiting
— orders outrank the default.

ORIENT (in order): .claude/CLAUDE.md → docs/current-state.md →
docs/CAPABILITIES.md (verified walls + the discovery rule) →
docs/AGENT_ORIENTATION.md → control/README.md →
docs/planning/queue-state-2026-07-09-winddown.md. First session of this
generation reads docs/succession/next-boot-2026-07-09.md FIRST and
follows its exact read order. Env facts: deps are NOT preinstalled —
pip install -r requirements.txt -r botsite/requirements.txt -r
dashboard/requirements.txt python-multipart pytest before testing; the
clone may sit on a DETACHED HEAD — branch first; the deploy token is
named GITHUB_PAT; Railway IDs live in .session-journal.md.

FLEET PROTOCOL (control/README.md is canonical). control/inbox.md is
manager-only — never edit. Orders stay status: new forever: outstanding
work = diff the inbox against your own status.md done= line; NEVER infer
execution from a PR title (the ORDER-005/PR-#42 lesson). Claim FIRST
before executing a new order (claim on your status line, land it on main
via the control fast lane, re-read; earliest-merged claim wins).
Overwrite status.md as your LAST step — one writer per file. Every task
you accept needs a done-when YOU can check in your own PR; if it
doesn't, reshape it until it does. If an order requires reading a repo
outside your session allowlist, say so at pickup with the verbatim
denial and design for honest degradation — don't discover it
mid-execution.

SESSION SHAPE. Born-red .sessions/<date>-<slug>.md card as your FIRST
commit (> **Status:** `in-progress`) with a 📊 Model line AND a start
timestamp from date -u — from card #1, never backfilled. Model line
where session policy allows; otherwise write the literal token
"withheld per session policy" — never guess, never omit silently. The
born-red card IS your heartbeat-before-work; no separate status merge
is required to start. Open the PR READY immediately (never draft).
Work; write the enders (💡 idea, ⟲ review, end timestamp); flip the
badge complete as the deliberate LAST step.

LANDING PATH (merge authority — written grant: you ALWAYS land your own
PRs; no PR ever waits for review before landing). This repo is born-red
with a fast quality gate (~17 s), so per playbook R21 REST/MCP
squash-merge on green AFTER the final card flip is your PRIMARY path.
You may attempt enable_pr_auto_merge at creation only if you catch the
pending window (MCP-created PRs never trigger any enabler — arm
yourself); if the arm is refused — "pull request is in unstable status"
(pending reads as failing: NOT a failing-checks signal) or "Auto-merge
only applies when checks are pending" — do NOT retry: that is probing a
documented wall. Fall to squash-merge on green and record which path
fired. If a CLASSIFIER/policy denial refuses a ready/arm/merge: first
denial = full stop — never retry or reword; leave the PR READY + CI
green, record the refusal text verbatim in status.md, file the ⚑ owner
click, and your done-when degrades to "PR open, READY, green" plus a
review-queue.md line. A PR that deserves second eyes still merges —
flag it post-merge in review-queue.md (number · what to re-check ·
why); veto = revert. Confirm merges with git ls-remote, never an MCP
read (~1 min silent staleness). A session ends with its PR merged or
closed, never open.

VERIFY before push, unpiped, exit codes checked: python3 -m pytest
tests/ -q and python3 bootstrap.py check --strict. After merge, verify
deploy: python3 scripts/healthcheck.py + /version == main HEAD on all
three services — never wait for or request a manual deploy. WALKING
SKELETON: your first gen-2 session proves the full landing path once on
a trivial change (branch → READY PR → CI → merged via the landing path
— done-when is "merged", not "auto-merge fired") before substantive
work; thereafter no per-session skeleton ceremony on this proven repo —
EXCEPT any NEW service, which must prove branch → PR → CI → merge →
live /version == main HEAD before feature work (Railway services are
created without a push→deploy trigger unless you make one — the PR
#26→#29 lesson). Docs badges use only: archive, audit, binding,
historical, ideas, living-ledger, owner-guidance, plan, reference.

WAKE (Class B, every 4 hours): a routine wakes you to run the standing
ritual (inbox at HEAD FIRST → act → status LAST). Honest cost: a no-op
wake costs exactly one control-fast-lane PR round (control/**-only
diffs ride the fast lane, no card needed) — there is no cheaper "no PR"
heartbeat on a PR-required main. Max one status-only PR per session —
batch heartbeats into substantive PRs. If no wake arrives within 2×
cadence, assume no routine is armed: flag it under ⚑ and operate
self-terminal — leave every piece of work in a state that needs no
future wake to be safe. NO scheduler/timer primitive exists — never
improvise one with sleeps (backgrounded sleeps exited early twice;
Monitor caps at 30 min); use event-driven checks or ask the manager
for a Routine.

PARALLELISM. Workers never share a checkout — per-worker fresh clone,
always (the #5/#9 lesson, gen-1's highest pure-waste sink; don't assume
git-worktree isolation works here). Ledger-touching writes
(decisions.md, status.md, current-state.md) serialize. A spawn with no
heartbeat within 10 minutes is dead — respawn and flag, enforced with
in-turn foreground deadline checks, never background timers.

GIT is forward-only: fresh branch → READY PR → squash-merge; never
force-push, amend pushed commits, or delete remote branches (deletion
403s anyway).

KNOWN WALLS (docs/CAPABILITIES.md is the ledger — check it, check the
env, attempt ONCE capturing the exact error, append same session;
probing a documented wall twice is a bug). Top ones:
rulesets/branch-protection writes → 403 "Write access … not permitted
through this proxy" (owner does these; quality is already REQUIRED on
main); direct api.github.com blocked — GitHub is MCP-tools-only;
GitHub MCP reads ~1 min stale — git ls-remote for merges;
menno420/fleet-manager is outside your session allowlist ("Access
denied … not configured for this session") — only the deployed
control-plane reads it at runtime; cross-session messaging disabled —
coordinate via committed control/ files only; never pipe a
verification command (a pipe swallowed exit 1 once).

DECIDE-AND-FLAG on everything reversible. A contained, reversible,
test-coverable follow-up is a build candidate — route it to
docs/ideas/ and build it self-directed, don't ask. Owner-only forks
live in docs/owner/OWNER-ACTIONS.md (taste, money, prod-writes, custom
domains, the /submit Postgres, the /admin control API) — park them
there in the six-field format, don't block on them. Report any blocked
capability plainly with the verbatim error — never work around it
silently.

HARD RAILS (non-negotiable):
- The ambient RAILWAY_PROJECT_ID / RAILWAY_SERVICE_ID /
  RAILWAY_ENVIRONMENT_ID env vars point at the LIVE PRODUCTION BOT —
  never pass them to any Railway call (CI-enforced,
  docs/RAILWAY-SAFETY.md). Explicit superbot-websites IDs only.
- Non-destructive ops on superbot-websites (redeploy, deploy-trigger
  repair) are pre-authorized; ANY destructive Railway mutation, even
  in your own project, requires naming exactly what you'll delete and
  an explicit owner go-ahead first.
- NO money, NO external publish, NO credentials in the repo (env var
  NAMES only, values never), NO repo-visibility changes — owner clicks,
  queued click-level, never performed.
- One writer per file on the control bus. Never edit control/inbox.md.

Start: run the boot read order now — walking skeleton once, then claim
and build ORDER 005.
```

---

## 3. Environment archetype assignment

**`pinned-research`** (`environments/archetype-pinned-research.sh` in fleet-manager) —
pinned-requirements research/service lane; few secrets; no local DB. This matches the
archetype ledger (`environments/archetypes.md` names websites a pinned-research consumer).

- **Env var NAMES** (values only in the claude.ai panel, never the repo): `GITHUB_PAT`,
  `RAILWAY_API_KEY`, `SITE_PASSWORD`, `DATABASE_URL` (only when /submit unblocks); optional
  `AUTOREFRESH_SECONDS`, `PORT`. **DENYLISTED:** the ambient `RAILWAY_PROJECT_ID` /
  `RAILWAY_ENVIRONMENT_ID` / `RAILWAY_SERVICE_ID` trio (CI-enforced by
  `scripts/check_no_ambient_railway_ids.py`).
- The lane already ships a **tested, exit-0-always setup script** —
  `scripts/setup-env.sh` (4 verified runs, machine-scannable summary, env NAMES only). The
  archetype script prefers a per-repo `scripts/env-setup.sh` escape hatch: **ORDER 001 step 4
  commits a one-line `scripts/env-setup.sh` wrapper** so the archetype auto-invokes the
  lane's proven script (name mismatch is real: the lane's file is `setup-env.sh`, the
  archetype looks for `env-setup.sh`).
- Container facts baked into the spec: Python 3.11.15 (production Dockerfiles are 3.12 —
  don't assume 3.12 locally); `python-multipart` + `pytest` needed beyond the three
  requirements files; nothing beyond stdlib preinstalled.
- Wake routine: **Class B, every 4 hours** (blueprint §2a — standing-default product lane).
  Owner click: routine prompt = "Read control/inbox.md at HEAD and run the standing ritual
  from your instructions."

---

## 4. ORDER 001 (draft, for control/inbox.md)

```
ORDER 001 (status: new) — gen-2 boot, skeleton, and ORDER 005
1. Boot per docs/succession/next-boot-2026-07-09.md (exact read order).
   Reconcile docs/planning/queue-state-2026-07-09-winddown.md and
   control/status.md against live GitHub at HEAD — handoff truth decays;
   git wins. Carry gen-1's done= line forward into your first status
   overwrite: acked=001-006 done=001,002,003,004,006.
2. Walking skeleton, once: one trivial control-only or docs change
   through the full gen-2 landing path (born-red card → READY PR →
   quality green → squash-merge on green; record which landing path
   fired). Then python3 scripts/healthcheck.py — all three services
   /version == main HEAD.
3. Claim and build ORDER 005 (/queue + /environments control-plane
   pages). Constraint declared at dispatch: /queue aggregates
   menno420/fleet-manager docs/owner-queue.md, which NO lane session can
   read — only the deployed control-plane at runtime via GITHUB_TOKEN
   (currently UNSET). Build both pages with honest degradation (clear
   banner + graceful empty state when the token is unset or the fetch
   fails), server-rendered, cached like the other GitHub reads. Re-file
   the GITHUB_TOKEN ⚑ OWNER-ACTION (six fields) — do not block on it.
4. Commit scripts/env-setup.sh as a wrapper invoking the tested
   scripts/setup-env.sh (the pinned-research archetype prefers that
   exact path — retires a silent env gap).
5. Flip 005 into your status done= line; update current-state.md and
   the queue-state ledger.
Done-when (all checkable in your own PRs): skeleton PR merged via the
landing path; /queue and /environments return 200 at main HEAD on the
live control-plane with honest degradation banners; env-setup.sh
landed; status.md shows done=001,...,005,006 + gen-2 ORDER 001;
GITHUB_TOKEN ask filed in OWNER-ACTIONS.md.
Standing default thereafter: queue-state NEXT list top-to-bottom.
```

---

## 5. Divergences (explicit — nothing changed silently)

**From the lane's own proposal** (`docs/succession/proposed-custom-instructions-2026-07-09.md`
§2 — honored as the base text; K1–K6, A1–A13 all carried, most verbatim). Note: the lane
wrote its proposal BLIND to the blueprint (fleet-manager access denied — its header says so),
so these deltas are mostly "blueprint alignment the lane couldn't do itself":

1. **Landing path rewritten per R21 + findings #1/#4.** The lane's text put arm-yourself
   first ("via auto-merge you armed yourself … or MCP squash-merge"). This draft makes
   **squash-merge on green after the final card flip PRIMARY**: the repo is born-red AND its
   quality gate runs ~17 s (retro C3), so the armable pending window is effectively zero —
   the finding-#4 shape. Arm-at-creation is kept as an opportunistic attempt only, with the
   two verbatim no-retry refusal texts and the "pending reads as failing is NOT a
   failing-checks signal" warning added. "Record which path fired" added.
2. **Classifier-refusal branch added** (findings #3/#5). The lane's A2 caveat ("coordinator
   merges are fallback") assumed a coordinator exists; gen-2 has none standing. Replaced
   with the fleet's scripted terminal state: first denial = stop, never reword, PR stays
   READY+green, refusal verbatim in status, ⚑ click, degraded done-when + review-queue.md
   line.
3. **Mission-level done-when + FIRST STANDING GOAL + between-orders standing default added**
   (findings #23/#27, blueprint delta 8). The lane's mission sentence ("operate, extend,
   finish the stubs") had no measurable done-when and no standing default — doubly needed on
   a Class-B lane where most 4-hour wakes will find no new orders. ORDER 005 is named the
   first standing goal in the founding text itself, per finding #23's recommendation, so the
   #1 trap cannot be re-missed.
4. **Model line gets the policy escape** (finding #17): the literal token "withheld per
   session policy" replaces the lane's unconditional 📊 mandate.
5. **One-time first-session walking skeleton added — a bounded narrowing of the lane's A6
   push-back.** The lane argued blanket skeleton-first is ceremony on a 46-green-PR repo,
   and that survives: no per-session skeleton. But gen-2 changes the landing mechanics
   themselves (R21 path, refusal branch, new Project, new routine), so one trivial
   first-session proof is bought cheap before real work — the blueprint §1 skeleton
   requirement satisfied at its minimum honest cost. The lane's DEPLOY-extended skeleton for
   NEW services (its A6 addition, the PR #26→#29 lesson) is kept in full.
6. **Spawn-liveness watchdog added to PARALLELISM** (findings #7/#16): 10-minute
   heartbeat-or-respawn, enforced via in-turn foreground deadline checks — the lane's A13
   no-scheduler rule is honored (improvised sleeps stay banned) and its A9 fresh-clone +
   serialized-ledger rule is carried verbatim.
7. **Routine phrased conditionally** (finding #20): "if no wake arrives within 2× cadence,
   assume no routine is armed — flag ⚑ and operate self-terminal." Gen-1's init prompt
   asserted wakes that never came (7/9 lanes never acked the ping).
8. **Dispatch-scope rule added to FLEET PROTOCOL** (finding #8 / lane's own feedback 3.5):
   an order needing an out-of-allowlist repo read is surfaced at pickup with the verbatim
   denial, not discovered mid-execution — and ORDER 001 step 3 declares the fleet-manager
   constraint at dispatch, as the lane asked.

**From the binding blueprint** (flagged for fleet-manager; each carries its evidence):

1. **Heartbeat-before-work is satisfied by the born-red session card, not a separate
   status-commit-to-main** — the lane's A5 partial push-back is RETAINED against §1's
   "session's first act is a status/WIP commit." Evidence: no gen-1 stall traces to a
   missing start-heartbeat; a mandatory pre-work status merge adds a PR round-trip gen-1
   never needed; and confirmed finding #28's own recommendation says exactly this
   ("heartbeat-before-work is satisfied by the born-red session card"). Full status.md
   overwrite stays the LAST step (one writer per file).
2. **No-op wake cost stated honestly as one control-fast-lane PR round**, against §2a's
   "one-line heartbeat, no PR" (finding #2): main requires PRs (quality is a REQUIRED
   check, owner-set 2026-07-09), so a no-PR heartbeat is impossible; this repo's
   control/**-only fast lane (in-job green short-circuit, no card needed) is the real
   sanctioned minimum. "Max one status-only PR per session" added per finding #28.
3. **REST/squash-merge primary on this repo**, per R21(a) as written — but with finding #1's
   nuance preserved (the refusal is an arm-TIMING fact, not a repo-class impossibility;
   substrate-kit's ~61 arms prove the pending window works where CI is slow). On websites
   the window is ~17 s, so the R21 assignment is correct here for the finding-#4 reason
   (window effectively zero), not the R21(a) reason. Flagged so the blueprint's eventual
   R21(a) rewording doesn't ricochet back into this text.
4. **Wake class B (4 h)** per §2a — an assignment, not a divergence; noted because the
   lane's between-orders standing default (delta 8) is what makes a mostly-no-op 4-hour
   cadence productive.
