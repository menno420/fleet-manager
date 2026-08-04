# 2026-08-04 · hub — provider references at model granularity, broadened past the first three

> **Status:** `complete`

- **📊 Model:** fable-5 · high · research — per-model capability sweep across providers

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1`

💡 Session idea: **a capability reference keyed to products answers "where do I
click"; keyed to models it answers "can this be done at all" — and sessions need
the second question far more often.** The first three provider docs described
surfaces (modes, plans, apps) because surfaces are what a browser shows. But the
questions a session actually brings — how much context fits, what modalities go
in and out, whether tool use and structured reasoning exist on this thing — are
properties of the *model*, and the same product answers them differently
depending on which model is selected. A reference that stops at the product layer
forces every session to re-derive the model layer, which is exactly the
re-derivation these docs exist to end.

## previous-session review

`2026-08-04-hub-provider-docs-accuracy-pass.md` (PR #707, merged) re-derived
gemini.md from the official release notes and closed on *when a process can fail
silently, the artifact should carry the evidence of how much work went into it*,
proposing a sourcing line per section. That card's own honest-nulls list was
better than its predecessor's — it named the Anthropic changelog gap that this
session now works — and its sourcing-line proposal is adopted here: every file
this session touches carries per-section source classes.

## Scope

Owner: make the set answer *what each model can do*, not limited to the three
covered so far. This session: (1) sweep Anthropic's own changelog and re-derive
claude.md's model table from it — the table has only ever been a skill cache;
(2) deepen chatgpt.md's model coverage from the reachable vendor docs site;
(3) broaden with new provider files, changelog-first, ordered by plausible use in
this estate. Not a program step; the NOW pointer (E1) is untouched.

## What landed

- **`claude.md`** — model table re-derived from Anthropic's own models overview
  and the full Platform release notes (both read in full). The cached table had
  missed two model launches: Sonnet 5 (2026-06-30, intro pricing, manual
  thinking removed, ~30% tokenizer shift) and Opus 5 (2026-07-24, thinking on
  by default, effort-ladder breaking change). Added the retirements ledger
  (Opus 4.1 dies 2026-08-05), the Fable 5 suspension/restoration (2026-07-01),
  and a new failure-mode entry: *a cached table is not a source.* Also
  corrected the "IDs carry no date suffix" claim — the vendor's rule is
  dateless-from-4.6, pinned snapshots.
- **`chatgpt.md`** — a vendor-sourced Models section. Reachability finding:
  `platform.openai.com/docs` 301s to **`developers.openai.com`, which answers
  cleanly** — OpenAI's API specs and deprecation schedule were never behind
  the help-center 403, just at an address nobody had tried. GPT-5.6
  sol/terra/luna specs, the five-level reasoning ladder, audio/image as
  separate model lines, and dated retirements with named replacements.
- **Five new files**, changelog/vendor-doc first, every claim cited or marked,
  honest nulls per file: **`github-copilot.md`** (multi-provider picker,
  cloud-agent environment — where *secrets DO reach the agent phase*, the
  designed opposite of Codex; AI-credits billing), **`grok.md`** (six text
  models, the generation stack, retired slugs that silently redirect),
  **`deepseek.md`** (V4 pair, MIT weights, peak-hour pricing), **`mistral.md`**
  (per-model license mix governing self-hosting), **`meta-llama.md`** (Llama 4
  as the last open generation; the Muse pivot, with the proprietary claim
  marked press-sourced).
- **`README.md`** — index rebuilt around model granularity, ordered by
  plausible use in this estate.

Coverage call, made without blocking on approval per the standing directive:
Copilot, Grok, DeepSeek, Mistral, Meta — ordered GitHub-adjacency first, then
API-relevant frontier providers, then open-weights lines. Perplexity, Cohere,
Qwen et al. left for a future pass; no genuine fork arose, so nothing was
routed to §6.

## Honest nulls

- **The five new files are vendor-doc-sourced and estate-unmeasured** — every
  file says so. Measurement (a probe call, a cloud-agent run) is the natural
  next pass.
- **x.ai's news domain 403s** (Cloudflare) — Grok announcement dates are
  docs-release-notes months plus search snippets, marked as such. xAI publishes
  max-output for no model.
- **help.openai.com stays unprobed** per the standing note; the owner said he
  would look at OpenAI's changelogs — the developers.openai.com finding may
  make that moot, worth telling him.
- **llama.com/developer.meta.com is a JS shell to fetchers** — a headless-
  Chromium pass could close it; not attempted this session.
- **Consumer-surface → model-ID mappings are published by almost nobody**
  (grok.com, chat.deepseek.com, consumer ChatGPT) — recurring null across
  files, and the owner's own model pickers remain the authority.
- The Codex agent-phase-exports check and the boot-read-path question remain
  open from the previous card; neither was this session's scope.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
