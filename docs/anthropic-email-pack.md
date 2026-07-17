# Anthropic email pack — capability self-knowledge (owner draft)

> **Status:** `owner-guidance`
>
> Living pack for the **next** feedback email to Anthropic (the 2026-07-14 final
> email was a separate, already-sent artifact — [eap-final-email-draft-2026-07-14.md](eap-final-email-draft-2026-07-14.md)).
> This doc is the durable home the owner-queue "Anthropic email pack" pointer
> references. The body below is safe to send as-is; provenance sits in the
> supporting-evidence section under the copy block (not inside it).

## What to send, where

Reply on the existing Gmail EAP thread ("Claude Code Projects Review" / claude-code@anthropic.com) with the block between **COPY FROM HERE** and **COPY TO HERE**. It is fully self-contained — a reader who opens only the email understands the problem, the evidence, the ask, and the one-line fix. Nothing else needs to be attached.

---

## COPY FROM HERE

**Subject:** Sessions can't answer "what can I do?" — a self-knowledge gap that cost me real time

Hi Diana,

One more piece of feedback from running Claude Code as an agent fleet, and it's a small fix with a big payoff. **My sessions can't reliably tell me what they themselves are able to do.** I keep having to explain, session after session, that auto mode doesn't read `settings.json`, or that yes, they *can* create scheduled routines — these are basic self-knowledge questions an agent should be able to answer about itself, and today it often gets them wrong. Here is exactly what happened this week, with the receipts.

**What happened (one representative case, today).** A seat needed to arm a failsafe wake timer. It first concluded it had *no scheduling tool at all* — because the scheduling tools (`create_trigger`, `send_later`) are **deferred**: they load only through a tool-search step and never appear in the session's visible tool list. Absence from that list is not absence of the tool, but the agent read it as "I can't do this" and reported a false wall.

It then tried a shell fallback, which the safety classifier denied, verbatim:

> "Permission for this action was denied by the Claude Code auto mode classifier. Reason: Blocked by classifier. ... To allow this type of action in the future, the user can add a Bash permission rule to their settings."

That hint is **misleading**: auto mode doesn't read `settings.json`, so it points me at a remediation surface that has no effect — I'd edit the file, nothing would change, and I'd have no idea why.

Finally the seat loaded the tool properly and called it natively — and it **worked the first time**: it armed a two-hourly failsafe (`trig_01Bo7dZxM9xz2hwR36L424Z8`, "Fleet Manager failsafe wake", cron `30 */2 * * *`, enabled, bound to the coordinator session) and, separately, repeated short-horizon pacemaker timers (`trig_01HvbDCuRZqrZQVW3DqAwEot`, `trig_01SEE6hs3W4Tc6KhHRWH68Eq`). So the capability was there the whole time; the session just couldn't see that it had it.

Two more things I saw the same session, both of which make self-knowledge harder:

- **The classifier is nondeterministic.** The same `list_triggers` call succeeded, then was denied seconds later — identical call, opposite verdict. An agent can't build a stable picture of "what I can do" against a moving line.
- **A connector-passthrough gap.** Triggers created this way store no MCP connectors, so any *brand-new* session such a trigger spawns comes up without connector tools. (It's moot when the trigger fires back into an existing session, but it's a real gap for fresh-session-per-fire routines, and nothing tells the agent this up front.)

**What I'd ask you to fix:**

1. **Let a session answer "what can I do?" accurately.** Expose the session's *full* tool inventory — including deferred / tool-search-only tools — to the agent's own self-inspection, so it stops declaring false "can't"s about tools it actually has.
2. **Make denial messages name the true remediation surface.** If auto mode doesn't read `settings.json`, don't tell the user to edit `settings.json`. Point at whatever actually governs the decision.
3. **Make permission decisions deterministic** — or at least idempotent for identical calls. Success-then-denial flapping on the same call is the opposite of something an agent can reason about.
4. **Fix the routines observability bugs I reported earlier** (they compound the same self-knowledge problem — an agent can't know its scheduling state if the panels disagree): routine runs aren't inspectable owner-side; the Runs panel and the Routines screen disagree; arming behaves inconsistently across seats; and a routine's model attribution differs across three surfaces (Routines menu, fired-session header, the session's own committed record).

The through-line is simple: **an agent should have accurate, stable self-knowledge of its own abilities.** Right now the visible tool list is partial, the denial hints misdirect, and the verdicts move — so every session re-learns its own capabilities from scratch, and I end up filling the gap by hand.

