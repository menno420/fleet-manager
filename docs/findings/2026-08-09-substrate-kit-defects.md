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
| 1 | `bootstrap.py:5458-5459` | the render-marker early return exempts the **whole** `seat-digest.md`, so authored prose outside the generated fences escapes the scan. Its docstring justifies the exemption by *"the render's SOURCE docs are independently scanned"* — which does not cover hand-added text. **REGRESSION:** old=1, new=0 | append `Agents cannot merge` outside the fences with `is_render_path=True` → no hit; the same text elsewhere is flagged |
| 2 | `bootstrap.py:5274` | a repudiation cue is searched clause-wide, so it clears **every** occurrence of the capability on the line, not the one it characterises. **A false-negative REGRESSION** — old=1, new=0. Caveat: v1.20.1 rejects the quote-only control too, so its red is right for the wrong reason and does not prove it isolated the second assertion | `scan_text('"agents cannot merge" was superseded, agents cannot merge')` → no findings; the second, genuine assertion escapes |
| 3 | `bootstrap.py:5034` | `\bre?deploy(?:s\|ed\|ing\|ment)?\b` — the `re` is *`r` plus optional `e`*, so it matches `redeploy`/`rdeploy` but **not `deploy` or `deploying`**. Intended: `(?:re)?deploy`. **Long-standing:** old=0, new=0 | `scan_text('Merging is not walled, agents cannot deploy')` → no finding: the deploy wall has no family, so an unrelated merge repudiation clears it |
| 4 | `bootstrap.py:5374-5378` | the lookforward stop set is `_HEADING` / `_DATED_BULLET` / `_NEW_BULLET` / `_CONTRAST_START` — **no fence, no blockquote** — so a cue inside a separate block attaches to a wall above it. **REGRESSION:** old=1, new=0 | `scan_text('The rule is "agents cannot merge"\n```\nThis example was superseded\n```')` → no finding |
| 5 | the `SKILLS-index` template — read as the **embedded constant inside the vendored `bootstrap.py`**, not as a standalone `.tmpl` | teaches *"install with `python3 bootstrap.py skills --build`"* (verbatim, one occurrence in each dist), which only **stages**. No kit command writes `.claude/skills/`. **Long-standing:** both commands exit 0 with 14 staged and 0 live skills | any fresh adopt: run it, then `ls .claude/skills/` |
| 6 | `bootstrap.py:5078` | the conjunction clause-splitter separates a repudiation from the wall it qualifies when the cue follows `and` in the **same predicate**, so ordinary correction prose is flagged. A **false positive** regression — the only one of the three that announces itself | `scan_text('The "agents cannot merge" rule is false and no longer applies.')` → **1 hit** on v1.20.2, **0** on v1.20.1 |
| **7** | `bootstrap.py:4969` | a `does not reproduce` cue describing **another subject** clears a genuine wall in a following subordinate clause, because `because` / `when` / `unless` are not clause boundaries. A **false negative** regression — **the most serious defect here** | `scan_text('The failure does not reproduce because agents cannot merge pull requests.')` → **0 hits** on v1.20.2, **1 hit** on v1.20.1 |

**Independent classification, fm #835:** five defect behaviours are new in
v1.20.2 (**1, 2, 4, 6, 7**) and two are long-standing (**3, 5**). The harness
originally printed only defects 2, 3, 6, and 7; defect 1 and 4 were established
with one-off probes and defect 5 only in prose. That did not satisfy the claim
that one command reran all seven. `tools/ab_kit_scan.py` now runs the six scanner
cases and the fresh-adopter command/template contract in one invocation.

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
**Five defect behaviours are new in v1.20.2** — defects 1, 2, 4, 6 and 7 —
while defects 3 and 5 are long-standing. **Defect 6 is the only loud one in the
set**; everything else either loses a wall or, for defect 5, teaches a step that
does nothing. Defect 2 needs a narrower statement than the first review gave it:
v1.20.1 returns one hit and v1.20.2 returns zero, so the line-level behaviour is
a regression, but the old scanner also returns one hit on the valid quote-only
control. It was red because it rejected the repudiated quote, not because the
harness proved it isolated the genuine second assertion. Raw hit counts require
semantic controls; they are not their own interpretation.

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
bare wall (control)                                  old=1 new=1            want=flag
authored prose in render file (kit defect 1)         old=1 new=0  DIFFERS   want=flag
wall after 'because' (kit defect 7)                  old=1 new=0  DIFFERS   want=flag
second assertion after repudiated quote (defect 2)   old=1 new=0  DIFFERS   want=flag
valid repudiation, conjunction (kit defect 6)        old=0 new=1  DIFFERS   want=clear
valid repudiation, same line                         old=1 new=0  DIFFERS   want=clear
deploy wall (kit defect 3 — family never matches)    old=0 new=0            want=flag
cue across a fence (kit defect 4)                    old=1 new=0  DIFFERS   want=flag
skills install contract (kit defect 5):
  old: claim=1,init=0,build=0,staged=14,live=0
  new: claim=1,init=0,build=0,staged=14,live=0
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

