# 2026-09-03 — the walkthrough prompt: ChatGPT Work + the Chrome extension review the live review site

> **Status:** `in-progress` — branch `claude/anthropic-program-review-site-27w608`
> (restarted from `main` after #1016 merged); flips to `complete` + PR number
> as the deliberate LAST code step.

- **📊 Model:** fable-5 · xhigh · idea/planning
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01GmkfGPyfxtKzVLoYCqDucb](https://claude.ai/code/session_01GmkfGPyfxtKzVLoYCqDucb) · "Program-review site for Anthropic"

**What this session is about:** the owner's follow-on ask after the review-site
pass landed (websites #524, fm #1016): *"use the continuation prompt skill so I
can review this website once more with ChatGPT work running locally with access
to my chrome extension, so it can fully walk the whole site and tell me if it
feels intuitive to browse through and if everything works and looks as
expected."* `continuation-prompt` → `prompt-preflight` run at fm `2d759ac` /
websites `137b80e`; the four surface sources read (`docs/providers/chatgpt.md`
§ Work, `docs/prompts/chatgpt-project-instructions.md`,
`docs/execution-surfaces.md`, `docs/CAPABILITIES.md` grepped for the surface —
the connector-as-complete-route entry of 2026-08-10).

## What was done

- `docs/prompts/2026-09-03-review-site-walkthrough-chatgpt-work.md` — the
  paste-ready prompt (skill shape, restate block verbatim): walk the live site
  cold through the extension, the mail's four links first (read from the
  #1017 card: Overview, `/after/`, `/examples/#projects-overview-mockup`,
  `/problems/`), judge intuitive / works / looks per page with severities,
  report first and fix only clear defects, land the report as
  `docs/audits/<date>-live-walkthrough-chatgpt-work.md` in websites through
  its own card + PR ritual (task-class `review/verify`, venue
  `chatgpt-work`). It carries what only this chat held: what the previous
  session could not check (light theme, mid-width nav wrap, the drawer on a
  real phone, the palette, fragment scrolling, external links, the prefilled
  issue links, story.json, the feed, the 25 lane pages), the fix-versus-report
  rule, the rejected options, the two open owner questions, three lessons.
  Surface facts stated as the ledger has them: connector for the remote, no
  `gh`/PAT probing, no `delete_trigger` rule, nothing waiting on approval.
- `docs/prompts/README.md` — the live-files note counts seven and names the
  new one.
- Verified: `python3 bootstrap.py check --strict` — (filled at flip).

## 💡 Session idea

**A "what the previous session could not check" line in the card template's
verification block.** This prompt's most useful payload was the list of things
the headless pass could not exercise; that list existed only in the chat until
now. Worth having because a card that names its own blind spots hands the next
reviewer its work order without a planning session. Deduped against
`docs/owner-queue.md` and the 2026-08-28 skill/rule map: not present. Captured
here.

## ⟲ Previous-session review

`.sessions/2026-09-03-final-eap-mail-draft.md` (#1017) did the linking right —
four site pages, each fetched 200 with its anchor before the draft named it —
which is why this prompt could tell the walker exactly which pages Anthropic
will open first instead of guessing; what it left for someone else was any
check that the links *render* well in a browser, which is this prompt's job.
