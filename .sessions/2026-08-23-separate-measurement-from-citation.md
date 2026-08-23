# 2026-08-23 — the record that reports TRAP-001 had committed TRAP-001

> **Status:** `complete` — branch `claude/r5-archive-execution-4dsvoh`, cut from
> `origin/main` at `c2ce94a` (fm #928). Flipped after
> `python3 bootstrap.py check --strict` returned a real exit 0 on this tree,
> read directly and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

fm #928 landed the intent audit. Its § 3 asserted **"The services were deleted"**
under a `MEASURED` tag. What was actually measured is that **no botsite or
dashboard service exists in `reliable-grace` now**; that they were *deleted* on
2026-08-20/21 was read from a document. Two true statements, one tag, and the
blend is exactly [TRAP-001](../docs/traps.md) — committed in the record that
reports TRAP-001, one section above where it names it.

Caught by owner-review, and worth fixing rather than leaving: a findings doc
carrying a laundered citation is the specific thing this estate has spent the
day learning not to produce.

## previous-session review

⟲ fm #928 (`c2ce94a`) is this session's own previous work. Its two owner threads
and its § 5 measurement stand unchanged; only § 3's tag boundary was wrong.
Its § 4 correctly marked *two* seams as unresolved — the discipline was present
in the doc, just not applied to its own headline bullet.

## What landed

**`docs/findings/2026-08-23-active-repo-intent-audit.md` § 3**, two edits:

1. The bullet now leads with what was measured — *"No such services exist in
   `reliable-grace` today"* — and carries an in-place note recording what the
   sentence used to claim and why that was wrong. The estate corrects in place;
   erasing the error would remove the only evidence the trap fires on its own
   authors.
2. **A second live query was run to close the gap the reviewer actually opened:**
   absence in a service list could mean *dormant or unlinked* rather than gone.
   Re-queried asking each service for its latest deployment status, since a
   paused service still appears with its state: `reliable-grace` returned the
   same **two** services, `Postgres` and `worker`, both `SUCCESS`. So the
   absence now rules out dormant, not merely not-running.
3. The dependabot consequence is re-grounded so it no longer leans on the
   borrowed half: closing #2448/#2447 needs only *nothing serves that code*,
   which the service list and superbot's root `Procfile`
   (`worker: python disbot/bot1.py`) establish independently.

## The second finding, from the same review round

**`GET /user/repos?affiliation=owner` excludes organisation-owned repositories**,
so every "26 repositories" claim this session made rested on an unexamined
assumption about account shape. Checked: `GET /user/orgs` → **0 orgs**;
`affiliation=owner` → **26**; `affiliation=owner,organization_member,collaborator`
→ **26**; account type `User`. Identical, so 26 is the whole estate and the
figure survives.

**It survived by account shape, not by reasoning.** And the follow-on caution —
*"if an org is ever created, that query silently undercounts"* — is **`REASONED`,
not verified**, corrected same-session: GitHub's docs define `owner` as
*"Repositories that are owned by the authenticated user"* and `organization_member`
as access *"through being a member of an organization"*, but say **nothing** about
a repo owned by an org the user administers. The empirical check could not settle
it either — comparing the two filters with **0 orgs** is vacuous. So treat it as
a plausible gap to test *if* an org ever exists, not as a known defect. Same
family as the `search/code` coverage finding — a method that may quietly omit
rather than error.

## Verify

`python3 bootstrap.py check --strict` → **exit 0**, read directly, never after a
pipe.
