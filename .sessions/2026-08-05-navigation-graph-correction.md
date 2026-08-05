# 2026-08-05 · hub — correct the menu-parity claim: the navigation graph is the product

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: the previous PR shipped a measurement that was precise, exact,
reproducible, and answering a question nobody had. It counted what fraction of
*commands* build a view — in a bot whose commands nobody types.

## Previous-session review

PR #759 landed the superbot-next live audit. It recorded the menu-versus-text
ratio as **"inherited, not introduced"** on a 17%-vs-21% comparison. The owner
sent a screen recording of the old bot that makes the claim untenable, and the
correction is large enough to change what milestone one should build.

## What landed

- `docs/findings/2026-08-05-superbot-next-live-audit.md` — a new **§ 4b** on the
  navigation graph, a correction banner at the head, the reachability figures
  folded into § 3, a third consequence in § 5 (**the navigation tree is
  milestone zero**), the wrong claim recorded in § 7, and two new honest nulls.
- `docs/findings/README.md` — index row rewritten to carry the correction.

## Measured

**The old bot, from the owner's screen recording (2026-08-05):** `!help` leads
into launchers, not listings. Blackjack ships eight action buttons; Casino
offers New Poker Table with Roulette honestly disabled; Server Stats renders
**live computed values** — 3 members, 16 text channels, 1 voice, 5 roles — above
an eleven-button grid.

**The rebuild:**

| | Panels | Zero buttons |
|---|---|---|
| all subsystems | 314 | **153 (48%)** |
| `help` | 66 | **60 (91%)** |

Counted generously — a panel scores as "has buttons" even when every button is
Back/Home — so both figures are **floors**.

The mechanism is `diagnostic/command_catalog.py`, already on the § 1 list of
four `CAPTURE-WORLD LITERAL` files: the help pages render the captured *text* of
the old bot's help output rather than a live route table. Byte-identical to the
oracle, which is exactly why golden parity scored it 100%.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run **post-commit**.
- Reachability computed from the committed `manifest.snapshot.json` (exact, not
  sampled); the old bot's behaviour read from 39 frames extracted from the
  owner's 77-second recording, not from recollection of the repository.

**New honest nulls:** the figures count *declared* buttons, so a panel whose
buttons all reach "not armed" terminals still scores as having them — the true
dead-end rate is higher. And the two-tap property itself was **not** measured;
proving it needs the route table walked as a graph, which is proposed as the
acceptance test rather than reported as a result.

## 💡 Session idea

**The previous PR shipped a measurement that was exact, reproducible, and
answering a question nobody had.** It counted what fraction of *commands* build
a view — 17% against the old bot's ~21% — and concluded the difference was
inherited. Both numbers were right. The question was wrong, because in this bot
commands are not the interface; the button graph is, and the graph is what
failed to port.

The tell was available and got walked past: the owner's complaint was
*"none of the menus have clickable buttons"* — a statement about **menus** — and
it was answered with a statistic about **commands**. When a measurement
contradicts the person who uses the thing daily, the live hypothesis is that the
measurement is aimed wrong, not that they are.

Worse, the wrong number read as reassuring, so it was reported as a
counterweight to their concern. A precise answer to the wrong question is more
dangerous than an admitted unknown: it terminates the search.