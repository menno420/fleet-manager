# `estate-backups` — what I think you intend

## Current evidence

`VERIFIED`: this is a private GitHub Actions venue for estate data backups and
carefully scoped Railway/Postgres operations. It is dormant between explicit
owner asks.

## My interpretation

`DERIVED`: this repository should be deliberately boring: minimal code, narrow
permissions, recoverable workflows, clear evidence, and no feature roadmap. Its
success is reliable recovery and safe one-shot operations, not activity.

## Questions for you

1. Which databases or data sets must it protect?
2. How long should backups be retained?
3. How often should restore—not just backup—be tested?
4. Which operations may run automatically and which always require you?
5. Should backup storage and operational workflows remain in the same repository?
6. What failure or growth would justify replacing this approach?

## Your words

`OWNER`:

