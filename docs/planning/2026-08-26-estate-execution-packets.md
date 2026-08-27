# 2026-08-26 — the estate execution packets: one plan, per-repo, for the two boot venues

> **Status:** `plan` · 2026-08-26 (evening) · the execution decomposition of
> [the legibility plan](2026-08-26-legibility-and-intent-plan.md), owner-directed
> the same day.
>
> **What this is:** the legibility plan's three moves — gate the next-agent
> contribution · the per-repo digest · the review surface — decomposed into
> **work packets, one target repository each**, sized for one sitting, executable
> by a session booted on either of the estate's two boot venues (§ 4). Plus the
> local-work surfaces (laptop · OneDrive hub · Google Drive), because the owner
> chose one coherent plan over two.
>
> **What it is NOT:** a replacement for the
> [consolidation program](2026-07-26-consolidation-program.md) (THE plan, whose
> NOW pointer now names this doc for legibility sequencing), the
> [roadmap](2026-08-08-agent-operating-environment-roadmap.md), or the
> [legibility plan](2026-08-26-legibility-and-intent-plan.md) (the baseline this
> refines — its diagnosis, measurement and § 9 levers are not restated here).
> It contains **no intent content** — intent is produced by the owner's own
> conversations, deliberately after Wave B — and **nothing scheduled**: every
> refresh is on-touch.
>
> Provenance per entry: `OWNER` / `MEASURED` / `REASONED` / `UNVERIFIED` per the
> [certainty legend](../findings/2026-08-05-foundation-continuation.md).

## 1 · The owner's frame — why this plan, in his words

`OWNER`, 2026-08-26 evening, hub chat (verbatim record:
[owner-direction § 5](../findings/2026-08-26-owner-direction.md); recorded as
**OD-22** in the program):

- **Boot venues are exactly two.** Sessions start on **fleet-manager** (cloud),
  or locally **inside the OneDrive / local-disk hub**, which already carries a
  copy of the skills and whose sessions are already told to review fleet-manager
  first (*"tho this might also need some work"*). The other repos *"will never
  be used as boot repo"* — **which is why fleet-manager must carry proper links
  and summaries of each repo.**
- **The OneDrive hub is *"basically a repo of its own … kinda like the local
  version of fleet-manager"***, and he wants the two centralised better
  (`OQ-ONEDRIVE-HUB`, § 5 Wave B).
- **Satellites CAN read fleet-manager.** They are just not routed to it unless
  directed. `MEASURED` this session: fleet-manager is public — an
  unauthenticated `https://raw.githubusercontent.com/menno420/fleet-manager/main/README.md`
  fetch returns HTTP 200 — and his local agents can view all of his GitHub
  (`OWNER`). What a satellite boot lacks is **auto-loaded apparatus and
  routing** (boot-triad case two, measured 2026-08-07) — a discovery gap, never
  an access wall. An earlier draft of this plan wrote "cannot read
  fleet-manager"; he corrected it, and § 3's claims audit carries the retraction.
- **The root cause he wants fixed:** agents should *"take initiative to do their
  own research inside and outside the repos they work in, to help solve the
  problems they encountered for the next sessions"* — the substrate-kit's
  purpose, *"obviously not working as intended"*. The estate is *"one large
  connected web of repos and files that should all agree on most things and
  make it easy for any agent to navigate."*

**The goal this plan serves, restated once:** any agent, booted on either venue,
orients fast, navigates the whole web, and leaves it better — initiative on the
way in, a gated contribution on the way out.

## 2 · What changed from the merged legibility plan, and why

The three moves and the § 9 levers survive intact. Eight changes, each with its
reason:

1. **The `.claude/` census is corrected: 10 of 19 non-archived repos have no
   `.claude/` directory, not 4.** `MEASURED` this session
   (`GET /repos/menno420/{repo}/contents/.claude` across all 19; six 404s
   spot-verified by direct curl against fleet-manager/spider-swing 200
   controls): absent in `creator-kit`, `estate-backups`, `gba-homebrew`,
   `pokemon-mod-lab`, `product-forge`, `sim-lab`, `spider-bot`,
   `substrate-kit`, `superbot-plugin-hello`, `venture-lab`. The plan's § 2.4
   listed four. Consequence reframed by OD-22: since satellites never boot,
   this is a **digest fact** (what a session would get *if* booted there, and
   which repos rely wholly on the kit's staged apparatus), not a workflow
   constraint.
2. **The writeback token's scope is `UNVERIFIED`, not "READ-scoped".** The
   merged plan § 4 states the deployed token is read-scoped; that is
   `app/writeback.py`'s docstring claim — nobody has probed the deployment, and
   per the owner's standing choice nobody does: the packet plans around the
   owner's mint either way (§ 5 Wave D).
3. **Move 1's checker is specified added-card-lane-scoped — never a
   `session_markers` needle.** `REASONED` from the kit's own text: the R13–R15
   precedent is exit-affecting *"scoped to this single added card so no
   historical card is retroactively reddened"* (vendored `bootstrap.py`
   :6950–6957), written after a card-grammar addition *"pre-reddened every
   later bare `check --strict` run via the newest-by-mtime fallback"*
   (:6921–6923). A needle would retro-red every hopped adopter's newest
   historical card — and put `superbot`'s deliberately red-at-2 gate at
   red-at-3. The `null` rule is pinned **one-directional**: a declared value
   requires its file delta in the same diff; extra deltas are never forbidden,
   and `null` + one line is always a legal answer.
