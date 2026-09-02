# Continuation prompt — the owner's step-by-step review sitting over the 2026-09-02 sessions

> **Status:** `reference` · a LIVE prompt, not seat-era history · written 2026-09-02 by the session that landed fm #1010
> and fm #1011, at the owner's ask: *"use the continuation prompt skill so
> the next session can review it and help me go over everything step by
> step."* Paste the block below as the first message of that session. State
> verified at HEAD when written (`main` @ `1f405d9`); the receiving session
> re-verifies it as its first step.

```text
CONTINUE: Walk the owner, one item at a time and at his pace, through everything
the two 2026-09-02 sessions landed on menno420/fleet-manager — fm #1010 (the
night fleet's EAP mail-evidence report) and fm #1011 (the Codex round cap and
the agent model tiers) — confirm or correct each decision with him, and settle
the open items. A review sitting, not a build.

BEFORE YOUR FIRST TOOL CALL — state the task back, inline in this same reply,
in four labelled lines (never one fused paragraph, never a question):
  HE SAID — the ask in your own words, one or two sentences.
  ALREADY SETTLED — what the repo already decided about it, naming the file,
                    or "nothing found yet".
  I INFER — the specs, constraints and scope the ask implies, and the follow-on
            the owner probably wants but did not spell out. Labelled inference.
  LEAST SURE — the one reading you are least sure of; he corrects it in a word.
Then begin. This is the owner's one cheap chance to correct your aim; a first
reply that only announces your first action spends it.

HOW HE WANTS TO BE SPOKEN TO (owner, 2026-09-02, verbatim: "Please reply when
I send a message"): every message he sends is acknowledged first, in the next
thing you write, with what it changes — before any progress note. One item
at a time; plain language; his pace. Do not fan out agents in this sitting.

WHERE THINGS STAND (verified at HEAD on 2026-09-02, ~13:45Z — re-verify first)
- main @ 1f405d9: fm #1011 merged 08:48:55Z; fm #1010 merged 07:59:18Z
  (3ae04b3). Both closed and merged; CI on main green.
- The records-only follow-up PR from the same session (branch
  claude/night-fleet-eap-pr-review-pcssm0, title "Records: the 2026-09-02
  sitting, retained verification data, two capabilities, this prompt") —
  believed merged by the time you read this; confirm it.
- The hook .claude/hooks/codex_round_guard.py is live on main. It loads
  automatically for sessions that boot with fleet-manager as root (boot
  triad case one); a multi-root session gets it only after
  `python3 tools/install_root_hooks.py --apply`, the rescue path.
- Nothing is in flight: no open PR from these sessions once the records PR
  lands, no running workflow.

READ FIRST (a floor, not a boundary — each verified at HEAD when written)
1. docs/findings/2026-09-02-owner-direction.md — his words from the sitting,
   verbatim, and what each led to; § 1–§ 6 are the agenda of your sitting.
2. .sessions/2026-09-02-eap-pr-review-and-codex-round-cap.md — the landing
   session's card: what shipped, the three Codex rounds, the corrections it
   owed, and the close-out addendum.
3. docs/traps.md TRAP-009 and the two 2026-09-02 entries of docs/decisions.md
   (the cap; the model tiers) — with the measurement behind them.
4. .sessions/2026-09-02-night-fleet-eap-audit.md, then
   docs/findings/2026-09-02-eap-mail-evidence-report.md § 5 and § 10 — the
   night session's card and the report's load-bearing sections (the report
   is 900+ lines; § 5 and § 10 first, the rest only if he asks).
On a cold start the boot file's six-read order still applies; this list is
what the sitting needs, not the estate.

DECIDED (do not re-litigate — confirm each with him, amend only on his word)
- Three Codex review rounds per PR, never more: a denying hook, not prose
  (owner; the cap entry in decisions.md). The fourth request is denied;
  FM_ALLOW_CODEX_ROUND=1 only when he asks for another himself. The hook's
  count is per PR PER SESSION (it never reads GitHub) — a PR handed on after
  three rounds starts at zero in the next session, so there the rule binds
  you, not the hook: read the PR's round tally before requesting any.
- Fan-out agents are staffed by task tier — Sonnet 5 reads and maps, Opus 5
  reasons, Fable 5.1 reviews last; `model` is never left to inheritance
  (owner; the model-tier entry in decisions.md; the MODELS line of the
  fleet-preflight contract sheet).
- A mid-turn message is acknowledged first, with what it changes (owner).
- Agents already running may finish; none start after he says so (owner).
- The EAP report is evidence only; only he writes and sends the mail.
- The CONTRACTS sheet's EXTERNAL line is the one place fm #1010's round
  tally lives; nothing restates it.

REJECTED, AND WHY
- A bare cap-then-merge → on fm #1010, rounds 4, 7, 9, 11, 13, 14 and 15 each
  corrected original-draft content; the cap is an exit with disclosure.
- An 18th Codex round on fm #1010 → he stopped the loop; the landing session
  reviewed the head itself against the retained JSON.
- Merging Codex's own sandbox fix for the hook (round 1) → it never pushed a
  branch (no codex/* ref on origin); the fix was reimplemented and tested.
- Restarting the two killed verifier agents → "do not start more"; their
  slices were verified by hand instead.
- A hook that reads GitHub to count rounds across sessions → ten seconds, no
  network promise; the count is session-local and says so in the hook.
- A fan-out for the review pass at all → the session ran one on the
  harness's reading of the word "ultracode" in his message; he had not opted
  in. Not in this sitting.

OPEN (what would settle each)
- The cap's exit semantics (fix · verify without Codex · disclose · flip or
  hand off; never merge with a known error hidden) are the session's reading,
  marked DERIVED in the cap entry — one word from him confirms or changes them; the
  constant CAP = 3 is one line in the hook if he wants another number.
- Whether a Sonnet or Opus session can dispatch Fable agents — unmeasured;
  the Sonnet→Opus half is measured and in docs/CAPABILITIES.md (2026-09-02
  line). One probe settles it: a Sonnet session spawns one Fable agent and
  reads the model field back; record either outcome in the ledger.
- Whether a mid-turn message passes through UserPromptSubmit (so a hook could
  deliver the acknowledge-first rule) — unmeasured; probe when a session has
  a second window open.
- The landing card's 💡: a checker for "one canonical place per fact" inside a
  PR (the churn's structural cause on fm #1010) — shaped, not built; his call.
- The subagent default question he was asked (A/B/C) — closed by his rule
  (the model-tier entry); listed so it is not re-asked.

YOUR FIRST STEP
Confirm the state above at HEAD (`git log --oneline -3 origin/main`; the three
PRs via the GitHub API), then open the sitting with the six DECIDED items as
six one-line questions in plain language, one at a time, waiting for his
answer on each; the only tool calls between answers are reads of the file the
item points at.

DONE WHEN
- Every DECIDED item is confirmed or amended by him, with amendments landed
  in the existing entries (the two 2026-09-02 decisions updated in place,
  never re-minted),
  and every OPEN item carries his answer or a named probe.
- Anything landed passes `python3 bootstrap.py check --strict` with exit 0;
  born-red card first, flipped complete last; one Codex round at
  flip-readiness, never a fourth.

OUT OF SCOPE
- Drafting any part of the EAP mail (owner-reserved). Re-running the night
  fleets. Editing the retained JSON under docs/findings/data/. Any fan-out.

LESSONS FROM THIS SESSION
- Three mid-turn messages went unacknowledged until he asked; the fix is
  placement (acknowledge first), not effort.
- "Finish your current agents" means the ones running when he says it; the
  runtime starts queued agents by itself the moment a slot frees, and the
  stop killed two that had just begun.
- A claim about last night's agents' models was written from inference and
  was false; the retained JSON's `model` fields settled it in one count, and
  Codex round 3 is what caught it.

CLOSE WITH
This repo's session-close skill: born-red card as the first commit, PR opened
ready, `python3 bootstrap.py check --strict` exit 0, the card flipped
complete as the last commit after the review round answers on that head, land
on green. Anything newly verified goes into docs/CAPABILITIES.md as a dated
line with its venue token — capability OR wall, per the ledger's own
discovery rule: a probe that is refused is a wall worth recording with the
observed error verbatim; what is never written is an unverified one.
```
