# 2026-08-04 · hub — measuring the chroma claim instead of quoting it

> **Status:** `complete`

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

- **`tools/chroma_spill_probe.py`** — reproducible synthetic probe: builds a
  hairy-edged subject antialiased against a chroma field, keys it, and reports
  green excess in semi-transparent pixels at source / runtime / gameplay scale,
  keyed-only vs despilled.
- **`docs/findings/2026-08-04-generated-art-pipeline.md` §3** — the measured
  table plus three corrections to the inherited mechanism.
- **`.claude/skills/image-prompt/SKILL.md`** — the hard rule rewritten from
  "key then re-check after downscale" to **"despill at full resolution"**, plus
  a new **key-by-sampling-never-by-hex** rule.

The numbers: keyed-only carries **+99.9 / +108.6 / +104.3** mean green excess
at source / runtime / gameplay; despilled carries **−0.4 / −0.5 / −1.3**. And
directly verified: PIL LANCZOS and ImageMagick 6.9 `-resize` both return
byte-identical RGB whether chroma or black sits under alpha 0 — the
"bleeds-from-behind-alpha" theory is false on both.

The reconciliation worth keeping: spider-swing's record says the matte was
*"despilled **again** after resize"*. That double despill previously read as
belt-and-braces; it now has a mechanism.

## Honest nulls

- **Synthetic, not the three real images.** My spill model is a reasonable
  approximation of an antialiased chroma edge, but it is mine. The generated
  outputs remain unmeasured.
- **The reconciliation with the original session's claim is inference.** I did
  not observe their pipeline; I observed that the plain reading of their
  sentence does not reproduce, and offer a mechanism that does.
- **ImageMagick 6.9 only** — older versions are widely reported to differ on
  alpha handling and were not tested.
- **A real surface limit found:** conversation images arrive as inline vision,
  not files on disk, so they cannot be processed programmatically. Videos and
  `.md` attachments do arrive as paths. The owner is checking whether another
  upload route exists; if not, the workaround is a repo upload or a URL.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
python3 tools/chroma_spill_probe.py    # reproduces the table
```