4. **Move 1's venue: prototype in fleet-manager first, kit release second.**
   The merged plan said "ship it in substrate-kit"; the roadmap § 6 promotion
   rule (`OWNER`: observe → prototype → test → promote, never "good idea →
   mandatory infrastructure everywhere") puts one working repo-local round
   first. The kit release (PKT-A2) follows immediately after the prototype
   holds — this is sequencing inside Move 1, not a demotion of it.
5. **The wave is enumerated, not counted.** "16 adopters" becomes **9 external
   hops + fleet-manager**, with named skips (owner-held, archive-queued,
   R2-bound) and per-repo methods — `superbot` is vendor-dist + bump-pin, never
   `adopt`/`upgrade` (program §7, 2026-08-13). The kit's adopter registry
   cannot drive the wave (its scan roster misses five adopters — recorded on
   [the kit's entry point](../repos/substrate-kit/README.md)); the census
   command in § 3 drives it, and PKT-A2 carries the roster fix.
6. **The kit release also carries the venue line and the activity-log pointer
   estate-wide.** Both are fleet-manager-local amendments today
   (`.sessions/README.md`, session-close 5c); shipping them in the kit's card
   protocol means the wave propagates them instead of nineteen hand edits —
   and closes the satellite-pointer gap the
   [activity README](../activity/README.md) header names as real undone work.
7. **Move 3's comments live in fleet-manager**, the records home — his
   *"centralise this better"*. Delivery per venue: cloud sessions boot
   fleet-manager (routing fires); local sessions review fleet-manager first
   (the hub's boot instruction, tightened in PKT-B3); every other surface gets
   the digest's "unconsumed comments" row and the per-repo `AGENTS.md` pointer.
   The alternative — committing each comment into its target repo — is
   **rejected with reason**: it scatters owner direction across 19 repos, and
   owner direction is estate-level record ([intent](../intent.md) § 1: product
   truth in the repo, estate records here).
8. **Figures refreshed and two tool facts added**: the same-day drift from the
   plan's numbers is explained in § 3, and `scripts/gen_kit_versions.py` is
   named as *seat-era precedent, not reusable* (it imports the retired roster
   and writes the frozen `registry/`), so Move 2's generator enumerates live
   repos from `GET /user/repos` instead.

## 3 · The figures this plan stands on — re-derived this session, command beside each

| figure | value | how it was measured (2026-08-26, this session) |
|---|---|---|
| repositories | **28 total · 19 non-archived · 9 archived** | `GET /user/repos?per_page=100&affiliation=owner` over the direct-PAT path |
| cards, last 7 calendar days | **79 across 6 repositories, 1 in flight** (this plan's own born-red card) | `python3 tools/estate_activity.py refresh` — the regenerated [estate-log](../activity/estate-log.md) in this PR |
| reachable from a fleet-manager session without the log | 59 own · **20 unreachable** (`websites` 9 · `couch-legend` 7 · `product-forge` 2 · `sim-lab` 1 · `idea-engine` 1) | same run |
| venue stated | **5 of 79** — all five are 2026-08-26 cloud cards, so the token took on day one | same run |
| invisible work | `spider-bot` · `creator-kit` · `superbot` (11-day gap) · `spider-swing` (11-day gap) · `estate-backups` | same run, its invisible-work section |
| kit versions | **5 live versions across 16 adopters**: 1.21.0 ×10 (couch-legend, creator-kit, fleet-manager, gba-homebrew, idea-engine, substrate-kit, superbot, superbot-next, venture-lab, websites) · 1.20.2 spider-swing · 1.20.1 shiftlife · 1.15.0 ×3 (pokemon-mod-lab, sim-lab, superbot-plugin-hello) · 1.7.0 product-forge | `GET /repos/menno420/{repo}/contents/substrate.config.json` → `kit_version`, all 19 |
| `AGENTS.md` | **0 of 19** | `GET /repos/menno420/{repo}/contents/AGENTS.md`, all 19 probed (404 = absent; positive control: the same call shape returns 200 on files that exist) |
| `.claude/` | **absent in 10 of 19** (list in § 2 item 1) | `GET /repos/menno420/{repo}/contents/.claude`, all 19 + six curl spot checks |
| no card protocol | `curious-research` · `estate-backups` · `spider-bot` · `superbot-plugin-hello` | the refresh run's own section |
| fleet-manager's ideas | **18 idea files — 15 dated 2026-07-09/10/11 (EAP), 3 dated August** | `ls docs/ideas/*.md` (19 entries minus the README) |
| fleet-manager's journal | still the planted placeholder headings | `head -20 .session-journal.md` |
| fleet-manager visibility | **public**; unauthenticated raw README → HTTP 200 | `curl -o /dev/null -w '%{http_code}' https://raw.githubusercontent.com/menno420/fleet-manager/main/README.md` |

**Drift from the merged plan's figures, explained:** the plan measured 74 cards
/ 54 reachable / venue 0-of-74 that morning; the day's four merges (#947–#950)
plus this card moved them to 79 / 59 / 5-of-79. Same window length, later
moment — drift, not disagreement.

**The claims audit this plan went through.** The owner asked for unproven
claims to be found before execution; three were: *"a satellite session cannot
read fleet-manager"* (**retracted** — access exists, discovery is the gap, § 1);
*"local sessions are per-folder in satellites"* (**superseded** by OD-22's
boot-venue statement); *"the laptop has no Python"* (**reworded** —
`UNVERIFIED`: the [setup sitting](../owner-steps-2026-08-21-laptop-setup.md)
installed none and no local card records a kit-gate run, but nobody probed his
PATH, so every local packet opens with a `python --version` precheck instead of
an assumption). Recorded measurements this plan leans on but did not re-verify
live — spider-swing's two required checks (2026-08-08) · superbot's watch-filter
rebuild-safety (2026-08-14) and red-at-2 gate · the kit's `min_upgrade_from`
release field — are each re-verified by the packet that consumes them, at
execution time, before acting.

## 4 · The execution model

**One packet = one sitting = one target repository.** The executor is a session
on one of the two boot venues:

| executor | what it has | how it reaches the target repo |
|---|---|---|
| **fm-cloud** — booted on fleet-manager (Claude Code web/container) | fm's `.claude/` (hooks, skills, routes), `$GITHUB_PAT` + MCP tools | `add_repo` + clone, or raw fetch for read-only |
| **hub-local** — booted in the OneDrive / local-disk hub on the laptop | the hub's skills copy; `gh` CLI; told to review fleet-manager first | per that repo's own venue rule — most: fresh clone → work → push → delete (spider-bot's documented rule; a stale resident clone reading as authoritative is the failure the hub already measured). The hub's exact layout is `UNVERIFIED` until PKT-B3 documents it |
| **either** | — | most packets; the packet says so |

**The venue block every packet inherits (stated once, referenced as
"the venue block"):**

- **Local precheck:** `python --version` (or `python3 --version`, or
  `py -3 --version`) — **record which interpreter answered and use IT for every
  command in the packet**: the packets write `python3` as the canonical form,
  and on a Windows hub where only the `py` launcher exists, a literal
  `python3` fails after the precheck passed (`@codex` fm #951). If none
  answers, the local gate cannot run; the **server-side required check on the
  PR is the binding gate** and the session must let it decide (never merge on
  red). Then `gh auth status` and `git --version`. Shell is Git Bash; in
  PowerShell read `$LASTEXITCODE`, never `$?`, and never an exit code after a
  pipe (TRAP-002).
- **Landing mode is per-repo and the packet names it:** PR-with-born-red-card
  (kit adopters) · push-to-main-deploys-production (`spider-bot`) · no CI
  (`estate-backups`). Where an auto-merge enabler arms at PR open (`superbot`,
  `superbot-next`, `venture-lab`), disable it or apply `do-not-automerge`
  **before** requesting review.
- **Windows traps already measured here:** UTF-8 explicitly on file IO (the 📍
  token broke a default-locale read once — fixed in `estate_activity.py`), and
  the case-collision that shadowed a file (fm #886).
- **Every satellite packet carries its fm context inlined** — for speed and
  self-sufficiency, not because fm is unreachable — plus the fm pointer for
  depth. A session that wants more **is expected to go read fleet-manager**
  (§ 1: initiative is the point).

**How completion becomes visible without anyone ticking a list:** the packet's
own born-red card lands in the target repo → `python3
tools/estate_activity.py refresh` rolls it into the derived lane → the digest
regen (once PKT-B1 lands) marks the repo current. The § 5 catalog is the
tracking surface; an fm-venue session refreshes its status column **on touch**,
never on a schedule.

## 5 · The packet catalog

Grammar per packet: **target · executor · context · steps · acceptance ·
verify · non-scope · needs**. The wave-A hop rows share one pattern (below) and
carry only their deltas.

### Wave A — close the inflow (Move 1)

> § 9's own test, restated: if only this wave lands, the estate still self-heals
> from that point forward. It must not slip.

**PKT-A1 · fleet-manager · either venue.** Add the contribution marker to the
card grammar and gate it repo-locally.
*Steps:* (1) the card protocol (`.sessions/README.md`) gains
`- **♻ Carried forward:** idea | journal | both | null — <one line>`;
(2) a deterministic checker — fm-owned, in `tools/`, **invoked from
`scripts/preflight.py`** (the planted local↔CI parity list: `check --strict`
and CI's substrate-gate both run it, so local green and CI green stay one
predicate — `@codex` fm #951: wiring it only through `scripts/repo_checks.sh`
would leave it CI-only, the exact divergence preflight.py was planted to end) —
runs **in the added-card lane only** and checks the declared value against the
same diff:
`idea` ⇒ a change under `docs/ideas/` · `journal` ⇒ a change to
`.session-journal.md` · `both` ⇒ both · `null` ⇒ nothing required, the line is
the record. No prose is read, content is never graded, extra deltas are never
forbidden (§ 2 item 3).
*Acceptance:* a test card declaring `idea` with no `docs/ideas/` delta reds the
lane; the same card with the delta greens; `null` greens; **a branch with only
pre-marker cards passes bare `python3 bootstrap.py check --strict`** (the
no-retro-red proof).
*Verify:* `python3 bootstrap.py check --strict`, real exit code.
*Non-scope:* no kit change; no content judgement; no backfill of old cards.

**PKT-A2 · substrate-kit · either venue (release runs from the kit repo).**
Ship the contract into the kit and cut the release.
*Steps:* port PKT-A1's marker + checker (same added-card scoping) into
`src/engine/` → `python3 src/build_bootstrap.py` (dist is GENERATED and
byte-pinned); add the **venue line** and the **activity-log pointer** to the
kit's card protocol (§ 2 item 6); fix the adopter scan roster
(`docs/fleet-repos.txt` — five adopters invisible today); record the release's
`min_upgrade_from`; cut via `release.yml` **workflow_dispatch** (tag pushes 403
through the git proxy — path quirk, use the workflow); verify the **published
asset** three-way sha256 against `release.json` and the sidecar — never a
changelog read (the fm #833 lesson: adopters vendor the published file, so what
it contains *is* the payload).
*Acceptance:* the downloaded published asset contains the checker and the venue
line; sha256 agrees three ways; the registry regen sees all adopters.
*Verify:* `python3 scripts/preflight.py` in the kit; `scripts/verify_release.py`.
*Non-scope:* no adopter hops in this packet; **the kit ships no `AGENTS.md`**
(that is the owner's estate-wide call, PKT-B4); the
[34-row kit worklist](../findings/2026-08-13-substrate-kit-v1210-followups.md)
is its own track — named here so it is not silently absorbed, not folded in.
*Needs:* PKT-A1 held for one round first (§ 2 item 4).

**PKT-A3…A11 · the rollout wave — one hop, one sitting, one repo.** Shared
pattern: read the repo's pin → download the new dist + verify sha256 three ways
→ bank a rollback copy of the vendored `bootstrap.py` → vendor + bump
`kit_version` → **diff every regenerated workflow and revert regens that drop
host customizations** (the recurring wave lesson) → run the repo's local gate →
born-red card, PR, `@codex review` at the exact head, wait ≥ 6 min, then
**read BOTH verdict surfaces and match the head SHA** (`@codex` fm #951):
findings arrive as inline comments (`/pulls/{n}/comments`, and the review
object carries `commit_id`), but **a clean pass creates no review object at
all** — it lands in `/issues/{n}/comments`, its shape varies, and the match
rule is `Reviewed commit:` first, else membership among the body's 40-hex SHAs
(`CAPABILITIES.md` § Codex's CLEAN verdict). Never conclude "no review" from
the review surface alone → land on green → verify pin + dist sha at `main`.

| hop | deltas the pattern must know |
|---|---|
| `couch-legend` | checks `ci` + `substrate-gate`; **land it yourself** (no live enabler, by design); local gate `pnpm check` + `python3 bootstrap.py check --strict` |
| `creator-kit` | 1.21.0, kit present but CI state unknown — read the repo first; brand new, one seed commit |
| `gba-homebrew` ⚑ | **owner-gated**: required `NDS ROM build` reds every cold-cache PR (BlocksDS pin unrecoverable), so a hop PR cannot merge on green — his letter first (owner lane) |
| `idea-engine` | standard; gate green at main (2026-08-14 measurement) |
| `superbot` | **vendor-dist + bump-pin only** — `adopt`/`upgrade` both over-correct here (program §7, 2026-08-13); gate **honestly red at 2** (orientation-budget, enforcement-unwired) — expected, never "fixed"; required check is `Code Quality`; **enabler arms at PR open — disable/label first**; docs-only pushes are rebuild-safe under the watch filter — re-verify the filter live before pushing anyway |
| `venture-lab` | required check `substrate-gate`; **enabler ACTIVE — `do-not-automerge` at open**; rider: restamp its `docs/current-state.md` kit-version line (recorded next-touch item) in the same PR |
| `websites` | required check `quality`; GITHUB_TOKEN-attributed merges fire **no** push-event workflows — a Pages rebuild needs an explicit dispatch; local gate + four pytest suites |
| `spider-swing` | 1.20.2 → new; **two** required checks, `substrate-gate` AND `game-quality` (re-verify from the rulesets endpoint, not prose); local `python3 tools/verify.py` + `check --strict` |
| `sim-lab` | 1.15.0 — check the release's `min_upgrade_from` first; hop stepwise if required |

**PKT-A12 · fleet-manager · the post-release hop** (`@codex` fm #951 round 2 —
without it fm stays on v1.21.0 running the prototype beside the engine copy
forever): vendor the published dist, bump the pin, **retire the A1 prototype
in the same PR** — reconcile `scripts/preflight.py` to the engine's checker,
expect the prototype in the carve-out list, and keep the added-card-scoped
acceptance tests green against the released implementation.

**Skipped, with reasons (the honest wave):** `pokemon-mod-lab` — owner-held
(program, 2026-08-14; owner lane) · `shiftlife` — paused by OD-15, hop
owner-paced (owner lane) · `product-forge` — 1.7.0 but R2-bound and its
remainder archive-queued; upgrading a repo slated for archive is spent effort
(flagged, his overrule welcome) · `superbot-next` **and**
`superbot-plugin-hello` — the archive-queued pair (R5's gated rows), treated
identically: no hop; if the owner archives them the question dissolves.

### Wave B — the digest, the hub, the pointers (Move 2)

**PKT-B1 · fleet-manager · fm-cloud (or hub-local with Python).** The digest
generator.
*Steps:* `tools/estate_digest.py` → one committed
`docs/repos/<name>/digest.md` per non-archived repo (creating Layer-2 dirs
where none exist), carrying **Configured** (kit version + delta vs latest ·
`.claude/` present · `AGENTS.md` · card protocol · required checks read from
the rulesets endpoint · gate command · deploy binding where recorded · live
scheduled workflows · last touch + venue) · **Intent** (the declared entry
point from [ESTATE](../ESTATE.md), whether it exists, its date,
written-or-template · Layer-2 threads · the dated audit verdict, stamped as a
judgement) · **Digest** (the hand-written summaries — **embedded at render
from a separate, hand-owned `docs/repos/<name>/summary.md`**, never generated
text: a full re-render would otherwise silently delete PKT-B2's prose,
`@codex` fm #951 round 2; empty slots rendered honestly until B2 writes them)
· **unconsumed owner comments** (empty until Wave D; reads
`docs/owner-comments/<repo>/` excluding `consumed/`). Every page
GENERATED-bannered with a per-repo `measured_at` **plus the printed
boundary** — "treat as stale after <measured_at + 14 d>" — because a
committed page cannot flip its own text when time passes: the page
self-describes the boundary and **consumers compute age at read time** (D1
renders the STALE mark from `measured_at`; an agent reader compares the
date — `@codex` fm #951 round 2). Never hidden, never auto-refreshed.
Fields are derived by diffing each repo's whole `substrate.config.json` against
a reference — a hand field list is what always goes stale here.
**Wired, not prose:** `session-close` gains the local-amendment step (the 5c
shape, fm #947 precedent) — *regenerate the digest for every repo this session
touched* — so freshness follows work, on the venue where the generator runs.
*Acceptance:* 19 digests committed; three spot-diffs against live API agree; a
second run is idempotent; every page prints `measured_at` and its "stale
after" boundary; **a re-render with a populated `summary.md` present
round-trips the hand prose byte-identical** (the preservation proof — the
stale-mark *rendering* test belongs to D1, which computes age at read time).
*Verify:* `python3 bootstrap.py check --strict`.
*Non-scope:* no hand summaries (B2); no website (D); no schedule.

**PKT-B2 · fleet-manager · either.** The hand-written summaries, batched
by cluster (the bots · the games · the labs · web/infra) — written into each
repo's **hand-owned `docs/repos/<name>/summary.md`** (the generator embeds it
at render; it never generates or overwrites it): dated pointer prose in the
Layer-2 register (what the repo is for at a glance, which files matter,
where its truth lives), **never intent** (his conversations own that) and never
a copy of the repo's own docs.
*Acceptance:* every digest's Digest slot filled from its `summary.md` or
carrying an honest "nothing beyond ESTATE's line yet"; each summary cites what
was actually opened. *Verify:* `check --strict`.

**PKT-B3 · the hub (OneDrive / local disk) · hub-local session, owner-directed
— held until his GO.** Amended 2026-08-27→28
([owner direction](../findings/2026-08-28-owner-direction.md) §§ 2–4, 6): his
2026-08-26 *"himself"* meant *via local sessions* — *"they have the full
ability to work on both sides and see everything"* — so the executor is
**hub-local only** (the one venue that reads both the hub and GitHub), and
nothing runs before his GO (*"no execution yet, because I still have more to
plan"*). This packet is the written target so that sitting starts from a page,
not a chat memory.
*Steps:* (1) document the hub into `docs/activity/onedrive.md` +
`laptop.md` + `google-drive.md` (the shape already planned in
[activity](../activity/README.md) § Planned: *what it is · what is on it ·
current state · what to know before continuing · last checked* — plus, per the
08-27→28 direction: the venue-handoff contract, a **lean account of the main
things that happened**, and the public-surface content rule) — including
the hub's actual layout (where the skills copy lives; whether repo clones live
inside it), which is `UNVERIFIED` until written; (2) tighten the hub's
review-fleet-manager-first boot instruction to mirror the six-read pointer —
his own *"tho this might also need some work"* — and wire the scope routing
rule into the hub's close hooks, all three branches (repo work → that repo's
own card · cross-repo/estate-level work → this section · machine/personal
work → the hub's own records, with only the lean public-safe account reaching
these pages · push when a handoff is intended): a mechanism at the moment of
action, never another rule statement ([intent](../intent.md) § 4); (3) the centralisation question is **no longer a
step here** — `OQ-ONEDRIVE-HUB` was rescoped 2026-08-27→28 to unhurried hub
housekeeping (git versioning for its own sake), its recommendation (a)
withdrawn as a sync path; it blocks nothing in this packet. **One residual
stays named (`@codex`, fm #954): the pages give a cloud session sight of
hub-only work, never the files themselves.** The routing rule's own answer is
that work meant to continue in the cloud lands in a repo before the handoff
(push-at-close); if a genuine handoff ever depends on artifacts that live only
in the hub, the a/b/c options are the recorded transfer candidates and the
question re-opens as a sync question — visibility satisfied is not transfer
solved.
*Acceptance:* the three pages exist and a cloud session can answer both "what
is on the laptop right now" and "can I pick up the task that was started
there" from them. *Non-scope:* nothing executes before the owner's GO; nothing
personal or security-relevant reaches the public pages.

**PKT-B4 (×N) · one packet per non-archived repo · either venue · gate OPEN —
his AGENTS.md yes landed 2026-08-28** (*"Agents.md should indeed be
everywhere"*, `OQ-FM-AGENTS-BOOT` answered — execution still waits on his GO
for plan work, and one design question is parked for the substrate-kit
sitting: hand-write the 19 files as below, or teach the kit to plant and
maintain them; the ×N form
is the C8 shape — landing modes and gates differ per repo, so each row is
independently completable, `@codex` fm #951 round 2). One ~15-line root
`AGENTS.md` per repo: what the repo is (one line) · its own read-first path
(from [ESTATE](../ESTATE.md)'s read-first column, inlined per row) · the hub
back-link (fleet-manager is the estate's router — public, raw-fetchable) · the
activity-log pointer · the owner-comments pointer (Wave D's delivery surface).
The argument stands as corrected 2026-08-26: **saving the first hunt and
declaring a read path — never remedying blindness.**
*Sequencing:* the four audit-failure repos (`spider-swing`, `product-forge`,
`estate-backups`, `websites`) get theirs **after** their Wave C fixes — a
pointer at a contradicting front door would deliver the falsehood faster.
*Per-repo deltas:* `gba-homebrew` — the cold-cache-red trap applies to any PR;
land with its hop or the owner's letter. `spider-bot` — see PKT-C6's deploy
caution; one batched docs commit. `pokemon-mod-lab` — private, plan-gated
protections; PR flow normal otherwise.
*Verify:* per repo's own gate where one exists; otherwise the PR checks.

### Wave C — per-repo truth passes (absorbs the intent audit's § 7 briefs)

> Order: the [audit](../findings/2026-08-23-active-repo-intent-audit.md) § 6
> rule — *contradicting beats empty; among contradicting, the one not corrected
> on contact goes first; a running clock breaks ties.* Classification precedes
> fixing (its § 7 preamble: two briefs changed on classification).

**PKT-C0 · fleet-manager · fm-cloud.** Rate the five unrated
(`superbot` · `superbot-next` · `websites` · `couch-legend` · `shiftlife`) —
one read each, raw fetches, no attach: open the declared entry point's
delegation target and judge pass / contradicting / empty. One sitting; the
audit's own § 1 note says exactly this is owed.
*Acceptance:* five verdict lines appended to the audit (dated, one read each
named); any new contradicting front door slots into the Wave C order by the
§ 6 rule. *Verify:* `check --strict`.

**PKT-C1 · spider-swing · either venue · THE FIRST SITTING** (declared
out-of-order exception: zero dependency on Waves A/B — `MEASURED`: the
pre-hop checker greps marker *presence* only, and this packet adds no marker —
~30 minutes, subtractive, and it teaches the packet form).
*Context inlined from the audit § 7.1:* the README's front matter contradicts
the repo's own ledger on the one thread with an external clock. Four claims to
delete/replace, two rows to add — **line numbers were against the 345-line file
as of 2026-08-24; re-read before editing**:
(1) the *"'Spider Swing' is a codename … not approved release branding"*
blockquote → the settled position: published as **Slingy Spider** /
`com.menno420.slingyspider` since 2026-08-05 (source:
`docs/product/name-status.md`, PR #171); (2) *"No release signing exists."* →
release signing exists and is owner-controlled (`android-release.yml`,
dispatch-only, has run through vc66); (3) *"…store publishing remain absent"* →
narrow to what is true: no public listing, no billing SDK — a signed build sits
on the internal-testing track (owner-confirmed in the repo's own ledger);
(4) the Documentation table lists ten docs and neither `docs/current-state.md`
nor the closed-test runbook — add both; (5) fix the table's own *Name status*
row the same way as (1). **The one addition:** the front door states the clock —
12 testers × 14 continuous days, then ~7 days review; finished code does not
compress it. **Do not rewrite the body** — the architecture, roadmap and verify
sections are accurate and are why the file reads as trustworthy.
*Acceptance (the audit's own):* a cold session reading `README.md` alone states
the name is decided, a signed build is on Play's internal track, closed testing
has not started, and the floor is three weeks.
*Verify:* `python3 tools/verify.py` + `python3 bootstrap.py check --strict`;
required checks `substrate-gate` + `game-quality`.
*Non-scope:* no Play actions (owner-gated `OQ-PLAY-*`); no tuning; no art.

**PKT-C2 · product-forge · either.** *Inlined from § 7.2, in this order:*
(1) **README first** — era-mark the seat-era framing (banner, never delete),
name **phone-controller** as what the repo now is (v0.22.0, 22 slice cards,
`products/phone-controller/README.md` 18 KB) **without dropping `games-web`**
(state it honestly: last touched 2026-07-10, deployment state unchecked unless
checked); (2) then `docs/current-state.md` (all four sections are template) —
the material lives in the slice cards + product README; (3) then `control/` —
four ORDERs still read `status: new` while `status.md` reports all four done;
the one-writer protocol names a seat retired 2026-07-21, so **the protocol
gets the era marker**; reconcile against `status.md`, never silently rewrite
`inbox.md`. *The check before writing:* R2 (graduation) is **next, not
started** — the ledger says so and what graduation means for the remainder;
the keystore edge is in this repo's Layer-2 folder (fresh-keystore
recommendation recorded).
*Acceptance (audit's):* a cold session states product-forge is the seat-era
shell whose living product is phone-controller, its state, and that R2 is
next — and `control/` no longer misdirects.
*Verify:* `check --strict` (kit 1.7.0 — if the old gate misbehaves, the PR
checks decide). *Non-scope:* no R2 execution; no kit hop (skipped, § A).

**PKT-C3 · estate-backups · either.** *Inlined from § 7.3:* the 130-byte
README grows to what the two workflow headers already say — `dump.yml` = the
restore-verified pre-deletion archive of `postgres-botsite` (ran 2026-08-16;
the archive lives on the repo's Releases page, tag
`postgres-botsite-final-2026-08-16`), `sizing.yml` = read-only catalog sizing
(2026-08-20), both one-shot and both already run; the sealed-box one-shot
secret pattern that *is* the venue; the read-only posture under the
worker/Postgres hard rail; and the line that prevents a real mistake: **the
recurring bot backup is a `superbot` workflow, not this repo.** Plus
`.sessions/` **with a dated seed card in the same diff** — an empty
`.sessions/` reads as "exists but holds no card", which the derived lane
reports as invisible work — and the same convention README as PKT-C6's
(Status · Model · Venue · the ♻ line as self-declared, ungated convention).
*Acceptance:* a cold session knows what the venue is, that both workflows
already ran, and where the recurring backup actually lives.
*Verify:* none local (3 blobs, no CI) — the PR diff is the deliverable.

**PKT-C4 · websites · either — "more than a stamp".** Its
`docs/current-state.md` is stamped 2026-07-21 and still describes the
pre-cutover world (review live on Railway, scheduled bake, kit v1.20.1) — it
predates the whole keep-bot-only cutover. Rebuild the header + live-state
section from the cutover truth (the repo's own `docs/decisions.md` two
2026-08-20 entries + its `.sessions/` cards carry it): review is a **Pages
static export** with no Railway service behind it; three services remain in
`superbot-websites`; kit is v1.21.0 (or newer post-hop).
*Needs:* a Railway read for the live service-list check the audit § 7.4 asks
for — if the session holds no `$RAILWAY_API_KEY`, **write the service claim as
`per the fm audit dated 2026-08-23, not re-verified`** rather than asserting.
*Acceptance:* the repo's own ledger now agrees with its tree and the live
world about review. *Verify:* `check --strict` + the four pytest suites;
required check `quality`.

**PKT-C5 · superbot · either.** **Step 1 is the rating read** — the audit
deliberately left `superbot` unrated (PKT-C0 may have done this; if so,
inherit its verdict): open `docs/AGENT_ORIENTATION.md` → what it delegates to →
`docs/current-state.md`. **The minimal root `README.md` lands regardless of
the verdict** (`@codex` fm #951 — the no-root-README fact is measured and
independent of how the delegation path rates; the repo renders nothing at its
root today): what the repo is (FROZEN, behind the LIVE production bot), the
hard rail, pointing at `docs/AGENT_ORIENTATION.md` → `docs/current-state.md`.
**The rating decides the content depth**, not whether the pointer file exists —
a fail verdict means the README also has to carry the corrections the read
surfaced.
*Cautions inlined:* the **auto-merge enabler arms at PR open — disable or
label before requesting review**; docs-only pushes are rebuild-safe under the
watch filter (`['disbot/**', 'requirements*.txt', 'pyproject.toml',
'Procfile']`) — **re-verify the filter live before pushing**; the kit gate runs
honestly red at 2 — expected, not yours to fix.
*Acceptance:* the repo root renders an honest front door; the bot never
restarted (deploy list shows SKIPPED for the docs push).
*Verify:* required check `Code Quality`; `check --strict` red-at-2 is the
recorded pass state.

**PKT-C6 · spider-bot · either (writes: fresh clone → work → push → delete
the clone — the repo's own venue rule).** Card protocol without the kit:
create `.sessions/` with a convention README (dated `YYYY-MM-DD-slug.md`
cards · Status badge · Model line · **📍 Venue line** — the derived lane
parses exactly this, `MEASURED` against `tools/estate_activity.py` — · and
the **♻ Carried forward line as self-declared convention**, stated honestly
as ungated here: nothing in this repo checks it, per § 6's scoping) **plus a
dated seed card in the same diff** (an empty directory reads as invisible
work). **No CI or landing change** — making `quality` required converts the
repo to a PR flow, which its entry point records as owner-gated twice over.
*The deploy caution, inlined:* **push to main deploys straight to the
production bot** — one batched docs commit, then verify the new deployment's
`meta.commitHash` equals HEAD (`needs:` Railway access; without it, say so and
ask the owner to glance at the deploy — deploy SUCCESS alone proves nothing
about which code runs).
*Acceptance:* the next refresh shows spider-bot in the derived lane instead of
"no card protocol"; the bot is running HEAD.
*Verify:* `python -m pytest -q` (78 tests, informational) if Python exists;
otherwise the deploy check is the verification.

**PKT-C7 · creator-kit · either.** Fill the unrendered `docs/current-state.md`
template's **mechanical** slots only — what exists (FreeCAD parts library,
Godot workbench, Windows launchers, kit v1.21.0), the commands, the
`REASONED`-tagged provenance (built on the laptop) — and give `.sessions/` its
convention README + seed card. **Intent slots stay explicitly empty with a
pointer**: *"purpose/goals: the owner's intent conversation, not yet held"* —
writing them would manufacture intent (§ header).
*Acceptance:* the repo can answer "what is here and how do I run it" without
answering "why" beyond ESTATE's line. *Verify:* `check --strict`.

**PKT-C8 (×N) · one packet per kit repo, after that repo's hop.** Seed
`.session-journal.md` from that repo's **already-measured** traps — each
packet inlines its own 2–3 lines verbatim, e.g. websites: *GITHUB_TOKEN
merges fire no push-event workflows (Pages rebuild needs a dispatch)* + *the
exporter's exit 0 proves routes rendered, not link integrity*; superbot: *the
enabler arms at open* + *vendor-dist+bump-pin only*; spider-swing: *despill at
full resolution; key by corner sample* + *seamless-tiling is a false
constraint (mirrored tiles)*; couch-legend: *count tests with `pnpm test`,
never from prose* + *per-run CI signing certs before #14*. A repo with nothing
measured writes the honest null («no recurring traps recorded yet — add the
first one you hit»). Under the post-wave gate, each seeding card declares
`journal` and the delta is the seed itself.
*Acceptance:* the journal is no longer byte-identical to the template and every
line cites its incident. *Non-scope:* no invented traps; no style preferences.

*(`curious-research`: no packet — parked by the owner's own word; its AGENTS.md
row in PKT-B4 is the only touch, if he says yes.)*

### Wave D — the review surface (Move 3; after Wave B **and** the intent conversations begin)

> The merged plan's order is kept deliberately: **Move 1 → Move 2 → the intent
> conversations → Move 3.** The conversations are what the review surface
> reviews; building the board first renders a decaying picture beautifully
> (the plan's own § 9 warning).

**PKT-D1 · websites.** `/repos` + `/repos/{name}` rendering fleet-manager's
committed digests — including `measured_at` and the STALE marks, so aging is
visible on his board — behind the existing owner gate (`app/owner_login.py`).
**The page also reads `docs/owner-comments/<repo>/` live from the same fm tree
fetch** (`@codex` fm #951): a writeback is not a session, so nothing
regenerates the digest when a comment lands — deriving the "unconsumed
comments" row at render time is what keeps site → commit → visible true
without a regen dependency (B1's generator still lists them when it runs; the
page never waits for it).
Fetch trade, recommendation first: **server-side raw fetch with the Tier-1
read-only token** (`OQ-WEBSITES-PAT` — already open for exactly this
rate-limit class) · alternative: a committed sync copy in websites (second
copy to drift — rejected unless the token stalls).
*Verify:* the pytest suites + `quality`; acceptance: the page renders what the
fm tree holds; **a digest whose `measured_at` is older than 14 days renders
the STALE mark, computed at read time** (the committed page cannot flip its
own text — `@codex` fm #951 round 2); a comment file appears without any
digest regen and disappears from "unconsumed" when moved to `consumed/`.

**PKT-D2 · websites.** Retire or repoint `/fleet` and `/projects` — the
control plane still renders the terminated seat roster; two competing answers
to "what is the estate" on the owner's own board, one of them 2026-07-21.
`/repos` replaces them (the merged plan's surface-count constraint: every
addition replaces a seat-era surface).

**PKT-D3 · websites + fleet-manager.** The comment loop, **route before box**:
extend `writeback.py` with a fleet-manager target and a per-repo comment kind →
each comment is one commit under `docs/owner-comments/<repo>/` **in
fleet-manager** (§ 2 item 7) — **landed via a branch + gate-compatible PR,
never a direct Contents-API write to `main`** (`@codex` fm #951, verified this
session: the effective rules on fm `main` include a `pull_request` rule, and
the estate has already measured a direct write failing GH013 — so a
main-targeted writeback would 403 every comment at the door). The writeback
pushes to a rolling comments branch and opens/updates its PR; a comments-only
diff adds no session card, so the added-card lane passes and the required
check can green (the alternative — a narrowly scoped ruleset bypass for the
writeback actor — is recorded and not preferred: it weakens the one
protection). Delivery: D1 renders the comment records live (below) + the fm
prompt-route so a cloud session touching that repo gets the comment injected +
the hub's review-fm-first step for local sessions + the AGENTS.md pointer for
everything else. A comment is *consumed* by the session that acts on it moving
it into the repo's record (its card or the relevant doc) — mechanical, no
grading.
**Two mechanics the branch+PR design makes load-bearing (`@codex` fm #951
round 2):** (1) each writeback also appends a line to the stable per-repo
index `docs/owner-comments/<repo>/README.md` in the same commit — the prompt
router routes **literal files only** (`route_docs.py` filters entries through
`is_file()`), so an arbitrarily named new comment file is undiscoverable
without a stable routed path; the route targets the index, the index names
the files. (2) **consumption is a file move, not a description**: the acting
session moves the comment file to `docs/owner-comments/<repo>/consumed/` in
its own PR (move, never delete — the record survives), and every reader —
D1's render, B1's generator, the route index — excludes `consumed/`. Copying
the direction into a card without the move leaves the comment reading
unconsumed forever.
*Needs (owner lane):* a fine-grained PAT in Railway for the fm target with
**Contents R/W AND Pull requests R/W** — Contents alone writes the branch but
cannot open the gate-compatible PR (`@codex` fm #951 round 2; the estate's
existing writeback recipe already requires both) — today's deployed token is
`UNVERIFIED` and the docstring says read-scoped either way; the engine
already fails honestly on 403.
*Acceptance:* a test comment travels: site → comments PR merged → the `/repos`
page shows it on next render → a session consumes it by moving it to
`consumed/` → the page and the route stop presenting it. *Non-scope:* no
notification system; no second store — the commit is the record.

### The owner lane — batched, one sitting each

| # | ask | shape |
|---|---|---|
| OWN-1 | `AGENTS.md` estate-wide (`OQ-FM-AGENTS-BOOT`) | **ANSWERED 2026-08-28: yes** (*"Agents.md should indeed be everywhere"*) — PKT-B4's gate is open; its sequencing rule stands |
| OWN-2 | the hub centralisation route (`OQ-ONEDRIVE-HUB`) | **RESCOPED 2026-08-28 — no letter owed**: the sync need is met by the fm local section; residual = optional hub housekeeping ([owner direction](../findings/2026-08-28-owner-direction.md) § 7) |
| OWN-3 | two token mints, one sitting | Tier-1 read-only (readiness + D1) per `OQ-WEBSITES-PAT` · the writeback token for D3 with **Contents R/W AND Pull requests R/W** — Contents alone cannot open the gate-compatible PR |
| OWN-4 | `pokemon-mod-lab` hop | release the hold, or keep it — one word |
| OWN-5 | `shiftlife` hop pacing | now / later |
| OWN-6 | `gba-homebrew` landing route for hop + AGENTS.md | admin-merge red / demote the check / defer — one letter |
| OWN-7 | Python on the laptop | **only if** a local venue precheck finds none — one install, `python --version` |
| OWN-8 | the hub pages themselves (PKT-B3) | a **hub-local session** sitting, on his GO (clarified 2026-08-28: *"I want to do this in local sessions … they have the full ability to work on both sides"*) |
| — | **the per-repo intent conversations** | after Wave B, clustered (the bots · the games · the labs), digest-fed so his time goes to intent, not reconstruction — the expensive, valuable part; explicitly not packet work |

## 6 · Ordering, and the first sitting

```
A1 → A2 → (the wave ∥ B1) → B2 · B3 → C0 → C1…C8 (audit order) → the intent conversations → D1 → D2 → D3
```

Packets are independent unless their `needs` line says otherwise — the wave
rows, B4's rows and C1–C7 can interleave freely once their gates are met.
**The first sitting is PKT-C1** (declared exception to the linear order: zero
dependency, thirty minutes, subtractive, teaches the form). **The pair that
must not slip is A1/A2** — the § 9 test: once Move 1 lands and a repo takes
its hop, every future session **in that repo** adds to the record instead of
drawing from it. **Scoped to the upgraded adopters, deliberately** (`@codex`
fm #951): the no-kit repos — `spider-bot`, `estate-backups`, `creator-kit`'s
gate-less half, `curious-research` — get the ♻ convention only as a
self-declared line in their C-packet convention READMEs, ungated, and full
coverage there arrives with kit adoption, which stays owner-gated
(spider-bot's landing flow twice over). Saying "every repo" would be the
claim-beyond-the-mechanism this plan exists to end. When
choosing among optional per-repo rows, rank by **fresh traffic, measured in
that sitting** (`GET /repos/menno420/{repo}/pulls?state=closed` filtered on
`merged_at`, one single window) — never by a frozen table and never by
last-commit dates (both withdrawn under review before).

## 7 · Working this plan from a local session — tomorrow

The owner's local session boots in the hub and reviews fleet-manager first;
this doc is reachable from that route three ways (current-state → Work state ·
the program's NOW note · the planning index). To start a sitting, one line is
enough:

> *Read `docs/planning/2026-08-26-estate-execution-packets.md` § 5, then
> execute PKT-C1 (or the packet I name). fleet-manager is public — raw-fetch
> it if you are not booted in it. Run the § 4 venue precheck first.*

The venue precheck, paste-ready: `python --version` (or `py -3 --version`) ·
`gh auth status` · `git --version`. If Python is missing, say so (OWN-7) and
let the PR's required check be the gate — never merge on red. The owner-lane
letters (§ 5) are one batched reply whenever convenient; none blocks C1.

## 8 · Relationship to the program and the queue

- These packets **absorb** the intent audit's § 7 fix briefs and serve
  OD-20/OD-21 under OD-13 (methods and legibility before high-value product
  work). Completing a packet appends the program's §7 row only when it
  completes a lettered step; otherwise the card + the refresh are the record.
- **`OQ-FM-D2-TARGET` stays open.** Wave C runs the audit's measured order —
  the standing no-target default — and selects nothing on his behalf.
- The program's NOW pointer carries a one-line note naming this doc as the
  executable queue for legibility work; **OD-22** records the owner's
  2026-08-26 evening statements (his words only — every design here is
  `DERIVED` and lives in this file, not in the OD row).

## 9 · Honest nulls

- The estate-wide ideas-per-card ratio is still unmeasured (§ 2.1 of the
  merged plan measured fleet-manager only); Move 1's clean test — gate an
  artifact of comparable semantic weight and compare — is named and still not
  run.
- The venue token stays self-reported; nothing verifies it, and nothing can.
- The hub's layout, and therefore how a hub-local session reaches a repo
  checkout, is `UNVERIFIED` until PKT-B3 writes it down.
- Whether OneDrive sync and a git repository coexist without corruption is
  untested — since 2026-08-28 this matters only to the rescoped
  `OQ-ONEDRIVE-HUB` housekeeping question, not to any sync path; if the owner
  ever picks that route, one sitting settles it before committing.
- The iOS listing and the laptop/phone capability questions
  ([2026-08-22 owner direction](../findings/2026-08-22-owner-direction.md)
  §§ 3–4) remain unhomed by this plan — named so they are not read as absorbed.
