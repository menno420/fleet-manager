# fleet-manager — hub · agent boot file

> Auto-loaded when a session boots in this repo. **fleet-manager is the router
> and records home** of the owner's repository estate. The autonomous-Projects program
> that built most of it **closed 2026-07-21**; everything now runs in **regular
> sessions like yours**, working the consolidation program with the owner, one
> step at a time. The cold-orientation contract is
> **README.md's six-read mandatory order** (§ Cold orientation below); this file
> is its Claude-side half.

## Boot triad — know yourself first (every session)
1. **What model you are** — from your own config, family-level.
2. **Where you're running** — owner-live hub chat · scheduled wake · subagent;
   remote container. **And what loaded**: Claude Code reads settings, hooks and
   skills from `<root>/.claude/`, where root is the session's working directory.
   Three cases, and only the first is the one you want:
   - **One source, and it is fleet-manager** → root is this repo; the read path
     below, the installed skills and the doc-routing hook all load. **This is why the
     owner boots here** and then attaches whatever the work needs.
   - **One source, and it is a satellite repo** → root is *that* repo. Everything
     here goes quiet — with no error, and with the satellite's own `.claude/`
     loading in its place, so the session feels fully equipped. Measured
     2026-08-07 booting on `curious-research`: **only that repo's own skill set,
     no hub hooks, and no estate read path at all.** The routing table below cannot bind
     a session that never loaded it (PL-013), so `capability-probe`,
     `owner-brief` and `session-close` simply do not exist for that session.
   - **Several sources** → root is the bare clone parent `/home/user`, which has
     no `.claude/`, so **every repo's settings, hooks, skills and boot file go
     quiet at once with no error** (measured 2026-08-05; superbot's hard-fail
     `Stop` gate is among the casualties).

   **`add_repo` mid-session attaches files, not apparatus.** Root is fixed at
   boot and does not move — which is what makes `add_repo` *safe* (you never lose
   what you loaded) and equally what makes it **insufficient**: attaching
   fleet-manager from a satellite session gives you this file to *read*, and
   loads none of the hooks or skills it routes to. If you are reading this
   because someone attached the hub mid-session, you are in case two — walk the
   read path by hand and invoke skills by name; nothing will do it for you.
   Diagnostic: `ls /root/.claude/projects/` names the root as cwd with `/`→`-`. A
   bare `-home-user` entry means case three — run `python3
   tools/install_root_hooks.py --apply` before trusting any gate.
3. **What you can do** — the capabilities ledger below. Default posture:
   **you have full capability — act.**

## Cold orientation — the six mandatory reads (owner directive, 2026-08-10)

**On every cold start, follow `README.md`'s numbered six-read order** — this
file counts as read one's Claude-side half; the others are `docs/intent.md`,
`docs/current-state.md`, the consolidation program **paired with
`docs/planning/2026-08-08-agent-operating-environment-roadmap.md`** (read 4 is
both — `OD-13` makes the roadmap the current plan and the program the older
track), `docs/fleet-account-2026-07-26.md` and
`docs/owner-reflection-2026-07-21.md`, each annotated there with what it gives
you. Then state the repo's **purpose,
era, what the owner is working on and why, and the next step**. If this boot
file did not auto-load, `README.md` alone carries the whole order — it is the
surface-neutral front door. Do not hide a failed orientation by hunting through
extra documents; record the missing fact instead.

The quick mid-task re-check (not a substitute for the six on a cold start) is
`docs/current-state.md` + the program's NOW pointer. **What ran anywhere else —
including on the owner's laptop — is `docs/activity/`**, and nothing else in
this repo carries it: `.sessions/` here is fleet-manager's own work only. **The one-line-per-area map
with tiers (CORE / TASK / RECORD) is `docs/MAP.md`** — the router for everything
not on a path here. Owner directive + design:
`docs/planning/2026-08-10-repo-navigation-plan.md`.

