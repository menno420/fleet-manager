# Owner comments — `websites`

> **Status:** `living-ledger`
>
> **Generated index.** Run `python3 tools/owner_comments.py reindex`;
> do not hand-edit this file. **Every record and all of its metadata
> are public.** Read the [storage and privacy contract](../README.md)
> before adding feedback. JSON preserves the owner's wording verbatim.

## Unconsumed (0)

No unconsumed owner comments.

## Consumed history (1)

| id | created at | consumed at | preserved record |
|---|---|---|---|
| `oc-c3c8bee2da350d92f9f32fe983e273bc` | `2026-08-28T00:34:26Z` | `2026-08-28T00:43:20Z` | [`oc-c3c8bee2da350d92f9f32fe983e273bc.json`](consumed/oc-c3c8bee2da350d92f9f32fe983e273bc.json) |

## Consume mechanically

After acting or explicitly reconciling a comment, run:

```text
python3 tools/owner_comments.py consume websites <comment-id> \
  --actor <session-card-or-actor> --evidence <record-or-PR-link>
```

Commit the moved record and both changed indexes together. Never delete it.
