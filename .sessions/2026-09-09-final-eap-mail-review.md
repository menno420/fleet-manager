# 2026-09-09 — the final EAP mail found and read again: where it is, what still needs his call

> **Status:** `in-progress` — the owner asked for the latest mail draft to be
> found and reviewed (*"I should have sent it a few days ago but I didn't really
> have the time to properly read this final version yet. Now I'm also unable to
> find it."*). What is about to happen: locate the draft in the repo and in his
> mailbox, verify the two agree, read both parts against their sources and
> against what the estate has measured since 2026-09-03, and hand back the
> findings as one-word calls — **nothing in the mail is edited and nothing is
> sent**; he said on 2026-09-03 he reads it again himself first.

- **📊 Model:** withheld · max · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01PrzQkc44A9Q3JyA94rnX1n](https://claude.ai/code/session_01PrzQkc44A9Q3JyA94rnX1n) · "Email draft review"

## What this session is about

Program step **E1** is NOW and is his: the mail was drafted in full and staged
as a Gmail draft on 2026-09-03 (fm #1017, rewritten in fm #1019). Six days
later he could not find it. This card records where it is, the word-for-word
comparison of the mailbox copy against the repo, the review findings, and the
calls that are his — as a records-only PR (no Codex round, [D-0019] as
amended 2026-09-02; the flip rests on the direct checks named below).

## State at start (verified at HEAD, 2026-09-09)

- `origin/main` at `3e1904d` (#1045). The draft file's last change is fm #1019
  (`caa6cd2`, 2026-09-03) and nothing has touched it since — `git log` on the
  file; the clone is shallow, but the file's own history in it reaches back to
  2026-08-31, before that change, so the sample covers the claim.
- `python3 tools/render_eap_mail.py --count` → **2299**; `--verify` →
  loss-free (2299 → 2299); `python3 tools/check_eap_figures.py` → 17
  occurrences across 5 files, 0 problems, liveness probe fired. Exit codes
  read directly, not after a pipe: 0 · 0 · 0.
- Orientation: targeted for the task, **not the full six reads** — README
  § Mandatory reading order, `docs/intent.md` § 6, `docs/current-state.md`'s
  E1 lines, the program's NOW pointer (E1 — his), the fresh-start redirect
  header, the owner-queue E1 entry, both 2026-09-03 cards. Stated from that:
  this repo is the estate's router and records home, becoming the read-only
  archive ([D-0025]); the era is post-close, regular sessions only; the owner
  is finishing E1, the final EAP review mail; the next step is his — read it,
  answer the calls, add the recipients, send.

## What was done

- **Found — in two places, and they agree.** Repo:
  `docs/planning/2026-08-24-final-eap-email-draft.md` — Part 1 (696 words,
  his own after fm #1019) sits above the COPY markers, Part 2 (2,299 words)
  between them. Mailbox: Gmail → Drafts → *"Claude Code Projects EAP — the
  final review, six weeks on"*, draft id `r-9208017789511753451`, message id
  `1a0693ba429cd37e`, dated 2026-09-03T21:45:11Z, `labelIds ["DRAFT"]`, no
  To/Cc/Bcc (read from the `RAW` headers). The card of fm #1019 recorded the
  restage's message id as `1a0691cd821da775`; the stored one is later and
  carries the round-1 sentence (*"the paste into each Project, and the
  re-paste after a reset, was the owner's"*), so the mailbox holds the
  reviewed head's text. A second draft in the same folder is the 2026-07-22
  coordinator note to the vendor about the shutdown not taking effect —
  addressed, starred, never sent; not this mail, and worth his glance.
- **Compared, word for word.** The draft read back `RAW`, MIME-decoded
  (`multipart/alternative`; plain part 19,270 chars, HTML part 21,428):
  Part 1 == the file's Part 1 section, Part 2 == `render_eap_mail.py`'s plain
  output — both whitespace-normalised, `difflib` — with **exactly one class of
  difference: every URL.**
- **The finding: the staged draft's 13 links are stored as Google
  redirects.** Every `href` in the stored HTML, and the same URLs in the
  stored plain part, read
  `https://www.google.com/url?q=<url>&source=gmail&ust=<draft date + 24 h, µs>&sa=E`;
  the nine bare `github.com/…` links were auto-linked as `http://`. To tell
  the write path from a display artifact: `create_draft` with a one-line body
  and one `https://` anchor → read back `RAW` → wrapped identically in both
  parts, `Received: … by gmailapi.google.com with HTTPREST` → `trash_message`
  → `{}`. What a recipient hits: `curl` on the draft's first GitHub href →
  `HTTP 200`, no `Location`, body *"Redirect Notice — The previous page is
  sending you to …"*. Recorded as a dated line in `docs/CAPABILITIES.md`, and
  the draft's § 1 sentence *"what is unverified is now his half only"* is
  retracted there with the measurement — the text was right, the links were
  not, and the 2026-09-03 read-back (`MINIMAL`, a snippet) could not have
  seen it.
- **Read against sources.** Every local link target exists (seven files);
  the review site's four pages answer 200 and `#projects-overview-mockup` is
  present on `/examples/`; superbot's July findings document and
  superbot-games PR 16 exist and both repositories are public (direct API,
  `private: false`); *"98 are closed"* is the audit's own sweep line
  (`docs/audits/2026-08-10-full-read/findings.md:144`); the arithmetic holds
  (19 + 1 + 7 = 27; 5 + 4 + 3 + 2 + 2 = 16; 14 of 16 "at a moment"); the July
  thread's headers hold the EAP alias in To and three cc addresses (his two
  2026-07-16 sent mails) — named to him in chat, not copied here.
- **The one substantive content finding.** Part 1: *"superbot-next is the
  example: … and the code itself was not faulty."* The estate measured
  otherwise the day after he wrote it —
  `docs/planning/2026-09-04-superbot-rebuild/run/boot-observation.md` § 5.5
  (two unhandled exceptions behind ordinary buttons: `setup_panel.py:159/:191`
  reading `result.ok` on a `WorkflowResult` → *"Something went wrong on our
  end"*; `guild_snapshot.py:243` → an exception logged on every setup
  recommender read), § 5.2 (`/setup` renders its first card and never sends
  it), § 5.4 (three of ten setup commands cannot work from slash). Part 2's
  Finding 1 explicitly makes no claim about code quality either way, so his
  half carries the mail's only code-quality claim and the record contradicts
  it. His sentence; put to him as *keep* / *"and the code ran"* / *drop the
  clause* — not applied.
- **The rest, as one-word calls** in the draft's § 2 (▶ 2026-09-09): *links*
  (send as staged, or paste the clean document into a fresh compose) ·
  *scheme* (the nine GitHub links carry no `https://`, so the renderer's HTML
  has them as text, not anchors) · *weeks* (the subject's "six weeks on" is
  seven weeks today: 50 days) · *fixed* (Finding 3's closing *"is fixed"* reads
  as "was repaired") · *twice* (the documentation ask appears in Part 1 and
  again as the addendum's last clause) · *recipients* (none on the draft).
- **Handed to him:** the combined document — Part 1 + `<hr>` + Part 2 built
  from the renderer's own `to_html`/`to_text` (4 anchors, 0 wrappers,
  `HTMLParser` clean; its Part 1 plain text == the staged Part 1) — through
  the session's file channel, so the clean-link paste is one open-select-copy
  away. It is not committed: a second copy of the mail in the repo is the
  drift the mail itself reports.
- **Not done, deliberately:** no edit to Part 1 or Part 2; no recipients
  added; nothing sent; no renderer change (the *scheme* call is his); no
  Codex round.
- Layer-2 handoff: null (fleet-manager itself; superbot and superbot-games
  were read only as public link targets over the direct API)

## 💡 Session idea

**A staging step that reads back what it STORED, not a snippet of what it
sent.** The 2026-09-03 restage read the draft back as `MINIMAL` and recorded
*"the body in Gmail is the reviewed head's text"* — true of every word and
false of every link, and nothing in that read could have said so. The check
is twenty lines: after any `update_draft`, fetch `RAW`, decode the parts, diff
the plain part against the renderer's output and count `google.com/url` in the
HTML; a non-zero count fails the staging. It generalises to every "sent it /
staged it / published it" claim in this estate: the surface that matters is
the stored artifact, and a snippet is a label read as substance (TRAP-008).
Deduped against `docs/owner-queue.md` and the 2026-09-0x idea slots: not
there.

## ⟲ Previous-session review

`.sessions/2026-09-03-final-eap-mail-rewrite-after-reviews.md` (fm #1019) did
the hard part right: his edits kept in his words, the reviewer's findings
folded in with dispositions, two Codex rounds to a clean verdict, the draft
restaged from the final text — the mailbox copy is the reviewed head's text,
verified here word for word. Its miss is the one this card's idea names: it
read the draft back as a snippet and wrote *"his half only"* into § 1 as
what remained unverified, a stronger sentence than its own read-back
supported; the links were wrapped from the first restage on and six days
passed with the record saying the opposite. The lesson is the estate's own
TRAP-001 in miniature — a read-back that returns a label is not a measurement
of the artifact.

## Verify

*(the commands and their tails, written at the flip)*

## Close-out

*(filled at the flip)*
