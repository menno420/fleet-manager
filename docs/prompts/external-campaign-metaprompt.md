# external-campaign-metaprompt — ChatGPT prompt-creation meta-prompt

> **Status:** `living-ledger`
>
> Gen-1 text, deployed 2026-07-09 to the owner's ChatGPT prompt-creation
> project to generate the external-review campaign's session prompts.
> **Reconstructed from the manager's dispatch record** (the deployed text lived
> in the ChatGPT side; this is the faithful structure, not a byte-exact copy).
> Never edit history here; add dated successors.

## Meta-prompt (reconstructed structure)

**STEP 1 — read the pack.** Instruct ChatGPT to first read the external review
pack at:
`https://raw.githubusercontent.com/menno420/superbot/main/docs/eap/external-review-pack-2026-07-09.md`

**STEP 2 — generate self-contained prompts** for three session types:

- **8 AGENT sessions** — one per repo: a repo-level audit of the repo's true
  state versus its own claims (docs, status files, READMEs).
- **CODEX sessions, one per code repo** — code-level review, including a
  verdict on each named technical claim in the pack.
- **4 DEEP RESEARCH thematic sessions:**
  1. multi-agent coordination patterns vs our git-message-bus;
  2. backtesting standards vs trading-strategy;
  3. chat-bot plugin architectures vs the manifest contract;
  4. AI-agent memory/workflow systems vs substrate-kit —
  each ending with: *"what are we missing that the field already knows?"*

**STEP 3 — output all prompts labeled + a dispatch plan.**

**Report contract baked into every generated prompt:** each session produces
ONE markdown report containing —

- a **findings table**: finding · evidence URL · severity · root-cause class
  (a) our instructions/setup / (b) platform limit / (c) the work itself;
- a **per-claim verdict**: verified / refuted / could-not-verify;
- **3 recommendations**;
- and the standing instruction: **prefer could-not-verify over invented
  confirmation.**

## Handling returned reports

Owner pastes reports back → commit to menno420/superbot
`docs/eap/external-reviews/` and cross-check every finding against the repos
(playbook R2: reports are claims; git is evidence). See
[`../handoff-2026-07-09.md`](../handoff-2026-07-09.md) — in-flight at handoff.
