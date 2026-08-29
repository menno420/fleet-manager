# spider-swing — how to work here

> **Status:** `reference` · true as of **2026-08-08**
>
> **RATIFIED 2026-08-08.** This file began as a proposal — the design's starting
> shape had no "how to work here" file. It exists because gates, verify commands
> and landing discipline are what a session needs **before** attaching, and they
> are neither state nor goals. The owner kept it as a **distinct file**, so it is
> part of the shape every folder replicates ([`../intent.md`](../../intent.md)
> § 8).
>
> **Canonical for nothing.** spider-swing's **binding** contracts are
> `CONSTITUTION.md` (working agreement + autonomy rails) **and
> `docs/architecture.md`** (layering, invariants, decomposition rules) — both
> carry the `binding` badge and both win over this file.
> `docs/AGENT_ORIENTATION.md` is a **reading-router**, not the instruction set:
> it tells you which docs a given task needs. What is here is the operational
> subset worth knowing *before* you attach, plus the traps that have actually
> bitten.

## The gates — `MEASURED` 2026-08-08 against the rulesets API

`main` carries one **active** ruleset, `main-required-checks` (id `20148292`),
with two **required status checks**:

| check | workflow |
|---|---|
| **`substrate-gate`** | `.github/workflows/substrate-gate.yml` |
| **`game-quality`** | `.github/workflows/game-quality.yml` |

Both must be green for a PR to land. Note the difference from fleet-manager,
which requires `substrate-gate` only — **do not carry this repo's assumptions
into that one, or the reverse.**

Read this from the rulesets endpoint, never from
`branches/main/protection` — that path returns 404 because no *classic*
protection is configured, which is a true answer that reads like an absence of
protection. There is protection; it is a ruleset. (`capabilities.md` § Access.)

The full active workflow set: `android-debug`, `android-release`,
`auto-merge-enabler`, `branch-sweep`, `game-quality`, `ref-cleanup`,
`substrate-gate`, plus Dependabot updates.

## Verify before you push

Two commands, and **read real exit codes — never `$?` after a pipe**:

```bash
python3 tools/verify.py            # engine + project checks
python3 bootstrap.py check --strict # kit discipline: docs, session card, walls
```

`tools/verify.py` is the repo-specific one and it is strict by design: it
rejects the wrong engine version, a Mono build, parse failures, fatal script
diagnostics, or a missing engine when engine checks are required. The engine is
pinned to **Godot 4.7.1 Standard (no .NET), GDScript only**, by `.godot-version`.

`android-debug` builds an installable APK on every push to `main` — which is the
supply line for the Play listing screenshots, and the reason those can be real
capture rather than mock-ups.

## Landing discipline

Same kit discipline as here: a **born-red session card first**
(`.sessions/<date>-<slug>.md`, status not `complete`), work, then flip to
`complete` last so `check --strict` goes green on the commit that closes the
session. The repo has **142 cards** — it is an unusually well-kept journal, and
the newest card is the fastest way to learn what the last session actually did.

**Always ask `@codex` explicitly** — post the literal comment `@codex review`
rather than relying on it noticing the PR. Its about-box also advertises PR-open
and draft→ready triggers, but those did not fire when measured (2026-08-29, fm
#974: zero activity after 26 minutes on a READY-opened PR). Once asked it
answers in about **5.5 minutes** with findings as *inline* comments. Wait for it; never merge a PR you have asked it to review.
(`capabilities.md` § Review.)

## The boundary that is easy to cross by accident

spider-swing's own `docs/reading-path.md` carries a standing rule: **writes stay
in that repo.** Cross-repo work routes through coordination, never a direct push
to a sibling. In the Layer 2 model this is automatic and worth stating anyway —
a session boots *here*, attaches spider-swing, works there, and comes back
*here* to update this folder. The folder update is a fleet-manager write made
while inside fleet-manager. There is no cross-repo write anywhere in the loop.

## Traps that have actually bitten

**Never commit** a keystore, a private key, `keystore.properties`, or anything
carrying a keystore password. The upload key is the owner's; a lost one is
recoverable through Play Console, but a committed one is not.

**Screenshots for the store must be real capture.** Generated imagery invents
interface and physics — one generated clip in this estate put three ATTACH
buttons in a single frame. Generated art is fine for the feature graphic and
never for anything implying "this is how it plays".

**A permanent field deserves a grep, not a memory.** The owner was mid-way
through the Play Console *Create app* form — where the package name is permanent
and non-reusable — while the owner queue still recommended an identifier derived
from a name ruled out hours earlier. It was caught by `grep -rn "swingyspider"`
across both repos, not by recall.

**Art: one asset per generation *call*.** A 41-item queue on a surface with no
execution boundary between items became **one** generation, and the assets were
sliced back out of a composite board — *"production-ready candidates: none"*,
with a **more** detailed manifest than the successful runs. A batch is safe
exactly when the surface turns it into N calls. Ask what the surface does with a
queue before handing it one.

**Art: despill at full resolution; key by sampling a corner pixel.** Downscaling
does not introduce chroma — measured directly, PIL LANCZOS and ImageMagick both
return byte-identical RGB regardless of what sits under fully-transparent
pixels. The fringe was always in the semi-transparent edge pixels; resize only
changes its *proportion*. And the key colour is never the hex you asked for
(measured fields near `#22C022` and `#3E8E3E`, none within tolerance 40 of
`#00FF00`), so an exact-hex keyer matches zero pixels. Full method:
[`../../findings/2026-08-04-generated-art-pipeline.md`](../../findings/2026-08-04-generated-art-pipeline.md)
and the `image-prompt` / `asset-pipeline` skills.

**Seamless backdrop tiling is a false constraint here.** The renderer draws every
second tile mirrored (`posmod(tile_index, 2) == 1` in
`game/presentation/scripts/swing_lab.gd`), so each tile's right edge meets its
own reflection. Asking a generator for seamless backdrops costs quality for
nothing. Tiling **is** required for the purpose-built rail tiles.
