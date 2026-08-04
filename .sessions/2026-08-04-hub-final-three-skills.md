# 2026-08-04 · hub — audio-prompt, capability-probe, owner-brief

> **Status:** `complete`

- **📊 Model:** fable-5 · high · docs-only — the last three gap skills, owner-approved

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#722)

💡 Session idea: **a skill can be honest about being ahead of its evidence.**
The image family was reverse-derived from accepted work; the audio skill has
no accepted example — the owner is explicitly not happy with the current
samples. The dishonest options were to wait (leaving the recurring task
unskilled) or to invent rules in the image family's confident voice. The
third option: build the skill from what IS solid — the committed delivery
contract, the transferable method — and **mark each section's provenance**
(measured · transferred · unmeasured), with the provider comparison written
in as the skill's own first step rather than its missing prerequisite. A
skill that knows what it doesn't know can still route work correctly.

## previous-session review

`2026-08-04-seed-skill-router.md` (kit PR #572, merged) seeded the router.
This card fills the last three routed-to gaps — and en route, this session
also resolved the PL-013 numbering collision in kit PR #565 (renumbered to
PL-014 across nine files, main merged in, 2116 tests green, pushed to that
PR's branch; it stays held for owner review under its law label).

## Scope

Owner-directed: create the remaining gap skills. Audio conditional on being
good without an accepted example (resolved via provenance marking);
capability-probe and owner-brief judged fully derivable — the first from the
discovery rule's own text, the second from the owner's observed asks and the
collaboration model's owner-assist standard. Router + index wired. Not a
program step; NOW (E1) untouched.

## What landed

- **`audio-prompt`** — both routes (procedural generator, AI generation)
  against spider-swing's committed contract (mono 44.1 kHz 16-bit WAV,
  sub-0 dBFS + 3 ms fades, mathematically continuous loops, manifested
  provenance). Explicit provenance labels per section; the unmeasured
  AI-provider question is the skill's own first-run comparison step, with
  the result routed to the capabilities ledger.
- **`capability-probe`** — the discovery rule as an executable method:
  ledger → environment → attempt once → verbatim evidence → same-session
  append. Fires at the moment of thinking "I can't". Carries the day's
  measured traps verbatim (the tool-routing false wall, one-probe
  generalisation, absence-of-evidence).
- **`owner-brief`** — LANDED / YOUR EYES / NEXT, plain language only, no
  technical identifiers in the body, one-letter decisions with bolded
  recommendations, under-a-minute rule, honest nulls survive translation.
- Router rows + `SKILLS-local.md` entries for all three.

## Honest nulls

- **None of the three has fired.** audio-prompt additionally cannot be
  validated until the owner's next real audio ask — and its Route B carries
  zero measured providers, by design and by label.
- **owner-brief's shape is derived from observed asks**, not from an
  owner-stated spec; its rules (no jargon, under a minute, one-letter
  choices) are inferences from how he actually works. First use will test
  them; he can correct cheaply.
- The kit #565 renumber leaves that PR's *content* unreviewed by me beyond
  the collision — its measured-claim ruling is its authoring session's work,
  held for the owner as law requires.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
