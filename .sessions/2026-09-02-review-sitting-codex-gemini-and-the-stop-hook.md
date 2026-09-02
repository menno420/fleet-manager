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

## Verify

`python3 bootstrap.py check --strict` — run before the flip; only the
born-red hold red. `python3 tools/test_owner_review.py` — the executable
prints its own case count. The pipe-tests in `.claude/hooks/README.md`
§ owner-review (`stop_hook_active` → exit 0, empty).

⚑ decide-and-flag: **which PRs owe a Codex round.** His sentence *"I don't
think every PR needs a review"* says not every one; the tree never draws the
line, and today's records-only fm #1012 ran all three. Put to him as one
question; his answer lands in D-0019 in place.

💡 Session idea: none yet.

⟲ Previous-session review: the landing session (fm #1011, fm #1012) left a
continuation prompt that was accurate at HEAD to the commit and named its
own three mistakes; the only state it could not know was that fm #1012 had
merged by the time this session read it, which the prompt itself said to
check.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached this
session).
