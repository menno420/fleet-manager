# 2026-09-01 — the restate block aligned with `intake`, and the owner's first Fable 5.1 sitting recorded

> **Status:** `in-progress` — born red. Flips to `complete` only after
> `python scripts/preflight.py` returns a real exit code read directly and the
> diff has been re-read whole.

- **📊 Model:** fable-5 · high · docs-only
- **📍 Venue:** local-desktop
- **🔗 Session:** unavailable — local Claude Code session on the owner's laptop (Claude Desktop, Code tab); the harness exposes a UUID, not a claude.ai/code session id

💡 Session idea: **a rule that lives in a skill binds only a session that
invoked the skill.** The four-line restatement (HE SAID · ALREADY SETTLED ·
I INFER · LEAST SURE) is now delivered three ways that agree: by the
`continuation-prompt` skill's block, by the laptop hub's first-prompt hook,
and — as plan input — by the kit's SessionStart composer. Three copies of one
instruction is the one place duplication is right: each reaches a session the
others cannot.

## Mission

Owner, live, choosing all defaults on the successor-structure proposal: *"for
the estate blueprint you made, I believe we can go with all defaults."*
Question D of that proposal was to land the restate fix upstream now. This PR
does that, and records the sitting's owner words and the four decisions it
produced.

## What this PR does

1. **`.claude/skills/continuation-prompt/SKILL.md` § 4 and § 4a** — the
   `BEFORE YOUR FIRST TOOL CALL` block asks for four labelled lines instead of
   "a few sentences". `intake` (2026-08-09) names the fused paragraph as the
   failure mode — *"three kinds of claim that read exactly alike, so nobody can
   check the one that is wrong"* — and the block it compresses contradicted it.
   The prompt shape also gains `CLOSE WITH` (surface-specific end-of-session
   obligations) and `LESSONS FROM THIS SESSION`, and `READ FIRST` entries carry
   a freshness tag.
2. **`.claude/skills/prompt-preflight/SKILL.md` § Output** — three lines added
   to the preflight note: `NUMBERS` (every count in the prompt with the command
   that produced it, or moved to `UNVERIFIED`), `VENUE` (hub · clone ·
   container, which decides whether the prompt says "clone first" and names
   the shell) and `CLOSE WITH`. Each answers a measured miss in the prompt that
   opened this session: a "~26 of 27 repos" figure carried un-derived
   (measured by blob SHA across 28 repos: 17 kit stubs, 10 absent, 0 copies);
   `python3 scripts/preflight.py` prescribed to a Windows hub session; no
   closing obligations for the hub surface.
3. **`docs/findings/2026-09-01-owner-direction.md`** — his words from the
   sitting, verbatim: the successor's purpose and acceptance test, the two
   ideas behind fixing agent mistakes, the mail and the successor as one
   thread, the deliberate hook placement, the automerger doubt, his changing
   involvement, the six defaults.
4. **`docs/decisions.md`** — [D-0033] archive shape · [D-0034] file length ·
   [D-0035] build order · [D-0036] hooks in the hub repo only, by design.
5. **`docs/findings/README.md`** — membership regenerated with
   `tools/gen_findings_index.py`.
6. Pointers from three intent workbooks to the owner-direction record, so his
   words are findable from the questions they answer; no `OWNER:` marker is
   written on his behalf (`owner/intent-workbooks/HOW-TO-ANSWER.md`).

## Not done here, deliberately

- No Codex round requested: the owner's cadence (2026-08-29) reserves it for
  flip-readiness and important changes; this is skill text and records. If
  that reading is wrong, this is the PR to point at.
- The automerger question (G) is recorded as open, not decided.
- The estate-side restate hook (kit SessionStart composer) is plan input
  (OD-26 § 13–14: mechanisms wait), not built.

## ⟲ Previous-session review

The previous fleet-manager session (fm #1008, 2026-09-01) pointed the
intent-workbook generations at each other with `VERIFIED` pointers and no
deletions; re-read at `cb3fc9a` and holding. Its record on the laptop hub
overstated one claim (the owner-profile duplication) — corrected there, not
here, because the overstatement never reached this repository.

## Verify

- `python scripts/preflight.py` — real exit code, read directly.
- `python tools/gen_findings_index.py` re-run after the record is added, and
  its drift check read.
