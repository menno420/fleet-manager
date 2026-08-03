# 2026-08-03 · hub — `gh` was never a wall: install it fleet-wide, and record why its absence never blocked anything

> **Status:** `complete`

- **📊 Model:** opus-5 · high · feature build — setup-base block + ledger entries

Time: 2026-08-03 · venue: owner-live hub chat · branch
`claude/gemini-video-qa-gem-jehvhh` (restarted from main after #696 merged) ·
PR fm #698

💡 Session idea: **a wall entry should carry the command that would refute it,
not just the one that produced it.** The two entries retired today were honest
reports of a real failure. What made them expensive is that neither shipped a
falsification test, so a later reader had no cheap way to ask *is this still
true, and was it ever general?* — and the safe-looking move was to believe them.
`gh` "is absent from these containers" was true of the image and never
re-attempted; `apt-cache policy gh` retires it in one second. Concretely: every
wall line should end with a **refutation recipe** — one command whose success
means the wall is gone. It costs a sentence at write time and converts the ledger
from a list of beliefs into a list of testable claims. This is the natural next
move for `tools/check_no_false_walls.py`, which today catches present-tense
denial phrasing but cannot tell a tested wall from an untested one; a wall with
no refutation recipe ages into folklore, and the estate has now produced several
inside three weeks.

## previous-session review

`2026-08-03-hub-gemini-video-qa-gem.md` (PR #696, merged) closed on the idea that
**a handoff should carry a negative inventory — what the evidence excludes**.
This card is the same shape one layer down: a wall entry states what failed and
omits what would prove it fixed, so the reader inherits a conclusion with no way
to test it. Both are cases of recording the positive claim and dropping the
boundary around it.

That card also failed its own standard within the hour — its close-out reported
"only push authority for fleet-manager" without ever attempting a push, which the
owner caught by asking. The claim never entered the repo, so
`check_no_false_walls.py` stayed clean while a false wall was stated in chat.
Worth knowing about the guard's actual coverage.

## Scope

Owner: sessions keep asking him to "enable `gh`", he does not know what it is or
where to add it, and he is right that they do not need it. Make it present, and
record that its absence is not a blocker. Plus close the ChatGPT half of the
share-link capability with a live link he supplied.

## What landed

- **`environments/setup-base.sh`** — new Block 2b installs `gh` when missing,
  non-fatal and idempotent, and logs the direct-PAT recipe. Every archetype
  sources this file, so it applies fleet-wide.
- **`docs/CAPABILITIES.md`** — two entries: `gh` is installable and required by
  nothing (retiring the 2026-07-14 wall), and the ChatGPT share-link path is now
  verified end to end.
- **`docs/conventions/reading-shared-ai-chats.md`** — ChatGPT status moved from
  "transport verified, extraction not" to verified.

## What was measured

`apt-cache policy gh` → candidate `2.45.0-1ubuntu0.3`. Installed, ran clean.

The auth behaviour is the part worth having, because it mimics a permission wall:

| call | proxied (ambient `GH_TOKEN`) | direct-PAT |
| --- | --- | --- |
| `gh api user` | `menno420` | `menno420` |
| `gh api repos/menno420/spider-swing` | **403** *"GitHub access is not enabled for this session. An org admin must connect the Claude GitHub App"* | 200 |
| `gh pr list --repo …` | **403** at GraphQL | real merged PRs |

That 403 names an org admin and a settings page. A session recording it at face
value would send the owner to fix a door that is already open — and `gh api user`
succeeding first makes it worse, because one endpoint answering reads as "auth is
fine, access is denied". **Both halves of a two-part check have to be run before
either is written down.**

The recorded owner request came from a session that, in the same message, listed
the open PRs and the open issue it had just read. Its GitHub access was working
while it declared itself blocked on a CLI it had not tried to install.

## Guard recipe

Before any GitHub wall goes in the ledger, the two commands that separate a real
wall from the proxied-REST quirk:

```bash
curl -sS --noproxy '*' -H "Authorization: Bearer $GITHUB_PAT" \
  -o /dev/null --write-out '%{http_code}\n' https://api.github.com/repos/menno420/fleet-manager
GH_TOKEN="$GITHUB_PAT" no_proxy='*' HTTPS_PROXY= gh api user --jq .login
```

Two successes mean the access is fine and the failure was the path. Anchors:
`environments/setup-base.sh` Block 2b, `docs/CAPABILITIES.md` append log.

## Verify

```bash
bash -n environments/setup-base.sh
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```

Last run this session: `bash -n` exit 0; gate red **only** on this card's own
designed hold before the flip; false-walls guard `CLEAN`.
