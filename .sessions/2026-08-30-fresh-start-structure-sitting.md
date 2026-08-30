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

## What the owner asked for that is not yet built

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

## Verification

- [ ] `python3 bootstrap.py check --strict` on a real exit code at the flip
- [ ] Codex round at flip-readiness ([D-0019]); Gemini for mid-session checks
- [ ] Card flipped to `complete` as the deliberate last step
