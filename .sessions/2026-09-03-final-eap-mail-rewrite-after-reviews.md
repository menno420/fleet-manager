# 2026-09-03 — the final EAP mail rewritten once more, from the owner's own edits and an independent review

> **Status:** `complete` — the owner's pull request (fm #1019, branch
> `owner-edits`) carried his rewrite of Part 1 and comments on Part 2;
> ChatGPT Work reviewed the mail cold the same evening; this session took
> both in, rewrote both parts on his branch and restaged the Gmail draft.
> **He reads it again before anything is sent** — his words, mid-turn: *"I
> won't just send the corrected mail at once. First I will read it again and
> see if there are any additions I should make."* Codex: two rounds — 3
> findings, all fixed; round two clean ("Didn't find any major issues",
> reviewed commit `8b7e2fb`, 21:28:55Z). **Reviewed SHA `8b7e2fb`. After
> it:** this flip commit only — the badge and the close-out text, the one
> exempt commit. Landed on green.

- **📊 Model:** withheld · xhigh · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01FYmmtAxtUAuXyAhWpejVYK](https://claude.ai/code/session_01FYmmtAxtUAuXyAhWpejVYK) · "Final EAP mail draft" (the same session as `.sessions/2026-09-03-final-eap-mail-draft.md`, continued after fm #1017 merged; a second PR because the owner opened it — the stated exception, [D-0024])

**Why a second card:** fm #1017's card is complete and merged; this is the
owner's PR, and the estate records every landing.

## What was done

- **Read first:** his diff on `owner-edits` (`0f3b68e`, two files: the mail
  and the merged card's Model line, which he changed to a model name himself
  — left as his edit); ChatGPT Work's review as pasted (sections A–I, one
  "one thing to change"); every source line the reviewer cited, opened at the
  line (`2026-08-12-intent-map-fresh-agent-test.md` § 1, `why-rules-dont-bind`
  :40–70 and :235–246, the full-read audit :56–80 and :112–129,
  `CAPABILITIES.md` :597–617, `eap-retrospective.md` :200–214, owner-direction
  :240–257, :293–310, :153–158, night review :715–730, the correspondence
  record :154–161, the superbot consolidated findings :240–262).
- **Part 1** is now his: his new paragraphs (purpose, the sessions-first
  reason, the errors-and-root-cause paragraph, the "time was due" sentence,
  the fleet-manager-will-retire clause, the one-feature ask, the interviews
  line) kept in his words, lightly tightened under [D-0041]; the pairs where
  the change is more than spelling:
  - his *"Tho not all of this is directly about the Projects itself, I do
    believe that this is relevant because especially during autonomous runs
    as the Projects were advertised; I believe that preventing errors…"* →
    *"Not all of that is directly about the Projects themselves, but I
    believe it is relevant: the Projects were advertised for autonomous runs,
    and preventing errors…"*
  - his *"Something that also took up a lot of my time during the recent
    week to search for and correct the errors and wrong assumptions that
    were made. This is something that I'm stil working on."* → *"Searching
    for and correcting the errors and wrong assumptions has taken up a lot
    of my time in recent weeks, and I am still working on it."*
  - his *"I felt like the time was really due to send this email sooner
    rather than later since you mentioned that these Projects would possibly
    become available to the public soon. I wanted to send it much sooner but
    I did feel like it was better to look for the root cause…"* → one
    sentence with the order reversed (root cause first, then "the time was
    due"); meaning unchanged, the vendor-plan clause kept and flagged (§ 2,
    *public-soon*).
  - his verdict sentence kept as he wrote it; "I might use them, but not as
    true autonomous agents" added from his 2 September answer 1 (the
    reviewer's one change: his own conditions instead of the derived thesis).
  - his unfinished *"…given me some more insight in what you wish to know
    from me. I"* → *"…gave me more insight into what you want to know from
    me."*
  Voice findings applied where his edit had not already answered them: the
  opening's "late on purpose" / "fifth list of complaints" gone (his own new
  paragraphs replace them); "But the functionality was not what I intended,
  so it was not ready to use"; "mostly started after the classifier update";
  the narrower "what I kept" (websites and fleet-manager not what he hoped;
  venture-lab parts valuable; the kit in use); the gift sentence as what he
  had said. Removed by him and respected: the permissions one-fix paragraph,
  "a couple of hours a day", "the complete record for both of us". Removed
  by the reviewer's finding: the derived thesis sentence. Part 1: 696 words.
