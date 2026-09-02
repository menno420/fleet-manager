# 2026-09-02 — the review sitting: fm #1010 and #1011 walked with the owner, item by item

> **Status:** `in-progress` — born red. The sitting is live: the owner is
> confirming or amending each 2026-09-02 decision in turn, and two hook
> corrections he asked for mid-sitting are landing in this PR. Flips
> `complete` as the last commit, after the sitting's review round answers on
> the head that flips.

- **📊 Model:** fable-5 · xhigh · review/verify
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01DSyapUpawGhaW1vThaQEvJ](https://claude.ai/code/session_01DSyapUpawGhaW1vThaQEvJ) · "Fleet manager 2026-09-02 review"

## Mission

The continuation prompt `docs/prompts/2026-09-02-step-by-step-review-sitting.md`:
walk the owner through everything fm #1010 (the night fleet's EAP
mail-evidence report) and fm #1011 (the Codex round cap, the agent model
tiers) landed, one item at a time, at his pace; confirm or correct each
decision; settle the open items. A review sitting, not a build — until he
asked for two mechanism fixes, recorded below with his words.

## What is about to happen

Six DECIDED items put to him as one-line questions, one per message; his
answers landed in the existing entries in place; the OPEN items given his
answer or a named probe; then the close. State verified at HEAD first:
main `b32e9b2`, fm #1010 / #1011 / #1012 all merged, zero open PRs, the cap
hook live with `CAP = 3`.

## The sitting so far (owner-live, in order)

1. **Item 1 of 6, the cap — confirmed as it stands.** *"I believe that's the
   right way."* Number and fine print unchanged (three rounds, the hook
   denies the fourth, per session, never reads GitHub).
2. **He widened item 1 to the whole review discipline:** *"lets make sure
   that everything related to the codex and gemini reviews is properly
   discussed. What is currently documented about both? How does an agent
   decide when to request a review or not?"* The session read every live
   surface that names either reviewer and reported the decision chain as the
   tree has it (D-0019 as amended, D-0039, the boot file's `@codex` bullet,
   TRAP-006/007/009, `session-close` step 6c, the review ladder in
   `docs/conventions/adversarial-review.md`). Three drifts found while
   reading, not yet landed: `session-close` step 6c says *"cap it at two
   re-review rounds"* (three in total, so the number agrees) and never names
   the hook or D-0039; the adversarial-review convention's Routing section
   still says Vertex (retired by D-0020); the cap hook's own docstring says
   *"91 findings"* where TRAP-009, D-0039, the hook README and the retained
   JSON say 88 (counted: 88).
3. **Two corrections from him, both checked at source and both his:**
   - *"About codex, it appears it's written down as if there is an automatic
     review trigger. There isn't, that is something I would have to
     personally enable and I explicitly didn't do that because I don't think
     every PR needs a review."* The boot file's `@codex` bullet, the
     capabilities ledger's 2026-08-29 entry and its 2026-08-07 entry's
     superseded sentence, and the product-forge #49 entry all frame the
     automatic triggers as advertised-but-unreliable. The true statement is
     that they are not enabled, by his choice. Not yet landed — waiting on
     his answer to which PRs a Codex round is owed on.
   - *"About the hook … I thought the hook was just a predetermined question
     that fires without any third party dependance. Please find out what the
     truth is."* He was right about the mechanism. `owner_review.py` blocks
     once per turn with a fixed pair of questions and no model, network or
     key (its own line 120); a Gemini call on the free key is an additive
     enrichment that appends specifics when it answers. This session's two
     firings both logged `HTTPError: HTTP Error 503: Service Unavailable`,
     so both times the fixed text alone fired — the session's earlier
     sentence *"the hook that just questioned me is Gemini"* was wrong and
     was withdrawn. Also stated to him: the reply text does leave the
     container to Google every turn while the key is set, and nothing in
     the tree records him deciding that either way (grepped the decisions
     ledger, the findings record, the hooks README, the hook, the owner
     queue).
