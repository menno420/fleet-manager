# 2026-08-31 — the SessionStart orientation hook, and the review hook's silent skip

> **Status:** `complete` — the hook is registered on both surfaces and verified
> on every `source` value plus casing variants, an unrecognised value and three
> malformed payload shapes; the owner-review no-key branch is countable.
> **Three** Codex rounds (13 findings, all `[conceded]`) and two free-key Gemini
> passes. Rounds 1–2 landed in fm #992; **round 3's four fixes landed separately**
> — see § The merge race below.

- **📊 Model:** withheld · high · feature build
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01CASNahqzfFmdGJYP2tmk46](https://claude.ai/code/session_01CASNahqzfFmdGJYP2tmk46) · "Hook usage review and improvements"

💡 Session idea: a hook's *firing* is the only cheap proof that the apparatus
loaded at all. The boot triad's dangerous cases — root is a satellite repo, root
is the bare clone parent — are both silent, and a session cannot distinguish
"the rule did not apply" from "the rule never arrived". A `SessionStart` hook
that speaks at boot converts that silence into one observable line.

## Mission

The owner read [an XDA article](https://www.xda-developers.com/added-one-hook-claude-code-stopped-same-mistake-twice/)
on a `Stop` hook that injects a mistakes checklist, and asked how it compares to
this estate's hooks and what is still missing. The comparison found this repo
already ahead on the article's own mechanism (`owner_review.py`, 2026-08-07, with
a measured argument the article never reaches) and behind on two things it does
not discuss.

Two of the four ranked gaps were approved for this session:

1. **A `SessionStart` orientation hook** — `docs/findings/2026-08-29-estate-agent-error-audit.md:259`
   already measured its absence (*"`fleet-manager` wires no `SessionStart` hook"*),
   and OD-24 §4 names the event as the cross-session chain's seam. The six-read
   cold-orientation mandate has failed at least three recorded times, and each
   repair was another paragraph of prose — which `docs/intent.md` § 4 names as
   the wrong move.
2. **The owner-review hook's unlogged no-key branch** — `_free_review` returns a
   bare `None` when `GEMINI_API_KEY` is absent, which is the one path producing
   the `{"route":null,"enriched":false,"error":null}` signature the hooks README
   banner recorded on 2026-08-26 and left undiagnosed.

**Non-scope, deliberately:** the other two ranked gaps — a `SubagentStop` review
round, and promoting TRAP-006/007 to Stop-time state checks. Both are real and
both are larger design questions; they are recorded for a later session rather
than bundled here.

## Previous-session review

Read the three most recent cards on `main`. `2026-08-30-fresh-start-structure-sitting`
and `2026-08-30-independent-fresh-start-review` establish the live context that
matters here: **[D-0025] redirected the execution target to a fresh `estate`
hub, and this repo becomes the read-only archive.** That is the strongest
argument *against* this session's work, and it is answered rather than ignored —
see § Why build into an archive below.

## Why build into an archive

The redirect makes fleet-manager the archive *of the program*, not a repository
that stops being booted. Sessions still boot here — this one did — and the
orientation failure the hook addresses is a boot-time failure, so it is live for
exactly as long as anyone boots this repo. The hook is also the first working
instance of the `SessionStart` injection OD-24 §4 asks for, in the one repository
of twenty that has a `.claude/hooks/` directory at all (`MEASURED`, the error
audit § 4), which makes it the natural place to prove the shape before the fresh
hub inherits it.

## What the next session needs to know

**What landed.** `.claude/hooks/session_start.py` — the estate's first
`SessionStart` hook — plus a countable no-key branch in `owner_review.py`, and
two stale counts removed from `docs/MAP.md`. PR
[menno420/fleet-manager#992](https://github.com/menno420/fleet-manager/pull/992).

**The review record, because the shape of it is the finding.** Four Codex rounds,
**18 findings, 18 `[conceded]`, 0 `[survived]`** — and the striking part is that
**most of every round after the first was defects in the previous round's
fixes**: 3 of round 2's 5, 1 of round 3's 4, 4 of round 4's 5.

| round | finding | class |
|---|---|---|
| 1 | reads resolved from `CLAUDE_PROJECT_DIR`, breaking the rescue path | wrong on the surface it was built for |
| 1 | unrecognised `source` fell to WARM against three documented promises | code contradicted its own docs |
| 1 | missing-doc list computed, then used only on the cold path | dead code path |
| 1 | `docs/MAP.md` hook count stale | count-in-prose |
| 2 | `_root_note` asserted *which* root caused a mismatch | over-claim on top of a round-1 fix |
| 2 | the round-1 fix silently disarmed the advertised positive control | **a control that cannot fail** |
| 2 | `_present` accepted a directory as a document | claim-not-matched-by-code |
| 2 | `MAP.md` line 65 still stale after line 37 was fixed | fixed the instance, not the class |
| 2 | wrong-shape JSON exited 0 unlogged | **the exact defect this file criticises `owner_review.py` for** |

| 3 | `.lower()` widened the warm set past the documented values | code contradicted its own docs, again |
| 3 | the positive control proved less than the table claimed (`grep -c` exits 0 on 1–5) | **a control that under-proves** |
| 3 | the README still carried the multi-root diagnosis round 2 removed from the code | one-surface fix |
| 3 | "fires once per session by construction" hid the compaction population | claim outran evidence |

**Three bolded rows**, and they are the ones worth carrying forward. Each is
*the same mistake as the thing being built* — a hook whose header argues that an
uncountable skip is the worst failure mode shipped an uncountable skip, and a
commit that published a positive-control result broke that control in the same
diff. **None was catchable by testing the feature; each needed someone asking what the
guard itself was worth.**

**Convergence, since that is the stop condition.** Round 1 found a broken rescue
path; round 2 found an unlogged crash handler and a disarmed control; round 3
found one small code nuance and three claims that outran their evidence. The
severity fell each round and no round-3 finding reshaped a round-2 one, so this
stopped for the right reason rather than from fatigue.

## The merge race — how round 3 landed in a second PR

**fm #992 merged at `09:36:10Z`, about 30 seconds before the `do-not-automerge`
label was applied.** The sweep had skipped it once (`substrate-gate:
in_progress/None`), then caught the next pass the moment the flipped card and
green gate lined up. TRAP-007 says the label must go on **before** the push that
makes a PR mergeable; applying it after the card flip lost the race by design,
not by accident.

Consequence, and it is the honest version: **rounds 1–2 are in fm #992; round 3's
four fixes are in a follow-up PR**, because the merged PR cannot carry new work.
Nothing was lost, and nothing shipped unreviewed — but the review that was
supposed to gate the merge arrived after it.

**One claim to correct, because it went into a commit message.** The round-3
review carried `commit_id: fe25f8d`, which was read as GitHub's squash-merge
*preview* on the reasoning that it had a single parent equal to `main`. It was
the **actual squash-merge commit** — the PR had already merged. The inference was
wrong; the observation that a review's `commit_id` need not equal the branch head
still holds, but the reason here is that the review ran after the merge, which is
a different and more useful fact for TRAP-007: **a review whose `commit_id` equals
the SQUASH-MERGE COMMIT is evidence the merge beat the review** — that commit did
not exist before the merge, so a review pointing at it can only have run after.

**Stated that narrowly on purpose** (fm #993 R4). The looser form — "a review at
a SHA belonging to a merged PR" — is false: a review submitted against a branch
head *before* the merge keeps that head's SHA afterwards, which is the ordinary
case and the opposite conclusion. The test is whether the SHA is the merge commit
itself, not whether the PR is now merged.

**A method note that generalised.** The cadence worked as `[D-0019]` describes:
free-key Gemini for intermediate verification (it caught the `abspath`/`realpath`
symlink inconsistency that would have made the root note false-alarm on a
symlinked checkout), Codex for the rounds that decide. Gemini's first pass
overran its token budget mid-reasoning and the useful finding was in the
truncated fragment — worth re-running with a bigger budget rather than reading
the truncation as a clean pass.

**One `[survived]`:** Gemini flagged the `KeyboardInterrupt`/`SystemExit`
re-raise as a fail-open contract violation. It is deliberate — `owner_review.py`
MEASURED 2026-08-08 that swallowing them makes a hook outlive the process that
owns it. Kept, but the docstring's contract bullet now names its own exception
rather than reading as an absolute.

**Not done, and deliberately** — the other two gaps from the same review, both
larger design questions than this session's scope:

1. **A `SubagentStop` review round.** Confirmed a real event in the current
   schema and blocking-capable (exit 2 prevents the subagent stopping). It
   covers the population `TRAP-003`/`TRAP-004` came from — subagent findings go
   straight into `docs/` with no review round at all, while `owner_review.py`
   only sees the main agent's turn end. The open design question is whether the
   fixed-question mechanism transfers: subagent output is a claim-bearing
   artifact, not a reply to the owner.
2. **Promoting `TRAP-006`/`TRAP-007` to Stop-time state checks.** Both are
   conditions about the world at turn end (is HEAD pushed, is the card
   `complete`, is a requested review unanswered) and are currently chased at
   `PreToolUse` by pattern-matching edit text — which only fires if the session
   phrases the write in a matched way. `docs/traps.md`'s own lifecycle
   (`mistake → trap → route → deterministic checker where possible`) puts them
   one stage short of the end.

**And a live thread this session narrowed but did not close.** The hooks README
banner recorded six `owner_review.py` firings on 2026-08-26 logging
`{"route":null,"enriched":false,"error":null}`. That signature is uniquely the
missing-key branch, which is now loud — but the incident itself is **not**
explained: hook processes inherit the parent environment (Claude Code strips only
`OTEL_*`), so "the key was in the session but not the hook" cannot be the cause,
and the original log died with its container. The next investigation is
provisioning, not plumbing. The diagnosis in the banner is tagged `REASONED`,
not `MEASURED`, for exactly that reason.