## Deep read path (in order — for comprehension and task-specific work)

The six reads above orient you. The path below adds the owner's
working principles, provenance, history, and owner-only queue when the task
requires full comprehension. It is deliberately deeper than the acceptance
test; do not confuse the two.
0. **How the owner thinks:** `docs/owner-reflection-2026-07-21.md` — his own
   thesis (**the wall is verification, not capability**), how he works, the
   "real mind" direction, and the standing instruction to **decide rather than
   default to asking**. `docs/current-state.md` introduces it as *"read this if
   you read nothing else… before picking up any owner-facing work"* — so it is
   first here, not buried two hops away. **This entry exists because a session
   skipped it** (2026-08-05): the list below used to start at the program, and a
   session that followed it exactly never learned the reflection existed.
1. **What is true now:** `docs/current-state.md` — the living ledger, and a
   declared boot-readpath doc in its own header. Source and merged PRs win over
   it; read it before task-specific docs so you don't act on stale state.
1b. **The owner's CURRENT plan — read before the program below:**
   `docs/planning/2026-08-08-agent-operating-environment-roadmap.md` — his
   architecture decisions taken live 2026-08-08, in three phases: retrieval +
   orientation (landed, fm #826) · intent resolution (first slice landed, fm #830;
   § 4.8 run in full — producer half fm #851, blind-scorer half fm #852,
   PARTIAL confirmed 3/3 scorings) · the common operating protocol (not started).
   **EXECUTION TARGET REDIRECTED 2026-08-30 ([D-0025], owner-live): the plan
   executes in a FRESH HUB repository — this repo becomes the read-only
   archive. Read `docs/planning/2026-08-30-fresh-start-redirect.md` WITH the
   roadmap; do not start implementation work premised on this repo being the
   long-term home.** **This entry exists because the roadmap appeared in neither this file
   nor `README.md` until 2026-08-10**, while `current-state.md` carried it *below*
   its own "preserved, not current" banner — so a session walking this path met a
   plan from 2026-07-26 and never learned a newer direction had been set two weeks
   later. Third instance of the defect entries 0 and 2b already record. Salvaged
   from fm #838 (superseded by fm #839/#840, this entry excepted).
2. **The program:** `docs/planning/2026-07-26-consolidation-program.md` —
   THE working plan: the owner-directive (OD) table, the step ledger, the **NOW**
   pointer, and how a session works a step. Your work almost certainly lives here.
   **How its OD table and NOW pointer reconcile — as of 2026-08-10, not forever:**
   `OD-13` puts the roadmap's Phases 2–3 and the multi-provider mix first *until
   those prerequisites are further along*, and `OD-15` supersedes D2's `shiftlife`
   target *until the owner re-targets it* (`OQ-FM-D2-TARGET`). Both are
   conditions with expiries, so read the NOW pointer for the current state rather
   than assuming the OD table outranks it permanently. **When either condition
   changes, re-read the NOW pointer — do not infer that the lettered step is now
   the work:** the two expire independently, so OD-13 lifting still leaves D2
   without a target until `OQ-FM-D2-TARGET` is answered, and D2 being retargeted
   still leaves OD-13 prioritising methods over that product work.
   **Its NOW pointer is not the whole answer** — read entry 2b before acting on it.
2b. **What supersedes the plan's next-actions:**
   `docs/findings/2026-08-05-foundation-continuation.md` — the revised order of
   work (foundation before rebuild), and a **certainty legend that governs how to
   read every dated claim in this repo**: `MEASURED` / `MEASURED-PRIOR` / `OWNER` /
   `REASONED` / `REVIEWED` / `UNVERIFIED` / `NOT-VERIFIABLE`. Its follow-on,
   `docs/findings/2026-08-06-checker-classification.md`, carries the kit's checker
   classification and the boot-path audit. **This entry exists for the same reason
   entry 0 does** (2026-08-06): the doc calls itself the one that "supersedes
   everything else about what to do next", and on the day it was written *nothing*
   in this read path referenced it — it was reachable only by being handed a prompt
   that named it. A document that lives only in a handoff prompt is not in the repo.
