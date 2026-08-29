# substrate-kit — intent

> **Status:** `owner-guidance` — **DRAFT,** **awaiting the owner's own words.** Written 2026-08-28 by a
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
agents *take initiative*.

**And the kit's own README already implies it — he said so himself.** The round
measured the word *initiative* returning zero hits across the kit's README,
closeout and register, and read that as a missing purpose. He corrected it
(2026-08-28): *"whats written there is also correct, the initiative part falls
into place perfectly with the existing sentence of 'little steering'"*. So the
ordered charter rewrite **makes an implication explicit**; it does not fix a
wrong sentence.

## What done looks like

`OWNER`, 2026-08-28, choosing *"Right now it's worth it, but it must end"* —
that the current round is a one-off correction because he stepped back too far,
and that afterwards **the kit should go quiet again.**

`OWNER`, 2026-08-28, and it is precise:

> *"the main goal is to ensure it's working correctly in such a way that it does
> not need more corrections, but only occasionally an addition or improvement
> when we come across a new problem"*

**Done is correction-free** — not feature-complete, not a version number.
`DERIVED`, and the distinction is load-bearing: a **correction** means the kit
was wrong, and those should trend to zero; an **addition** means the world
presented a new problem, and those keep arriving forever. Any proposed kit work
should say which it is. **Recurring corrections are the failure signal;
recurring additions are health.** It also means the 34-row worklist is not a
plan to burn down — the rows exist because problems were found, and finishing
them is not itself the goal.

**✅ ANSWERED 2026-08-28:** *"Quiet, but it can still grow when something proves
out."* **Maintenance ends; development does not.** New capability is permitted
only through the promotion rule — after it measures useful in a real repo first.
He declined "shrink from here", so removal is not ordered. The failure signal is
specifically **recurring upkeep**, not growth.

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

`OWNER`, 2026-08-28 — **and the answer is nothing.**

> *"The kit is meant to be a real product that keeps existing"*

Retirement is not on the table. No session should propose going back to
per-repo conventions with no shared substrate. **This slot is not empty for want
of asking — it is genuinely not applicable here**, which is a more useful record
than a blank.

## Who it's for

`OWNER`, 2026-08-28: *"The kit is definitely meant to be used by others and I'm
pretty sure that that is already explained there. At least by the MIT license"* —
so the audience is **agents in any repo, including repos that are not his.**

**Verified at `main`, 2026-08-28, because the claim about the tree was hedged:**
he is substantially right — `LICENSE` is MIT, and `README.md` carries a one-step
adopt recipe, three modes that explicitly *pace adoption*, and a pip-installable
form, in a repo-agnostic voice. **One exception that stands:** the repository
description reads *"AI self improvement system in progress"*, with no topics and
no homepage — the first thing an outside adopter meets, and it undersells a kit
he intends others to use. *(A second, that the README's purpose sentence omits
initiative, he refuted on sight — see "Why it exists".)*

One measured oddity worth his eye: **`superbot` — the origin repo, and the only
one running a live production service — never adopted the kit.**

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

