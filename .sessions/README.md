# Session logs

Per-session logs live here as `<date>-<slug>.md`, newest first. Create the log as the session's FIRST commit with a born-red status (`> **Status:** `in-progress``) so in-flight work is visible to parallel sessions, then flip it to `complete` as the deliberate LAST step once the close-out is written — a half-done session never reads as finished. Before it counts as complete, a log must carry these markers: Status badge, Session idea, Previous-session review, Model line.

If the card is missing at session end, the kit **auto-drafts** one from evidence (files touched, git HEAD movement, the verify command); an in-progress card missing its close-out gets the drafted section appended. A draft is a starting point, not a close-out: verify the evidence, resolve every `[[fill:]]` slot, then flip the Status badge — unresolved slots (and the `drafted` status) keep the card counting incomplete.

**Guard recipes:** when a card records friction-to-guard material for a *later* session (a deferred fix, a flagged footgun), carry a one-line **guard recipe** naming the code anchors — function + file + the test target — not just the symptom. A symptom-only entry costs the next session a re-derivation grep pass; a recipe lets it land the guard in minutes.

<!-- substrate-kit: model-attribution doctrine (family-level names — ORDER 012) -->
The `📊 Model:` model segment is the **family-level model name your own harness/environment reports this session** (e.g. `fable-5`, `opus-4.8`, `sonnet-5`) — the committed card's self-report is the attribution ground truth. Never copy it from an external surface (schedule/Routines screens are evidenced to misattribute), and never record a full dated model ID — family-level names only.

<!-- fleet-manager local amendment, 2026-08-26 (fm #947) — NOT kit text.
     A kit upgrade's install may overwrite this file; re-apply this section
     after one (docs/SKILLS-local.md § Why the local half exists). -->

## 📍 Venue — which machine ran this session (local amendment, 2026-08-26)

Directly under the `📊 Model:` line, one line:

```
- **📍 Venue:** local-desktop
```

The closed set: `local-desktop` (the owner's laptop, Claude Desktop's Code tab)
· `local-cli` (his laptop, `claude` in a terminal) · `cloud-container` (Claude
Code on the web / a remote container) · `codex-cloud` · `chatgpt-work` ·
`other` (say what, in the body).

**Why it is a separate line and not a fourth Model segment:** the `📊 Model:`
line has a kit-validated three-segment taxonomy, and a local convention does not
belong inside a gated grammar.

**Why it exists at all:** the Model line answers *who*, and until 2026-08-26
nothing answered *where* — so a session reading another session's card could not
tell laptop work from container work. `MEASURED` at `39c9d6e`: **0 of 418**
dated cards here carried it — 418 and not 419, because this directory's own
`README.md` is not a session card. The owner asked for the fix on 2026-08-26; the measurement is
[`docs/findings/2026-08-26-cross-session-visibility.md`](../docs/findings/2026-08-26-cross-session-visibility.md)
and the estate-wide index it feeds is [`docs/activity/`](../docs/activity/README.md).

**Omit it rather than guess.** The generator reports an absent line as
`unstated` and prints the coverage count, so an honest null is visible and a
wrong venue is not.
