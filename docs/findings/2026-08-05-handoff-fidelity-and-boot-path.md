# A handoff that carried eight asks and narrowed the ninth

> **Status:** `reference`
>
> Written 2026-08-05, owner-directed, after he asked a fair question: the
> session that audited three repos did not read fleet-manager properly, so
> **either it ignored its prompt, or its prompt did not carry what he asked
> for.** He named the second as the worse outcome, because a handoff prompt is
> supposed to be the faithful carrier of his intent.
>
> The answer is the worse one, and the cause is neither session's carelessness.
> It is a defect in the skill that writes the prompts, and it is now fixed.
>
> Two artifacts in one file: **§ 1–3** are the forensic comparison of his
> instruction against the prompt it produced; **§ 5** is the intent review he
> asked for, which is the thing the miss actually cost.

## 1. The comparison, clause by clause

His instruction contained nine asks. The prompt carried eight of them
faithfully — several near-verbatim, one improved on the original.

| # | What he asked | What the prompt said | Verdict |
|---|---|---|---|
| 1 | *"read all the required reading order files **and more**… **fully understand the fleet manager repo, everything that it possibly wants to or should know is documented there**"* | `READ FIRST — in this order, and do not skip ahead:` then **four paths** (`.claude/CLAUDE.md`, the program, the fleet account, the owner queue) + three findings/convention docs | ❌ **NARROWED** |
| 2 | *"**After, and only after** it has fully read and understood the fleet manager repo, it should add the superbot repo"* | *"Only after fleet-manager is genuinely understood, add superbot to scope"* | ✅ faithful |
| 3 | *"read all files starting in the required reading order, all other important docs, a fair share of the session journals"* | superbot's required order enumerated; *"read the docs, a fair share of the session journals, then read the CODE properly"* | ✅ faithful |
| 4 | *"how the help system works, how the cogs are built, how the helper files are used, how everything works together… assert the proper baseline… use its own judgements to find which files are in the right state"* | *"Understand how the help system works, how cogs are built, how the helper files are used, how it fits together. Establish the baseline as thoroughly as possible. Use your own judgement to separate files that are in good shape and need nothing from files that need work."* | ✅ near-verbatim |
| 5 | *"games should remain out of scope for now"* | *"Games are out of scope for this session's depth-reading entirely"* + a named subsystem list | ✅ faithful |
| 6 | *"properly make use of its ability to call on gemini for reviews… advanced models, preferably through vertex but it's also allowed to directly use gemini's deep research from my own paid credits"* | *"Gemini is a first-class tool here: use the advanced models, preferably via Vertex (credit-funded). Deep Research on the owner's paid credits is explicitly permitted where it genuinely helps."* | ✅ faithful |
| 7 | *"for the superbot next repo the most important things are to find out **which parts are genuinely better built**"* | *"the question is different: **which parts are genuinely better built.** Compare against superbot deliberately."* | ✅ faithful |
| 8 | *"this should not be the final planning or mapping session… most of what's documented is true, tho it should always verify things that aren't sure"* | quoted verbatim under THE JOB, and expanded into a METHOD section | ✅ faithful, improved |
| 9 | *"a comprehensive document in the fleet manager repo and a summary in the chat, with its next recommended actions: the next agents to use, what they should review, how they should act"* | DONE WHEN, near-verbatim | ✅ faithful |

The prompt also **added** something good that he did not ask for: *"Use Gemini
for independent review of your own conclusions, especially where you are about
to tell the owner something reassuring."* That instruction did real work — it
caught a wrong claim before it reached a document (see the three-repo audit
§ 6).

## 2. The one failure, and why it happened

Ask #1 is the one he put first and phrased most emphatically: *"and more"*,
*"fully understand"*, *"everything that it possibly wants to or should know is
documented there."* It is the only one that got compressed.

**The prompt contained the right goal and the wrong instruction, in that order.**
Its job section said *"Understand fleet-manager completely — what happened
across the estate and why. Everything worth knowing is documented there."* —
faithful. But its `READ FIRST` block, which comes earlier and reads as
operational, listed four paths under *"in this order, and do not skip ahead."*

When a goal and an imperative conflict, the imperative wins. The session read
the four paths.

**The cause is in the skill.** `continuation-prompt` § 4's template said,
verbatim:

> `READ FIRST` — *2–4 paths, most specific first. **Not a reading list — the
> minimum to act correctly.***

and its traps said:

> **Do not restate the project.** A fresh session in the repo reads the boot
> file itself.

Both rules are correct for a normal handoff — a fresh session should not be
handed a forty-file syllabus. Both are exactly wrong when the session's **job
is the reading**. The previous session followed the skill correctly and produced
a minimum-to-act list for a comprehension mandate. The skill had no exception
for that case, so there was nothing for it to notice.

