# Claude — provider capability reference

> **Status:** `living-ledger`
>
> Models, surfaces, and what a session in this estate can actually do. **Model
> facts re-derived 2026-08-04 from Anthropic's own
> [models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
> and the [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/api),
> read in full** — replacing the `claude-api` skill's 2026-06-24 cached table,
> which had gone stale (it predated Sonnet 5 and Opus 5 entirely).
> **Not a routing table** — see [`README.md`](README.md).

## Models

*Source: vendor docs (models overview, fetched 2026-08-04).*

| Model | ID | Context | Max output | $/1M in | $/1M out | Thinking | Cutoff¹ |
|---|---|---|---|---|---|---|---|
| Fable 5 | `claude-fable-5` | 1M | 128k | $10 | $50 | adaptive, **always on** | Jan 2026 |
| Mythos 5 | `claude-mythos-5` | 1M | 128k | $10 | $50 | adaptive, always on | Jan 2026 |
| **Opus 5** | `claude-opus-5` | 1M | 128k | $5 | $25 | adaptive, on by default | May 2026 |
| Sonnet 5 | `claude-sonnet-5` | 1M | 128k | $3 | $15 ² | adaptive, on by default | Jan 2026 |
| Haiku 4.5 | `claude-haiku-4-5-20251001` (alias `claude-haiku-4-5`) | 200k | 64k | $1 | $5 | extended thinking (manual) | Feb 2025 |

¹ "Reliable knowledge cutoff" per the vendor table; training-data cutoff is broader.
² **Introductory pricing $2 / $10 through 2026-08-31** (release notes, 2026-06-30).

These are **API** prices. The consumer subscription (claude.ai / Claude Code) is
a separate ladder and is not billed per token. Legacy models still served: Opus
4.8, 4.7, 4.6, Sonnet 4.6, Sonnet 4.5, Opus 4.5 — and Opus 4.1, **deprecated
with retirement 2026-08-05**.

Corrections to the previous version of this table, for the record: it carried
Opus 4.7/4.8 as current when Opus 5 shipped 2026-07-24; it had no launch dates at
all; and it stated that IDs "carry no date suffix" as a general rule — the
vendor's actual rule is that **dateless IDs started with the 4.6 generation and
are pinned snapshots, not evergreen pointers**, while earlier models (including
Haiku 4.5) keep dated IDs with dateless aliases.

### Model-level notes that change how you call them

*Source: vendor release notes, 2026 entries, read in full 2026-08-04.*

- **Fable 5 / Mythos 5** (launched 2026-06-09): adaptive thinking is the *only*
  mode — `thinking: {"type": "disabled"}`, manual budgets, and assistant prefill
  all return 400. Runs safety classifiers; a declined request returns
  `stop_reason: "refusal"` (unbilled if nothing was generated), with an opt-in
  `fallbacks` parameter to re-run on another model. Requires 30-day data
  retention — not available under zero-data-retention. Access was suspended and
  **restored 2026-07-01** (vendor statement: anthropic.com/news/redeploying-fable-5).
  Mythos 5 is invitation-only (Project Glasswing, defensive cybersecurity).
- **Opus 5** (launched 2026-07-24): effort is the primary control — full ladder
  `low`→`max`. Disabling thinking is allowed only at effort `high` or below;
  `disabled` + `xhigh`/`max` returns 400 (breaking change from Opus 4.8).
- **Sonnet 5** (launched 2026-06-30): manual extended thinking removed (400);
  non-default `temperature`/`top_p`/`top_k` return 400; no Priority Tier.
- **Tokenizer:** Opus 4.7 introduced a new tokenizer used by everything since
  (Fable 5, Sonnet 5, Opus 5): **the same text produces roughly 30% more tokens**
  than pre-4.7 models. Budget arithmetic carried over from old sessions is wrong
  by about that margin.
- **Effort defaults to `high`** on Opus 4.8 (all surfaces) and on Opus 5 /
  Sonnet 5 (API and Claude Code). Set it explicitly to spend less.
- **Max output is 128k on the synchronous API**; the Batch API reaches **300k**
  on Opus 5/4.8/4.7/4.6 and Sonnet 5/4.6 with the `output-300k-2026-03-24` beta
  header.
- **Query capabilities programmatically:** `GET /v1/models` returns
  `max_input_tokens`, `max_tokens`, and a `capabilities` object per model —
  cheaper than trusting any cached table, including this one.

### Retirements ledger

*Source: vendor release notes.* Opus 4.1 retires **2026-08-05**. Already
retired: Opus 4 + Sonnet 4 (2026-06-15), Haiku 3 (2026-04-20), Sonnet 3.7 +
Haiku 3.5 (2026-02-19), Opus 3 (2026-01-05). The 1M-context beta for Sonnet
4.5/4 ended 2026-04-30. A request to a retired ID errors — an unfamiliar-looking
current ID is more likely to postdate your training than to be wrong.

For parameter shapes — thinking config, effort, tool definitions, migration —
**invoke the `claude-api` skill rather than answering from memory**, then trust
the vendor docs over the skill where they disagree; this file is evidence they
can disagree.

## Platform features a session might not know exist

*Source: vendor release notes, 2026 entries.* Dated because they postdate many
models' training:

- **Mid-conversation system messages** — `role: "system"` after a user turn,
  cache-preserving; Fable 5, Mythos 5, Opus 4.8+ (no beta header).
- **Automatic prompt caching** (2026-02-19) — one `cache_control` field, the
  cache point moves forward automatically.
- **Compaction API** (beta) — server-side context summarization.
- **Task budgets** (beta) — advisory token budget for a whole agentic loop, with
  a running countdown the model sees.
- **Advisor tool** (beta) — a higher-intelligence model advising a faster
  executor mid-generation.
- **Fast mode** — Opus 4.8 only now (research preview); removed for 4.6
  (2026-06-29) and 4.7 (2026-07-24).
- **Code execution is free with web search/fetch** (2026-02-17); web search,
  programmatic tool calling, tool search, memory tool all GA.
- **Docs moved:** `docs.claude.com` now redirects to `platform.claude.com/docs`
  (console moved 2026-01-12; measured here 2026-08-04).

## The surfaces

*Source: vendor docs + measured here.*

| Surface | What it is | Notable |
|---|---|---|
| **Claude Code — web** | Sessions in a managed remote container, started from claude.ai/code, mobile, or a trigger | Where this estate's work happens. Repo cloned fresh per session; container reclaimed after inactivity, so anything worth keeping must be committed |
| **Claude Code — CLI / desktop / IDE** | Same agent, local machine | No agent proxy, so the GitHub path quirks below do not apply |
| **claude.ai** | Chat, Projects, Artifacts | Projects carry instructions + files; separate from Code sessions |
| **API** | `POST /v1/messages` and the surrounding endpoints | Where model IDs and per-token pricing above apply. Also reachable via Bedrock, Google Cloud, Microsoft Foundry, and **Claude Platform on AWS** (first-party API, AWS billing — launched 2026-05-11) |
| **Managed Agents** | Anthropic runs the agent loop and hosts a per-session sandbox | Public beta 2026-04-08. Versioned agents, scheduled deployments, vault-held credentials, webhooks, memory stores |

## What a Code session can do here — measured

All verified in this estate; each has a dated entry in
[`../CAPABILITIES.md`](../CAPABILITIES.md).

- **Full GitHub authority.** Admin + push on every repo in the estate, over the
  direct-PAT path and via the MCP GitHub tools. Merging own PRs, deleting
  branches, changing rulesets, creating releases and secrets are all ordinary
  work.
- **Media is readable end to end.** Video via `ffmpeg` frame extraction; audio via
  transcription; PDFs by rendering pages. And **client-rendered web pages** via
  headless Chromium — see
  [`../conventions/reading-shared-ai-chats.md`](../conventions/reading-shared-ai-chats.md).
- **Arbitrary bash, plus package installation.** `apt-get` and `pip` both work.
  A missing binary is a one-command fix, not a wall.
- **Skills.** Kit-shipped skills are staged into `.substrate/skills/` and must be
  **installed** to `.claude/skills/` by the host before they are invocable — the
  kit never writes a live `.claude/` tree. Locally-authored skills in
  `.claude/skills/` survive kit upgrades. See
  [`../SKILLS-local.md`](../SKILLS-local.md).

## The three quirks that have produced false walls

*Source: measured here, each with a dated CAPABILITIES entry.*

Each of these has been recorded as a wall at least once and each is a path
problem, not a capability limit.

**1. The proxied GitHub REST path 403s; the direct path does not.** Over the
agent proxy, `gh api user` answers but `gh api repos/{owner}/{repo}` returns
*"GitHub access is not enabled for this session. An org admin must connect the
Claude GitHub App for this organization"*, and GraphQL returns *"only the pinned
set of PR-review operations is served"*. Both succeed on the direct path. The
error names an org admin and a settings page, which is why it reads as a
permission problem — it is not.

```bash
curl -sS --noproxy '*' -H "Authorization: Bearer $GITHUB_PAT" \
  -o /dev/null --write-out '%{http_code}\n' https://api.github.com/repos/<owner>/<repo>
```

A 200 here means the access is fine and the failure was the path.

**2. `$GITHUB_PAT` is environment-scoped, not universal.** Some environments
carry it, some do not. Check before reaching for it — and note that its absence
is not a blocker either: git over the configured remote does
clone/fetch/push/branch without it.

```bash
printenv GITHUB_PAT >/dev/null && echo present || echo absent
```

**3. Chromium's TLS trust is separate from everything else's.** `curl`, Python
`requests`, Java and Node all read `/root/.ccr/ca-bundle.crt`; Chromium reads an
NSS database at `/root/.pki/nssdb` which does not exist on a fresh container. So
"TLS is preconfigured" and "the browser cannot verify anything" are both true.
Fix by importing the bundle with `certutil` — never by disabling verification.
`tools/read_shared_chat.py --setup` does it.

## Weaknesses — relative, not absolute

Graded on the distinction in [`README.md`](README.md): worse at, not incapable of.

- **Image and video generation.** Weak to absent in chat. A session asked for a
  concept sprite, a mockup or a video will not produce one the way the other two
  providers will. **Not a limitation** — it can write the code that renders an
  image, drive a tool that generates one, and read and critique any image it is
  given; the gap is in-chat generation, not visual work.
- **Speed on interactive turns.** Deliberate rather than fast — good for
  long-horizon work, worse when the value is in rapid back-and-forth.
- **First-party consumer integrations.** No native Gmail/Calendar/Drive
  equivalent to Gemini's Personal Intelligence. Reaching those is connector or
  API work rather than a built-in.

## Known failure modes of Claude sessions in this estate

*Source: measured here.* Written down because they are ours, they recur, and a
session that knows them catches them earlier than the owner does.

- **Stating a limit that was never tested.** The single most expensive pattern
  here — twice in one day on 2026-08-03, both caught by the owner rather than by
  a guard. `tools/check_no_false_walls.py --strict` catches present-tense denial
  phrasing **in living docs only**; a false wall stated in chat passes it clean.
- **Generalising from one successful probe.** `gh api user` succeeding was read
  as "auth works" when only that endpoint was served. Both halves of a two-part
  check have to run before either is written down.
- **`$?` after a pipe.** Reports the last command in the pipeline, so a red gate
  reads green. Capture the checker's own exit code.
- **Local green is not CI green.** At least one gate check fires only on a card
  added in the merge-base diff, so it passes locally and fails in CI.
- **Re-reading a document is not re-deriving it.** A grounding block was re-read
  and passed as sound while contradicting, in four places, the files it named.
- **A cached table is not a source.** This file's own model table sat on a
  skill cache for six weeks and missed two model launches. The Models API and
  the vendor changelog are one fetch away.

## Verify before building on this

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```

Model facts: the [models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
and `GET /v1/models` outrank both the `claude-api` skill's cache and this table.
Estate capabilities: [`../CAPABILITIES.md`](../CAPABILITIES.md), and re-verify
anything past the 14-day staleness window before depending on it.
