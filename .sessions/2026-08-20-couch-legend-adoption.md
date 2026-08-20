# 2026-08-20 · hub — the Grok one-prompt game adopted: couch-legend created, rebuilt, live

> **Status:** `in-progress`

- **📊 Model:** fable-5 · product work, owner-live directive — the owner asked
  the session to orient, open the Grok-built app at `idle-stoner.grok.me`, see
  if it can be improved, create a new repo for it with his PAT, and state back
  how the goal is perceived; mid-session he added the durable frame: *"Eventually
  I want this to be a fully working android game. What I need is a solid base
  for the mechanics. The main idea should be clearly mapped and decided."*
  This session created `menno420/couch-legend`, reconstructed the game from its
  deployed bundles into a tested platform-neutral engine + web UI, added
  identity-preserving improvements, deployed it to GitHub Pages, and records
  the adoption here.

Time: 2026-08-20 · venue: owner-live hub chat (remote container) · branch
`claude/grok-app-review-setup-qu2bz2`

## What is about to happen

The records batch for the new repo: Layer-2 folder `docs/repos/couch-legend/`,
`docs/current-state.md` shipped-entry, program §7 row (product work, not a
lettered step), this card's close-out, strict gate, Codex loop, flip.

## Previous-session review

⟲ fm #869 (merged `e72b949`): the Slices 21+22 records. Checked at `main`:
`docs/repos/product-forge/README.md` carries the keyboard+foldables thread as
landed, §7 rows present, current-state entry present. Nothing to repair.

## 💡 Session idea

The reconstruction method itself is reusable: a Grok App Builder app exposes no
source, but its deployed Vite bundles beautify into fully readable data tables
and formulas — a one-session path from "AI prototype at a URL" to "owned tested
repo". If the owner prototypes more apps this way, the ORIGIN.md +
DESIGN.md + faithful-port-then-additive-improvements shape from couch-legend is
the template.

## Close-out

**Shipped (this PR — records only):**
- This card · [`docs/repos/couch-legend/README.md`](../docs/repos/couch-legend/README.md)
  (Layer-2 entry point: three threads — mechanics base landed · Android shell
  next · balance pass open) · `docs/current-state.md` shipped-entry · program
  §7 row (appended at ledger end).

**Shipped (outside this PR, verified live):**
- `menno420/couch-legend` — created via the PAT path (repo, description,
  homepage), source pushed as `142cd14` (45 files): pure engine + content
  tables (`src/lib/`), React/Vite UI, original art/fonts, `docs/DESIGN.md`
  (binding mechanics map + the decided Capacitor Android path),
  `docs/ORIGIN.md` (provenance), 32-test suite, `ci.yml` + `pages.yml`.
- GitHub Pages enabled (`build_type: workflow`, API 201); both workflows
  green on `142cd14`; <https://menno420.github.io/couch-legend/> + every
  referenced asset probed 200.
- Played end-to-end in Chromium on the byte-identical local build (hits
  including keyboard, generator purchase, achievements + revelation toasts,
  save persistence, reload-resume, zero console errors). Chromium cannot
  reach external hosts from this container (connection reset both direct and
  proxied) — venue fact; curl verifies the deployed surface.

**Verify:** `pnpm check` in couch-legend — typecheck + 32/32 vitest + vite
build, exit 0 (run three times across fixes; final run clean). fm strict gate
at flip. Workflow poll: `ci:completed:success | pages:completed:success` on
`142cd14` (2 × 15 s iterations).

**⚑ decide-and-flag (MEDIUMs, all reversible):** repo name `couch-legend`
(the game's actual title; the URL slug `idle-stoner` was Grok's project name) ·
public visibility (D-0012 publish-by-default; the owner had already published
the prototype + share link) · GitHub Pages over Railway (static SPA, zero
cost, the Railway estate was just consolidated down) · no required status
check day one (revisit when a second session works there) · no LICENSE file
yet (owner call; this card is the flag's home).

**Layer-2 handoff:** docs/repos/couch-legend/README.md — created (entry point
+ three threads).

**PR:** fm #870 — terminal state recorded at flip.
