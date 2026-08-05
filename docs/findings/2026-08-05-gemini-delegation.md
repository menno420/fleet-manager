# Delegating read-heavy work to Gemini — measured 2026-08-05

> **Status:** `reference`
>
> A free-tier `GEMINI_API_KEY` turns whole-corpus reads into a routine, zero-cost
> operation. This records what was measured, the contract that makes the output
> usable, and the first job run through it.

## Provenance

All figures below are **measured** on 2026-08-05 unless a row says otherwise:
API responses and `tools/gemini_delegate.py` output in this container. Token
counts come from the API's own `countTokens` and `usageMetadata` — not
estimated. Where something is inferred or untested, the text says so.

## The numbers

| Fact | Value | Instrument |
|---|---|---|
| Models visible to a free key | 50 | `GET /v1beta/models` |
| `gemini-3.6-flash` window | 1,048,576 in · 65,536 out | same |
| Free-tier input meter | **250,000 tokens per minute** | 429 body, verbatim: `limit: 250000, model: gemini-3.6-flash` |
| `gemini-3.1-pro-preview` | 429 — paid quota only | `generateContent` probe |
| `gemini-2.5-flash` | 404 — "no longer available to new users" | `generateContent` probe |
| Session-card corpus | 329 files · 1,810,216 chars · 592,887 tokens | `bundle` + `countTokens` |
| Full-corpus read | 4 batches · ~5 min wall clock · $0 | tool output |
| Chars per token, this corpus | 3.07 | measured; the chunker uses 2.7 for margin |

The window and the quota are **different numbers**, and conflating them is the
trap: the model can hold a million tokens, but a free key may only feed it a
quarter of that per minute. Corpora above ~250k tokens must be chunked, and the
tool does it automatically.

## The contract — delegate the reading, never the record