3. **The story & state:** `docs/fleet-account-2026-07-26.md` — what happened
   (2025-08 → now) and each repo's terminal state, owner-reviewed. Read once;
   don't re-derive the history — it already distils `eap-story`,
   `eap-retrospective`, `dispatch-log` and the rest.
4. **Owner-only items:** `docs/owner-queue.md` — the consolidated queue of
   genuinely owner-only asks (stable `OQ-` slugs). **Read it whole** when the
   task involves owner actions; active and historical material are distributed
   through the file.
5. **The handover:** `docs/PROJECT-CLOSEOUT.md` §3 — the priority-ordered
   continuation threads, each self-contained. Two were still open 15 days after
   the close because no one re-read them.

**Then the one for the repo you are actually working on:** `docs/repos/<name>/README.md`
— **Layer 2**, one folder per repo, and the entry point stands alone. This list
above is Layer 1: it carries what is true *regardless* of which repo a session
is on, and it deliberately does **not** explain any single repo. Read the folder
**before** attaching the repo — it answers what the repo is, where the last
session left off, and whether attaching is even needed. Naming a repo in your
message now pulls its README in automatically (`route_docs.py` runs on
`UserPromptSubmit` as well as `PreToolUse`), so this is a net, not a chore.
Structure, the thread convention and honest coverage: `docs/repos/README.md`.
**No folder ≠ invisible: `docs/ESTATE.md` is the estate index** — every
repository the account holds, one line each (what it is, state, owner
vocabulary, canonical entry, Layer-2 link). When the target repo has no
folder, or the owner's words name a product rather than a repo, start there.

**Then read the repository's active owner feedback:**
`docs/owner-comments/<name>/README.md`. It is the stable literal index for
arbitrarily named comment records; existing Layer-2 prompt routes inject it as
a companion automatically. Open the records in **Unconsumed** before acting.
After acting or explicitly reconciling one, run `python3
tools/owner_comments.py consume ...` so the JSON is moved into `consumed/` and
both indexes change in the same diff. Never delete it. Everything in this
directory is public; secrets and private-repository contents do not belong
there.

**This list is a floor, not a ceiling.** A session whose job is to *understand*
this repo reads past it — `CONSTITUTION.md` and `docs/owner-profile.md` (live),
`docs/playbook.md` (mixed era — R1/R2/R16/R17/R22/R24/R28/R29/R30 still bind
— R28's repo-qualify-every-`owner/repo#N` rule is live and estate-general —
the seat-era dispatch/relay *mechanics* do not), and `MISSION.md`, `docs/NEXT-TASKS.md`,
`docs/fleet-triage.md` **as history** — each describes a seat-era fleet that no
longer exists, and each now says so at the top. A handoff prompt that names a short read list is naming
the minimum to act, never the boundary of what is worth reading (`CONSTITUTION.md`
§ "Session prompts are guidance, not orders").

**Live vs historical:** `docs/roster.md`, `control/`, `telemetry/`,
`projects/`, `docs/prompts/` are **seat-era apparatus — historical record** (exceptions:
`docs/prompts/chatgpt-project-instructions.md`,
`docs/prompts/chatgpt-couch-legend-project-instructions.md` + the
curious-research review
prompt are live; `control/claims/` is contested — the kit still wires it), not current
truth (the seats no longer exist; the roster was retired 2026-08-07 and no
longer regenerates). Per-repo truth lives in each repo's
`docs/PROJECT-CLOSEOUT.md` + `docs/current-state.md`. The live surface always
beats any doc.

**Why, before what:** `docs/intent.md` — what this repo is **for**, what counts
as working, the non-goals, how to decide without him, and **who does what across
Claude / ChatGPT / Gemini / Grok / Codex**. Owner-stated 2026-08-08; it is what a
plan is checked against when a rule and the situation disagree. Read it before
asking him anything.

