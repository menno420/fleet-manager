# Session logs

Per-session logs live here as `<date>-<slug>.md`, newest first. Create the log as the session's FIRST commit with a born-red status (`> **Status:** `in-progress``) so in-flight work is visible to parallel sessions, then flip it to `complete` as the deliberate LAST step once the close-out is written — a half-done session never reads as finished. Before it counts as complete, a log must carry these markers: Status badge, Session idea, Previous-session review, Model line.

If the card is missing at session end, the kit **auto-drafts** one from evidence (files touched, git HEAD movement, the verify command); an in-progress card missing its close-out gets the drafted section appended. A draft is a starting point, not a close-out: verify the evidence, resolve every `[[fill:]]` slot, then flip the Status badge — unresolved slots (and the `drafted` status) keep the card counting incomplete.

**Guard recipes:** when a card records friction-to-guard material for a *later* session (a deferred fix, a flagged footgun), carry a one-line **guard recipe** naming the code anchors — function + file + the test target — not just the symptom. A symptom-only entry costs the next session a re-derivation grep pass; a recipe lets it land the guard in minutes.

<!-- substrate-kit: model-attribution doctrine (family-level names — ORDER 012) -->
The `📊 Model:` model segment is the **family-level model name your own harness/environment reports this session** (e.g. `fable-5`, `opus-4.8`, `sonnet-5`) — the committed card's self-report is the attribution ground truth. Never copy it from an external surface (schedule/Routines screens are evidenced to misattribute), and never record a full dated model ID — family-level names only.

<!-- fleet-manager local amendment, 2026-08-26 (fm #947) — NOT kit text.
     A kit upgrade does NOT overwrite this file and this section does NOT need
     re-applying: `_adopt_plant` reports `kept:` and returns without writing
     when the file exists, and `_merge_model_doctrine` is append-only,
     idempotent, and preserves existing content byte-for-byte (bootstrap.py
     :19563, :19652). The earlier wording here said the opposite; following it
     would have duplicated the amendment on every upgrade. Corrected fm #976
     after Codex checked the installer. Context: docs/SKILLS-local.md § Why the
     local half exists. -->

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
     Kit-owned text is the doctrine block above the Venue section; everything
     below it is local. A kit upgrade preserves all of it — see the note on the
     Venue amendment for the two functions and why. -->

## `withheld` — the one token for a session that may not name its model (local amendment, 2026-08-29)

**The default is unchanged: name the family-level model.** 417 of the 430 cards
that carry a `📊 Model:` line do, and that ledger is the whole point of the
field.

> Reproduce: enumerate `.sessions/*.md` from the tree (`git ls-tree -r
> --name-only <sha> .sessions/` — 441 files at fm #976, minus this README), take
> each card's **first line-anchored** `📊 Model:` occurrence — the kit's
> `MODEL_LINE_NEEDLE`, bold or not — and read segment 1. 430 cards carry one.
> Counting *files* instead gives 441, and requiring the bolded
> `- **📊 Model:**` form gives 260; both are different questions and neither is
> the number above. Read the kit
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

`withheld` **exactly** — not a phrasing of your own. Under the same selector,
thirteen of those 430 cards decline in five distinct spellings:
`unrecorded-by-policy` ×4 (2026-07-09/10) · two different
`withheld per session policy (…)` variants (2026-07-10) ·
`identity withheld by session policy` (2026-08-11) · `withheld` ×6
(2026-08-28/29). The checker fails open on all five
(`_exact_model_id_findings_for_card` reds only an *exact model ID*, correctly —
reddening an honest null invites an invented one, the same reasoning as the
`unrecorded` effort carve-out). So nothing surfaced the split; it just
fragmented the ledger. One token makes the exception countable.

**Check your own instructions — never inherit `withheld` from a neighbouring
card.** The restriction is *not* uniform across sessions and never has been: it
was live and attributed to harness policy on 2026-07-09
([`docs/findings/retro-synthesis-2026-07-09.md`](../docs/findings/retro-synthesis-2026-07-09.md)
§7 — **one lane of ten**, not of five: that doc is titled *"all 10 lanes"* and
its model table lists nine, of which `codetool-lab-fable5` is called *"the only
lane that deliberately does not name its model in-doc"*; a second row,
`codetool-lab-opus4.8`, records a *successor's* model withheld under the same
policy. The "of five" was wrong when first written here and is corrected in
place rather than left to propagate), while cards from the same venue one day before the
2026-08-29 batch name a family-level model freely. Copying another card's `withheld` is the
suppressed attempt the never-write-a-wall rule exists to prevent — walls decay,
and re-discovering one costs less than never trying.

**It is narrower than "no model names in the repo."** The same instruction set
that forbids the identifier also hands the session a `Co-Authored-By` trailer
containing one and says to end every commit message with it. **That instruction
is the basis for the distinction — read your own; do not try to count it.**

> **Do not quote a trailer count here, in any scope.** Two attempts were wrong
> for two different reasons. `git log --all` counts whatever refs the clone
> holds (656 across 123 refs in the container that wrote this; 343 at a
> reviewer's checkout of the same commit). `origin/main` looked stable and was
> not: **this container's clone is shallow**, so `rev-list --count` returned 62
> where full history has **993**, and the 1-trailer result it produced was a
> truncation artifact — which then got a squash-merge explanation invented to
> fit it. The real count from the same base is 341. The distinction this
> paragraph draws needs no number; the instruction is the evidence.

So the rule bites on *content you author* — prose, titles, code comments — not
on the mandated attribution channel. The card's `📊 Model:` line is the
ambiguous case, which is why sessions split on it; `withheld` is how this repo
resolves it.

Measurement and the full reasoning:
[`.sessions/2026-08-29-model-slot-grammar.md`](2026-08-29-model-slot-grammar.md).

<!-- fleet-manager local amendment, 2026-08-29 (session-identity slot, [D-0023]) — NOT
     kit text. Kit upgrades preserve this file — see the Venue amendment's note. -->

## 🔗 Session — which conversation wrote this card (local amendment, 2026-08-29; REQUIRED)

Directly under the `📍 Venue:` line, one line, **required on every card added
from 2026-08-29 on** (owner directive, live — required with an honest null,
*"a small fix that benefits us right away"*; decision ledger [D-0023]):

```
- **🔗 Session:** [session_01ABC…](https://claude.ai/code/session_01ABC…) · "the session's title"
```

**Read your own identity — never copy a neighbouring card's.** In a cloud
container, `get_session` (claude-code-remote MCP, called with no argument)
returns this session's `id` and `title`; the id doubles as the URL
`https://claude.ai/code/<id>`. Quote the title as a search hint for the
owner's session list — titles can be renamed, so the **id is the key**.

**The honest null is the single literal token `unavailable`**, plus one line
saying why (a venue with no session-reading tool, say). Same reasoning as
`withheld` above: reddening an honest null invites an invented one, so the
checker accepts exactly the token — but silence is not a null. A card with
neither an id nor the token reds the added-card preflight
(`scripts/preflight.py`, session-line check; local and CI run the same
script).

**Why:** the Model line answers *who*, Venue answers *where*, and nothing
answered *which conversation* — so "ask the session that did this" meant the
owner scrolling chat history from memory. The harness's `Claude-Session`
commit trailer already carries exactly this and the repo's squash-merge
discards the commit body (measured — fm #977's card, § 3), so the card is
the artifact that survives. **No backfill**: existing cards say what their
sessions knew (record tier).
