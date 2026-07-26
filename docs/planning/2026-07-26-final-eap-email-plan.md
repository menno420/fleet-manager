# The final EAP email — plan for the writing session

> **Status:** `plan` — owner-directed 2026-07-26 (late night), execution
> targeted for the owner's next free sitting (~2026-07-27). This file tells the
> writing session **where every piece of source material lives** and how to
> help the owner assemble the mail. Program step **E1** (the program's NOW).

## 1 · What the owner wants (his words, distilled)

- **One clear review of the whole EAP and how we perceived it** — a synthesis,
  not new argument.
- **All requests/issues as a clear, overseeable numbered list without much
  explanation** — "here's what we'd like to see, and why", one line of *why*
  per item. His example: *"1. Manageable settings that are easy to find and
  easy to enable/disable. Because we ran into a lot of permission problems."*
- **The good parts too** — the full picture in one mail.
- **Same two-part format as the earlier reviews** (Part 1 the owner's own
  voice, Part 2 written by Claude) — but **much shorter** than before.
- **A FRESH thread** — a new compose with a new subject, *not* a reply to the
  old "Claude Code Projects Review" thread, so no old mail gets linked and the
  document stands alone, very clear.

Why fresh-thread matters (understood intent): the earlier mails were long,
incident-driven, and buried in a reply chain. This is the standalone closing
statement — readable by anyone on the team in minutes with zero context.

## 2 · Facts the writing session needs (verified 2026-07-26)

- **The correspondence so far** (thread "Claude Code Projects Review",
   2026-07-08 → 07-16, plus announcements): 07-08 intro review · 07-12
  scale-up report (1→15 repos) · 07-14 team ack · 07-16 ×2 the
  classifier-crisis pair · 07-16 21:42 attachment resend. Separately: the
  program-end "power user" thank-you thread (07-21, gift box, warm close) and
  a UX-research interview invite (07-21, unanswered as of this writing).
- **The 2026-07-18 follow-up draft was NEVER sent** (verified in sent mail):
  its net-new findings — the venue-scoped guard, agent-memory wall
  propagation + the CI antidote, stale-text-outranks-live-instruction, the
  trigger-tool forced-approval finding — are **unused material** available to
  the final list. Draft: superbot `docs/eap/2026-07-18-followup-email-draft.md`.
- The program **closed 07-21**; sessions read-only 07-22. Projects may return
  ~August for general use (owner-heard, not fact).

## 3 · The source map — where to look, in priority order

**The spine (read these first):**

1. **fm `docs/owner-reflection-2026-07-21.md` § "The vendor final-review email"**
   — guidance written FOR this exact mail: what's already said exhaustively
   (permission/scoped-grant proposal · coordinator↔worker trust — **reference
   in one line, never re-argue**), what's net-new and worth space (capability
   evaluations owed · the week-over-week scorecard · the
   "what I had to build myself" teardown · economics · the standing
   test-harness offer · **the consolidation number**), the opening thesis
   (*"I scaled it until I found the wall; the wall is human review, not agent
   capability"*), and the form (tight; lead with genuine enthusiasm).
2. **fm `docs/eap-retrospective.md`** — the harvest fields: §1 likes (the
   good-parts list), §2 dislikes, **§3 "platform/tooling features that would
   have helped"** (closest thing to a ready wish list), §4 wishlist.
3. **superbot `docs/eap/permission-classifier-findings-consolidated-2026-07-16.md`**
   — the whole permission picture in one place, incl. the scoped-grant
   proposal (cite, don't repeat).
4. **superbot `docs/eap/2026-07-18-followup-email-draft.md`** — the unsent
   findings (see §2).
5. **fm `docs/eap-story.md` §10** — the numbers for the review paragraph
   (growth, what got fixed, what stayed hard) and the honest-count caveats.
6. **The sent mail itself** (Gmail thread "Claude Code Projects Review") — to
   check any candidate item against what was already said, so the list stays
   pointers-only for known topics.

**Supporting:** fm `docs/audits/eap-project-audit-2026-07-14.md` (top-5 pains
with paste-ready asks) · fm `docs/anthropic-email-pack.md` (the four routine
bugs) · substrate-kit trigger forensics (`docs/reports/trigger-forensics-2026-07-12`)
· fm `docs/findings/fleet-economics-2026-07.md` (costs not agent-visible).

## 4 · Seeded candidate list (pre-harvested — the owner trims/reorders)

Format per his example: **what we'd like to see. Because <one line>.**

**Requests / wishes:**
1. Manageable permission settings — easy to find, easy to enable/disable,
   respected in automode. *Because we ran into permission problems constantly,
   and the projects kept suggesting settings that don't exist for automode.*
2. Owner-scoped pre-authorization (allow AND restrict, per repo/branch/action).
   *Because the owner should set the rules once, not be present for every
   step — proposed in detail in our earlier mails; pointer only.*
3. A trusted coordinator→worker channel. *Because coordinator instructions
   were treated as untrusted data, and merges/routines died on it.*
4. Let the coordinator itself act (create/edit PRs, merge, arm auto-merge).
   *Because it holds the most context, and you already trust it to change its
   own model and repos.*
5. Clear per-session oversight — what each finished session did, in one place.
   *Because the owner reviews through what he can see, and had to build his
   own status site to get it.*
6. Reliable, inspectable routines — runs viewable, model attribution correct,
   panels agreeing, failures leaving a tombstone. *Because schedulers failed
   silently twice, and nothing on the platform showed it.*
7. Routines created by a project should carry the repo. *Because sessions woke
   up with nothing attached ~1 in 3 times for one project.*
8. Native fleet primitives: an inter-session channel + a real scheduler.
   *Because our whole control-bus/roster layer was a workaround built on git.*
9. Agents that reliably know their own capabilities. *Because most of our
   stalls were an agent believing a wall that wasn't there — we ended up
   building a CI gate that forbids writing walls down.*
10. A project setup interview (goals, workflow, permissions) at creation.
    *Because a few open questions at the start would replace most of the
    custom-instruction engineering we did by hand.*
11. PRs opened by agents should default to READY, with native auto-merge
    armable by the agent (incl. MCP-created PRs). *Because the draft-default
    silently stranded finished work for hours.*
12. Fresh containers that start on origin HEAD with a proven setup script.
    *Because stale clones and one bad setup script were our only session
    deaths.*
13. Usage/cost telemetry visible to the agent tier. *Because costs were
    invisible to every agent surface, so our economics stayed honest nulls.*

**The good parts (keep — the mail must carry these too):**
- Worker-tier autonomy worked from day one — the born-red → claim → PR →
  auto-merge loop ran with zero prompts and zero tool failures.
- Velocity **with** recoverability: ~19 repos and thousands of PRs in a week,
  and an adversarial audit that found zero fabrication (integrity held).
- The platform's best unlocks were real: agent self-armed routines,
  Contents-API bootstrap, the self-updating Projects features shipped
  mid-program.
- The models themselves: the 14-hour zero-rework rebuild; 533-golden
  byte-parity; honest negative results treated as deliverables.
- The team: responsive (extension, mid-program feature ships, the power-user
  recognition). Genuine thanks belongs in Part 1.

**The two review-paragraph numbers** (from the reflection's guidance): started
~20 repos → the owner found **~8 parallel projects was already past one
person's review ceiling** → now consolidating to ~7 sections. That number IS
the finding.

## 5 · How the writing session works (method)

1. Read §3's spine (1→4 minimum). Harvest → dedupe against §4 → sort each item:
   **wish-list** / **good-part** / **already-reported** (one-line pointer max).
2. Present the owner the trimmed candidate list for picking/reordering —
   choices, not prose.
3. Draft **Part 2** (Claude's half): ≤1 page — a 3–4 sentence honest review
   paragraph (the thesis + the consolidation number), then the numbered list
   in his exact format, then the good-parts block. No screenshots, no
   attachments; link public repo docs only where a pointer genuinely helps.
4. **Part 1 is the owner's voice — never ghost-write it.** Offer at most a
   skeleton of pointers (open warm → the one-paragraph verdict → hand off to
   Part 2 → the standing offer + thanks). He writes it himself, as before.
5. Assemble in one copy-paste block. **Logistics:** a FRESH Gmail compose (not
   a reply — compose new, so no thread linkage), new subject (suggestion:
   *"Claude Code Projects EAP — final review & wishlist"*), to the EAP address
   with the usual team cc's (they're in the prior thread). Target length:
   the whole mail well under a fifth of the earlier ones.
6. After sending: mark E1 done in the program ledger; the unsent 07-18 draft
   and the email-pack get a one-line "superseded by the final mail" note.

## 6 · Boundaries

- **Don't re-argue** the permission/classifier case or the trust-model case —
  the reflection is explicit; one pointer line each.
- **Don't inflate** — every wish stays one "what + because" line; detail lives
  in the public repos if anyone wants it.
- **The mail carries no confidential program specifics beyond what the owner's
  own prior mails already shared.**
- Nothing sends without the owner — he sends it himself, from his own compose.