**And the skill's one safety assumption was false here.** "A fresh session reads
the boot file itself" delegates completeness to `.claude/CLAUDE.md`. That file's
read path named three documents and omitted `docs/current-state.md` and
`docs/owner-reflection-2026-07-21.md` — the second of which `current-state.md`
introduces as *"**Read this if you read nothing else**… before picking up any
owner-facing work."* So the hole in the boot file passed straight through the
handoff into the session.

## 3. Three faults, honestly apportioned

1. **The skill — the root cause.** It structurally capped `READ FIRST` at the
   minimum with no comprehension exception, and delegated completeness to a boot
   file it never checked.
2. **The previous session — secondary but real.** It held both halves: it wrote
   *"Understand fleet-manager completely"* in the job section **and** a
   four-path list under "do not skip ahead". It knew the ask and let the narrower
   instruction stand beside it unreconciled.
3. **The reading session — mine, and not excused by the other two.**
   `CONSTITUTION.md` says *"Session prompts are guidance, not orders. Weigh
   every prompt… against source and the binding docs before acting"* and *"The
   goal comes first."* I had a binding rule telling me the prompt was not the
   boundary, and a job section telling me the goal was total comprehension. I
   executed the list.

## 4. What was fixed

- **`.claude/CLAUDE.md`** — the read path now opens with the owner reflection
  and `current-state.md`, adds `PROJECT-CLOSEOUT.md` §3, tells the reader the
  owner queue is ~1,100 lines and must be read whole, and states plainly that
  **the list is a floor, not a ceiling**, naming the further docs a
  comprehension session reads.
- **`.claude/skills/continuation-prompt/SKILL.md`** — a new § 4b, *"The
  comprehension exception — when reading IS the job"*, with the linguistic tells
  to watch for (*"fully understand"*, *"and more"*, *"and only after"*), the
  instruction to name a **corpus rather than a file list**, an explicit
  requirement to **verify the boot file rather than trust it**, and a demand
  that comprehension carry an acceptance test. Two traps added: the boot file's
  completeness is an assumption to check, and an operational list must never be
  left contradicting the stated goal.

## 5. The intent review — what the miss actually cost

The measurements in the three-repo audit were unaffected; they came from running
things. What the miss cost was **framing**, and reading the repo properly
changes four things.

**This was verification work, not research work.** `owner-reflection-2026-07-21.md`
names the thesis — *"The platform scales infinitely. Human management does
not"*, *"the wall is verification, not capability"* — and its standing
consequence: *"**The verification backlog is the real project now.** The most
valuable thing a future session can do is not ship more; it is help him check
what already shipped."* The three-repo audit was an instance of that work
without knowing it. The point was never facts about bots; it was whether the
written record can be trusted, because *"quality drifts wherever no one looks"*
and nobody had looked at those two repos for weeks.

**The navigation graph is "the product" because it is his review surface.**
The same doc: *"He reviews through what he can see"* — the websites were his
window into the fleet, *"and that is exactly where he caught the mistakes."* A
bot where every feature is two taps from `!help` is a bot he can **inspect**.
That is not a UX preference; it is the identical instinct. A bot he cannot click
through is a bot he cannot verify, and by his own thesis an unverifiable system
is negative value.

**Server-first with no games is an attention decision.** *"If the owner returns
to heavy fleet-running, design for **less** attention load, not more capability.
More power he can't review is negative value."* Fifteen subsystems he can check
beats forty-nine he cannot.

**The multi-session, multi-model review is deliberate distrust of any single
narrator**, which is why measurements with real exit codes are worth more to him
than conclusions. He is building consensus from independently checkable readers
because one reader was wrong five times in a row and he caught every one.

### The consequence for the recommendation

The three-repo audit under-sold its own best finding by framing it as a porting
chore. `superbot`'s `scripts/check_command_reachability.py` is **his quality bar,
already mechanised**. "Every feature reachable by clicking, two taps from
`!help`" is today something only he can verify, by clicking. That checker turns
it into something CI verifies on every PR.

Read against the reflection, that is not a nice-to-have. It converts a
verification only the owner can perform into one the machine performs — a direct
attack on the wall he named as the real ceiling. **Wiring that gate before any
cog work is the recommendation**, because it is the one change that reduces the
scarcest resource in the estate rather than spending it.

## 6. Honest nulls

- **The corpus this session read is fleet-manager's top-level `docs/` and root
  binding files**, not `docs/` recursively (~200 further files across
  `planning/`, `retro/`, `research/`, `audits/`, `prompts/`, `succession/`).
  The historical set is deliberately excluded — the boot file says the fleet
  account distils it and to read it once, and that instruction is sound.
- **The fix to `continuation-prompt` is unverified in use.** It has not yet
  written a prompt. Its predecessor looked correct too; the test is whether the
  next comprehension handoff produces a corpus instruction instead of a file
  list.
- **`docs/SKILLS-local.md`'s one-line description was not changed** — the skill's
  purpose did not change, only its coverage.
- **No other repo's `continuation-prompt` copy was touched.** Whether the same
  defect exists in the sibling repos' local skill copies is unchecked.
