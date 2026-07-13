# 2026-07-13 — v3 registry: fold the autonomy rider + superbot seed skills (v3.4 → v3.5)

> **Status:** `complete`

**Task (ORDER 039 seat-task 5, owner night-run directive; = superbot fleet-grounding.md §2
goal 5).** Fold the Q-0271 AUTONOMY RIDER and the two Q-0273 seed skills
(`chase-references`, `prep-owner-steps`) into the v3 prompt sources so the next
restamp/re-paste inherits them.

📊 Model: fable-5 (worker seat, night run)

## Shipped (PR #151)

- **Source material verified at superbot HEAD `cdb2680`:** router Q-0271 (never-wait
  fleet-wide; owner-only park classes; queue-and-continue), Q-0272 (standing cross-repo
  read authorization + fleet-reading-path), Q-0273 (hub-venue model + the seed skills as
  reference implementations), the AUTONOMY RIDER canonical text
  (`docs/owner/fleet-rearm-2026-07-12.md` §3 — Q-0271: "destined verbatim for the v3.4
  instruction bodies"), both SKILL.md bodies, and `fleet-grounding.md` §2 (PRESENT at
  HEAD; its goal 5 names this exact fold).
- **All 8 startups:** AUTONOMY RIDER + SEED SKILLS blocks inserted byte-identically in
  the shared `════ DOCTRINE ════` section (doctrine-identity drift check enforces it).
- **All 8 CIs:** BOOT TRIAD entry extended with `/ **AUTONOMY** (Q-0271) — owner away =
  NORMAL, queue-and-continue`; `skills` entry extended with `seeds Q-0273:
  **chase-references** + **prep-owner-steps** -> sb:.claude/skills/`; compensating
  wording-only trims (shared-entry compressions ×8 + small seat-section compressions —
  no rule dropped); final counts 7,985–7,996 bytes, all under the 8,000 wall.
- **v3.5 restamp per registry convention:** README title/lead/changelog/size table,
  per-file header stamps + char-counts, regen tool stamp regex + SEATS bumps +
  PROVENANCE_DATE, `--write-registry` re-sync (all 24 projects/<seat>/ copies match;
  versions +1: fm v7/v7/v7 · websites v7/v6/v6 · venture v6/v7/v6 · others v5/v5/v5).
- **planned-routes.md §B row** records the CI/startup split; **docs/SKILLS.md** gained a
  seat-local pointer section (canonical bodies = superbot `.claude/skills/` until
  kit-generalized, ORDER 034 lane).
- **Deliberately NOT folded:** ORDER 039's open-PRs-stay-open rule — a night-mode rule,
  not durable doctrine; the registry is STATELESS (D-9) and has no mode-rider slot.

## Incident (untangled, no damage)

The parallel night-watchdog-1 wake shares this checkout and switched branches mid-work:
my fold commit initially landed on `claude/night-watchdog-1` (local only — its remote
head 2401b40 and merged PR #150 were never disturbed). Resolved by rebuilding
`claude/v3-rider-fold` from origin/main (169e371) with cherry-picks of only this
session's commits and restoring the watchdog branch pointer; registry re-stamped against
the rebuilt commit.

## 💡 Session idea

**Card-declared branch guard for shared checkouts.** Tonight's collision class: two
sessions in ONE container checkout; a `git checkout -B` under a live session moves later
commits onto a foreign branch silently. Cheap enforcing guard: the session card carries a
`branch:` line (set at card creation) and the kit gate warns when a commit's HEAD branch
≠ the newest in-progress card's declared branch. Dedup: GIT HYGIENE mandates fresh
worktrees for *workers*, but nothing *detects* the violation when a wake/session lands in
the shared checkout anyway — this makes the existing rule self-enforcing (friction →
guard, superbot Q-0194).

## ⟲ Previous-session review

Previous session = night-watchdog-1 (#150): honest, well-evidenced — a full 1034-record
registry export and a FAIL 2/7 health verdict with named ids, not a papered-over green.
Improvement it surfaces: it branch-switched the shared checkout mid-flight without
checking for concurrent live work (my card commit sat between its commits) — wakes
sharing a container should take a worktree or scan `git status` + control/claims/ before
`checkout -B`; the session idea above is the enforcing half.

## Walls

None hit — no platform denials this session. (Not merge-attempted by design: fm lane =
park green / merge-on-green sweep, ORDER 039 rule 2.)
