# spider-swing — what is verified about reaching it from here

> **Status:** `reference` · true as of **2026-08-08**
>
> **Scope, and it is narrow on purpose:** this file covers **reaching and
> operating on `menno420/spider-swing` from a fleet-manager session**. It is a
> different file from spider-swing's own `docs/CAPABILITIES.md`, which is
> canonical for what an agent can do **inside** that repo — read that one once
> attached; it wins on anything about the repo's internals.
>
> **Canonical for nothing.** Every row below is an index into
> [`../../CAPABILITIES.md`](../../CAPABILITIES.md) (the estate's append-only
> ledger, and the source of record) or into a dated session card. Where this
> file and the ledger disagree, the ledger wins.
>
> Certainty tags per
> [`../../findings/2026-08-05-foundation-continuation.md`](../../findings/2026-08-05-foundation-continuation.md).

## The short version

You hold **admin + push on spider-swing**, the same as every repo in the estate.
It is **public**, so read-only work needs no attach at all. Nothing about this
repo is a special case; the only thing worth knowing is which *path* to take.

## Access — re-measured 2026-08-08, this container

`MEASURED`. Same URLs back to back, one flag apart:

| endpoint | proxied | direct | direct + `$GITHUB_PAT` |
|---|---|---|---|
| `repos/menno420/spider-swing` | 403 | 200 | 200 |
| `.../rulesets` | 403 | — | 200 |
| `.../branches/main/protection` | 403 | — | **404** |
| `/user` | — | — | 200 |
| `raw.githubusercontent.com/.../main/README.md` | — | 200 | — |

Identical to the 2026-07-31 measurement, re-stamped today rather than
transcribed.

Three things follow, and the third is the one that matters:

1. **The `/user` 200 proves the token genuinely authenticates** on the direct
   path, rather than the endpoint merely serving public reads.
2. **Use direct egress** — `curl --noproxy '*'`, or `requests` with
   `trust_env=False` and `verify=/root/.ccr/ca-bundle.crt`. The proxied REST 403
   is a **path quirk**; switch flags and continue.
3. **`branches/main/protection` returns 404 on the direct path and 403 on the
   proxy.** The 404 is the true answer — no *classic* branch protection is
   configured on that repo — and the proxy turns a factual "not configured" into
   something that reads like a refusal. This is precisely how a path quirk gets
   written down as a capability wall, and it is why that row was corrected across
   two repos on 2026-07-31 (`.sessions/2026-07-31-false-github-api-wall.md`).
   **Protection is configured — as a ruleset, not classic protection.** See
   [`working-here.md`](working-here.md).

`gh` is installable (`apt-get install gh`) and works against this repo on the
direct path: `GH_TOKEN="$GITHUB_PAT" no_proxy='*' HTTPS_PROXY= gh pr list --repo
menno420/spider-swing` returns real PRs. Over the proxy the ambient `GH_TOKEN`
serves a pinned subset, so `gh api repos/menno420/spider-swing` answers 403
there — same quirk, same fix. `MEASURED` 2026-08-03, ledger.

## Review — `@codex` works on this repo's PRs

`MEASURED` 2026-08-07 on fleet-manager #812, and it is a GitHub-side relay so it
applies to any repo in the estate:

- Trigger: PR open, draft→ready, or the literal comment **`@codex review`**.
- Latency: **~335 seconds** (request 13:46:59Z → review 13:52:34Z on the exact
  head SHA). **Wait ≥6 minutes.** A 150-second probe once produced *"no review
  appeared"* written into a public PR comment as if it were evidence, followed
  by a merge three minutes before the review landed with four real findings.
- Findings arrive as **inline review comments**, not in the review body — a
  summary that looks empty is not an empty review. Read `/pulls/{n}/comments`.
- Yield: 13 findings over 5 rounds across #812/#813, several proving a PR did
  not do what its own title claimed.
- **Never merge a PR you have asked Codex to review before it answers.**
- Quota refusals are **retry-later**, never a property of the tool.

Note that `docs/providers/chatgpt.md` records Codex **cloud** as
desktop/web/CLI/IDE-only. That is a different surface from this GitHub relay and
does not bear on it.

