# Provider capability references

> **Status:** `living-ledger`
>
> One document per AI provider, so a session can find out what a provider's
> surfaces can do without re-deriving it. Dated facts with sources; re-verify
> anything you build on — these platforms move faster than any doc.

## Read this first — none of these is a routing table

**These documents describe what each provider *can do*. They assign no roles and
say nothing about who should do what.**

If you are a session reading one: **do the work you were asked to do.** Nothing
here licenses declining a task. The purpose is narrower and more useful — telling
*"this surface works differently, use the other path"* apart from *"this is
impossible"*, which is the confusion that repeatedly costs the owner a turn.

## The documents

The set covers capabilities at **model granularity** where models differ —
context, modality in and out, tool use, reasoning modes — because that is where
the answers a session actually needs live. Ordered by plausible use in this
estate:

| Provider | Covers |
|---|---|
| [`claude.md`](claude.md) | Model family and IDs re-derived from Anthropic's own changelog, the surfaces (Code on web/CLI/desktop, claude.ai, API), what a Code session can actually do here, and the estate-specific quirks that have produced false walls |
| [`chatgpt.md`](chatgpt.md) | The GPT-5.6 family at model granularity, the post-consolidation modes, Projects and custom GPTs, and the **Work / Codex cloud environment** with its variables, secrets and network defaults |
| [`gemini.md`](gemini.md) | Plans and what actually differs between them, context-window ceilings, native video and the token arithmetic that governs it, Gems and knowledge files, Deep Research |
| [`github-copilot.md`](github-copilot.md) | The multi-provider model picker, the cloud agent and its Actions environment (firewall, secrets-reach-the-agent), AI-credits billing — the provider the estate touches without choosing it |
| [`grok.md`](grok.md) | xAI's text models and reasoning knobs, the image/video/voice generation stack, X Search, and the silent-redirect retirement scheme |
| [`deepseek.md`](deepseek.md) | The V4 pair, thinking modes, MIT open weights, and the pricing (including peak-hour) that makes it the cost floor of this set |
| [`mistral.md`](mistral.md) | The per-model license mix (Apache/MIT/Premier/NC) that governs self-hosting, the specialist bench (OCR, Voxtral audio), and Vibe |
| [`meta-llama.md`](meta-llama.md) | The open-weights Llama generations and their Community License, and the 2026 pivot to Muse that froze the open line at Llama 4 |

## How these relate to the other docs

- [`../execution-surfaces.md`](../execution-surfaces.md) — the **comparison**: the
  handful of rows that change how a prompt must be written. Start there when
  writing a prompt; come here when you need depth on one provider.
- [`../CAPABILITIES.md`](../CAPABILITIES.md) — the **evidence log**: dated,
  venue-scoped findings with the exact error text and the workaround. When
  something here turns out to be wrong, correct it here and append the
  measurement there.
- [`../SKILLS-local.md`](../SKILLS-local.md) — the prompt/handoff skills that
  consume all of the above rather than restating them.

## Weakness is not limitation

The owner's distinction, and it governs every entry here. **A weakness is "worse
at this than the alternative"; a limitation is "cannot."** Almost nothing in this
estate is genuinely the second.

Claude generating images is the worked example: weak-to-absent in chat, and that
is a *weakness* — it says nothing about whether the outcome is reachable. Reading
video was written down here as impossible once, and ffmpeg frame extraction
retired it in an afternoon.

So an entry that says "X is weak at Y" is a **steer**, never a stop. If a session
reads one of these files and declines a task on the strength of it, the file has
failed at its job.

## Keeping them honest

Four rules, three of them learned the expensive way and the fourth learned by
getting it wrong in the first version of these very documents:

1. **Cite or mark.** Every claim is either sourced to a vendor page, measured
   here, or explicitly labelled as inference. A confident unsourced specific is
   the failure mode these documents exist to prevent.
2. **Name the precondition.** A recipe that depends on a variable, a binary or a
   plan tier says so, with the check that confirms it — otherwise a reader whose
   setup differs concludes they are blocked rather than that they need a
   different line.
3. **A provider's own account of itself is training data, not telemetry.** Every
   one of these models will describe its own tiers and limits confidently and
   sometimes wrongly, because the answer changed after it was trained and nothing
   told it. Read the vendor's page.
4. **Changelog first; aggregators never, for anything volatile.** The first
   version of these documents was assembled from a handful of searches that
   surfaced mostly secondary sites, and it went wrong in exactly the places you
   would predict: a mode taxonomy that a July 2026 consolidation had already
   retired, and a Drive integration filed as a weakness when it is one of the
   provider's strengths. **Product surfaces, mode lists and plan contents are the
   fastest-moving facts on these platforms and the ones aggregators get most
   wrong.** Start at the vendor's release notes — `gemini.google/release-notes/`,
   `learn.chatgpt.com/docs`, the Claude docs changelog — and only then fill gaps,
   marking what came from where.
