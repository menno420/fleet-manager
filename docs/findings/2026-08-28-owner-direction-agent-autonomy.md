# Owner direction, 2026-08-27→28 (second sitting) — agent autonomy, session hygiene, and the substrate-kit review round

> **Status:** `reference` · the **second** overnight 2026-08-27→28 hub sitting
> (owner-live, on the laptop — venue `local-desktop`), which ran in parallel
> with the local/cloud-sync sitting recorded in
> [`2026-08-28-owner-direction.md`](2026-08-28-owner-direction.md). That
> record's closing line — *"the substrate-kit sitting is next"* — is this
> sitting. `OWNER` throughout unless marked; his words verbatim, so the
> directives derived from them can be checked against source.
>
> **What it is NOT:** a queue, and not a design. Every mechanism sketched from
> these words is `DERIVED`, is governed by the
> [roadmap's § 6 promotion rule](../planning/2026-08-08-agent-operating-environment-roadmap.md)
> (observe → prototype → test → measure → promote, never
> idea → mandatory infrastructure), and **nothing here GOs the held execution
> packets** — OD-23's *"no execution yet"* stands.
>
> **Context:** the sitting began as a laptop question (why file search was not
> instant) and became direction after the owner, browsing his own disk to
> understand what everything is for, asked how to prevent sessions leaving
> residue. Recorded as **OD-24** in the program.

## 1 · The session-hygiene mandate — leave every touched surface better than found

His statement of the goal, from the first exchange:

> *"we should create a local skill and hook that ensures that when a local
> session is done with it's task it needs to make sure that everything it put
> on the laptop or the onedrive that does not belong there, so mostly the repo
> clones. Are then all removed again and the laptop is checked for any badly
> organized files etc. The goal should be that each session leaves the local
> disk and onedrive, aswell as all repos on github, in a better shape than it
> found them."*

And the scope rule, his own:

> *"this should only be applicable to repos that have actually been worked in
> that session. so it's not necessary for each session to go through all the
> repos, that would be too muvh to do anyways. So a local session cleans the
> onedrive and diks + any repo it worked on, and the cloud sessions just clean
> the repos they worked on."*

The session put four design questions to him; his entire acceptance,
verbatim: **"mostly all defaults with a few minor additions"** — the
additions being § 2's D override and § 3's walls correction. `DERIVED`, the
table below — and the label matters: it restates the **session's own proposal
text** that his sentence accepted, so the defaults' wording (what blocks,
what warns, the escape hatch, the audit shape) is the agent's, not his. Only
the acceptance sentence and the D-override quote are `OWNER`:

| Q | decided |
|---|---|
| **A — strictness** | default accepted: the closing hook **blocks** a session from ending while its own *objective* residue exists (unreleased claim, clone it created, missing log); judgment-flavoured findings warn rather than block. An honest escape exists for deliberately handing a clone to a next session. |
| **B — doubtful finds** | default accepted: something a sweep cannot classify is **left in place and flagged to a list**; reorganising stays a separate deliberate act, never an end-of-session reflex. |
| **C — the deep audit** | default accepted: per-session checks stay narrow (what the session touched, plus the chutes); a **periodic whole-disk audit** reports rather than deletes — a natural later fit for the always-on machine. |
| **D — repo scope** | **OVERRIDDEN — see § 2.** Not "no trace of my work" but active improvement. |

`DERIVED`, the mechanism sketch the sitting converged on (design, not build):
**deterministic detector script** at the stop/end hook moment → **judgment in
a skill** only when the detector says dirty → **detector re-run as proof**.
Hard lines carried from the laptop's own measured history: claims-aware always
(the night of this sitting, a naive cleaner would have deleted a live parallel
Claude workspace — all four `C:\dev` clones were claimed and alive), delete
only what the session itself created, Recycle Bin never hard delete, flag
don't file. The venue split follows OD-23's routing rule: hub-local sessions
sweep OneDrive + disk + repos they worked; cloud sessions sweep the repos they
worked. **Measured the same night, for calibration, not alarm:** zero stale
clones existed; the real residue found was 13 leftover pytest temp repos in
`%TEMP%` — small, but proof that unenforced discipline leaks.