- **fm's own `tools/check_no_false_walls.py` shared defects 2 and 7 at the fm
  #833 baseline; fm #835 closes defect 7 locally and leaves defect 2 explicit.**
  The first version of this record said *"does not share defects 1–4 … nothing
  in fleet-manager needs patching"*, generalising from the one defect actually
  tested. The independent review ran a positive control and each payload before
  changing the checker, then reran the acceptance fixtures after it:

  | shape in a scanned `docs/current-state.md` fixture | before fm #835 | after fm #835 | verdict |
  |---|---:|---:|---|
  | bare wall — control | exit **1** | exit **1** | still caught |
  | defect **7** — `does not reproduce because agents cannot merge` | exit **0** | exit **1** | local hole fixed |
  | direct correction — `does not mean agents cannot merge` | exit **0** | exit **0** | valid prose remains clear |
  | defect **2** — repudiated quote, then a second assertion | exit **0** | exit **0** | still a separate local hole; outside fm #835's accepted scope |

  **The confirmed mechanism** was the old fixed lookback: any negation token in
  the 48 characters before a wall signal cleared it, even if a clause boundary
  such as `because` put that negation on another predicate. A sweep of the old
  source found the exact token-end cliff: distance 44 and 45 cleared; 46 through
  48 flagged; the bare-wall control flagged. The coarse fixture requested by the
  owner therefore also reproduces: 44 clears and 48 flags.

  fm #835 preserves the 48-character bound for a direct correction that hard-
  wraps, but starts it after the last punctuation, conjunction, or subordinator.
  `because`, `when`, `unless`, and a comma now prevent an earlier predicate's
  negation from attaching to the wall. The permanent self-test covers the bare
  wall, the `does not reproduce because` failure, the direct-negation control,
  and hard-wrapped versions of both attachment directions.

  **The two scanners are now redundant for defect 7 where they were jointly
  blind before.** The vendored v1.20.2 scanner still misses the payload, but the
  fleet-manager checker makes the combined gate red. Defect 2 remains jointly
  blind and is recorded rather than silently broadened into this narrow fix.

- **An earlier attempt at this test was invalid and is recorded rather than discarded.** The payload was first appended to `docs/CAPABILITIES.md`, where **the bare-wall control also passed** — because that file is the capability ledger and `tools/check_no_false_walls.py:296` special-cases it. The run proved nothing in either direction. **It was the positive control that exposed it**, which is the whole reason `capability-probe` step 3b requires one before recording an absence.
- **Both scanners run in `substrate-gate`**, which is worth knowing before assuming a single fix point: fm's at the `repo checkers` step, the kit's via `bootstrap.py check --strict` → `check_no_false_walls` (`:5596`) → `scan_text` (`:5628`).
- **Defect 6 has no live impact on fleet-manager.** Searched, not inferred: `git grep -n -i -E "(is|was) false and (no longer|never)|and no longer applies|and (was|is) superseded" -- '*.md'` returns only documentation of the repro itself plus one unrelated hit. Positive control: `no longer applies` matches 4 files.
- **A green gate does not establish this**, and an earlier draft wrongly said it did: the kit's scanner walks `iter_adopter_files(...)` (`:5617`), not the tree, so `.sessions/` is outside it entirely.
