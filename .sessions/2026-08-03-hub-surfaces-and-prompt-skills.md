# 2026-08-03 · hub — execution surfaces documented, kit skills actually installed, four prompt skills added

> **Status:** `complete`

- **📊 Model:** opus-5 · high · feature build — skills + surface research

Time: 2026-08-03 · venue: owner-live hub chat (owner asleep, autonomous stretch)
· branch `claude/agent-surfaces-and-prompt-skills`

💡 Session idea: **the estate's skills were documented, staged and unreachable —
and nothing in the system could tell.** `docs/SKILLS.md` described fourteen skills
and named `.claude/skills/<name>/SKILL.md` as the live location; `cmd_skills`
writes only to `.substrate/skills/` and says in its own docstring that the kit
*"never writes a live `.claude/` tree"*. The install step in between belonged to
the host and nobody ran it, so for the whole life of this repo the skill index
described a set that could not be invoked.

The generalisable part is not "install the skills". It is that **a handoff
between two systems that each believe the other owns a step is invisible to
both** — the kit correctly reported staging, the index correctly described where
bodies live, the gate correctly checked skill grounds against files it found, and
none of them was positioned to notice that the last copy never happened. A guard
that would have caught it is trivial and does not exist: `check` already reads
`.claude/skills/` and `.substrate/skills/`, so it could compare the two sets and
warn when the staged set is not installed. **Worth proposing upstream** — this
class of gap will exist wherever the kit stages and a host installs, which is
`render`, `skills`, and `agents` alike.

## previous-session review

`2026-08-03-hub-pat-is-environment-scoped.md` closed on *a ledger entry has an
implied audience, and this ledger's entries do not say who it is* — a recipe whose
precondition is unstated reads as a wall to whoever lacks it. Directly applied
here: `docs/execution-surfaces.md` is a capability comparison whose whole risk is
being read as a routing table, so it opens by saying it is not one, and every
prompt skill checks preconditions rather than asserting them. The three cards
before it each pitched their lesson one level too narrow; this one deliberately
states the guard as a *class* (staged-vs-installed, all three kit stagers) rather
than as the single instance that produced it.

## Scope (owner ask, five parts)

1. How does ChatGPT Work operate, and can variables be added the way they can in
   Claude Code environments?
2. Research the advised ways to use AI agents generally.
3. Document each surface's strengths and weaknesses in this repo.
4. Build skills focused on prompt creation and session handoffs, adapting to the
   surface a prompt is aimed at.
5. Read the owner's ChatGPT prompt project if it is reachable.

## What landed

- **`docs/execution-surfaces.md`** — the capability comparison, opening with an
  explicit "this is not a routing table" so it cannot be read as role assignment.
  Nine comparison rows, the four that actually change prompt wording, measured
  strengths and weaknesses per surface, and cited external guidance with the
  parts that match local measurement marked.
- **`.claude/skills/`** — the fourteen staged kit skills, installed. They appeared
  in the session's available-skills list immediately, confirming the diagnosis.
- **Four local skills** — `prompt-preflight`, `continuation-prompt`,
  `implementation-prompt`, `decision-capture`.
- **`docs/SKILLS-local.md`** — index for hand-authored skills, kept separate
  because `SKILLS.md` regenerates and would drop a hand-added row.
- **`docs/CAPABILITIES.md`** — three entries: skills staged-not-installed;
  ChatGPT Work environments take variables (with the three defaults that break a
  prompt written elsewhere); the project-URL Cloudflare challenge with its
  refutation recipe and the verified per-chat workaround.

## The owner's questions, answered

**Can variables be added on the other surface?** Yes — and the three defaults
around them are what matter. Environment variables persist for the full duration
including the agent phase; **secrets do not** (removed before the agent phase
starts); **`export` in a setup script does not persist** into the agent phase; and
**agent-phase internet is off by default** while setup-phase internet is on. So a
credential the task itself needs must be a *variable*, not a secret, and anything
needing the network belongs in *setup*.

**Could the prompt project be read?** No — HTTP 403 behind a Cloudflare
interstitial, where the `/share/` route on the same host serves normally. Project
sharing is workspace-scoped rather than a public link. The workaround is verified:
share an individual chat from inside the project and send the `/share/` link.

**What belongs in a prompt versus a pointer?** One rule, now the spine of all four
skills: *the prompt carries what is not in the repo; the repo carries the rest.*
Pointers stay true when the repo moves, inlined copies rot and then outrank the
file they were copied from, so the only things that belong inline are the ones a
fresh session cannot recover — decisions made, options rejected and why, and
constraints stated aloud but never written down. When that payload grows, the fix
is a commit, not a longer prompt: `decision-capture` exists to make that the easy
path.

## Honest nulls

- **The prompt project could not be read**, so the owner's existing prompts were
  not used as reference. The skills are built from this estate's measured failures
  and cited external guidance instead.
- **Whether a Codex agent-phase step sees spider-swing's setup exports is
  unverified** — no run was observed. Flagged in the surfaces doc as the highest-
  value next check, since `~/.bashrc` only reaches a shell that sources it and
  `CLAUDE_ENV_FILE` does not exist on that surface.
- **Neither repo has an `AGENTS.md`**, the file both surfaces read natively.
  Noted, not created — that is a change to how every session boots and belongs to
  the owner, not to an autonomous stretch.
- **The four new skills have never been invoked.** They are written from evidence
  and are untested as skills.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```

Last run: gate green after the flip (skill-grounds advisories cleared to zero by
fixing an exemplar path that existed only in another repo); false-walls `CLEAN`.
