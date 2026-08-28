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

**✅ ANSWERED 2026-08-28, and it is bigger than "a second bot":**

> *"Superbot itself is a repo that's filled with too much history, too many
> trials and errors. What I want from spiderbot and superbot-next (this one will
> have to be remade aswell since the current build is nothing like the desired
> product) is that they eventually are rebuild as one real well functioning bot
> thats build right from the start … The goal is to create a bot without
> architectural debt for as far as that's possible. Everything should be planned
> and connected from the start so it remains manageable and able to grow
> indefinitely."*

**`spider-bot` is not the finished successor — it is one of two inputs to a bot
that does not exist yet.** The end state is **one** bot, rebuilt from the start,
with a named design criterion: **no architectural debt · planned and connected
from the start · able to grow indefinitely.**

`DERIVED`: this is the first intent in the sitting that gives a **checkable
design criterion** rather than a purpose. It also means the shape matters more
than the feature set — a session adding features here should know it is adding
to an input, not to the destination.

**Already recorded, and worth reading before treating any of this as new:** the
consolidation into one new repository is a standing constraint in
[the GCB plan](../../planning/2026-08-21-game-community-bot/README.md) `:40-43`
(*"the eventual consolidation he describes is of the two `superbot`
**repositories** into one new repository … **not** a merge of running bots"*),
and `superbot-next`'s unreadiness is measured in
[its own entry point](../superbot-next/README.md) `:29` (*"golden-parity green
must not be read as 'ported'"* — capture-world literals, 60/66 help panels
button-less). What his 2026-08-28 answer **adds** is the verdict the record left
to him (`superbot-next` gets remade) and the growth requirement (*"able to grow
indefinitely"*), which appears in no prior record. **The plan also flags its own
unresolved contradiction one line later** — *"the executable roadmap now
contradicts this, and that is not resolved here"* — which anyone acting on this
should resolve first.

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
