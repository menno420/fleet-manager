# Claude — provider capability reference

> **Status:** `living-ledger`
>
> Models, surfaces, and what a session in this estate can actually do. Model
> facts current as of 2026-06-24 (the `claude-api` skill's cached table); the
> estate-specific findings are measured here and dated. **Not a routing table** —
> see [`README.md`](README.md).

## Models

| Model | ID | Context | Max output | $/1M in | $/1M out |
|---|---|---|---|---|---|
| Fable 5 | `claude-fable-5` | 1M | 128K | $10 | $50 |
| Mythos 5 | `claude-mythos-5` | 1M | 128K | $10 | $50 |
| **Opus 5** | `claude-opus-5` | 1M | 128K | $5 | $25 |
| Opus 4.8 | `claude-opus-4-8` | 1M | 128K | $5 | $25 |
| Opus 4.7 | `claude-opus-4-7` | 1M | 128K | $5 | $25 |
| Sonnet 5 | `claude-sonnet-5` | 1M | 128K | $3 | $15 |
| Haiku 4.5 | `claude-haiku-4-5` | 200K | 64K | $1 | $5 |

These are **API** prices. The consumer subscription (claude.ai / Claude Code) is
a separate ladder and is not billed per token.

Two things worth knowing about the IDs: they carry **no date suffix** —
`claude-sonnet-5`, never `claude-sonnet-5-20251114` — and a model string that
looks unfamiliar is more likely to postdate a given session's training than to be
wrong. Mythos 5 is invitation-scoped (Project Glasswing); everything else is
generally available.

For anything beyond this table — thinking parameters, effort levels, tool
definitions, migration between models — **invoke the `claude-api` skill rather
than answering from memory.** Several parameter shapes changed during 2025–2026
and a recalled pattern is likely to be a 400.

## The surfaces

| Surface | What it is | Notable |
|---|---|---|
| **Claude Code — web** | Sessions in a managed remote container, started from claude.ai/code, mobile, or a trigger | Where this estate's work happens. Repo cloned fresh per session; container reclaimed after inactivity, so anything worth keeping must be committed |
| **Claude Code — CLI / desktop / IDE** | Same agent, local machine | No agent proxy, so the GitHub path quirks below do not apply |
| **claude.ai** | Chat, Projects, Artifacts | Projects carry instructions + files; separate from Code sessions |
| **API** | `POST /v1/messages` and the surrounding endpoints | Where model IDs and per-token pricing above apply |
| **Managed Agents** | Anthropic runs the agent loop and hosts a per-session sandbox | Versioned agent configs, scheduled deployments, vault-held credentials |

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

## Known failure modes of Claude sessions in this estate

Written down because they are ours, they recur, and a session that knows them
catches them earlier than the owner does.

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

## Verify before building on this

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```

Model facts: invoke the `claude-api` skill. Estate capabilities:
[`../CAPABILITIES.md`](../CAPABILITIES.md), and re-verify anything past the
14-day staleness window before depending on it.
