# 2026-08-29 — the `📊 Model:` slot has no token for "my session may not name it", so five sessions invented five

> **Status:** `in-progress`

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against putting a
  model identifier in a pushed artifact; the effort and PL-004 task-class
  halves are exact. Which is the subject of this card — see § Finding 2 on why
  the note is *not* a wall and *not* a new default.
- **📍 Venue:** cloud-container

💡 Session idea: a rule that fires on some sessions and not others produces no
error and no red gate — it produces **synonyms**. Nine cards decline to name a
model in five different spellings, and the checker fails open on all five, so
the attribution ledger fragments silently instead of failing loudly.

## Mission

The owner asked a narrow question — *is the no-model-identifier rule new in the
harness?* — after noticing that recent cards say `withheld` where older ones name a
family-level model. He then opened a fresh test session
(`session_01HHeAKmJhrYTudDyecmhveK`) which also could not record its model.

Answering it properly overturned my own previous answer and exposed a grammar
gap worth fixing.

## Finding 1 — the rule is not new, and never was uniform · `MEASURED`

Parsed every `.md` in `.sessions/` **from the git tree** (`git ls-tree -r
--name-only HEAD .sessions/` → 441 files, minus this README), taking each
card's first line-anchored `📊 Model:` occurrence — the kit's
`MODEL_LINE_NEEDLE` at `bootstrap.py:1469`, bold or not. **430 cards carry the
line; 417 name a model and 13 decline, in five spellings, across seven weeks:**

| spelling | cards | dates |
|---|---|---|
| `unrecorded-by-policy` | 4 | 2026-07-09 ×3, 2026-07-10 |
| `withheld per session policy (Fable-5 review wave, …)` | 1 | 2026-07-10 |
| `withheld per session policy (manager worker, …)` | 1 | 2026-07-10 |
| `identity withheld by session policy` | 1 | 2026-08-11 |
| `withheld` | 6 | 2026-08-28, 2026-08-29 ×5 |

(Plus a 14th on the open fm #973 branch, absent from this tree.)

**Matcher note — this table is the third count, not the first.** The first used
`- **📊 Model:**` and saw 260 cards; the kit's own `MODEL_LINE_NEEDLE` is the
bare `📊 Model:`, and 170 cards carry it unbolded. The second dropped the bold
requirement but took the *last* needle on each card, so prose mentions of the
field displaced header lines on the cards discussing it — including this one.
The table above is line-anchored and takes the first header occurrence.

The 2026-07-09 cards annotate themselves *"(fleet program policy: no model
identifiers in committed files)"*, and
[`docs/findings/retro-synthesis-2026-07-09.md`](../docs/findings/retro-synthesis-2026-07-09.md)
§7 attributes it one word more precisely for the `codetool-lab-fable5` lane —
*"**Withheld from repo artifacts per harness policy** … The only lane that
deliberately does not name its model in-doc."*

So the restriction was live **on 2026-07-09**, was already attributed to the
harness, and was already noted as affecting exactly one lane out of five. The
other 417 cards name a model — including `cloud-container` cards dated
2026-08-28, one day before mine, same venue.

**The variable is not the calendar. It is which sessions carry the
instruction.** That is what makes it invisible: there is no transition to
detect, so a session comparing its own card to yesterday's concludes something
changed when nothing did.

### This corrects an earlier claim of mine in the same chat

I reported *"255 of 260 cards name a real model; the only 5 saying `withheld`
are mine from today."* Wrong: seven of the thirteen withholding cards are
neither mine nor from today, and I found only the literal token `withheld`
because I grepped for that string and never for the condition.

Then I reported the correction with a 259-card denominator — and **that was
wrong too**, for the reason in the matcher note above: 259 was the bolded
subset of 430. Same defect one layer up. Both reduce to one sentence: **my
matcher was narrower than the population I claimed to have counted**, first on
the value, then on the format.

This is **TRAP-002** (mis-scoped grep produces a confident false null) from
[`docs/findings/2026-08-29-estate-agent-error-audit.md`](../docs/findings/2026-08-29-estate-agent-error-audit.md),
committed by the session that wrote it, four hours later, against its own
corpus. Logged here rather than quietly fixed, because a trap register whose
author re-commits its entries is evidence about the register's delivery, not
about the author.

## Finding 2 — the restriction is narrower than "no model names in the repo" · `MEASURED`

The same instruction set that forbids a model identifier in a pushed artifact
**mandates a commit trailer that contains one**, verbatim, and says to end
every commit message with it. **The instruction is the evidence; the count is
not.** Trailers reachable from branch tips, in five forms — and see the scope
warning below the table before quoting any of these numbers:

| trailer | commits |
|---|---|
| `Co-Authored-By: Claude Fable 5` | 473 |
| `Co-Authored-By: Claude Opus 5` | 138 |
| `Co-Authored-By: Claude Opus 4.8 (1M context)` | 19 |
| `Co-Authored-By: Claude` | 14 |
| `Co-Authored-By: Claude Opus 4.8` | 8 |

**This measurement is not reproducible, and Codex demonstrated it.** `git log
--all --format="%B" | grep -c "Co-Authored-By: Claude"` returns whatever refs
the local checkout happens to hold — 656 across 123 refs in the container that
wrote this card, 343 at Codex's checkout of the same commit, and the breakdown
above is likewise container-local. The one stable number is `origin/main`:
**1 trailer across 62 commits**, because this repo squash-merges and that
collapses every PR's per-commit trailers into a single squashed message.

So the finding stands on the instruction text, which any session can read in
its own prompt, and **not** on the tally. A count whose value depends on which
branches your clone fetched is not evidence — which is the same defect this
card's § *Matcher note* records one layer down, and the same one the audit
catalogues as a claim wider than the sample that produced it.

