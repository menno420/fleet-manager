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

**4. `$GITHUB_PAT` is not universal.** Some environments here carry it, and the
Codex side does not. Any recipe that names it must branch on
`printenv GITHUB_PAT` rather than assume it — see the 2026-08-03 ledger entry.
Git over the configured remote does clone/fetch/push/branch without it.

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
