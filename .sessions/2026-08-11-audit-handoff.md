# 2026-08-11 · hub — commit what only the chat holds, then hand the audit over

> **Status:** `in-progress`

- **📊 Model:** identity withheld by session policy · high · docs-only
- Time: 2026-08-11 · venue: owner-live hub chat · branch
  `claude/fleet-manager-full-audit-lty31q`

💡 Session idea: a handoff prompt is the wrong home for anything that will still
be true next week. Everything in this card was about to be typed into a prompt;
committing it first made the prompt four pointers long.

Layer-2 handoff: null (fleet-manager itself)

## What is about to happen

The owner asked for a continuation prompt so the next session can **verify** the
full-read audit and continue from its findings. Running `prompt-preflight` first
turned up three things that exist only in this conversation and would have been
carried inline — which is the failure mode that skill exists to prevent:

1. **The one-PR constraint was never his.** *"The 1 PR instruction wasn't mine,
   that's probably something the previous session invented… It does not matter
   if it happens in 1 PR or 100."* `docs/current-state.md:180` records the grep
   result; nothing records the **directive**, so the next prompt would have had
   to re-carry it and the one after that would have drifted it.
2. **Four of the audit's headline seven have moved since `findings.md` was
   written** — this session's own PRs closed one and part-closed two. A session
   handed that list re-fixes what already landed and concludes the audit was
   wrong about the rest.
3. **The open-PR read gap has no home outside a closed PR's comment thread and
   fm #842's card**, both `RECORD` tier. A planned mechanism recorded only in
   records is a planned mechanism nobody builds.

## Previous-session review

⟲ fm #842 salvaged fm #838's residue and named the open-PR asymmetry in its
⚑ Owner-facing block. That was the right place to *report* it and the wrong
place to *keep* it: the card is provenance, and provenance is not a backlog.
This card exists partly to correct that.

## Close-out

### Shipped

- `docs/decisions.md` — **`[D-0016]`**, the owner-directive that work is sized by
  what is properly done rather than by pull-request count, with the measured
  grep (zero rules anywhere in `.claude/skills/`, `.claude/CLAUDE.md` or
  `docs/*.md`) as its evidence and the CONSTITUTION's "prompts are guidance, not
  orders" as what it rules out.
- `docs/audits/2026-08-10-full-read/findings.md` — a **status block on the seven**,
  measured against the tree on 2026-08-11 rather than asserted: 1 closed,
  2 partial, 4 open, each with the command that re-checks it. Plus the
  **anchor-drift warning**: this session edited four of the files the defect
  entries cite, so `path:line` anchors in those entries are re-resolved by quote,
  not trusted.
- `docs/ideas/consume-the-open-pr-signal-2026-08-11.md` — the one-directional
  protocol, captured with its honest counter-argument and route.
- `docs/current-state.md` — the fm #842/#844 recently-shipped entry that was
  missing, so the `CORE` read reflects what landed.

### Verify — real exit codes

Recorded on the flip commit, not predicted here.

### ⚑ Owner-facing

- `OQ-FM-D2-TARGET` — unchanged; still his call, and still the one thing
  blocking D2 from naming a repository.
- The audit's 101 defects remain an **edit pass nobody has started**. This
  session read, reported and recorded; it did not fix. That is the next
  session's work and the handoff prompt says so.

### Ideas

💡 The estate has a `RECORD`/`TASK` tier system and no rule about which tier a
*commitment* may live in. Three of this session's follow-ups were sitting in
`RECORD`-tier session cards, which are read as history and therefore never
actioned. A commitment recorded in a record is a commitment discarded politely.
