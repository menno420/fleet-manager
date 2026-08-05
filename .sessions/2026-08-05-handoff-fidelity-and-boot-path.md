# 2026-08-05 · hub — fix the boot path and the handoff skill that narrowed an owner's ask

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: a session skipped the document its own repo calls
*"read this if you read nothing else"* — and it did so by following the
handoff prompt correctly. The prompt was faithful to eight of nine owner asks
and narrowed the first one, because the skill that wrote it caps `READ FIRST`
at *"the minimum to act"* with no exception for a session whose job **is** the
reading.

## Previous-session review

The three-repo state audit (#761/#763) measured well and landed clean, but its
Phase 1 was scoped to what the bot audit needed rather than to the repo. The
owner caught it. Root-causing that miss is this session's work, and it lands on
the skill rather than on either session's care.

## Scope

Three fixes plus their record, all owner-directed live:

1. `.claude/CLAUDE.md` — the read path omits the two docs `current-state.md`
   names as essential, including the one it calls *"read this if you read
   nothing else."*
2. `.claude/skills/continuation-prompt/SKILL.md` — `READ FIRST` is capped at
   2–4 paths, *"not a reading list — the minimum to act correctly"*, and the
   traps delegate completeness to the boot file. Both are right for a normal
   handoff and wrong for a comprehension mandate.
3. A findings doc carrying the forensic comparison and the intent review, so
   neither lives only in chat.

## What landed

- `.claude/CLAUDE.md` — read path opens with `owner-reflection-2026-07-21.md`
  and `docs/current-state.md`, adds `PROJECT-CLOSEOUT.md` §3, flags that the
  owner queue is ~1,100 lines and must be read whole, and states that the list
  is **a floor, not a ceiling**. Owner-directed live.
- `.claude/skills/continuation-prompt/SKILL.md` — new §4b, the **comprehension
  exception**: the phrases that trigger it, name a corpus rather than a file
  list, verify the boot file rather than trust it, give the reading an
  acceptance test. Two traps added.
- `docs/findings/2026-08-05-handoff-fidelity-and-boot-path.md` — the
  clause-by-clause comparison and the intent review.
- `docs/findings/README.md` — index row.
- `docs/planning/2026-07-26-consolidation-program.md` — §7 row; this was **D2
  failing on the hub's own front door**, so it is logged as D2 (partial).

## Measured

**The comparison: 8 of 9 owner asks carried faithfully, 1 narrowed.** Several
near-verbatim. The prompt also *added* a good instruction the owner did not ask
for — review your own reassuring conclusions with Gemini — which caught a wrong
claim before it reached a document.

The failure is ask #1, the one phrased most emphatically: *"read all the
required reading order files **and more** … fully understand the repo"* became a
four-path `READ FIRST` under *"do not skip ahead"*. The prompt held both the
correct goal and the narrower imperative; **the imperative won**, which is what
imperatives do.

Root cause is the skill: `READ FIRST` was templated as *"2–4 paths … not a
reading list — the minimum to act correctly"*, and the traps delegated
completeness to the boot file. That delegation was the load-bearing error,
because `.claude/CLAUDE.md` omitted the very doc `current-state.md` calls
*"read this if you read nothing else."*

Fault apportioned three ways in the finding: the skill (root), the previous
session (held both halves unreconciled), and this one — `CONSTITUTION.md` says
prompts are guidance, not orders, and the goal comes first. I had the rule and
executed the list anyway.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run **post-commit**.
- The two closeout §3 threads were re-checked live rather than trusted:
  superbot-next #602 `open / blocked` and trading-strategy #160 `open`, both
  still unlanded 15 days after the program closed.

**Honest nulls** (carried into §6 of the finding): the docs read were
fleet-manager's top-level `docs/` and root binding files, not `docs/`
recursively (~200 further files in `planning/`, `retro/`, `research/`,
`audits/`, `prompts/`); the historical set stays deliberately excluded because
the fleet account distils it. The skill fix is **unverified in use** — its
predecessor also looked correct, and the real test is whether the next
comprehension handoff emits a corpus instruction instead of a file list.
Sibling repos' local copies of `continuation-prompt` were not checked for the
same defect.

## ⟲ Previous-session review

The three-repo audit measured honestly and landed clean, and its own §6
recorded a claim it got wrong — that reflex is working. What it did not do was
question the prompt that produced it. It treated `READ FIRST` as the boundary
of Phase 1 when the same prompt's job section asked for total comprehension,
and it never opened the skill that wrote it. The improvement is structural
rather than attitudinal: **when a prompt's operational list and its stated goal
disagree, that disagreement is itself a finding** — resolve it out loud in the
first response rather than silently picking the narrower one.

## 💡 Session idea

**Give every handoff prompt an orientation acceptance test, not a reading
list.** The fix shipped here tells a prompt-writer to name a corpus when the job
is comprehension, but "read the corpus" still has no floor — the next session
decides its own depth, which is exactly how this failed.

The durable version is a test the reading has to pass: *"you are oriented when
you can state this repo's purpose, its live state, its next step, and the one
document it says matters most — from its own docs, without asking."* That last
clause is the one that would have caught this, because the answer for
fleet-manager is `owner-reflection-2026-07-21.md` and a session that could not
name it had not finished reading. It is cheap, it is checkable in one
paragraph, and unlike a file list it cannot go stale when the docs move.
