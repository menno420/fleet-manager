# substrate-kit — intent

> **Status:** `DRAFT — awaiting the owner's own words.** Written 2026-08-28 by a
> session from committed evidence, as the first record of the intent-elicitation
> sitting. **He rewrites this; the draft exists to give him something to react
> to**, which his own profile names as the form that works.
>
> **How to read the labels:** `OWNER` = his words, quoted. `DERIVED` = the
> session's inference — *revisable, and explicitly not his statement.* Every
> slot below says which it is. **Nothing here is his intent until he says so.**
>
> **Template:** the six slots he chose (2026-08-28) plus a free section —
> *"there should be a default template but also room for extra free
> explanation."*

## Why it exists

`OWNER`, 2026-08-28 (OD-24 § 2), and it is the clearest purpose statement in
the estate:

> *"Especially on github I think it's important that each sessions tries to
> improve the repo in any way it can, mostly when those things are related to
> it's task but also unrelated things that it notices, and each session should
> actively participate in that. **Which is mostly why I created the
> substrate-kit, so agents become more autonomous and think more for themselves
> and take more initiative.**"*

`DERIVED`: the kit is not primarily a memory system, a checker suite, or a
session-card convention — those are its **mechanisms**. Its purpose is to make
agents *take initiative*. The gap this round measured is that the word
**initiative** appears nowhere in the kit's own README, closeout or program-law
register (grep, zero hits), which is why he ordered the charter rewritten
(2026-08-28).

## What done looks like

`OWNER`, 2026-08-28, choosing *"Right now it's worth it, but it must end"* —
that the current round is a one-off correction because he stepped back too far,
and that afterwards **the kit should go quiet again.**

`DERIVED`: **done is the kit not needing sessions.** Not a feature list, not a
version number — an absence of upkeep. The current round ends with the charter
rewrite, the doc-surface sweep and one release; after that, recurring kit work
is a symptom rather than progress.

> ❓ **Guiding question.** "It must end" — end meaning *no more maintenance*, or
> *no more development at all*? Does the kit ever get genuinely new capability
> again, or is it finished and only kept correct from here?

## What it must never become

`OWNER`, 2026-08-08, as a fleet-manager non-goal he confirmed on 2026-08-28
still applies to the kit rather than exempting it:

> **"An apparatus that needs maintenance sessions of its own."**

`OWNER`, 2026-06-13 (superbot:Q-0101), the shape of failure he ruled against
before it happened:

> *"generating 24 stubs that then rot would be worse than the current gap"*

`DERIVED`: the kit must never become something that plants files nobody fills.
Measured: its planted `.session-journal.md` was byte-identical to its template
in **11 of 14** adopter repos — precisely the stub-rot he pre-judged.

## What would make me stop

`DERIVED` — **this slot is inference, and it is the one most in need of his
words.** From his 2026-08-28 answer: if kit work keeps recurring after this
round, that is the signal it is too big, and the response is **to make it
smaller**, not to schedule more maintenance.

> ❓ **Guiding question.** Is there a version of this where you'd retire the kit
> entirely — go back to per-repo conventions with no shared substrate — or is
> the kit permanent and only its *size* negotiable?

## Who it's for

`DERIVED`: agents working in every adopter repo — 12 registry rows plus five
adopters the roster cannot see. Not for him: he has never read the kit's
internals, and its surfaces are agent-facing by construction.

One measured oddity worth his eye: **`superbot` — the origin repo, and the only
one running a live production service — never adopted the kit.**

> ❓ **Guiding question.** Is the kit ever meant to be used by anyone outside
> your estate? It is public, it has shipped 21 releases, and it carries a
> placeholder name you have now decided to change — which reads like a decision
> about *other people seeing it*.

## How much it matters right now

`DERIVED`, dated **2026-08-28** — the slot he identified as the one guaranteed
to go stale, so it carries a date by design.

**High, with an end in sight.** It is the subject of the active review round and
of his own root-cause answer (*agents don't take enough initiative to leave the
repos in a better shape*) — the kit is the artefact meant to fix that. But he
has time-boxed it: worth it now, must end.

## — anything else

`DERIVED`, the things a session should know that do not fit a slot:

- **The kit was founded on a measured failure, and its own bench predicted the
  regression he later noticed.** Cold-start A/B FAILed twice; the founding
  thesis became *"the door, not the notebook"* — enforcement over documentation.
  On 2026-07-12, nine days before the program closed, its bench returned **1
  PASS / 8 FAIL** with the enforcement *pull* measured as a null. He observed
  that regression independently six weeks later.
- **What the kit shipped was the enforceable half of a two-part practice.** The
  ritual (born-red cards, gates) held ~100 % across the program's close; the
  loop behind it (interview → mine → owner-ratified promotion) died, because
  nothing mechanised it.
- **Portability is a live requirement, not an aspiration** — *"the skills we
  make, and possibly also some of the hooks we make, also work for chatGPT, tho
  some of them will probably need to be a little finetuned based on the model
  it's for"* (`OWNER`, OD-24 § 4).

> ❓ **Guiding question.** The kit's daily culture — markers, badges, born-red —
> was deliberately demoted at founding to *"house style, not program law"*,
> while the autonomy mechanics became binding law for every adopter. Was that
> the right split? It is the decision that made the card ritual survive and the
> ideas loop die.

