# universal-wakeup — self-review / wake-up prompt (all 10 lanes)

> **Status:** `living-ledger`
>
> Gen-1 text, deployed 2026-07-09 to all 10 lanes as the full self-review +
> wake-up pass. Produced the retro corpus synthesized in
> [`../findings/retro-synthesis-2026-07-09.md`](../findings/retro-synthesis-2026-07-09.md).
> Verbatim — never edit history; add dated successors.

## Deployed text (verbatim)

```
DECIDED: full self-review + wake-up pass. Do all of this in THIS session, in your own repo, and land everything as READY PRs (never drafts).

1. SELF-UNBLOCK FIRST. Before asking me for anything: re-read your control inbox(es) and your open PRs. For every item that appears to wait on me, ask: "can I decide or do this myself under decide-and-flag?" If yes — do it now and note the decision with one line of why. Only what is genuinely owner-only (product taste, money, credentials, irreversible or external actions, platform clicks an agent cannot perform) may go on my list in step 4.

2. EXECUTE YOUR QUEUE. Run your standing ritual: execute every order in your control inbox with status `new`, in priority order — including the retro order: answer every question in docs/retro/QUESTIONS.md by ID in the file that order names, honest over flattering, every claim tied to a PR/commit/file. "I don't know" is a valid answer; invented certainty is not.

3. AGENT AUDIT. List every session, agent, and subagent that has worked in this Project so far, including yourself. For each: what it was tasked with; what it actually delivered (verify against the repo); what MODEL it ran on — state your own model, and the model of every agent you spawned; if you cannot determine a model, write "cannot determine" and explain why; and — most important — every point where it stalled, died, went silent, or needed human input, with your best reconstruction of the cause, classified as: (a) our instructions/setup, (b) a platform limit or bug, or (c) the work itself. If a session's fate is unknowable from where you sit, say so explicitly rather than guessing.

4. THE DOCUMENT. Produce ONE comprehensive markdown document at docs/retro/project-review-2026-07-09.md (if your Project shares its repo with another lane, suffix the filename with your lane name — same rule as your status file). Contents: (a) what this Project is and its current TRUE state, verified against the repo, not memory; (b) the agent audit from step 3; (c) your answered retro questions, or a link to that file; (d) an honest efficiency verdict — where the time actually went, what you would redo and in what order; (e) ⚑ OWNER ACTIONS — the short list of things only I can do, each with EXACT instructions (where to click, what to type or paste — assume I can infer nothing) and what it unblocks; (f) CONTINUATION — what you will do next WITHOUT me, and then actually start doing it after this document lands.

5. Land the document and retro answers as READY PRs and see them merged (arm auto-merge if checks are pending). Update your control status file(s) as the deliberate LAST step — orders acked/done, ⚑ needs-owner mirroring your owner-actions list. If any step hits a platform wall, record the exact error text in the document instead of stopping.

Rails unchanged: forward-only git; decide-and-flag, never wait; never edit inbox files; honest uncertainty over invented certainty.
```
