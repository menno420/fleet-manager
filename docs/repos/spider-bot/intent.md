# spider-bot — intent

> **Status:** `owner-guidance` — **DRAFT,** **awaiting his words.** Written 2026-08-28 from committed
> evidence. The Layer-2 entry point says plainly that *"what the bot does next
> is the OWNER's pick — do not infer a feature"* — so this draft deliberately
> proposes **no** feature direction.
>
> `OWNER` = his words, quoted · `DERIVED` = the session's inference, revisable.

## Why it exists

`DERIVED`: created 2026-08-24 under his direction as the game-community plan's
**clean** repo — a fresh start rather than an extension of `superbot`, which
stays frozen as the behaviour oracle while `superbot-next` serves as
architecture donor. He chose the name `spider-bot` over the plan's
`superbot-community` default.

> ❓ **Why a second bot at all?** `superbot` has been running the live Discord
> bot for months. Was `spider-bot` about a clean codebase, about this being the
> *game's* community rather than a general server, or about finally getting a
> bot you could actually change without fear?

## What done looks like

**Nothing recorded.** v0.1 shipped the tester funnel, the human-only roster,
owner utilities and AI chat, and the record is explicit that the next step is
his to name.

> ❓ Is this a **tool for the game** — its job is to run the tester funnel and
> feedback loop, and it is done when that works — or a **community thing in its
> own right** that keeps growing as long as the server does?

## What it must never become

`DERIVED` from the repo's own twelve invariants, two of which the record names
as the most tempted: **never Administrator**, and **the AI never causes side
effects.** AI initiative is confined to named channels; every AI decision is
audited to stdout and `#mod-log`.

> ❓ The AI replies on mention anywhere public and takes initiative only in
> `general`. What do you want people to *feel* about it — a useful utility that
> stays out of the way, or a character that belongs in the server? That
> judgment is yours and nothing else in the record implies it.

## What would make me stop

**Nothing recorded.**

> ❓ This one is unusually concrete: if the game's closed test ends and the
> community doesn't grow, does the bot keep running? It costs a Railway worker
> continuously and has real users today.

## Who it's for

`DERIVED`, and it is the estate's clearest answer to that question:
**the members of the Slingy Spider Discord server — real people, daily.** This
is the only thing in the estate that strangers interact with as a matter of
course.

## How much it matters right now

`DERIVED`, dated **2026-08-28**: **live and load-bearing.** Push to `main`
deploys straight to production with no PR gate, and the tester funnel it runs
feeds the game's Play closed test — the estate's one hard external clock.

## — anything else

> ❓ It is the only repo where a careless push reaches real people within
> minutes, and it has the *lightest* gate in the estate (informational CI, no PR
> requirement). Is that deliberate — you want to be able to fix the live bot
> fast — or is it just how it ended up?
