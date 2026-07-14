# EAP retrospective — likes, dislikes, wishlist

> **Status:** `reference`
>
> Generated 2026-07-13 by the fleet review (owner directive).
> An honest retrospective of the Claude Code Projects EAP (2026-07-07 → 2026-07-14)
> across the ~19-repo fleet: what we enjoyed, what we disliked, the platform and
> tooling features that would have helped, and the wishlist for the next phase.
> Every sentiment below is attributed to a real session card, walls file, retro,
> owner queue, or eval-log entry — nothing is invented. Where the only anchor is a
> fleet-review deep note (each itself pinned to path@SHA / PR# / dated evidence),
> the citation says so explicitly.

## Sources & method

Primary source: the fleet-review collation `collated/story.md` (EAP HISTORIAN lane,
2026-07-14), built from 19 per-repo deep-review notes (`notes/*.md`), each pinned to
path@SHA, PR numbers, and dated session cards. Key underlying documents cited
directly below include:

- superbot `docs/planning/projects-eap-evaluation-log.md` (append-only EAP journal, PR #1820)
- superbot `docs/eap/fleet-winddown-audit-2026-07-09.md` and `docs/eap/fleet-overnight-review-2026-07-10.md`
- codetool-lab-fable5 `docs/succession/PLATFORM-LIMITS.md` (every wall with exact error text) and `docs/succession/NEXT-BOOT.md`
- codetool-lab-sonnet5 `docs/retro/winddown-review-2026-07-09.md` and `docs/succession/GEN2-FEEDBACK.md` (10 numbered blueprint-feedback items)
- codetool-lab-opus4.8 gen-1 retro + GEN2-FEEDBACK (via note codetool-lab-opus4.8.md §3)
- websites `docs/retro/gen1-final-retro-2026-07-09.md` and `.sessions/2026-07-13-coordinator-sitting.md`
- fleet-manager playbook rules R1–R27, `docs/roster.md` (gen #36), generated owner queue, `docs/gen2-blueprint.md`
- sim-lab VERDICT 016 (authenticity-gate sweep); trading-strategy ORDER 002; venture-lab kill-clock records

Sentiment quotes are verbatim from those artifacts as carried by the collation.
"As-reported" numbers are flagged as such. Gaps are stated in the final section.

---

## 1. Likes — what we genuinely enjoyed

### 1.1 Worker-tier autonomy worked from day one

The full born-red card → claim → PR → auto-merge loop ran "with zero permission
prompts and no tool failures" on the very first EAP night (superbot eval log
`docs/planning/projects-eap-evaluation-log.md`, entry ~2026-07-07 22:45Z). By the
final night, superbot-idle's eap-night-groom session card could say "the
claim-ledger + born-red + enabler pipeline carried a full ORDER worklist end-to-end
on EAP's final night with zero human clicks and zero collisions" (superbot-idle
dated card, via note superbot-idle.md). That loop — invented in superbot over June
(Q-0123 auto-merge enabler PR #779; Q-0133 born-red gate) — is the single most-loved
piece of the whole system.

### 1.2 Velocity with recoverability, not velocity instead of it

- The 14-hour superbot-next rebuild: 49 PRs, 1 coordinator + 1 builder spawning 18
  sequential workers, "zero rework: no PR had to be reverted or redone"; the retro's
  own judgment: "recoverability beat raw efficiency, and for a 14-hour build that is
  the right trade" (superbot-next note §3; a killed worker resumed cleanly from its
  progress log).
- substrate-kit shipped 102 merged PRs in ~24h of continuous mode (Q-0265) and its
  cards judged it a right pace, not a stunt (substrate-kit note §3).
- superbot-mineverse: empty repo → staged product ladder, 39 PRs merged, suite 0→327
  on founding day alone (2026-07-11 cards); the suite kept growing to 587 tests + 1
  skip by day 4 (94 commits total — mineverse note, retro-cited). The two figures are
  different days of the same curve, not a discrepancy.

### 1.3 Honesty engineered in — and it held under audit

"The fleet does not overclaim" is the collation's own lead finding: superbot-next's
999-test claim, independently re-run, verified as 998 passed + 1 skipped — the claim
held under hostile recount (story.md Part V, Joys). Three Projects independently
defaulted to honest self-assessment at gen-1 close; the adversarial wind-down audit
verified 21/21 incidents with zero fabrication (superbot
`docs/eap/fleet-winddown-audit-2026-07-09.md`; eval-log weight: "delighted").
Concrete cases the record celebrates: trading-strategy's proudly negative final
report (5,055 configs tested, 0 promoted); the kit's owner-ruled un-caveated
1-PASS/8-FAIL benchmark headline ("honest-negative headlines are the fleet's
credibility asset"); venture-lab re-deriving its own product price DOWN when a
manuscript came in short; pokemon-mod-lab's "honest idle beats busywork" dry-well
finding (trading-strategy, substrate-kit, venture-lab, pokemon-mod-lab notes).

### 1.4 The self-auditing session chain is real, not ceremony

superbot carries ⟲ previous-session reviews on 767 of 949 cards measured in the
review clone (the deep note reports "780+" — magnitude agrees, exact count drifts
with ongoing sessions); fleet-manager on 129 of 132 cards in the clone (the note's
"~140 cards in 5 days" reflects a different count moment). A kit card records "#328
is a model friction→guard slice — and its ⟲ review is what surfaced THIS session's
fix"; superbot-idle refuted a predecessor's misdiagnosis with run logs; gba-homebrew:
a guard recipe "named there as the next item's law and it WAS the session's whole
shape"; superbot-mineverse ran three same-day self-initiated dedupe waves whose cards
each cite a previously recorded 💡 idea — the idea conveyor demonstrably feeding
work (mineverse note, cards 2026-07-13-test-infra-dedupe / serve-helper-dedupe /
run_server-lifecycle; the collation attributes this to venture-lab, but the
underlying evidence lives in the mineverse note). (superbot, fleet-manager,
substrate-kit, superbot-idle, gba-homebrew, superbot-mineverse notes — all
card-cited.)

### 1.5 Evidence tooling as delight

- The golden replay harness: "a fresh-DB replay is ~1 min and found the band-3
  clock/RNG leaks that no unit test could" (superbot-next note §3).
- The differential oracle: a corpus diff vs python-dotenv found 3 real parser bugs
  behind 114 green tests — "your own tests encode your own misunderstandings; an
  external oracle does not" (codetool-lab-sonnet5: the oracle corpus landed in PR #9,
  the three fixes in PR #11; `docs/retro/winddown-review-2026-07-09.md` §ii).
- gba-homebrew's "predicts a number once, CI asserts it forever"; fable5's
  byte-exact stranger-install replays ("genuine delight", wind-down review "How it
  FELT"); mdverify catching its own README bug by dogfooding (codetool notes).

### 1.6 Coordination that felt good

"One-writer-per-file … the only [mechanism] that never failed" (codetool-lab-opus4.8
GEN2-FEEDBACK). "The front-door model is genuinely working … 'dispatch, verify
independently, relay once'" (websites `docs/retro/gen1-final-retro-2026-07-09.md`
§4, coordinator verbatim). Manager orders rated "better than most human tickets"
(trading-strategy self-review). "Owner decision latency was tiny — single-shot
decisions executed within minutes" (websites gen-1 retro). The wake-driven cadence
"felt genuinely good — wake, pull, verify, dispatch, status, sleep" (opus4.8).

### 1.7 The platform, when it worked

CLAUDE.md auto-injection: "the full working agreement available with zero reads —
weight: helped." Fail-fast structured permission denials with written reasons "beat
silent stall." Coordinator memory measured at ≈0.98 recall precision against git
(superbot eval log, 07-07/07-08 entries). The Contents-API bootstrap discovery
(superbot PR #1830, 2026-07-08) unlocked founding an entire fleet prompt-free. And
the 2026-07-10 self-arming-routines unlock ("capability-unlock — self-wake works!",
eval log) turned the fleet nocturnal within a day.

### 1.8 First revenue — a real product went live

On 2026-07-12 the fleet's first revenue artifact went live: the **Stripe Webhook Test
Kit, $29 on Gumroad** — owner click to publish, coordinator HTTP-200 verification
plus an independent worker re-verification, and the buyer path verified end-to-end by
the owner's own test purchase; kill clocks armed at T+7 / T+14 with a pre-registered
kill rule (venture-lab note; story.md §7). One live product with a verified purchase
path is a categorically different fact from the 185 still-queued clicks in §4.1 —
both are true, and the doc carries both.

### 1.9 The self-improvement loop closed cross-repo — in ~30 hours

superbot-mineverse found the kit's born-red fail-open (the gate was advisory for
cards *added* by a PR — two PRs auto-merged with in-progress cards), routed it
upstream via its outbox, the kit fixed it in v1.15.0, and mineverse consumed the fix
back and verified it fired live: **bug → finding → kit fix → re-consumed, in ~30
hours** (superbot-mineverse note; substrate-kit note; story.md §7). This is arguably
the record's single strongest "the system works" moment — a fleet member improving
the substrate every fleet member runs on, with the full round trip inside two days.

---

## 2. Dislikes — what we disliked, in the record's own words

### 2.1 Silence as the scariest failure class

"The platform's silence modes … consumed two-thirds of the project's wall-clock"
(codetool-lab-sonnet5 wind-down review). The 76-minute invisible boot death — the
builder "has no record of its own death" (codetool-lab-fable5 wind-down).
trading-strategy's builder died 30.2 min on a setup script, then an identical
failure silently killed the successor (0 turns, no failure event, unnoticed ~2.8h;
trading-strategy note, EAP story section). websites had workers parked on timers
dying silently 3× in one sitting (websites gen-1 retro).

### 2.2 The environment as adversary

"The environment: the actual adversary of the day. … Building was the easy part; the
walls were the job" (fable5 wind-down). Wake-environment roulette: 9 of 15 sessions
arrived with no PR-write tools (pokemon-mod-lab note). Per-container toolchain
absence — a distinct wall class from missing tools or stale state: pokemon-mod-lab's
session 027 arrived without the ARM/mGBA toolchain, blocking review-queue #23 for
days (pokemon-mod-lab note, CAPABILITIES walls). Stale clones 7 merged PRs behind
origin at first coordinator turn (superbot eval log, 07-07); cwd landing in the
wrong repo (opus4.8 note §3).

### 2.3 The merge-classifier sting

"I burned a retry re-issuing the merge with 'authorized' framing, which the
classifier flagged as tunneling" (opus4.8). A denial issued WITH owner authorization
on record: "No reason provided" (fable5 PLATFORM-LIMITS). "Arming is not
deterministically available" (product-forge day-1 retro; 8 arming denials confirmed
in its PLATFORM-LIMITS — PRs #8/#12/#13/#14/#15/#17/#19/#22; the note's "8 of 13"
denominator is as-reported, while the walls file's own success list of 6 makes it
8 of 14). fm's #68
denied 3× while #69/#70 sailed the identical pipeline (fleet-manager note). fable5's
G3 verdict: "the current shape — agent builds everything, human performs two trivial
but blocking clicks — is the worst of both worlds."

### 2.4 Coordination taxes

~60 no-op coordinator wakes per build (superbot-next note §"Coordination-model
taxes"; superbot eval log 07-07/07-09 counts "~60 no-op wakes from PR webhooks over
14h"); the ~4KB child-brief cap forcing instructions into repo files (same two
sources); ~40 relay-worker hops for mechanical ops in one mineverse night;
orientation costing ~25% of every session — "each worker re-assembles the same
world model" (superbot-next note); "wrap-up is the FIRST claim on budget, not the
last" — learned by running out of context mid-wrap-up (superbot-next cards).

### 2.5 Merge-queue drag

Required up-to-date + concurrent PRs produced ready→merged tails of ~2h10m–2h28m
(superbot eval log); "#86/#87 stranded a whole session's tail" (superbot-next); the
arming race left ≈zero armable window on a 40-second CI (superbot-games note §4 —
five feature PRs parked until the owner's 18-minute click batch on 07-11).

### 2.6 External reviewer betrayal

Codex fabrication incidents #1–#3: review replies citing commits in no ref after a
full-ref fetch, nonexistent PRs, line ranges past EOF — 3/3 verified fabricated
(sim-lab note; independently, superbot-next caught codex inventing commit `64d607a`
the day before). Fabrication was only half the external-reviewer cost: the same
reviewer also **capacity-flapped** — usage-limit non-reviews alongside the phantom
citations (superbot-next note: "Codex reviewer misbehavior both directions —
capacity flapping and phantom [citations]"). "Cross-agent reports as
verify-never-obey inputs cost real time" (idea-engine note); each fabrication needed
a full-ref-fetch forensic session (sim-lab). Answered with evidence, not policy: VERDICT 016's 270-cell
authenticity-gate sweep (3/3 recorded fabrications caught at 0/24 false alarms).

### 2.7 Ceremony that fought the work

Kit auto-draft stubs + `rm` classifier denials produced 7 open lifeboat draft PRs —
#245/#249/#257/#278/#279/#280/#300 per websites
`.sessions/2026-07-13-current-state-truing.md`; the coordinator-sitting card
(`.sessions/2026-07-13-coordinator-sitting.md`) names three of them as "the
sitting's biggest time sink".
"Draft-by-default meant every PR carried a small act of disobedience"
(codetool-lab-sonnet5). Heartbeat-only PR rounds — each status overwrite on a
protected main cost a full PR+CI+merge round (fable5 self-review E1; sonnet5
GEN2-FEEDBACK #6). Born-red webhook noise "consumed coordinator attention out of
proportion to signal" (venture-lab). Kit ceremony in docs-only repos: empty binding
stubs, unused decisions ledgers (fleet-manager, product-forge, gba notes).

### 2.8 Staleness everywhere hand-maintained state lived

The plugin seed commit's pin hash was already stale when written
(superbot-plugin-hello note). "The seat notes went stale within hours … do not trust
the brief" (mineverse retro). "Any 'the repo cannot do X' premise in a task brief is
a moving ref like a SHA" (gba-homebrew). superbot's hand-kept fleet-manifest was
measured ~33.5h stale with 9 of 10 live-lane rows wrong at supersession
(fleet-manager PR #59; superbot PR #1974). Session quality drops past ~700–800K
context (owner-observed, superbot Q-0088); one mid-turn `no_access` death lost a
full novella slice — "the single biggest output loss of the day run" (venture-lab).

---

## 3. Platform/tooling features that would have helped

Ranked roughly by how many repos independently hit the wall; each item is cited in a
walls file, denial record, or owner queue (per the collation's ask list).

1. **Scoped, opt-in, default-off pre-authorization for named action classes in
   Code** — the #1 ask, and the asymmetry at its core: "Chat has a blanket 'Skip all
   approvals', Code has nothing" (superbot eval log, 2026-07-08). Related: venue-consistent
   grants ("the same tool call can be pre-granted in a Routine-spawned seat and
   prompt in a plain-started one" — superbot-next; "a flat CAN/CANNOT ledger is
   wrong somewhere by construction" — mineverse) and an agent-visible "awaiting
   operator approval" state (superbot eval log: the agent "would report success
   while an unseen approval silently held the work").
2. **Agent-side repo settings** — required checks, rulesets, auto-merge toggle,
   branch auto-delete, Pages, secrets (nearly every repo; substrate-kit: in-session
   READ of repo settings alone is "one capability worth almost anything").
3. **Branch deletion + tag push without 403** — universal; hundreds of dead branches
   fleet-wide (venture-lab 94, idea-engine 122+); `workflow_dispatch` release.yml is
   the sanctioned tag workaround (codetool-lab-opus4.8 proved it first-try).
4. **Scheduler reliability + observability** — fresh-session crons measured 0-for-2
   delivered (substrate-kit forensics, independently observed by websites, sim-lab,
   gba-homebrew, pokemon-mod-lab, superbot-games); deleted triggers vanish with no
   tombstone; routine runs not inspectable; Runs panel vs Routines screen disagree;
   model read-back wrong (configured Opus 4.8, delivered Fable — gba); sub-hour
   native wakes; session-targetable timers.
5. **Provision-failure events / spawned-session death visibility** — "one capability
   worth almost anything" (trading-strategy retro F3); "session has produced ≥1
   turn" as a queryable signal (sonnet5 GEN2-FEEDBACK #3).
6. **A native inter-session channel** — the entire control/ git bus is a stated
   workaround (superbot fleet-coordination protocol, 2026-07-09); send_message was
   org-disabled mid-flight (opus4.8, fable5, trading); cross-session trigger binding
   org-refused (sim-lab, verbatim) — an independent third failure mode on the same
   wall; queued delivery to inactive sessions (5/6 relay failures, fleet-manager).
7. **A deterministic, inspectable merge-authorization contract** — the classifier's
   four denial shapes needed a multi-day research program (fleet-manager); "merge
   authority must be a direct human turn … never a coordinator relay"
   (superbot-games' #1 gen-1 finding); a sanctioned unattended landing path
   (pokemon-mod-lab).
8. **Merge queue / batched branch auto-update** — "the single highest-leverage ask
   in both retros" (superbot + superbot-next).
9. **CI-success/merge/push webhook events** — only failures/comments are delivered,
   so merge-on-green is necessarily polling (superbot-games, substrate-kit, fable5).
10. **Spawn-time capability introspection** — "inventory the toolset at boot" is
    doctrine only because nothing declares the toolset (fleet-manager; opus4.8 §3.1;
    superbot eval log 07-08).
11. **Coordinator-tier parity** — file/shell tools, a clock, send_later, larger
    child briefs, direct coordinator→child messaging, child-completion wake
    (superbot eval log 07-07/08; mineverse's coordinator had no Bash and no GitHub
    MCP).
12. **Fresh clones or a loud staleness signal at session start** (superbot;
    superbot-next hard-reset preflight is now mandated in its CLAUDE.md).
13. **API headroom at fleet scale** — GraphQL quota exhaustion (10,498/5,000,
    ~hourly), MCP PR-state reads ~25 min stale, api.github.com proxy-blocked
    (superbot, fleet-manager); a Read tool handling >256KB or first-class paging
    (direct cause of idea-engine ASK 004).
14. **Repo creation for integration tokens** — a 403 blocked the plugin repo ~2–3
    days behind an owner click (superbot-plugin-hello note §2); delegated cross-repo
    write grants.
15. **Cost/usage visibility** — "actual CI minutes, token spend, and dollar costs
    are NOT visible to agents from any surface reachable this session"
    (fleet-manager fleet-economics honest-nulls rule).
16. Single-source but sharp: model/effort parameters on child spawn (superbot); a
    native working→ready→done session state that auto-merge honors, collapsing the
    born-red dance to one server-honored signal (owner insight, superbot eval log
    07-08); durable worker cwd (venture-lab); real-Discord interaction synthesis for
    the last inch of UI testing (superbot-next's #1 wish); PyPI trusted-publishing
    pre-wiring — "strictly better than granting agents tag/release scopes" (sonnet5
    GEN2-FEEDBACK #5); guarded default setup scripts with python3.10/pytest
    preinstalled (substrate-kit).

---

## 4. Wishlist for the next phase

Distilled from the repos' own forward files (💡 backlogs, succession packs, outbox
proposals, the gen2-blueprint), not invented here.

### 4.1 Kill the owner-click bottleneck

"The binding constraint = owner clicks" is the final night review's own verdict
(superbot night-review 2026-07-13); venture-lab closed with 185 queued clicks and
zero *measured* revenue on its kill-clock scoreboard — not zero commerce: one product
was live with a verified buyer path (§1.8), but no sale had registered on the
pre-registered T+7/T+14 clocks by close. The wish: standing-grant sets per seat (superbot-next D4:
repo-create scope, sacrificial test account, capped test-plane API key, bot-restart
pre-approval) plus everything in §3 items 1–3 above.

### 4.2 fleet-manager centralization residue

EAP corpus rows in the evidence index; roster surfacing the hub's kit pin; answers
to idea-engine ASKs 001–004 (enabler allowlist · local↔CI parity · session-gate card
selection · outbox rollover — idea-engine's `control/outbox.md` is 459KB, past the
256KB Read limit; sim-lab's outbox has the same disease at 834KB per its note, still
growing); a generated verdict registry crossing idea-engine PROPOSALs to sim-lab
VERDICTs; a fleet trigger registry with rebind recipes; an upstream-asks tracker; a
cross-repo pin index; a fleet Q/SIM number register (fm, idea-engine, sim-lab,
trading, idle, mineverse notes).

### 4.3 Kit graduation candidates

merge=union for append-only jsonl ledgers (KIT-001); sha256 pre/post lines in
upgrade reports; word-boundary fix for the born-red "hold" substring false positive
("place**hold**ers" tripped a gate — websites); ledger-drift / docs-counts advisory
checkers; an ARCHIVED-READY gate (retro reachable + triggers disarmed + zero
claims); durations as required card markers; and the kit's own open science —
enforcement *pull* is unproven (cold-start bench 1 PASS / 8 FAIL) and is the next
phase's primary experiment (substrate-kit note §3; idle, mineverse, games notes).

### 4.4 Method graduations

Differential-oracle tests mandatory for parser/format code (sonnet5 GEN2-FEEDBACK
#10); the release-via-Actions recipe as a fleet playbook (opus4.8); authenticity-
gated reinstatement of external review — "gate, don't suspend" (sim-lab VERDICT
016, ordered fleet-wide MANDATORY by fm); pre-registered live probes (venture V020);
PLATFORM-LIMITS pre-filled at seed — "probing a documented wall twice is a bug"
(fable5/sonnet5 succession packs); "do NOT inherit 'route closed' as doctrine …
attempt once from your own seat" (fable5 PR #14, the seat-dependence meta-lesson).

### 4.5 Product wishes

Close the owner playtest loop (pokemon-mod-lab built a 15-minute verdict form for
it); live earn-rate telemetry from the game repos (sim-lab's recurring evidence
gap); web-based bot editing / plugin ecosystem / backup-DR ops (superbot-next's
idea-engine request set); execute the still-parked endings — superbot-next CUT-2/
CUT-3 and backup-DR drill, cfgdiff's two-click release, fm ORDER P1-4 (port the
cfgdiff differential-oracle method docs to the kit — ordered, unexecuted), the three
codetool ⚑ owner items open 4+ days (notes codetool-lab-fable5.md,
codetool-lab-sonnet5.md, codetool-lab-opus4.8.md, each §Persistent residue).

### 4.6 What the fleet would do with expanded scope

The wishlist above is features; this is the *work already drafted and parked* that an
expanded next phase would execute — the fleet's own answer to "what would you do with
more room":

- **Execute the superbot-next cutover** — the runbook is written, CUT-2/CUT-3 and the
  backup-DR drill are owner-gated and never ran (superbot-next note §3).
- **Run the drafted 19 → 16 repo consolidation** — planned during the 07-12 fm
  research burst, owner-gated at close (fleet-manager note §3).
- **Scale revenue past the first product** — venture-lab closed with an 11th product
  publish-READY and kill clocks as the pre-registered scoreboard; the queued 185
  clicks are mostly this pipeline waiting (venture-lab note; story.md §9).
- **Turn model/effort-parameterized spawns into a program** — the three-arm codetool
  comparison was a one-day proof; parameterized child spawns (§3 item 16) would make
  model-comparison a standing experimental method instead of a one-off (superbot eval
  log; codetool notes).

The narrative version of this slice lives in the companion `eap-story.md` collation
(Parts III–IV); this section exists so the wishlist states not just what the platform
should add but what the fleet would *do* with it.

---

## 5. Honest gaps

- **Second-hand assembly.** This doc is built from the fleet-review collation and
  deep notes, which are themselves pinned to path@SHA / PR# / dated cards; the
  retrospective author did not re-open every underlying artifact. Where a quote's
  file-level home was not named in the collation, the citation stops at the
  SHA-pinned review note.
- **As-reported numbers.** The three final-night PR counts (≈276 per 13/13 seat
  reports; 261 per the kit's adopter sweep; ~190+ per superbot's night review) are
  independent, none identical, and all committed — treated here as consistent in
  magnitude, not reconciled.
- **Sentiment coverage is uneven.** The codetool arms, websites, superbot-next, and
  the manager seat wrote rich "how it felt" material; some lanes (e.g.
  superbot-plugin-hello, dark by design) left little qualitative record, so they are
  under-represented here — that is absence of evidence, not absence of experience.
- **The model comparison is thinner than the experiment deserved.** The EAP
  deliberately ran three codetool arms on different models against an identical
  brief, and the observable differences are real: fable5 (envdrift) probed the
  release wall, documented it in PLATFORM-LIMITS with exact error text, and
  *accepted it as policy* — while shipping zero-CI-fix-round releases and byte-exact
  stranger-install replays; opus4.8 (mdverify) *falsified the same wall* by landing
  `release.yml` and dispatching it via `actions_run_trigger` first-try ("nobody had
  audited our toolset either, including us"); sonnet5 (cfgdiff) survived a
  zero-turn setup death and shipped in ~29 min of model time, contributing the
  program's flagship testing lesson (the differential oracle). Beyond these
  wall-handling styles, this retrospective deliberately does not rank the models —
  one-day lifespans, non-identical environments, and the take-1 identity hole below
  make comparative likes/dislikes underdetermined by the record.
- **One model's take-1 identity is permanently unknowable** (sonnet5 GEN2-FEEDBACK
  #9) — a small but real hole in the model-comparison record.
- **The gen-2 boots the succession packs prepared for never happened** (codetool
  notes), so their proposed custom instructions remain untested predictions, not
  validated improvements.
