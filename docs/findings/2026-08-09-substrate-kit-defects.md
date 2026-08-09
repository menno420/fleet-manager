# Defects in substrate-kit v1.20.2 — the v1.21.0 session's worklist

> **Status:** `reference` · 2026-08-09 · `MEASURED` unless a row says otherwise
>
> **Who this is for:** the session that cuts **substrate-kit v1.21.0**. The owner
> ruled *"both, in order"* on 2026-08-09 — fleet-manager took released v1.20.2
> (fm #833), and the cut is a separate session because a release is
> outward-facing and reaches twelve adopters.
>
> **Why it is a `docs/findings/` file and not a session card.** It was written
> into fm #833's card first. That was the wrong home and the mistake is worth
> naming: a session card is a **record of a past session**, and a session that
> boots later walks the read path — it never opens a dated card it was not told
> about. The boot file already records this exact failure mode: *"a document
> that lives only in a handoff prompt is not in the repo."* A worklist nobody
> can find is a false-done waiting to be reported. Raised by owner-review.

## How these were found, and why that matters for how you use them

Every one came from **Codex reviewing the vendored `bootstrap.py`** across seven
rounds on fm #833 — it was in the diff because that PR upgraded the dist, so the
kit's own code got read by something other than its author, probably for the
first time since it shipped.

**Every one but the `SKILLS-index` template defect is in the kit's own
false-wall scanner** — the checker the
boot file calls load-bearing and that `substrate-gate` runs as a required status
check. That is the number to weigh when planning the session: **v1.21.0 should
budget review time, not just a version bump.** It is the same result as fm #831,
where 14 of 15 findings were in the checks themselves.

**None was patched in fleet-manager, deliberately.** `cmd_upgrade` archives and
then overwrites the vendored dist — observed directly on fm #833, where
`.substrate/backup/bootstrap-1.20.1.py` was created as `bootstrap.py` became
1.20.2 — and **no gate verifies the vendored file's hash.** That second half is
measured, not assumed: `grep -rn "sha256\|hashlib\|shasum" tools/ scripts/
.github/workflows/` returns **3 hits, all in `tools/sim/ci_tier_sim.py`**, which
uses hashlib for deterministic per-cell seeding and never touches the dist;
`check --strict`'s own output contains **0** hash mentions. Positive control:
the same search shape returns 33 `bootstrap` hits across those trees, so it does
reach the files.

A local patch would therefore be erased at the next upgrade while giving false
confidence in the meantime, and would silently fork the kit in one adopter until
then — with nothing anywhere able to notice either the fork or its erasure.

## The defects

Line numbers are against **vendored v1.20.2**.

| # | site | defect | reproduction |
|---|---|---|---|
| 1 | `bootstrap.py:5458-5459` | the render-marker early return exempts the **whole** `seat-digest.md`, so authored prose outside the generated fences escapes the scan. Its docstring justifies the exemption by *"the render's SOURCE docs are independently scanned"* — which does not cover hand-added text | append `Agents cannot merge` outside the fences with `is_render_path=True` → no hit; the same text elsewhere is flagged |
| 2 | `bootstrap.py:5274` | a repudiation cue is searched clause-wide, so it clears **every** occurrence of the capability on the line, not the one it characterises. **A false-negative REGRESSION** — v1.20.1 caught this, v1.20.2 does not | `scan_text('"agents cannot merge" was superseded, agents cannot merge')` → no findings; the second, genuine assertion escapes |
| 3 | `bootstrap.py:5034` | `\bre?deploy(?:s\|ed\|ing\|ment)?\b` — the `re` is *`r` plus optional `e`*, so it matches `redeploy`/`rdeploy` but **not `deploy` or `deploying`**. Intended: `(?:re)?deploy`. Verified: `deploy` → False, `deploying` → False, `redeploy` → True | `scan_text('Merging is not walled, agents cannot deploy')` → no finding: the deploy wall has no family, so an unrelated merge repudiation clears it |
| 4 | `bootstrap.py:5374-5378` | the lookforward stop set is `_HEADING` / `_DATED_BULLET` / `_NEW_BULLET` / `_CONTRAST_START` — **no fence, no blockquote** — so a cue inside a separate block attaches to a wall above it | `scan_text('The rule is "agents cannot merge"\n```\nThis example was superseded\n```')` → no finding |
| 5 | the `SKILLS-index` template — read as the **embedded constant inside the vendored `bootstrap.py`**, not as a standalone `.tmpl` | teaches *"install with `python3 bootstrap.py skills --build`"* (verbatim, one occurrence in the dist), which only **stages**. No kit command writes `.claude/skills/`. **Every new adopter is told an install step that installs nothing** | any fresh adopt: run it, then `ls .claude/skills/` |
| 6 | `bootstrap.py:5078` | the conjunction clause-splitter separates a repudiation from the wall it qualifies when the cue follows `and` in the **same predicate**, so ordinary correction prose is flagged. A **false positive** regression — the only one of the three that announces itself | `scan_text('The "agents cannot merge" rule is false and no longer applies.')` → **1 hit** on v1.20.2, **0** on v1.20.1 |
| **7** | `bootstrap.py:4969` | a `does not reproduce` cue describing **another subject** clears a genuine wall in a following subordinate clause, because `because` / `when` / `unless` are not clause boundaries. A **false negative** regression — **the most serious defect here** | `scan_text('The failure does not reproduce because agents cannot merge pull requests.')` → **0 hits** on v1.20.2, **1 hit** on v1.20.1 |

## Defect 7 is the one to fix first — a false NEGATIVE on a required gate

`MEASURED` 2026-08-09, same harness.

| input | v1.20.1 | v1.20.2 |
|---|---|---|
| `The failure does not reproduce because agents cannot merge pull requests.` | **1 hit** — correctly red | **0 hits** — the wall passes |
| `Agents cannot merge pull requests.` | 1 hit | 1 hit — control, correct in both |

**Rank this above defect 6, and the direction is why.** Defect 6 is a false
*positive*: it rejects valid prose, which is visible, annoying, and
self-announcing — someone hits it and fixes it. Defect 7 is a false *negative*:
**a genuine standing wall passes the required gate** whenever it sits after
`because`, `when`, `unless` or a similar unsplit subordinator. Nothing announces
it. The wall gets written down, the gate goes green, and a later session reads
the wall as fact.

That is precisely the failure the whole apparatus exists to prevent — the boot
file's *"never write down a limitation"* rule, the checker enforcing it, and its
required-check status all assume the scanner catches a wall when it sees one.
**Three of the five clearing relaxations v1.20.2 shipped are now measured to
mis-fire** — defects 2, 6 and 7 — and **two of the three are false negatives**
(2 and 7), so most of the damage is silent. An earlier version of this line said
*two*, and catalogued defect 2 as a long-standing hole; running
`tools/ab_kit_scan.py` showed v1.20.1 catching it and v1.20.2 not, which makes
it a regression. **The mistake was assuming a defect's age from its
description instead of measuring it**, which is the whole reason the harness
exists.

## Defect 6 is a measured regression — and the release is not simply worse

Both dists were loaded and asked the same three questions. This is the strongest
evidence here: not a reading of code, but the same function answering
differently in two released versions.

| input | v1.20.1 | v1.20.2 | reading |
|---|---|---|---|
| `The "agents cannot merge" rule is false and no longer applies.` | 0 hits | **1 hit** | **regression** — valid repudiation prose rejected |
| `Agents cannot merge pull requests.` | 1 hit | 1 hit | correct in both; the real wall still reds |
| `The "agents cannot merge" rule was superseded.` | **1 hit** | 0 hits | **improvement** — v1.20.1 false-positived here |

**Report it as a trade, because that is what it is.** v1.20.2's whole changelog
entry is *"`check_no_false_walls` clearing gains five attachment-based
relaxations"*, and row 3 is one of them working. The clause-splitter causing row
1 was added **deliberately** — the changelog says a mid-line conjunction *"is now
a clause boundary"* so a cue cannot bleed across it and blind a genuine wall.
Row 1 is the price, evidently unmeasured against the `X is false and no longer
applies` shape. **Adopting v1.20.2 was still right**: one false-positive class
traded for another, plus four other fixes.

### The harness — `tools/ab_kit_scan.py`, runnable

```
python3 tools/ab_kit_scan.py            # newest bank vs the live dist
python3 tools/ab_kit_scan.py --old <p>  # pin an older bank
python3 tools/ab_kit_scan.py --case "…" # add an ad-hoc string
```

Exit 0 always — an instrument, not a gate. Current output against v1.20.1:

```
bare wall (control)                          old=1 new=1            want=flag
wall after 'because' (defect 7)              old=1 new=0  DIFFERS   want=flag
second assertion after repudiated quote (d2) old=1 new=0  DIFFERS   want=flag
valid repudiation, conjunction (defect 6)    old=0 new=1  DIFFERS   want=clear
valid repudiation, same line                 old=1 new=0  DIFFERS   want=clear
deploy wall (defect 3)                       old=0 new=0            want=flag
```

**It was a fenced code block in this file until owner-review asked which path
held it.** That question was the point: a reproduction you must copy-paste is
not a harness. Making it a file found two bugs in it within one run —

1. it picked `bootstrap-1.9.0.py` over `bootstrap-1.20.1.py`, because
   `sorted()` is lexicographic and `"1.9.0" > "1.20.1"` as strings; that version
   predates `scan_text`, so every case errored. **A version sort that is really
   a string sort is wrong for about one release in twenty — the worst frequency
   for noticing.** Now sorted by parsed semver.
2. a dist without `scan_text` produced six identical stack-trace rows, reading
   like six failures rather than one wrong input. Now one plain line.

**Neither would have been found by re-reading the code block**, which is the
same lesson the defects below teach about the kit.

**Generalise it rather than treating it as one-off.** Any kit upgrade can be
A/B'd this way, because the banked previous dist is right there — the upgrade
creates it. Comparing old and new behaviour on the cases a checker is *supposed*
to get right is cheap, and it is the only thing here that found a regression as
opposed to a long-standing hole.

## What was checked and came back clean — do not redo these

- **fm's own `tools/check_no_false_walls.py` shares two of these — corrected 2026-08-09, and the first version of this line was the error.** It said *"does not share defects 1–4 … nothing in fleet-manager needs patching"*, generalising from the **one** defect actually tested (defect 3 — fm carries no `deploy` family, still true). **Measured properly**, by appending each payload to `docs/current-state.md` and running the checker, control first:

  | shape appended to `docs/current-state.md` | fm's checker | verdict |
  |---|---|---|
  | `Agents cannot merge pull requests.` — **control** | exit **1**, `FLAG [false-wall] …:482` | caught, so the test is valid |
  | defect **7** — `The failure does not reproduce because agents cannot merge pull requests.` | exit **0** | **shares the hole** |
  | defect **2** — `"agents cannot merge" was superseded, agents cannot merge` | exit **0** | **shares the hole** |
  | defect **6** — `The "agents cannot merge" rule is false and no longer applies.` | exit **0** | **correct** — this is valid repudiation prose; fm is right and kit v1.20.2 is wrong |

  **The mechanism in fm's checker, located and confirmed by prediction —
  so the fix is specific rather than "add a test".** `tools/check_no_false_walls.py:284-288`
  clears a wall if a negation token appears anywhere in the **fixed 48
  characters before the wall signal**, with **no clause boundary**:

  ```python
  # Negation in the ~48 chars before the wall signal (across the window).
  lead = window[max(0, sig_start - 48):sig_start]
  if NEG_TOKEN_RE.search(lead):
      return False
  ```

  In the payload, that lead is `The failure does not reproduce because ` — the
  `not` belongs to *"reproduce"* and clears a wall it does not negate.
  **Predicted and confirmed:** pushing the same negation past the 48-character
  window (`…does not reproduce in any of the very many long scenarios we tried,
  because agents cannot merge…`) makes the checker **catch** it (exit 1), while
  the short form passes (exit 0) and a bare wall is caught. **The boundary is
  literally a character count.**

  **This is not "silent by construction" and an earlier note wrongly said so** —
  that was a claim about the implementation, written before the implementation
  was read. It is a bounded heuristic missing a clause boundary: fixable by
  stopping the lookback at `because` / `when` / a comma, or by requiring the
  negation to attach to the wall's own subject. It is **the same class of bug as
  the kit's defect 7, reached independently in a separate implementation** —
  which is the more interesting fact, and the reason the two are not redundant.

  **So there is no redundancy where it matters most.** Defect 7 passes *both*
  implementations end-to-end: with the payload in a scanned doc,
  `check_no_false_walls.py --strict` exits 0 and `check --strict` reports zero
  false-wall findings, while the same file with a bare wall reds. **A genuine
  standing wall can be committed to a read-path doc today and no gate in this
  repo will notice.** That makes defects 2 and 7 fleet-manager's own bugs as
  well as the kit's, not merely upstream ones to file.

- **An earlier attempt at this test was invalid and is recorded rather than discarded.** The payload was first appended to `docs/CAPABILITIES.md`, where **the bare-wall control also passed** — because that file is the capability ledger and `tools/check_no_false_walls.py:296` special-cases it. The run proved nothing in either direction. **It was the positive control that exposed it**, which is the whole reason `capability-probe` step 3b requires one before recording an absence.
- **Both scanners run in `substrate-gate`**, which is worth knowing before assuming a single fix point: fm's at the `repo checkers` step, the kit's via `bootstrap.py check --strict` → `check_no_false_walls` (`:5596`) → `scan_text` (`:5628`).
- **Defect 6 has no live impact on fleet-manager.** Searched, not inferred: `git grep -n -i -E "(is|was) false and (no longer|never)|and no longer applies|and (was|is) superseded" -- '*.md'` returns only documentation of the repro itself plus one unrelated hit. Positive control: `no longer applies` matches 4 files.
- **A green gate does not establish this**, and an earlier draft wrongly said it did: the kit's scanner walks `iter_adopter_files(...)` (`:5617`), not the tree, so `.sessions/` is outside it entirely.
