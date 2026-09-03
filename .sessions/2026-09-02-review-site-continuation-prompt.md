# 2026-09-02 — records only: the continuation prompt for the review-site session

> **Status:** `complete` — the review-site session's continuation prompt
> landed at `docs/prompts/2026-09-02-review-site-session.md`, listed in the
> prompts README, his words in the owner-direction record's § 6, the order
> against E1 recorded as unsettled beside the NOW pointer, and the three
> front doors pointing at the one live-prompt list. Codex: three rounds, the
> cap — 6 + 3 + 3 findings, all real, all fixed; round three's fixes
> verified directly, no fourth round. **Reviewed SHA `43b574c` (round 3).
> After it:** the round-three fix commit (verified by the link, false-walls
> and owner-index checks and the strict gate) and this flip commit. Landed
> on green.

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

## Codex — three rounds, the cap, on a 229-line prompt (tier 2 of the review-cadence entry)

- **Round 1 (`f03128a`): 6 findings, 1 P1 + 5 P2, all real, all fixed.** The
  P1 was the stamp gate: the prompt cited websites' own decision ids and
  the checker counts any id under `docs/` (fixed before the round answered
  — the session ran the gate after the request, the wrong order, and the
  gate said what Codex then said). P2s: screenshots made conditional ("see
  if"), the cold read widened to every dynamic route family, added hrefs
  must resolve under `_site` rather than grep, the mail/site ordering
  recorded as UNSETTLED in both prompts and the NOW block instead of the
  session's invented "parallel", and the clone path branches on the PAT
  per the 2026-08-21 ledger entry.
- **Round 2 (`c454c7b`): 3 findings, all P2, all real, all fixed.** The
  REJECTED bullet still promised screenshots (made conditional); the
  cutover dated 20/21 August per the Layer 2 entry; the mail prompt's
  DONE WHEN now requires the review-site link (the draft carries none).
- **Round 3 (`43b574c`), the last: `round 3: 3 findings — 3 fixed, 0
  refuted, 0 open`,** verified directly, no fourth round. The ordering
  question moved out of the no-question restate block into the first
  message after it (both prompts); the cold site read moved AHEAD of the
  site's README so the reviewer's-eye critique is not pre-informed; and the
  three front doors that enumerated the live prompt exceptions — the root
  README, `docs/MAP.md`, the boot file — now point at `docs/prompts/README.md`
  as the one list (each had fallen a file behind; the boot file line is the
  one edit in this PR that is not a record, disclosed here). Verification
  after the fixes: the link checker, the false-walls checker, the
  owner-index check and the strict gate (born-red hold only, zero stamp
  findings) — the direct checks the cap's exit names.

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
