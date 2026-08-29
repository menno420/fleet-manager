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

<!-- fleet-manager local amendment, 2026-08-29 (fm #976) — NOT kit text.
     A kit upgrade's install may overwrite this file; re-apply this section
     after one (docs/SKILLS-local.md § Why the local half exists). -->

## `withheld` — the one token for a session that may not name its model (local amendment, 2026-08-29)

**The default is unchanged: name the family-level model.** 417 of 430 dated
cards do, and that ledger is the whole point of the field. Read the kit
doctrine above first; this amendment only covers the exception.

**Some sessions carry a harness instruction against putting a model identifier
into an artifact pushed to a repository.** When yours does, the card cannot
carry a model name, and the segment has no taught value for that — so record
the single literal token and one line saying which halves are still exact:

```
- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
```

`withheld` **exactly** — not a phrasing of your own. Before this amendment,
thirteen cards declined in five different spellings (`unrecorded-by-policy` ×4
from 2026-07-09/10 · two distinct `withheld per session policy (…)` variants
from 2026-07-10 · `identity withheld by session policy` from 2026-08-11 ·
`withheld` ×6 from 2026-08-28/29), and the checker fails open on all five
(`_exact_model_id_findings_for_card` reds only an *exact model ID*, correctly —
reddening an honest null invites an invented one, the same reasoning as the
`unrecorded` effort carve-out). So nothing surfaced the split; it just
fragmented the ledger. One token makes the exception countable.

**Check your own instructions — never inherit `withheld` from a neighbouring
card.** The restriction is *not* uniform across sessions and never has been: it
was live and attributed to harness policy on 2026-07-09
([`docs/findings/retro-synthesis-2026-07-09.md`](../docs/findings/retro-synthesis-2026-07-09.md)
§7, for one lane of five), while cards from the same venue one day before the
2026-08-29 batch name a family-level model freely. Copying another card's `withheld` is the
suppressed attempt the never-write-a-wall rule exists to prevent — walls decay,
and re-discovering one costs less than never trying.

**It is narrower than "no model names in the repo."** The same instruction set
mandates a `Co-Authored-By` commit trailer that carries a model name; **654**
across this repo's branch tips carry one (`git log --all`; `origin/main`'s own
history shows 1, because squash merges collapse per-commit trailers). The rule bites on *content you author* —
prose, titles, code comments — not on the mandated attribution channel. The
card's `📊 Model:` line is the ambiguous case, which is why sessions split on
it; `withheld` is how this repo resolves it.

Measurement and the full reasoning:
[`.sessions/2026-08-29-model-slot-grammar.md`](2026-08-29-model-slot-grammar.md).
