# ORDER 016 follow-ups — draft ORDERs (2026-07-11)

> **Status:** `plan` — ready-to-file draft ORDER text produced by the ORDER 016
> now-scope session (audit:
> [`../findings/instruction-and-env-audit-2026-07-11.md`](../findings/instruction-and-env-audit-2026-07-11.md)).
> **These are DRAFTS for the coordinator to file into `control/inbox.md`**
> (one-writer rule — this worker never touches `control/`). Numbers 017/018
> are the next-free suggestions at draft time; the coordinator assigns the
> final numbers and timestamps at filing.

## Rider from the R5 execution (one line, per the audit's low-urgency call)

The R5 repoint landed in the doc registry only
(`projects/codetool-lab-*/meta.md`): **if/when any codetool-lab-\* environment
is re-provisioned on the live console, the owner must also paste
`environments/archetype-python-lab.sh` into that environment's Setup-script
field** — console fields have no agent write surface. Archived labs, low
urgency (audit R5: "a real bug, low urgency"); deliberately NOT a hot
owner-queue item.

---

## ORDER 017 · 2026-07-11T06:5xZ · status: draft

priority: P1 — **GATED ON owner-queue item 16 (the §2.4 UNIVERSAL.md merge
clause): do NOT execute until the owner-queue item resolves** (the corrected
block must exist as owner-provenance text before any file is re-issued from
it).
owner: manager (self-executable once the gate clears; no further owner click)
do: **Re-issue every walled `projects/<repo>/instructions.md` from the
corrected UNIVERSAL merge clause** (audit §2.2 table — 12 of 13 files
prescribe the classifier-walled arm/REST-merge path as PRIMARY; only
substrate-kit is correct; superbot-idle / games-program / mobile-lab have
`meta.md` only and must be *born correct*). Keep each repo's own
required-check names and born-red gate. In the same pass:
(1) fix the **§3.2 same-file contradictions** — `fleet-manager/
instructions.md:76` mandates the REST squash-merge it lists as a classifier
wall at `:85`; `trading-strategy/instructions.md:92` says "MERGE AUTHORITY is
yours" then `:93-96` calls the classifier denial terminal;
(2) resolve the **§3.1 mandatory-block drift** — UNIVERSAL.md + README.md
claim the permissions block is carried verbatim in every `instructions.md`,
but a grep returns zero hits in 0/13; either actually insert the (corrected)
block into each file, or retract the "verbatim" claim and keep it
wake-prompt-only;
(3) execute the **§3.3 hoist** — centralize the ~10 near-verbatim duplicated
rule blocks into a "Fleet-canonical working rules" section of UNIVERSAL.md
(proposed block text in audit §3.3), leaving per-repo files only
repo-specific mission / CI-landing specifics / hard rails. *(Note: the hoist
adds text to owner-provenance UNIVERSAL.md — bundle it into the same
owner-landing sitting as §2.4 / the PR #47 v2 fold, or land it as a follow-up
owner paste; never self-edit that file.)*
Also fold in the **§5.4 per-lane enabler verification** before trusting the
"open READY, do nothing" doctrine per repo: confirm each repo actually has
`auto-merge-enabler.yml` installed in `.github/workflows/` AND "Allow
auto-merge" + a required check set — lanes that structurally can't arm
(fast-CI race / no checks-pending window / venture-lab
substrate-gate-not-required / trading Allow-auto-merge-OFF) get the two-party
non-author review-then-merge or a `GITHUB_TOKEN` merge-on-green workflow
noted in their re-issued file, not just corrected wording.
why: the fleet's canonical instruction tells every seat to do the thing the
platform classifier terminally denies — seats stall on merges and route
one-click asks to the owner nightly; fixing the root then re-issuing
propagates the fix to all 13 lanes (audit §0.1, §2).
done-when: all §2.2 walled rows re-issued from the corrected block (each with
its own required-check names/born-red gate kept); both §3.2 contradictions
gone; §3.1 resolved one way or the other with the claim and the files
agreeing; §3.3 hoist landed via an owner-provenance path; per-lane
enabler/arm status recorded per repo.
> **Per-lane verification landed (2026-07-11, ORDER 016 step 4):**
> [`../findings/enabler-install-verification-2026-07-11.md`](../findings/enabler-install-verification-2026-07-11.md)
> — only 3/13 lanes (substrate-kit, superbot, idea-engine) have the enabler
> installed, so **10 lanes need an enabler (or a `GITHUB_TOKEN` merge-on-green
> workflow) INSTALLED — an agent-doable PR per repo — before the corrected §2.4
> wording is true for them**.

## ORDER 018 · 2026-07-11T06:5xZ · status: draft

priority: P2
owner: manager (delegable to a lane worker; all doc/script work in this repo)
do: **Env-consolidation lane — audit R2/R3/R4/R6** (R1+R5 already landed by
the ORDER 016 now-scope session):
(1) **R2 — collapse the 4 Python archetype scripts into ONE base shim + 3
knobs** (`BASELINE_PIP`, `ENV_REPORT` var-list, `pick_python` table) —
coordinator's `setup_one` is already a strict superset of python-lab /
bot-prod / pinned-research manifest handling; the four become ~20–30-line
config diffs. **Fix in-flight: add the missing `superbot-next→python3.11`
case to the coordinator `pick_python` table** — superbot-next is a child of
the live multi-repo (coordinator) env and today installs under bare
`python3`, correct only by luck (audit §4.2 latent bug).
(2) **R3 — gba-lab stays separate; fix two lane gaps:** (a) it installs no
ROM-patch/distribution tooling — confirm pokemon-mod-lab's shipping model and
add `xdelta3`/`flips` if it emits base→modded patches (the ROM itself is
un-distributable); (b) gate the Block-3 devkitARM Track-B mirror pull behind
Butano/homebrew detection so a pokeemerald-only env stops pulling an
unsigned-mirror toolchain it never uses (directly affects the Retro-Games
seat spanning both game repos).
(3) **R4 — retire the per-package `setup-script.sh` probe variants** (dual,
drifting lineage; websites / substrate-kit / fleet-manager metas already flag
it) — pick one lineage; normalize superbot-games' split `environment/` vs
`environments/` dirs.
(4) **R6 — decide mobile-lab's shape before launch:** its Node/Expo toolchain
is orthogonal to all 5 archetypes; if a second JS lane appears, promote a
thin `node-lab` knob on the R2 base rather than repeating the repo
escape-hatch (mobile-lab is registered python-lab-with-escape-hatch as of
ORDER 016 R1, pending this decision).
why: the multi/single-repo detection block is byte-identical in all 5 scripts
and 4 of 5 archetypes are one base shim + a small knob-diff apart —
consolidation cuts the setup-script surface ~4→1, kills the drifting probe
lineage, and fixes a latent interpreter-pin bug on a live env (audit §4.2,
§4.3).
done-when: one base shim + knob table on main with the 4 archetype scripts as
thin configs (superbot-next→3.11 case included); gba-lab's two gaps
dispositioned; probe variants retired to one lineage; a recorded R6 decision
(node-lab knob vs escape-hatch stays) in `environments/archetypes.md`.
