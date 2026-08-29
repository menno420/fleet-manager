# 2026-08-29 — the initiative-loop design, captured while it was still warm

> **Status:** `in-progress` — born-red. The design conversation converged in
> the live sitting (*"Yes I agree with your suggestions"*), and per the
> decision-capture rule — explaining it twice costs more than committing it
> once — this PR lands it before the next session has to re-carry it.

- **📊 Model:** withheld · max · docs-only
- **⚑ Model-slot note:** harness policy forbids a model identifier in a
  pushed artifact; effort and task class are exact.
- **📍 Venue:** cloud-container (owner-live)

## Mission

Third records PR of the sitting (after the directive capture and the
review-round consumption), under the same carve-out — which this PR also
finally writes down as [D-0022]. Captured:

- **`docs/planning/2026-08-29-initiative-loop-design.md`** — the owner's
  initiative-loop design with his verbatim quotes: engineered end-of-session
  output (hook → skill → detectors → dispositions), tier (c) building,
  consumption through `continuation-prompt`, the queue's one home, the
  retirement rule, the falsifiable reds, what stays open, S1–S4 slices.
- **[D-0021]** — the design decision, owner-directive labelled.
- **[D-0022]** — the planning-hold carve-out from earlier tonight, which two
  merged PRs already exercised before it existed anywhere but chat.
- Index row in `docs/planning/README.md`.

## Choices worth one line each

- **Routing beats building, found in the act of writing it:** the "one queue
  home" improvement nearly specified a new file; the planning README's own
  index shows `idea-backlog.md` + `scripts/gen_idea_backlog.py` already
  exist, and the script (read, line 70) harvests only the `- 💡` bullet
  form. The design now says extend the harvester, not invent a surface.
- **Denominator earned before use:** the "382 of 449 cards carry the heading
  form" figure was measured this session (`grep -l '💡 Session idea'`) after
  the review hook caught it being asserted on a borrowed 441.
- **What was deliberately NOT captured** (decision-capture step 5): the
  review-cadence amendment question — asked, unanswered, still open; and
  everything in S1–S4, which is named for the plan's implementation
  sessions, not started (OD-26 §13/§14).

## ⚠ Near-miss: the capture "merged" before it was ever pushed

The first landing attempt failed in a way worth its whole record:

1. **The session was on a detached HEAD and its pushes were no-ops.** A stray
   `git checkout -q origin/main --` inside an earlier compound command
   detached HEAD, so the capture commits landed on no branch; every
   subsequent `git push -u origin <branch>` then pushed the *stale local
   branch ref* — still at the fm #982 head — and reported "Everything
   up-to-date", which a `| tail -1` reduced to the tracking line. The push
   looked successful, was technically successful, and moved nothing. (First
   written up here as a non-fast-forward rejection — wrong mechanism,
   corrected by measuring: `git branch --show-current` came back empty and
   the fix-context hook addressed the branch as `HEAD`. Two lessons, both
   instrument-class: never truncate a push's output, and after any push that
   matters verify `git ls-remote` against `git rev-parse HEAD` — the pair
   that actually caught this.)
2. **A PR was then created against the stale head** — content already on
   `main` — and the merge-on-green lander merged it at `22:48:08Z` on the
   old head's still-green checks: **fm #983 is a merged PR whose title
   claims a capture its diff does not contain** (tree-identical merge;
   `main` unchanged). The estate's "PR did not do what its title claimed"
   class, produced this time by infrastructure rather than prose.
3. **A Codex round was requested against that head** and ran on a
   merged-empty PR — one wasted round, the exact waste the cadence decision
   exists to avoid.

Detection: the Codex Running summary named the *old* SHA, which did not
match the pushed commit — the mismatch was the alarm. This PR (the
successor) carries the actual capture; fm #983's thread gets one comment
saying so.

## Verify

- `python3 bootstrap.py check --strict` → real exit code, no pipe; born-red
  on this card until the flip.
- One instrument divergence, cause `UNVERIFIED`: CI's substrate-gate fired
  `[stamp]` on this doc's bare decision-token example (correctly — two
  citing homes) while the local strict run on the same content surfaced
  only the born-red hold. Fixed by de-tokenizing the example either way;
  the divergence itself is left as a recorded observation, not a diagnosis.
- One Codex round at flip-readiness (ledger + planning-surface changes
  matter); fixes, if any, verified on the free-key Gemini route.

## ⟲ Previous-session review

Previous card:
[`2026-08-29-lane-denominator-fix.md`](2026-08-29-lane-denominator-fix.md)
(a genuinely different conversation — read whole). **Held up:** its central
lesson — *"verifying a quote is not verifying the sentence containing it"* —
fired twice in this very session before this card was written: once when a
borrowed 441 nearly shipped as the idea-section count, once when the
harvester's behaviour was nearly described from an index row instead of the
script. Its declined-review reasoning (two-integer correction, precedent
stated) also reads as an honest early data point for the cadence question
this sitting put to the owner. **What it left implicit:** its 💡 idea
(mark borrowed figures inline) overlaps detector 1 of tonight's design —
the contradiction/borrowed-claim sniff — which is where that idea would
naturally get its corpus test.

## 💡 Session idea

**The design's consumption check applies to its own capture chain.** Three
records PRs landed tonight, each carrying a 💡 section — and under the
current harvester none of them will appear in the generated backlog, because
all three use the heading form its regex skips. S1 (extend the harvester) is
therefore self-testing: run it on this very sitting's cards and the queue
should gain exactly the ideas the design was derived from. A first-use test
that ships inside the thing it tests, per the design's own birth rule.
