# 2026-08-04 · hub — measuring the chroma claim instead of quoting it

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · research — synthetic chroma-pipeline probe

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#718)

💡 Session idea: **a quoted mechanism is a claim wearing a measurement's
clothes.** This morning's art finding carried *"downscaling reintroduced magenta
into partially transparent edge pixels even though the full-resolution key was
clean"* as its single non-obvious technical fact — sourced, verbatim, from the
session that discovered it, and never tested here. Testing it took twenty
minutes and showed the plain reading is wrong: neither PIL nor current
ImageMagick bleeds colour out of fully-transparent pixels, and the spill that
does cause fringing is present at **every** scale including source. Downscaling
does not introduce it; it makes it *visible*. The remedy changes accordingly —
despill at full resolution as a rule, rather than audit-and-repair after resize.

The generalisable form: **inheriting a mechanism verbatim from a credible source
is not the same as knowing it.** A quote gets you the phenomenon; only a probe
gets you the causal direction, and the causal direction is what determines the
fix. Cite-don't-copy applies to *rulings*; mechanisms need re-derivation.

## previous-session review

`2026-08-04-hub-structure-converges-models.md` (PR #718, merged) closed with
"fringe after downscaling is still untested — the highest-value open
measurement of the day." The owner tried to supply the three generated images
and hit a real surface limit: **images arrive in-conversation as inline vision,
not as files on disk**, so Pillow has nothing to open (verified: nothing in
`/root/.claude/uploads/` or `/mnt/user-data/`; no MCP tool reads inline
attachments). Videos and `.md` files *do* arrive as file paths. Rather than
park the measurement on that, this session tested the mechanism synthetically —
which turned out to answer a more useful question than the original one.

## Scope

Probe the chroma pipeline end-to-end with a synthetic subject; correct the
mechanism in the art finding and the `image-prompt` skill. Not a program step;
NOW (E1) untouched.

## What landed

*(written at close)*

## Honest nulls

*(written at close)*

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
python3 tools/chroma_spill_probe.py    # reproduces the table
```
