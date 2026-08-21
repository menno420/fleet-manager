# Execution surfaces — what each one can do

> **Status:** `living-ledger`
>
> A capability comparison of the surfaces that run sessions against these repos.
> Facts dated 2026-08-03, each with its source. Re-verify anything you build on;
> these platforms move faster than this file.

## Read this first — it is not a routing table

**This document describes what each surface *can do*. It does not say who should
do what, and it assigns no roles.**

If you are a session reading this: **do the work you were asked to do.** Nothing
here licenses declining a task because some other surface looks better suited to
it. The purpose is the opposite — so that a session meeting a limit can tell
*"this surface works differently here, use the other path"* apart from *"this is
impossible"*, which is the confusion that has repeatedly cost the owner a turn.

Use it for two things only: writing a prompt that will actually run where it is
sent, and diagnosing a failure before recording it as a wall.

**Roles now exist — and they live somewhere else, deliberately.** The owner
assigned per-agent roles on 2026-08-08. The canonical roster is
[`intent.md`](intent.md) § 7, because who *should* do what is intent, not
capability; **this file does not restate it**, so it cannot drift from it. Read
both when writing a prompt for a surface that is not this one, and note his
portability rule: **do not assume every method works on every agent**, but write
for the fact that more than one agent works these repos.

## The comparison

| | **Claude Code environments** | **ChatGPT Work / Codex cloud** |
| --- | --- | --- |
| **Env vars** | Set per environment; available to the session | Set per environment; **available for the full duration** including setup scripts and the agent phase |
| **Secrets** | — | Separate, encrypted, **available to setup scripts only — removed before the agent phase starts** |
| **Setup script** | `environments/setup-base.sh` + auto-discovered `scripts/env-setup.sh` per repo | Custom bash setup script per environment; auto-installs for npm/yarn/pnpm/pip/pipenv/poetry |
| **Does `export` in setup reach the agent?** | Yes — via `CLAUDE_ENV_FILE` and `~/.bashrc` | **No.** "Setup scripts run in a separate Bash session from the agent, so commands like `export` do not persist into the agent phase" |
| **Network during setup** | Yes, through the agent proxy | Yes — "Setup scripts run with internet access" |
| **Network during the agent phase** | Yes, through the agent proxy | **Off by default.** Can be set to on, optionally with a domain allowlist and allowed HTTP methods |
| **Container caching** | Image cached after setup | Cached up to 12 h; **invalidated automatically** when the setup script, maintenance script, env vars or secrets change |
| **GitHub access** | MCP GitHub tools + git over the configured remote; `$GITHUB_PAT` in *some* environments | Platform-native GitHub connection; **no `$GITHUB_PAT`** |
| **`gh` CLI** | Not in the base image; installed by `setup-base.sh` Block 2b | Not present by default; nothing requires it |
| **Reads `AGENTS.md`** | Yes | Yes |
| **What actually auto-loads in THIS repo** | `.claude/CLAUDE.md`, plus the skills in `.claude/skills/` and the hooks registered in `.claude/settings.json` — **derive the counts, never quote them** (see below) | **nothing — there is no `AGENTS.md` here** (measured 2026-08-09) |
| **`delete_trigger` stalls on owner approval** | Yes — the reason for the deny-hook and its decision | **No.** No equivalent tool, and nothing there has ever waited on owner approval (owner, 2026-08-10) |

