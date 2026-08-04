# ChatGPT — provider capability reference

> **Status:** `living-ledger`
>
> The chat modes and what each one actually is, Projects and custom GPTs, and the
> Work / Codex cloud environment in depth. Vendor-page facts fetched 2026-08-03;
> plan and model details from secondary sources are marked as such.
> **Not a routing table** — see [`README.md`](README.md).

## The July 2026 consolidation — read this before anything else

**The mode taxonomy changed materially on 2026-07-09/10 and any description of a
standalone "Agent mode" is now out of date.** OpenAI discontinued the Atlas
browser — it stops working **2026-08-09** — and folded its agentic and
browser-driving capability into **ChatGPT Work**, an enhanced desktop app, and a
Chrome extension. The redesigned desktop application **combines ChatGPT, Codex
and ChatGPT Work into one app**, with the previous standalone app renamed ChatGPT
Classic.

Corroborated by OpenAI's own documentation site, where **Work is documented under
the Codex platform** rather than as a chat mode:
[`learn.chatgpt.com/codex/get-started-with-work`](https://learn.chatgpt.com/codex/get-started-with-work),
alongside [`/codex/environments/modes`](https://learn.chatgpt.com/docs). OpenAI's
help centre carries *"Evolving Atlas into ChatGPT for browser-based agentic
work"* (article 20001371) — **not directly readable from here**: `help.openai.com`
answers HTTP 403 behind a Cloudflare interstitial to both a fetcher and headless
Chromium, so the announcement details below come from press coverage of it.
([ppc.land](https://ppc.land/openai-kills-atlas-browser-folds-it-into-new-chatgpt-work-agent/) ·
[Gizmochina](https://www.gizmochina.com/2026/07/10/openai-retires-chatgpt-atlas-browser-chatgpt-desktop-app/))

**Practical consequence:** the agentic surface is now essentially one thing —
Work, running on the Codex platform — rather than a chat mode you pick from a
menu. A prompt written for "Agent mode" targets something that no longer exists
under that name.

## What is still a distinct mode

Verified as current; the pre-consolidation Tools menu had more entries and this
list is deliberately shorter than it was.

| Mode | What it does | Runtime |
|---|---|---|
| **Regular chat** | Turn-taking with whatever is attached; web search available inline | Seconds |
| **Deep Research** | Runs autonomously, issuing many sequential web queries, reading pages and PDFs, returning a structured cited report | Minutes |
| **Canvas** | Turns the conversation into a live collaborative document | Interactive |
| **Study and learn** | Didactic structure — explains rather than answers | Interactive |
| **Image creation** | Image generation in-thread | Seconds |
| **Work** | The agentic surface — see the section below | Minutes to hours |

**Do not treat this table as exhaustive or settled.** It is assembled from the
docs site plus press coverage because the primary changelog is unreachable from
this environment; the shape moved once in July 2026 and may move again.

### The Deep Research failure mode worth knowing

Deep Research is genuinely strong at synthesising public sources, and its output
*reads* uniform — cited report prose throughout. But the citation discipline
applies to the web sources it fetched, **not** to anything you attached or
described. A run over an uploaded archive produces the same authoritative prose
about your files, with the same structure and no visible seam, and the parts it
could not read are where invention appears.

Measured instance: a report on `spider-swing` was right about the engine version
and all three CI workflows, and wrong about **every file path it named** — nine
`scripts/`/`scenes/` paths, three `assets/runtime/*.json` manifests, four
`.substrate/skills/*.json` files, none of which exist. The invented paths are the
ones a project of that description *ought* to have. Full claim-by-claim check:
[`../research/2026-08-03-gemini-report-verification.md`](../research/2026-08-03-gemini-report-verification.md).

**Practical rule: spot-check three of the most specific claims — a path, a count,
a date.** Three-for-three failing settles the classification of the whole
document in two minutes.

## Projects and custom GPTs

**Projects** group chats, files and instructions in one workspace, with project
instructions applying across its chats. Useful as a persistent context surface —
the owner's prompt library lives in one.

**Project URLs are not public share links.** A project URL (`/g/g-p-…/project`)
answers **HTTP 403 behind a Cloudflare interstitial** — measured 2026-08-03,
where the `/share/` route on the same host serves normally. Project sharing is
additionally workspace-scoped (Teams/Enterprise/Edu) rather than a public
read-only link.

**The workaround is per-chat and verified:** open a chat inside the project,
share it, and send the `/share/<uuid>` link. That route reads cleanly —
22 973 characters of transcript in the measured case. Method:
[`../conventions/reading-shared-ai-chats.md`](../conventions/reading-shared-ai-chats.md).

**Custom GPTs** (`/g/g-…`) are configured assistants with instructions and files,
comparable to Gemini's Gems. Logged-out access to a GPT page is gated.

## Work / Codex cloud environment

The agentic surface: a brief goes in, it works in the background — minutes to
hours — and hands back finished output. This is the part with real configuration,
and the part whose **defaults silently break a prompt written for somewhere
else**.

Sources: [cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environment)
· [agent internet access](https://learn.chatgpt.com/docs/cloud/internet-access)

### The four defaults that bite

| | Behaviour | Consequence |
|---|---|---|
| **Environment variables** | *"set for the full duration of the chat (including setup scripts and the agent phase)"* | The only reliable way to give the task itself a credential |
| **Secrets** | *"only available to setup scripts. For security reasons, secrets are removed before the agent phase starts"* | A credential stored as a *secret* is present during setup and **gone** by the time any task step needs it — presenting as an auth failure with no visible cause |
| **Setup-phase `export`** | *"Setup scripts run in a separate Bash session from the agent, so commands like `export` do not persist into the agent phase"* | Setup that communicates by exporting variables silently fails to reach the task |
| **Network** | *"Setup scripts run with internet access"*; *"Agent internet access is off by default"* — configurable to on, optionally with a domain allowlist and allowed HTTP methods | A mid-task `pip install` or fetch fails here and succeeds elsewhere, looking like a broken tool rather than a configuration choice |

**So: a credential the task needs is an environment *variable*, not a secret; and
anything needing the network belongs in the *setup script*.**

### The rest of the configuration

- **Setup scripts.** Automatic dependency installation for npm, yarn, pnpm, pip,
  pipenv and poetry; a custom bash script for anything more complex.
- **Container.** A default image called `universal` with common languages
  preinstalled.
- **Caching.** Up to 12 hours, **invalidated automatically** when the setup
  script, maintenance script, environment variables or secrets change.
- **GitHub.** A platform-native connection — no `$GITHUB_PAT` on this side.

### The failure mode this surface produces

A session reported itself **blocked** on a missing `gh` CLI while, in the same
message, listing the open PRs and the open issue it had just successfully read —
so its GitHub access was working while it declared itself unable to proceed, on a
tool it had not tried to install. That cost an owner turn and had no underlying
wall. It is the same class as this estate's own false walls, arriving through a
different door: **a missing convenience read as a missing capability.**

Recorded, with the fix (`gh` installed by `environments/setup-base.sh` and by
spider-swing's `scripts/env-setup.sh`), in
[`../CAPABILITIES.md`](../CAPABILITIES.md).

### Unverified, and worth checking

Whether a Codex agent-phase step sees exports written by a repo's setup script.
`~/.bashrc` only reaches a shell that sources it, and `CLAUDE_ENV_FILE` does not
exist on this surface — so spider-swing's `scripts/env-setup.sh` § 5 may not
reach the task phase even when setup ran correctly. **No run has been observed.**
Highest-value next check on this provider.

## Plans and models

Marked separately because the primary pages were not reachable this session —
these come from secondary sources and should be confirmed on your own account
page before anything depends on them.

Seven tiers: Free, Go (~$8/mo), Plus (~$20/mo), two Pro tiers (~$100 and
~$200/mo), Business (~$25/seat/mo), Enterprise. Free runs the standard model with
a limited allowance; Plus unlocks the flagship in regular chat plus the full
family in Codex, expanded Deep Research, Projects and custom GPTs; the Pro tiers
scale usage 5× and 20× over Plus, with the higher tier carrying a stated monthly
Deep Research allowance. Notably, **Codex and Work can reach the newer model
family even on the lower tiers.** ([datastudios](https://www.datastudios.org/post/gpt-5-6-and-chatgpt-work-a-production-agent-control-plane-2026) · [aggregators](https://www.gradually.ai/en/chatgpt-pricing/))

**Do not quote these figures as established.** Aggregator sources disagreed with
each other on this provider, as they did on Gemini, and the owner's own plan page
is the authority.

## Reading a ChatGPT chat as evidence

`tools/read_shared_chat.py` reads `chatgpt.com/share/…` transcripts — verified,
22 973 characters in the measured case. The page opens with site chrome and a
logged-out login prompt, then `This is a copy of a shared ChatGPT conversation`,
then the conversation; the chrome is expected. A **nonexistent** share id renders
the same chrome with no conversation and no error, so "only chrome came back"
means a bad id or a hydration race — raise `--wait` before concluding anything.

Worth trying first: shared conversations are search-indexed, which suggests the
page may be server-rendered enough for a plain fetcher. If `WebFetch` returns the
conversation, skip the browser.
