---
name: delegate-read
description: "Hand a read-heavy job to Gemini instead of burning session context on it — reading every session card, every bench result, every doc in a tree — and get back claims that are citation-verified against the repo before you read them. Use when a task means reading more of a corpus than fits comfortably in context, or when a sweep keeps not happening because it costs too much attention."
---

# delegate-read

The estate has jobs that never get done because they cost more attention than
they are worth: read all 329 session cards, read 391 bench results, find every
claim in the docs that states a number without its instrument. A free
`GEMINI_API_KEY` reads a 592k-token corpus in about five minutes for $0, which
changes what is worth attempting.

What it does NOT change is who is accountable for the answer.

## The one rule

**Delegate the reading, never the record.**

Measured 2026-08-05: asked to build a dashboard over substrate-kit, Gemini
produced 18 fluent, plausible "decisions" while the real `docs/decisions.md`
(10 entries) sat unread in its own workspace, reported 142 sessions against 329
real cards, and asserted a validation that never ran. Nothing about the output
looked wrong.

So every delegated claim comes back with **file + line + verbatim quote**, and
those quotes are checked mechanically against the tree before anyone reads the
finding. Review becomes a string comparison instead of a judgement call. That
is the whole reason this is safe.

## When this runs

- A task means reading a whole corpus — every card, every result file, every
  doc under a tree — and only conclusions are needed back.
- A sweep has been deferred repeatedly because of its size.
- Anything where the output is **extraction** (find, list, classify, locate),
  not **decision** (choose, design, rule).

## When it does NOT run

- **Anything that writes a record.** Rulings, session cards, docs, code. The
  delegate finds; this session decides and writes.
- **Private repos.** Free-tier submissions may be used for training
  (`docs/providers/gemini.md`). Public repos only unless the owner says
  otherwise — `shiftlife` is private.
- **Small reads.** Under ~50k tokens, read it here; the round trip costs more
  than it saves.

## The method

1. **Scope the corpus and measure it first.**
   ```bash
   python3 tools/gemini_delegate.py bundle --repo <path> --glob '.sessions/*.md'
   ```
   Prints files, chars, and the exact token count. Above ~250k tokens the run
   chunks automatically (the free tier meters input at 250k/minute — the
   model's 1M window is a different number from the quota).

2. **Write the task file as an extraction spec, not a question.** Name the
   output shape, the categories, and what to skip. State that an empty result
   is a correct answer — otherwise a model with nothing to report invents
   something to report.

3. **Run it.**
   ```bash
   python3 tools/gemini_delegate.py run --repo <path> --glob '<pattern>' \
       --task-file <task.md> -o <out.json>
   ```
   Output: `verified N · rejected M`. The tool bundles, calls, and verifies.

4. **Read the rejects before the findings.** A reject is not noise — it is the
   most informative line in the run. Two shapes, and they mean opposite things:
   - *low coverage* (under ~70%) — the quote was reconstructed. The finding may
     still be real, but its evidence is not; re-check it by hand or drop it.
   - *high coverage* (90%+) — a formatting or marker mismatch. The evidence is
     real; the verifier is being strict.

5. **Verify anything load-bearing yourself.** The verifier proves the quote
   exists. It does not prove the *claim* follows from the quote — that judgement
   never leaves this session.

6. **Re-verify later runs against the current tree** when acting on an older
   report: `verify <out.json>` re-checks every citation, which is how a finding
   that went stale gets caught.

## Traps

- **The window is not the quota.** 1M tokens of context, 250k tokens per minute
  of free input. Chunking is not optional above that.
- **Long quotes get rewritten.** Both fabrications measured so far were 699 and
  1,392 characters, each stitching real fragments into a passage that appears
  nowhere. Short quotes were copied.
- **Cross-run dedupe by string key does not work.** Two runs over the same
  corpus phrase the same idea differently; naive merging inflated 22 findings to
  42. Compare runs by hand or with a second pass.
- **A verified citation is not a verified conclusion.** The most dangerous
  output is a true quote supporting a claim it does not actually support.
- **Do not paste the delegate's prose into a repo doc.** Its sentences are
  drafting material; the record is written here, in this estate's voice, by the
  session that is accountable for it.
