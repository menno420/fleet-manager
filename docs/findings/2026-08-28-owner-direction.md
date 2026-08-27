# Owner direction, 2026-08-27→28 — local/cloud sync: the handoff goal, the routing rule, and two answers

> **Status:** `reference` · the overnight 2026-08-27→28 hub sitting
> (owner-live, on the laptop — venue `local-desktop`). `OWNER` throughout
> unless marked. Same job as
> [`2026-08-26-owner-direction.md`](2026-08-26-owner-direction.md): his words
> verbatim, so the directives derived from them can be checked against source.
>
> **What it is NOT:** a queue, and not a design. Every mechanism sketched from
> these words is `DERIVED` and lives in the plans this record amends
> ([the activity area](../activity/README.md) ·
> [the execution packets](../planning/2026-08-26-estate-execution-packets.md)).
>
> **Context:** the sitting reviewed the whole 2026-08-26 sync cluster (the
> visibility finding, `docs/activity/`, the legibility plan, the packets) and
> answered the open questions it raised. Recorded as **OD-23** in the program.

## 1 · The goal, sharpened — visibility is the means, handoff is the goal

> *"the goal should be to make what happened locally visible to the cloud
> sessions in such a way that if you start a task that can only be done locally
> because you need the browser or any other part of my device to use, it should
> be simple to then start a new session in the cloud that continues the work."*

This sharpens 2026-08-26's *"could be helpfull if I have done certain
preparations on my laptop and want to continue in the cloud"* into the defining
acceptance test: **a device-bound task started locally must be continuable by a
fresh cloud session, simply.** `DERIVED`, one consequence with teeth: only
pushed work exists for the cloud, so a handoff-intended local sitting must end
in a push.

## 2 · The local section in fleet-manager — deeper than a pointer, lean, history included

His first statement of the shape:

> *"the local sessions should keep a personal section inside fleet-manager,
> just like every repo has it's own pointer in there, but for the local
> sessions it should be a little more in depth because there is no real repo
> for the cloud sessions to read."*

> *"it is not important that everything is know, but certain things like
> what's currently possible on the laptop with the local session and why
> certain tasks would be better locally etc. so that a cloud session can see
> and understand what's going on locally."*

And his own correction of the first, same sitting — **read the two together**:

> *"So the main things should be written down in fleet-manager, I previously
> worded it a little bit wrong, I meant that it should stay lean, but not that
> it should exclude all feature work."*

So the planned surface pages (the [activity area](../activity/README.md)
§ Planned) carry **state AND a lean account of what happened** — capabilities,
why certain tasks run better locally, and the main things that were done —
written tight, never exhaustive. *Lean is a property of the writing, not a
licence to drop history.*

## 3 · The routing rule, and local sessions on full discipline

> *"A local session should basically just follow the same rules as a cloud
> session, leave a session journal and all the other required thing. And it
> should also still work per repo as normal, so if you work in "spider-swing"
> you will leave a session journal there etc, but it should be properly scoped
> to the task. So in spider-swing you do not write things that are unrelated to
> that repo, for that you still use fleet-manager and the local onedrive. the
> goal is to make everything easily accessible and easy to trace back."*

> *"So both me and another session will know where to look and can rely on the
> fact that everything that happened is properly documented."*

The routing rule, stated once: **repo work → that repo's own session card,
scoped to that repo only · cross-repo / estate-level → fleet-manager ·
machine/personal → the OneDrive hub, with fleet-manager's local section as the
lean cloud-readable account of it.** This confirms the 2026-08-26 split rule
(off-repo in fm, repo work in the repo with the venue marker) and extends it:
local sessions carry the full card discipline, not an exemption.

`DERIVED`, the two-halves reading the amendments act on: the per-repo half is
already mechanised (the kit's added-card gate binds any local session landing a
PR); the non-repo half has no mechanism anywhere, and under
[`../intent.md`](../intent.md) § 4 it needs one on the hub side (close-hook
routing by scope) rather than another rule statement. That wiring is planned
work, **not executed** (§ 6).

## 4 · PKT-B3 ownership, clarified — "himself" meant "via local sessions"

Asked directly whether the recorded *"owner-executed … no session pre-empts"*
line on PKT-B3 should be replaced:

> *"yes, what I meant by that is that I want to do this in local sessions.
> Because they have the full ability to work on both sides and see everything."*

So the 2026-08-26 record's *"he is executing this himself, locally"* was a
venue statement, not a by-hand statement: **hub-local sessions execute the
local-surface pages** — they are the only venue that can read both the hub and
GitHub — with the owner directing. The packets and the activity area are
amended accordingly; the 2026-08-26 record carries a pointer here and is
otherwise untouched (it is history of what he said then).

## 5 · Two one-letter answers

> *"Agents.md should indeed be everywhere, and public is fine"*

- **`OQ-FM-AGENTS-BOOT` — ANSWERED: yes, estate-wide.** Unlocks PKT-B4's ×N
  rows (their sequencing rule stands: the audit-failure repos after their
  Wave C fixes).
- **Public stays acceptable** — the owner-comments contract's explicitly-public
  records and the world-readable local-surface pages. The option he accepted
  carried a standing content rule (session-proposed, owner-accepted):
  **capability/work level only — nothing personal, no paths or
  security-relevant detail** on public surfaces; personal context stays in the
  hub.

## 6 · Process notes from the sitting — worth keeping

- **Execution is explicitly held.** *"No execution yet, because I still have
  more to plan."* The pages, the hub wiring and every packet stay untouched;
  this record and its amendments are the only landing he authorised.
- **He set a removal-preview protocol and it worked:** *"before you remove
  anything tell me what and why you removed so I can examine if the removal of
  that was appropriate, or if maybe it just needs to be adjusted a little
  bit."* Six removal/change rows were previewed in-chat; he approved all six,
  adjusting rows 1–2 (the clarification in § 4). The protocol generalises:
  plan amendments that delete or demote recorded positions get an owner
  preview first.
- **The substrate-kit conversation is next, deliberately its own sitting:**
  *"Did you also read something about the substrate-kit there while you were
  looking for this plan? I believe this is also part of the same plan. I want
  to talk about this for a while aswell. to make sure everything is properly
  understood."* He is right on the connection — Wave A propagates only through
  kit releases — and he already named the kit as connected on 2026-08-26
  ([that record](2026-08-26-owner-direction.md) § 5, last quote).

## 7 · What this sitting did NOT decide — honest nulls

- **`OQ-ONEDRIVE-HUB` is rescoped, not answered.** No a/b/c letter was given.
  The question's sync motivation (how the cloud sees the laptop) is dissolved
  by § 2 — the cloud reads the fm local section. What survives is unhurried
  hub housekeeping (whether the hub itself wants git versioning/backup),
  blocking nothing; the old recommendation **(a)** no longer stands as a sync
  path. `DERIVED`, review-raised (`@codex`, fm #954): the pages give sight,
  not file access — work meant to continue in the cloud lands in a repo before
  the handoff, and a genuine handoff depending on hub-only artifacts would
  re-open the a/b/c trade as the recorded transfer candidates.
- **No GO for PKT-B3's pages or the hub-side wiring** — planned, specified,
  held.
- **The kit questions are open for the kit sitting**, including one his
  AGENTS.md yes reopens (`DERIVED`, session-raised, unanswered): whether the
  kit should plant/maintain `AGENTS.md` so upgrade waves keep 19 files fresh,
  versus PKT-B4's recorded hand-write-per-repo.