Happy to share the full evidence trail or demo it live.

Best,
Menno

## COPY TO HERE

---

## Supporting evidence — trigger ids, verbatim quotes, provenance

Every claim in the copy block ties back to one of these. All are recorded in [`docs/CAPABILITIES.md`](CAPABILITIES.md) (the seat's verified can/cannot ledger) and its 2026-07-17 wake-chain UPDATE / the ToolSearch standing lesson landed in PR #294 — cross-referenced here, **not** duplicated.

### 1 · Deferred-tool invisibility → false "can't"
- `create_trigger` and `send_later` are **deferred** (tool-search-loaded); they do **not** appear in the visible tool list. The seat read that absence as tool-absence and reported a false "no direct scheduling tool."
- Standing lesson (CAPABILITIES.md, PR #294): *before declaring a tool absent, tool-search for it — absence from the visible list is not tool absence.* Referenced, not restated.

### 2 · Misleading classifier denial hint (verbatim)
> "Permission for this action was denied by the Claude Code auto mode classifier. Reason: Blocked by classifier. ... To allow this type of action in the future, the user can add a Bash permission rule to their settings."

Per the owner, **auto mode does not read `settings.json`** — so the hint names a remediation surface that does not apply. Recorded at CAPABILITIES.md § wake-chain (2026-07-17).

### 3 · Native MCP call SUCCEEDED — the capability was there
- Failsafe armed: `trig_01Bo7dZxM9xz2hwR36L424Z8` — "Fleet Manager failsafe wake", cron `30 */2 * * *`, enabled, next `2026-07-17T22:36Z`, coordinator-bound, `persist_session: true`.
- Pacemaker `send_later` timers armed repeatedly, e.g. `trig_01HvbDCuRZqrZQVW3DqAwEot`, `trig_01SEE6hs3W4Tc6KhHRWH68Eq`.
- Hygiene that made it work: load the deferred tool via tool-search, call it **natively** (never via Bash), one trigger-MCP call per worker, fresh worker per call.

### 4 · Classifier nondeterminism
- An identical `list_triggers` call **succeeded, then was denied seconds later** — same call, opposite verdict. Treat a denial as retry-later (retry once from a fresh worker), not a wall (CAPABILITIES.md, 2026-07-17 UPDATE).

### 5 · Connector-passthrough caveat
- Triggers created via `create_trigger` store **no MCP connectors**, so any **new** session they spawn runs without connector tools. Moot when firing into an existing session; a real gap for fresh-session-per-fire routines.

### 6 · The four routines platform bugs (ask #4 — folded from the 07-14 pack)
Carried forward from [eap-final-email-draft-2026-07-14.md](eap-final-email-draft-2026-07-14.md) appendix theme #3 and the owner-queue "Anthropic email pack" item; evidence in [`docs/CAPABILITIES.md`](CAPABILITIES.md) § routine self-arm rider:
1. **Routine runs are not inspectable** owner-side — the committed heartbeat is the only readable record; trust git, not the panels.
2. **Runs panel vs. Routines screen disagree** on state.
3. **Arming is seat-inconsistent** — the same call is pre-granted in one seat, prompts/denies in another.
4. **Model attribution is inconsistent across three surfaces** — Routines menu (shows fable-5 for all project-created routines), fired-session chat header (showed "Sonnet 5"), and the fired session's own committed card (self-reported `claude-sonnet-5`) — with no authoritative panel and no model parameter on `create_trigger`.

---

## Self-knowledge crib — what every session should already know

The short list the owner asked for, so no session has to be told these again (keep current; source of truth is [`docs/CAPABILITIES.md`](CAPABILITIES.md)):

- **Auto mode does not read `settings.json`** — a denial hint pointing there does not apply; don't act on it.
- **You CAN create routines / triggers** via native MCP (`create_trigger`, `list_triggers`, `send_later`) — they are **deferred**, so tool-search to load them first, then call them **natively** (never via Bash).
- **The visible tool list is partial** — deferred / tool-search-only tools exist and are usable; absence from the visible list is **not** tool absence.
- **The permission classifier is nondeterministic** — an identical call can succeed then deny; treat a denial as retry-later (retry once from a fresh worker), not a wall.
- **Merges land server-side, not agent-side** — open PRs ready with green CI; the repo's lander workflow (or the owner) merges. Agents do not arm auto-merge or REST-merge (classifier-denied since ~2026-07-15).
