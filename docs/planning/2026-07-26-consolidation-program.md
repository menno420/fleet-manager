# The consolidation program — the working plan

> **Status:** `living-ledger` — **THE plan.** The owner works this program
> together with any future session, one step at a time. Update the step ledger
> and the NOW pointer as steps complete; nothing else about this file should
> churn. Supersedes [`2026-07-26-consolidation-plan-v2.md`](2026-07-26-consolidation-plan-v2.md)
> (kept as analysis); background: [`../fleet-account-2026-07-26.md`](../fleet-account-2026-07-26.md)
> (the full documentation-derived read-back, owner-reviewed 2026-07-26).

## 0 · The goal, in the owner's sentence

> "Create a plan from which I can work together with any future session to
> consolidate the repos in a structured way, one step at a time."

And the quality bar, also his: **make all the repos feel right** — a fresh
session orients correctly and fast (this program exists partly because one
session needed three tries), the documentation tells the truth, the websites
reflect reality, and CI is a few checks that mean something.

## 1 · Owner directives (standing — do not re-ask these)

Recorded from the owner live in the hub chat; each is a durable decision.

| # | Date | Directive |
|---|---|---|
| OD-1 | 07-26 | `superbot-next` is the bot's future; **live testing gates the cutover**. Old `superbot` is already frozen as the behavioral oracle (recorded 2026-07-17). |
| OD-2 | 07-26 | `venture-lab` stays a live repo. |
| OD-3 | 07-26 | **Archive, never delete.** Nothing is deleted under this program. **AMENDED 2026-08-09 (owner, intent interview):** cleanup is now allowed and wanted. *"Stale docs, and eventually repos, could be deleted if they do not have any value. The goal is not a perfect archive, but rather an efficient workflow. Any doc or repo that has served its purpose and could not be of value anymore will only be noise and it's probably better to clean them up every once in a while."* The bar moves from **never** to **has it served its purpose and can it still be of value** — a judgement, so it is decided-and-flagged per repo/doc, not swept. Archive remains the default for anything still arguably useful; deletion needs a stated reason. |
| OD-4 | 07-26 | **`idea-engine` + `sim-lab` remain active** — standing assets for future projects (566 idea files; the 4-gate verification method). |
| OD-5 | 07-26 | **The claude.ai Projects are terminated (since 07-21).** May return ~August for general use — not a fact. Everything runs in **regular sessions**, possibly indefinitely. No return to EAP-scale parallelism — that scale existed to produce vendor feedback. |
| OD-6 | 07-26 | ~~**Pace: slow.**~~ **RESTATED 2026-08-09 (owner, intent interview) — "slow" was the wrong word for it.** *"That does not mean we should ever rush things, though it does also not mean we can't make progress. What I meant by it is that we should just focus on one thing at a time and do it properly from start to finish."* So the directive is **one thing at a time, finished properly** — not deliberate slowness, and not a reason to stop short of a finished job. Nothing needs profit now; incremental testing and reviews stand. |
| OD-7 | 07-26 | **Priorities: documentation first, websites second.** |
| OD-8 | 07-26 | **Websites:** execute the cutover — the new `websites`-repo services replace the old `superbot`-repo sites **under the old names**; then rework the sites that don't serve their purpose, one at a time. (The cutover plan exists and is prerequisite-cleared: websites `docs/plans/site-consolidation-cutover.md`.) |
| OD-9 | 07-26 | **CI: consolidate to a few checks — ideally ONE required check per repo** wherever possible. |
| OD-10 | 07-26 | **Ideas Lab is ON-DEMAND.** No standing loop. If work runs dry, use `idea-engine` to source the next feature; when building a new feature or improving an existing one, **run it through a dedicated `sim-lab` simulation** (the 4-gate method) before/while building. |
| OD-11 | 07-26 | **Venture: let it sit.** The live $29 listing stays as-is (owner: "I don't think anyone would ever buy it" — no kill-clock action, no delist, no publish wave). The owner will work the sellable-products angle himself, at his own pace, later. |
| OD-12 | 07-26 | **proxybench: no action required.** Origin recorded: built with a session mostly as a joke, in response to a cold sales email from a proxy vendor about venture-lab — it is the honest benchmarking harness for exactly that vendor's claims (success rate / geo / stickiness). Stays parked as-is; disposition is open and unimportant. |
| OD-13 | **08-09** | **Method and enforcement work comes before high-value product work.** Owner, intent interview: *"Before we can reliably focus on product work, we should make sure to further improve the methods and the rule enforcement. Product work is not explicitly blocked, but my advice is to first improve the workflow and further define the right mix of AI agents across different providers before we actually continue high value product work."* Two prerequisites, both named by him: **the methods/enforcement layer** (the roadmap's Phases 2–3) and **the multi-provider agent mix** ([`../intent.md`](../intent.md) § 7). Product work is not forbidden — it is deprioritised against these until they are further along. This is the standing answer to *"what should a session pick up"*. |
| OD-14 | **08-09** | **fleet-manager's intent is recorded, and it is the thing plans are checked against.** [`../intent.md`](../intent.md) — purpose, success criteria, non-goals, decision heuristics, the agent roster, and the growth rule (**records may grow, instructions may not**). Owner-stated content is labelled `OWNER` and is not revisable by a session; anything labelled `DERIVED` is. |

## 2 · Target picture — 7 sections

| Section | Repos | End state |
|---|---|---|
| ShiftLife | `shiftlife` | The consumer app. Healthy — untouched by this program. |
| SuperBot | `superbot-next` absorbing games · idle · mineverse · plugin-hello (+ botsite/dashboard code); old `superbot` archived **only after** the owner-paced cutover | One bot, one repo. |
| Phone Controller | `phone-controller` (graduated from product-forge) | Own repo, own APK releases. |
| Game Lab | `gba-homebrew` + `pokemon-mod-lab` | Two repos forever (copyright rail), one section. |
| Venture | `venture-lab` | Live; owner-paced publishing. |
| Ideas Lab | `idea-engine` + `sim-lab` | **Active, on-demand** (OD-4/OD-10); conformance + truth pass only, no fold. |
| Workshop | `substrate-kit` + `fleet-manager` + `websites` | The kit, the records, the owner's visible surfaces. |
| *(archive)* | codetool ×3 (opus4.8 stays unarchived — live mdverify URLs) · product-forge remainder · trading-strategy · old superbot (post-cutover) · `curious-research` stays as-is (owner's parked gift) · `proxybench` parked as-is (OD-12) | Read-only, zero attention cost. |

## 3 · The step ledger

**Rules of the ledger:** steps are small (one session each), sequential within
a track, and only ONE step is NOW at a time — the owner (or the session, if he
hasn't said) picks the next NOW from the top of any track. **Verify before
fold** — no repo is merged or archived before its conformance/truth pass. Every
completed step appends a row to §7 with its PR.

### ➡ NOW: **E1 — the final EAP email** *(owner-priority, ~2026-07-27: "probably
the most important thing we can do separate from our own repo work." Plan +
source map + seeded candidate list:
[`2026-07-26-final-eap-email-plan.md`](2026-07-26-final-eap-email-plan.md).
Then next: D2, fleet-manager truth pass.)*

> **Before acting on this pointer, read
> [`../findings/2026-08-05-foundation-continuation.md`](../findings/2026-08-05-foundation-continuation.md)** —
> it revises the order of work (foundation before rebuild) and carries the
> certainty legend that governs every dated claim in this repo, including the
> ones on this page. The boot file has said so since 2026-08-06; this page did
> not, so a session arriving here by grep, route or handoff never learned it.

> **E1 is OWNER-RESERVED and deliberately deferred — status 2026-08-01, from the
> owner live.** It is not stalled and it is not available to pick up. He has the
> prework and a plan for how he wants to write it, and has declined a drafted
> version twice: *"this is something that deserves an evening of my full
> attention and I won't rush it. I will probably finish it within the next few
> days."* A session must NOT draft, send, or restart this step. If you are
> looking for work, take **D2** (fleet-manager truth pass) instead.
>
> Why he has deferred it: every evening since 07-26 has gone to **spider-swing**
> — a repo created 2026-07-28 that is not in the fleet account, and the only
> asset in the estate with a live external signal (returning players, unprompted
> difficulty feedback). Deferring E1 for it is triage, not neglect.

### Track E — one-off, owner-paced

| Step | What | Done when |
|---|---|---|
| **E1** | Help the owner write and send the **final EAP review email**: fresh thread, short, Part 1 owner voice / Part 2 Claude, the numbered wish list + the good parts. Method + sources: the plan doc above. | The owner has sent it from a fresh compose; §7 row added; the unsent 07-18 draft + email-pack get a superseded note. |

### Track D — Documentation *(priority 1, OD-7)*

| Step | What | Done when |
|---|---|---|
| **D1** | Refresh `.claude/CLAUDE.md` (hub boot file) to the post-program era: sessions-not-seats, this program as the entry point, live-vs-historical map. | A fresh session orients from the boot file alone, without the 3-try failure. **← this PR** |
| **D2** | **The truth pass, one repo per session** — for each active repo: boot docs say what it is NOW; seat-era docs get an `historical` era-banner (never rewritten); its closeout + current-state are linked from the front door. Order: `fleet-manager` → `shiftlife` → `superbot-next` → `websites` → `substrate-kit` → `idea-engine`/`sim-lab` → `venture-lab` → game repos → the archive-bound. | Per repo: the fresh-session test passes (a cold session states the repo's purpose, live state, and next step correctly from ≤3 files). |
| **D3** | Fill the empty journal guidebooks with the real recurring traps (fm's `.session-journal.md` is placeholder headings today). Seed list: exit-code-read-through-a-pipe; proxied-vs-direct GitHub paths; born-red flow; MCP PR-read staleness; badge vocabulary. | Guidebook sections non-empty in fm + each active repo, each trap citing its incident. |
| **D4** | ~~Retire the dead apparatus *records*~~ **— roster half DONE 2026-08-07.** The owner ruled *"retire the roster, I don't need it"*; both `roster-regen.yml` crons and `roster-freshness.yml`'s `pull_request` trigger are gone (`workflow_dispatch` kept, OD-3), `docs/roster.md` is era-bannered `historical`, PR #808 closed. **Still open:** the trigger-registry and prompt-registry docs, and the three generated `projects/curious-research/` prompt copies that its 2026-08-07 handover flagged. | Roster no longer regenerates against a seatless fleet ✅; the remaining seat-era docs say so at the top. |

### Track W — Websites *(priority 2, OD-8)*

| Step | What | Done when |
|---|---|---|
| **W1** | Execute the cutover, **review-site first** (lowest risk), per websites `docs/plans/site-consolidation-cutover.md`: repoint references → reclaim old names → retire the three `reliable-grace` surfaces (`review-…-f027`, `superbot-app`, `superbot-dashboard`). **HARD RAIL: never touch the `worker` service (the LIVE Discord bot) or the two Postgres DBs in that project.** The old "keep reliable-grace URLs reachable for the vendor reference" constraint has lapsed (correspondence concluded 07-21; verified 07-26). | One estate; old names serve the new sites; bot + DBs untouched. |
| **W2** | Per-site purpose review, one site at a time (control-plane → botsite → dashboard → review): does each page show what it is, what it does, its most important features (the owner's clarity bar)? Rework what fails it. | Owner signs off per site. |
| **W3** | Make this program visible: a control-plane page that renders §7 progress + the NOW pointer, so the owner reviews by looking, not asking. | The page exists and is current. |

### Track R — Repos *(verification-led, slow)*

| Step | What | Done when |
|---|---|---|
| **R1** | Generalize shiftlife's `plan-conformance.md` into the conformance template (claims vs code; module + test per row; wrong row > tidy table). | Template in this repo; applied first to `superbot-games` (known drift: claims plugin-shipping, has no packaging). |
| **R2** | Graduate `phone-controller` to its own repo (subtree split, history + release workflow + signing secret carried; pointer left behind). | Clean clone builds a signed APK; CI green; product-forge remainder ready for archive queue. |
| **R3** | Releases-before-archive: tag + Release `cfgdiff` v0.1.1 and `envdrift` v0.1.0/v0.2.0 (archiving freezes tag-push forever — this is the one time-ordered step). | Both released; their repos join the archive queue. |
| **R4** | Bot consolidation, one sub-step per session, each behind a conformance pass: idle+plugin-hello → `plugins/` (real move, already pinned); games → plugins **after** its adapters are actually built; mineverse → `web/` keeping its fail-closed rails as CI; botsite/dashboard code per W-track outcome. | superbot-next boots with plugins loaded; 533-golden parity stays green. |
| **R5** | Archive the emptied/parked repos per OD-3, one at a time, each verified migrated first. | Active repo list ≈ the §2 table. |
| **R6** | Ideas-Lab truth pass (active, no fold): make the two-era reality legible from the front door (fleet-ideation corpus vs the math-verification loop); surface the 566-file idea corpus so the owner can actually browse it. | Owner can find and read the idea corpus without archaeology. |
| **R7** | SuperBot cutover ladder, owner-paced (the ladder already exists in the record): live-test prep → test guild → wallet-race concurrency tests → 1 live drive → 7-day shadow → cutover → rename → archive old superbot. | The bot runs on superbot-next in production. |

### Track C — CI *(OD-9; mostly falls out of R)*

| Step | What | Done when |
|---|---|---|
| **C1** | The model: **one required check per repo** — the `websites` pattern (everything runs inside `bootstrap.py`/one workflow behind a single required context). Apply to each active repo as its D2/R step touches it; never retrofit archive-bound repos. | Each active repo: 1 required check (2 max where an artifact build is genuinely separate). |
| **C2** | Delete the agent merge-plumbing class where sessions are attended (keep `merge-on-green`/enabler only where it still lands PRs — note: private repos can't use GitHub's native auto-merge on this plan, so shiftlife keeps its enabler). | No workflow exists whose only job was serving the terminated seats. |
| **C3** | Confirm the pre-close standing failsafe crons are actually disabled (page the trigger registry to exhaustion; wipe survivors — the 07-21 snapshot showed 10 standing crons enabled; unverified since). | Registry shows zero seat-era crons enabled. |

## 4 · How any session works this program

1. **Boot:** hard-sync main → read `.claude/CLAUDE.md` → this file → the NOW step.
2. **One step per session** unless the owner directs otherwise. Small PRs, kit
   discipline (born-red card, `check --strict` green, real exit codes — never
   `$?` after a pipe).
3. **Verify-first:** the live surface beats any doc; each fold is preceded by
   its conformance pass.
4. **Initiative + the flag rule (owner-stated):** take initiative in organizing
   and planning; **flag to the owner only the genuinely ambiguous forks** you
   cannot resolve from the record — add them to §6, don't block on them.
5. **Close:** update §7 + move the NOW pointer + session card. Leave the truth
   accurate.

## 5 · What this program is NOT

No deadlines. No revenue pressure. No deletions (OD-3). No seat revival, no
mass parallelism (OD-5). No merging of the two GBA repos (copyright rail). No
production-bot changes outside R7's owner-paced ladder.

## 6 · Open forks for the owner (non-blocking — answer whenever)

*All three founding forks were answered 2026-07-26 and promoted to OD-10 /
OD-11 / OD-12 above. Sessions: add new genuinely-ambiguous forks here — one
line each, never blocking.*

*(none open)*

## 7 · Progress ledger (append-only)

| Date | Step | What landed | PR |
|---|---|---|---|
| 2026-07-26 | — | Program created; fleet account (read-back) reviewed by owner; OD-1..OD-9 recorded | fm #540/#541/#543/#545 + this |
| 2026-07-26 | D1 | Hub boot file refreshed to the post-program era | fm #547 |
| 2026-07-26 | — | §6 forks answered by owner → OD-10/11/12 recorded; Gmail layer read on owner direction (EAP thread · vendor thread), proxybench origin recorded | fm #548 |
| 2026-07-26 | — | **E1 planned + set as NOW** (owner: final EAP email is tomorrow's priority): plan, source map, seeded candidate list · verified the 07-18 follow-up draft was never sent (its findings are unused material) | fm #545 |
| 2026-08-05 | — | *(ledger gap noted, not reconstructed)* Eleven substantive PRs landed 08-01→08-05 outside the program tracks — the Vertex-first directive, two Gemini benchmarks, the Play submission requirements, the superbot-next live audit and the navigation-graph correction. They are spider-swing / bot-rebuild work, not program steps, so they get this one summary row rather than back-filled step rows. **NOW is unchanged: E1 stays owner-reserved; D2 is the available step.** | fm #742–#760 |
| 2026-08-05 | — | Three-repo state audit (fleet-manager · superbot · superbot-next) as the foundation for the server-first rebuild: superbot's reachability guard found and **run green at HEAD** (0 GAP), the "help renders transcribed text" reading overturned, four record claims corrected, `tools/gemini_delegate.py` given a Vertex path so delegated reads spend credit not card | fm #761/#763 |
| 2026-08-05 | **D2 (partial — fleet-manager)** | Hub read path repaired. It omitted `current-state.md` and `owner-reflection-2026-07-21.md` — the doc `current-state.md` introduces as *"read this if you read nothing else"* — so a session following the boot file exactly never met it. The path now opens with those two, adds `PROJECT-CLOSEOUT.md` §3, and declares itself **a floor, not a ceiling**. Root cause traced past the boot file to the `continuation-prompt` skill, which templated `READ FIRST` as *"the minimum to act"* with no exception for a comprehension mandate; skill gains §4b. **This was the D2 fresh-session bar failing on the hub's own front door.** The rest of D2 — every other repo — is untouched and still open. | this PR |
| 2026-08-06 | **D2 (partial — substrate-kit) + foundation** | Kit checker classification and a second boot-path repair. **Measured:** `check --strict` output was 87% (kit) / 90% (fm) non-exit-affecting advisory, both trees exiting 0, and every tag that fired was an ager or a false positive (13 stale-wall rows titled `'any'`; nine skill-grounds rows naming `READ FIRST` and a numpy expression as "commands"). All 29 advisory sites are now classified deterministic/heuristic in `guards.ADVISORY_CENSUS`, pinned by a parity meta-test, with the heuristic tail routed off the agent's channel (`--advisories` to read it, `--gate-preview` to size the promotion). Output 47→7 and 89→10 lines, exit codes unchanged. **substrate-kit had no working boot read path at all** — its router's step 1 named a `.claude/CLAUDE.md` the kit by design never installs, a dead pointer already fixed in the template on 07-12 and never re-rendered into the kit's own copy (recorded in the kit's own decisions ledger). fleet-manager's path omitted the foundation-continuation doc; added. **Deliberately not done:** promoting the deterministic checkers to exit-affecting — two trees is not evidence for ~22 adopters; `--gate-preview` makes that a sweep. | fm #789 · kit #577 |
| 2026-08-07 | **D4 (partial — roster) + curious-research handover** | **The owner retired the roster** (*"Yes retire the roster, I don't need it"*), and it needed retiring for a second reason nobody had noticed: the regen had **deadlocked** since 2026-08-06T08:02Z. It opened its PR with `github.token`, GitHub suppresses workflow runs for that actor, `substrate-gate` never reported, and `main` requires it — **18 consecutive failed runs**, PR #808 permanently unmergeable, a red `freshness` on every `claude/*` PR. The workflow's own header knew the token behaviour and compensated by parking the PR for *"the next manager wake"*; that wake was the fleet, which closed 07-21. Crons removed, `workflow_dispatch` kept (OD-3), `docs/roster.md` bannered `historical` with its purpose preserved, PR #808 closed, `OQ-FM-APPARATUS-SIZING` resolved, `OQ-FM-ROSTER-READ-PAT` mooted. **Same root cause, second repo:** `curious-research`'s site silently stopped publishing for exactly this reason — auto-merge landing PRs as `GITHUB_TOKEN` so `pages` never fired. Fixed there **without a new credential** (owner declined one): merges attributed to a real user are not suppressed, so the enabler now refuses to arm PRs touching `site/`/`guides/`. Also: boot-source finding (booting on a satellite repo loads 1 skill instead of 27, silently), three corrected ledger claims, `OQ-CR-SLICER-ANSWER` closed after 23 days, 11 research dossiers landed + made discoverable, 3 guides translated to Dutch, the `lasersnijden` tab filled, and an external-review prompt built on the measured "unframed reviewers endorse anything" finding. | fm #810/#811 + this · cr #67–#75 |
| 2026-08-08 | — *(index restructure, not a lettered step)* | **Layer 2 exists, one folder deep.** `docs/repos/spider-swing/` built as the reference shape — README (standalone entry + four thread blocks) · `capabilities.md` · `records.md` · `working-here.md`, with `current-state.md` and `goals.md` **deferred and the reasons recorded** rather than silently omitted. Deliberately stopped at one folder: the first instance of a repeated shape is the only cheap place to be wrong, and the owner has not yet seen it. Both owner-stated acceptance tests written down and run — test 1 PASS 14/14 from the folder alone with the repo unattached; test 2 PARTIAL, correct on the one folder that exists and honest about the 23 that do not. Retrieval closed the gap that lets Layer 1 stay light: `route_docs.py` now also runs on `UserPromptSubmit`, payload key **verified from the shipped binary** (top-level `prompt`, not `tool_input`) rather than assumed, opt-in per route so the 21 existing probe routes keep their blast radius; `install_root_hooks.py` registers both events, so the case-three rescue path no longer installs half the mechanism. Two Layer-1 gaps closed: a **27-skill roster** (`rationalize` and `scope-backlog-item` were in *no* index; `chase-references`/`prep-owner-steps` were indexed as living in superbot and are installed here), and `@codex` added to the boot file — 0 occurrences before, despite being a measured, load-bearing review path. This is D2-adjacent (per-repo truth, fresh-session test) but is not filed as D2: D2 is a truth pass over a repo's *own* docs, and nothing in spider-swing was touched. **NOW is unchanged: E1 stays owner-reserved.** | fm #818 |
| 2026-08-08 | — *(instruments, cont.)* | **The owner's root-cause ask, answered and mechanised.** After #818's shape work, the day's follow-ups (#819–#822 + this) revived the owner-review hook (it had never fired — google-auth absent, every skip now logged, free-key-first routing), built `read_before_write` (unread-file descriptions + closed vocabularies), planted `scripts/preflight.py` (ORDER-018 parity — CI's added-card lane now reds locally), and added `git_state_guard` (squash-stack, force-push tree check, dirty reset). The finding that organises it: [2026-08-08-why-rules-dont-bind.md](../findings/2026-08-08-why-rules-dont-bind.md) — 17 incidents, catchers owner 5 / hook 4 / gate 1 / CI 2 / self 2 / after-the-fact 2 / **docs 0**, so rules move from recall to injection. NOW unchanged: E1 owner-reserved; Layer 2 replication awaits owner sign-off on the spider-swing shape. | fm #819–#823 |
| 2026-08-08 | — *(correction to the row above)* | **"17 incidents" is wrong; the number is 16** — and the row's own catcher list proves it (5+4+1+2+2+2 = 16). The finding corrected itself the same day and this ledger did not follow, so the stale headline outlived it on a read-path page. Kept as a correction row rather than an edit, because §7 is append-only and a silently-fixed number teaches nothing: the defect class is a **gloss composed over a correct table instead of computed from it**, which is the same failure the finding catalogues as its own incident #24. | this PR |
| 2026-08-08 | — *(D2, partial — the orientation layer)* | **Retrieval and orientation repaired so the corpus can be retrieved from.** Boot file corrected at net-zero words (stale route count and roster clause; one-command verify truth; the Stop-hook answer protocol; a canonical-for line for the decision records; era flags on the floor list). `session-close` gained the Layer 2 handoff step that [`2026-08-08-fleet-manager-as-index.md`](2026-08-08-fleet-manager-as-index.md) § Maintenance decided and the skill never carried, plus the §7/NOW step and a live-venue rewrite. One prompt route added under a stated admission bar, replayed against 12 real owner utterances (0 false fires). Seat-era routers (`NEXT-TASKS`, `RESUME`, `reading-path`, `PROJECT-CLOSEOUT` §5, `AGENT_ORIENTATION`, `MISSION`) now say which era they describe. This is **D2's method applied to fleet-manager's own front door** — era-banner the seat-era, point the live surfaces at what is true now — so it is filed as partial D2. **NOW unchanged: E1 owner-reserved.** | this PR |
| 2026-08-09 | — *(intent layer, Phase 2 opened)* | **The owner's intent asked, recorded, and two standing directives changed by his answers.** A 21-question intent batch, all answered, landed as [`../intent.md`](../intent.md) — the first instance of the roadmap's § 4.6 invariant (one discoverable canonical intent source per active repo). Purpose, success criteria, non-goals, decision heuristics, and the **agent roster** (Claude everything + credentials · ChatGPT *Work* doing real implementation in spider-swing · Gemini/Grok review and planning · Codex PR review) — none of which any record here carried. **The measured result: none of the 21 questions was already answered by the corpus** — twelve OD rows, two `[D-NNNN]` entries and a PL register all record *what was decided* and nothing recorded what the repo is *for*. **Two answers amended directives rather than adding to them** — OD-3 (cleanup of spent docs and repos now wanted, per item, with a reason) and OD-6 (*"slow"* → **one thing at a time, finished properly**) — so the interview's output is not additive-only, and Phase 2's procedure now names a reconciliation step (roadmap § 4.8). New **OD-13** (methods + provider mix precede high-value product work — the standing answer to *"what should a session pick up"*) and **OD-14** (intent is what a plan is checked against). Also corrected: *"his attention is the scarcest resource"* implied minimising asks; he wants **ask immediately, keep working, stop only when genuinely blocked**. **NOW is unchanged: E1 stays owner-reserved.** | fm #827 |
