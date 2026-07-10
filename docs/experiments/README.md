# Experiments — pre-registered protocols + judge records

> **Status:** `living-ledger`
>
> Pre-registered fleet experiments: each experiment commits its protocol +
> rubric BEFORE launch (fairness doctrine,
> [`docs/findings/gpt-5-6-report-2026-07-09.md`](../findings/gpt-5-6-report-2026-07-09.md));
> after launch the protocol is append-only (judge notes). Judge tooling lives
> in `tools/`.

| Experiment | Protocol | Prompt packages | Status |
|---|---|---|---|
| Harness × model (ultracode web session vs plain Project; 3 pairs, 6 repos) | [`harness-x-model-2026-07-09.md`](harness-x-model-2026-07-09.md) | [`pair-fable.md`](prompts/pair-fable.md) · [`pair-opus.md`](prompts/pair-opus.md) · [`pair-sonnet.md`](prompts/pair-sonnet.md) | pre-registered 2026-07-09; launch tonight; judging 2026-07-10 |

Judge tooling: `tools/wcag-contrast-check.py` — pre-registered WCAG contrast
recomputation (authoritative over in-repo checkers, PAIR-OPUS rubric).

## Standing caveats — apply to EVERY cross-arm comparison

- **Seat contamination (recorded 2026-07-10; superbot
  `docs/eap/fleet-overnight-review-2026-07-10.md` finding 6).** The gen-1
  codetool model-comparison (fable5 / opus4.8 / sonnet5 arms, launched
  2026-07-09) is **contaminated for cross-arm model conclusions**: coordinator
  and wind-down seats ran claude-fable-5 in at least the sonnet5 (and likely
  fable5) lanes — only sonnet5 discloses it loudly. Rules going forward:
  1. **Cross-arm comparisons score BUILDER seats only** — coordinator/
     wind-down/janitorial output is excluded from model attribution.
  2. Every arm records per-seat model identity (family-level names — fable-5,
     opus-4.8 — never exact IDs) **at the moment of work**; identity not
     written then is unrecoverable (blueprint §1 last bullet, same class).
  3. An arm whose builder-seat identity cannot be established from committed
     evidence is reported **"model unverifiable"**, not scored as its nominal
     tier.
  4. Per-seat *capability* differences (merge classifier, scheduling tools —
     `../capabilities.md`) are themselves a confound of the same class: a
     harness/model verdict must check whether the arms even had the same
     walls before attributing the delta to the model.