## The Codex / ChatGPT Work surface — where this repo's history actually comes from

`MEASURED-PRIOR`, and worth knowing before assuming a Claude session built any
of this. Much of spider-swing's art and structure came from ChatGPT sessions
running under project instructions descended from substrate-kit conventions —
the first *evidenced* transfer of the kit's discipline to a non-Claude agent.
Full account: [`../../findings/2026-08-04-generated-art-pipeline.md`](../../findings/2026-08-04-generated-art-pipeline.md).

Two surface facts recorded in
[`../../execution-surfaces.md`](../../execution-surfaces.md):

- **`$GITHUB_PAT` is not universal.** Environments here carry it; the Codex side
  does not. Any recipe naming it should branch on `printenv GITHUB_PAT` rather
  than assume it. Git over the configured remote does clone/fetch/push/branch
  without it.
- **`export` in a setup script does not survive into the Codex agent phase.**
  Concretely: spider-swing's `scripts/env-setup.sh` § 5 exports `GODOT_BIN` and
  three `XDG_*` paths into `~/.bashrc` and `$CLAUDE_ENV_FILE`. The `~/.bashrc`
  half only reaches a shell that sources it, and `CLAUDE_ENV_FILE` is a
  Claude-side variable. `UNVERIFIED` on that surface — no run has been observed,
  and `execution-surfaces.md` flags it as the highest-value thing to check next.
  **This is a live, cheap, unclaimed measurement.**

## Image generation — which surface, and why it barely matters

`MEASURED` 2026-08-04, owner-run, identical cold prompts style-anchored to this
repo's Garden Spider:

| surface | instruction compliance, cold |
|---|---|
| ChatGPT | 3/3 — only surface obeying the enumerated 4-near/2-far leg layout |
| Gemini Flash | matched the painterly style, keyed cleanly, overrode layout with its own anatomy prior |
| Grok chat | muted olive instead of `#00FF00` in 3/3, plus stray web elements |
| Grok Imagine (standard) | 8+ style-matched candidates per roll, every one with a forbidden cast shadow |
| Grok Imagine (quality tier) | fixed in one step what four rounds of prompting could not |

**And the correction that matters more than the table:** re-running the same
brief through the eight-section `image-prompt` structure with the Garden Spider
attached made **all three** surfaces return a compliant keyable field, correct
leg layout and correct palette — including Grok Imagine, which had failed the
background spec on all four prior cold attempts. The shipped art's advantage is
a committed contract, a serial gate and a numeric audit, **none of which is a
model property.** Reach for the skill, not for a different provider.

## Related surfaces used on this repo's work

- **Shared AI chat transcripts are readable** — `share.gemini.google/…`,
  `chatgpt.com/share/…` yield full text through headless Chromium (70,426
  characters extracted twice). A plain fetcher returns app shell with zero
  conversation, which is a *false empty*, not an empty page. Tool:
  `tools/read_shared_chat.py`. `MEASURED` 2026-08-03.
- **Gemini for reading volume** — default to **Vertex** (draws the prepaid
  credit); the free `GEMINI_API_KEY` serves AI Studio including the Interactions
  API. Recipe and the billing chain:
  [`../../conventions/vertex-first-for-gemini.md`](../../conventions/vertex-first-for-gemini.md).
- **Grounded citations are leads, not facts.** Measured twice in seven queries
  on this repo's Play research: a zero-`groundingChunks` response is formatted
  identically to a grounded one, and one citation pointed at a plausible wrong
  page. Read `groundingMetadata` / `urlContextMetadata` every time.

## Honest nulls

- **No claim here is about spider-swing's internals.** Its own
  `docs/CAPABILITIES.md` covers those and has not been read into this file
  deliberately — that would be the copy this folder exists to avoid.
- **`android-release.yml` has never been observed running end to end.** Recorded
  as an honest null in the 2026-08-05 session card; it is not known to be
  broken, it is unexercised.
- **The Codex setup-export behaviour is inferred from the two surfaces' contracts**,
  not from an observed spider-swing run.
