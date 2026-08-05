# fleet-manager — hub · agent boot file

> Auto-loaded when a session boots in this repo. **fleet-manager is the hub and
> records home** of the owner's ~22-repo estate. The autonomous-Projects program
> that built most of it **closed 2026-07-21**; everything now runs in **regular
> sessions like yours**, working the consolidation program with the owner, one
> step at a time. This file is your orientation — the whole picture is two more
> reads away.

## Boot triad — know yourself first (every session)
1. **What model you are** — from your own config, family-level.
2. **Where you're running** — owner-live hub chat · scheduled wake · subagent;
   remote container. **And what loaded**: Claude Code reads settings, hooks and
   skills from `<root>/.claude/`, where root is the session's working directory.
   One source at boot → root is the repo and everything loads. Several sources
   → root is the bare clone parent `/home/user`, which has no `.claude/`, so
   **every repo's settings, hooks, skills and boot file go quiet at once with no
   error** (measured 2026-08-05; superbot's hard-fail `Stop` gate is among the
   casualties). The owner boots one source per session for exactly this reason —
   that choice is his, not yours. Yours: `add_repo` **mid-session is safe** (root
   is fixed at boot and does not move), and if `ls /root/.claude/projects/` ever
   shows a bare `-home-user` entry, run `python3 tools/install_root_hooks.py
   --apply` before trusting any gate.
3. **What you can do** — the capabilities ledger below. Default posture:
   **you have full capability — act.**

## The read path (in order — this is the fix for slow orientation)
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
2. **The program:** `docs/planning/2026-07-26-consolidation-program.md` —
   THE working plan: owner directives OD-1..OD-12, the step ledger, the **NOW**
   pointer, and how a session works a step. Your work almost certainly lives here.
3. **The story & state:** `docs/fleet-account-2026-07-26.md` — what happened
   (2025-08 → now) and each repo's terminal state, owner-reviewed. Read once;
   don't re-derive the history — it already distils `eap-story`,
   `eap-retrospective`, `dispatch-log` and the rest.
4. **Owner-only items:** `docs/owner-queue.md` — the consolidated queue of
   genuinely owner-only asks (stable `OQ-` slugs). **Read it whole** — it is
   ~1,100 lines and the active asks do not all sit at the top.
5. **The handover:** `docs/PROJECT-CLOSEOUT.md` §3 — the priority-ordered
   continuation threads, each self-contained. Two were still open 15 days after
   the close because no one re-read them.

**This list is a floor, not a ceiling.** A session whose job is to *understand*
this repo reads past it — `CONSTITUTION.md`, `MISSION.md`, `docs/playbook.md`
(the R-series), `docs/owner-profile.md`, `docs/NEXT-TASKS.md`,
`docs/fleet-triage.md`. A handoff prompt that names a short read list is naming
the minimum to act, never the boundary of what is worth reading (`CONSTITUTION.md`
§ "Session prompts are guidance, not orders").

**Live vs historical:** `docs/roster.md`, `control/`, `telemetry/`,
`docs/prompts/` are **seat-era apparatus — historical record**, not current
truth (the seats no longer exist; the roster still regenerates until program
step D4 lands). Per-repo truth lives in each repo's `docs/PROJECT-CLOSEOUT.md`
+ `docs/current-state.md`. The live surface always beats any doc.

## The working style (owner-set, 2026-07-26)
- **Slow and structured.** One program step per session unless directed;
  small PRs; nothing needs to be fast, nothing is deleted (OD-3/OD-6).
- **Verify before fold; verify with real exit codes** (never `$?` after a
  pipe). Kit discipline: born-red session card, `python3 bootstrap.py check
  --strict` green, session close updates the program's progress ledger.
- **Initiative, with one flag rule:** organize and plan on your own judgment;
  route to the owner only the genuinely ambiguous forks — add them to the
  program's §6, don't block on them. His attention is the scarcest resource.

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
- **Gemini: default to Vertex, not the AI Studio key** (owner directive
  2026-08-05, "at least this month"). The AI Studio key spends the owner's card;
  Vertex spends a **€251.37 credit balance already paid for**. Same models. The
  service account is not in your environment — pull `GEMINI_VERTEX_SA_JSON` from
  Railway (`reliable-grace` / `worker` / `production`) with `$RAILWAY_API_KEY`,
  then OAuth to `aiplatform.googleapis.com`. Grounding is `googleSearch`
  (camelCase) on Vertex. Verified end to end 2026-08-05 — full recipe and the
  billing chain: `docs/conventions/vertex-first-for-gemini.md`.
- **When the owner states something about this estate, it is source truth — act
  on it.** *"The token is account-scoped." · "You have access to my test bot
  token." · "Use Vertex." · "The Interactions API works fully turn based."* He
  built this and each of those cost him real time to make true. Do not probe to
  check whether he is right, and do not reply with questions about what a
  credential or an API can do — **do the thing.** Working *is* the verification;
  failing gives you a real error to report instead of a hypothetical doubt. Not
  an exception to verify-first: that doctrine guards against stale *records* and
  your own *inferences*, and he is neither. Measured 2026-08-05 — seven
  corrections from him in one session, **all seven right, zero false positives.**
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
  automatically — `.claude/hooks/route_docs.py`, 19 routes, silent unless one
  matches, never blocks. It is a **net, not a substitute for looking**: it fires
  once per route per session and only on triggers someone thought to add. It
  exists because on 2026-08-05 a session probed a discovery document, found no
  `interactions` endpoint and recorded "unavailable" while
  `docs/providers/gemini.md` held the working recipe — having authored the rule
  against that three hours earlier. Add a route when you find a doc that would
  have saved you: `.claude/hooks/README.md`.
- **Never write down a limitation.** A refused call is transient classifier
  state — route around it and leave no wall behind. The guard is
  `tools/check_no_false_walls.py` — **run it yourself** (`--strict`), because
  as of 2026-07-31 nothing runs it for you: it appears in no workflow, and
  `main`'s only ruleset (`main-branch-protection`, active) carries a
  `pull_request` rule but **zero required status checks**. Read agent-side
  from the rulesets API, not owner-reported — see the 2026-07-31 row in
  `docs/CAPABILITIES.md`. Treat the discipline as self-enforced.

## Task → skill routing — invoking the skill IS part of the task

When a task matches a row below, **loading that skill is part of doing the
task**, not an optional extra — a skill you didn't load can't bind you
(PL-013). Full index with descriptions: `docs/SKILLS-local.md` + `docs/SKILLS.md`.

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
| Owner asks anything status-shaped ("where are we", "what's left") | `owner-brief` |
| Ending the session | `session-close` (verify: BOTH gates, real exit codes) |
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