- **Part 2**, his three comments: ask 1 names the custom instructions as the
  closest thing to rules arriving at the moment of action; ask 5 is now his
  ("an agent that can see its own context limit" — the hosting-store example
  out as not relevant, his correction that agents can already see usage and
  cost); "the shared working agreement" → "the custom instructions". The
  reviewer's evidence corrections, each checked at the cited line: the
  blind-scored evaluation described as what it tested; "can survive" a
  review; "far more likely to bind" for "only if"; "tests and self-checks"
  for "test runs"; "caught the false-dones in these reviews" for "reliably";
  Finding 3's three-later-counts parenthetical compressed to one sentence;
  "The reports and methods are public" for "Everything above is public".
- **Addendum**, his words restored: "basically the same capability … tho not
  exactly the same"; "mostly found stalls"; "possible only because usage was
  unlimited; fewer would probably have been better"; the task qualification
  (ideas, the kit) and "immensely valuable" if it can continue indefinitely;
  "did not ensure" judgement for "could not carry"; "about 81 %" for a second
  949; "no exceptions" out of quotation marks; "publicly readable when
  checked" for "the whole time"; the instruction-box default argument and
  its source bullet cut (the reviewer's first trim, and an editorial claim).
  Survived: the Projects-overview ask stays in Part 1 by his 2 September
  choice; the two linked files the reviewer flagged for confidentiality are
  existing public records, no new disclosure.
- **Figures:** block **2,299 words** (`--count`), Part 1 696, addendum 488 +
  75 source bullets, 30 bold + 13 italic (one italic restored so the
  2026-08-25 card's guarded figure stays true), `--verify` loss-free,
  `--selftest` 13/13, `check_eap_figures.py` clean — after one more tool
  touch: its links-block anchor string (`"Everything above is public"`)
  renamed with the mail's closing line, or it crashed. Five consumers moved
  2,322 → 2,299; the #1017 ledger row and card keep their own 2,322.
- **A correction to what this session told him earlier:** the figure checker
  IS in CI — `scripts/repo_checks.sh` runs it inside `substrate-gate` — which
  the earlier grep of `scripts/preflight.py`, `bootstrap.py` and the
  workflow files did not cover. His PR went red on exactly that: his three
  `##` comment lines sat inside the COPY block and counted as mail words.
  Said to him in chat; recorded here.
- **Gmail:** the draft restaged from the rewritten file (plain + HTML), same
  draft id, message id `1a0691cd821da775`; no recipients. He reads it again
  before anything is sent.
- **Landing:** four session commits on his branch (`7b1fc8b` the rewrite,
  `8b3ae5c` and `9c1d984` records — two record scripts stopped at wrapped
  anchors and the shell pushed the partial sets, which is why there are
  three record commits — `66ce999` the rest and this card).
- **Codex round 1** on `66ce999` (requested 21:12:52Z, review 21:19:25Z):
  **3 findings, all P2, 3 conceded, 0 survived** — the custom-instructions
  praise overstated what was automatic (scoped: pasted once per Project,
  delivered to every agent that Project spawned; the paste and the re-paste
  after a reset were his — `docs/prompts/v3/README.md:18-26`, owner-direction
  :330-333); the owner-queue WHAT, current-state and the program NOW block
  still told him to rewrite Part 1 (now: re-read, additions, the one-word
  calls, recipients, send); the edit pairs promised by the draft were not yet
  in the pushed card (they are above). Block 2,279 → 2,299 with the scoped
  sentence; guarded consumers moved; `--verify` loss-free; checker clean.
- **Codex round 2** on `8b7e2fb` (requested 21:25:34Z, verdict 21:28:55Z):
  **clean** — "Didn't find any major issues", reviewed commit `8b7e2fb0de`.
  No third round needed. **Tally: 3 findings, 3 conceded, 0 survived.**

## 💡 Session idea

**A record-edit script that refuses to push if any of its edits failed.**
Three times this evening a Python edit script asserted on a wrapped anchor
and the shell line after it committed and pushed whatever had been written
so far, producing commit messages that named files the commit did not
touch. The fix is one line: `python3 edits.py && git commit …` instead of
`;`, or a `set -e` at the top of the block — and the estate's own
`check_pipe_exit_code` idea generalises to it: a compound command that
continues past a failed step is the same defect as `$?` after a pipe. Worth
having because the false commit message is exactly a false-done in
miniature, produced by the session writing about false-dones.

## ⟲ Previous-session review

`.sessions/2026-09-03-final-eap-mail-draft.md` (this session's first card, fm
#1017) did what the prompt asked and its § 2 one-word calls are what made the
owner's edit and the reviewer's pass cheap to fold in — every change tonight
maps to a call or a finding, not to a re-argument. Its miss was the CI claim:
it grepped three places for the figure checker and told the owner his push
could not go red on it, when `scripts/repo_checks.sh` was the fourth place.
The lesson is the estate's own: a negative from a grep is a claim about the
grep, and the gate's list lives in one script, not in prose.
