# 2026-08-07 · hub — the gift repo stopped being a seat and became a gift

> **Status:** `complete`

- **📊 Model:** opus-5 · high · feature build

Time: 2026-08-07 · venue: owner-live chat (curious-research session, fleet-manager
attached mid-session) · branch `claude/curious-research-handover-note`

💡 Session idea: I wrote two inferences as facts about a person's workshop, and both
times the inference **made my own work look more necessary than it was**. The owner
caught both. That is the finding worth carrying back here, more than any of the code.

## What the session did

In `curious-research` (PRs #53–#65, all merged): removed the autonomous-fleet
machinery (−41,399 lines), rebuilt `substrate-gate` as a relative-link checker while
keeping its required name, shipped a live website, and added guides for the things the
maker actually asked for. Full account:
[`docs/findings/2026-08-07-curious-research-handover.md`](../docs/findings/2026-08-07-curious-research-handover.md).

Here: that findings file, plus a `historical` status warning on
`projects/curious-research/meta.md`, whose archetype line still described a kit-run
seat with a heartbeat in `control/status.md` — machinery that no longer exists.

## The error, twice, in one shape

1. I read an Amazon listing for the maker's arm kit, saw servos and brackets and no
   controller, and wrote **"NOT included: no controller board, no power supply, no
   wiring"** into the repo. Then planned a *"how to power your arm"* guide with a
   shopping list. Video showed an enclosed switching supply, a distribution board, and
   the arm sweeping under program control. He had solved it months before the repo
   mentioned power at all.
2. Having recorded that, I still shipped copy to the **live site** reading *"voordat de
   arm ook maar één keer beweegt"* and *"de software weigert elke beweging"*. His arm
   moves. What was true is only that **curious-research's own tool** refuses to start
   without a calibration file. I collapsed "our tool will not run" into "your machine
   does not work".

Neither was caught by verification. Both were caught by the owner.

**The shape:** the inference that makes the repo more important and the person less
capable is the one that slips through, because nothing in the session pushes back on
it. It is not a knowledge gap — I had the video before I shipped (2).

`curious-research/CLAUDE.md` §0 now carries this as a standing rule with the example.
I think it generalises: any fleet doc that asserts something about a person's setup or
another repo's state is exposed to the same failure, and the tell is that the claim
flatters the asserting party.

## Two capability findings — appended to the ledger, not restated here

Both went into `docs/CAPABILITIES.md` as dated entries, which is where they belong and
where the staleness rule can age them: a workflow token cannot **create** a GitHub Pages
site (only deploy to one), and PRs merging on curious-research fired **no** push-triggered
workflow runs, so its publishing workflow silently never ran.

The second entry is written with the measurement and the explanation **separated on
purpose**. I measured the effect — zero `pages` runs across five merges, green checks
throughout. The `GITHUB_TOKEN`-suppression mechanism is best-fit and I did not confirm it:
I never checked whether `ROUTINE_PAT` exists, nor which actor performed each merge. Given
what this session got wrong twice already, stating that cause as fact would have been the
same mistake a third time.

## Open, flagged not fixed

- `projects/curious-research/{coordinator,failsafe,instructions}` are GENERATED copies
  describing a seat that no longer exists. Regenerating or retiring them belongs to
  consolidation step D4 — editing generated files in place is how drift gets baked in.
- `docs/CAPABILITIES.md` frames a proxy 403 as a false wall to route around with
  `--noproxy '*'`. Correct about GitHub's permissions, wrong about what the proxy is,
  and it leaves a session that declines the bypass with no documented alternative —
  when the MCP GitHub tools served every operation needed today. Reasoning in § 6 of
  the findings file, marked as opinion.

## ⟲ Previous-session review

The newest card here (`2026-08-06-free-on-cost-global-in-scope`) records verifying
what a mechanism *does* while assuming what it *applies to* — a claim checked on
cost and unchecked on scope.

Mine is the same cut, one layer out. I verified a **listing** (the arm kit ships
servos and brackets) and assumed the **bench** (therefore he has no controller or
supply). Correct about the box, wrong about the workshop — and the gap was fillable
the whole time, by asking, which is what eventually resolved it.

That card's author was corrected by another agent. I was corrected by the owner,
twice, and in both cases the check that would have caught it was available before I
shipped. So this is not a new class — it is the same one, with the added twist that
**the wrong version was the flattering one.** Worth watching whether that bias shows
up in the other direction anywhere, or only where the asserting party benefits.

## Left running

Twelve deep-research runs (six prompts × ChatGPT + Gemini). Results land in
`curious-research/research/dossiers/`, then get cut into Dutch cards on the site.
Then the owner's introduction email with a Claude subscription.