## 2 · The initiative duty — his D answer, and what substrate-kit is for

> *"Especially on github I think it's important that each sessions tries to
> improve the repo in any way it can, mostly when those things are related to
> it's task but also unrelated things that it notices, and each session should
> actively participate in that. Which is mostly why I created the
> substrate-kit, so agents become more autonomous and think more for
> themselves and take more initiative."*

`DERIVED`, the executable form the sitting agreed: initiative is a duty, and
it is **bounded** — a small unrelated improvable gets fixed inline; a large
one gets **recorded** (a backlog item, a thread, a finding) so it is never
silently dropped and never derails the task either. This is OD-22's
*"take initiative to do their own research … to help solve the problems they
encountered for the next sessions"* restated as a per-session obligation.

## 3 · The freedom doctrine — walls exist by ratification, not by agent caution

> *"Sometimes this has backfired a little bit because agents really like to
> add restrictions and walls and guards, while I personally would rather make
> sure that my agents have as much freedom as I have myself, and by that I
> mean that they can edit certain settings and variables completely by
> themselves and have full access to most of my accounts. this saves me a lot
> of time and effort since a lot of context lives there."*

And his correction, when the session called the standing safety lines "his
walls, not agent walls":

> *"small correction, those walls have also been made up by agents. But I
> agreed to them so they can indeed stay, tho I'm really not too worried
> about it."*

`DERIVED`, the doctrine in one line: **default to enabling; an agent never
introduces a restriction on its own initiative; proposals are welcome and his
ratification is what makes a wall legitimate — authorship is irrelevant, and
unratified walls must not accumulate.** The ratified lines (no credentials in
files or chat; confirm before sending or deleting; unattended work that
leaves the machine, spends money or speaks in his name waits) stay. Tone
matters: he is relaxed about this, not anxious.

## 4 · The mechanism architecture — skills, hooks, and chains across sessions

His model of the two mechanisms:

> *"A skill is basically just a hook that gets invoked through a personal
> trigger word or context."* … *"ofcourse that isn't as foolproof as a hook in
> the sense that it doen't activate automatically after a certain event, but
> at the same time it's also a really good feature that allows us to dothing
> in exactly the same way each time, and we can upgrade some skills to make
> sure that one skill automatically triggers the next, or to make sure that a
> skill triggers a hook at the right moment."*

The chain, in his worked example:

> *"we could make sure that the continuation prompt tell the agent making the
> prompt to always include a certain instruction that will trigger a certain
> skill, so the next session that starts with that prompt will automatically
> use skill once it starts, and then that skill could include a certain type
> of action that triggers a hook etc."*

On the trigger gap and where rules must come from:

> *"we need to make some rules which also determine when certain actions need
> to happen and how we can ensure that it happens at the right moment, so by
> using hooks ofcourse. But the one problem is that hooks only have a few
> triggers, which can make it hard to do certain things."*

And on portability:

> *"the skills we make, and possibly also some of the hooks we make, also
> work for chatGPT, tho some of them will probably need to be a little
> finetuned based on the model it's for."*

`DERIVED`, how this maps onto the standing plan — it extends the
[roadmap](../planning/2026-08-08-agent-operating-environment-roadmap.md)
rather than replacing any of it:

