# 2026-09-03 — the review-site pass: the websites program-review site for a first-time Anthropic reader

> **Status:** `complete` — branch `claude/anthropic-program-review-site-27w608`,
> PR #1016. Born red until this flip, the deliberate LAST step: the site work
> landed first (websites #524 → `137b80e`, live at 10:46Z).

- **📊 Model:** fable-5 · xhigh · feature build
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01GmkfGPyfxtKzVLoYCqDucb](https://claude.ai/code/session_01GmkfGPyfxtKzVLoYCqDucb) · "Program-review site for Anthropic"

**What this session is about:** executing
`docs/prompts/2026-09-02-review-site-session.md` — the owner's 2026-09-02 ask
to make the existing program-review site (<https://menno420.github.io/websites/>)
navigable and self-explanatory for an Anthropic reviewer who has never seen
the repositories, with examples of how he wants things to look, including a
mockup of the claude.ai Projects overview with each Project's state visible.
The site work lands in `menno420/websites` (its own born-red card and PR);
this card is the fleet-manager half: the Layer-2 handoff line in
`docs/repos/websites/README.md`, anything newly verified in
`docs/CAPABILITIES.md`, and the close.

## What was done

- **State check first** (owner's first step): fm `origin/main` at `ef3c0c8`
  (#1015); the live index over direct egress HTTP 200, 17,414 B, footer
  snapshot `883f52ec`, last Pages deploy 2026-08-24 on `bba93a8`; websites
  head `9ba7df4` (#523), zero open PRs; `GITHUB_PAT` present. `add_repo`
  (push) + `git clone --depth 1` over the plain URL; the plain-URL push through
  the proxy worked again (as measured 2026-08-21).
- **The cold read** — all ten nav pages, `/fleet/superbot`, `/fleet/websites`
  and both editions fetched over direct egress and read as text BEFORE the
  README or any template — produced one paragraph per page and the work
  order, put to the owner in one message with the two open questions (the
  A/B/C shape of the examples; whether the site pass must land before the
  mail). Proceeded on C (examples first) and on "every commit must stay safe
  to link" until he answers.
- **The site work — websites #524** (`claude/review-site-navigation-examples`,
  its own born-red card `.sessions/2026-09-03-review-site-navigation-examples.md`,
  which carries the file-by-file account): Overview rewritten for a cold
  reader; grouped nav; one-line era note off the Overview; `/story`,
  `/examples` (with the Projects-overview mockup, labelled a proposal with
  illustrative values), `/after`; the three owner-named problems and two
  fleet-level successes; the stale "routed to the fleet as an order" promise
  removed from five places; a link-integrity test over the static export.
  Every fleet-manager citation on the new pages is pinned to `ef3c0c8`;
  superbot citations to `8558179` / `95fc025`; the "July 8 email" file this
  site had been about to cite is the gen-1 wrap-up *candidate* (superseded by
  the July 12 mail, never sent) and is labelled as such.
- **Rendered for the owner before merge**: the Overview and the mockup section,
  chromium headless over the served export, sent with `SendUserFile` — the
  capability line below.
- **This repo**: `docs/repos/websites/README.md` — the thread block gains this
  pass (its two traps: the promise lived in five places; the mail-file
  mislabel), stamp 2026-09-03; `docs/CAPABILITIES.md` — the render-to-PNG
  line (2026-09-03).
- **Review rounds on websites #524** (the session cap is three; fleet-manager's
  hook counted each): round 1 at `af7de0d` — nine findings (one P1: the
  fixed-position mobile drawer could not scroll past 13 links on a short
  phone; eight P2), **9 conceded**, fixed in `13b383c`; round 2 at `13b383c`
  — three findings (45-not-46 PRs on the 07-09 row, a hardcoded edition
  count on the Overview, the `/ask` map row ignoring export mode),
  **3 conceded**, fixed in `41df1f3`; each fix batch verified on the
  free-key Gemini route (`gemini-3.6-flash`, one `generateContent` call with
  the findings + the diff — the first call went out with an EMPTY diff
  because of a pathspec typo and correctly reported nothing addressed; the
  second, with the real diff, 9/9 addressed, no regressions; the round-2
  batch 3/3). Round 3 requested at `41df1f3` 10:27:56Z.
- **Landing:** round 3 at `41df1f3` — clean ("Didn't find any major issues",
  `Reviewed commit: 41df1f3bad`, 10:30:58Z; tally 12 conceded · 0 partial ·
  0 survived). The card flipped at `dc6380a`; CI then went red on a real
  grammar finding — the card's Model task-class "site build" is off the
  kit's nine-class taxonomy — fixed to "feature build" at `8274b59`
  (this card had the same word; fixed here too). `quality` green 10:44:48Z,
  auto-merged 10:45:30Z → websites `main` at **`137b80e`** (#524). No
  push-event `review-pages` run fired for the merge (the trap holds);
  `workflow_dispatch` on `main` → run 33746044580, success 10:46Z. Live over
  direct egress at 10:46Z: `/`, `/story/`, `/examples/`, `/after/`,
  `/problems/`, `/process/`, `/reviews/`, `/questions/`, `/fleet/superbot/`
  all HTTP 200; the banner renders build `137b80eb`; the Overview carries
  the new h1 and the exact era sentence with its `#era` anchor and no "now
  running"; `/examples/` carries `id="projects-overview-mockup"` and "A
  proposal, not a screenshot." with no `role="img"`; `/problems/` carries
  all four anchors; `/process/` has `#glossary`; the phrase "routed to the
  fleet as an order" appears on none of the nine pages.
- **The mail session's link list, coordinated through the repo:** the review-site
  prompt's `OPEN` bullet in `docs/prompts/2026-09-02-eap-mail-session.md` now
  says the pass landed and names the pages the addendum's claims read
  against (`/after`, `/examples#projects-overview-mockup`,
  `/problems#coordinator-authority`, `/story`). Whether the site pass had
  to land before the send is moot: it landed first.
- **Open with the owner (asked in the first message, unanswered at close):**
  the examples' shape — built on C (an Examples page first; the Problems page
  already had the finding shape, so B's restyle was mostly already true) —
  and the mail order. One letter still corrects the first.

## 💡 Session idea

**A kit-taxonomy check for the `📊 Model:` task-class at card-write time.**
Both cards this session wrote "site build", a word that is not one of the
kit's nine PL-004 classes, and the finding surfaced only in CI after the
flip — one extra red run and one extra commit per repo. The `.sessions/`
README template lists the marker needles but not the nine class words; the
`session-card-venue` doc-route fires at write time and could carry them.
Worth having because it converts a post-flip CI red into a sentence read at
the moment the line is typed. Deduped against `docs/owner-queue.md` and the
findings' skill/rule map: the rule map names the marker checks, not the
task-class vocabulary. Captured here (this repo keeps ideas in cards and
findings, not a backlog file).

## ⟲ Previous-session review

`.sessions/2026-09-03-review-site-prompt-crossref-fix.md` (#1015) did the
small right thing — one stale cross-reference in the prompt this session ran
on, fixed before the session that would trip on it — and it is why the first
tool call here found every named file where the prompt said. What it could
not do was read the site: the prompt's "the July 8 email" pointed a reader at
a superbot file that is the gen-1 wrap-up candidate, never sent, and only the
cold read caught it.
