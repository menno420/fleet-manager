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
| 2 | `bootstrap.py:5274` | a repudiation cue is searched clause-wide, so it clears **every** occurrence of the capability on the line, not the one it characterises | `scan_text('"agents cannot merge" was superseded, agents cannot merge')` → no findings; the second, genuine assertion escapes |
| 3 | `bootstrap.py:5034` | `\bre?deploy(?:s\|ed\|ing\|ment)?\b` — the `re` is *`r` plus optional `e`*, so it matches `redeploy`/`rdeploy` but **not `deploy` or `deploying`**. Intended: `(?:re)?deploy`. Verified: `deploy` → False, `deploying` → False, `redeploy` → True | `scan_text('Merging is not walled, agents cannot deploy')` → no finding: the deploy wall has no family, so an unrelated merge repudiation clears it |
| 4 | `bootstrap.py:5374-5378` | the lookforward stop set is `_HEADING` / `_DATED_BULLET` / `_NEW_BULLET` / `_CONTRAST_START` — **no fence, no blockquote** — so a cue inside a separate block attaches to a wall above it | `scan_text('The rule is "agents cannot merge"\n```\nThis example was superseded\n```')` → no finding |
| 5 | the `SKILLS-index` template — read as the **embedded constant inside the vendored `bootstrap.py`**, not as a standalone `.tmpl` | teaches *"install with `python3 bootstrap.py skills --build`"* (verbatim, one occurrence in the dist), which only **stages**. No kit command writes `.claude/skills/`. **Every new adopter is told an install step that installs nothing** | any fresh adopt: run it, then `ls .claude/skills/` |
| 6 | `bootstrap.py:5078` | the conjunction clause-splitter separates a repudiation from the wall it qualifies when the cue follows `and` in the **same predicate**, so ordinary correction prose is flagged. A **false positive** regression | `scan_text('The "agents cannot merge" rule is false and no longer applies.')` → **1 hit** on v1.20.2, **0** on v1.20.1 |
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
**Two of the five clearing relaxations v1.20.2 shipped are now measured to
mis-fire**, one in each direction, and only one of them is loud.

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

### The harness — committed, because a reproduction in prose is not runnable

The original A/B run lived in an ephemeral scratchpad and would have vanished
with the container. Save as a file and run from the repo root with a banked
`bootstrap-<old>.py` present:

```python
import importlib.util, sys

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m
    spec.loader.exec_module(m); return m

CASES = [
    ('valid repudiation', 'The "agents cannot merge" rule is false and no longer applies.'),
    ('real wall (MUST stay red)', 'Agents cannot merge pull requests.'),
    ('same-line quoted repudiation', 'The "agents cannot merge" rule was superseded.'),
]
for label, path in (('old', '.substrate/backup/bootstrap-1.20.1.py'),
                    ('new', 'bootstrap.py')):
    m = load(path, 'kit_' + label)
    print('---', label, path, '---')
    for name, txt in CASES:
        print(f'   {name:32} -> {len(m.scan_text(txt))} hit(s)')
```

**Generalise it rather than treating it as one-off.** Any kit upgrade can be
A/B'd this way, because the banked previous dist is right there — the upgrade
creates it. Comparing old and new behaviour on the cases a checker is *supposed*
to get right is cheap, and it is the only thing here that found a regression as
opposed to a long-standing hole.

## What was checked and came back clean — do not redo these

- **fm's own `tools/check_no_false_walls.py` does not share defects 1–4.** It carries no `deploy` family and is a **separate implementation**. Nothing in fleet-manager needs patching for them.
- **Both scanners run in `substrate-gate`**, which is worth knowing before assuming a single fix point: fm's at the `repo checkers` step, the kit's via `bootstrap.py check --strict` → `check_no_false_walls` (`:5596`) → `scan_text` (`:5628`).
- **Defect 6 has no live impact on fleet-manager.** Searched, not inferred: `git grep -n -i -E "(is|was) false and (no longer|never)|and no longer applies|and (was|is) superseded" -- '*.md'` returns only documentation of the repro itself plus one unrelated hit. Positive control: `no longer applies` matches 4 files.
- **A green gate does not establish this**, and an earlier draft wrongly said it did: the kit's scanner walks `iter_adopter_files(...)` (`:5617`), not the tree, so `.sessions/` is outside it entirely.
