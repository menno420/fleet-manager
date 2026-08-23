# Front-door audit — the documentation gap is not presence, it is the return path

> **Status:** `audit` · 2026-08-23 · `MEASURED` unless tagged otherwise.
> Certainty legend:
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
>
> **Why this exists:** the owner's 2026-08-23 direction (OD-20) names the remedy
> for an estate that has grown hard to manage — *"making sure that each repo has
> proper documentation and is linked and explained in the fleet-manager for easy
> discovering."* Acting on that without measuring first would have commissioned a
> documentation sweep across 17 repositories. **Most of that sweep is already
> done.** What is missing is something else, and much cheaper.

## 1 · What was measured

For each of the **17 non-archived repositories**, the live default-branch tree
and commit list, via the direct-PAT path (`curl --noproxy '*'`, proxy bypassed):

- `GET /repos/menno420/{repo}/git/trees/HEAD?recursive=1` — presence and size of
  `README.md`, `docs/current-state.md`, any `PROJECT-CLOSEOUT`
- `GET /repos/menno420/{repo}/commits?per_page=1` — last commit date
- `GET /repos/menno420/{repo}/contents/README.md` → base64-decoded →
  `grep -ci "fleet-manager"` — whether the front door names the hub

## 2 · Presence — largely solved

| measure | result |
|---|---|
| carry a root `README.md` | **16 of 17** |
| carry `docs/current-state.md` | **15 of 17** |
| carry a closeout record | 8 of 17 |

**The three structural holes, all of them narrow:**

- **`superbot` has no root README** — the repo behind the **LIVE production
  Discord bot**, whose entry point is `docs/AGENT_ORIENTATION.md`. Anyone or
  anything arriving at the repository page gets nothing. This is the sharpest of
  the three because it is the highest-consequence repo in the estate.
- **`estate-backups`** — a **130-byte** README and no state file.
- **`superbot-plugin-hello`** — no state file (README present).

## 3 · The actual gap — the return path is missing in 9 of 15

`grep -ci "fleet-manager"` over each README, decoded from the live tree:

| names the hub | does not name the hub |
|---|---|
| `gba-homebrew` (3) · `pokemon-mod-lab` (3) · `idea-engine` (2) · `shiftlife` (2) · `venture-lab` (1) · `estate-backups` (1) | **`spider-swing` · `couch-legend` · `websites` · `superbot-next` · `substrate-kit` · `product-forge` · `sim-lab` · `curious-research` · `superbot-plugin-hello`** — 0 mentions each |

**So the estate's linking is one-directional.** `ESTATE.md` points *outward* to all
26 repositories; **9 of 15 front doors point nowhere back.** The four most
actively worked repositories — `spider-swing`, `couch-legend`, `websites`,
`substrate-kit` — are all in the silent column.

## 4 · Why the return path is the load-bearing half

`REASONED`, and it follows directly from a measurement this repo already holds.

The boot triad in [`.claude/CLAUDE.md`](../../.claude/CLAUDE.md) records
(`MEASURED` 2026-08-07 on `curious-research`) that a session booting in a
satellite repository loads **that repo's** `.claude/` and nothing of the hub's —
no estate read path, no doc-routing hook, no skills. The hub's apparatus cannot
route a session that never loaded it (PL-013).

**A back-link in the satellite's README is therefore the only mechanism that can
tell such a session the hub exists.** Every other channel is, by construction,
switched off. This is why the fix is not cosmetic: for 9 repositories, an agent
starting there currently has no reachable path to the orientation the owner is
asking to be discoverable.

It applies to the owner's own surfaces too — he is standing up an
AI-integrated laptop and using more than one assistant, and a surface that does
not load `.claude/` sees only the README.

## 5 · What this changes about OD-20

The directive reads as a large documentation programme. **Measured, it is three
narrow content holes plus nine one-line back-links** — and the second half is
mechanical enough to be checkable rather than remembered.

**Not done here, deliberately:** no README was edited. This finding sizes the
work; landing it across nine repositories is its own step, and OD-6's
one-thing-at-a-time rule applies to a nine-repo sweep more than to anything.

## 6 · Honest nulls

- **Truth was not assessed, only presence.** Whether each README *tells the
  truth* is the D2 fresh-session test and cannot be measured by tree shape. A
  large README can be confidently wrong; four repositories have not been
  committed to in over three weeks (`shiftlife` 07-27, `pokemon-mod-lab` 07-21,
  `superbot-plugin-hello` 07-15, `curious-research` 08-07), which is a staleness
  *signal*, not a finding — a paused repo whose README says it is paused is
  correct.
- **`grep -ci "fleet-manager"` counts mentions, not working links.** A repo
  scoring 1 might carry a broken path; a repo scoring 0 could conceivably link
  the hub by URL without naming it. Spot-checking the nine zeros was not done.
- **The nine archived repositories were not audited.** Several are explicitly
  kept as references — `superbot-mineverse` carries the SuperBot-World MASTER
  closeout, and the three code-tool labs are the install documentation for three
  released CLIs — so the same gap may exist there and is unmeasured.
  (`superbot-next` is **not** archived: it is active, gated on GCB-1, and is
  counted in the 17 above. An earlier draft of this bullet listed it as archived,
  which is wrong.)
