# 2026-08-06 · Verify the foundation — classify the kit's checkers, fix two boot paths

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · foundation-verification

💡 Session idea: **a document that only exists in a handoff prompt is not in
the repo.** `docs/findings/2026-08-05-foundation-continuation.md` calls itself
the doc that "supersedes everything else about what to do next", and today it
is referenced by nothing — not `.claude/CLAUDE.md`, not `current-state.md`, not
the program plan, not `PROJECT-CLOSEOUT.md`, not `NEXT-TASKS.md`. It is
reachable only by being pasted a prompt that names it. That is precisely the
failure that cost 2026-08-05 a day, one document later, and the boot path was
edited that same day without catching it.

## previous-session review

The 2026-08-05 continuation left five next actions and a first step: land
superbot-next #602. **#602 was already merged** at 2026-08-05T23:05:49Z —
after the handoff was written — so the estate had zero outstanding items on
arrival, not one. Verified at HEAD: the two `docs/current-state.md:101/118`
false-wall lines are fixed on `main`, and superbot-next has 0 open PRs.

The handoff also recorded that "substrate-kit and fleet-manager have ZERO
required status checks (`contexts: []`)". Re-read from the rulesets API today:
**true for fleet-manager, stale for substrate-kit** — the kit now requires
`kit-quality` (the P10 swap its own `WORKFLOW_JOB_CENSUS` anticipated). That
correction matters, because it is the difference between auto-merge landing an
unfinished PR and the born-red gate holding it.

## What this lands

- `docs/findings/2026-08-06-checker-classification.md` — the measurement and
  the classification, with what deliberately was not done and why.
- `.claude/CLAUDE.md` — the foundation-continuation doc added to the read
  path, so it stops depending on a prompt to be found.
- The program's §7 ledger + progress record.

Companion, in substrate-kit: PR #577 — the `ADVISORY_CENSUS`, its parity
meta-test, census-routed advisory emission, `check --advisories`,
`check --gate-preview`, and a boot read path for the kit itself [D-0011].

## Verification

Filled at close. Born red: this card declares `in-progress`.