4. **Two asks, both delivered in this PR:**
   - *"I notice that the hook makes you send your entire message twice …
     Can you find a way to make sure that you and other sessions don't
     repeat what you already said but instead only write whatever is
     genuinely new or different?"* Cause: the hook's `REASON` text said
     *"address each point IN the reply the owner reads — amend the reply"*,
     written as if a Stop block withheld the message; it does not, so every
     session re-sent the whole reply plus one `[survived]` line. Worse when
     the enrichment fails, because then the second message is 100 %
     repetition. Fix: the `REASON` text now says the owner has already seen
     the reply and asks for only what is new; the boot file's Stop-hook
     bullet says the same. The old sentence survives verbatim in two dated
     audit records under `docs/audits/2026-08-10-full-read/` — quotations of
     the 2026-08-10 boot file, left as the record they are.
   - *"About the hook that is supposed to send your message to Gemini, can
     you find out what's causing the 503?"* Cause, `MEASURED` this hour on
     the live endpoint: Google's free tier is shedding load — body *"This
     model is currently experiencing high demand. Spikes in demand are
     usually temporary"*, status `UNAVAILABLE`, on 3 of 8 calls across two
     model ids and both network routes, each 503 back in 1–6 s and the next
     call succeeding. Not the proxy (the hook uses `ProxyHandler({})`), not
     the key, not the model id. The hook made one attempt with no retry;
     `tools/gemini_delegate.py` has retried this endpoint since 2026-08-05.
     Fix: `_free_review` retries a 503 twice (2 s, then 4 s), logs
     `attempts`, and does not retry a 429. Suite:
     `tools/test_owner_review.py`.

