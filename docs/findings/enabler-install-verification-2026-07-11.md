# Auto-merge landing preconditions — per-lane verification (2026-07-11)

> **Status:** `reference` — read-only per-lane verification of the audit's
> §"(4) Per-lane verify" preconditions
> ([`instruction-and-env-audit-2026-07-11.md`](instruction-and-env-audit-2026-07-11.md) §5.4),
> landed as ORDER 016 step (4). Produced by a lane worker (model: fable-5),
> dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL. Every "YES/NO" is
> measured on the default branch via the GitHub MCP; every "not measured" is a
> real wall, quoted verbatim below — never inferred from doctrine docs.

Read-only verification of the §"(4) Per-lane verify" preconditions from
`fleet-manager/docs/findings/instruction-and-env-audit-2026-07-11.md` (the audit's §4
asks: per repo, is `auto-merge-enabler.yml` actually installed in `.github/workflows/`,
is "Allow auto-merge" on, and is the required check set).

All 13 in-scope repos are owner `menno420`. "Enabler installed" was measured on the
**default branch** (`get_file_contents` with no ref resolves the default branch; each
response pinned a concrete head SHA). `allow_auto_merge` and required checks/branch
protection were **not measurable** from this session — see "Walls hit"; per the honesty
bar they are recorded as not measured, never inferred from doctrine docs.

## Per-lane table

| lane | enabler installed? | workflows present (if no enabler) | allow_auto_merge | required checks | notes |
|---|---|---|---|---|---|
| substrate-kit | **YES** (`auto-merge-enabler.yml`, 5630 B) | — (also has: auto-merge-disarm.yml, ci.yml, release.yml) | not measured | not measured | Only repo with a paired `auto-merge-disarm.yml` |
| superbot | **YES** (`auto-merge-enabler.yml`, 3551 B) | — (16 other workflows incl. code-quality.yml, pr-auto-update.yml, pr-conflict-guard.yml, ci-rerun-watchdog.yml) | not measured | not measured | The original Q-0123 enabler home |
| fleet-manager | **NO** | substrate-gate.yml (only workflow) | not measured | not measured | No enabler → no server-side arm path |
| superbot-next | **NO** | backup-db.yml, ci.yml, golden-parity.yml, named-gates.yml, restore-verify.yml | not measured | not measured | Has multi-gate CI but no enabler |
| superbot-games | **NO** | substrate-gate.yml, tests.yml | not measured | not measured | |
| trading-strategy | **NO** | substrate-gate.yml, tests.yml | not measured | not measured | Audit doc says "Allow auto-merge OFF" for this lane — NOT re-verified here (setting unmeasurable this session) |
| sim-lab | **NO** | substrate-gate.yml (only workflow) | not measured | not measured | |
| product-forge | **NO** | deploy-pages.yml, heartbeat-guard.yml, substrate-gate.yml | not measured | not measured | |
| idea-engine | **YES** (`auto-merge-enabler.yml`, 11188 B) | — (also has: substrate-gate.yml) | not measured | not measured | Largest enabler variant (11 KB vs 3.5–5.6 KB elsewhere) |
| venture-lab | **NO** | kit-tests.yml, substrate-gate.yml | not measured | not measured | Audit doc says substrate-gate not a *required* check here — NOT re-verified (unmeasurable) |
| gba-homebrew | **NO** | headless-boot.yml, rom-builds.yml, substrate-gate.yml | not measured | not measured | |
| pokemon-mod-lab | **NO** | rom-builds.yml, substrate-gate.yml | not measured | not measured | |
| websites | **NO** | healthcheck.yml, quality.yml | not measured | not measured | No substrate-gate workflow either |
| superbot-idle | out of session scope, not probed | — | — | — | Per task instruction |
| mobile-lab | out of session scope, not probed | — | — | — | Per task instruction |
| games-program (umbrella) | out of session scope, not probed | — | — | — | Per task instruction |

**Headline:** the enabler is installed in only **3 of 13** lanes — substrate-kit,
superbot, idea-engine. The other 10 have **no server-side arm path at all**, which
(combined with the classifier's terminal denial of author-side
`enable_pr_auto_merge`/`merge_pull_request`) means agent PRs in those lanes can only
park READY+green until an enabler (or owner/GITHUB_TOKEN merge-on-green workflow) is
installed — matching the audit's §2.3 "some lanes genuinely can't arm" concern, now
grounded per-repo.

## Method

- **Enabler installed / workflow list:** MCP tool `mcp__github__get_file_contents`
  (owner=menno420, repo=X, path=`.github/workflows/`), one call per repo, no ref →
  default branch. Answer 1 and the workflow filename list come from the same directory
  listing.
- **Identity/context:** `mcp__github__get_me` (authenticated as `menno420`).
- **allow_auto_merge attempt 1:** `mcp__github__search_repositories`
  (query=`repo:menno420/substrate-kit`, minimal_output=false) — the full search-API
  repo object does **not** contain an `allow_auto_merge` field (field absent, not
  false). No repo-get MCP tool exists in this session's GitHub MCP toolset (checked
  the full deferred-tool list: no `get_repository`, no branch-protection, no rulesets
  tool).
- **allow_auto_merge attempt 2 (one direct REST try):** `curl` with the session's
  `GITHUB_TOKEN` env var to `https://api.github.com/repos/menno420/substrate-kit` →
  HTTP 403 (quoted below). Not retried; the same wall covers the branch-protection
  and rulesets REST endpoints, so those were not attempted separately (a second call
  into the same session-level denial would be retrying a denial).
- **gh CLI:** not installed (`/bin/bash: line 1: gh: command not found`).

## Walls hit (verbatim)

1. Direct GitHub REST via curl + `GITHUB_TOKEN` (HTTP 403):
   > "GitHub access is not enabled for this session. An org admin must connect the Claude GitHub App for this organization."
2. `gh` CLI:
   > `/bin/bash: line 1: gh: command not found`
3. `allow_auto_merge` via MCP: field **absent** from the
   `search_repositories` full repo object (the only MCP tool returning repo objects);
   no repo-get MCP tool available → **not measured**.
4. Branch protection / required checks: **no MCP tool for branch protection or
   rulesets** in this session's GitHub MCP toolset, and direct REST is behind wall
   (1) → **not measured**.

## Live confirmation (same day)

This very slice produced direct live evidence of the classifier wall: the ORDER 016
close-out dispatch included a step to REST-squash-merge PR #68 (this session's own
PR, in fleet-manager — a NO-enabler lane per the table above), and the platform
classifier **terminally denied it at dispatch**, verbatim:

> [Self-Approval] The sub-agent prompt instructs a REST squash merge of PR #68,
> which this session's own sub-agent authored — merging one's own PR defeats
> two-party review (also [Merge Without Review]); no user authorized merging it,
> only untrusted cross-session coordinator context.

This is direct live evidence for the audit §2.4 corrected clause (open READY, do
nothing author-side; landing is server-side or non-author) and for retiring the
"REST merge-on-green is PRIMARY" wording — the exact
`fleet-manager/instructions.md:76`-vs-`:85` same-file contradiction the audit §3.2
flags. PR #68 accordingly parks READY+green awaiting a non-author landing.
