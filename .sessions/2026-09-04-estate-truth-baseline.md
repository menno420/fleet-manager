# 2026-09-04 — the successor-ready estate truth baseline: a change-only re-audit and the `estate` seed manifest

> **Status:** `complete` — **verdict `PARTIAL`**, deliberately, not
> `READY_FOR_THIN_SEED`. Codex ran to the three-round cap and every round was
> non-empty (**9 · 6 · 5 findings, 20 in all — every one conceded and fixed**);
> in two of the three, the new findings were fresh evidence that the previous
> round's fixes had not held. Three independent internal critics before that
> returned PARTIAL/BLOCKED/BLOCKED with eleven P1s, all correct. **Reviewed SHA
> `5fff76d`; after it, the round-3 fixes and this flip.** Landed on green.
> Real exit code of `python3 bootstrap.py check --strict` before the flip: **1**,
> sole finding this card's own born-red hold. **What was:** the
> owner's fresh-start sequence step 2 (*"establish a baseline of trustworthy
> information … but only if the information has changed so far"*) is executed
> as an ultracode run: an authoritative 28-repository census reconciled
> against the live account, a baseline-of-baselines that says for each repo
> which prior evidence is still reusable and why, a re-audit of only the
> changed/weak/new slice, a carry · distill · archive pass over
> fleet-manager's own candidate live truth, and a deterministic seed manifest
> that a later `estate` creation session can work from. Ends with a
> `READY_FOR_THIN_SEED` / `PARTIAL` / `BLOCKED` verdict and an exact handoff.
> **Hard boundary:** substrate-kit is a concurrent session's work (kit #590,
> K1–K5, open at launch) — this session records the dependency and does not
> touch it.

- **📊 Model:** withheld · xhigh · research
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01UDjg5xQNdu1pwTBaagELz4](https://claude.ai/code/session_01UDjg5xQNdu1pwTBaagELz4) · "Estate truth baseline for successor"

## What shipped

- **[The baseline finding](../docs/findings/2026-09-04-estate-truth-baseline.md)** — corpus, method,
  census, delta, re-audit, contradictions, manifest, kit dependency, cold test, verdict, handoff,
  and what was not established.
- **[The seed manifest](../docs/planning/2026-09-04-estate-seed-manifest.csv)** — 183 rows, 21
  columns, GENERATED. The artifact the build order names as a prerequisite of the seed.
- **`tools/estate_baseline/`** — `delta.py` (the reproducible changed/unchanged test), `seed_rule.py`
  (the survival rule + its field audit + 12 fixtures), `build_manifest.py`, and two fixture suites.
- **Evidence** — `docs/findings/data/2026-09-04-estate-truth-baseline/`: the contract sheet, anchors,
  delta, classification, three raw journals, the extracted readings/refutations/dispositions, the
  reuse and archived-provenance lanes, the pilot log, the session's own spot-checks, and the
  pre-registered cold-session rubric.
- **Four inline fixes to fleet-manager's own live truth**, each of which blocked the baseline:
  `current-state.md`'s three states for one open question · `current-state.md` never saying this
  repository is being replaced · `ESTATE.md`'s stale deletion clearance · the findings index.
- **Capability delta** — two entries appended to `docs/CAPABILITIES.md`: measuring fan-out
  concurrency by demand test (peak 2 here against a documented 16), and a `Workflow` schema refused
  for size, with the flattening route around it. Both `CAN`, neither a wall.

Layer-2 handoff: null (this session audited the hub itself and read thirteen satellites read-only;
no repository's own thread state changed).

## ⟲ Previous-session review

`.sessions/2026-09-03-final-eap-mail-rewrite-after-reviews.md` (fm #1019) left the estate in the
state this session had to establish from scratch: it did its own job well — the mail rewritten from
the owner's edits and an independent review — and, like every session before it, it had no way to
answer *"has anything changed since the evidence that measured it?"* because the 2026-08 audit wave
recorded almost no SHAs. That is not a criticism of any one card; it is the gap this session's
`delta.py` closes, and the reason the next one is cheaper.

What it did right and this session copied: the two-round Codex discipline with the reviewed SHA
named in the card, and correcting the owner's own words only for spelling.

## 💡 Session idea

**A `stamp-at-one-home` check at write time, not at gate time.** This session added 29 second
citing homes across eleven decisions before `bootstrap.py check --strict` caught them in one
batch — and the fix was mechanical in every case, because the estate already has an idiom for a
non-home reference (*"decision 25 in `docs/decisions.md`"*). A `PostToolUse` route on a write
containing `[D-0` that is not the decision's home would deliver the idiom at the moment the
citation is typed, which is the estate's own stated preference: a mechanism that delivers the rule
at the moment it applies, never another statement of it. Deduped against `docs/traps.md` (nine
entries, none covers citation stamping) and the skill/rule reuse map. Cheap: the home is derivable
from `docs/decisions.md` plus one grep.
