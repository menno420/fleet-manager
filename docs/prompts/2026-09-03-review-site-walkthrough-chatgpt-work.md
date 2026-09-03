# Continuation prompt — the live walkthrough of the program-review site (ChatGPT Work, local, with the owner's Chrome extension)

> **Status:** `reference` · paste-ready, `continuation-prompt` skill shape,
> preflight run 2026-09-03 at fm `2d759ac` / websites `137b80e` (live build
> `137b80eb`). Written for **ChatGPT Work running on the owner's laptop with
> his Chrome extension attached** — a browsing review, not a build session.
> The owner's words behind it, 2026-09-03: *"review this website once more
> with ChatGPT work running locally with access to my chrome extension, so
> it can fully walk the whole site and tell me if it feels intuitive to
> browse through and if everything works and looks as expected."*
> Standing instructions for that surface are a file, not restated here:
> [`chatgpt-project-instructions.md`](chatgpt-project-instructions.md).

```text
CONTINUE: Walk the whole program-review site — https://menno420.github.io/websites/
— in a real browser through the owner's Chrome extension, as a first-time
Anthropic visitor would, and tell him whether it feels intuitive to browse,
whether everything works, and whether everything looks as expected. Report
first; fix only clear defects.

BEFORE YOUR FIRST TOOL CALL — state the task back, inline in this same reply,
in four labelled lines (never one fused paragraph, never a question):
  HE SAID — the ask in your own words, one or two sentences.
  ALREADY SETTLED — what the repo already decided about it, naming the file,
                    or "nothing found yet".
  I INFER — the specs, constraints and scope the ask implies, and the follow-on
            the owner probably wants but did not spell out. Labelled inference.
  LEAST SURE — the one reading you are least sure of; he corrects it in a word.
Then begin. This is the owner's one cheap chance to correct your aim; a first
reply that only announces your first action spends it.

HOW HE WANTS TO BE SPOKEN TO (owner, 2026-09-02): acknowledge every message
he sends at the next natural boundary with how you understood it and what it
changes. One item at a time, plain language, his pace. He reviews through
what he can see: show him a page, a screenshot, a URL — not a diff.

WHERE THINGS STAND (verified 2026-09-03 ~21:30Z — re-verify first)
- The site is the websites repo's `review/` app exported to GitHub Pages from
  committed data (`review/gen_static.py`); no service, no live API; the
  "Ask about this page" links are prefilled GitHub new-issue links and the
  only intake. websites `main` is `137b80e` (#524 merged 2026-09-03); the
  live build banner says `137b80eb`; zero open PRs.
- What #524 changed, for a first-time reader: the Overview rewritten (plain
  account, a ten-minute reading path, a timeline strip, tiles scoped to that
  one repo); a grouped nav — Read first · The record · Questions — 13 links;
  three new pages: /story/ (the fortnight, the eight Projects joined to the
  seat registry, how a Project was run), /examples/ (a finding, a session
  card, a timeline, and the Projects-overview MOCKUP, labelled a proposal
  with illustrative values), /after/ (what a Project adds over a session,
  the owner's words with OWNER/DERIVED/REVIEWED labels per paragraph);
  Problems gained the three the owner names first; a one-line era note on
  every page off the Overview. Full account: websites
  `.sessions/2026-09-03-review-site-navigation-examples.md`.
- The final EAP mail is drafted and staged as a Gmail draft (fm #1017). It
  links exactly four pages: the Overview, /after/,
  /examples/#projects-overview-mockup and /problems/. Those four are the
  ones Anthropic will open first — walk them first and hardest.
- What the previous session could NOT check, which is why this walkthrough
  exists: it had a headless browser only — desktop-width screenshots in the
  dark theme, a phone width only through an iframe, no clicking. Unverified:
  the light theme; the nav at widths between about 880 and 1200 px (13
  links may wrap); the mobile drawer on a real phone-sized window (a Codex
  finding made it scrollable — confirm); the "/" and Ctrl-K palette; the
  theme toggle; whether every fragment link scrolls to the right place
  (/#era, /process/#glossary, /story/#projects, /story/#ritual,
  /examples/#projects-overview-mockup, /problems/#coordinator-authority,
  #false-done, #stall-visibility, #incident-2026-07-12); every EXTERNAL
  link (the link-integrity test covers internal hrefs only — the GitHub
  links into fleet-manager at commit ef3c0c8 and superbot at 8558179 were
  never opened in a browser); the prefilled issue links (open one, read the
  title and body it prefills, do NOT submit); /story.json and
  /reviews/feed.xml; all 25 /fleet/<repo>/ lane pages; both editions.

READ FIRST (a floor, not a boundary — each verified at HEAD 2026-09-03)
1. The live site itself, cold, before any file — the Overview's own
   suggested order (Overview → Story → Problems → Examples → After), then
   every nav page, then the dynamic ones listed above. Write your notes as
   you go; reading the repo first masks exactly what a stranger would trip on.
2. websites `review/README.md` (verified at HEAD) — the surface table, the
   bake→commit→render model, the house rules: every claim cites a
   PR/commit/file; problems as specific as successes; nothing estimated.
3. websites `.sessions/2026-09-03-review-site-navigation-examples.md`
   (verified at HEAD) — what was changed and why, the twelve Codex findings
   already fixed (do not re-report those), and the card template you will
   follow is in websites `.sessions/README.md`.
4. fleet-manager `docs/repos/websites/README.md` (verified at HEAD) — the
   entry point: the measured traps (a merge fires no Pages rebuild — dispatch
   `review-pages.yml` by hand; the exporter's exit 0 is not link integrity).

DECIDED (owner, 2026-09-02/03 — do not re-litigate)
- The existing site is the target; static export from committed data; no
  service, no form that pretends to submit.
- The Projects-overview mockup is a proposal, labelled as such, with
  illustrative values; it is never presented as a screenshot of the product.
- Every claim on a page cites a PR, commit or file; nothing estimated;
  "we don't know" is a valid sentence.
- This session REPORTS. Fix only a clear defect — a broken link, a typo, a
  layout that is plainly broken at a common width — in the same PR, each fix
  named in the report. Anything judgement-shaped (wording, ordering, colour,
  "I would have put this first") is a finding for him, not a change.

REJECTED, AND WHY
- Restyling or restructuring pages during the walkthrough → the owner has
  not yet answered which shape he wants the examples in (A/B/C, asked
  2026-09-03); a restyle now would pre-empt his answer.
- Refreshing the data mirrors (review/data/*.json) → allowed by the README
  but not needed for a walkthrough; a stale mirror banners honestly.
- Touching control-plane, dashboard or botsite → separate services; the
  footer links to them are labelled "not part of this review".
- Any fan-out → one attended browsing session; the owner did not opt in.

OPEN (his to answer; carry, do not decide)
- The examples' shape, A/B/C (asked 2026-09-03; built on C meanwhile).
- Whether findings from this walkthrough become a second site pass, and on
  which surface — your report is the input to that decision.

YOUR FIRST STEP
Confirm the state above: open https://menno420.github.io/websites/ in the
browser through the extension, read the footer/banner build SHA (expected
137b80eb) and the nav (expected 13 links in three groups); then check the
websites repo through the GitHub connector — `main` at 137b80e, zero open
PRs. If the extension cannot open the page, report the exact message it
gives — never a wall. Then begin the walk, notes per page.

WHAT TO JUDGE, PER PAGE (the report's shape — one block per page, in the
order walked; a page with nothing wrong still gets its block, one line)
- URL · what worked · what confused you as a first-time visitor · what looks
  off (misalignment, overflow, contrast, a label that does not match the
  page) · severity: P1 broken / P2 confusing / P3 polish · screenshot name
  if the extension can capture, otherwise a precise description.
- Sitewide, answer his three questions in his words: does it feel intuitive
  to browse through; does everything work; does everything look as expected
  — each yes/no with the one or two things that decide it.
- Specifically: can a stranger say within one minute what the program was,
  who ran it, and that it ended? Is the mockup unmistakably a proposal? Are
  Q&A, Answer log and Archived answers distinguishable from the nav alone?
  Do the three problems he names first read as prominent as the successes?
  Light theme and dark theme both. Desktop, a ~1000 px window, and a phone
  width.

DONE WHEN
- The report exists as websites `docs/audits/2026-09-DD-live-walkthrough-chatgpt-work.md`
  (the audits folder has a README; match its neighbours), in the shape above,
  landed through the repo's normal path: a session card in `.sessions/`
  committed FIRST with Status in-progress (the four markers from
  `.sessions/README.md`; `📊 Model:` at family level with task-class
  `review/verify`; `📍 Venue: chatgpt-work`), a READY PR, `quality` green,
  the card flipped complete as the LAST step. Auto-merge is armed on open by
  the repo's workflow, so a green head lands itself.
- The same report given to him in chat in plain language, his three
  questions answered first, the per-page blocks after.
- If a template, CSS or Python file was touched for a clear defect:
  `python -m pytest review/tests -q` green (`python3` where that is the
  name) and `python bootstrap.py check --strict` exit 0 at the flip; after
  the merge, `review-pages.yml` dispatched by hand and the live page
  re-opened to confirm — a merge alone rebuilds nothing.

OUT OF SCOPE
- Restyling, reordering, rewriting content; refreshing mirrors; the other
  three services and their known dead links; the final EAP mail (drafted,
  the owner sends); anything in fleet-manager (its activity index reads
  websites' cards on its own).

LESSONS FROM THE PASS THIS CONTINUES
- A stale promise ("routed to the fleet as an order") lived in five places —
  the ask-url body and four templates; grep the rendered pages, not one file.
- A superbot file the record called "the July 8 email" was the gen-1 wrap-up
  candidate, never sent; the label was fixed only because the page was read
  cold. Read what a link opens, not what its label says.
- Headless captures clamp at about 500 px wide, so a "mobile overflow" was
  an artifact; a real browser at a real width is the check — which is you.

CLOSE WITH
websites' own close: card flipped complete last, PR green and merged, the
Pages dispatch and live re-check only if you changed a rendered file. Local
git for the tree, the connector for the remote — do not look for `gh` or
a PAT there; nothing waits on the owner's approval on this surface. Append
to websites `docs/CAPABILITIES.md` anything newly verified about browsing
through the extension (what it could open, capture, click), with the
observed result verbatim — a capability, never a wall.
```

## What was verified for this prompt, and what was not

Verified 2026-09-03 ~21:30Z: fm `origin/main` at `2d759ac` (#1017 — the
mail drafted and staged, its four site links read from that session's card);
websites `main` at `137b80e`, zero open PRs in either repo; the live index
banner renders `137b80eb`; the 13-link nav counted from `review/app.py`
`NAV`; the four `READ FIRST` paths present at HEAD; websites `docs/audits/`
exists with a README; the connector-as-complete-route fact is
`docs/CAPABILITIES.md` (2026-08-10, fm #835). Not verified: that the owner's
Chrome extension can capture screenshots (he states it can browse — source
truth; capture is asked for "if it can"); the interpreter's name on his
laptop (`python` written, `python3` allowed).
