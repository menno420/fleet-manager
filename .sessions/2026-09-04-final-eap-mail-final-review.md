# 2026-09-04 — the final EAP mail: one final review, the owner Q&A, and what his answers changed

> **Status:** `in-progress` — **what is about to happen:** one cold read of
> the sendable mail as an Anthropic recipient (Part 1, the COPY block, and the
> Gmail delivery copy read back), a compact assessment to the owner instead
> of a review ledger, a Q&A workspace placed in the draft **outside the COPY
> markers** for him to answer in his own words, then his answers folded in
> where they belong, the figure consumers moved by the checker in the same
> pass, and one final recipient-view read of the rendered mail. Nothing
> sends; the Gmail draft is not restaged while a placeholder is unanswered.

- **📊 Model:** withheld · xhigh · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_017KJ3ipHJVQ9vFCWi8tNz5i](https://claude.ai/code/session_017KJ3ipHJVQ9vFCWi8tNz5i) · "Final EAP email review"

**What this session is about:** program step **E1**, the owner's final EAP
review mail — its last review pass before he sends. Working file:
`docs/planning/2026-08-24-final-eap-email-draft.md`. The owner's brief for
the pass: a strong presumption for the existing mail, small high-leverage
edits over rewrites, his voice over polished prose, a Q&A he answers himself,
and no send from any session.

## State at start (verified at HEAD, 2026-09-04)

- `main` at `69e1a71` (#1035); the draft's last change is fm #1019
  (`caa6cd2`), the owner-edits rewrite of 2026-09-03 evening.
- `python3 tools/render_eap_mail.py --count` → 2299 words in the mail;
  `--verify` loss-free (2299 → 2299); `python3 tools/check_eap_figures.py`
  → 17 pinned locations, 0 drift, 0 problems, liveness probe fired. All exit
  0, read directly.
- Gmail draft `r-9208017789511753451` read back (`get_draft`, MINIMAL then
  PLAIN_TEXT): `labelIds ["DRAFT"]`, message id `1a0693ba429cd37e`, dated
  2026-09-03T21:45:11Z, subject *"Claude Code Projects EAP — the final
  review, six weeks on"*, no recipients. Part 1 and Part 2 in it read as the
  repo's text at fm #1019 — a read-through, not a word diff.
- Every URL in the COPY block answers HTTP 200 over direct egress (13 of 13,
  the four review-site pages included).
- The 18 August async study invitation is in the mailbox (subject *"20
  minutes on how you'd describe Projects"*, bcc to participants); whether he
  did it is not on the record — it is one of the Q&A questions.
- The full-read audit's "98 of 101 closed" is the 2026-08-11 sweep figure
  (`docs/audits/2026-08-10-full-read/findings.md:144`).

## What was done

*(filled at close)*
