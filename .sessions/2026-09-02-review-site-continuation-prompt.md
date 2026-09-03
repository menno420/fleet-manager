# 2026-09-02 — records only: the continuation prompt for the review-site session

> **Status:** `in-progress` — born red. A records-only follow-up to the
> review sitting (fm #1013, merged `015c292`), at the owner's ask after that
> PR landed: the continuation prompt for the session that improves the
> program-review site for Anthropic. Flips `complete` as the last commit.

- **📊 Model:** fable-5 · xhigh · review/verify
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01DSyapUpawGhaW1vThaQEvJ](https://claude.ai/code/session_01DSyapUpawGhaW1vThaQEvJ) · "Fleet manager 2026-09-02 review"

## Mission

Owner, live, after fm #1013 merged: *"Use the continuation prompt skills so
the next session can work on the review website for Anthropic. I want to
make sure that thos website is easy to navigate and explains everything
properly. Preferably with some examples of how we want things to look. I
will see if I can find some example screenshots later, but for now it
should just try to create it based on the descriptions we have."*

**Why a second PR from one session (D-0024 exception, stated):** the
sitting's PR had merged and the card flipped when he asked; a records-only
PR at the owner's ask is one of the five named reasons.

## What is about to happen

`prompt-preflight` at HEAD (the live Pages site fetched over direct egress,
the review app's README, the export losses decision, the exporter's usage,
the deploy trap, the websites repo's own conventions), then the prompt at
`docs/prompts/2026-09-02-review-site-session.md`, listed in
`docs/prompts/README.md`; his words appended to the owner-direction record's
§ 6; one sentence beside the program's NOW pointer.

## Verify

`python3 bootstrap.py check --strict` — exit 1 with only the born-red hold
before the flip, exit 0 after. `python3 scripts/check_docs_links.py` —
CLEAN. `python3 tools/gen_owner_index.py --check` — exit 0.

⚑ decide-and-flag: none — the prompt carries his open choices as its
first question.

💡 Session idea: none new.

⟲ Previous-session review: the same session's main PR (fm #1013) — three
Codex rounds found 22 real findings in the sitting's records, most of them
consistency drift between entries amended in the same PR; the one-place-
per-fact checker shaped in that card would have caught about half.

Layer-2 handoff: null (fleet-manager itself; websites read over the API,
not attached — the receiving session attaches it).
