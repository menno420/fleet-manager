# The owner's direction, 2026-08-22 — captured verbatim

> **Status:** `reference` · his words from one live hub session, committed because
> they existed nowhere else.
>
> **Why this file:** four of the statements below set direction for work that has
> not started, and two of them (OD-17, OD-18) became directives. The rest are
> product and capability asks with no home yet. A directive that lives only in a
> chat transcript is not in the repo — this repo's own read path lost the
> agent-operating-environment roadmap that way for two weeks.
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
> Everything quoted is `OWNER`; everything unquoted is `DERIVED` and marked.

## 1 · The repo pass — became OD-17 and OD-18

`OWNER`:

> "I think something that we should do today is some final verification and
> reviews of the reos, making sure the important ones are kept and
> improved/merged, and the others are either archived or deleted. I think we
> should really focus on cleaning up excessive repos and documentation where
> possible while still making it easy for an agent to understand work."

And, sharpening the ask a few hours later:

> "review the remaining repos to finalize the plan, which set of repos to keep
> eventually and should they start fresh or just be reworked etc"

`DERIVED`, and it is the part worth carrying: **the second quote adds an axis the
program never had.** Track R has only ever asked keep-vs-archive. *"Start fresh
or just be reworked"* is a third disposition, and the estate has already answered
it once — for the Discord bot, in favour of fresh
([the 2026-08-21 plan](../planning/2026-08-21-game-community-bot/README.md)),
on grounds of live coupling, accidental product scope, and parity that was never
porting. That reasoning is a **precedent to test each repo against**, not a rule
to apply to all of them.

`DERIVED` on the tension in the first quote: *cleaning up* and *keeping it easy
for an agent to understand* pull against each other only if you cut by volume.
Cut by **tier** instead — [`MAP.md`](../MAP.md)'s CORE / TASK / RECORD — and they
are the same goal.

## 2 · The EAP email, and a website ask that is new

`OWNER`:

> "later today or possible tomorrow, I want to start and finish writing the final
> mail for anthropic and really finalize our EAP testing work. which also means
> we should improve the website for it too where possible"

Two things here, and only one of them is in the repo.

- **The email is E1**, owner-reserved by his own ruling; no session drafts or
  sends it (`OQ-E1-FINAL-EAP-EMAIL`). What is new is only the timing — *today or
  tomorrow*, after months of deferral.
- **"improve the website for it too" is a NEW ask with no record anywhere.**
  `DERIVED` on what it likely means: the email's strongest section, per
  [`owner-reflection-2026-07-21.md`](../owner-reflection-2026-07-21.md), is the
  *"what I had to build myself"* teardown — his substrate, journals, routines and
  status site mapped to product gaps. The websites estate is the visible half of
  that claim, so improving it makes the email's central argument demonstrable
  rather than asserted. **This is inference. Ask him which surface he means
  before building anything** — control-plane, dashboard, and the Pages review
  site are all candidates and they are not interchangeable.

`DERIVED`, ordering: doing the repo pass first **feeds** the email rather than
delaying it — the consolidation figure ("started at ~20, forced down to 8") is one
of its named sections, and today's pass is what makes that number current.

## 3 · Slingy Spider — and an App Store ask that is new

`OWNER`:

> "for slingy spider at the moment I feel a little stuck on inspiration etc, tho
> the next steps should be to comlete the proper play store listing and if
> possible an app storelisting"

- **The Play listing is already scoped** — `OQ-PLAY-LISTING` (critical path) and
  `OQ-PLAY-PRIVACY-POLICY`, both open since 2026-08-05, both with a drafted-copy
  half already done. `DERIVED`: it needs no inspiration, which is precisely why
  it is the right thing to do while he is short of it — and it is the only work
  in the estate with a clock (12 testers × 14 continuous days, then ~7 days
  review).
- **An iOS App Store listing has never been discussed in this estate.**
  `MEASURED` 2026-08-22: `spider-swing/export_presets.cfg` carries only
  `Android Debug` and `Android Release` — there is no iOS preset. **Everything
  else about iOS feasibility is UNVERIFIED**, in both directions: the session
  that recorded this first told him iOS needs a Mac, then "corrected" that to
  macOS CI runners removing the requirement, and **checked neither**. Whether
  certificates and provisioning profiles can be generated and managed without a
  local Mac, whether Godot's iOS export runs on a CI runner, and whether App
  Store Connect upload works from CI are all **open questions, not settled
  ones**. Do not inherit either answer.

## 4 · The laptop and mobile capability question

`OWNER`:

> "I'm also working with claude to set up my new leptop as you could probably see
> in some of the recent PRs, I also intend to further find out how much claude
> and chat GPT can do on my laptop especially if I have them connected with my
> mobile devices etc"

Context that IS in the repo: the Galaxy Book6 Pro setup landed 2026-08-21/22
(fm #883/#884), and the first PR raised from that machine immediately found a
real defect — a Windows case-collision that shadowed the capability ledger
(fm #886, card in `.sessions/`).

`DERIVED`: this is a **capability question, and the estate has a method for it**
(`capability-probe`). It has not been run for the local-Windows or
phone-connected surfaces, and `docs/execution-surfaces.md` has no row for
either. Worth a dedicated session rather than a guess — no answer should be given
without a probe.

## What this file is not

Not a plan. The plan is the [consolidation program](../planning/2026-07-26-consolidation-program.md);
OD-17 and OD-18 are where two of these became binding. This file exists so the
other three asks — the website, the App Store, the laptop probe — are findable by
the session that eventually picks them up, instead of being lost with the
transcript.
