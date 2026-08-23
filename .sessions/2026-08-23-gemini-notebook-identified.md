# 2026-08-23 — the Gemini notebooks product is identified, and my first reading of it was wrong

> **Status:** `complete` — branch `claude/r5-archive-execution-4dsvoh`, cut from
> `origin/main` at `dfbca97` (fm #930). Flipped after
> `python3 bootstrap.py check --strict` returned a real exit 0 on this tree,
> read directly and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

`OQ-GEMINI-NOTEBOOKS` was opened earlier today with the product deliberately
**unestablished** — the entry said one question would settle it and save a wrong
build. He answered with two screenshots. The entry can now stop asking.

## previous-session review

⟲ fm #930 (`dfbca97`) calibrated two asserted claims. The habit it was enforcing
— separate what was measured from what was read — is exactly what this card had
to apply to itself, one screenshot later.

## What landed

`docs/owner-queue.md` → `OQ-GEMINI-NOTEBOOKS`, product established with its
constraints:

- **`Gemini Notebook` IS NotebookLM, renamed.** Its own splash, verbatim:
  *"NotebookLM heet nu Gemini Notebook. Nieuwe naam. Hetzelfde geweldige
  product."* One product, **two entry points** — the standalone surface, and a
  `Notebooks` section inside the Gemini app *"mogelijk gemaakt door Gemini
  Notebook"*. PRO on both.
- **Max 300 sources** — scoped honestly to where it was read (the Gemini Apps
  splash, PRO account); whether the standalone surface or another tier differs
  is **not** established. It matters immediately: `idea-engine` is **566 files**
  and does not fit, so a bundle must consolidate rather than dump.
- **Custom instructions supported**, so a notebook can carry a standing brief.
- **The privacy split is asymmetric** — sources added in Gemini Apps are *not*
  used to train the models, but conversations *are* stored per Activiteit
  bewaren and used to improve them. Sources protected, chat not.
- **First-notebook candidate from his own recent chats** — Laser Cutting, Hobby
  CNC Milling, Servo Robot Arm, Fusion 360 — which is `curious-research`'s exact
  domain, and a repo parked by his own words, so feeding it disturbs nothing.

## The correction, recorded because it is the third of its kind today

My first pass wrote **"NOT NotebookLM"** into the entry, inferred from the first
screenshot's footer naming two surfaces. The second screenshot's rename banner
overturned it. Caught before commit, but written with the same unearned
confidence as the two earlier instances — the superbot services and the borrowed
PR counts.

**Same shape all three times: his live knowledge beat my reading of a partial
surface.** The pattern is now explicit in the entry itself rather than only in
`docs/traps.md`, because this one was not a stale *document* — it was a stale
*inference from an incomplete look*, which no route currently catches.

## What was checked, not assumed

- **The gate caught a dead relative link** (`../findings/…` from a file already
  inside `docs/`) and it was fixed, not silenced.
- **The 300-source figure is scoped to the screen it was read from**, rather than
  generalised to the product.

## Verify

`python3 bootstrap.py check --strict` → **exit 0**, read directly, never after a
pipe. Before the link fix it returned 1 on that one real finding.