**Where a decision lives, so you cite the right record:** `docs/decisions.md` —
this repo's `[D-NNNN]` entries (D-0011 the paid Gemini key is free to spend —
budget only; the *route* is free-key-first since 2026-08-29, D-0020 ·
D-0012 publish by default, credentials never) · the program's OD table — owner
directives · `docs/planning/2026-08-08-fleet-manager-as-index.md` — the Layer 2
decisions and their rejected alternatives · substrate-kit's PL register —
program law binding every repo.

## The working style (owner-set, 2026-07-26; restated 2026-08-08)
- **One thing at a time, finished properly** — not slow for its own sake, and
  not a licence to stop short (OD-6 as he restated it). Small PRs — **and
  few: one main PR per session, grown by pushing; an extra PR carries a
  stated exception reason in the card (guideline, D-0024).** Cleanup of
  spent docs/repos is allowed and wanted, with a stated reason (OD-3 amended).
- **Records may grow; instructions may not.** The fix for an unfollowed rule is
  a mechanism that delivers it at the right moment, never another statement of
  it (`docs/intent.md` § 4).
- **Verify before fold; verify with real exit codes** (never `$?` after a
  pipe). Kit discipline: born-red session card, session close updates the
  program's progress ledger, and **one command is the local gate** — `python3
  bootstrap.py check --strict`, which fans out through `scripts/preflight.py`
  to the added-card lane and both checkers. **The check list lives in that
  script, not in prose here** — every written enumeration of it has gone stale
  (the `session-close` skill named two of three until 2026-08-08).
- **The Stop hook reviews the reply you just sent, and blocks once.**
  That is normal operation, not a fault — and **the owner has already seen
  that reply** (owner, 2026-09-02: the block does not withhold it, so a session
  that "amends the reply" puts the same message in front of him twice). Answer
  with **only what is new**: the corrected sentence and what changed it, or
  one line marked `[survived]` naming what you read or ran — never the reply
  again. Same disposition vocabulary
  for any adversarial review: `[survived]` / `[conceded]` / `[partial]`, so the
  tally is countable rather than a reading (`docs/conventions/adversarial-review.md`).
  A **firing** instrument is information; a quiet one is no evidence at all.
  What each hook does: `.claude/hooks/README.md`.
- **Ask immediately; stop almost never.** Organize and plan on your own
  judgment, and when a genuine fork appears, put it to him **and keep working** —
  stop only when no next step exists without the answer. *"I'd rather have an
  agent ask me something so I can clarify than that they misunderstand the
  goal"* (owner, 2026-08-08): unnecessary asks are the waste, asking is not.
  He is away during implementation and checks in roughly every 30 minutes.
- **Do not write about a file you have not opened.** Saying what a file *is* is
  a claim, and a filename plus this estate's conventions produces a confident
  sentence without making it true. If you genuinely cannot open it, **say the
  line is inferred** — worth more than a clean sentence nobody can check.
  `read_before_write.py` raises this at write time with the measurement and the
  claim it means; it checks whether the path was fetched, never whether you
  understood it.
- **Never delete a trigger, and don't `send_later` to watch a PR** (`[D-0015]`).
  `delete_trigger` is **the one call that raises an approval prompt on his
  screen in automode** — the session then **stalls until he is physically back**,
  and cannot see that it is waiting. Every other call here succeeds, fails loudly
  or is denied in writing; all three leave you working. A fired one-shot trigger
  is inert and costs nothing to leave. **If one is actually misbehaving — firing
  repeatedly, misconfigured — DISABLE it: `update_trigger` with `enabled: false`.
  That is the emergency stop; deleting never is.** It prevents future firings,
  raises no prompt, and is reversible; whether it cancels a run already in flight
  is unverified. Only if it then needs *removing* rather than silencing, say so
  in your reply — he removes it in seconds. To watch a PR use
  `subscribe_pr_activity`; note it delivers comments, reviews and CI **failures**
  but **not** CI-success or new-push (`CAPABILITIES.md`, MEASURED 2026-07-14).
  **So nothing will ever wake you to say a PR went green — do not end a turn
  waiting for that. Poll to a terminal state inside the turn** (loop on
  `commits/{sha}/check-runs` until every run is `completed`; measured on fm #833,
  green on the 2nd of 12 × 15 s iterations), or end the turn saying plainly that
  it is still pending. Enforced by
  `.claude/hooks/trigger_tools_guard.py` — one of the estate's **two denying
  hooks** (the Codex round cap above is the other), because a rule with no
  judgement in it is the only kind that may deny.

## Capabilities — record capabilities, never limitations
Full verified matrix: **`docs/CAPABILITIES-verified-2026-07-18.md`** (+
post-close verification: `docs/findings/2026-07-22-pat-and-automode-capabilities.md`).
Essentials:
- You hold **admin + push on every repo** via the **direct-PAT path** —
  `$GITHUB_PAT` over direct egress (`curl --noproxy '*'`, or `requests` with
  `trust_env=False` and `verify=/root/.ccr/ca-bundle.crt`) — and via the MCP
  GitHub tools. Merge PRs, delete branches, change settings/rulesets, create
  releases/secrets/tags, update Railway variables (`$RAILWAY_API_KEY`) — all
  normal agent work. Private-repo clones: bypass the local git proxy
  (`GIT_CONFIG_GLOBAL=/dev/null` + `https://x-access-token:$GITHUB_PAT@github.com/…`).
