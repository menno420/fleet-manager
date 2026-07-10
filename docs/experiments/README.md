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
