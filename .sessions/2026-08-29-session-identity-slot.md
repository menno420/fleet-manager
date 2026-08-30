# 2026-08-29 — the card learns which conversation wrote it

> **Status:** `complete` — owner directive, live, minutes before the PR:
> *"Yes we should make it required with an honest null, and this is one of
> the exceptions that should happen immediately. Because it's a small fix
> that benefits us right away."* Landed under [D-0022]'s carve-out at his
> explicit word. Flipped after the flip-readiness round answered (review
> object on `507c612`) and all three findings were fixed and
> Gemini-verified — the checker hardened, both authoring-time delivery
> surfaces updated, and the refuted squash rationale narrowed.

- **📊 Model:** withheld · max · runtime bugfix
- **⚑ Model-slot note:** harness policy forbids a model identifier in a
  pushed artifact; effort and task class are exact.
- **📍 Venue:** cloud-container (owner-live)
- **🔗 Session:** [session_01D2EKd9GfuiWbyuNmCDisLk](https://claude.ai/code/session_01D2EKd9GfuiWbyuNmCDisLk) · "2026-08-28/29 audits and fleet-preflight review"

## Mission

The owner asked whether a card could carry its own session's name, so a card
can be traced back to the conversation that wrote it — and the mechanism was
proven in the same sitting: `get_session` (no argument) returned this
session's own id and title from inside the container, across an MCP
reconnect he screenshotted. The line above is the first card wearing it.

Shipped:

- `.sessions/README.md` § 🔗 Session — the grammar: required on added cards,
  id-as-URL plus title-as-search-hint, the single literal honest-null token
  `unavailable` (+ one line why), never invent, never inherit, no backfill.
- `scripts/preflight.py` — the session-line check on ADDED cards, riding the
  existing `added_cards()` selection; local `check --strict` and CI's
  substrate-gate run the same script, so one edit covers both predicates.
- `docs/decisions.md` **[D-0023]** — his words verbatim, enforcement and
  citing home named.
- `docs/CAPABILITIES.md` — the capability half: a session can read its own
  identity from inside.

## Why the card and not the commit trailer

Every commit here already ends with a `Claude-Session:` URL — and fm #977's
card measured that this repo's squash-merge discards the commit body, so the
trailer never reaches `main`. The card is the artifact that survives the
merge. The trailer stays (harness-mandated); the card line is the durable
copy.

## Verify

- **The checker's red, seen at birth** (the first-use rule [D-0021]
  captured an hour before this): `missing_session_line` was exercised
  directly on this very card — with the line present it returns `[]`; with
  the line temporarily stripped it returns the card; restored, `[]` again.
  The regex ran a six-case suite first (id+URL, bare id, the literal null —
  all match; missing line, an invented token, a prose-phrased null — all
  correctly red). Known-positive and known-negative both exercised before
  push; the full-script path is what CI runs on this same PR.
- **And an unprompted first fire on real data:** the first full gate run
  redded `session-line (.sessions/2026-08-29-initiative-loop-capture.md)` —
  that merged, line-less card still read as ADDED because this branch sat on
  pre-merge history; the standard branch restart cleared it. Correct
  behavior under its selection rule, seen live before the PR existed.
- `python3 bootstrap.py check --strict` → real exit code, no pipe; born-red
  on this card until the flip.
- One flip-readiness Codex round (checker + grammar change matters); fixes,
  if any, verified on the free-key Gemini route per [D-0019].

## ⚖ Flip-readiness review (Codex on `507c612`, per [D-0019])

Answered `00:16:54Z` as a review object. Three P2 findings, all measured,
all real, all **[conceded]**:

1. **The regex was substring-loose.** `unavailable-ish`, prose-wrapped ids,
   non-Claude URLs and a fenced body example all passed (four attack cases
   confirmed before fixing). Hardened to full-match the two canonical forms
   — backreferenced id-in-URL + quoted title, or `unavailable — <reason>` —
   scanned only in the header block (above the first `## `). Nine-case
   suite + strip/restore + line-only-in-body integration all green.
2. **The requirement wasn't delivered at authoring time** — the estate's
   own delivery-gap thesis, pointed back at this PR: the session-card
   doc-route injected only the venue text, and session-close's born-red
   step named no session line. Both updated; the kit-named skill amendment
   is registered in `docs/SKILLS-local.md`'s ⚠ re-apply table (the
   PreToolUse hook caught the upgrade-revert trap at edit time). The kit's
   auto-draft skeleton still lacks the slot — said honestly in the grammar;
   a drafted card already counts incomplete.
3. **The squash rationale was refuted forty lines above my own edit.** The
   `withheld` section's count blockquote records 341 trailer-carrying
   commits of 993 on `main` and calls the general "squash discards
   everything" reading a shallow-clone artifact — I had read that paragraph
   this sitting and still carried the stale claim from fm #977's card past
   it. Narrowed everywhere it appeared (grammar, ledger why-block, PR
   body): specific squashed PRs lost their bodies; the card survives
   regardless of merge style. The sharpest catch of the round — a
   borrowed claim surviving adjacent to its own refutation.

Fix diff verified on the free-key route (three RESOLVED, no new issues)
before this flip.

## ⟲ Previous-session review

Previous card:
[`2026-08-29-audit-catalogue-export.md`](2026-08-29-audit-catalogue-export.md)
(fm #973, a genuinely different conversation — read whole). **Held up:**
13 findings over two rounds, all measured before disposition, zero argued;
its Correction section models the discipline this estate wants — it
re-opened its own flattering claim ("no lens caught it") against the
verdicts and wrote the less flattering truth over it. **Its sharpest shape
is tonight's most-repeated lesson:** five of its six round-2 findings were
created by round 1's own fix prose — "text I generate faster than I verify
it" — the same overreach class as this session's conflated 382 baseline.
**What it left for the queue:** its 💡 (a close-time check for unreferenced
fan-out output) is heading-form and therefore invisible to the current
harvester — a live example of why [D-0021]'s S1 extends it.

## 💡 Session idea

**The session line makes the activity index joinable to live conversations.**
`docs/activity/` indexes what ran estate-wide; with [D-0023] every new card
carries a conversation URL, so a future `estate_activity` refresh could link
each card row to the session that produced it — turning "which session do I
ask about this?" from memory into a lookup. Cheap once the line exists;
worthless to build before cards carry it. One for the queue, not for
tonight.