So the rule cannot mean *no model name anywhere in a commit*. The coherent
reading is **don't editorialize model identity into content** — titles, bodies,
prose, code comments — while the mandated attribution trailer is the sanctioned
channel. The `📊 Model:` card line is the genuinely ambiguous case: it is
document content, not a trailer, which is why sessions split on it rather than
converging.

## Finding 3 — nothing surfaces the split, by design · `MEASURED`

`bootstrap.py` grades segment-1 of the Model line against
`EXACT_MODEL_ID_RE = ^(?:us\.)?(?:anthropic\.)?claude-|-\d{8}$` and **fails open
on everything else** (`_exact_model_id_findings_for_card`, and the advisory
`check_model_line`). Only a dated/prefixed exact ID reds. So
`unrecorded-by-policy`, `identity withheld by session policy` and `withheld` all
pass — correctly, since reddening an honest null would invite an invented one,
exactly as the `unrecorded` effort carve-out reasons.

The gap is not the fail-open. **It is that segment-1 has no sanctioned token
where segment-2 has `unrecorded`.** Given a condition, no vocabulary and no
feedback, five sessions produced five strings.

## The change

One local amendment to [`.sessions/README.md`](README.md), in the same marked
style as the 2026-08-26 Venue amendment (the kit block above it is kit text and
a kit upgrade's install may overwrite the file):

- **The default is unchanged and stated first:** name the family-level model.
  250 of 259 cards do, and that ledger is the point of the field.
- **One sanctioned token** — `withheld` — for a session that actually carries
  the restriction, plus the one-line `⚑ Model-slot note` naming which half is
  exact. Not a new phrasing per session.
- **Re-test, do not inherit.** The restriction is not uniform across sessions,
  so a session must check its own instructions rather than copy a neighbouring
  card's `withheld`. This clause is the reason the amendment is not a wall:
  per the owner (2026-08-29), the walls rule exists because *documented walls
  suppress future attempts and walls decay* — *"I'd rather have agents having to
  re-discover they can't do something, than that they do not try it at all
  while they might be able to."* A `withheld` copied from another card is
  precisely the suppressed attempt that rule guards against.

## Guard recipe (deferred, for a later session)

A checker could collapse the synonym class without reddening honest nulls:
warn (advisory lane, never exit-affecting) when segment-1 is neither
family-level-model-shaped nor the exact literal `withheld`. Anchors:
`_exact_model_id_findings_for_card` and `_last_model_payload` in
`bootstrap.py`; the fleet-wide half is `engine.checks.check_model_line`; the
taxonomy constants live beside `EXACT_MODEL_ID_RE` (`bootstrap.py:1519`) and
`MODEL_EFFORT_UNRECORDED` is the precedent to mirror. Not landed here because
the kit owns those surfaces and this repo owns the amendment; splitting them
keeps the PR small.

## Previous-session review

Continues the 2026-08-29 audit thread — the catalogue-export card, which lives
on the open [fm #973](https://github.com/menno420/fleet-manager/pull/973) branch
and is deliberately **not** linked relatively, because it is not in this tree —
and
[`2026-08-29-audit-od26-reconcile.md`](2026-08-29-audit-od26-reconcile.md)
(merged). Same session, a question the owner raised after those landed.

## Codex round 1 on fm #976 — 4 P2 findings, all `[conceded]`

Reviewed `60eb15b` (before the census correction), delivered as a review with
**four inline comments** — a different channel from fm #973's issue comment, in
the same hour. Any check that reads one channel and concludes "no review" is
wrong twice over.

| # | finding | disposition | fix |
|---|---|---|---|
| 1 | The card-corpus counts conflate two selectors and are not reproducible as written | `[partial]` | The **values** were already corrected before this review landed (430/13, not 259/9). The **reproducibility** complaint is conceded in full: neither the amendment nor this card named its selector or its tree, so 441 files / 430 cards / 260 bolded all looked like the same measurement. Both now state the selector, the tree-level command and what the other two selectors return. |
| 2 | The trailer count is unreproducible — 343 at the reviewed checkout, not 654 | `[conceded]` | Correct and decisive: `git log --all` counts whatever refs the clone holds (656 across 123 refs here). The count is withdrawn as evidence; the finding now rests on the instruction text, which any session reads in its own prompt. The one stable figure — `origin/main` carries **1** trailer across 62 commits, because the repo squash-merges — is stated as such. |
| 3 | The re-apply-after-upgrade warning misstates the installer | `[conceded]` | Verified from source: `_adopt_plant` (`bootstrap.py:19563`) reports `kept:` and returns without writing when the file exists; `_merge_model_doctrine` (`:19652`) is append-only, idempotent, and preserves existing content byte-for-byte. Following the warning would have **duplicated** the amendment on every upgrade. **The warning was inherited verbatim from the 2026-08-26 Venue amendment, so the repo has carried it since then** — both instances corrected here. |
| 4 | The previous-session link is dead in this tree | `[conceded]` | The catalogue-export card is on fm #973's branch, not this one. Replaced with the PR URL and a line saying why it is not a relative link. |

One `[partial]`, three `[conceded]`, zero `[survived]`.

**Finding 3 is the one worth carrying forward.** It is not a slip in this diff —
it is a false instruction that has been in `.sessions/README.md` since
2026-08-26, which I propagated by copying the surrounding convention instead of
checking it. Copying a neighbouring block's provenance comment is exactly the
inheritance the amendment's own "never inherit `withheld`" clause warns against,
committed in the same file, in the same PR, by the session writing the clause.

## Verify

```
python3 bootstrap.py check --strict
```
