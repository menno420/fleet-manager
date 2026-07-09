# Deployed prompts — verbatim ledger

> **Status:** `living-ledger`
>
> Verbatim record of every Custom Instructions block and startup/coordination
> prompt deployed to the fleet, 2026-07-09. These are the gen-1 texts — the
> gen-2 blueprint revises them; never edit history here, add dated successors.

## Index

| File | What it is | Deployed? |
|---|---|---|
| [`init-prompt-universal.md`](init-prompt-universal.md) | Per-project fleet-protocol init prompt (puts a Project on the coordination protocol) | ✅ fleet-wide |
| [`trading-lab.md`](trading-lab.md) | trading-strategy Custom Instructions + startup prompt | ✅ |
| [`codetool-arms.md`](codetool-arms.md) | The three identical-by-design model-arm Custom Instructions + startup (fable5 / opus4.8 / sonnet5) | ✅ ×3 |
| [`game-mining.md`](game-mining.md) | superbot-games mining-lane Custom Instructions + startup | ✅ |
| [`game-exploration.md`](game-exploration.md) | superbot-games exploration-lane Custom Instructions + startup | ✅ |
| [`universal-wakeup.md`](universal-wakeup.md) | Universal self-review / wake-up prompt (sent to all 10 lanes) | ✅ fleet-wide |
| [`external-campaign-metaprompt.md`](external-campaign-metaprompt.md) | ChatGPT prompt-creation meta-prompt for the external review campaign | ✅ (to ChatGPT) |
| [`venture-lab-draft.md`](venture-lab-draft.md) | Proposed venture-lab mission | ❌ NOT YET DEPLOYED — gen-2 born-right pilot candidate |

## Conventions this ledger records

- **Custom Instructions** blocks live in each claude.ai Project's settings
  (owner-pasted — agents cannot edit them; R16/R17 queue changes to the owner).
- **Startup prompts** are the first owner message that boots the lane.
- Model assignment is set in the Project UI, not in the prompt text.
- Related gen-1 revision work: [`../gen2-blueprint.md`](../gen2-blueprint.md)
  §2 lists what these texts lacked, from the fleet's own retros
  ([`../findings/retro-synthesis-2026-07-09.md`](../findings/retro-synthesis-2026-07-09.md)).
