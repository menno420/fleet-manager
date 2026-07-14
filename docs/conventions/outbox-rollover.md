# Outbox rollover — the append-only control-file archival convention

> **Status:** `binding`
>
> Authored 2026-07-14 (central-docs-plan A10, Slice 0 item 8 — the fm-side
> answer to idea-engine **ASK 004**, 2026-07-13T20:05:52Z). fm is the
> authored master for this convention (plan §4 class A); repos apply it to
> their own `control/outbox.md` (and any append-only control file) and may
> keep a local-delta appendix. The kit-side half — an advisory size check in
> `check --strict` — is kit-owned and routes as an ORDER to substrate-kit.

## The problem (measured)

Append-only outboxes outgrow single-read tooling: idea-engine's outbox
measured 368,007 bytes at its ASK (459KB by the fleet review), sim-lab's
~875KB (895,885 bytes, re-measured 2026-07-14) — both past the 256KB
Read-tool wall, forcing chunked reads on every consult. Meanwhile the fleet
cites into these files by `@SHA` + line number, so a naive split breaks the
citation web (plan §6, append-only citation breakage).

## The convention

1. **Threshold:** when `wc -c control/outbox.md` exceeds **200,000 bytes**
   (margin under the 256KB wall), the NEXT session that touches the file
   performs a rollover before appending.
2. **What rolls:** only **terminal** blocks — delivered/answered ASKs,
   PROPOSALs whose verdict landed, REPORTs already consumed by the manager.
   Open blocks never roll.
3. **Where to:** `control/outbox-archive-YYYY-MM.md` (dated by roll month,
   append-only itself, same grammar). An archive file that itself nears the
   threshold rolls to a `-partN` suffix rather than growing past it.
4. **Pointer stubs are mandatory and precede the roll** (plan §6 guard:
   "pointer stubs + pinned-SHA archive filenames BEFORE any file is
   rolled"). Each rolled block leaves a one-line stub in place:
   `## ASK 004 · … → ROLLED 2026-07-14 to control/outbox-archive-2026-07.md
   (originally appended @ <short-SHA>)`. HEAD readers follow the stub;
   historical `@SHA` citations stay valid because git history is immutable —
   the stub protects only the "read at HEAD" path.
5. **Numbering is content-stable, never positional** (fm playbook R19 /
   plan §6): a rolled ASK/PROPOSAL/VERDICT keeps its number forever; the
   live file never renumbers to fill gaps.
6. **One roll per PR, nothing else in it** — a rollover commit is pure
   moves + stubs, so the diff is mechanically reviewable and `git blame`
   stays useful.
7. **Kit half (routed, not local):** substrate-kit adds an advisory
   `check --strict` warning at the threshold so seats learn they're due
   before the Read wall bites. Until it ships, the threshold is enforced by
   this convention alone.

## First execution targets

- **sim-lab** `control/outbox.md` (~875KB — the worst case; ORDER-to-lane)
- **idea-engine** `control/outbox.md` (459KB; answering its own ASK 004 —
  ORDER-to-lane)

Both rolls are lane writes performed by the lane per this convention, not by
fm (each repo stays canonical for its own control files — fm authored the
rule, never the roll).
