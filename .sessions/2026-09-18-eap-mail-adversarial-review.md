# 2026-09-18 — one more adversarial review of the final EAP mail before he sends it

> **Status:** `in-progress` — reconfirming the Gmail draft against the
> committed text and re-verifying claims against their cited sources, one
> more pass before he reads it. Nothing edited yet; see close-out for the
> verdict.

- **📊 Model:** withheld · xhigh · review/verify
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_015fb1NcYcoMwoZtxufgScZ9](https://claude.ai/code/session_015fb1NcYcoMwoZtxufgScZ9) · "EAP mail final adversarial review"

## What this session is about

Program step **E1**, owner-directed continuation: one more adversarial pass
on the final EAP mail before he reads it — verify every claim against its
cited source, resolve the one open call in Part 1 (`your-question`), and
reconfirm the Gmail draft still matches the committed text byte-for-byte.

## State at start (verified at HEAD, 2026-09-18)

- `origin/main` at `4b7aa00` (#1048). Nothing open or in flight; this
  session's branch (`claude/practical-einstein-4vejc4`) was already at the
  same commit, so no merged-branch restart was needed.
- `python3 tools/render_eap_mail.py --count` → **2286**; `--verify` →
  loss-free (2286 → 2286); `python3 tools/check_eap_figures.py` → 17
  occurrences across 5 files, 0 problems, liveness probe fired on the
  corrupted-copy fixture.

## What was done

- **The draft reconfirmed against the committed text — every difference
  is a Google link wrapper and nothing else.** Fetched the Gmail draft
  (`r-9208017789511753451`) as `RAW`, MIME-decoded both parts. Built the
  same combined document the mail is: Part 1 (the file's own `Hi
  everyone,` … `Menno van Hattum` block) rendered through
  `render_eap_mail.py`'s `to_text`/`to_html`, plus Part 2 via `extract()`
  + the same functions.
  - **Plain part:** word-level diff (`difflib`, both sides tokenized the
    same way `--verify` does) — **3,012 words on each side, 12 replace
    hunks, all 13 links** (one hunk carries two adjacent link tokens),
    every one a `https://www.google.com/url?q=…&source=gmail&ust=…&sa=E`
    wrapper around the correct target. No dropped or added words outside
    those hunks.
  - **HTML part:** all 13 `href` values individually extracted and
    checked — same wrapper, same 13 correct targets underneath (including
    the bare `github.com/…` links auto-linked as `http://` by Gmail's
    write path, matching the *scheme* finding already on record).
  - Subject (`Claude Code Projects EAP — the final review`) and
    recipients (none) confirmed from the decoded headers.
  - This reconfirms the 2026-09-09/2026-09-17 finding still holds after
    the 2026-09-17 restage: the stored draft is the reviewed head's text,
    link-wrapping aside.
- **Claims re-verified against their cited sources, not against a summary
  of them** (the TRAP-008 lesson from the last two passes). Opened the
  actual file at the actual line for each, rather than trusting a prior
  session's characterization:
  - `docs/audits/2026-08-10-full-read/findings.md:144` — *"98 of 101
    entries closed"* — matches Finding 2's 101/98.
  - `docs/findings/2026-08-08-why-rules-dont-bind.md:74-75,88` — 116
    statements across 66 files; `§ 2`'s catcher table (owner 5, Stop-hook
    4, local gate 1, CI/GitHub 2, own test runs 2, after-the-fact 2 — the
    116/0 row) sums to Finding 3's 5+4+3+2+2=16 exactly (mail's "gate and
    CI together (3)" = source's local-gate-1 + CI/GitHub-2).
  - `docs/eap-retrospective.md:65-69` — the 999-test/998-passed-1-skipped
    claim and the 21-of-21-zero-fabrication claim, both verbatim.
  - `docs/CAPABILITIES.md:689-706` — the 335-second Codex review time and
    the 13-findings-over-5-rounds figure, both verbatim.
  - `docs/findings/night-review-2026-07-10.md` Q7 (:330-345, the 73-of-121
    test-collection gap), Q16 (:694-696, :715-716, the "no exceptions"
    PRIVATE repo publicly readable + all 13 account repos public that
    night).
  - `docs/fleet-inconsistencies-2026-07-13.md` INC-04 (:78, the
    integration-enabled/quota-capped conflation) and INC-43 (:147, the
    3-of-3 fabricated-review suspension) — both back the addendum's
    remaining two false-done examples.
  - `docs/findings/2026-08-24-e1-source-sweep.md:226-229` — the
    67-doc-routes/61-the-day-before figure, correctly dated in the mail
    the same way every other moving count in it is dated.
  - `docs/eap-retrospective.md:80-82` — 767 of 949 superbot session cards
    carry the review section = 80.8%, which is what the addendum's
    "about 81 %" rounds from.
  - Part 1's own word count, recomputed independently with the renderer's
    counting method on just the Part-1 block: **726**, matching the
    status line and `docs/owner-queue.md`.
  - **No discrepancy found in any of the above.** Nothing in Part 1 or
    Part 2 needed a correction this pass.
- **The `your-question` open call (draft § 2, raised by Codex round 2 on
  fm #1047) — re-read, still correctly framed, not resolved by editing.**
  Part 1's *"to answer your question about what would make me choose a
  Project over a session"* is his sentence, and the record
  (`docs/findings/2026-09-02-owner-direction.md`:230-236) establishes only
  his recollection that Anthropic asked it, not that these recipients did
  — the same asymmetry the draft already documents accurately as *keep*
  / *"a question I was asked"* / *"the question I remember being asked"*.
  This is his call under the same reservation as his sentences generally;
  the session does not pick for him. Put to him in chat, not applied here.
- **`docs/owner-queue.md` and `docs/current-state.md` checked against the
  draft — already consistent** (726/2,286/474 word figures agree across
  all three; the queue's WHAT line still correctly scopes his remaining
  choices to the links route, recipients and send). No edit needed.
- **Not done, deliberately:** no edit to Part 1 or Part 2; no recipients
  added; nothing sent; the `your-question` call not picked for him; no
  Codex round (records-only — nothing changed for a reviewer to see).
- Layer-2 handoff: null (fleet-manager itself; no other repo attached)

## 💡 Session idea

**The byte-diff check this session ran by hand belongs in the render
tool, not in a session's ad-hoc script.** Three sessions running now
(2026-09-09, 2026-09-17, this one) have each independently written the
same ~30-line RAW-fetch/MIME-decode/word-diff routine to answer "does the
staged draft still match the committed text." The 2026-09-17 card already
named this as a session idea; this session is the third rediscovery of
the same gap. Worth shipping as `render_eap_mail.py --check-draft
<draft-id>` (or similar) so "reconfirm the draft" is one command instead
of a rebuilt script — not done here, since it touches the renderer and
this pass is deliberately records-only.

## ⟲ Previous-session review

`.sessions/2026-09-17-eap-mail-owner-edits.md` (fm #1047, flip corrected
by fm #1048) applied the owner's six edits cleanly and caught its own
near-miss before it shipped — a replacement citing the 533/533 parity
figure from a doc-route summary rather than the file, withdrawn once the
file was actually opened. Its miss, corrected the same day: the
self-critical tally counted the owner's own `not-faulty` sentence (fm
#1019, his words) as a session's defect instance, inflating "second" to
"third." This session found nothing to add to either record — both
corrections held under a fresh, independent check against the same
sources.

## Verify

- `python3 tools/render_eap_mail.py --count` → exit **0** — `2286 WORDS
  IN THE MAIL`.
- `python3 tools/render_eap_mail.py --verify` → exit **0** — `source
  words 2286 -> rendered words 2286` · loss-free.
- `python3 tools/check_eap_figures.py` → exit **0** — `[inventory] 17
  pinned location(s); drift: 0` · `[all consumers] 17 occurrence(s)
  checked across 5 file(s); problems: 0` · liveness probe fired on the
  corrupted-copy fixture as designed.
- Draft vs. combined document (`RAW` → MIME-decoded → tokenized
  `difflib`): plain part 3,012/3,012 words, 12 hunks, all Google
  `url?q=` wrappers; HTML part 13/13 `href`s wrapped identically over the
  correct targets. Subject and recipients read from the decoded headers,
  unchanged.
