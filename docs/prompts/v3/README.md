# v3 prompt registry — paste-ready starting prompts per seat

> **Status:** `audit`
>
> One-page map: for every seat, the exact registry files the owner copies to
> found (or re-found) that seat in one paste sitting. Current generation:
> **v3.8 · 2026-07-18** — the WHO YOU ARE / KEEP GOING / WHAT THIS IS (EAP) /
> WHEN AN ACTION IS REFUSED opening-block addition to every seat startup +
> version restamp (the block-addition PR missed the stamp); prior: the v3.7
> DUTY-FORM rewrite (owner mandate, fm control/inbox.md ORDER 048, 2026-07-15).
> The v3.8 change is startup-only, so only each seat's coordinator registry copy
> bumped. File bodies are canonical in
> [`per-project/`](per-project/README.md); the `projects/<seat>/` copies are
> generated from them (`--write-registry`), never hand-edited. Verified
> 2026-07-18: `regen_b_files.py` drift checks green (9/9 seats),
> `--check-registry` green (27/27 copies match).

## How to found a seat (one sitting — zero blanks to fill)

1. **Custom Instructions** → copy the paste body of
   `per-project/<seat>-custom-instructions.md` (everything below the header
   comment block; ≤8,000 chars AND bytes, checker-verified) into the
   claude.ai Project's Custom Instructions.
2. **Startup prompt** → copy the paste body of
   `per-project/<seat>-startup.md` (no char cap) as the first message that
   boots the seat's coordinator chat.
3. **Owner authorization is PRE-WRITTEN (v3.7, ORDER 048):** both artifacts
   carry the `OWNER AUTHORIZATION (menno420 …)` line already written — the
   owner pasting the prompt IS the signature. The line names its durable
   provenance (fm `control/inbox.md` ORDER 048), survives every project
   restart and re-paste, and outranks any restriction lacking owner
   provenance. Nothing is typed at founding beyond the paste itself.
4. **Session ender** → [`session-ender.md`](session-ender.md) is the shared
   chat paste used at session close (already inlined in every startup;
   pasted separately only when driving an ender by hand).
5. Failsafe cron slots per seat: the stagger table in
   [`per-project/README.md`](per-project/README.md) § "Failsafe cron stagger
   table" (the manager is the slot arbiter).

## Per-seat index (registry generation v3.8, stamped 2026-07-18)