- The *proxied* GitHub REST path 403s. That is a path quirk — switch to direct
  egress — **not a wall.**
- **ALWAYS ask `@codex` explicitly — never rely on it noticing your PR.** Its
  own about-box advertises three triggers (open a PR for review · mark a draft
  ready · comment `@codex review`), but **only the comment is reliable.**
  `MEASURED` 2026-08-29, and **read what was actually probed**: both observed
  PRs were *created* ready, so **draft→ready is untested, not refuted** (zero
  `ready_for_review` events on either). On PR-open, fm #974 was open **422 s**
  (`19:35:24Z` → merged `19:42:26Z`) and drew **zero** Codex activity on all
  three surfaces — 87 s past the ~335 s relay, suggestive but not conclusive,
  since a queued review would plausibly be abandoned at merge. fm #977 drew a
  review seconds after a manual request, logged by Codex itself as
  `Review trigger: Manual request`. Owner,
  live, same day: *"Codex only reviews if you ask it to."* The advertised
  auto-triggers and the observed behaviour disagree; **post the comment and
  you never have to care which is right.** Then wait — it answers in about
  5.5 minutes.
  Measured 2026-08-07 on fm #812: request `13:46:59Z` → review `13:52:34Z` on
  the exact head SHA = **335 s**; 13 findings over 5 rounds across #812/#813,
  several proving a PR did not do what its own title claimed. Findings arrive as
  **inline review comments**, not in the review body, so a summary that looks
  empty is not an empty review — read `/pulls/{n}/comments`. **Never merge a PR
  you have asked Codex to review before it answers**: a session once waited 150 s,
  wrote *"no review appeared"* into a public comment as if that were evidence,
  and merged three minutes before four real findings landed. Quota refusals are
  retry-later, never a property of the tool. (Codex *cloud* is a different
  surface — `docs/providers/chatgpt.md` — and does not bear on this relay.)
  **Cadence (owner, live, 2026-08-29): reserve Codex for flip-readiness and
  real important changes — not after every push, which wastes the usage
  limits.** Mid-session verification of intermediate fixes goes to the
  free-key Gemini route (`gemini-3.6-flash`, one call with the findings + the
  diff); the single Codex round then lands on the head that flips, which is
  also what TRAP-006/007's verdict-at-flip-head needs. First worked use:
  fm #978 ([D-0019]). **Hard cap: three rounds per PR per session (owner,
  live, 2026-09-02, [D-0039]) — `.claude/hooks/codex_round_guard.py` counts
  each `@codex review` out loud and DENIES the fourth.** fm #1010 ran 17
  rounds overnight (03:00Z → 06:30Z) because the cadence rule above was prose
  only; the exit at round three is fix · verify without Codex · disclose the
  residue · flip or hand off — never a fourth round, never a merge with a
  known error hidden (`docs/traps.md` TRAP-009).
