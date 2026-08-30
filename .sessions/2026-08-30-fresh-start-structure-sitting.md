# 2026-08-30 — the fresh-start structure sitting: nine open items answered

> **Status:** `in-progress` — born red. The owner is answering the redirect
> doc's § Open and § Addendum one topic at a time; this card grows as answers
> land and flips only when the PR is verified green with a Codex round on the
> flip head.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact. The
  sanctioned token and why it is not a wall: [`.sessions/README.md`](README.md).
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_0135KbiXT3G8WY4yyni2nEJM](https://claude.ai/code/session_0135KbiXT3G8WY4yyni2nEJM) · "Fresh-start redirect planning"

💡 Session idea: the owner's B2 answer redefined a rule I had written as a
*decision* procedure into a *surfacing* one — "the value the file holds is
gone" is a judgement no script makes. Every mechanical rule this estate writes
should be checked against that split before it is built: does it decide, or
does it surface for someone who can decide?

## Mission

Continue the fresh-start redirect planning conversation
([`docs/planning/2026-08-30-fresh-start-redirect.md`](../docs/planning/2026-08-30-fresh-start-redirect.md)),
turn-based, one topic at a time, in the owner's stated format: how I see it →
what I would suggest → one guiding question. Capture everything settled before
the session ends. No implementation — the [D-0022] planning hold governs, with
records and captures as its carve-out.

## Previous-session review

The three cards before this one (`2026-08-29-disposition-tally-fix`,
`2026-08-29-fleet-orchestration-retro`, `2026-08-29-fm981-round2-consumption`)
close out the 2026-08-29/30 sitting that produced [D-0019]–[D-0025] across
fm #981–#987. State verified at HEAD `45076b1`: all seven merged, tree clean.
**One correction to the handoff's state block:** it claimed zero open PRs;
fm #958 (`codex/consume-owner-comment-e2e`, opened 2026-08-28) is open. Its
diff is unread — the owner-comments index shows 0 unconsumed and 0 consumed
for `fleet-manager`, which is suggestive of mootness, not sufficient for it.
Left alone; raised to the owner.

## What the next session needs to know

*(This block is written to the shape proposed under B3 in this sitting — a
short brief for a reader who was not here, ahead of the long-form record.)*

- The redirect ([D-0025]) is unchanged: the plan executes in a fresh hub, this
  repo becomes the read-only archive. Nothing is created or moved yet.
- Nine open items went to the owner; his answers are recorded below verbatim
  and folded into the redirect doc's § Open.
- The likely next sitting is **naming the folder tree**, because the archive
  freezes and renames become expensive at cutover.

## Answers landed this sitting

Nine open items went to the owner in his stated format (how I see it → what I
would suggest → one guiding question), one topic at a time. All nine drew an
answer; his words are quoted in
[the redirect doc](../docs/planning/2026-08-30-fresh-start-redirect.md)
§ *Answered — the 2026-08-30 morning sitting*, which is the citing home. In
brief: hard cutover **agreed on the split form** (write cutover absolute, the
GitHub archive flag may lag) · carry-cut **agreed** with his strictness
principle and a third verb (carry whole · distill · archive only), seeding
scoped to *"mostly fleet-manager and superbot"* · the name **leaning `estate`**,
not confirmed · no per-file stubs with the rewrite pass made a **tool** ·
archive-eligibility redefined from a *decision* rule to a **surfacing** one
(value-is-gone is a judgement; N = 30 days is the proxy) · pin-in-file plus
generated roster · session cards age on a fixed clock and get **read** (last 3
per session, with a short brief block near the top — the shape this card uses)
· per-vendor instruction files **kept separate** (`AGENTS.md` shared,
vendor files delta-only) with the Gemini half served by the existing
`tools/build_notebook_bundle.py` · mirror **frozen**, with role-naming as the
upstream fix so renames never arise.

**Landed in this PR from those answers:** the § Answered section above;
[D-0019]'s dated cadence amendment (his *"Yes, agreed"* to C1);
`OQ-FM-FRESH-START-CONFIRMS` moved to two-of-three answered with only the name
owed; the initiative-loop design's review-cadence item closed.

**Three corrections this session made to its own earlier claims**, each caught
by the owner-review round rather than by a reader: a design budget built on a
source cap read from a hook summary instead of
[`docs/providers/gemini-notebook.md`](../docs/providers/gemini-notebook.md)
(whose own § built table shows corpora already running at 6× the number being
budgeted against); a predicted idea-queue breach argued from the *harvest*
total while the cap was being defined over *undisposed* ideas — the one weak
signal (4 of 57 ungroomed) points the other way; and a claim that nothing
routes to the per-repo `intent.md` files, asserted before the entry points were
grepped. The last one held: 0 hits in `README.md`, `docs/MAP.md`,
`.claude/CLAUDE.md`, `docs/repos/README.md` and `docs/current-state.md`; 1 in
`docs/owner-queue.md`.

## Built this sitting, on his blanket assent

He answered the five open recommendations as a list — *"Yes I agree with all
current suggestions."* That is a real authorization and is recorded as one, but
it is not a per-item verbatim ruling, so each decision entry names the exact
recommendation it ratifies and can be corrected alone. Four entries landed:
**[D-0026]** the new hub is named **`estate`** · **[D-0027]** the generated
`owner/` index, built now here rather than deferred · **[D-0028]** the idea cap
(50, provisional, triggers a review and never blocks recording, counts
undisposed ideas) · **[D-0029]** the archive-candidate check as a detector
inside [D-0021]'s S2 hook rather than a cron. `OQ-FM-FRESH-START-CONFIRMS` is
now fully answered and closed.

`tools/gen_owner_index.py` + `owner/README.md` are the build. **Two defects
caught by positive control before landing**, and the control is the point —
running the generator only proved it ran. First, `OQ-FM-FRESH-START-CONFIRMS`
was classified closed and dropped: its header reads `✅ TWO OF THREE ANSWERED`,
and the ✅ test ran before the partly-answered test, so the entry most live that
day vanished from the index built to surface it. Precedence reversed, with the
reason in a code comment. Second, "Read and edit" listed 23 owner-guidance
documents undifferentiated, burying the three `intent.md` files he had gone
looking for under twelve seat-era drafts from July — split into live and
historical on the estate's own stated rule, with the demotion visible in a
collapsed block rather than silent, per his own A2 principle.

## The skill fix he asked for, and the defect that earned it

Writing the ChatGPT Work prompt, this session read `docs/providers/chatgpt.md`,
`docs/prompts/chatgpt-project-instructions.md` and `docs/execution-surfaces.md`
— and then hedged that it *"could not verify whether ChatGPT Work can open a PR
through the connector."* The owner corrected it in one line: *"Gpt work has full
access and you could verify that in the repo."* He was right and the record is
unambiguous — `docs/CAPABILITIES.md:429`, `MEASURED` 2026-08-10 across fm #835's
entire landing: branch, commits, a READY PR, review replies, resolved threads,
check runs and a full Actions job log, all through the connector, with repo
metadata `admin: true, push: true`, and the entry closing *"Do not probe for
`gh` or `$GITHUB_PAT` on that surface; their absence blocked nothing."*

**The hedge was a false wall written into a prompt** — an artifact the receiving
session would have obeyed — and `tools/check_no_false_walls.py` does not scan
prompts, so nothing would have caught it. His fix, his words: *"Whenever I
mention who the prompt is for the skill should tell you to read the relevant
information about the specified AI."* Applied to
`.claude/skills/prompt-preflight/SKILL.md` § 3, which now names **four** sources
instead of one — `providers/<vendor>.md`, `prompts/<vendor>-*.md`,
`execution-surfaces.md`, and `CAPABILITIES.md` **grepped for the surface name**,
with the last marked mandatory and this incident as its measurement — and to
`.claude/skills/continuation-prompt/SKILL.md` § 5, which routes to it. Both
skills are `local` tier in `docs/SKILLS-local.md`, so no kit re-apply row is
owed.

### The same defect, one layer up — in the review round itself

The owner's second correction, immediately after the first: *"This is a defect
in the review round aswell."* He is right, and it is the more interesting half.
The owner-review hook's question 1 ended *"If you only inferred it, say so in
the reply"* — and this session discharged it by **writing the hedge**. A
confession reads as rigour, costs one sentence, and satisfies the question
literally; the `grep` that would have refuted it costs a tool call. So the
review round was **rewarding wall-writing**: it converted an unchecked
assumption into an explicitly stated limitation and called that an answer.

Fixed in `.claude/hooks/owner_review.py`'s `FIXED` block by **ordering the
discharge**: check first — grep `docs/CAPABILITIES.md` for the surface or
credential, open the `providers/` or `conventions/` doc, read the file at the
line, hit the live API — and confess only when the tree and the live surface
genuinely cannot answer, naming the lookup you ran and what it returned. The
question now states the rule outright: ***"I could not verify X" is a false wall
unless you tried***, and a wall in a reply or a prompt is worse than one in a
doc because `tools/check_no_false_walls.py` scans neither. The incident is
recorded in a comment above the block, per the file's existing convention of
carrying each question's measurement with it.

Verified: `ast.parse` clean, and the hook exits 0 on an empty payload
(fail-open, as designed). The real positive control is the next Stop event —
the amended text appears in the feedback or the edit did not take.

## What the owner asked for, and what was still missing

He asked for **a folder directed at him** — one place showing the ideas,
decisions owed, open questions, and the documents written for him to edit.
Proposed as a **generated** `owner/` folder (truth stays at source, the index
is swept from it, so it cannot rot); go/no-go and the fleet-manager-now vs
new-hub-birth question are with him. Same build as his *"made visible in a more
efficient way"* under the idea cap.

The documents he could not find are
`docs/repos/<repo>/intent.md` — **three exist** (`spider-bot` 4 questions,
`spider-swing` 5, `substrate-kit` 1; all three written 2026-08-28, all
`Status: owner-guidance`, awaiting his words), plus `docs/intent.md` for
fleet-manager itself — against the 28 repositories the owner-comments checker
enumerates. The prepared prompts are
[`docs/planning/2026-08-28-owner-intent-questions.md`](../docs/planning/2026-08-28-owner-intent-questions.md)
(167 lines, 12 sections), tracked as `OQ-INTENT-WRITE-UP`.

## The afternoon batch — four more packages

The sitting continued past the nine opening items. Settled and recorded as
[D-0030] (card idea markers: one canonical bullet form, gated by the preflight
added-card lane, coached by [D-0021]'s S2 skill, no backfill), [D-0031] (the
no-idea null retires rather than votes, stated in chat + card + the durable
disposition source that S1 must build), and [D-0032] (the findability contract:
the required reading order stays, the acceptance test is restated around
retrieval, one question per file, no file outside a folder, generated map).

Measurements this session produced, all reproducible from the tree:

- 453 cards · **452 carry 💡, 0 text-only** · bullet 59 / heading 198 /
  paragraph-start 206 · `gen_idea_backlog.py:70` harvests the bullet only, so
  **391 structural ideas are invisible to the queue**.
- `docs/` + root: 371 files, median 132 lines, **75 files over 300 lines hold
  57% of all prose**.
- Median filename **2 words**; **62 of 65** subfolders carry a README; **64**
  loose files at `docs/` top level belong to no folder.

## Corrections this session made to its own claims

Eight, each caught by the owner-review round rather than by a reader. The three
that changed a recommendation: a design budget built on a source cap read from
a hook summary rather than `docs/providers/gemini-notebook.md` (whose own table
shows corpora already run at 6× that number); a queue-growth ceiling quoted as
"up to 393" when the real structural figure was **391**; and a claim that every
failure this session was a top-level file, when **four of eight were foldered** —
the scope correction now carried in [D-0032] itself.

The pattern behind most of them, stated so the next session can look for it:
**grep-and-truncate reported as a read.** `head -50` on a 114-line result is
what hid `docs/execution-surfaces.md:137`, and that single failure is the
evidence base for [D-0032]'s one-question-per-file rule.

## Cross-vendor review — fm #989

ChatGPT Work delivered the independent second opinion (tree-only cold read,
structure review, five `owner/` workbooks, draft `AGENTS.md` + `codex.md`).
Reviewed at head `ce6044fc`: three findings raised, of which **F2 was withdrawn**
after the owner clarified that the required reading order stays — the doc's
wording, not the review, was wrong, and [D-0032] fixes it. Its review caught two
real defects in this branch, both since fixed: `docs/MAP.md` carried no route to
`owner/`, and `docs/planning/README.md` still listed the fresh-start confirms as
open after they were answered.

## Codex round on fm #988 — 11 findings, all `[conceded]`

Requested at flip-readiness per [D-0019], on head `bd3384a`. Codex returned
**2 P1 and 9 P2**. Every one was verified locally and fixed; none survived.

| # | Sev | Where | Finding | Disposition |
|---|---|---|---|---|
| 1 | P1 | `gen_owner_index.py:94` | closure inferred from `DONE` anywhere in a wrapped headline dropped a live entry (`OQ-SHIFTLIFE-PHASE0`, which retains two owner asks) | `[conceded]` — closure now read from the entry-status position only; the entry is back in the index (verified: 1 occurrence) |
| 2 | P1 | `gen_owner_index.py:114` | only the ❓ line was kept, so questions rendered as fragments ending in "and"/"the" | `[conceded]` — continuation captured to the next question/heading/blank; output now full sentences |
| 3 | P2 | `docs/decisions.md` D-0025 | open items listed as unanswered after the morning sitting answered all three | `[conceded]` — closed with a pointer to § *Answered* |
| 4 | P2 | `gen_owner_index.py:83` | duplicate filter knew `(original body)` but not `(superseded body)`, so a resolved entry's superseded copy showed as open | `[conceded]` — both forms filtered |
| 5 | P2 | redirect doc :133 | § structure-first still named the six-read order as compensation, leaving both the old and corrected readings in one document | `[conceded]` — that section rewritten; the reading order is explicitly excluded from the class |
| 6 | P2 | `prompt-preflight/SKILL.md:79` | the literal `<vendor>` route resolves to `docs/providers/codex.md`, which does not exist | `[conceded]` — routed to `docs/providers/chatgpt.md` (Work/Codex § at :154) with a check-the-path-exists instruction |
| 7 | P2 | redirect doc :490 | **391 counted cards, not blocks** — five cards carry several paragraph ideas, and one "heading" was an H1 title | `[conceded]` — re-derived: **409** structural blocks (197 heading + 212 paragraph). Sizing S1 on 391 understated recovery by 18 |
| 8 | P2 | redirect doc :582 | README denominator excluded three tracked dirs for holding no Markdown | `[conceded]` — **62 of 68, six uncovered**, which is materially weaker evidence than 62 of 65 |
| 9 | P2 | `gen_owner_index.py:307` | no drift check anywhere, so the generated CORE surface goes stale on the next source edit | `[conceded]` — `--check` mode added and wired into `scripts/preflight.py`; negative-controlled (exit 1 on injected drift, 0 clean) |
| 10 | P2 | `gen_owner_index.py:295` | bare `\| … \|` rows without a header are not a Markdown table on GitHub | `[conceded]` — header + separator emitted |
| 11 | P2 | `gen_owner_index.py:172` | an unreadable owner-comment index became a silent zero, so the page could assert "none unconsumed" about a source it never read | `[conceded]` — unreadable indexes collected and rendered as an explicit incompleteness warning |

**Tally: 11 `[conceded]`, 0 `[survived]`, 0 `[partial]`.** Findings 7 and 8 are
the notable ones — both corrected numbers this session had published, and both
are the same defect class the session spent the day correcting in itself: a
figure derived from a convenient denominator rather than the one the claim
needs.

## Verification

- [ ] `python3 bootstrap.py check --strict` on a real exit code at the flip
- [ ] Codex round at flip-readiness ([D-0019]); Gemini for mid-session checks
- [ ] Card flipped to `complete` as the deliberate last step
