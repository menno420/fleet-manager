# 2026-08-31 — the SessionStart orientation hook, and the review hook's silent skip

> **Status:** `in-progress` — born red. Flips to `complete` only once the hook
> is registered on both surfaces, pipe-tested on every `source` value, the
> owner-review no-key branch is countable, and `bootstrap.py check --strict`
> exits 0.

- **📊 Model:** withheld · high · feature
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

[[fill: written at close]]
