#!/usr/bin/env python3
"""Validate, index, and consume Fleet Manager owner-comment records.

The committed files under ``docs/owner-comments/`` are the record.  This tool
does not talk to GitHub and does not make a local queue durable.  A website
writeback must put the record and both derived indexes in one Fleet Manager
branch commit, then use the repository's protected-main PR path.

Commands::

    python3 tools/owner_comments.py check
    python3 tools/owner_comments.py reindex
    python3 tools/owner_comments.py consume websites <comment-id> \
        --actor .sessions/2026-08-27-example.md \
        --evidence https://github.com/menno420/websites/pull/123

``consume`` is a move, never deletion: it moves the JSON into ``consumed/``,
changes its state, records consumption evidence, and regenerates the stable
per-repository README plus the cheap root ``index.json`` in the same working
tree operation.  The caller commits that whole diff together.
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
COMMENTS_REL = Path("docs/owner-comments")
ESTATE_REL = Path("docs/ESTATE.md")
SCHEMA_VERSION = 1
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{2,79}$")
SURFACE_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{0,63}$")
TIMESTAMP_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z$"
)
ESTATE_ROW_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|")
MAX_COMMENT_CHARS = 20_000
MAX_CONTEXT_CHARS = 1_000


class ContractError(ValueError):
    """The committed owner-comment contract is invalid or unsafe to change."""


@dataclass(frozen=True)
class Record:
    path: Path
    data: dict[str, Any]

    @property
    def repository(self) -> str:
        return str(self.data["repository"])

    @property
    def comment_id(self) -> str:
        return str(self.data["id"])

    @property
    def state(self) -> str:
        return str(self.data["state"])


def _utc_timestamp(value: str, field: str) -> str | None:
    if not isinstance(value, str) or not TIMESTAMP_RE.fullmatch(value):
        return f"{field} must be an RFC3339 UTC timestamp ending in Z"
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return f"{field} is not a real timestamp"
    return None


def _json_bytes(data: Any) -> bytes:
    return (json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode(
        "utf-8"
    )


def _atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def validate_record(data: Any, *, relative_path: Path | None = None) -> list[str]:
    """Return all deterministic schema/path errors for one record."""
    errors: list[str] = []
    label = relative_path.as_posix() if relative_path else "record"
    if not isinstance(data, dict):
        return [f"{label}: record must be a JSON object"]

    required = {
        "schema_version",
        "id",
        "repository",
        "created_at",
        "state",
        "source",
        "comment",
    }
    allowed = required | {"consumption"}
    missing = sorted(required - set(data))
    unknown = sorted(set(data) - allowed)
    if missing:
        errors.append(f"{label}: missing field(s): {', '.join(missing)}")
    if unknown:
        errors.append(f"{label}: unknown field(s): {', '.join(unknown)}")
    if missing:
        return errors

    if data.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"{label}: schema_version must be {SCHEMA_VERSION}")

    comment_id = data.get("id")
    if not isinstance(comment_id, str) or not ID_RE.fullmatch(comment_id):
        errors.append(f"{label}: id must match {ID_RE.pattern}")

    repository = data.get("repository")
    if not isinstance(repository, str) or not repository:
        errors.append(f"{label}: repository must be a non-empty string")

    timestamp_error = _utc_timestamp(data.get("created_at"), "created_at")
    if timestamp_error:
        errors.append(f"{label}: {timestamp_error}")

    state = data.get("state")
    if state not in {"unconsumed", "consumed"}:
        errors.append(f"{label}: state must be unconsumed or consumed")

    comment = data.get("comment")
    if not isinstance(comment, str):
        errors.append(f"{label}: comment must be a string")
    elif not comment.strip():
        errors.append(f"{label}: comment must contain non-whitespace text")
    elif len(comment) > MAX_COMMENT_CHARS:
        errors.append(f"{label}: comment exceeds {MAX_COMMENT_CHARS} characters")
    elif "\x00" in comment:
        errors.append(f"{label}: comment must not contain a NUL byte")

    source = data.get("source")
    if not isinstance(source, dict):
        errors.append(f"{label}: source must be an object")
    else:
        source_unknown = sorted(set(source) - {"surface", "context"})
        if source_unknown:
            errors.append(
                f"{label}: source has unknown field(s): {', '.join(source_unknown)}"
            )
        surface = source.get("surface")
        if not isinstance(surface, str) or not SURFACE_RE.fullmatch(surface):
            errors.append(f"{label}: source.surface must match {SURFACE_RE.pattern}")
        context = source.get("context")
        if context is not None and not isinstance(context, str):
            errors.append(f"{label}: source.context must be a string or null")
        elif isinstance(context, str) and len(context) > MAX_CONTEXT_CHARS:
            errors.append(
                f"{label}: source.context exceeds {MAX_CONTEXT_CHARS} characters"
            )
        elif isinstance(context, str) and "\x00" in context:
            errors.append(f"{label}: source.context must not contain a NUL byte")

    consumption = data.get("consumption")
    if state == "unconsumed":
        if consumption is not None:
            errors.append(f"{label}: unconsumed record must not have consumption")
    elif state == "consumed":
        if not isinstance(consumption, dict):
            errors.append(f"{label}: consumed record requires consumption object")
        else:
            unknown_consumption = sorted(
                set(consumption) - {"at", "actor", "evidence"}
            )
            missing_consumption = sorted(
                {"at", "actor", "evidence"} - set(consumption)
            )
            if missing_consumption:
                errors.append(
                    f"{label}: consumption missing field(s): "
                    + ", ".join(missing_consumption)
                )
            if unknown_consumption:
                errors.append(
                    f"{label}: consumption has unknown field(s): "
                    + ", ".join(unknown_consumption)
                )
            if not missing_consumption:
                consumed_at_error = _utc_timestamp(consumption.get("at"), "consumption.at")
                if consumed_at_error:
                    errors.append(f"{label}: {consumed_at_error}")
                for key in ("actor", "evidence"):
                    value = consumption.get(key)
                    if not isinstance(value, str) or not value.strip():
                        errors.append(
                            f"{label}: consumption.{key} must be a non-empty string"
                        )
                    elif len(value) > MAX_CONTEXT_CHARS:
                        errors.append(
                            f"{label}: consumption.{key} exceeds "
                            f"{MAX_CONTEXT_CHARS} characters"
                        )
                    elif "\x00" in value:
                        errors.append(
                            f"{label}: consumption.{key} must not contain a NUL byte"
                        )
                if not consumed_at_error and not timestamp_error:
                    created = datetime.fromisoformat(
                        str(data["created_at"])[:-1] + "+00:00"
                    )
                    consumed = datetime.fromisoformat(
                        str(consumption["at"])[:-1] + "+00:00"
                    )
                    if consumed < created:
                        errors.append(
                            f"{label}: consumption.at must not precede created_at"
                        )

    if relative_path is not None and isinstance(comment_id, str):
        if relative_path.name != f"{comment_id}.json":
            errors.append(f"{label}: filename must be {comment_id}.json")
        parts = relative_path.parts
        if len(parts) == 2:
            path_repository, filename = parts
            if filename.endswith(".json") and state != "unconsumed":
                errors.append(f"{label}: direct record must be unconsumed")
        elif len(parts) == 3 and parts[1] == "consumed":
            path_repository = parts[0]
            if state != "consumed":
                errors.append(f"{label}: consumed/ record must have consumed state")
        else:
            path_repository = ""
            errors.append(f"{label}: record path has unsupported nesting")
        if path_repository and repository != path_repository:
            errors.append(
                f"{label}: repository field {repository!r} does not match path "
                f"{path_repository!r}"
            )
    return errors


class OwnerCommentsStore:
    def __init__(self, root: Path = REPO) -> None:
        self.root = root.resolve()
        self.comments = self.root / COMMENTS_REL
        self.estate = self.root / ESTATE_REL

    def repositories(self) -> list[str]:
        if not self.estate.is_file():
            raise ContractError(f"missing estate index: {self.estate}")
        repositories = [
            match.group(1)
            for line in self.estate.read_text(encoding="utf-8").splitlines()
            if (match := ESTATE_ROW_RE.match(line))
        ]
        if not repositories:
            raise ContractError("docs/ESTATE.md contains no canonical repository rows")
        if len(repositories) != len(set(repositories)):
            raise ContractError("docs/ESTATE.md contains duplicate repository rows")
        return repositories

    def scan(self) -> tuple[list[Record], list[str]]:
        canonical = set(self.repositories())
        records: list[Record] = []
        errors: list[str] = []
        seen_ids: dict[str, Path] = {}
        if not self.comments.exists():
            return [], []

        for candidate in sorted(self.comments.rglob("*.json")):
            rel = candidate.relative_to(self.comments)
            if rel == Path("index.json"):
                continue
            if len(rel.parts) not in {2, 3}:
                errors.append(f"{rel.as_posix()}: unsupported JSON path")
                continue
            repository = rel.parts[0]
            if repository not in canonical:
                errors.append(
                    f"{rel.as_posix()}: repository is not indexed by docs/ESTATE.md"
                )
            try:
                data = json.loads(candidate.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"{rel.as_posix()}: invalid JSON ({exc})")
                continue
            record_errors = validate_record(data, relative_path=rel)
            errors.extend(record_errors)
            if record_errors:
                continue
            comment_id = str(data["id"])
            if comment_id in seen_ids:
                errors.append(
                    f"{rel.as_posix()}: duplicate id; first seen at "
                    f"{seen_ids[comment_id].as_posix()}"
                )
                continue
            seen_ids[comment_id] = rel
            records.append(Record(path=rel, data=data))

        if self.comments.is_dir():
            for child in sorted(self.comments.iterdir()):
                if child.is_dir() and child.name not in canonical:
                    errors.append(
                        f"{child.relative_to(self.root).as_posix()}: directory is not "
                        "a canonical docs/ESTATE.md repository"
                    )
        return records, errors

    def _by_repository(self, records: list[Record]) -> dict[str, list[Record]]:
        result = {repository: [] for repository in self.repositories()}
        for record in records:
            if record.repository in result:
                result[record.repository].append(record)
        for values in result.values():
            values.sort(key=lambda item: (item.data["created_at"], item.comment_id))
        return result

    def render_root_index(self, records: list[Record]) -> bytes:
        grouped = self._by_repository(records)
        rows = []
        for repository in self.repositories():
            active = [r for r in grouped[repository] if r.state == "unconsumed"]
            consumed = [r for r in grouped[repository] if r.state == "consumed"]
            rows.append(
                {
                    "repository": repository,
                    "index": f"docs/owner-comments/{repository}/README.md",
                    "unconsumed_count": len(active),
                    "consumed_count": len(consumed),
                    "latest_unconsumed_at": (
                        max((r.data["created_at"] for r in active), default=None)
                    ),
                    "latest_consumed_at": (
                        max(
                            (r.data["consumption"]["at"] for r in consumed),
                            default=None,
                        )
                    ),
                }
            )
        return _json_bytes(
            {
                "schema_version": SCHEMA_VERSION,
                "derived_from": [
                    "docs/ESTATE.md",
                    "docs/owner-comments/<repo>/*.json",
                    "docs/owner-comments/<repo>/consumed/*.json",
                ],
                "repositories": rows,
            }
        )

    def render_repository_index(self, repository: str, records: list[Record]) -> bytes:
        active = sorted(
            (r for r in records if r.repository == repository and r.state == "unconsumed"),
            key=lambda item: (item.data["created_at"], item.comment_id),
        )
        consumed = sorted(
            (r for r in records if r.repository == repository and r.state == "consumed"),
            key=lambda item: (item.data["consumption"]["at"], item.comment_id),
        )
        lines = [
            f"# Owner comments — `{repository}`",
            "",
            "> **Status:** `living-ledger`",
            ">",
            "> **Generated index.** Run `python3 tools/owner_comments.py reindex`;",
            "> do not hand-edit this file. Comment text is a **public record**. The",
            "> JSON files preserve the owner's wording verbatim.",
            "",
            f"## Unconsumed ({len(active)})",
            "",
        ]
        if active:
            lines.extend(
                [
                    "| id | created at | source | record |",
                    "|---|---|---|---|",
                ]
            )
            for record in active:
                source = str(record.data["source"]["surface"]).replace("|", "\\|")
                lines.append(
                    f"| `{record.comment_id}` | `{record.data['created_at']}` | "
                    f"{source} | [`{record.comment_id}.json`]({record.comment_id}.json) |"
                )
        else:
            lines.append("No unconsumed owner comments.")
        lines.extend(["", f"## Consumed history ({len(consumed)})", ""])
        if consumed:
            lines.extend(
                [
                    "| id | created at | consumed at | preserved record |",
                    "|---|---|---|---|",
                ]
            )
            for record in consumed:
                lines.append(
                    f"| `{record.comment_id}` | `{record.data['created_at']}` | "
                    f"`{record.data['consumption']['at']}` | "
                    f"[`{record.comment_id}.json`](consumed/{record.comment_id}.json) |"
                )
        else:
            lines.append("No consumed owner comments.")
        lines.extend(
            [
                "",
                "## Consume mechanically",
                "",
                "After acting or explicitly reconciling a comment, run:",
                "",
                "```text",
                f"python3 tools/owner_comments.py consume {repository} <comment-id> \\",
                "  --actor <session-card-or-actor> --evidence <record-or-PR-link>",
                "```",
                "",
                "Commit the moved record and both changed indexes together. Never delete it.",
                "",
            ]
        )
        return "\n".join(lines).encode("utf-8")

    def expected_indexes(self, records: list[Record]) -> dict[Path, bytes]:
        expected = {self.comments / "index.json": self.render_root_index(records)}
        for repository in self.repositories():
            expected[self.comments / repository / "README.md"] = (
                self.render_repository_index(repository, records)
            )
        return expected

    def check(self) -> list[str]:
        records, errors = self.scan()
        if errors:
            return errors
        for path, expected in self.expected_indexes(records).items():
            relative = path.relative_to(self.root).as_posix()
            if not path.is_file():
                errors.append(f"{relative}: missing generated index")
            elif path.read_bytes() != expected:
                errors.append(f"{relative}: generated index is stale; run reindex")
        return errors

    def reindex(self) -> None:
        records, errors = self.scan()
        if errors:
            raise ContractError("\n".join(errors))
        for path, content in self.expected_indexes(records).items():
            _atomic_write(path, content)

    def consume(
        self,
        repository: str,
        comment_id: str,
        *,
        consumed_at: str,
        actor: str,
        evidence: str,
    ) -> Path:
        canonical = self.repositories()
        if repository not in canonical:
            raise ContractError(
                f"{repository!r} is not a canonical repository in docs/ESTATE.md"
            )
        if not ID_RE.fullmatch(comment_id):
            raise ContractError("unsafe or invalid comment id")
        timestamp_error = _utc_timestamp(consumed_at, "consumption.at")
        if timestamp_error:
            raise ContractError(timestamp_error)
        if not actor.strip() or not evidence.strip():
            raise ContractError("actor and evidence are required for consumption")

        preflight_errors = self.check()
        if preflight_errors:
            raise ContractError(
                "owner-comment tree is not clean before consume:\n"
                + "\n".join(preflight_errors)
            )

        source = self.comments / repository / f"{comment_id}.json"
        destination = self.comments / repository / "consumed" / f"{comment_id}.json"
        if not source.is_file():
            if destination.is_file():
                raise ContractError(f"{comment_id!r} is already consumed")
            raise ContractError(f"unconsumed comment does not exist: {source}")
        if destination.exists():
            raise ContractError(f"consumed destination already exists: {destination}")

        data = json.loads(source.read_text(encoding="utf-8"))
        errors = validate_record(
            data, relative_path=source.relative_to(self.comments)
        )
        if errors:
            raise ContractError("\n".join(errors))
        updated = copy.deepcopy(data)
        updated["state"] = "consumed"
        updated["consumption"] = {
            "at": consumed_at,
            "actor": actor,
            "evidence": evidence,
        }
        updated_errors = validate_record(
            updated,
            relative_path=Path(repository) / "consumed" / f"{comment_id}.json",
        )
        if updated_errors:
            raise ContractError("\n".join(updated_errors))
        destination.parent.mkdir(parents=True, exist_ok=True)

        tracked = {
            path: path.read_bytes() if path.exists() else None
            for path in (
                source,
                destination,
                self.comments / repository / "README.md",
                self.comments / "index.json",
            )
        }
        try:
            source.replace(destination)  # the lifecycle transition is a real move
            _atomic_write(destination, _json_bytes(updated))
            self.reindex()
            postflight_errors = self.check()
            if postflight_errors:
                raise ContractError(
                    "consume produced an invalid tree:\n"
                    + "\n".join(postflight_errors)
                )
        except Exception:
            for path, prior in tracked.items():
                if prior is None:
                    if path.exists():
                        path.unlink()
                else:
                    _atomic_write(path, prior)
            raise
        return destination.relative_to(self.root)


def _now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="validate records and generated indexes")
    sub.add_parser("reindex", help="regenerate root and per-repository indexes")
    consume = sub.add_parser("consume", help="move one active comment into history")
    consume.add_argument("repository")
    consume.add_argument("comment_id")
    consume.add_argument("--at", default=None, help="RFC3339 UTC; defaults to now")
    consume.add_argument("--actor", required=True)
    consume.add_argument("--evidence", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    store = OwnerCommentsStore()
    try:
        if args.command == "check":
            errors = store.check()
            if errors:
                for error in errors:
                    print(f"ERROR  {error}")
                print(f"owner comments: {len(errors)} error(s)")
                return 1
            records, _ = store.scan()
            active = sum(record.state == "unconsumed" for record in records)
            consumed = sum(record.state == "consumed" for record in records)
            print(
                f"owner comments: CLEAN — {len(store.repositories())} repositories, "
                f"{active} unconsumed, {consumed} consumed"
            )
            return 0
        if args.command == "reindex":
            store.reindex()
            print(
                f"owner comments: indexed {len(store.repositories())} repositories"
            )
            return 0
        path = store.consume(
            args.repository,
            args.comment_id,
            consumed_at=args.at or _now_utc(),
            actor=args.actor,
            evidence=args.evidence,
        )
        print(f"owner comments: consumed and preserved at {path.as_posix()}")
        return 0
    except ContractError as exc:
        print(f"ERROR  {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
