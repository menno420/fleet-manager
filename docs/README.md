# `docs/` — what is behind each door

> **Status:** `living-ledger` · tier map and the repo-wide router:
> [`MAP.md`](MAP.md). This page is narrower on purpose — it describes only what
> sits **directly** beneath `docs/`, so that opening this folder tells you where
> to go next instead of showing you a sorted list of names.
>
> **Why it exists:** GitHub renders a folder's `README.md` when you open the
> folder. Until 2026-09-01 this one had none, so `docs/` opened as ~79 entries
> with nothing saying what any of them were — while every subdirectory below it
> already carried its own description. Owner's rule, live the same day:
> *"every time you go one layer deeper it should be clear which direction to
> go."*

## The doors

Each line is that folder's **own** first-line self-description, not a summary
written here — so this page cannot drift from what the folder says it is.

| Door | What it says it is |
|---|---|
| [`activity/`](activity/README.md) | what every session did, wherever it ran |
| [`audits/`](audits/README.md) | dated audits |
| [`conventions/`](conventions/README.md) | working conventions a live session is expected to follow |
| [`experiments/`](experiments/README.md) | pre-registered protocols + judge records |
| [`findings/`](findings/README.md) | dated measurements and their evidence |
| [`ideas/`](ideas/README.md) | idea backlog & lifecycle |
| [`owner-comments/`](owner-comments/README.md) | durable public feedback records |
| [`planning/`](planning/README.md) | plans and launch records |
| [`prompts/`](prompts/README.md) | deployed prompts — verbatim ledger |
| [`proposals/`](proposals/README.md) | owner-decision documents |
| [`providers/`](providers/README.md) | provider capability references |
| [`repos/`](repos/README.md) | Layer 2, one folder per repo |
| [`research/`](research/README.md) | overnight program reports |
| [`retro/`](retro/README.md) | seat-era retrospectives |
| [`succession/`](succession/README.md) | seat-era coordinator handoffs |

## What this page does NOT cover

**The 64 other files at this level** — 65 counting this README, `MEASURED`
2026-09-01. *(This line first said "64 files sitting loose at this level",
written in the same change that added this README and so wrong on arrival by
one: `docs/traps.md` TRAP-008, a count restated without re-testing it after the
thing it counts changed. Corrected 2026-09-01, phrased so the README is
excluded explicitly rather than silently.)* They are real and several are
CORE, but they are not doors — they are objects on the floor of this room, and
listing them here would duplicate [`MAP.md`](MAP.md), which is the repo-wide
router and already carries them with their tiers.

That is a **known defect, stated rather than hidden**: a room with 15 doors and
64 loose objects makes you check the floor before you can trust the doors. The
successor's folder design is where it gets fixed —
[`../owner/intent-workbooks/successor/`](../owner/intent-workbooks/successor/README.md).