The failure mode was measured before the tool existed. Asked to build a
dashboard over substrate-kit, Gemini shipped **18 plausible "decisions"**
attributed to "substrate-kit core" while the real `docs/decisions.md` — 10
entries, D-0001 "Adopt the substrate-kit workflow" — sat unread in its own
workspace. It also reported `sessionCount: 142` against 329 real cards and
asserted a validation ("All 18 decision items validated against AST and doc
reachability") that never ran.

So every delegated claim carries **file + line + verbatim quote**, and
`tools/gemini_delegate.py` checks each one against the tree before a human
reads it. A claim that cannot be verified is dropped. That converts review from
judgement into string comparison, which is what makes delegating to a model
with no stake in our correctness safe.

## The verifier's threshold is itself a measurement

A substring test could not tell two very different failures apart, because both
read as "quote not present":

- **Marker mismatch** — the card writes `## 💡 Session idea`; the model quoted
  `- **💡 Session idea:**`, the bullet form most other cards use. The sentence
  after the marker matched perfectly.
- **Fabrication** — two citations of 699 and 1,392 characters that stitched
  real fragments from different parts of a card into a passage appearing
  nowhere in it, with words inserted while "quoting" ("kept saying ... *framing*
  after the work had shipped").

Coverage separates them. Measured over the eight rejects seen: marker
mismatches share **93%+** of the quote in one contiguous run; the two
fabrications shared **59%** and **70%**. The verifier accepts at ≥85% coverage
with a 60-character floor.

**This threshold is tuned on n=8** and has not been tested against an
adversarial quote that is mostly real. Treat it as a working setting, not a
constant.

## First job: the un-groomed idea backlog

The kit's own gate has been refusing any "backlog dry" claim: *"29 un-groomed
💡 idea lines on session cards newer than the newest groom doc"*. Reading 329
cards to extract and classify them is exactly the shape that never got done
because it cost more attention than it was worth.

One run: 592k tokens, 4 batches, 22 distinct ideas, every one citation-verified
against the tree.

| Idea | Category | Card |
|---|---|---|
| Add measuring-seat git SHA and clone depth provenance to freeze sidecar artifacts | `bench-harness` | [`2026-07-20-s13-clone-depth-provenance.md`:30](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-20-s13-clone-depth-provenance.md#L30) |
| Automate executing pre- and post-session check --strict commands in run_ab.py to record exit codes directly in T5 benchmark run artifacts | `bench-harness` | [`2026-07-20-t5-headless-guard.md`:56](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-20-t5-headless-guard.md#L56) |
| Evaluate process rules by testing whether they fire actively at the keystroke where a mistake occurs rather than relying on memory | `docs-convention` | [`2026-08-03-verify-before-assert-rule.md`:52](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-08-03-verify-before-assert-rule.md#L52) |
| Explicitly define and name manual verification steps in process rules for claims that lack command-line verification tools | `docs-convention` | [`2026-08-03-owner-claims-are-asked.md`:46](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-08-03-owner-claims-are-asked.md#L46) |
| Require authoritative rule documents to include an explicit precedence yielding statement at the top | `docs-convention` | [`2026-08-03-precedence-live-instruction.md`:52](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-08-03-precedence-live-instruction.md#L52) |
| Add a bootstrap.py closeout --check command to verify handover document claims against current repository state | `engine-check` | [`2026-07-21-project-closeout.md`:26](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-21-project-closeout.md#L26) |
| Add a check_wall_families advisory to notify adopters when a repudiation fails to clear a false wall due to a capability-family mismatch | `engine-check` | [`2026-07-20-p2-p3-detector-hardenings.md`:67](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-20-p2-p3-detector-hardenings.md#L67) |
| Add a combinatorial property test to generate repudiation cue and wall trigger combinations over clause separators | `engine-check` | [`2026-07-21-false-wall-bare-conjunction-split.md`:35](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-21-false-wall-bare-conjunction-split.md#L35) |
| Add a corpus-replay test guard containing real adopter repudiation lines to validate false-wall clearing behavior against real fleet constructs | `engine-check` | [`2026-07-21-false-wall-quoted-wall-bridge-gate.md`:41](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-21-false-wall-quoted-wall-bridge-gate.md#L41) |
| Add a phantom-shipped-claim advisory to warn when heartbeat narrative entries claim a check or flag deliverable shipped that does not resolve in the tree | `engine-check` | [`2026-07-20-baton-freshness-advisory.md`:95](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-20-baton-freshness-advisory.md#L95) |
| Add an adopter-side advisory check_inline_date_suggest to print exact inline-date rewordings for section-dated wall findings | `engine-check` | [`2026-07-20-fix-false-wall-clearing-vocab.md`:99](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-20-fix-false-wall-clearing-vocab.md#L99) |
| Add an advisory check to flag owner-gated status flags in control/status.md that lack links to their open PRs | `engine-check` | [`2026-07-20-t5-doc-reconcile.md`:52](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-20-t5-doc-reconcile.md#L52) |
| Add an advisory check to warn when a document cites figures as settled that other documents mark as inferred or assumed | `engine-check` | [`2026-08-01-claim-provenance-pl014.md`:120](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-08-01-claim-provenance-pl014.md#L120) |
| Add an advisory check_wave_pending checker to cross-check open upgrade PRs in docs/adopters.md distribution wave sections against live registry tree cells | `engine-check` | [`2026-07-20-adopter-wave-v1.20.0.md`:83](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-20-adopter-wave-v1.20.0.md#L83) |
| Construct a shared lazily-cached TreeCorpus structure once per check run to amortize full-tree scans across content-scanning advisories | `engine-check` | [`2026-07-20-s17-recipe-discovery.md`:72](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-20-s17-recipe-discovery.md#L72) |
| Extend check --explain-wall to print the exact false-wall rule kind string required for check-exceptions.yml entries | `engine-check` | [`2026-07-21-false-wall-exemptions-v1.20.2.md`:41](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-21-false-wall-exemptions-v1.20.2.md#L41) |
| Refactor false-wall clearing paths into a single clears(cue, wall) scope-and-strength predicate function | `engine-check` | [`2026-07-21-false-wall-weak-cue-same-clause.md`:40](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-21-false-wall-weak-cue-same-clause.md#L40) |
| Suppress check_dateless_walls warnings on seed-wall summary rows if a matching dated append-log twin exists | `engine-check` | [`2026-07-20-s14-dateless-wall-advisory.md`:22](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-20-s14-dateless-wall-advisory.md#L22) |
| Add a --print-dispatch flag to cut_release to print the exact workflow dispatch invocation and SHA-equality check pinned to the bump commit at cut time | `release-process` | [`2026-07-20-release-v1.20.1.md`:46](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-20-release-v1.20.1.md#L46) |
| Assert that the header version of rebuilt dist/bootstrap.py matches the bump target during cut_release --rebuild-dist | `release-process` | [`2026-07-20-s15-cut-release-rebuild-dist.md`:27](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-20-s15-cut-release-rebuild-dist.md#L27) |
| Pin release dispatches to the exact bump commit SHA or add a preflight check so release tags do not land on doc-aftermath commits | `release-process` | [`2026-07-20-cut-release-v1.20.0.md`:33](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-07-20-cut-release-v1.20.0.md#L33) |
| Include a harness-supplied static capability roster in working templates so providers receive an empirical self-description of environment abilities | `skill-or-prompt` | [`2026-08-04-idea-capability-roster.md`:7](https://github.com/menno420/substrate-kit/blob/main/.sessions/2026-08-04-idea-capability-roster.md#L7) |
**This is groom INPUT, not a groom.** Nothing here is routed into the backlog,
deduped against `docs/ideas/`, or sized. That is the kit-side pass this unblocks.

## A third reject shape, and a path the free-tier caveat does not cover

Measured 2026-08-05, two runs on the superbot / superbot-next card corpora
(1,843,098 and 641,442 input tokens; 82 findings verified, 6 rejected):

**Every one of the 6 rejects carried no citation at all** — `file`, `line` and
`quote` all absent, not a mismatched or reconstructed quote. That is a third
shape alongside the marker mismatch (93%+ coverage) and the fabrication
(59–70%) recorded above, and it is the benign one: the verifier drops a
citationless claim without needing a coverage judgement at all.

It is also weak evidence on the open question below. The short-quote rule was
in force for both runs, and **no fabrication appeared** — but neither did a
marker mismatch, so the runs cannot separate "short quotes prevent
reconstruction" from "this task shape produced no reconstruction". n is still
too small; the rule stays unmeasured.

**These runs went through Vertex, not the free tier.** The training-data
caveat below applies to free-tier AI Studio submissions; the Vertex path is
governed by the Cloud terms attached to the owner's billing account. That is
why two public bot repositories could be delegated without the public-repo
rule being the binding constraint — the rule still holds for the free key.
Recipe: [`../conventions/vertex-first-for-gemini.md`](../conventions/vertex-first-for-gemini.md).

## What is not established

- **One job class has run.** Bench-evidence summarisation and provenance sweeps
  are proposed, not proven.
- **The short-quote rule is unmeasured.** Capping quotes at 200 characters was
  meant to reduce reconstruction; in the rerun every reject was a marker
  mismatch instead, so the rule's actual effect on fabrication is unknown.
- **Cross-run dedupe does not work by string key.** Two runs over the same
  corpus produced 20 and 22 findings phrased differently; naive merging reported
  42 "unique" ideas, which is wrong. Each run is self-consistent; comparing runs
  needs a human or a second pass.
- **Free-tier submissions may be used for training** (see
  [`../providers/gemini.md`](../providers/gemini.md)). Public repos only —
  `shiftlife` is private and stays out unless the owner decides otherwise.
