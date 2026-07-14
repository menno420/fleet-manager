# Fleet kit-version table — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — do not hand-edit** (`scripts/gen_kit_versions.py`; INC-42 / central-docs-plan C4). Regenerate with every manager wake that touches kit state; kit `docs/adopters.md` stays sole-writer kit-lab — this table is derived from TREES (`substrate.config.json` + `.substrate/state.json` at verified HEADs), never from heartbeat prose (INC-40) and never from the adopters doc.
>
> generated-at **2026-07-14T04:49Z** · newest fleet tree version measured: **v1.15.0** (proxy for current release — the kit's own release ledger is kit-owned; this column is measured, not asserted). Kill-switch: if generated-at goes stale >7d, re-derive from trees before trusting a row.

| Repo | Pinned (`substrate.config.json`) | Tree (`.substrate/state.json`) | Drift verdict | Evidence (HEAD) |
|---|---|---|---|---|
| superbot | v1.0.0 | — | DELIBERATE PIN (INC-41 — never auto-'fix') | `50481b7` |
| superbot-next | v1.15.0 | v1.15.0 | CURRENT (= newest fleet tree) | `ef12ebe` |
| substrate-kit | v1.0.0 | — | DELIBERATE PIN (INC-41 — never auto-'fix') | `c0297d8` |
| websites | v1.15.0 | v1.15.0 | CURRENT (= newest fleet tree) | `2b5947d` |
| trading-strategy | v1.15.0 | v1.15.0 | CURRENT (= newest fleet tree) | `d857e50` |
| venture-lab | v1.15.0 | v1.15.0 | CURRENT (= newest fleet tree) | `991dd96` |
| superbot-games | v1.15.0 | v1.15.0 | CURRENT (= newest fleet tree) | `bc85689` |
| superbot-idle | v1.15.0 | v1.15.0 | CURRENT (= newest fleet tree) | `5ddd5a2` |
| superbot-mineverse | v1.15.0 | v1.15.0 | CURRENT (= newest fleet tree) | `0b388f1` |
| pokemon-mod-lab | v1.15.0 | v1.15.0 | CURRENT (= newest fleet tree) | `759dee4` |
| gba-homebrew | v1.15.0 | v1.15.0 | CURRENT (= newest fleet tree) | `b778d39` |
| product-forge | v1.7.0 | v1.7.0 | LAGS newest fleet tree (v1.15.0) | `4fdfa8a` |
| idea-engine | v1.15.0 | v1.15.0 | CURRENT (= newest fleet tree) | `d90a06a` |
| sim-lab | v1.15.0 | v1.15.0 | CURRENT (= newest fleet tree) | `09782df` |
| codetool-lab-fable5 | — | — | NO KIT (no substrate.config.json / state.json in tree) | `a6cf1a9` |
| codetool-lab-opus4.8 | — | — | NO KIT (no substrate.config.json / state.json in tree) | `80f6cd1` |
| codetool-lab-sonnet5 | — | — | NO KIT (no substrate.config.json / state.json in tree) | `66c3dfc` |
| fleet-manager | v1.15.0 | v1.15.0 | CURRENT (= newest fleet tree) | `e100bfe` |
| superbot-plugin-hello | v1.13.0 | — | PLUGIN-PIN DRIFT — host superbot-next pins v1.15.0 (INC-42: 'mirroring the host's pin' no longer holds) | `bbaccec` |

Notes: DELIBERATE PIN rows are design, not drift (INC-41 — superbot Q-0254 pin + the kit's owner-held self-pin). PLUGIN-PIN DRIFT compares a plugin repo's pin to its host's (superbot-plugin-hello→superbot-next); the 06023075→ff75b9eb manifest-hash class stays a follow-up (plan C10 `registry/pins.md`).
