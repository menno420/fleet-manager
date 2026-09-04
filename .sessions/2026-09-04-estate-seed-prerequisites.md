# 2026-09-04 — the `estate` seed's own prerequisites: row-level source drift, a provenance validator, the canonical-state column

> **Status:** `in-progress` — **What is about to happen:** the merged estate truth
> baseline (fm #1020, verdict `PARTIAL`) is re-read at HEAD and the seed-time
> requirements its § 11/§ 12 name are worked inside fleet-manager — not the
> seed itself (gated on the kit release cut, [D-0025] + the build order), not
> substrate-kit (another session's K1–K5), not E1 (the program's NOW pointer,
> the owner's). First step, already run: the delta against `anchors.tsv`; the
> moved set is the same four repositories the handoff named (couch-legend,
> fleet-manager, spider-swing, substrate-kit). Next: a row-level instrument
> that says for each manifest row whether the FILE it cites moved since the SHA
> it was verified at (the handoff's "every carry row's source SHA" re-check,
> made mechanical), which doubles as the path/instant provenance validator
> § 12 item 10 says is missing; the `canonical_state_source` column § 12 item
> 11b names as a seed-time requirement, added through the generator and the
> manifest REGENERATED; the refute lane's overclaim schema given a consumer
> that joins on a named subject (§ 12 item 11).

- **📊 Model:** withheld · xhigh · feature build
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01DwEAXW4q4eT8v4nPqJbTq6](https://claude.ai/code/session_01DwEAXW4q4eT8v4nPqJbTq6) · "Estate truth baseline review"

## What shipped

*(in progress — written at close)*

## ⟲ Previous-session review

*(in progress — written at close)*
