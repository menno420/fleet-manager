# 2026-08-05 · hub — correct the menu-parity claim: the navigation graph is the product

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: the previous PR shipped a measurement that was precise, exact,
reproducible, and answering a question nobody had. It counted what fraction of
*commands* build a view — in a bot whose commands nobody types.

## Previous-session review

PR #759 landed the superbot-next live audit. It recorded the menu-versus-text
ratio as **"inherited, not introduced"** on a 17%-vs-21% comparison. The owner
sent a screen recording of the old bot that makes the claim untenable, and the
correction is large enough to change what milestone one should build.

## Planned

- `docs/findings/2026-08-05-superbot-next-live-audit.md` — replace the
  command-ratio metric with a **reachability** measurement, add the
  per-subsystem table, retarget § 5, and record the wrong claim in § 7.
- `docs/findings/README.md` — index row updated to lead with the corrected
  finding.

## Verification

To run: `python3 tools/check_no_false_walls.py --strict` and
`python3 bootstrap.py check --strict`, both post-commit, real exit codes.
