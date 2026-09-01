# Failure → moment → mechanism (2026-09-01)

> **Status:** `plan` · plan input under OD-26 § 13 — nothing here is built. Written 2026-09-01 by the first Fable 5.1 session on the owner's laptop from a fresh clone at `cb3fc9a`; the owner chose all six defaults the same evening (A–F, see [`../../findings/2026-09-01-owner-direction.md`](../../findings/2026-09-01-owner-direction.md) § 7; four decisions in `docs/decisions.md` dated 2026-09-01). The laptop-hub copy of this folder is `OneDrive\Hub
ecords6-09-01 estate-successor-planning\`.
>

> Your idea: "incorporate multiple hooks and skills that inject the right
> rules and questions around the time where the errors happen most." The
> estate already runs on that thesis (`docs/intent.md` § 4). This map puts
> every known failure class next to the moment a machine can see it, and says
> what exists, what is proposed, and what is decided but not built.
>
> **Standing rule from your 2026-08-28 sitting (OD-26 § 13–14): mechanisms
> wait for the revised plan; document corrections do not.** Everything marked
> PROPOSED is plan input. The test each must pass (§ 20): *does it stop
> something being re-derived?*

## The map

| Moment | Hook event | What fires | Failure it targets | Status |
|---|---|---|---|---|
| Session boot | `SessionStart` startup/clear | the six reads with a missing-doc check; clone-vs-remote drift (substrate-kit #589) | skipped reads; a stale clone read as current | EXISTS — fleet-manager hook; kit section |
| **First user prompt** | `UserPromptSubmit`, first only | restate: HE SAID · ALREADY SETTLED · I INFER · LEAST SURE | a misread goal — your costliest failure (`intent.md` § 3); the 2026-08-06 "I'll start by getting oriented" reply | **BUILT + TESTED this session, file 07** |
| After compaction | `SessionStart` compact | three-line re-anchor: task · done · next | the goal drifting after context loss | BUILT, same script |
| Before compaction | `PreCompact` | append "where I am" to the session card | handoff state lost with the context | PROPOSED, design only |
| A repo or topic is named in a prompt | `UserPromptSubmit` | `route_docs` pulls the repo README or the provider doc | never finding the right doc — failure cost #2 | EXISTS in fleet-manager only; kit ships no routing (K6) |
| About to state what is true now from a dated record | `PreToolUse` Bash | TRAP-001 route: read the live surface | dated document read as current | EXISTS |
| About to write a count, an absence, a `MEASURED` tag | `PreToolUse` Write/Edit | TRAP-003/004 routes; `stamping-a-measured-claim` | claim wider than the sample; absence as evidence | EXISTS |
| **About to create a new file** | `PreToolUse` Write, new path | placement: does the folder have a README, does the path match a contract, is the filename generic | loose files, wrong room — the birth rule in decision 25 in docs/decisions.md | PROPOSED, mechanical |
| **After any edit** | `PostToolUse` | over the length cap → "split by question"; a table cell over 200 chars → "one claim per line"; the old text survives elsewhere (`change_guard` C) | long files; TRAP-008's shape; a correction that leaves copies standing | PARTLY EXISTS (`change_guard`); length and cell checks PROPOSED |
| About to `git push` or flip a card | `PreToolUse` Bash/Edit | TRAP-006/007 routes, `repeat: true` | complete before pushed; flipped while a review is unanswered | EXISTS |
| About to `rm`, `branch -D`, or move a file by hand | `PreToolUse` Bash | "use `tools/moves/archive_move.py`; run claims first" | broken citations; another agent's live work deleted (decision 35 in docs/decisions.md) | PROPOSED; the laptop already has `claims.ps1` |
| Turn end | `Stop` | owner-review: "what made you draw this conclusion?", blocks once | claims that exist only in the reply — 4 of 13 catches in the 2026-08-09 audit | EXISTS in fleet-manager only |
| Session end, after real work | `Stop`, gated on ≥ 10 tool calls | initiative loop S2: card top block, one idea disposition, archive candidates (decision 29 in docs/decisions.md), session log | leaving the repo no better; ideas lost; the hub's own rule 5 | DECIDED, not built; the hub has `journal-reminder.ps1` |
| Before merge | CI preflight | generated indexes fresh; no loose files; hard length cap; state headers dated; folder/header agreement; a positive-control fixture per checker | the companion record the diff owes (13 repos); a guard never seen red (10 repos) | PROPOSED checkers |
| About to write a limitation | `PreToolUse` Write | `recording-a-wall` → CAPABILITIES step 0 | false walls | EXISTS |

## What the map shows

- **Seven of the fifteen moments already have a mechanism — in one repository
  of twenty.** The kit's four-event hook channel is wired in 18 of 20 repos and
  carries none of them. Moving routing into that channel (K6 in file 05) is
  worth more than any single new hook.
- **Two moments were empty and are the ones you named:** the first prompt and
  the moment after compaction. Both are covered by one 120-line script now.
- **Hooks deliver reminders; checkers deliver reds.** A reminder at write time
  plus a red in preflight is the pair that worked here (`owner-comments`,
  TRAP-002). A reminder alone is what 116 statements were.
- **A hook cannot make a model comply.** It can make the instruction arrive at
  the right moment, in the channel the model reads. The measurement that
  matters afterwards is the one the estate already uses: did the first reply
  carry the four lines, counted across sessions from the hook's own log.

## Skills versus hooks — where each belongs

| Use a hook when | Use a skill when |
|---|---|
| the moment is a tool call, a prompt, a turn end | the work is a procedure with judgement in it |
| the check is mechanical or the reminder is short | the session must invoke it deliberately (`intake`, `session-close`) |
| the session may not know it needs it | the task is recurring and named in the routing table |

The gap the estate keeps measuring: a skill binds only a session that invokes
it. The restate lived in `intake` and in prompts; it now arrives by hook.

## Correction, same evening — the one-repo hook placement is deliberate

Menno, live (2026-09-01): *"it was deliberate that only one repo has these
hooks etc. I always use fleet-manager as the root repo for a cloud session. So
all the hooks and skills get loaded every time, if a session later adds another
repo to its scope that does not remove the functionality of the hooks and
skills. Only if I personally attach 2 or more repos to a session at start then
the hooks and skills do not load."*

So "in one repository of twenty" above is a design choice for cloud sessions,
not a gap. What remains uncovered by design: a session started with two or
more repos attached, a Codex or ChatGPT Work session, and a local session
opened directly in a repo clone on this laptop. And `estate` inherits the role:
it must become the root that carries the hooks, or nothing does. K6 in file 05
is therefore about those residual venues and the successor, not about
fleet-manager today.
