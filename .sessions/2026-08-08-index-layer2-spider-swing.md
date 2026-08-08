# 2026-08-08 · hub — Layer 2's first folder, built once so the shape can be judged

> **Status:** `complete`

- **📊 Model:** opus-5 · high · feature build — the index restructure, one repo

Time: 2026-08-08 · venue: owner-live hub chat · branch
`claude/fleet-manager-index-gq7lfw`

💡 Session idea: **the first instance of a repeated shape is the only cheap
place to be wrong.** The design names a five-file folder as a *starting shape*
and explicitly asks each repo to earn its files. Building five folders to that
shape and then discovering two of them are redundant costs five rewrites;
building one costs none. So the deliverable is not "spider-swing is documented"
— it is **a shape the owner can accept or reject after seeing it filled with
real content.**

## Previous-session review

The design session (fm #817) recorded the decisions and their reasons, including
three reversals, which is what made this session a build rather than a
re-litigation. Two things it left for here, both correctly: which files a Tier-1
repo actually needs, and whether `UserPromptSubmit` can carry retrieval.

It also left **#817 itself `dirty`** — the branch carried the design doc behind a
merge conflict, so the document that "supersedes anything else that conflicts"
was not on `main`, and a fresh session following the read path could not reach
it. Landed first, for that reason. Both conflicts were artefacts of #816 landing
as a squash, not content disagreements; the telemetry union was verified lossless
(main's 5,782 lines a strict subset of the branch's 5,874).

## What shipped

**Layer 2, one folder deep** — `docs/repos/spider-swing/`:

- `README.md` — the standalone entry: what it is, where it stands, **four thread
  blocks** (core feel & difficulty *active* · Play release *active, owner-gated* ·
  run evidence *closed 2026-08-06* · art pipeline *paused*), whether to attach at
  all, and the per-repo boot path once attached.
- `capabilities.md` — what is verified about **reaching it from here**,
  deliberately not about its internals (that is its own ledger's job).
- `records.md` — the 28 dated files in this repo that mention it, indexed **where
  they sit**; nothing moved.
- `working-here.md` — gates, verify commands, traps. **Marked as a proposal**,
  because whether this earns a distinct file is the owner's call.
- `current-state.md` and `goals.md` **DEFERRED, with reasons recorded in the
  README** rather than silently omitted.

Plus `docs/repos/README.md` (structure, thread convention, honest coverage, and
why this is not `projects/`) and `docs/repos/ACCEPTANCE-TESTS.md`.

**Retrieval** — `route_docs.py` now runs on `UserPromptSubmit` as well as
`PreToolUse`, so naming a repo pulls its README in *before* the work starts.
`install_root_hooks.py` registers both events.

**Two Layer-1 gaps** — a 27-skill roster in `docs/SKILLS-local.md`, and `@codex`
in the boot file.

## Measured

**The payload key was verified, not assumed.** The prompt that set this work
warned not to assume `UserPromptSubmit` delivers its text under the same key as
`PreToolUse`. It does not, and the public hooks reference does not publish the
field. Read out of the shipped binary (`/opt/claude-code/bin/claude`, not
stripped), which builds the payload as
`{...,hook_event_name:"UserPromptSubmit",prompt:e,...}` — a **top-level `prompt`
key**, no `tool_input` at all. Six hook cases run directly against the script,
all as expected: fires on the repo name and on the publishing name, silent on an
unrelated prompt, **silent when only `cwd`/`transcript_path` contain the repo
name**, no `PreToolUse` regression, exit 0 on malformed stdin.

Prompt routing is **opt-in per route**. Adding the event to `DEFAULT_TOOLS`
would have switched all 21 existing probe routes onto the owner's prose at once
— patterns written for shell commands and URLs, suddenly matching conversation.

**The skills gap was three defects, not one.** The design recorded
`SKILLS-local.md` as naming 13 of 27. True, and the count hid the causes:
`rationalize` and `scope-backlog-item` were in **no index at all** — installed,
invocable, undiscoverable except by listing the directory. `chase-references`
and `prep-owner-steps` were indexed in `SKILLS.md` as living in **superbot**,
stale since the kit shipped them. And neither file stated its own scope, so a
session reading one had no signal the other half existed. **An index that does
not state what it covers reads as complete** — the same failure as a wall that
reads as measured.

**spider-swing's own ledger corrected the picture this repo had.** From here the
obvious story was "the Play submission is the thread". Its `docs/current-state.md`
carries an owner directive of 2026-08-02 making **core feel and difficulty** the
north star, with unlocks, Campaign trees and monetisation *deferred* until the
core loop is right. Both threads are live and they are in tension: the game is
still *"too difficult and moves too quickly"*, and the closed test is a hard
three-week floor. A folder written only from fleet-manager's records would have
pointed the next session at the wrong one.

**Access re-measured rather than transcribed** — the 2026-07-31 proxied-vs-direct
table reproduces exactly at 2026-08-08, including `branches/main/protection`
returning **404 direct / 403 proxied**. The 404 is the true answer and reads like
an absence of protection; spider-swing's `main` in fact requires **two** checks
(`substrate-gate` **and** `game-quality`, ruleset `main-required-checks`), read
from the rulesets endpoint. fleet-manager requires one. That difference is now
written where a session will meet it.

## Verification

Real exit codes, each command run on its own — never `$?` after a pipe:

- `python3 bootstrap.py check --strict` → **exit 0** (born-red hold cleared by
  this commit; sole prior finding was that hold).
- `python3 tools/check_doc_routes.py --strict` → **exit 0**, 22 routes · 18 docs
  routed · 0 errors · 0 notes.
- `python3 tools/check_no_false_walls.py --strict` → **exit 0**, CLEAN across 5
  living/binding docs.
- `python3 tools/check_no_false_walls.py --selftest` → **PASS**.
- `python3 tools/install_root_hooks.py --apply` → idempotent on re-run
  ("already installed — nothing to do"); the `Stop` hook is untouched.
- **The two invocations CI actually runs**, after the first red:
  `check --strict --session-log .sessions/__born-red-card-added__.md --added-card <card>`
  → **exit 0**, and `check --strict --require-session-log --session-log <card>`
  → **exit 0**.
- Acceptance test 1 → **14/14** answerable from the folder with the repo
  unattached. Acceptance test 2 → **partial**, correct on the one folder that
  exists. Both recorded at `docs/repos/ACCEPTANCE-TESTS.md`.

## The one red, and why local green did not predict it

`MEASURED` this session. `substrate-gate` failed on PR #818 while all three
gates were green locally. Cause: the card's `📊 Model:` line read
`... · build — ...`, and **`build` prefix-matches none of the 9 PL-004 task
classes** — the taxonomy word is `feature build`.

The part worth carrying is *why local was green*. **`bootstrap.py check
--strict` does not run the card-grammar check; only the added-card gate does**,
and CI reaches it through an invocation a session never types by hand:

```bash
python3 bootstrap.py check --strict \
  --session-log .sessions/__born-red-card-added__.md --added-card <card>
```

So the local ritual and the CI gate were checking different things, and the
local one is the weaker. The gate's own output says so in passing — a NOTE that
`scripts/preflight.py` is absent, *"plant one to converge the local ritual and
the CI gate on one check list"*. Nothing was built for that here (it is a gate
change and out of scope), but the divergence is now written down with the exact
command that reproduces CI, which is the cheap half.

Also worth noting for the next reader: the failing line was **`check: 1
finding(s):`** sitting above ~80 lines of never-exit-affecting `[stale-wall]`
and `[dateless-wall]` advisories. A 60-line log tail showed only advisories and
`exit code 1`, which reads like the advisories caused it. They did not. Read up
to the `finding(s):` header, not the tail.

## Honest nulls

- **Test 2 cannot fully pass yet** and is recorded as partial, not as a pass. It
  exercises *every* folder by definition; one exists. The coverage table makes
  the other 23 visibly absent rather than silently missing, which is the most
  that can be true today.
- **Test 1's mechanical half proves the answers are present, not that they are
  good.** The qualitative judgement is `REASONED` and mine. The real
  falsification — an unprimed reader who has never seen the repo — has not been
  run.
- **The `UserPromptSubmit` route has not yet fired in a live session**, only
  against piped payloads. Its first real firing will be the next session that
  names a repo. The `PreToolUse` half of the same route *did* fire live this
  session.
- **`working-here.md` is a proposal**, and the survey/attach questions in § Open
  are genuinely open. Nothing here should be replicated to a second repo before
  the owner has looked.
- **Only one repo's folder was built, by instruction.** The other four Tier-1
  repos and ~19 Tier-2 stubs are untouched.

## Post-merge correction — the owner asked how much of the repo I actually read

`MEASURED` 2026-08-08, after #818 merged. The honest answer is **three files,
partially — about 180 lines** of a **732-file** repo (305 markdown / 2.12 MB,
120 under `game/`, 76 GDScript, 207 assets, 142 session cards): its
`docs/current-state.md`, `docs/reading-path.md` and the newest session card,
plus complete structural metadata from the API and 28 files read properly *here*.

Asking the question was worth more than the answer, because checking it found
**three wrong claims** in the shipped folder — all of the same kind: a one-line
description of a file this session never opened.

| claim as shipped | what the file actually says |
|---|---|
| `docs/AGENT_ORIENTATION.md` "how an agent is expected to work in it", and in `working-here.md` "the real instruction set" | it is the **task reading-router** — it tells you which docs a task needs. It routes; it does not instruct |
| `docs/decisions.md` "the decision ledger (ADRs)" | append-only ledger citing bare **`[D-NNNN]`** ids |
| `docs/architecture.md` listed as ordinary reference | badge is **`binding`** — a second binding contract, which `working-here.md` had omitted from the pair that outranks it |

Two claims that *were* second-hand held up on check: `posmod(tile_index, 2) == 1`
is real at `game/presentation/scripts/swing_lab.gd:420` (quoted here from a
fleet-manager finding, never from the file until now), and `tools/verify.py`
exists (HTTP 200) though its behaviour is still described from spider-swing's
prose rather than from the script.

**The generalisable bit:** existence and badge are cheap to verify and were not
verified; *"what it is"* for an unopened file is an inference that reads exactly
like a fact. The folder now carries a § "How much of the repo this was built
from" stating its own basis, so the next reader can weight the pointer lines
differently from the state lines.

## The rule, and the hook the owner asked for

`OWNER`, 2026-08-08: the read-before-you-describe lesson belongs in
fleet-manager's own working explanation, *"something we should probably enforce
with a hook."*

**The doctrine** is now a bullet in `.claude/CLAUDE.md` § working style, carrying
the measurement rather than just the instruction — 0/3 wrong when read, 3/5
wrong when not, and the reason it needs a mechanism: an unread description reads
exactly like a read one, so it survives every downstream check.

**The hook** is `.claude/hooks/read_before_write.py`, advisory and fail-open,
registered `PreToolUse`. It records the paths a session fetches and flags prose
describing paths it never fetched.

**The split that keeps it honest.** The owner's rule has two halves — *read* and
*understood*. Only the first is a fact and only the first is mechanised. The
second is a judgement, and this estate has withdrawn two gates for trying to
mechanise meaning. So the hook never blocks, and **a quiet hook is not evidence
of anything**; only a firing one carries information. That asymmetry is written
into both the hook's output and the boot-file bullet, because an advisory that
reads as an all-clear is worse than none.

**Two defects found by testing against real files rather than fixtures**, both
of which would have made it useless in a different direction:

1. Matching on tool *results* let a directory listing launder a filename into
   "read" — `ls docs/` made the hook believe `decisions.md` had been opened,
   which is precisely the file it needed to catch. Fixed: record tool **inputs**
   only, and the 3/3 detection above is measured under that rule.
2. It went **silent on `records.md`'s 25 described paths**, because markdown
   link syntax hid the path from the describing pattern. For an advisory, a
   silent miss is the worst available outcome. Fixed by collapsing `[x](y)` to
   its label first; output stays bounded at 5 + a count.

`tools/install_root_hooks.py` is now table-driven over both hooks rather than
hardcoded to one, so the case-three rescue path installs the whole apparatus.

**Correction, same session:** the card and PR #820 first said *"the hook has not
fired in a live session — only against piped payloads,"* reasoning that hooks
load at boot and this one was registered mid-session. **That was wrong, and it
was an inference stated as a fact — the exact failure this hook exists to catch,
committed in the paragraph describing the hook.** Checked instead of assumed:
`/tmp/claude-read-set/<session>.json` exists for this session, written at
11:50:37 against a registration at 11:44:27, holding **30 recorded paths.**
**Hooks do reload mid-session** in this environment; the boot-triad claim covers
which `.claude/` tree is *found*, not whether a live edit to it takes effect.

So the accurate statement: it is **live and recording**, and it has **reported
zero times** — it has had no cause, because every file described since it went
live had been opened. Its first real *firing* is still ahead.

**And the thing it has never done, by construction: block.** The script has no
`permissionDecision` path anywhere in it; every branch returns 0 with at most an
`additionalContext` note. The `PreToolUse` schema in the shipped binary does
carry `permissionDecision` + `permissionDecisionReason`, so hard-denying a Write
is available and deliberately unused — see the owner question below.

## Open owner questions

Three, none blocking — the folder stands either way.

1. **Does a folder carry "how to work here" as a distinct file?**
   `working-here.md` exists so the question is concrete. It is what a session
   needs *before* attaching and it is neither state nor goals — but it could
   fold into `README.md`.
2. **In the survey, should a repo with no active thread appear at all?**
   Silence and "nothing active" are different answers and the owner is choosing
   work from this. Current shape shows everything and marks the empties.
3. **Was deferring `current-state.md` and `goals.md` right?** The reasoning is
   recorded in the folder; both are one commit away if the answer is no.
