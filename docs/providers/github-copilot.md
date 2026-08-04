# GitHub Copilot — provider capability reference

> **Status:** `living-ledger`
>
> Surfaces, the multi-provider model picker, the cloud agent and its environment,
> and the AI-credits billing mechanics. **Derived 2026-08-04 from GitHub's own
> docs ([docs.github.com/en/copilot](https://docs.github.com/en/copilot)) and the
> official changelog ([github.blog/changelog](https://github.blog/changelog/label/copilot))**
> — no aggregator sources. In the set because the estate lives on GitHub, so
> Copilot is the provider a repo touches without anyone choosing it.
> **Not a routing table** — see [`README.md`](README.md).

## What this provider is, concretely

Not one model but a **front-end over many providers' models, embedded in
GitHub itself**. The same subscription reaches OpenAI, Anthropic, Google, xAI,
Moonshot and Microsoft models across GitHub.com, the IDEs, a CLI, and an
autonomous cloud agent. Its distinctive capability is *where* it runs — inside
issues, PRs and Actions — rather than any model of its own.

## Models — the picker, not a family

*Source: vendor docs
([supported models](https://docs.github.com/en/copilot/reference/ai-models/supported-models),
fetched 2026-08-04).*

Available in the picker as of the fetch: **OpenAI** GPT-5.6 Sol/Terra/Luna,
GPT-5.5, GPT-5.4 (+mini/nano), GPT-5.3-Codex, GPT-5 mini; **Anthropic** Claude
Opus 5, Fable 5, Sonnet 5, Opus 4.5–4.8 (4.8 also in a fast-mode preview),
Sonnet 4.5/4.6, Haiku 4.5; **Google** Gemini 3.1 Pro, 3.5 Flash, 3.6 Flash;
**xAI** Grok 4.5 (added 2026-07-28); **Moonshot** Kimi K2.7 Code; **Microsoft**
MAI-Code-1-Flash and Raptor mini (*"fine-tuned GPT-5 mini"*).

Per-model capability facts (context, modality, reasoning) are the upstream
provider's — see that provider's file in this directory. Copilot-specific facts:

- **GitHub does not tabulate per-model context windows.** The CLI doc states
  *"a 1 million token context window"* with configurable reasoning levels, and
  the supported-models page mentions 1M availability for certain models in
  select clients — but there is no per-model table. Honest null; the upstream
  provider's figure is an upper bound, not a guarantee of what Copilot passes.
- **Auto model selection** (*"Auto"*) picks a model *"based on availability and
  to help reduce rate limiting"* — availability-driven, not capability-driven.
- **Frontier models arrive fast**: Opus 5 on 2026-07-24 (launch day), GPT-5.6
  on 2026-07-09, Gemini 3.6 Flash on 2026-07-21 (its go-global day). The picker
  tracks upstream launches within days.
- On **Business/Enterprise**, model switching is an admin policy; since
  2026-07-29 GA models default to enabled rather than needing per-model opt-in.
- Third-party **Claude and Codex coding agents on github.com** are included
  with a Copilot subscription (changelog 2026-04-14) — distinct from Copilot's
  native cloud agent below.

## The surfaces

*Source: vendor docs, fetched 2026-08-04.*

| Surface | What it is |
|---|---|
| **Code completions** | In-IDE suggestions; unlimited on all paid plans, never billed in credits |
| **Copilot Chat** | IDE + GitHub.com + Mobile chat with model picker |
| **Code review** | *"Reviews your pull requests, identifies issues, and suggests fixes"* — GitHub.com, CLI, Mobile, VS Code, Visual Studio, Xcode, JetBrains, Azure DevOps (preview). Agent skills + MCP GA 2026-07-29 |
| **Copilot CLI** | Terminal agent: `/model` switching, plan mode, MCP, custom model providers via env vars (OpenAI-compatible, Azure, Anthropic, *"local options like Ollama"*) |
| **Cloud agent** | The autonomous surface — below. GA 2026-06-22 (formerly "Copilot coding agent") |
| **Custom agents** | Markdown+YAML *"agent profiles"* in `.github/agents/`, org- and enterprise-level too; can carry MCP server configs |
| **Automations** | Run the cloud agent *"on a schedule or in response to events in a repository"* |
| **GitHub Copilot app** | Desktop app for *"parallel workstreams, GitHub integration, and PR lifecycle management"* |
| **GitHub Spark** | Natural-language app building |

## The cloud agent — the surface with real configuration

*Source: vendor docs
([about the cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)
and linked how-tos, fetched 2026-08-04).*

Assign an issue to **Copilot** as assignee (or start a task); it researches the
repo, plans, edits on a branch, runs tests, and opens a PR — in a **GitHub
Actions-powered environment**.

The constraints, from GitHub's own pages — steers for prompt-writing, not walls:

- **One branch, one PR per task**: *"Copilot can only work on one branch at a
  time and can open exactly one pull request to address each task."*
- **59-minute session cap** — *"a hard limit that cannot be extended or
  bypassed."* A task must be sized to fit or split.
- **Single-repo scope** per task, GitHub-hosted repos only.
- **Default-on firewall**: internet access is limited; the recommended allowlist
  covers OS/package registries, container registries and CAs. Settings are
  Enabled / Disabled / *"Let repositories decide"* (default). A blocked request
  is surfaced as a **warning in the PR body or a comment** — so a
  half-succeeded task with a firewall note is a config finding, not a model
  failure.
- **Secrets reach the agent phase.** *"Agents secrets and variables are
  automatically available to Copilot cloud agent… exposed to the agent as
  environment variables"* (Settings → Security → Secrets and variables →
  **Agents**). The direct opposite of the ChatGPT Codex default, where secrets
  are stripped before the agent phase — a prompt written for one surface's
  secret model silently breaks on the other.
- Environment customization via `.github/workflows/copilot-setup-steps.yml`.

## Plans and billing — credits replaced premium requests

*Source: vendor docs
([plans](https://docs.github.com/en/copilot/get-started/plans),
[models and pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing),
fetched 2026-08-04). Prices are GitHub's published list; the owner's own billing
page is the authority for his account.*

Free ($0, limited, auto-model only, 2,000 completions/mo) · Pro $10 · Pro+ $39 ·
**Max $100** · Business $19/seat · Enterprise $39/seat.

The mechanics changed on **2026-06-01**: per-request "premium requests" are
legacy; billing is now **AI credits**, *"1 AI credit = $0.01 USD"*, consumed by
per-model token pricing (e.g. Claude Opus models $5/$25 per 1M in/out — the
provider's list price passed through). Monthly allowances: Pro 1,500 · Pro+
7,000 · Max 20,000 credits (base + flex). Completions and next-edit suggestions
stay unlimited outside credits. Any doc or memory reasoning in "premium
requests" (300/mo, 13-per-review, multipliers) describes the **legacy** path.

## Weaknesses — relative, not absolute

Graded per [`README.md`](README.md): worse at, not incapable of.

- **Bounded autonomy.** The 59-minute cap and one-PR-per-task shape make long
  multi-repo campaigns a poor fit for a single cloud-agent task. Not a
  limitation: Automations chain scheduled runs, and tasks can be decomposed.
- **Opaque context handling.** With no per-model context table, what fits in a
  Copilot call is not knowable from the docs alone; a context-heavy job may do
  better against the model's own API. Steer, not stop — measure before
  concluding.

## Deprecations to watch

*Source: changelog.* Gemini 2.5 Pro and Gemini 3 Flash deprecated 2026-07-31; a
batch of model deprecations announced 2026-07-31 takes effect **2026-09-01**
(the affected-model list was not extracted — check the changelog entry before
pinning any older model in an automation).

## Honest nulls

- Per-model context windows within Copilot (GitHub doesn't publish them).
- Business/Enterprise monthly credit-pool sizes (described, not quantified).
- Non-OpenAI/Anthropic per-token credit rates (tables exist; not extracted).
- The exact 2026-09-01 deprecation list.
- Nothing here is measured in this estate yet — every claim above is
  vendor-doc-sourced, none verified by a run.