5. **Which PRs owe a Codex round — answered.** His words: *"I think only
   when it's substantial new work or actual coding that this is necessary.
   And I guess aswell during large batches of document restructuring etc. To
   make sure that no important things are forgotten. But this is a tricky
   thing to determine tho, because Claude agents often make mistakes in
   reading and understanding the documents they write about."* The session
   put the measured case to him (fm #1010 was a document; `factual-reversal-core:
   16` counted from the retained JSON) and proposed making the decision a
   property of the diff, read at the flip moment: (1) touches an executable
   or binding surface → one round; (2) a large docs change over a threshold
   → one round; (3) otherwise no Codex — the Gemini pass or a direct check.
   He chose **A** (*"I think I agree"*), adding the expectation, not a
   measurement, that *"once the new repo and everything is properly made …
   these errors will go down aswell since it will be easier for agents to
   read and find the right information."* Lands as an amendment to D-0019
   in this PR; the checker itself is shaped, not built.
6. **The new hook answer style, confirmed:** *"this way of answering the
   hook is a lot more clear to read."*
7. **Item 2 of 6, the model tiers — confirmed with one amendment.** *"Yes
   that's right, tho Fable should only be used when I explicitly request
   it, since Fable uses a lot more usage than the other models, I try to
   only use it when I believe that it would really make a difference."*
   Landed in place: D-0040 carries the amendment; the `fleet-preflight`
   contract sheet's MODELS line now ends `fable: none | <stage> — owner
   asked, in words, for this run`, § 8's table puts the last look on
   `opus` and makes a Fable stage a quoted owner ask.
8. **Item 3 of 6, acknowledging a mid-turn message — refined.** Not an
   interrupt: *"once it's done or in between steps I'd like some
   acknowledgement so I know my message came through properly. Just like at
   session start … I'd like to know how you understood my message."* His
   words and the refined reading are in
   `docs/findings/2026-09-02-owner-direction.md` § 3 (record grown in
   place). Whether a mid-turn message passes through `UserPromptSubmit`
   stays the probe that decides if a hook can deliver it; the recipe is one
   trigger phrase sent while a command runs, and the routing hook's note
   arriving with the message is the positive result. **Run, same sitting,
   n = 2: negative.** Both of his mid-turn messages arrived bare with the
   harness's own notice and no route block; the `repo-websites-prompt`
   route had never fired (route state read); the positive control is his
   first message of the session, which did carry a `UserPromptSubmit`
   block. Recorded as a dated wall in `docs/CAPABILITIES.md` with the
   workaround candidates (the harness notice; a `Stop`-hook check).
10. **Item 4 of 6, stopping agents — confirmed, with the two-tier form.**
   *"Yes that's right, unless I would say something like 'stop all your
   agents' but then usually I would hit the stop button myself."* Landed in
   `docs/findings/2026-09-02-owner-direction.md` § 2 (record grown in
   place): "finish current, start none" lets anything already started
   finish, runtime-started included; "stop all" is the stop button.
11. **Item 5 of 6, the mail — amended.** *"Yes that's mostly it tho I would
   like a proper draft created which I can read and edit … your
   continuation prompt will be for the email session … it's also important
   that we discuss what the email should contain. After we are done with
   the rest of the topics."* Landed as § 5b of
   `docs/findings/2026-09-02-owner-direction.md` and a dated pointer at the
   top of the report's § 10. The sitting's close is redirected: item 6, the
   OPEN items, then the mail's contents with him, then a continuation
   prompt for the mail session.
12. **Item 6 of 6, one place per fact — confirmed** (*"Yes I think that's a
   good rule to have"*); the checker decision is the 💡 below, taken by the
   session at his ask.
13. **The cap's exit and the Gemini add-on — both decided.** *"What's your
   opinions on these? has the gemini add on ever fired as far as you know?
   And what would be the most efficient and correct way to handle the codex
   review exit?"* Answered from the hook's log (20 firings this session: 10
   skipped as too short, 2 enriched, 5 × 503, 3 × 429) and two live probes
   — the 429 is the free tier's per-day, per-model cap on
   `gemini-3.8-flash`, what `gemini-flash-latest` resolved to, while
   `gemini-3.5-flash-lite` and `gemini-3.6-flash` still answered. His
   answer: *"Yes I agree, make the gemini route to a lite model with higher
   caps. All agreed."* Landed: `FREE_MODEL = "gemini-3.5-flash-lite"` in the
   hook (suite pins it), the exit as recommended in D-0039 (amended in
   place), the which-PRs-owe-a-round tiers in D-0019 (amended in place), the
   auto-trigger correction in the boot file's `@codex` bullet and as a new
   ledger line, and the three drifts: `session-close` step 6c now names the
   hook and D-0039; the adversarial-review convention's Routing section
   carries a D-0020 supersession note; the cap hook's docstring says 88.
14. **The time after — Projects versus sessions, and the mail's contents.**
   He asked for a proper answer to Anthropic's question (*"what would make
   me choose a Project over a regular claude code session"*), corrected the
   session twice (the instruction box was a real delivery tier, not the
   weakest — checked against the v3 registry and the retrospective; and the
   workers refused the coordinator as *"an untrusted source"*, matching the
   2026-07-12 ledger wall — the session had swapped the cause), answered
   six guiding questions and six more an Anthropic reader would ask, all
   verbatim in `docs/findings/2026-09-02-owner-direction.md` § 5c–5d with
   the DERIVED answer beneath them. The four sent July mails and two unsent
   drafts were read from superbot over the direct API and mapped against
   the planned mail: the outcome findings, the outside review, asks 1, 2, 4,
   5, the instruction box, the honest-queue ask and the false-done rows are
   new; three of the four "Project fixes" and the coordinator-continuous
   ask were sent in July and become pointer lines. The instruction box was
   sorted into defaults / scaffolding / seat-specific from one v3.8 paste.
   *"ultracode"* in one of his answers was read by the harness as an
   opt-in and the workflow reference loaded itself; not acted on — the
   second such misread in two days, now in the mail prompt's lessons.
15. **The close, at his direction:** the continuation prompt is for the
   mail session — `docs/prompts/2026-09-02-eap-mail-session.md` (preflight
   at HEAD: the draft's 1,686 words and loss-free render from its own tool;
   Gmail draft creation offered but unmeasured, left as that session's
   first step); listed in `docs/prompts/README.md`; the program's NOW
   pointer moved to E1 on his words (*"your continuation prompt will be
   for the email session"*), the kit records step demoted to "behind it".
   The mail's shape (A, false-done in, Part 1 drafted, ~2,100 words) went
   to him as four letters and was not answered in a word — the prompt
   carries the length as its LEAST SURE line.
16. **His words may be corrected for spelling** (owner, live, after seeing
   his typos quoted into the record): landed as the typo entry of
   2026-09-02 in `docs/decisions.md` and § 3b of the owner-direction
   record; the tree held no earlier statement of it.
17. **Codex round 1 on this PR (`b8ff610`): 10 findings, 2 P1, 8 P2 — all
   real, all fixed on the next head.** P1: the new prompt's
   `owner-guidance` badge put it in the owner index as *historical* and
   `gen_owner_index.py --check` failed — badge set to `reference`, its
   sibling prompt's choice (fixed differently from the suggested
   exception; check exit 0). P1: five `stamp` findings from the strict gate
   — decision ids cited from more than one doc under `docs/` (the check
   counts any `D-NNNN`, bracketed or not, outside the ledger) — every id
   the diff added outside `docs/decisions.md` is now a prose name
   ("the cap entry of 2026-09-02"). P2s: the review-cadence entry's tier 3
   "a ledger line" now says *capabilities*-ledger and tier 1 keeps the
   decisions ledger; the flip-commit exemption is stated in both amended
   entries, reconciling "flip on an answered verdict" with "one commit
   past it"; the model-tier entry's heading now matches its amended rule;
   exhausted retries log `attempts` (pinned on the raised error) with a
   `main()`-level suite case; **the claim that the review hook was spending
   the verification pass's quota was false** — `gemini-flash-latest`
   resolved to `gemini-3.8-flash`, the verification model is
   `gemini-3.6-flash`, and the measurement itself showed the latter still
   answering; corrected in the hook comment, the hooks README, the cap
   entry, the mail prompt and this card's item 13 (which said "the budget
   the flip-time check needs" — it did not); review-quality parity on the
   lite model marked UNMEASURED (the 2026-08-08 comparison was
   flash-latest vs Vertex Pro); the close skill's severity table gained a
   round-three row; and the mail prompt's shape/false-done/Part 1/length
   package moved from DECIDED to OPEN, since he never answered it in a word.
9. **Pre-existing, not this PR's, noted for the record:**
   `python3 tools/test_change_guard.py` exits 1 on `origin/main` as well as
   on this branch (15/16; the failing case is *"real historical defect still
   caught (6 rows) [silent, wanted fire]"*). It is not in the gate's
   fan-out, so CI does not see it. Left alone in a review sitting; named
   here so the next session that touches `change_guard.py` starts from it.

## Verify

`python3 bootstrap.py check --strict` — run before the flip; only the
born-red hold red. `python3 tools/test_owner_review.py` — the executable
prints its own case count. The pipe-tests in `.claude/hooks/README.md`
§ owner-review (`stop_hook_active` → exit 0, empty).

⚑ decide-and-flag: **which PRs owe a Codex round.** His sentence *"I don't
think every PR needs a review"* says not every one; the tree never draws the
line, and today's records-only fm #1012 ran all three. Put to him as one
question; his answer lands in D-0019 in place.

💡 Session idea: **the one-place-per-fact checker, narrowed to what a script
can decide** (owner confirmed the rule, item 6: *"Yes I think that's a good
rule to have"*; asked for the session's decision on the checker, since
*"I'm not yet that technical that I see myself as the right fit to make
these decisions on my own"*). Not the general form — a checker over prose
cannot tell a claim from a quotation of it (`docs/conventions/adversarial-review.md`
§ the permanent false positive). The buildable form: over a PR's **added
lines only**, a number with its label (`88 findings`, `17 rounds`, `204
agents`, `335 s`) that appears in two or more files of the same diff is
reported once per number with the files. Acceptance before it may go red:
**fires on fm #1010's diff** (the known positive — the round tally in six
places), **silent on a records-only PR** with one card and one ledger line
(the known negative), and advisory for its first ten PRs so the
false-positive rate is measured, not assumed. Home when built: the
`check --strict` fan-out beside `check_no_false_walls.py`. For a build
session after the mail session; not this sitting.

💡 Session idea (second): **the owes-a-round verdict, computed from the
diff** ([D-0019] as amended 2026-09-02). Input: `git diff --name-status
origin/main...HEAD` plus added-line counts. Rule: any path under
`.claude/hooks/`, `.claude/skills/`, `.claude/settings.json`, `tools/`,
`scripts/`, `.github/workflows/`, `bootstrap.py`, `.claude/CLAUDE.md`,
`docs/decisions.md` or `docs/traps.md` → *owes a round, because <path>*;
else more than five files or two hundred added lines under `docs/` → *owes
a round, large docs change (<n> files, <m> lines)*; else → *no Codex round:
direct check or Gemini pass*. Printed by the `card-flip-to-complete` route
at the flip moment (the route exists; the verdict is the addition), or as a
standalone `tools/codex_round_owed.py` the session-close skill names.
Acceptance: says *owes* on fm #1011 (hook) and fm #1010 (a 931-line report
plus scripts), says *no round* on a one-card, one-ledger-line PR. Same build
session as the checker above.

⟲ Previous-session review: the landing session (fm #1011, fm #1012) left a
continuation prompt that was accurate at HEAD to the commit and named its
own three mistakes; the only state it could not know was that fm #1012 had
merged by the time this session read it, which the prompt itself said to
check.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached this
session).