- **The § 5.2 hook-moment table gains the cross-session dimension.** The
  three moments (`UserPromptSubmit`/INTENT · `PreToolUse`/ACTION ·
  `Stop`/CLAIM) cover one session; his chain adds continuity **across the
  boundary**: a `SessionStart`-moment injection ("unfinished work exists;
  invoke skill X") plus the prompt-embedded invocation his example names.
  Belt and braces — the prompt *says* it, the hook *enforces* it — because a
  prompt-carried instruction is read by a model (high but not total
  compliance) while an injection arrives mechanically. The trigger-gap he
  names is real but smaller than feared: a `UserPromptSubmit` hook can watch
  for his own trigger words and inject the matching procedure, which is
  § 4.7's intent-time routing said in his vocabulary.
- **Deterministic parts in scripts, judgment in skills** — a must-happen step
  never lives only in skill prose (§ 2's measured thesis: 116 statements,
  0 catches; rules bind when they *arrive*).
- **Chains stay short and mapped.** Two links preferred; every link
  self-announces ("invoked by X, will trigger Y"); one chains map lives with
  the kit, because the owner cannot debug a broken chain himself and the
  agent that must debug it changes every session.
- **Portability is § 1's `provider-aware, model-portable` made concrete:**
  each skill is a model-agnostic procedure core plus a thin per-agent adapter
  (tool names, invocation mechanics, declared capability dependencies).
  Hooks stay per-agent; procedures travel.

## 5 · The stepping-back experiment — why agents drifted, and the verdict

> *"I'm now just trying to get as much of my own explanations through to the
> agents as I can, this is something I haven't really done in a while, at
> least not like in the beginning, so I have also told myself that I will be
> more consistent in this where it matters, cause once I have my proper
> explanations everywhere and each project/repo has good instructions and the
> right ways to enforce them, I know that I can get a lot done without having
> to say a lot."*

> *"Right now the problem has been that I stepped back a little too far, and
> the agents forgot their purpose because I stopped reminding them of it,
> multiple reasons for that but the most important reason is that I wanted to
> find out how well the agents would currently work with the subtrate kit, in
> some ways it actually goes well, but in a lot of ways it still doesn't."*

> *"But that's not perse a bad sign, it just means we need to review it again
> and improve it."*

`DERIVED`: this is the injection thesis observed at estate scale — while he
supplied purpose by hand, sessions held course; when he deliberately stopped
(to measure the kit unattended, a real experiment with a real result), drift
returned. The fix he names is the fix the roadmap already orders: his
explanations recorded once in the right surfaces, delivered at the right
moment by mechanism, so stepping back stops costing alignment. His stepping
back was the *test*, not the failure.

## 6 · The substrate-kit review round — directed, with a method

The direction: *"the substrate kit itself needs some work to make it actually
do it's job in an efficient way"* — and the § 5 verdict, *"review it again and
improve it."* `DERIVED`, the method for the review session, honouring
§ 4 (intent first) and § 6 (promotion by measurement):

1. **Harvest drift incidents** — concrete cases where sessions forgot purpose
   or skipped method during the stepped-back window, from the committed
   record (cards, findings, review rounds), not from memory.
2. **Classify each gap:** instruction absent · instruction present but never
   injected at the moment of action · injected but unenforced · procedure
   missing entirely. The classes map to different fixes (write / route /
   hook / build), and OD-24's material above says which fix family the owner
   prefers where judgment is needed.
3. **Fix in the kit's own venue**, starting from fleet-manager's Layer-2
   threads — the
   [v1.21.0 follow-up worklist](2026-08-13-substrate-kit-v1210-followups.md)
   leads, and the kit tree still routes to its own worklist **nowhere**, which
   is itself a first-order finding for the review.
4. **Promote only what measures useful** — § 6 verbatim, because a review
   round that outputs mandatory infrastructure by default would recreate the
   wall-accretion he is correcting in § 3.

**Not scheduled here.** He said *"so I can continue this later"* — the round
is directed, its starting materials are pointed at, and its first session
should open with the intent map (§ 4.1), not with edits.

## 7 · What this record does NOT decide

- **No packet GO.** OD-23's hold stands untouched.
- **AGENTS.md plant-vs-hand-write** stays parked — now for the review round
  of § 6 rather than for "the substrate-kit sitting", which this was.
- **No mechanism ships from this record.** The hygiene detector/skill/hook
  (§ 1) prototypes on the laptop hub first, is measured there, and reaches
  the kit only through § 6's promotion rule.
- **No numeric anything** — thresholds, cadences and block-lists get decided
  at prototype time against real cases, per § 4.4's fake-precision rule.
