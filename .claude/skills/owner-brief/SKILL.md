---
name: owner-brief
description: "Produce the owner's status brief on demand — what landed since he last looked, what needs his eyes, what happens next — in plain language with zero technical vocabulary, decisions as one-letter choices. Use when he asks 'where are we', 'what's left', 'what did I miss', or any status-shaped question."
---

# owner-brief

The owner-facing counterpart of a session card. A card records for the next
*session*; this brief reports to the *owner* — a different reader with a
different question. He works by pattern recognition on plain-language
summaries, rarely uses technical vocabulary, and his attention is the
estate's scarcest resource. The brief exists so a status question costs him
one read, not a scroll through PRs and cards.

## When this runs

He asks anything status-shaped: "where are we", "what's left", "what did I
miss", "is there anything for me", "give me an update". Also unprompted at
the end of any session that leaves more than one item waiting on him — the
brief is then the session's closing message, not a separate artifact.

## Sources — read these, in this order, before writing

1. Session cards since his last visible touchpoint (`.sessions/`, newest
   first) — what actually landed.
2. Open PRs in every repo touched (an open PR is either in-flight or waiting
   on him — say which).
3. ⚑ flags — decide-and-flag items awaiting his veto, wherever they live.
4. `docs/owner-queue.md` — standing owner-only asks (OQ items).
5. The program's NOW pointer — only to say whether it moved (it usually
   should not have; say so in one line).

## The shape — three sections, strict order, hard rules

**1. LANDED** — what is finished and merged, grouped by outcome not by PR.
One line per outcome, plain words. "The skills now fire automatically" beats
"merged #721 adding a router section to CLAUDE.md."

**2. YOUR EYES** — everything waiting on him, each as a finished step per
`prep-owner-steps`: the direct link, what he'll see, the one-letter choice
where there is one, with the **recommendation bolded first**. Risk-class
every action (✅ safe / ↩️ reversible / ⚠️ irreversible). Vetoes are stated
as "live unless you object" — never as questions that block.

**3. NEXT** — what happens without him, in one or two lines. If nothing
happens without him, say that plainly; an empty NEXT is information.

Hard rules:
- **No PR numbers, file paths, branch names, or tool names in the body** —
  links carry the technical identity; prose carries the meaning. (PR numbers
  may appear inside a link's text, nowhere else.)
- **Nothing in YOUR EYES that an agent could do itself** — the
  attempted-it-or-named-the-exact-wall bar from the collaboration model
  applies to every item.
- **Honest nulls survive into the brief** — if something is unverified or
  unmeasured, one plain sentence says so. The brief inherits the estate's
  honesty rules; a smooth brief that hides a doubt is a defect.
- **Length: he should finish it in under a minute.** If it cannot compress
  that far, the estate has too many open items — say *that*, and list only
  the top three.

## Traps

- **The card is not the brief.** Cards are written in estate vocabulary
  (born-red, gates, venues) — every one of those words is translated or
  dropped. Test: would the brief read to someone who has never seen this
  repo? It should.
- **"FYI" items are attention theft.** If it needs no decision and no action,
  it belongs in LANDED as one clause or nowhere.
- **Don't manufacture decisions.** A genuinely settled call presented as a
  choice costs him a read and erodes decide-and-flag; the bar for YOUR EYES
  is "only he can do or veto this".
- **Recency is not importance.** Order YOUR EYES by consequence, not by when
  each item appeared.
