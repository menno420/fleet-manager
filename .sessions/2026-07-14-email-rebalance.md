# 2026-07-14 — EAP final email draft rebalance (owner-directed)

> **Status:** complete

📊 Model: Claude Fable (Claude 5 family)

about to do: revising the EAP final email draft per live owner directive (drop 600-word trim, ~700–800 words, self-contained).

Provenance: live owner directive 2026-07-14 ~11:00Z (relayed via coordinator dispatch) — the final email must stay concise but be complete and self-contained; keep all 7 ranked asks, restore the fuller "what genuinely worked" paragraph, expand shorthand for a non-fleet reader.

## Close-out
- done: body rebalanced 600 → 788 words on PR #196 — all 7 asks in rank order, every measured number script-verified present ("missing numbers: none"), fuller "what worked" paragraph restored (landing automation · born-red gate · one-file-per-claim · wake-chain redundancy · friction-to-guard, each in plain English), jargon expanded on first use; COPY markers + cited appendix untouched. Claim bullet reformatted to the parseable check_claims grammar mid-session. Heartbeat 11:33Z; card flipped last.

💡 Session idea: pin the email draft's cited numbers with a tiny fixture test. This session verified by ad-hoc script that all ~23 measured numbers in the COPY block survived the rewrite ("missing numbers: none") — that check dies with the session. A ~20-line test reading docs/eap-final-email-draft-2026-07-14.md and asserting each number in its own HTML-comment provenance still appears in the visible body would make every future edit to UPDATABLE owner-facing drafts unable to silently drop a cited figure (same enforce-don't-exhort instinct as Q-0132).

⟲ Previous-session review: the synthesis session (PR #194) turned the audit collection into a sendable email in one pass with airtight provenance comments — genuinely strong compression work. Its miss: it treated "600 words" as the spec and optimized against the cap, producing shorthand ("born-red gate", bare "seats") a non-fleet reader can't parse — exactly what forced this owner-directed rebalance hours later. Concrete workflow improvement: owner-facing external drafts should carry a self-containedness bar, not a word cap — "every term parseable by a first-time reader; length is a range (~700–800)" — worth a line in the drafting conventions so the next external doc is born self-contained.
