# 2026-09-03 — the review-site pass: the websites program-review site for a first-time Anthropic reader

> **Status:** `in-progress` — branch `claude/anthropic-program-review-site-27w608`;
> flips to `complete` + PR number as the deliberate LAST code step.

- **📊 Model:** fable-5 · xhigh · site build (attended, no fan-out)
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
- Landing: (filled at close — the Codex round, the merge, the `review-pages.yml`
  dispatch, the live fetch.)

## 💡 Session idea

(filled at close)

## ⟲ Previous-session review

(filled at close)
