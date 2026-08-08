# spider-swing — what fleet-manager has written about it

> **Status:** `reference` · index built **2026-08-08**
>
> **This is the one thing fleet-manager is genuinely canonical for:** what
> happened in sessions run from here. Every file below stays exactly where it
> sits — nothing was moved, renamed or rewritten to build this index, by design
> (`OD-3`/`OD-6`: nothing is deleted).
>
> **28 files in this repo mention spider-swing** and until now nothing indexed
> them, so finding the art-pipeline finding meant already knowing it existed.
> Each row gets one line on **what it is and when to reach for it** — that line
> is the whole value; the file itself is the record.

## Findings — the durable research

| file | what it is |
|---|---|
| [`../../findings/2026-08-04-generated-art-pipeline.md`](../../findings/2026-08-04-generated-art-pipeline.md) | **The most important file here.** How the art got consistent, and why it is *not* a prompting story: a committed contract, a serial gate and a numeric audit. Produced program law **PL-013 — inhabiting beats observing**. Read before generating anything, or before believing a provider comparison explains the quality |
| [`../../findings/2026-08-05-google-play-submission-requirements.md`](../../findings/2026-08-05-google-play-submission-requirements.md) | Every Play requirement with the URL **this estate fetched itself**, and explicit `NULL — unverified` for anything it could not confirm. Also where the AAB-from-Godot numbers come from (read out of engine source, because the class reference never gives them) |
| [`../../findings/2026-08-05-owner-calibration-three-sessions.md`](../../findings/2026-08-05-owner-calibration-three-sessions.md) | Tangential to this repo but load-bearing for how to treat the owner's statements: his corrections counted, independently, across three sessions |

## Research — the Gemini/visual-QA line

| file | what it is |
|---|---|
| [`../../research/2026-08-03-gemini-visual-qa-gem.md`](../../research/2026-08-03-gemini-visual-qa-gem.md) | The spider-swing visual-QA Gem, paste-ready in three blocks, plus its four-point acceptance test. The fourth point — a repository-history question asked mid-review — is the one that catches the expensive failure |
| [`../../research/2026-08-03-gemini-report-verification.md`](../../research/2026-08-03-gemini-report-verification.md) | A Gemini report **about this repo**, verified claim by claim. The template for treating any model report as leads rather than facts |
| [`../../research/2026-08-03-reducing-invented-detail.md`](../../research/2026-08-03-reducing-invented-detail.md) | Why a model invents specifics, and the procedure that stops it |

## Session cards — grouped by the thread they belong to

**Google Play / naming** *(the release thread)*
- [`2026-08-05-play-submission-requirements`](../../../.sessions/2026-08-05-play-submission-requirements.md) — the three-week floor found: *"the requirement everyone repeats is rarely the one that sets the date"*
- [`2026-08-05-play-closed-test-and-gemini-benchmark`](../../../.sessions/2026-08-05-play-closed-test-and-gemini-benchmark.md) — same model, same key, opposite answers to "how many testers", decided by which **tool** it used. `url_context` retrieval scored 0/8 on `support.google.com`
- [`2026-08-05-name-decided-queue-sync`](../../../.sessions/2026-08-05-name-decided-queue-sync.md) — the queue still recommended an identifier from a ruled-out name while the owner was on the *Create app* form. Caught by grep, not recall

**Art** *(the paused pipeline thread)*
- [`2026-08-04-hub-art-pipeline-archaeology`](../../../.sessions/2026-08-04-hub-art-pipeline-archaeology.md) — reading the six ChatGPT transcripts that made the art
- [`2026-08-04-hub-chroma-spill-measured`](../../../.sessions/2026-08-04-hub-chroma-spill-measured.md) — measuring the chroma claim instead of quoting it; the session that reversed the causal direction
- [`2026-08-04-hub-skill-family-and-audit`](../../../.sessions/2026-08-04-hub-skill-family-and-audit.md) — fresh-eyes audit + the `image-prompt` family
- [`2026-08-04-hub-final-three-skills`](../../../.sessions/2026-08-04-hub-final-three-skills.md) — `audio-prompt`, `capability-probe`, `owner-brief`

**Capability corrections that started here**
- [`2026-07-31-false-github-api-wall`](../../../.sessions/2026-07-31-false-github-api-wall.md) — the false `api.github.com` wall, found in an owner-live spider-swing session and carried back here. Also the **false guardrail** finding, which is the costlier inverse
- [`2026-08-03-hub-gh-is-not-a-wall`](../../../.sessions/2026-08-03-hub-gh-is-not-a-wall.md) — `gh` installable fleet-wide; its absence never blocked anything
- [`2026-08-03-hub-surfaces-and-prompt-skills`](../../../.sessions/2026-08-03-hub-surfaces-and-prompt-skills.md) — execution surfaces documented; the kit's staged skills finally *installed*
- [`2026-08-03-hub-gemini-video-qa-gem`](../../../.sessions/2026-08-03-hub-gemini-video-qa-gem.md) — tier research, grounding block, share-link capability
- [`2026-08-05-gemini-retrieval-not-reading`](../../../.sessions/2026-08-05-gemini-retrieval-not-reading.md) — it was retrieval, not reading
- [`2026-08-01-e1-owner-reserved`](../../../.sessions/2026-08-01-e1-owner-reserved.md) — why program step E1 is deferred, and that spider-swing is the reason

**This folder**
- [`2026-08-08-index-layer2-spider-swing`](../../../.sessions/2026-08-08-index-layer2-spider-swing.md) — the session that built `docs/repos/spider-swing/`

## Living documents that carry spider-swing content

These are **not** spider-swing records — they are estate-wide files with
spider-swing sections. Go to the section, not the file.

| file | the spider-swing part |
|---|---|
| [`../../owner-queue.md`](../../owner-queue.md) | `OQ-PLAY-APP-ID`, `OQ-PLAY-UPLOAD-KEY`, `OQ-PLAY-LISTING`, `OQ-SWINGY-NAME` (resolved). **The authoritative list of what waits on the owner** |
| [`../../CAPABILITIES.md`](../../CAPABILITIES.md) | The measured access rows, the `@codex` relay entry, the image-surface comparison. 1,638 lines — reach via `capabilities.md` in this folder, which indexes the relevant ones |
| [`../../execution-surfaces.md`](../../execution-surfaces.md) | The Codex-side `env-setup.sh` export gap, and `$GITHUB_PAT` not being universal |
| [`../../planning/2026-07-26-consolidation-program.md`](../../planning/2026-07-26-consolidation-program.md) | Why E1 is owner-reserved: *"every evening since 07-26 has gone to spider-swing… deferring E1 for it is triage, not neglect"* |
| [`../../providers/chatgpt.md`](../../providers/chatgpt.md) · [`../../providers/grok.md`](../../providers/grok.md) | Per-provider rows measured on this repo's art work |

## Skills this repo produced

Worth its own section because the direction is unusual: **spider-swing is the
source, and the estate is the adopter.** Five installed skills were
reverse-derived from its art sessions and carry its measurements as their
grounds — `image-prompt` (the shared method) routing to `sprite-prompt`,
`parallax-prompt` and `cover-art-prompt`, plus `asset-pipeline` for the
post-generation half and `audio-prompt` against its committed audio contract.

Where this index and a skill disagree, **the skill wins** — it is the living
copy and the one that actually fires.

## What is deliberately not indexed here

spider-swing's own 142 session cards, its ADRs, and its `docs/` tree. Those are
canonical **in that repo** and indexing them from here would create a second
list that drifts. `README.md` § "Once attached" points at its reading path
instead.