Sources: [Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environment) ·
[Agent internet access](https://learn.chatgpt.com/docs/cloud/internet-access) ·
this estate's own measurements, recorded in [`CAPABILITIES.md`](CAPABILITIES.md).

## What actually changes a prompt

Four of those rows are not trivia — each one silently breaks a prompt that
assumes otherwise.

**1. Agent-phase network is off by default on the Codex side.** A prompt that
says *"install X"*, *"fetch the spec from Y"* or *"pip install"* mid-task will
fail there and succeed here, and the failure looks like a broken tool rather than
a configuration choice. Anything that needs the network belongs in the **setup
script**, which always has it — or the environment's internet setting has to be
turned on deliberately.

**2. Secrets vanish before the agent runs; env vars do not.** A credential the
agent itself must use has to be an **environment variable**, not a secret. As a
secret it will be present while the setup script runs and gone by the time any
task step needs it — which presents as an auth failure with no obvious cause.

**3. `export` in a setup script does not survive into the Codex agent phase.**
Any setup that communicates by exporting variables has to write them somewhere
durable instead, or set them as environment variables in the first place.
*Concretely, in this estate:* spider-swing's `scripts/env-setup.sh` § 5 exports
`GODOT_BIN` and the three `XDG_*` paths into `~/.bashrc` and `$CLAUDE_ENV_FILE`.
The `~/.bashrc` half only reaches a shell that sources it, and `CLAUDE_ENV_FILE`
does not exist on the Codex side — so an agent-phase step there may not see them
even though setup ran correctly. **Unverified on that surface** (no run observed);
flagged as the highest-value thing to check next.

**4b. A ChatGPT Work session boots BLIND in this repo, and the row above is why.**
`MEASURED` 2026-08-09: `ls AGENTS.md .github/AGENTS.md` → neither exists. The
table says both surfaces read `AGENTS.md`, which is true and is not the point —
**fleet-manager does not have one.** Claude Code loads `.claude/CLAUDE.md`
automatically; ChatGPT Work does not read that path, so it starts with **no boot
file, no read path, no skills, and none of the hooks.**

That last part is the one that changes an outcome rather than a convenience. On
2026-08-09 those hooks — the reply-reviewer, the propagation checker, the
unread-file checker, the doc router — caught **every single wrong claim a Claude
session made that day, and the author caught none of them by re-reading.** A
ChatGPT session doing the same work has none of that watching it. The **gates**
(`bootstrap.py check --strict` and the `tools/` checkers) are plain `python3`
and DO run there; only the moment-of-action hooks are absent.

**Do not write the hook or skill count down here — derive it.** This line said
*"none of the five hooks"* from 2026-08-09 to 2026-08-10 while there were six,
because the sentence was committed in `e9214c5` **after** `a02a4b1` added the
sixth hook in the same session. `ls .claude/hooks/*.py` and the `hooks` block of
`.claude/settings.json` are the answer and cannot go stale; a number in prose
goes stale the moment the thing it counts changes. Found by the fm #835
reviewer, fixed in fm #836 ([findings/2026-08-10-fm835-verification.md](findings/2026-08-10-fm835-verification.md)).

**So a prompt aimed at that surface has to carry what the boot file would have
given for free**, and should say plainly that nothing will catch a mistake
except the gates and the session itself. Adding an `AGENTS.md` that points at
the same read path would close the orientation half. It was deliberately absent
for the D2 cold-read test, and remains absent after the test so the owner can
make that surface-wide choice explicitly. The evidence and recommendation are
recorded in `docs/findings/2026-08-10-fleet-manager-cold-read.md`; the action is
`OQ-FM-AGENTS-BOOT`.

**4. `$GITHUB_PAT` is not universal.** Some environments here carry it, and the
Codex side does not. Any recipe that names it must branch on
`printenv GITHUB_PAT` rather than assume it — see the 2026-08-03 ledger entry.
On the measured Work surface, read-only clone/fetch works without it; remote
branches, commits and pull requests use the GitHub connector. An authenticated
local push returned the error recorded in the ChatGPT section below.

## Strengths and weaknesses, as measured here

Only behaviours this estate has actually observed. Where something is general
knowledge rather than measured, it says so.

### Claude Code environments

**Observed strengths.** Long autonomous stretches against a repo with real
verification in the loop — this session ran six PRs across two repos to green
without supervision. Repo-native tooling: MCP GitHub tools, `git` over the
configured remote, arbitrary bash. Media is readable end to end (ffmpeg frame
extraction; headless Chromium for client-rendered pages). Fleet-wide setup is
centralised in `environments/setup-base.sh`, so one edit reaches every archetype.

**Observed weaknesses.** The agent proxy makes GitHub access *path-dependent*:
the same REST call 403s proxied and succeeds direct, and the 403's text names an
org admin, so it reads as a permission problem. This has produced repeated false
walls — the reason `tools/check_no_false_walls.py` exists. Verification is
uneven: local `bootstrap.py check --strict` and CI have disagreed at least once
(a card-grammar check that fires only on an added card). And this surface will
state a limit it has not tested — twice today, both caught by the owner rather
than by a guard.

**Update 2026-08-05 — the same weakness, twice more, same day.** The line
above ("twice today, both caught by the owner rather than by a guard") repeated
in a session that was itself reading these documents. It dismissed nine open
dependabot PRs as "noted, not touched" because a status doc said the open-PR
surface was dependabot — six of the nine could not affect runtime at all, and
three were the security scanner going stale on a live bot. Earlier the same
session treated a four-path `READ FIRST` list as the boundary of a
comprehension task and skipped the document its repo calls *"read this if you
read nothing else."* **Four instances in three days, every one owner-caught,
none guard-caught.** In both cases the stopping force was not a measurement but
a document that had already concluded — inheriting a conclusion rather than
deriving one.

### ChatGPT Work / Codex cloud

**Observed strengths.** Long unattended runs producing finished, reviewable
output; a platform-native GitHub connection that does not need a PAT; and a
configurable environment with real primitives — env vars, encrypted secrets,
setup and maintenance scripts, container caching.

**Observed weaknesses.** The default posture is more locked down than it looks:
agent-phase network off, secrets stripped, setup-phase exports discarded. Each of
those turns into a mid-task failure whose cause is invisible from inside the task.
One recorded instance: a session reported itself **blocked** on a missing `gh` CLI
while, in the same message, listing the open PRs and the open issue it had just
successfully read — a false blocker that cost the owner a turn. That is the same
failure class as this side's false walls, arriving through a different door.

**Update 2026-08-10 — measured on a real review task (fm #835), and it went
well.** Given fm #833/#834 to attack, a Work session reran both instruments
offline, corrected the defect classification, found that a script advertised as
a seven-case harness ran four, fixed the local false-wall hole, and took ten
Codex findings across three exact-head reviews with a reproduction and a
`[conceded]` disposition on every one. Verified independently in fm #836: gates
`0/0/0/0/0`, the fix reproduces, and an adversarial battery written elsewhere
scores it 23/24 against the old checker's 9/24
([findings/2026-08-10-fm835-verification.md](findings/2026-08-10-fm835-verification.md)).

Three surface facts came out of it, each of which had cost a turn to guess:

- **The GitHub connector is the publishing route, not `gh` and not
  `$GITHUB_PAT`.** `command -v gh` → 1, `printenv GITHUB_PAT` → 1, and an
  authenticated local `git push` → 128 (`could not read Username`). The
  connector did branches, commits, ready PRs, review replies, thread
  resolution, **and Actions job logs** — the last being the one operation this
  estate's docs still describe as needing `gh`. Read-only `git clone` / `fetch`
  worked fine, so the shape is: **local git for the tree, connector for the
  remote.**
- **The repo checked itself out — it did not arrive.** The initial working
  directory was empty and `.claude/CLAUDE.md` returned *No such file or
  directory*. Codex *cloud* checks out a selected repo automatically; a **Work
  project chat does not**. Treat them as two surfaces, not one.
- **`merge-on-green` only sweeps `claude/*`.** Its branch filter is literal
  (`merge-on-green.yml:162`), so an `agent/*` head is skipped and must be merged
  directly. Any prompt aimed at this surface should either name a `claude/*`
  branch or say the landing is manual.

**The cost, stated honestly:** ten review findings over three rounds means Codex
did a lot of the correcting, and the loop hit its two-round cap with four fixes
to a required-CI checker still unexamined. It converged, and not cheaply.

**Update 2026-08-10 — the deliberate documentation test (fm #837).** A Work
session began with an empty directory and no repository file loaded, then ran
fleet-manager's D2 truth pass under the repo's own procedure. The cold route
failed before the edit: purpose required a fourth file, the living ledger led
with seat-era state, and two next-action pointers had to be negated. The repaired
README → current-state → consolidation-program route now states purpose, live
era and next action within D2's limit. The full observation, including the
things this surface had to hunt for, is
[`findings/2026-08-10-fleet-manager-cold-read.md`](findings/2026-08-10-fleet-manager-cold-read.md).
This resolves the documentation-work question in `intent.md` for one real,
landed pass; it does not remove the need for exact-head review.

### The pattern both share

**Neither surface reliably distinguishes "this path is misconfigured" from "this
is impossible", and both report the second when the first is true.** That is the
single most expensive shared failure mode in this estate, it has now been
observed on both, and it is what the *preconditions and refutation* habit in the
capability ledger exists to counter.

## Advice worth following, from outside this estate

Current public guidance, cited, with the parts that match what has been measured
here marked.

- **`AGENTS.md` is a cross-tool standard.** A Markdown file at the repo root read
  natively by 30+ agent tools, including both surfaces above — instructions for
  machines rather than documentation for humans. **Neither `fleet-manager` nor
  `spider-swing` has one**, which means each surface is currently oriented by a
  different file. ([betterclaw](https://www.betterclaw.io/blog/agents-md-best-practices))
- **Separate planning from execution.** Interview, write a self-contained spec,
  then execute it in a *fresh session with clean context.* This is already the
  owner's workflow, and it is what the continuation-prompt skill formalises.
  ([Blink](https://blink.new/blog/agentic-coding-best-practices))
- **Spec before prompt.** Write what gets built, what does *not*, edge cases and
  acceptance criteria — so the agent builds to a contract rather than to an
  assumption. **Matches what is measured here:** every expensive failure today
  came from an unstated assumption, never from a stated one being wrong.
- **Keep the agent file small and earn every line.** Start ~30 lines; add a
  section when an agent consistently gets something wrong; remove one when the
  convention changes. Treat it as code, not documentation. **Contradicts current
  practice here** — this estate's boot files are long, and the honest note is
  that the length has not been tested against a short alternative.
- **Name files and constraints.** "A prompt that names files and constraints gets
  a plan you can trust, while a one-line ask gets a guess."
  ([SSOJet](https://ssojet.com/blog/best-coding-agent-prompts))

## Reading a shared chat from either platform

`tools/read_shared_chat.py` reads client-rendered transcripts — verified on both
`share.gemini.google/…` and `chatgpt.com/share/…`. Procedure and failure
symptoms: [`conventions/reading-shared-ai-chats.md`](conventions/reading-shared-ai-chats.md).

**A ChatGPT *project* URL (`/g/g-p-…/project`) is not readable this way.** It
answers **HTTP 403** with a Cloudflare interstitial (`Just a moment…`,
`__cf_chl_rt_tk` in the URL) where the `/share/` route serves normally. Project
sharing is also workspace-scoped rather than a public read-only link. **The
workaround is per-chat:** open a chat inside the project, share it, and send the
`/share/` link — that route is verified working.

## Per-provider depth

This document is the comparison — the handful of rows that change how a prompt
must be written. For depth on one provider (model families, chat modes and what
each one actually is, environment configuration, plan ceilings), see
[`providers/`](providers/README.md): [Claude](providers/claude.md) ·
[ChatGPT](providers/chatgpt.md) · [Gemini](providers/gemini.md).

## Writing a prompt against this

Four skills consume this document rather than restating it —
[`SKILLS-local.md`](SKILLS-local.md): `prompt-preflight` (the checks before any
prompt), `continuation-prompt` (carry a planning session into a fresh one),
`implementation-prompt` (direct a session to build a defined thing) and
`decision-capture` (commit the decisions so the prompt can point instead of
carry). Each reads the surface rows above and adjusts only what actually
differs — network, credentials, tooling, setup-phase exports.

**A ChatGPT project's standing instructions are a file, not a chat artifact** —
one per project:
[`prompts/chatgpt-project-instructions.md`](prompts/chatgpt-project-instructions.md)
(Fleet Manager) ·
[`prompts/chatgpt-couch-legend-project-instructions.md`](prompts/chatgpt-couch-legend-project-instructions.md)
(Couch Legend, 2026-08-21).
A brief aimed at that surface should point at the right project's file rather
than restate it — and
should not re-add the `delete_trigger` rule, which is Claude-Code-specific
(owner, 2026-08-10; see the surface table).

**Known gap, 2026-08-05.** `continuation-prompt` was promoted into substrate-kit
so it reaches every adopter, but **this document was not** — so the kit copy
carries surface-adaptation guidance with no surface data behind it. The content
here is estate-specific (this proxy's path-dependence, spider-swing's setup
exports) while the *structure* is general, so the fix is the shape the kit
already uses for `CAPABILITIES.md`: ship the general rows as a template and let
each adopter fill in its own measurements.

## Keeping this honest

Every row above is either cited to a vendor page or observed here. When a row
turns out to be wrong, correct it in place and append the measurement to
[`CAPABILITIES.md`](CAPABILITIES.md) — this file is the comparison, that one is
the evidence log.

Two rows are **unverified and marked as such**: whether a Codex agent-phase step
sees spider-swing's setup exports, and whether shortening this estate's boot
files would help or hurt. Both are cheap to test and neither has been.
