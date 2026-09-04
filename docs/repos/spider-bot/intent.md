# spider-bot — intent

> **Status:** `owner-guidance` — **ANSWERED 2026-09-04, live.** Supersedes the
> 2026-08-28 DRAFT, which was written from committed evidence only and
> deliberately proposed no feature direction while the record said *"what the
> bot does next is the OWNER's pick"*. He has now said what it is for. Every
> ❓ the draft carried is closed below; none was deleted, so the question and
> its answer stay side by side.
>
> **Canonical for:** what spider-bot is **for**, what done looks like, what it
> must never become. That is fleet-manager's half of the boundary in
> [`../../intent.md`](../../intent.md) § 1 — *"what the repo is for"* lives
> here; *"its architecture, its internal state, how to work inside it"* lives
> in the repo. The repo's own `docs/product-shape.md` (`binding`) is canonical
> for the product model this intent generates, and its `docs/architecture.md`
> for how that model is built. When this file and the repo disagree about
> mechanism, the repo wins; when they disagree about purpose, this file wins.
>
> `OWNER` = his words · `DERIVED` = the session's inference, revisable.

## Why it exists

`OWNER`, 2026-09-04, live, and this is the sentence the whole file hangs on:

> *"Spider Bot exists to manage the Slingy Spider server and help during
> testing of the game. It should become a reliable automoderator with heavy AI
> integration. People should be able to talk naturally to it for guidance,
> complaints, bugs, feedback and improvement ideas. Those reports should become
> durable, easy for the developer to find and act on — preferably through
> GitHub or an equally clear developer-facing system."*

`DERIVED`, and it is the load-bearing consequence: **spider-bot is a tool for
operating one server and one game's testing process.** Not a general community
platform, not a multi-game product. The
[game-community-bot plan](../../planning/2026-08-21-game-community-bot/README.md)'s
headline — *"a clean, multi-game Discord bot repository"* — is **narrowed by
this statement, not extended by it**. That plan stays the record of the
architecture research; it is no longer the description of what this bot is for.

**Still true, and not superseded:** his 2026-08-28 answer that `spider-bot` and
a remade `superbot-next` are *"eventually … rebuild as one real well
functioning bot thats build right from the start"*, with the design criterion
**no architectural debt · planned and connected from the start · able to grow
indefinitely**. The 2026-09-04 direction says what this input is *for*; the
2026-08-28 direction says what shape it must be in when it becomes an input.
They compose: build the operations bot, build it clean enough to carry forward.

## What done looks like

`DERIVED` from his four sentences, decomposed into the four responsibilities a
session can actually check work against:

| # | Responsibility | Done when |
|---|---|---|
| A | **Server operations** — event logging, member lifecycle, roles, cleanup, tester status, an owner/mod console, moderation, health, safe announcements | Running the server costs the owner less attention than doing it by hand, and every autonomous action can be explained after the fact |
| B | **Testing assistant** — how to join, the current process, the current build, how the game works, known issues, troubleshooting, what feedback is useful, where a report went, what has since been fixed | A tester can answer all of those without the owner, and the owner can see what testers are reporting without reading scrollback |
| C | **AI community assistant** — natural conversation as a first-class route, not a fallback behind command names | Someone who knows no command names gets a useful answer or is guided into the right durable workflow |
| D | **AI-assisted moderation** — *reliable* is his word and it is the acceptance bar | Obvious problems are handled deterministically, uncertain ones stay reviewable, and no member can make the bot punish someone incorrectly |

**The one number has not moved and still ranks the work:** Google will not let
Slingy Spider leave closed testing until 12 testers stay opted in for 14
continuous days. A capability that does not help A–D or that number is *later*,
not wrong.

> ✅ **Closes the draft's** *"Is this a tool for the game … or a community thing
> in its own right?"* — **a tool for the game and its server.** Recorded rather
> than deleted, because the draft's framing is what his answer was given
> against.

## What it must never become

`OWNER`, by direct implication of *"reliable"*: **heavy AI integration is not a
language model with Discord permissions.** The AI supplies **judgement**; the
deterministic system supplies **authority**.

`DERIVED`, the refinement this forces on the repo's invariant 5 (*"the AI never
performs side effects"*) — **refined, never deleted**:

```
Discord event → deterministic pre-check → optional AI analysis → typed verdict
→ deterministic policy engine → permission/risk gate → typed operation
→ Discord API → audit + case record
```

The AI may influence the verdict. The AI never calls delete, timeout, kick,
ban, a role mutation or a channel mutation itself; the policy and service layers
own those. A verdict is a validated structured schema or it is nothing —
free-form prose is never parsed into a moderation action, and invalid or
incomplete model output means **no automatic action**.

Unchanged and still absolute: never Administrator · the bot never DMs a member
first · the tester role is never granted by code · unconfigured = silent.

Standing non-goals, `DERIVED` from his framing plus the repo's own list:
economy, games inside the bot, XP, casino, general-purpose platform
abstractions, a web dashboard without a current need, arbitrary AI shell or
database tools, autonomous server redesign, and **a second source of Slingy
Spider product truth** — `spider-swing` owns the game; this bot consumes and
projects it.

> ✅ **Closes the draft's** *"What do you want people to feel about it — a
> useful utility that stays out of the way, or a character that belongs in the
> server?"* — **answered by function rather than by taste**: *"people should be
> able to talk naturally to it"* makes conversation a first-class route, so it
> is neither a silent utility nor a mascot; it is a member of the team people
> address directly. The *voice* question (how playful) remains open and is a
> matter of taste, not architecture.

## What would make me stop

**Still nothing recorded**, and the draft's question is now sharper rather than
answered:

> ❓ If the closed test ends and the community does not grow, does the bot keep
> running? It costs a Railway worker continuously. His 2026-09-04 direction
> makes the bot's job *the test*, which means the honest reading is that its
> job has an end date — but he has not said so, and inferring a shutdown
> condition from a purpose statement would be manufacturing product intent.

## Who it's for

`DERIVED`, unchanged and now reinforced: **the members of the Slingy Spider
Discord server — real people, daily.** Still the only thing in the estate that
strangers interact with as a matter of course, and now the only one that will
form judgements about them.

## How much it matters right now

`DERIVED`, dated **2026-09-04**: **live and load-bearing.** Push to `main`
deploys straight to production with no PR gate, and the funnel it runs feeds the
estate's one hard external clock.

> ✅ **Closes the draft's** *"Is the lightest gate in the estate deliberate?"* —
> **partially, and by working practice rather than by his word.** He has not
> ruled on the gate. What this session did instead is treat production safety as
> a hard constraint regardless: branch, PR, verification before merge, new risky
> capability shipped disabled or in shadow mode, deployed SHA verified after any
> production-affecting merge. Making CI a *required* check is still his call and
> still changes the landing workflow, so it stays owner-gated.

## — anything else

`DERIVED`. The direction creates one genuinely new estate obligation: **a
cross-repository seam.** For the bot to know the *current* game rather than a
copy of it, `spider-swing` must produce something and `spider-bot` must consume
it, under spider-swing's own `CONSTITUTION.md` rule that *"cross-repo feeds
carry a pinned contract"*. That is the first time either repo has owed the other
anything, and it is recorded here because neither repo's own intent would carry
it.
