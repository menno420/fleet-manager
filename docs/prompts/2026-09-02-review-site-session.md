# Continuation prompt — the review-site session (drafted 2026-09-02, after the review sitting)

> **Status:** `reference` · paste-ready, `continuation-prompt` skill shape,
> preflight run at HEAD `015c292` (main after fm #1013). Written for a fresh
> cloud session booting with **fleet-manager as its root** (boot triad case
> one) that then attaches `menno420/websites` with push access. The owner's
> words behind it are in `docs/findings/2026-09-02-owner-direction.md` § 6;
> the site's Layer 2 entry is `docs/repos/websites/README.md`.

```text
CONTINUE: Improve the program-review site for Anthropic —
https://menno420.github.io/websites/ — so a reviewer who has never seen the
repositories can navigate it, understand the program from it, and see
examples of how the owner wants things to look, including a mockup of the
Projects overview with each Project's state visible. Build from the written
descriptions and the one screenshot described below; he will "see if" he
can find more screenshots — proceed as if none arrive, and use them if they
do.

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

HOW HE WANTS TO BE SPOKEN TO (owner, 2026-09-02): every message he sends is
acknowledged at the next natural boundary — a step finished, a tool result
read — with how you understood it and what it changes for the task, so he
can see whether his intent landed. One item at a time, plain language, his
pace. He reviews through what he can see: show him a rendered page, not a
diff. No fan-out agents unless he opts in himself ("ultracode" in his own
sentence is a description, not an opt-in). No agent on Fable unless he asks,
in words, for that run. His words may be corrected for spelling and lightly
tightened when quoted, meaning unchanged; show him both versions when in
doubt.

WHERE THINGS STAND (verified 2026-09-02 ~22:30Z — re-verify first)
- The site is the websites repo's `review/` app: FastAPI renders committed
  data under `review/data/`, `review/gen_static.py --out _site --base-path
  /websites` exports it, and `review-pages.yml` publishes to GitHub Pages.
  No Railway service behind it since 2026-08-20 (websites' static-export
  decision of that date: the live `/ask/api` path died with the process;
  seeded answers survive as static pages). Everything a page shows is a committed file; a missing or
  stale mirror banners honestly (`fleetdata.STALE_HOURS` = 48 h).
- Live at HEAD: title "Program Review — how an owner + agent fleet shipped";
  ten pages — Overview, Process, Growth, Fleet, Reviews, Q&A (questionnaire),
  Answer log, Archived answers, Successes, Problems — plus `/story.json` and
  an Atom feed; footer snapshot `883f52ec`, data last refreshed
  2026-08-20T05:50Z. The Overview opens with "Start here — five findings
  worth your first five minutes" and a "How this site is organized" list.
  Its era framing (the program ended 2026-07-21) was fixed in websites #512.
- Fetch it with `curl --noproxy '*'`: `*.github.io` is not reachable through
  the egress proxy (ledger, 2026-07-14) and fine over direct egress
  (measured today, HTTP 200, 17 KB index).
- The websites repo is PUBLIC, default branch `main`, 303 session cards, its
  own `.claude/CLAUDE.md` + `settings.json` (which load only when a session
  boots THERE — you boot here and attach it, so read that file by hand),
  `bootstrap.py check --strict` + four pytest suites as the local gate,
  `quality` the required CI check with the born-red card hold, and Codex on
  the literal `@codex review` comment. Templates: `review/templates/*.html`
  (index, process, growth, fleet, fleet_detail, reviews, edition,
  questionnaire, questions, ask, successes, problems, base, not_found).
- Two measured traps in that repo (Layer 2 entry): pushes attributed to
  `GITHUB_TOKEN` fire NO push-event workflows, so after a merge the Pages
  rebuild needs an explicit `review-pages.yml` dispatch; and the exporter's
  exit 0 proves every route rendered 200, NOT link integrity — grep the
  `_site` tree for the links you added.
- The final EAP mail has its own session prompt
  (docs/prompts/2026-09-02-eap-mail-session.md) and will link to this site.
  WHICH COMES FIRST IS NOT SETTLED: he said the mail session would be the
  next one, then asked for this prompt so "the next session can work on
  the review website", and said he would finalize and send the mail the
  next day. Nothing he said orders the two. Ask him in your first reply
  whether the site pass must land before the mail is sent; until he
  answers, assume the mail may go out first, so any page it links must be
  correct at all times — the era framing and the "Start here" cards must
  not regress at any commit.
- The owner's screenshot of the claude.ai Projects overview, 11 July 2026
  23:34, during the program (described here because the image is not in
  the repo): a grid of eight project cards — Ideas Lab, Game Lab, Venture
  Lab, SuperBot World, Project Manager, Self Improvement, Websites,
  SuperBot 2.0 — each showing ONLY the name, an age ("yesterday", "2 days
  ago", "3 days ago") and "Only visible to you"; a sidebar listing two
  Routines (a failsafe wake, a docs reconciliation) and the same eight
  Projects. Nothing on any card says whether the Project is working,
  stalled, or waiting on him. His words on it: "This screen is where I'd
  like the projects to be showing whether or not they are active."

READ FIRST (a floor, not a boundary — each verified at HEAD 2026-09-02)
1. docs/repos/websites/README.md — the Layer 2 entry: what the repo is, the
   cutover, the traps, the paused follow-ups. Read before attaching.
2. websites: review/README.md — the surface table, the bake→commit→render
   data model, the edition ritual, the house rules (every claim cites a
   PR/commit/file; problems get the same specificity as successes; nothing
   is estimated; "we don't know" is a valid sentence), the verify commands.
3. The live site, read cold as a reviewer would, BEFORE opening a template:
   the ten navigation pages AND at least one page from every dynamic route
   family — a `/fleet/{repo}` detail, a `/reviews/{slug}` edition, the
   `/questions` ledger, an `/ask` seeded answer (the exporter renders about
   35 routes; the export-losses decision and `gen_static.py` say which).
   Write one paragraph per page of what confused you, what you could not
   find, and what a first-time reader would need. That critique is the
   work order; put it to him before editing.
4. docs/findings/2026-09-02-owner-direction.md § 5c and § 5d — what he
   wants Anthropic to understand: what a Project adds over a session (the
   instruction box as a delivery tier; a coordinator that is a mind of its
   own), the four things a Project must fix (state visible on the home
   screen; no false "queue exhausted"; workers accept the coordinator's
   authority; a channel between Projects), his 50/50 verdict, and the
   sorted instruction box (defaults / scaffolding / seat-specific).
5. websites: docs/decisions.md — its five entries of 2026-08-20 (the fleet
   source repoint, the route gate, the static export and its losses,
   `/repos` as the owner view, review comments as public records).

DECIDED (owner, 2026-09-02 — do not re-litigate)
- The existing site is the target, not a new one. ("Yes it's the existing
  one.")
- Three goals, his words: "easy to navigate", "explains everything
  properly", "preferably with some examples of how we want things to look".
- "Examples of how we want things to look" includes a mockup of the
  Projects overview — the screen above, redrawn so each Project card shows
  its state. Built from the description now; further screenshots only if he
  finds them ("I will see if I can find some example screenshots later") —
  never wait on them.
- Build from the descriptions in the tree: the July mails' findings (the
  site's "Start here" cards already are the 12 July mail's findings), the
  night report's verified findings, his answers in § 5c–5d. Nothing on a
  page that is not cited; nothing estimated; problems as prominent as
  successes; the program ended 2026-07-21 and every page says so where it
  matters.
- The site stays a static Pages export from committed data. No service, no
  live API, no form that pretends to submit (the GitHub new-issue link is
  the intake).
- Every claim cites a PR, commit or file. A mockup is labelled as a mockup
  — a proposal of how the product should look, never a screenshot of
  something that exists.

REJECTED, AND WHY
- Rebuilding on another stack or framework → the app, its tests
  (`review/tests` pin the edition format and the routes) and the exporter
  work; the ask is navigation, explanation and examples, not a rewrite.
- Reviving the Railway service or the live `/ask/api` path → websites'
  static-export decision; the audience is a reader of a static archive.
- Inventing screenshots, or presenting a mockup as the product → he will
  supply real screenshots; until then a mockup is drawn and labelled.
- Hardcoding a fleet size, a count or a date into a template → house rule;
  the pages render what the committed mirrors hold and banner when stale.
- Any fan-out for the pass → he did not opt in; one attended session.

OPEN (what would settle each — put the first to him before editing)
- THE SHAPE OF THE EXAMPLES. (A) An "Examples" section: one exemplar page
  per kind — a finding in the target shape (headline · what was measured ·
  the evidence link · what it cost · what would fix it), a session card as
  a reader should see it, a timeline of the fortnight, and the Projects-
  overview mockup — so he reacts to something concrete; (B) restyle the
  existing pages to that shape instead of adding examples; (C) both, the
  examples first as the spec for the restyle. The sitting's recommendation
  is C, examples first; he has not chosen. One letter settles it.
- The Projects-overview mockup's states. Working / idle / stalled / needs
  your input, plus last heartbeat, open asks, what it is doing now, is the
  session's reading of his four fixes and his § 5d answer 2 ("quickly
  determine which Project needs my input"). Draw it, then ask him which
  states are right — he has direct observation of what he needed.
- Whether the "time after" — Projects versus sessions, his answer to
  Anthropic's question — becomes a page of its own. The mail's addendum
  carries it; a page the mail can link would let the mail stay short.
  Recommended; not decided.
- Which pages the final mail will link. Coordinate with the mail session
  through the repo (its card and the draft's link list), not by guessing.
- Whether the data mirrors (`review/data/*.json`, refreshed 2026-08-20)
  should be refreshed for this pass. Allowed by the README ("an agent can
  refresh by running the generators"); only if a page you touch needs it,
  and say so in the card.

YOUR FIRST STEP
Confirm the state above: `git log --oneline -3 origin/main` here; the live
index over direct egress; the websites repo's head and open PRs via the
API. Attach websites with `add_repo(menno420, websites, access: "push")`,
then clone and push over the plain `https://github.com/menno420/websites`
URL through the configured remote — measured 2026-08-21 (ledger): once
attached with push, the plain URL pushes through the proxy and no PAT is
needed. `printenv GITHUB_PAT >/dev/null && echo present || echo absent`
tells you whether the direct-egress path exists as a spare route; it is
never a prerequisite. Then do READ FIRST item 3 — the ten-page cold read with one
paragraph per page — and put the critique and the OPEN shape question (A/B/
C) to him in one message before changing anything.

DONE WHEN
- A PR in websites landed green on `quality` with its own born-red card,
  carrying: the navigation and explanation changes the critique named and
  he confirmed; the examples in the shape he chose, each labelled and each
  claim cited; the Projects-overview mockup labelled as a proposal.
- `python3 -m pytest review/tests -q` green; `python3 review/gen_static.py
  --out _site --base-path /websites` exit 0 AND every internal href you
  added RESOLVES to a file under `_site` at the `/websites` base path — a
  short script that parses each added page's hrefs and stats the target
  (or a real link checker over `_site`), not a grep for the string: a
  misspelled or double-prefixed href passes the exporter and a grep alike,
  which is exactly how the double-prefix P1 shipped before;
  `python3 bootstrap.py check --strict` exit 0 in websites.
- `review-pages.yml` dispatched after the merge and the live site fetched
  over direct egress showing the change.
- This repo: your own session card with the Layer-2 handoff line, and
  docs/repos/websites/README.md's thread block updated (your thread only).
- Codex: a websites PR changing templates or Python is an executable
  surface, so it owes one round at flip-readiness, three at most, on the
  bare literal `@codex review`; the review-cadence and cap entries of
  docs/decisions.md govern, and fleet-manager's hook counts when you boot
  here.

OUT OF SCOPE
- The control-plane, dashboard and botsite services; their three known dead
  links; the `/queue` gate; `OQ-WEBSITES-PAT`. Sending or drafting the mail.
  Refreshing the mirrors unless a touched page needs it. Any mechanism in
  fleet-manager.

LESSONS FROM THE REVIEW SITTING
- A mid-turn message arrives attached to the next tool result and bypasses
  the prompt hook; acknowledge it at that boundary with how you understood
  it, or he asks why you ignored him.
- Quote his words before deriving from them, in separate paragraphs; the
  sitting swapped a cause once by restating instead of quoting.
- A listing piped through `head` was read as a whole directory and written
  into a review comment as fact; Codex caught it. Count and list before you
  write a number or an absence.

CLOSE WITH
Two repos, two cards. In websites: its own session-close — born-red card
first, PR ready, `quality` green, the card flipped last, `review-pages.yml`
dispatched. In fleet-manager: this repo's session-close skill — your card
with the Layer-2 handoff line, the websites entry point updated,
`python3 bootstrap.py check --strict` exit 0, landed on green. Anything
newly verified goes into docs/CAPABILITIES.md as a dated line with its venue
token, capability or wall, with the observed result verbatim.
```

**What was verified for this prompt, and what was not.** Verified over
direct egress at HEAD: the live index (HTTP 200, its ten navigation
targets and headings), the review app's README, the exporter's usage line,
the websites repo's visibility, workflows, templates and `.claude/`
contents, its five 2026-08-20 decisions by heading, and the Layer 2 entry's
traps. The screenshot is described from the image the owner sent in the
sitting; the image itself is not in the repo. Not verified: the current
render of the nine pages beyond the index — the receiving session's cold
read is that verification.