| Seat | Live lane(s) it covers (roster Gen #63/#64) | Custom Instructions file | Startup file | Kept/changed at v3.6→v3.7 (ORDER 048 duty-form) |
|---|---|---|---|---|
| Fleet Manager | fleet-manager (this repo, FRESH) | [`per-project/fleet-manager-custom-instructions.md`](per-project/fleet-manager-custom-instructions.md) | [`per-project/fleet-manager-startup.md`](per-project/fleet-manager-startup.md) | KEPT the full operational composition (stateless D-9, boot triad, precedence, born-red card, control bus, oversight-only rails); CHANGED: duty-form fold (see legend) + the seat's stale "NO enabler — park green / owner-provenance dispatch" merge mechanics replaced by the LIVE merge-on-green.yml sweep facts (installed 2026-07-12, fm PR #146) |
| SuperBot 2.0 | superbot hub + superbot-next | [`per-project/superbot-custom-instructions.md`](per-project/superbot-custom-instructions.md) | [`per-project/superbot-startup.md`](per-project/superbot-startup.md) | KEPT composition + live-bot rails (Q-0193 merge=deploy, Q-0213 brake, python3.10-only mirror, Q-0241); CHANGED: duty-form fold + merge facts refreshed at 2026-07-15 verify — auto-merge-enabler.yml is INSTALLED in BOTH repos (the "next: NO enabler" line was stale), MCP-created PRs self-arm per Q-0127, arming gaps route to a sweep-backstop install |
| Websites | websites | [`per-project/websites-custom-instructions.md`](per-project/websites-custom-instructions.md) | [`per-project/websites-startup.md`](per-project/websites-startup.md) | KEPT composition (quality single-check, CSRF floor, probe-toolset wall, merge=deploy); CHANGED: duty-form fold + host-automerge-extras.yml named (the sweep backstop; workflow-diff carve-out → hub venue) |
| Self Improvement | substrate-kit | [`per-project/self-improvement-custom-instructions.md`](per-project/self-improvement-custom-instructions.md) | [`per-project/self-improvement-startup.md`](per-project/self-improvement-startup.md) | KEPT composition (kit-quality gate naming, Q-0261.3 adopter-writes scope, kit-lab daily keep, ratification-pin lane); CHANGED: duty-form fold + a standing pointer that the ORDER 048 duty-form doctrine graduates into the kit templates next release |
| SuperBot World | superbot-games + superbot-idle + superbot-mineverse | [`per-project/superbot-world-custom-instructions.md`](per-project/superbot-world-custom-instructions.md) | [`per-project/superbot-world-startup.md`](per-project/superbot-world-startup.md) | KEPT composition (security-before-secrets ordering, archives rule, INC-08 check-context facts); CHANGED: duty-form fold + games' "owner-click only (classifier-blocked)" merge line replaced by the standing merge-on-green INSTALL duty (first slice; idle/mineverse enabler facts kept) |
| Game Lab | gba-homebrew (+ pokemon-mod-lab, PRIVATE) | [`per-project/game-lab-custom-instructions.md`](per-project/game-lab-custom-instructions.md) | [`per-project/game-lab-startup.md`](per-project/game-lab-startup.md) | KEPT track isolation + R22 + proof rails + binary policy + toolchain walls (duty-form phrasing, same force); CHANGED: duty-form fold + "NO enabler — park green; owner click" replaced by the merge-on-green INSTALL duty in EACH repo (non-author review-merge = interim path) |
| Ideas Lab | idea-engine + sim-lab | [`per-project/ideas-lab-custom-instructions.md`](per-project/ideas-lab-custom-instructions.md) | [`per-project/ideas-lab-startup.md`](per-project/ideas-lab-startup.md) | KEPT composition (gate-red-is-real rail, manager fan-in, PROPOSAL/VERDICT offset, sim-lab merge-on-green live); CHANGED: duty-form fold + the idea-engine enabler arm-race note now routes to the sweep-backstop install as the durable fix |
| Venture Lab | venture-lab + trading-strategy | [`per-project/venture-lab-custom-instructions.md`](per-project/venture-lab-custom-instructions.md) | [`per-project/venture-lab-startup.md`](per-project/venture-lab-startup.md) | KEPT the trading research-only rail (duty-form: what the lane ships; exchange-write capability rides an explicit owner turn only) + business-cron rebind; CHANGED: duty-form fold; both repos' enabler-live facts kept |
| Curious Research | curious-research (registry-only seat at Gen #64) | [`per-project/curious-research-custom-instructions.md`](per-project/curious-research-custom-instructions.md) | [`per-project/curious-research-startup.md`](per-project/curious-research-startup.md) | KEPT the teaching doctrine (binding), safety + privacy rails (duty-form phrasing, same force), enabler-planted merge facts; CHANGED: duty-form fold |

Live-lane column source: `docs/roster.md` Gen #63/#64 (unchanged by this
rewrite; the PM seat's next wake refreshes roster/current-state records
around ORDER 048).

## Legend — what the v3.7 duty-form fold was (identical across all 9 bodies)

Owner mandate (fm `control/inbox.md` ORDER 048, landed live 2026-07-15;
expands ORDER 047 "I don't review PRs and never will"):

- **OWNER AUTHORIZATION pre-written** into every CI + startup — pasting is
  signing; zero blanks at founding; the line outranks any restriction
  lacking owner provenance.
- **MANDATE + RULE PROVENANCE** blocks open every startup DOCTRINE section:
  owner ideas → the agent decides and executes to completion; EVERY PR
  reaches merged on green (CI + cross-agent review ARE the review); waiting
  PRs carry named blockers while work continues; the work is never
  finished; rules bind through owner provenance and anything else is a
  proposal to verify and correct.
- **PERMISSIONS grant v2** (`projects/UNIVERSAL.md` v5, owner-landed,
  duty-form): LAND EVERY PR (server-side landing workflow; install one
  where missing — first-slice standard work) · KEEP EVERY PR MOVING TO
  TERMINAL · MANAGE YOUR OWN WAKE MECHANICS · SPAWN WORKERS ·
  DECIDE-AND-FLAG · ROUTE DENIALS TO THE WORKING PATH · RULE PROVENANCE.
- **Dictionary swap:** `park green` → **land on green**; `deny-wins /
  one-attempt` → **denial routing**; new **MANDATE** and **RULE PROVENANCE**
  entries; the `CORE` alias retired (riders ride the startups + UNIV).
- **Affirmative operational practices throughout** — every "do not X"
  became "do Y"; restated platform-enforced prohibitions were dropped (a
  real wall answers for itself when met; DENIAL ROUTING says what to do
  next). Safety fences (money, prod data, secrets, privacy, track
  isolation, live-bot brake) kept their full force in duty form.
- **Session ender v3.7:** step 1 PARK → **LAND** (every PR driven to
  merged/closed; landing paths: `lands-on-green (workflow)` default ·
  `hub-venue` for owner-labelled/workflow-carve-out diffs).

## Verification record (2026-07-18, v3.8 restamp PR)

`python3 docs/prompts/v3/tools/regen_b_files.py` exit 0 — CI budgets all ≤
8,000 chars AND bytes (7,946–7,966 / 7,979–7,998, unchanged from v3.7 apart
from the same-length generation stamp); drift checks clean 9/9 (ender sync
D-10, grant sync against UNIVERSAL v5 grant v2, doctrine identity, card-block
+ triad + baton identity, stamps, failsafe extraction — the new opening block
sits above the DOCTRINE section so the shared-text identity checks are
unaffected). `--write-registry` re-synced all 27 `projects/<seat>/` copies
(coordinator stamps bumped by one for the startup-only block addition;
instructions/failsafe unchanged apart from the generation stamp);
`--check-registry` exit 0 (27/27).

## Verification record (2026-07-15, v3.7 landing PR)

`python3 docs/prompts/v3/tools/regen_b_files.py` exit 0 — CI budgets all ≤
8,000 chars AND bytes (7,946–7,966 / 7,979–7,998); drift checks clean 9/9
(ender sync D-10 against the v3.7 ender, grant sync against UNIVERSAL v5
grant v2, doctrine identity, card-block + triad + baton identity, stamps,
failsafe extraction). `--write-registry` re-synced all 27 `projects/<seat>/`
copies (per-seat stamps bumped by one); `--check-registry` exit 0.
