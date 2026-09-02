# 2026-09-02 — fm #1010 reviewed and landed on its flip head; the Codex round cap (TRAP-009 · D-0039)

> **Status:** `in-progress` — the morning-after session: review the night
> fleet's PR #1010 on its exact head, land it, and turn the owner's "three
> rounds, never more" into a denying hook. Flips to `complete` as the
> deliberate last commit of this PR.

- **📊 Model:** fable-5 · max · feature build
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_018UX5M46NG1DJ9WdrfW3t8n](https://claude.ai/code/session_018UX5M46NG1DJ9WdrfW3t8n) · "Night-fleet EAP PR review and merge readiness"

## Mission

Owner, live, 2026-09-02, the morning after the night fleet: *review what the
sonnet 5 ultracode has documented tonight* on fm #1010; *for some reason it
thought it was necessary to have 17 rounds of codex reviews*; *I think there
should be a maximum of 3 review rounds at most, never more than that. What do
you think? Do you think that all 17 review rounds were necessary?* The night
session's continuation prompt was used as guidance, with one of its rules
kept absolutely: **this session requested no Codex round.**

## What this session did

1. **fm #1010 — reviewed on its exact head `8470c9d`, not re-reviewed by
   Codex.** Round 17 (requested by the night session on that head) came back
   with one P2: the session card's "method finding" phrase, a copy that had
   not followed § 3's round-15 correction. No report defect. This session ran
   its own verification pass instead of an eighteenth round — a 7-agent
   workflow (two classifiers over all 88 inline Codex threads and their fix
   commits; four adversarial verifiers, one report slice each, against the
   retained raw JSON; one completeness critic on the flip decision) — and
   read § 2, § 3, § 5 and § 10 directly. Outcome and the edits made before
   the flip: see that PR's own card and its CONTRACTS sheet's EXTERNAL line,
   the one place its round tally lives.
2. **The cap — a mechanism, not a fourth statement of the rule.**
   `.claude/hooks/codex_round_guard.py` counts each `@codex review` per PR per
   session out loud and denies the fourth (`FM_ALLOW_CODEX_ROUND=1` when the
   owner asks himself); `tools/test_codex_round_guard.py` walks the fm #1010
   sequence; wired in `.claude/settings.json` and the rescue table in
   `tools/install_root_hooks.py`; recorded as `docs/traps.md` TRAP-009 (the
   measurement) and `docs/decisions.md` [D-0039] (the rule and its exit);
   one sentence in the boot file's `@codex` bullet points at it. **Codex
   round 1 on this PR (`173dcd2`) found one real defect:** the retry dedup
   keyed on the comment body alone, so the literal `@codex review` posted on
   each successive fix commit — fm #1010's exact shape — would have counted
   as one round and bypassed the cap. Fixed: the key is now head + body,
   an unreadable head disables the dedup rather than the count, and the
   suite walks both (37 cases). Codex also fixed it in its own sandbox on a
   branch it never pushed (verified: no `codex/*` ref on origin, no second
   open PR); the fix here is this session's own. **Round 2 (`358c2c8`), three
   findings, all real:** the Bash leg missed the GitHub CLI (`gh pr comment N
   --body '@codex review'`, `gh api …/comments -f body=…` — no endpoint or no
   verb in the text) — now matched as request shapes of their own; the count
   was keyed on the PR number alone, so two repositories' `#42` would share
   one allowance — keys are now `owner/repo#N` from the MCP fields, the
   endpoint path or `-R`, with `?` for an unknown half; and this card's own
   Verify line still said 30 cases after the suite grew — the number is
   gone, the executable prints it. Round 3 is the last the cap allows.

**Why two PRs this session (D-0024 exception, stated):** fm #1010 is another
session's PR, finished on its own branch because its own card's born-red
discipline requires the flip to be that PR's last commit; this PR carries
this session's own work. One of the two is not this session's PR.

## Verify

`python3 bootstrap.py check --strict` — run in this branch's worktree before
the flip, only the born-red hold red; `python3 tools/test_codex_round_guard.py`
— 0 failed, and the executable prints its own case count (a number written
here went stale within one round — Codex, round 2 — so it is not restated).

⚑ decide-and-flag: **what the cap means at round three** — fix · verify
without Codex · disclose the residue · flip or hand off, never a fourth round
and never a merge with a known error hidden. `DERIVED` from his words, put to
him in the reply; the constant is one line (`CAP = 3`) if he wants another
number.

💡 Session idea: the churn's structural cause on fm #1010 was the same fact
restated in six places inside one PR (front matter, § 3, § 5, § 10, the card,
the contract sheet), so every correction bred sync findings. A checker that
flags a number or a named mechanism claim appearing in more than one of a
PR's own files — "one canonical place per fact" as a red, not a sentence —
would remove the drift rounds at the source. Not built.

⟲ Previous-session review: fm #1010 (the night session, sonnet-5) — the
fleets ran as contracted, the evidence is real, and the per-round accounting
is honest to a fault. What failed was the loop's exit condition, not the
work: it treated "one clean round" as the exit, and against a 931-line prose
report that exit does not exist. It also wrote the round tally into six
places and then had to fix five of them every round until round 7 taught it
otherwise for one of the numbers.

**Owner feedback, live, mid-session (two observations, recorded for the
next session):** (1) *"you tend to ignore messages mid turn, meaning you do
not show in chat that the message has arrived and that you understand what
that means for your task"* — it happened twice here; the first line after a
mid-turn message must acknowledge it and say what it changes. (2) *"all your
agents are also Fable 5.1, why didn't you choose to use Opus or Sonnet for
that?"* — the workflow's `agent()` inherits the session model unless `model`
is set; it was left unset. Mechanical reads (classifying review threads)
are Sonnet work and verification is Opus work, both cheaper against his Max
allowance; a default was put to him as a one-letter choice. **He answered
with the rule itself** — reading/mapping on Sonnet 5, reasoning on Opus 5,
final review on Fable 5.1 — recorded as [D-0040] and delivered as the
`MODELS` line of the `fleet-preflight` contract sheet (§ 8 of that skill),
the sheet every fan-out fills before its first agent spawns. His follow-up
question — why none of the agents chose a tier themselves — has the same
answer as the seventeen rounds: the harness default said "leave it", the
cost was out of view, and a question a default has already answered does
not get asked. That is the case for the sheet line.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached this
session).