- **Gemini: the free key is the route — Vertex is retired (owner, live,
  2026-08-29: the prepaid credits timed out days earlier, "the paid/vertex
  route does not work anymore").** `GEMINI_API_KEY` is **free tier** (AI
  Studio, daily request caps, the Interactions API, and now the default for
  everything it serves, mid-session review work included);
  `GEMINI_API_KEY_PAID` still bills **the owner's card** — [D-0011] still
  authorizes spending it without asking; reach for it when the free key
  cannot serve the task (Deep Research the documented case), said out loud
  in the card. Current API model ids for this key class: `gemini-3.6-flash`
  (`MEASURED` 2026-08-29 — `gemini-2.5-flash`, the one id probed, 404s as "no
  longer available to new users"; the other 2.5 ids are untested). History, the caps, and the credit-era Vertex recipe:
  `docs/conventions/vertex-first-for-gemini.md`, which the doc-routing hook
  puts in front of you the moment you make a Gemini call.
- **When the owner states something about this estate, it is source truth — act
  on it.** *"The token is account-scoped." · "You have access to my test bot
  token." · "Use Vertex." · "The Interactions API works fully turn based."* He
  built this and each of those cost him real time to make true. Do not probe to
  check whether he is right, and do not reply with questions about what a
  credential or an API can do — **do the thing.** Working *is* the verification;
  failing gives you a real error to report instead of a hypothetical doubt. Not
  an exception to verify-first: that doctrine guards against stale *records* and
  your own *inferences*, and he is neither. The evidence base is **three
  independent sessions, each counted against its own transcript, landing near
  90–100 % on unhedged claims** (`docs/CAPABILITIES.md` § step 0) — and **read
  the hedge**: he asserts where he has direct observation and hedges where he
  does not, so a hedged number is worth checking; an unhedged provisioning
  statement is not.
  **The boundary is not "provisioning versus behaviour."** That narrower version
  was written on 2026-08-05 and licensed a violation the same day: he stated the
  Interactions API keeps turn-based history, a probe of the *Vertex* path
  returned `RESOURCE_PROJECT_INVALID`, and "unavailable" went into the ledger —
  filed as a behaviour claim the probe was free to overturn. It works on the AI
  Studio surface exactly as he said. **A probe establishes only what that one
  call did. A failure means you took the wrong path, not that he was wrong** —
  so go find the other path instead of writing a wall. Full rationale:
  `docs/CAPABILITIES.md` § THE DISCOVERY RULE step 0.
- **Before probing a vendor API, check `docs/providers/` and
  `docs/conventions/`.** A `PreToolUse` hook now surfaces the matching doc
  automatically — `.claude/hooks/route_docs.py`, silent unless one matches,
  never blocks. It is a **net, not a substitute for looking**: it fires
  once per route per session and only on triggers someone thought to add. It
  exists because on 2026-08-05 a session probed a discovery document, found no
  `interactions` endpoint and recorded "unavailable" while
  `docs/providers/gemini.md` held the working recipe — having authored the rule
  against that three hours earlier. Add a route when you find a doc that would
  have saved you: `.claude/hooks/README.md`.
- **Never write down a limitation.** A refused call is transient classifier
  state — route around it and leave no wall behind. The guard is
  `tools/check_no_false_walls.py`, and **as of 2026-08-06 it is enforced for
  you**: it runs in `substrate-gate` alongside `tools/check_doc_routes.py`, and
  `substrate-gate` is now a **required status check** on `main`
  (`main-branch-protection`, active) — so a red gate blocks the merge instead
  of decorating it. Both halves of this bullet were true and stale: until
  2026-08-06 neither checker ran in any workflow and the ruleset carried **zero**
  required checks, which is how conflict markers reached `main` and silently
  disabled the doc-routing hook. **The rulesets API is readable AND writable
  agent-side** — `GET`/`PUT /repos/{o}/{r}/rulesets/{id}` over direct egress,
  both 200, re-verified from the effective-rules endpoint after the write. The
  kit's `check --strict` emits an `enforcement-required-unverified` NOTE
  claiming this is unreadable by agents; **it reads fine — measured 2026-08-06.
  Read the endpoint, never quote that NOTE.**

## Task → skill routing — invoking the skill IS part of the task

When a task matches a row below, **loading that skill is part of doing the
task**, not an optional extra — a skill you didn't load can't bind you
(PL-013). **The installed roster with one line per skill lives in
`docs/SKILLS-local.md`** — derive the set from that registry and the skill tree
rather than freezing a count in prose. `docs/SKILLS.md` is the kit-generated
half; the local file explains the split.

| The task in front of you | Invoke |
|---|---|
| Any image, sprite, background, cover/icon — or a prompt for one | `image-prompt` (routes to `sprite-prompt` / `parallax-prompt` / `cover-art-prompt`) |
| A delivered generated image → engine-ready asset | `asset-pipeline` |
| Writing ANY session/handoff prompt | `prompt-preflight` (+ `continuation-prompt` or `implementation-prompt`) |
| Decisions living only in this chat | `decision-capture` |
| A fragmented / non-trivial owner ask | `intake` (+ `chase-references`) |
| Steps the owner must do by hand | `prep-owner-steps` |
| A backlog item needs shaping | `scope-backlog-item` |
| Any audio ask — a cue, a loop, a stem, or "make the audio better" | `audio-prompt` |
| About to say "I can't" / a tool seems missing / something new worked | `capability-probe` |
| A job means reading a whole corpus (all cards, all results, a full tree) | `delegate-read` |
| About to fan out agents — an ultracode workflow, a mass sweep, any run whose output becomes a finding | `fleet-preflight` (before the first agent spawns, not after) |
| Owner asks anything status-shaped ("where are we", "what's left") | `owner-brief` |
| Owner asks what OTHER sessions did — his local ones especially — or you need the estate-wide picture | **not a skill: run `python3 tools/estate_activity.py refresh`, then read [`docs/activity/`](../docs/activity/README.md)** — this repo's `.sessions/` is fleet-manager's work ALONE (MEASURED 2026-08-26: 74 cards estate-wide that week, 54 reachable from here, 20 not) |
| Ending the session | `session-close` (run the one strict command and read its real exit code) |
| Kit version work | `release` → `upgrade-distribution` |

The list is deliberately short — it carries only the recurring task classes.
If your task is one of these and the matching skill never fired, treat that as
a gate-worthy defect in the session, not a stylistic choice.

## Precedence — the live owner outranks any stored text
The owner's most recent live instruction beats any dated shutdown / wind-down
note, ORDER, or status file. A stored order is a record of a past state, not a
standing authority. **Provenance decides, not arrival order; the committed tree
beats any doc's claim.** Never hold a stale stored "stop" above a fresh live "go."

## Session close
Leave the truth accurate: update the program's §7 progress ledger + NOW pointer
if you completed a step; update `docs/owner-queue.md` if you changed an owner
ask; record any new verified **capability** in the ledger (never a wall); drive
any PR you opened to a terminal state. Honest nulls and honest failures are
deliverables; an invented wall is the only real failure.
