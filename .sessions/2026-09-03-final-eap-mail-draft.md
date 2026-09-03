# 2026-09-03 — the final EAP mail, drafted for the owner to read, edit and send

> **Status:** `complete` — program step **E1**'s draft, both parts, built
> from the night fleet's evidence report and the owner's 2026-09-02 answers
> under Shape A, staged as a Gmail draft in his own mailbox with no recipients.
> He reads, rewrites Part 1, answers the one-word calls, adds the recipients and
> sends; this session never does. Codex: three rounds, the cap — 4 + 5 + 3
> findings, all real, all fixed; round three's fixes verified directly (the
> cap's exit), no fourth round. **Reviewed SHA `4d90d43` (round 3). After it:**
> `815a0b9` (the round-three fixes, verified by the figure checker, `--verify`,
> preflight and the strict gate) and this flip commit — the one exempt commit,
> a badge flip plus close-out text. Landed on green.

- **📊 Model:** withheld · xhigh · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01FYmmtAxtUAuXyAhWpejVYK](https://claude.ai/code/session_01FYmmtAxtUAuXyAhWpejVYK) · "Final EAP mail draft"

**What this session is about:** executing
`docs/prompts/2026-09-02-eap-mail-session.md` — Shape A (owner, 2026-09-02):
Part 2 stays at its verified length plus one addendum of at most ~450 words
framed as the Projects-versus-sessions answer, the false-done ledger in as the
evidence that verification is the deciding line, both required one-clause
patches applied, and Part 1 drafted from the beat table and his § 5d opinions
as a proposal he rewrites in his own voice. Working file:
`docs/planning/2026-08-24-final-eap-email-draft.md`.

## State at start (verified at HEAD, 2026-09-03)

- `origin/main` at `a65fcfd` (#1016). fm #1013 (the review sitting) merged
  2026-09-02T22:04:44Z; fm #1016 (the review-site pass) merged
  2026-09-03T10:51:05Z — the site pass LANDED before this session, so the
  "site before mail" order question is moot, and the pages the addendum links
  are live (checked over direct egress: `/`, `/story/`, `/examples/`, `/after/`,
  `/problems/`, `/process/` all HTTP 200; anchors `#projects-overview-mockup`,
  `#coordinator-authority`, `#false-done`, `#stall-visibility` present).
- `python3 tools/render_eap_mail.py --count` → 1686 words in the mail; `--verify`
  → loss-free (1686 → 1686); `python3 tools/check_eap_figures.py` → 0 problems,
  liveness probe fired. Both exit 0 (read directly, no pipe).
- Gmail probe, the API half: `create_draft` (subject "EAP mail — draft in
  progress (session probe)", one-line body, no recipients) returned
  `{"id":"r-9208017789511753451","messageId":"1a0687ba98696dbd","threadId":"1a0687ba98696dbd"}`;
  `list_drafts` with `subject:` query and `DRAFT_VIEW_FULL` read it back with
  subject, plaintext body and `labelIds: ["DRAFT"]`. The owner half — that he
  sees and can edit it in Gmail — is his to say in words; nothing is recorded
  as the broader capability until he does.

## What was done

- **The restate, then the reads.** The four labelled lines first; then the
  six-read orientation as the boot hook delivered it, the owner-direction record
  § 5b–5d, the draft file whole, the evidence report § 10 → § 5 → § 3 → § 7 → § 2,
  the correspondence record § 0–7, both sent mails from superbot (`docs/eap/`
  over the direct API, read in full), `night-review-2026-07-10.md` (Q7 at
  :330–348, Q16 at :694–745 — read BEFORE FD-01/FD-02 were used, per § 10
  item 2), and the raw verifier records for FD-01/FD-02/FD-17 out of
  `fleet-b-full-wf_fb35b278-362.json`. Not from the report's summaries.
- **Part 1 proposed** (`docs/planning/2026-08-24-final-eap-email-draft.md`,
  below the beat table, outside the COPY markers): 536 words by the same
  method as `--count`; every fact in it is one he stated in § 5d or the beat
  table's facts column; beat 3 is marked as his alone and its proposal is
  assembled from his sitting answers plus the reflection's DERIVED thesis line.
- **Part 2 patched** — patch 1 on the 21-of-21 sentence, keyed to the false-done
  rows the addendum actually carries (not the spine's citation finding, which
  the sitting did not choose); patch 2 on the outside-vendor paragraph, two
  scopes: the fortnight's false-dones were caught by a commissioned review, and
  the July 3-of-3 fabricated reviews (`docs/audits/eap-project-audit-2026-07-14.md:151`
  · `docs/fleet-inconsistencies-2026-07-13.md:147`, INC-43) with the self-fix.
- **The addendum** — 453 words of body plus 88 in its five source bullets (541 in all, the figure the owner's length call is put against), framed as the answer to Anthropic's question in
  his terms: what the two share (shiftlife, his § 5c words), the three adds
  (verbatim delivery — with `docs/eap-retrospective.md:80`'s 767 of 949 as the
  rules-of-form evidence and the judgement caveat; the coordinator as a mind of
  its own, his degree claim marked inferred; eight at once under unlimited
  usage), the four fixes (stall visibility + the mockup; the honest queue with
  his "not nearly anything you could call done"; coordinator authority as the
  16 July pointer; the inter-Project channel as the 12 July pointer), then the
  three false-done rows: **FD-01** (superbot-games PR #16 — its title and body
  READ DIRECTLY today: *"ci: substrate-gate runs the pure-domain test suite"*,
  body counting "mining 62 + encounters 11 + exploration" as 73; the gate
  collected 73 of 121; the close-out heartbeats' "complete green" at
  `docs/launch-readiness-2026-07-10.md:504–518`), **FD-02** (Q16: README
  "no exceptions" PRIVATE, 8 PR bodies — pokemon PRs #2, #4–#10 — all 13
  account repos public; the mail does not name the repository or the vendored
  source, by the confidentiality decision's spirit and because the point does
  not need them), **FD-17** narrowed to INC-04 (`fleet-inconsistencies:78` —
  integration-ENABLED vs usage-QUOTA-capped). No spine text copied; the A1-6
  clause the report corrects is not in the mail at all.
- **The overlap rule applied from the sent bodies, not headings:** the 12 July
  mail's asks (d)1 continuous mode, (d)6 fleet visibility, the inter-session
  channel; the 16 July mail's whole argument (coordinator authority, venue-scoped
  denial, scoped grants) — each is one pointer clause or the existing link
  bullet; nothing re-argued.
- **Links:** the review site — Overview as the entry, `/after/`,
  `/examples/#projects-overview-mockup`, `/problems/` — all HTTP 200 over direct
  egress at start with the four anchors present; his words (§ 5c–5d); the night
  review + PR #16 (superbot-games is public, `private=false` checked);
  fleet-inconsistencies (INC-04, INC-43); the instruction box (present on
  `main`). All five pre-existing links confirmed on `main`; superbot's doc 200
  via the API.
- **Figures re-derived:** block **2,322 words** (`--count`), `--verify`
  loss-free (2322 → 2322 at the reviewed head `4d90d43`; 2323 → 2323 one commit earlier), 30 bold + 13 italic (italics deliberately held at 13
  so the 2026-08-25 card's guarded figure stays true), `--selftest` 13/13.
  `check_eap_figures.py` clean after two changes: the "three pages" pattern now
  accepts any page word (the block is about four), and the three figures that
  were measurements of the 1,686-word text — cut-only 1,678, the 487-word
  one-sentence floor, "1,678 after the cut" — are computed from the pinned
  pre-addendum commit `a65fcfd` instead of the live mail, so the 2026-08-25
  card and the historical sentences stay true without being rewritten. **That
  is the one tool touch in a records-and-draft PR**, taken because the
  alternatives were falsifying a historical card or leaving the checker red;
  it is the checker's own "update in the same commit" clause, and it is
  disclosed here and in the PR.
- **Consumers updated in the same diff:** the draft's § 1 (rows 6–8), status
  header, the ⚠ Part 1 note, the subject line, § 2's one-word-calls block;
  `docs/owner-queue.md` (E1 ▶ 2026-09-03 block + two figure sentences);
  `docs/current-state.md` (work state + two E1 lines); the program's NOW
  pointer + § 7 row; `owner/README.md` regenerated (preflight's owner-index
  drift). Layer-2 handoff: null (fleet-manager itself; no repo attached —
  superbot's files were read over the API).
- **The census re-run, not rewritten:** 28 repositories on 2026-09-03
  (`creator-kit`, created 2026-08-25, the day after the census) and 8,124 PRs by
  the search endpoint; 72 doc routes today (`doc-routes.json`). The mail keeps
  the dated 24 August figures because the linked census carries them; the
  refresh is one of the one-word calls in § 2.
- **Gmail:** the probe draft was then UPDATED in place with the full mail —
  plain body + HTML body from the render tool, subject *"Claude Code Projects
  EAP — the final review, six weeks on"*, no recipients — three times as the
  text moved — **four updates in all**, the last carrying the round-2 body
  (message ids `1a0688cbba3238fb` → `1a06898c5ba3551a` → `1a068adeab59caad`;
  draft id stable). `get_draft` MINIMAL read the final one back at ~19:23Z:
  `labelIds ["DRAFT"]`, `messageId 1a068adeab59caad`, the Part 1 snippet —
  the body in Gmail is the reviewed head's text. Capability line in
  `docs/CAPABILITIES.md`, API half only.
- **The mailbox, re-checked (the critic's own flag):** thread A still holds only
  the 07-16 21:12 and 21:42 messages; thread B unchanged; nothing from the
  vendor since 2026-08-18 — an async UX-study invitation ("20 minutes on how
  you'd describe Projects"), metadata only here, unanswered on the record.
- **Verification before Codex:** the free-key Gemini pass (`gemini-3.6-flash`,
  one `generateContent` call with the rendered mail + the diff; three 503s then
  200 on the fourth attempt each run; the first run's answer was cut off by its
  own thinking budget at `maxOutputTokens` 4000 — re-run at 20000). Seven
  findings: **5 conceded** (beat 3 contradicted Part 2's "ran clean from the
  first night" — his own timing added, "in the second week"; beat 3's
  finished-product sentence reordered; 949 used for MB and for cards — unit
  added; "his words" on the documentation ask replaced by his exact phrase;
  patch 2 split into a sentence), **2 survived** (Finding 3's "recalled at the
  right moment" is approved Part 2 text outside this change; the night-review
  link's Q7/Q16 labels are what a reader needs to find the rows).
- **Codex round 1** on `d70f748` (requested 18:47:32Z, review 18:56:01Z —
  509 s; findings as inline comments, the summary body empty as the ledger
  says): **4 findings, all P2, 4 conceded, 0 survived** — the owner-queue's
  Part 1 count (518 → 537); the draft's verification paragraph still quoting
  the pre-addendum `--verify` and DOM figures (re-run 2026-09-03 with Chromium
  `--dump-dom` on the combined document: 30 `<strong>`, 14 `<em>`, 15 `<li>`,
  26 `<p>`, 0 asterisks, `HTMLParser` clean — recorded, the old figures marked
  superseded); the second live `OQ-E1` header double-counting in the generated
  owner index (the 2026-08-28 entry marked `(superseded body)`, index back to
  38 open of 69); and `--eml` previewing Part 2 only under the tool's older
  hard-coded subject (the docs narrowed — the Gmail draft is the complete
  preview; the tool itself untouched, per the no-mechanism-change scope).
- **Codex round 2** on `57021fb` (requested 18:58Z, review 19:06:45Z): **4
  findings, all P2, 4 conceded, 0 survived** — beat 3's "in the second week …
  many of them" was the session's dating, not his words (replaced by his own
  § 5d phrase, "after the classifier changed", and the proposal's intro now
  names that source); the review-site paths were backticked text in the HTML
  body, not links (each named page is now a markdown link → an anchor in HTML,
  "label (url)" in plain text); the addendum's budget must count its own five
  source bullets (453 + 88 = 541, now the figure the § 2 length call is put
  against); the owner-queue send step named only the cc list (now the EAP
  alias in To and the cc addresses, both from the July thread's headers).
  **Missed in round 2's own review body** (read only at round 3, because the
  round-2 poll printed review ids and not bodies — the finding sat in the
  review body, not inline): owner-queue's "is **1,686** now" — fixed, "was
  1,686 after his 2026-08-25 cut and is 2,322 with the addendum".
- **Codex round 3** on `4d90d43` (requested 19:10Z, review 19:17:52Z; the
  cap's last round): **3 findings, all P2 — 3 fixed, 0 refuted, 0 open**,
  each verified directly, no fourth round: the card had not recorded the
  post-round-2 Gmail update (it had happened — message id `1a068adeab59caad`;
  now recorded with its read-back); the card's `--verify` figure was one
  commit stale (2323 → 2322, corrected); `docs/current-state.md`'s retained
  2026-08-25 paragraph mixed the live count with a superseded "does not draft
  Part 1" instruction (the instruction marked superseded by Shape A). Direct
  verification after the fixes: `check_eap_figures.py` clean,
  `render_eap_mail.py --verify` loss-free, `scripts/preflight.py` failing only
  on the born-red hold, `python3 bootstrap.py check --strict` exit 0 after the
  flip. **Tally across the three rounds: 12 findings — 12 conceded, 0
  survived** (4 + 4 + 3, plus the round-2 body finding counted with round 2's
  four — 4 + 5 + 3 = 12).

## § 10 preconditions, ticked

1. Flagged rows: #4 UNVERIFIED, #7 PROVENANCE FLAG, #11 WORDING RISK — none
   used in the mail (the chosen addendum is the Projects-versus-sessions
   answer, not Fleet A's findings); #1's 9-vs-10 — not used. Dropped, not
   resolved, and said so.
2. `night-review-2026-07-10.md` read before FD-01/FD-02 — yes (Q7, Q16, and the
   executive summary's "caught only by this commissioned review... on no
   schedule", :40–47, which the addendum's "none by a gate" rests on).
3. B5 vs the false-done ledger — the ledger (Fleet B), his own priority.
4. The 25 bare "refuted" reasons — not pulled (out of scope for a draft
   session; the retained JSON still holds them).
5. Every citation re-opened — the three FD rows, both patches' sources, the
   767/949 line, his quoted phrases (§ 5c–5d), the 13-public-repos line.
6. Every linked document on `main`, every count dated in the text; the live
   re-counts above recorded here, not silently substituted.

## 💡 Session idea

**A figure checker that knows which figures are measurements of a past text.**
`check_eap_figures.py` treated cut-only, the one-sentence floor and "after the
cut" as live properties of the mail, so the first by-design growth of the mail
turned three true historical sentences into MISMATCHes and the only fixes were
to rewrite a historical card or to pin them, which this session did by hand
(`CAP_BASE`). The general form: a guarded figure carries the SHA of the text
it measured, and the checker recomputes it from that SHA — "as of" is data,
not prose. Worth having because the same shape sits behind every dated count
in this estate (routes 67 → 71 → 72, PRs 8,000 → 8,124), and a checker that
reads the date from the claim would end the "which of the three counts is
current" argument the mail's own Finding 3 describes. Deduped against
`docs/owner-queue.md` and the 2026-09-01/02 idea slots: not there.

## ⟲ Previous-session review

`.sessions/2026-09-03-review-site-pass.md` (#1016) did the thing that made this
session cheap: it landed the site first, wrote the four page paths the mail
should link into this session's prompt file, and pinned every citation on the
new pages to a SHA — so the addendum's site links were a check, not a hunt. Its
one gap for this session was small and honest: it recorded the examples-shape
question as unanswered, and it still is; nothing in the mail depends on it.
The sitting card (#1013) is the reason Part 1 could be proposed at all — his
twelve answers verbatim, with the DERIVED paragraphs separated — and its
lesson (quote first, derive in a separate paragraph) is what the addendum's
"the quoted phrases are his" line enforces.
