# ChatGPT — provider capability reference

> **Status:** `living-ledger`
>
> The chat modes and what each one actually is, Projects and custom GPTs, and the
> Work / Codex cloud environment in depth. Vendor-page facts fetched 2026-08-03;
> plan and model details from secondary sources are marked as such.
> **Not a routing table** — see [`README.md`](README.md).

## Why the modes matter

This is the provider where "which chat is it" changes the answer most. A regular
chat, a Deep Research run, an Agent-mode run and a Work session are different
execution models with different tools, different runtimes and different failure
modes — and the same prompt sent to the wrong one produces a confidently wrong
result rather than an error.

## The modes

Six modes reach from a Tools menu in the composer. ([datastudios](https://www.datastudios.org/post/chatgpt-and-the-new-tools-interface-six-modes-to-access-agent-research-study-and-creation))

| Mode | What it does | Runtime | Reach for it when |
|---|---|---|---|
| **Regular chat** | Ordinary turn-taking, plus whatever is attached | Seconds | Anything conversational; the default |
| **Deep Research** | Runs autonomously for **5–30 minutes**, issuing many sequential web queries, reading pages and PDFs, and returning a structured cited report | Minutes | A question whose answer needs many sources synthesised. **Not** for questions about a repo it cannot see |
| **Agent mode** | Plans a sequence of steps, picks tools, and executes — opening a **visible browser window** you can watch | Minutes | Tasks needing real interaction with a site, not just reading it |
| **Canvas** | Turns the conversation into a live collaborative document | Interactive | Iterating on a document or a piece of code side by side |
| **Study and learn** | Didactic structure — explains rather than answers | Interactive | Learning something, not shipping something |
| **Web search** | Ordinary chat plus live retrieval | Seconds | A current fact, without paying for Deep Research |
| **Create image** | Image generation in-thread | Seconds | Visual assets |

**Deep Research can be combined with Agent mode**, giving the research run a
visual browser. That is the most capable and slowest combination.

### The Deep Research failure mode worth knowing

Deep Research is genuinely strong at synthesising public sources, and its output
*reads* uniform — cited report prose throughout. But the citation discipline
applies to the web sources it fetched, **not** to anything you attached or
described. A run over an uploaded archive will produce the same authoritative
prose about your files, with the same structure and no visible seam, and the
parts it could not read are where invention appears.

Measured instance: a report on `spider-swing` was right about the engine version
and all three CI workflows, and wrong about **every file path it named** — nine
`scripts/`/`scenes/` paths, three `assets/runtime/*.json` manifests, four
`.substrate/skills/*.json` files, none of which exist. The invented paths are the
ones a project of that description *ought* to have. Full claim-by-claim check:
[`../research/2026-08-03-gemini-report-verification.md`](../research/2026-08-03-gemini-report-verification.md)
(same verification method, different provider — the failure class is shared).

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
