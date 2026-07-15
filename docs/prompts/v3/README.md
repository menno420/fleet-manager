# v3 prompt registry — paste-ready starting prompts per seat

> **Status:** `audit`
>
> One-page map: for every seat, the exact registry files the owner copies to
> found (or re-found) that seat in one paste sitting, plus the kept/changed
> note for the ORDER 040 TASK 1 synthesis (v3.4 → v3.5 → v3.6). File bodies
> are canonical in [`per-project/`](per-project/README.md); the
> `projects/<seat>/` copies are generated from them (`--write-registry`),
> never hand-edited. Verified 2026-07-15: `regen_b_files.py` drift checks
> green (9/9 seats), `--check-registry` green (27/27 copies match).

## How to found a seat (one sitting)

1. **Custom Instructions** → copy the paste body of
   `per-project/<seat>-custom-instructions.md` (everything below the header
   comment block; ≤8,000 chars, checker-verified) into the claude.ai
   Project's Custom Instructions.
2. **Startup prompt** → copy the paste body of
   `per-project/<seat>-startup.md` (no char cap) as the first message that
   boots the seat's coordinator chat.
3. **Session ender** → [`session-ender.md`](session-ender.md) is the shared
   chat paste used at session close (already inlined in every startup;
   pasted separately only when driving an ender by hand).
4. Failsafe cron slots per seat: the stagger table in
   [`per-project/README.md`](per-project/README.md) § "Failsafe cron stagger
   table" (the manager is the slot arbiter).

## Per-seat index (registry generation v3.6, stamped 2026-07-13)

| Seat | Live lane(s) it covers (roster Gen #63/#64) | Custom Instructions file | Startup file | Kept/changed at v3.5→v3.6 (ORDER 040 T1) |
|---|---|---|---|---|
| Fleet Manager | fleet-manager (this repo, FRESH) | [`per-project/fleet-manager-custom-instructions.md`](per-project/fleet-manager-custom-instructions.md) | [`per-project/fleet-manager-startup.md`](per-project/fleet-manager-startup.md) | KEPT the full v3.4 composition (stateless D-9, boot triad, precedence, born-red card, landing doctrine, walls-quoting); CHANGED: v3.5 rider+skills fold, v3.6 completion fold (see legend below) |
| SuperBot 2.0 | superbot hub + superbot-next | [`per-project/superbot-custom-instructions.md`](per-project/superbot-custom-instructions.md) | [`per-project/superbot-startup.md`](per-project/superbot-startup.md) | KEPT v3.4 composition; CHANGED: v3.5 + v3.6 folds, plus one seat-specific v3.6 refresh — the CI `Q-0241 never-wait` entry no longer reads "superbot-next ONLY" (Q-0271 generalized never-wait fleet-wide) |
| Websites | websites | [`per-project/websites-custom-instructions.md`](per-project/websites-custom-instructions.md) | [`per-project/websites-startup.md`](per-project/websites-startup.md) | KEPT v3.4 composition (incl. the v3.4 enabler-live merge mechanics); CHANGED: v3.5 + v3.6 folds only |
| Self Improvement | substrate-kit | [`per-project/self-improvement-custom-instructions.md`](per-project/self-improvement-custom-instructions.md) | [`per-project/self-improvement-startup.md`](per-project/self-improvement-startup.md) | KEPT v3.4 composition (incl. kit-lab daily keep-don't-rebind note); CHANGED: v3.5 + v3.6 folds only |
| SuperBot World | superbot-games + superbot-idle + superbot-mineverse | [`per-project/superbot-world-custom-instructions.md`](per-project/superbot-world-custom-instructions.md) | [`per-project/superbot-world-startup.md`](per-project/superbot-world-startup.md) | KEPT v3.4 composition; CHANGED: v3.5 + v3.6 folds only |
| Game Lab | gba-homebrew (+ pokemon-mod-lab, PRIVATE) | [`per-project/game-lab-custom-instructions.md`](per-project/game-lab-custom-instructions.md) | [`per-project/game-lab-startup.md`](per-project/game-lab-startup.md) | KEPT v3.4 composition (track isolation + R22 + proof rails verbatim); CHANGED: v3.5 + v3.6 folds only |
| Ideas Lab | idea-engine + sim-lab | [`per-project/ideas-lab-custom-instructions.md`](per-project/ideas-lab-custom-instructions.md) | [`per-project/ideas-lab-startup.md`](per-project/ideas-lab-startup.md) | KEPT v3.4 composition (incl. sim-lab merge-on-green line); CHANGED: v3.5 + v3.6 folds only |
| Venture Lab | venture-lab + trading-strategy | [`per-project/venture-lab-custom-instructions.md`](per-project/venture-lab-custom-instructions.md) | [`per-project/venture-lab-startup.md`](per-project/venture-lab-startup.md) | KEPT v3.4 composition (trading research-only rail verbatim); CHANGED: v3.5 + v3.6 folds only |
| Curious Research | curious-research (registry-only seat at Gen #64) | [`per-project/curious-research-custom-instructions.md`](per-project/curious-research-custom-instructions.md) | [`per-project/curious-research-startup.md`](per-project/curious-research-startup.md) | NEW at v3.6 — the founding pair (superbot `docs/owner/curious-research-project-prompts-2026-07-13.md`) conformed to registry format, stateless (D-9); failsafe slot `20 */2 * * *` adopted into the stagger table |

Live-lane column source: `docs/roster.md` Gen #63/#64. Live lanes at Gen #63
(superbot hub · substrate-kit · websites · idea-engine · sim-lab ·
venture-lab · trading-strategy · gba-homebrew) all map to a seat row above;
fleet-manager is this repo's own seat.

## Legend — what the shared folds were (identical across all 9 bodies)

- **v3.5 (stage-1, PR #151):** AUTONOMY RIDER (Q-0271) + the two seed skills
  (chase-references, prep-owner-steps) into the shared DOCTRINE section + CI
  dictionary hooks, with compensating budget trims (no rule dropped).
- **v3.6 (stage-2):** open-PRs-stay-open promoted to the STANDING default,
  FLEET READ (Q-0272), VENUE MODEL (Q-0273, `VENUE:hub`), GROUNDING (Q-0274)
  boot-read + per-seat grounding route, ninth seat added; trims, no rule
  dropped. Why the number is v3.6 and not "v3.5 stage-2": the stamp line is
  the DRIFT CHECK — a body-changing re-sync takes the next number
  ([`per-project/README.md`](per-project/README.md) § v3.6 changelog).
- Owner skim doc for the whole delta:
  [`CHANGES-v3.4-to-v3.5.md`](CHANGES-v3.4-to-v3.5.md).

## Synthesis verification record (2026-07-15, ORDER 040 T1 close)

Hub artifacts named by ORDER 040 diffed against the shipped v3.6 bodies:
every fold verified present in all 9 startups (grep: Q-0271, seed-skill
names, OPEN-PRs-STAY-OPEN sentence, Q-0272 fleet-read paragraph, `VENUE:hub`,
Q-0274 grounding route); `python3 docs/prompts/v3/tools/regen_b_files.py`
exit 0 (ender sync D-10, grant sync, doctrine identity, card-block identity,
BOOT TRIAD identity, stamps, failsafe extraction — all 9 seats clean);
`--check-registry` exit 0 (all 27 `projects/<seat>/` copies match). **No
real body drift found → no body edits, no version bump this pass** (registry
convention: no body change = no bump).
