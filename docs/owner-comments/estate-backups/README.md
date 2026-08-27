# Owner comments — `estate-backups`

> **Status:** `living-ledger`
>
> **Generated index.** Run `python3 tools/owner_comments.py reindex`;
> do not hand-edit this file. **Every record and all of its metadata
> are public.** Read the [storage and privacy contract](../README.md)
> before adding feedback. JSON preserves the owner's wording verbatim.

## Unconsumed (0)

No unconsumed owner comments.

## Consumed history (0)

No consumed owner comments.

## Consume mechanically

After acting or explicitly reconciling a comment, run:

```text
python3 tools/owner_comments.py consume estate-backups <comment-id> \
  --actor <session-card-or-actor> --evidence <record-or-PR-link>
```

Commit the moved record and both changed indexes together. Never delete it.
