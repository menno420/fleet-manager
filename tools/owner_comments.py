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
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
COMMENTS_REL = Path("docs/owner-comments")
ESTATE_REL = Path("docs/ESTATE.md")
SCHEMA_VERSION = 1
SCHEMA_SHA256 = "f20d60213aafd6abe5ca315d9b468cb5ddbab14fd9e3bddea8263c2fbedb76a4"
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{2,79}$")
SURFACE_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{0,63}$")
REPOSITORY_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,99}$")
TIMESTAMP_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z$"
)
ESTATE_ROW_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|")
MAX_COMMENT_CHARS = 20_000
MAX_CONTEXT_CHARS = 1_000
WINDOWS_RESERVED = {
    "con", "prn", "aux", "nul",
    *(f"com{number}" for number in range(1, 10)),
    *(f"lpt{number}" for number in range(1, 10)),
}
ROOT_RESERVED = {"readme.md", "index.json", "record.schema.json"}


class ContractError(ValueError):
    """The committed owner-comment contract is invalid or unsafe to change."""


def _windows_safe_component(value: str) -> bool:
    return (
        not value.endswith((".", " "))
        and value.split(".", 1)[0].casefold() not in WINDOWS_RESERVED
    )


def _valid_comment_id(value: Any) -> bool:
    return (
        isinstance(value, str)
        and bool(ID_RE.fullmatch(value))
        and ".." not in value
        and not value.endswith(".lock")
        and _windows_safe_component(value)
    )


def _valid_repository(value: str) -> bool:
    return (
        bool(REPOSITORY_RE.fullmatch(value))
        and _windows_safe_component(value)
        and value.casefold() not in ROOT_RESERVED
    )


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


def _parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value[:-1] + "+00:00")


def _utc_timestamp(value: str, field: str) -> str | None:
    if not isinstance(value, str) or not TIMESTAMP_RE.fullmatch(value):
        return f"{field} must be an RFC3339 UTC timestamp ending in Z"
    try:
        _parse_timestamp(value)
    except ValueError:
        return f"{field} is not a real timestamp"
    return None


def _json_bytes(data: Any) -> bytes:
    return (json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode(
        "utf-8"
    )


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ContractError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def _load_json(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    return _decode_json(raw), raw


def _decode_json(raw: bytes) -> dict[str, Any]:
    data = json.loads(raw.decode("utf-8"), object_pairs_hook=_reject_duplicate_keys)
    if not isinstance(data, dict):
        raise ContractError("record must be a JSON object")
    if _contains_surrogate(data):
        raise ContractError("record contains an invalid Unicode surrogate")
    return data


def _contains_surrogate(value: Any) -> bool:
    if isinstance(value, str):
        return any(0xD800 <= ord(character) <= 0xDFFF for character in value)
    if isinstance(value, dict):
        return any(
            _contains_surrogate(key) or _contains_surrogate(item)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return any(_contains_surrogate(item) for item in value)
    return False


def _atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        _fsync_directory(path.parent)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def _fsync_directory(path: Path) -> None:
    """Best-effort directory sync for transaction markers on supported OSes."""
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError:
        return
    try:
        os.fsync(descriptor)
    except OSError:
        pass
    finally:
        os.close(descriptor)


def _write_transaction_manifest(path: Path, data: dict[str, Any]) -> None:
    """Durably replace a transaction manifest without using the data writer."""
    content = _json_bytes(data)
    fd, temporary = tempfile.mkstemp(prefix=".manifest.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        _fsync_directory(path.parent)
    except BaseException:
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

    if type(data.get("schema_version")) is not int or data.get(
        "schema_version"
    ) != SCHEMA_VERSION:
        errors.append(f"{label}: schema_version must be {SCHEMA_VERSION}")

    comment_id = data.get("id")
    if not _valid_comment_id(comment_id):
        errors.append(
            f"{label}: id must be lowercase path/ref-safe text, 3–80 "
            "characters, with no '..', trailing '.', '.lock', or Windows "
            "reserved device name"
        )

    repository = data.get("repository")
    if not isinstance(repository, str) or not repository:
        errors.append(f"{label}: repository must be a non-empty string")

    timestamp_error = _utc_timestamp(data.get("created_at"), "created_at")
    if timestamp_error:
        errors.append(f"{label}: {timestamp_error}")

    state = data.get("state")
    if not isinstance(state, str) or state not in {"unconsumed", "consumed"}:
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
        if "consumption" in data:
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
                    created = _parse_timestamp(str(data["created_at"]))
                    consumed = _parse_timestamp(str(consumption["at"]))
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

    def _assert_safe_target(self, path: Path) -> None:
        if self.comments.is_symlink():
            raise ContractError("docs/owner-comments must not be a symlink")
        base = self.comments.resolve(strict=False)
        resolved = path.resolve(strict=False)
        try:
            resolved.relative_to(base)
        except ValueError as exc:
            raise ContractError(f"owner-comment path escapes storage root: {path}") from exc
        if path.is_symlink():
            raise ContractError(f"owner-comment target must not be a symlink: {path}")

    def _lock_path(self) -> Path:
        """Return a store-stable lock path independent of process TMPDIR.

        A Git common-dir lock serializes all worktrees of the same repository
        without dirtying the tree.  The non-Git fallback is derived from the
        resolved store path and its parent, so two processes cannot evade each
        other merely by carrying different temporary-directory environments.
        """
        digest = hashlib.sha256(str(self.root).encode("utf-8")).hexdigest()[:20]
        result = subprocess.run(
            ["git", "rev-parse", "--git-common-dir"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0 and result.stdout.strip():
            common = Path(result.stdout.strip())
            if not common.is_absolute():
                common = self.root / common
            return common.resolve() / f"fleet-manager-owner-comments-{digest}.lock"
        return (
            self.root.parent
            / ".fleet-manager-owner-comment-locks"
            / f"{digest}.lock"
        )

    def _transaction_root(self) -> Path:
        """Non-worktree journal home shared by every process for this store."""
        lock_path = self._lock_path()
        return lock_path.parent / f"{lock_path.stem}-transactions"

    def _git_identity(self) -> dict[str, str | None]:
        """Return the exact HEAD/index identity a rollback was prepared for."""
        inside = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )
        if inside.returncode != 0 or inside.stdout.strip() != "true":
            return {"head": None, "index_tree": None}

        head_result = subprocess.run(
            ["git", "rev-parse", "--verify", "HEAD"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )
        head = head_result.stdout.strip() if head_result.returncode == 0 else None
        tree_result = subprocess.run(
            ["git", "write-tree"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )
        if tree_result.returncode != 0:
            detail = tree_result.stderr.strip() or "git write-tree failed"
            raise ContractError(
                f"cannot identify owner-comment transaction Git index: {detail}"
            )
        index_tree = tree_result.stdout.strip()
        oid = re.compile(r"^[0-9a-f]{40,64}$")
        if (head is not None and not oid.fullmatch(head)) or not oid.fullmatch(
            index_tree
        ):
            raise ContractError("Git returned an invalid transaction identity")
        return {"head": head, "index_tree": index_tree}

    @contextmanager
    def mutation_lock(self):
        """Take a non-blocking process lock for a consume transaction.

        The lock lives in Git's common metadata (or a root-derived fallback),
        and the OS releases it if a process dies. That avoids both concurrent
        rollbacks undoing a successful consume and TMPDIR-specific lock islands.
        """
        lock_path = self._lock_path()
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        handle = lock_path.open("a+b")
        try:
            if os.name == "nt":
                import msvcrt  # noqa: PLC0415 — platform-specific stdlib

                handle.seek(0, os.SEEK_END)
                if handle.tell() == 0:
                    handle.write(b"\0")
                    handle.flush()
                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl  # noqa: PLC0415 — platform-specific stdlib

                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except (BlockingIOError, OSError) as exc:
            handle.close()
            raise ContractError(
                "another owner-comment mutation transaction is in progress"
            ) from exc
        try:
            self._recover_transactions()
            yield
        finally:
            if os.name == "nt":
                import msvcrt  # noqa: PLC0415 — platform-specific stdlib

                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl  # noqa: PLC0415 — platform-specific stdlib

                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
            handle.close()

    def _transaction_manifest(
        self, paths: tuple[Path, ...]
    ) -> dict[str, Any]:
        entries = []
        for number, path in enumerate(paths):
            try:
                relative = path.relative_to(self.root)
            except ValueError as exc:
                raise ContractError(
                    f"transaction path is outside repository root: {path}"
                ) from exc
            entries.append(
                {
                    "path": relative.as_posix(),
                    "existed": path.exists(),
                    "backup": str(number) if path.exists() else None,
                }
            )
        return {
            "schema_version": 2,
            "state": "prepared",
            "root": str(self.root),
            "git_identity": self._git_identity(),
            "entries": entries,
        }

    def _read_transaction_manifest(
        self, backup_root: Path
    ) -> dict[str, Any] | None:
        manifest_path = backup_root / "manifest.json"
        if not manifest_path.exists():
            return None
        if manifest_path.is_symlink() or not manifest_path.is_file():
            raise ContractError(
                f"invalid owner-comment transaction manifest: {manifest_path}"
            )
        try:
            data, raw = _load_json(manifest_path)
        except Exception as exc:
            raise ContractError(
                f"cannot read owner-comment transaction manifest {manifest_path}: {exc}"
            ) from exc
        if raw != _json_bytes(data):
            raise ContractError(
                f"owner-comment transaction manifest is not canonical: {manifest_path}"
            )
        if set(data) != {
            "schema_version",
            "state",
            "root",
            "git_identity",
            "entries",
        }:
            raise ContractError(
                f"owner-comment transaction manifest has unknown fields: {manifest_path}"
            )
        if data.get("schema_version") != 2 or data.get("state") not in {
            "prepared",
            "committed",
        }:
            raise ContractError(
                f"owner-comment transaction manifest has invalid state: {manifest_path}"
            )
        if data.get("root") != str(self.root):
            raise ContractError(
                f"owner-comment transaction belongs to another worktree: {manifest_path}"
            )
        identity = data.get("git_identity")
        if not isinstance(identity, dict) or set(identity) != {"head", "index_tree"}:
            raise ContractError(
                f"owner-comment transaction Git identity is invalid: {manifest_path}"
            )
        oid = re.compile(r"^[0-9a-f]{40,64}$")
        head = identity.get("head")
        index_tree = identity.get("index_tree")
        if (
            head is not None
            and (not isinstance(head, str) or not oid.fullmatch(head))
        ) or (
            index_tree is not None
            and (
                not isinstance(index_tree, str)
                or not oid.fullmatch(index_tree)
            )
        ) or (head is not None and index_tree is None):
            raise ContractError(
                f"owner-comment transaction Git identity is invalid: {manifest_path}"
            )
        if not isinstance(data.get("entries"), list):
            raise ContractError(
                f"owner-comment transaction manifest entries are invalid: {manifest_path}"
            )

        seen: set[Path] = set()
        for entry in data["entries"]:
            if not isinstance(entry, dict) or set(entry) != {
                "path",
                "existed",
                "backup",
            }:
                raise ContractError(
                    f"owner-comment transaction entry is invalid: {manifest_path}"
                )
            relative_text = entry.get("path")
            existed = entry.get("existed")
            backup_name = entry.get("backup")
            if not isinstance(relative_text, str) or not isinstance(existed, bool):
                raise ContractError(
                    f"owner-comment transaction entry types are invalid: {manifest_path}"
                )
            relative = Path(relative_text)
            if (
                relative.is_absolute()
                or ".." in relative.parts
                or not relative.parts
                or relative.parts[:2] != COMMENTS_REL.parts
                or relative in seen
            ):
                raise ContractError(
                    f"unsafe owner-comment transaction path {relative_text!r}"
                )
            seen.add(relative)
            target = self.root / relative
            self._assert_safe_target(target)
            if existed:
                if not isinstance(backup_name, str) or not backup_name.isdigit():
                    raise ContractError(
                        f"owner-comment transaction backup is invalid: {manifest_path}"
                    )
                backup = backup_root / backup_name
                if (
                    data["state"] == "prepared"
                    and (backup.is_symlink() or not backup.is_file())
                ):
                    raise ContractError(
                        f"owner-comment transaction backup is missing: {backup}"
                    )
            elif backup_name is not None:
                raise ContractError(
                    f"owner-comment transaction has a backup for an absent path: "
                    f"{manifest_path}"
                )
        return data

    def _quarantine_transaction(self, backup_root: Path) -> Path:
        """Preserve a stale prepared journal without touching this checkout."""
        suffix = backup_root.name.removeprefix("txn-")
        quarantine = backup_root.with_name(f"quarantine-{suffix}")
        if quarantine.exists() or quarantine.is_symlink():
            raise ContractError(
                "cannot quarantine stale owner-comment transaction because "
                f"the deterministic destination exists: {quarantine}"
            )
        os.rename(backup_root, quarantine)
        _fsync_directory(backup_root.parent)
        return quarantine

    def _restore_transaction(
        self, backup_root: Path, manifest: dict[str, Any]
    ) -> None:
        """Idempotently restore a prepared transaction without consuming backups."""
        for entry in manifest["entries"]:
            target = self.root / entry["path"]
            if entry["existed"]:
                backup = backup_root / entry["backup"]
                target.parent.mkdir(parents=True, exist_ok=True)
                fd, temporary = tempfile.mkstemp(
                    prefix=f".{target.name}.recover.", dir=target.parent
                )
                os.close(fd)
                try:
                    shutil.copy2(backup, temporary)
                    with open(temporary, "rb") as handle:
                        os.fsync(handle.fileno())
                    os.replace(temporary, target)
                    _fsync_directory(target.parent)
                except BaseException:
                    try:
                        os.unlink(temporary)
                    except FileNotFoundError:
                        pass
                    raise
            elif target.exists() or target.is_symlink():
                if target.is_dir() and not target.is_symlink():
                    raise ContractError(
                        f"transaction recovery refuses to delete directory: {target}"
                    )
                target.unlink()
                _fsync_directory(target.parent)

    def _recover_transactions(self) -> None:
        """Recover any process-terminated transaction while holding the lock."""
        transaction_root = self._transaction_root()
        if not transaction_root.exists():
            return
        if transaction_root.is_symlink() or not transaction_root.is_dir():
            raise ContractError(
                f"invalid owner-comment transaction root: {transaction_root}"
            )
        transactions: list[tuple[Path, dict[str, Any]]] = []
        for backup_root in sorted(transaction_root.glob("txn-*")):
            if backup_root.is_symlink() or not backup_root.is_dir():
                raise ContractError(
                    f"invalid owner-comment transaction path: {backup_root}"
                )
            manifest = self._read_transaction_manifest(backup_root)
            if manifest is None:
                # ``txn-*`` is published into this root-digested, non-worktree
                # directory only after a durable manifest exists.  Therefore a
                # manifest-less published directory can only be residue from
                # committed cleanup deleting the manifest before the directory.
                shutil.rmtree(backup_root, ignore_errors=True)
                _fsync_directory(transaction_root)
                continue
            transactions.append((backup_root, manifest))

        prepared = [item for item in transactions if item[1]["state"] == "prepared"]
        if prepared:
            current_identity = self._git_identity()
            mismatched = [
                item
                for item in prepared
                if item[1]["git_identity"] != current_identity
            ]
            if mismatched:
                quarantined = [
                    self._quarantine_transaction(backup_root)
                    for backup_root, _ in mismatched
                ]
                raise ContractError(
                    "prepared owner-comment transaction belongs to a different "
                    "Git HEAD/index tree; the current checkout was not changed and "
                    "the stale recovery data was quarantined at "
                    + ", ".join(str(path) for path in quarantined)
                )

        for backup_root, manifest in transactions:
            if manifest["state"] == "prepared":
                self._restore_transaction(backup_root, manifest)
                manifest["state"] = "committed"
                _write_transaction_manifest(
                    backup_root / "manifest.json", manifest
                )
            shutil.rmtree(backup_root, ignore_errors=True)
            _fsync_directory(transaction_root)

    @contextmanager
    def rollback_snapshot(self, paths: tuple[Path, ...]):
        """Restore files on exceptions and journal recovery across process death.

        Backups live on the repository filesystem and prefer hard links, so a
        persistent failure in ``_atomic_write`` cannot also disable rollback.
        A durable prepared/committed manifest lets the next locked operation
        recover an ``os._exit``/SIGTERM interruption deterministically.
        """
        transaction_root = self._transaction_root()
        transaction_root.mkdir(parents=True, exist_ok=True)
        _fsync_directory(transaction_root.parent)
        backup_root = Path(
            tempfile.mkdtemp(prefix=".initializing-", dir=transaction_root)
        )
        manifest = self._transaction_manifest(paths)
        prepared = False
        try:
            for entry in manifest["entries"]:
                if entry["existed"]:
                    path = self.root / entry["path"]
                    backup = backup_root / entry["backup"]
                    try:
                        os.link(path, backup)
                    except OSError:
                        shutil.copy2(path, backup)
            _write_transaction_manifest(backup_root / "manifest.json", manifest)
            final_root = transaction_root / (
                "txn-" + backup_root.name.removeprefix(".initializing-")
            )
            os.replace(backup_root, final_root)
            _fsync_directory(transaction_root)
            backup_root = final_root
            prepared = True
            yield
            manifest["state"] = "committed"
            _write_transaction_manifest(backup_root / "manifest.json", manifest)
        except BaseException:
            if prepared:
                self._restore_transaction(backup_root, manifest)
                # Mark the restored state final before cleanup, so a cleanup
                # interruption never retries against partially removed backups.
                manifest["state"] = "committed"
                _write_transaction_manifest(
                    backup_root / "manifest.json", manifest
                )
                shutil.rmtree(backup_root, ignore_errors=True)
                _fsync_directory(transaction_root)
            else:
                shutil.rmtree(backup_root, ignore_errors=True)
                _fsync_directory(transaction_root)
            raise
        else:
            shutil.rmtree(backup_root, ignore_errors=True)
            _fsync_directory(transaction_root)

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
        invalid = [repo for repo in repositories if not _valid_repository(repo)]
        if invalid:
            raise ContractError(
                "docs/ESTATE.md has unsafe repository name(s): "
                + ", ".join(repr(repo) for repo in invalid)
            )
        if len(repositories) != len(set(repositories)):
            raise ContractError("docs/ESTATE.md contains duplicate repository rows")
        folded = [repository.casefold() for repository in repositories]
        if len(folded) != len(set(folded)):
            raise ContractError(
                "docs/ESTATE.md contains case-folding repository collisions"
            )
        return repositories

    def staged_blob_errors(self) -> list[str]:
        """Validate committed/index bytes before checkout normalization masks them.

        GitHub's Contents/Git Data APIs can commit CRLF blobs directly.  An
        ``eol=lf`` checkout then presents LF worktree bytes while the PR still
        contains CRLF, so worktree-only validation is insufficient.  The index
        is the exact candidate tree in CI and the next committed tree locally.
        """
        if not (self.root / ".git").exists():
            return []
        listing = subprocess.run(
            ["git", "ls-files", "-z", "--", COMMENTS_REL.as_posix()],
            cwd=self.root,
            capture_output=True,
            check=False,
        )
        if listing.returncode != 0:
            return ["owner-comment blobs: git ls-files failed"]

        errors: list[str] = []
        for encoded in listing.stdout.split(b"\0"):
            if not encoded:
                continue
            path_text = encoded.decode("utf-8", errors="strict")
            shown = subprocess.run(
                ["git", "show", f":{path_text}"],
                cwd=self.root,
                capture_output=True,
                check=False,
            )
            if shown.returncode != 0:
                errors.append(f"{path_text}: cannot read staged blob")
                continue
            raw = shown.stdout
            if b"\r" in raw:
                errors.append(
                    f"{path_text}: staged blob contains CR bytes; committed "
                    "owner-comment files must use LF"
                )
            if not path_text.endswith(".json"):
                continue
            if path_text == (COMMENTS_REL / "record.schema.json").as_posix():
                if hashlib.sha256(raw).hexdigest() != SCHEMA_SHA256:
                    errors.append(
                        f"{path_text}: staged schema differs from the executable "
                        "contract"
                    )
                continue
            try:
                data = _decode_json(raw)
            except Exception as exc:
                errors.append(f"{path_text}: invalid staged JSON ({exc})")
                continue
            if raw != _json_bytes(data):
                errors.append(
                    f"{path_text}: staged JSON blob is not canonical; the Git "
                    "object, not only checkout bytes, must be canonical"
                )
        return errors

    def scan(self) -> tuple[list[Record], list[str]]:
        canonical = set(self.repositories())
        records: list[Record] = []
        errors: list[str] = []
        seen_ids: dict[str, Path] = {}
        if not self.comments.exists():
            return [], []
        if self.comments.is_symlink() or not self.comments.is_dir():
            return [], [
                "docs/owner-comments: must be a real directory, not a symlink"
            ]

        candidates: list[Path] = []
        for child in sorted(self.comments.iterdir()):
            if child.name in {"README.md", "index.json", "record.schema.json"}:
                if child.is_symlink() or not child.is_file():
                    errors.append(
                        f"{child.relative_to(self.root).as_posix()}: must be a "
                        "regular file, not a symlink"
                    )
                continue
            if child.name not in canonical:
                errors.append(
                    f"{child.relative_to(self.root).as_posix()}: path is not part "
                    "of the closed owner-comment storage contract"
                )
                continue
            if child.is_symlink() or not child.is_dir():
                errors.append(
                    f"{child.relative_to(self.root).as_posix()}: repository path "
                    "must be a real directory, not a symlink"
                )
                continue
            for entry in sorted(child.iterdir()):
                if entry.name == "README.md":
                    if entry.is_symlink() or not entry.is_file():
                        errors.append(
                            f"{entry.relative_to(self.root).as_posix()}: must be "
                            "a regular file, not a symlink"
                        )
                elif entry.name == "consumed":
                    if entry.is_symlink() or not entry.is_dir():
                        errors.append(
                            f"{entry.relative_to(self.root).as_posix()}: consumed "
                            "must be a real directory, not a symlink"
                        )
                        continue
                    for history in sorted(entry.iterdir()):
                        if (
                            history.is_symlink()
                            or not history.is_file()
                            or history.suffix != ".json"
                        ):
                            errors.append(
                                f"{history.relative_to(self.root).as_posix()}: "
                                "only regular lowercase .json records are allowed "
                                "under consumed/"
                            )
                        else:
                            candidates.append(history)
                elif (
                    entry.is_symlink()
                    or not entry.is_file()
                    or entry.suffix != ".json"
                ):
                    errors.append(
                        f"{entry.relative_to(self.root).as_posix()}: only README.md, "
                        "consumed/, and regular lowercase .json records are allowed "
                        "under a repository index"
                    )
                else:
                    candidates.append(entry)

        for candidate in sorted(candidates):
            rel = candidate.relative_to(self.comments)
            repository = rel.parts[0]
            try:
                data, raw = _load_json(candidate)
            except Exception as exc:
                errors.append(f"{rel.as_posix()}: invalid JSON ({exc})")
                continue
            record_errors = validate_record(data, relative_path=rel)
            if raw != _json_bytes(data):
                record_errors.append(
                    f"{rel.as_posix()}: record JSON is not canonical; use sorted "
                    "keys, two-space indentation, UTF-8, and one final newline"
                )
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
        return records, errors

    def _merge_base(self) -> tuple[str | None, list[str]]:
        if not (self.root / ".git").exists():
            return None, []  # isolated contract tests, not a repository gate
        branch = os.environ.get("GITHUB_BASE_REF") or "main"
        for candidate in (f"origin/{branch}", branch):
            result = subprocess.run(
                ["git", "merge-base", candidate, "HEAD"],
                cwd=self.root,
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip(), []
        return None, [
            "owner-comment lifecycle: cannot establish merge base with "
            f"origin/{branch} or {branch}"
        ]

    def _base_records(self) -> tuple[list[Record] | None, list[str]]:
        base, errors = self._merge_base()
        if base is None:
            # ``None`` means lifecycle comparison is unavailable (the focused
            # unit-test store is intentionally not a Git repository, or Git
            # could not establish a trustworthy base).  An empty list, by
            # contrast, is a real Git base containing no comment records.
            return None, errors
        listing = subprocess.run(
            [
                "git", "ls-tree", "-r", "--name-only", "-z", base, "--",
                COMMENTS_REL.as_posix(),
            ],
            cwd=self.root,
            capture_output=True,
            check=False,
        )
        if listing.returncode != 0:
            return [], ["owner-comment lifecycle: git ls-tree failed at merge base"]

        records: list[Record] = []
        seen: set[str] = set()
        prefix = COMMENTS_REL.as_posix() + "/"
        for encoded in listing.stdout.split(b"\0"):
            if not encoded:
                continue
            path_text = encoded.decode("utf-8", errors="strict")
            if not path_text.startswith(prefix):
                continue
            relative = Path(path_text[len(prefix):])
            is_record = (
                len(relative.parts) == 2 and relative.suffix == ".json"
            ) or (
                len(relative.parts) == 3
                and relative.parts[1] == "consumed"
                and relative.suffix == ".json"
            )
            if not is_record:
                continue
            shown = subprocess.run(
                ["git", "show", f"{base}:{path_text}"],
                cwd=self.root,
                capture_output=True,
                check=False,
            )
            if shown.returncode != 0:
                errors.append(f"{path_text}: cannot read merge-base record")
                continue
            try:
                data = _decode_json(shown.stdout)
            except Exception as exc:
                errors.append(f"{path_text}: invalid merge-base JSON ({exc})")
                continue
            record_errors = validate_record(data, relative_path=relative)
            if shown.stdout != _json_bytes(data):
                record_errors.append(f"{path_text}: merge-base JSON is not canonical")
            if record_errors:
                errors.extend(record_errors)
                continue
            comment_id = str(data["id"])
            if comment_id in seen:
                errors.append(f"{path_text}: duplicate merge-base id {comment_id!r}")
                continue
            seen.add(comment_id)
            records.append(Record(path=relative, data=data))
        return records, errors

    def lifecycle_errors(self, current: list[Record]) -> list[str]:
        """Enforce append-only records and the sole active→consumed mutation."""
        base, errors = self._base_records()
        if base is None:
            return errors
        if errors:
            return errors
        old_by_id = {record.comment_id: record for record in base}
        new_by_id = {record.comment_id: record for record in current}

        for comment_id, old in old_by_id.items():
            new = new_by_id.get(comment_id)
            if new is None:
                errors.append(
                    f"owner-comment lifecycle: {comment_id} was deleted; records "
                    "must be preserved"
                )
                continue
            if old.state == "consumed":
                if new.path != old.path or new.data != old.data:
                    errors.append(
                        f"owner-comment lifecycle: consumed record {comment_id} "
                        "is immutable"
                    )
                continue
            if new.state == "unconsumed":
                if new.path != old.path or new.data != old.data:
                    errors.append(
                        f"owner-comment lifecycle: active record {comment_id} may "
                        "not be edited or renamed"
                    )
                continue

            expected_path = (
                Path(old.repository) / "consumed" / f"{comment_id}.json"
            )
            preserved = all(
                new.data.get(key) == value
                for key, value in old.data.items()
                if key != "state"
            )
            if (
                new.path != expected_path
                or new.data.get("state") != "consumed"
                or set(new.data) != set(old.data) | {"consumption"}
                or not preserved
            ):
                errors.append(
                    f"owner-comment lifecycle: {comment_id} may change only by "
                    "moving to consumed/, changing state, and adding consumption"
                )

        for comment_id, new in new_by_id.items():
            if comment_id in old_by_id:
                continue
            expected_path = Path(new.repository) / f"{comment_id}.json"
            if new.state != "unconsumed" or new.path != expected_path:
                errors.append(
                    f"owner-comment lifecycle: new record {comment_id} must be "
                    "added unconsumed at its canonical repository path"
                )
        return errors

    def _by_repository(self, records: list[Record]) -> dict[str, list[Record]]:
        result = {repository: [] for repository in self.repositories()}
        for record in records:
            if record.repository in result:
                result[record.repository].append(record)
        for values in result.values():
            values.sort(
                key=lambda item: (
                    _parse_timestamp(item.data["created_at"]),
                    item.comment_id,
                )
            )
        return result

    def render_root_index(self, records: list[Record]) -> bytes:
        grouped = self._by_repository(records)
        rows = []
        for repository in self.repositories():
            active = [r for r in grouped[repository] if r.state == "unconsumed"]
            consumed = [r for r in grouped[repository] if r.state == "consumed"]
            latest_active = max(
                active,
                key=lambda item: _parse_timestamp(item.data["created_at"]),
                default=None,
            )
            latest_consumed = max(
                consumed,
                key=lambda item: _parse_timestamp(item.data["consumption"]["at"]),
                default=None,
            )
            rows.append(
                {
                    "repository": repository,
                    "index": f"docs/owner-comments/{repository}/README.md",
                    "unconsumed_count": len(active),
                    "consumed_count": len(consumed),
                    "latest_unconsumed_at": (
                        latest_active.data["created_at"] if latest_active else None
                    ),
                    "latest_consumed_at": (
                        latest_consumed.data["consumption"]["at"]
                        if latest_consumed
                        else None
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
            key=lambda item: (
                _parse_timestamp(item.data["created_at"]),
                item.comment_id,
            ),
        )
        consumed = sorted(
            (r for r in records if r.repository == repository and r.state == "consumed"),
            key=lambda item: (
                _parse_timestamp(item.data["consumption"]["at"]),
                item.comment_id,
            ),
        )
        lines = [
            f"# Owner comments — `{repository}`",
            "",
            "> **Status:** `living-ledger`",
            ">",
            "> **Generated index.** Run `python3 tools/owner_comments.py reindex`;",
            "> do not hand-edit this file. **Every record and all of its metadata",
            "> are public.** Read the [storage and privacy contract](../README.md)",
            "> before adding feedback. JSON preserves the owner's wording verbatim.",
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
        with self.mutation_lock():
            return self._check_locked()

    def _check_locked(self) -> list[str]:
        records, errors = self.scan()
        if errors:
            return errors
        for name in ("README.md", "record.schema.json"):
            path = self.comments / name
            relative = path.relative_to(self.root).as_posix()
            if path.is_symlink() or not path.is_file():
                errors.append(
                    f"{relative}: missing required regular contract file"
                )
            elif name == "record.schema.json":
                actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
                if actual_hash != SCHEMA_SHA256:
                    errors.append(
                        f"{relative}: schema artifact differs from the executable "
                        "contract; update both deliberately"
                    )
        for path, expected in self.expected_indexes(records).items():
            relative = path.relative_to(self.root).as_posix()
            if not path.is_file():
                errors.append(f"{relative}: missing generated index")
            elif path.read_bytes() != expected:
                errors.append(f"{relative}: generated index is stale; run reindex")
        errors.extend(self.staged_blob_errors())
        errors.extend(self.lifecycle_errors(records))
        return errors

    def reindex(self) -> None:
        with self.mutation_lock():
            self._reindex_locked()

    def _reindex_locked(self) -> None:
        records, errors = self.scan()
        if errors:
            raise ContractError("\n".join(errors))
        changes: dict[Path, bytes] = {}
        for path, content in self.expected_indexes(records).items():
            self._assert_safe_target(path)
            if not path.is_file() or path.read_bytes() != content:
                changes[path] = content
        if not changes:
            return
        # A standalone reindex is one exception-safe projection transaction,
        # just like the
        # index half of consume: interruption on any write restores every
        # already-written index instead of leaving root and repository views
        # disagreeing.  consume adds an outer record snapshot around this.
        with self.rollback_snapshot(tuple(changes)):
            for path, content in changes.items():
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
        if not _valid_comment_id(comment_id):
            raise ContractError("unsafe or invalid comment id")
        timestamp_error = _utc_timestamp(consumed_at, "consumption.at")
        if timestamp_error:
            raise ContractError(timestamp_error)
        if (
            not isinstance(actor, str)
            or not actor.strip()
            or not isinstance(evidence, str)
            or not evidence.strip()
        ):
            raise ContractError("actor and evidence are required for consumption")

        with self.mutation_lock():
            return self._consume_locked(
                repository,
                comment_id,
                consumed_at=consumed_at,
                actor=actor,
                evidence=evidence,
            )

    def _consume_locked(
        self,
        repository: str,
        comment_id: str,
        *,
        consumed_at: str,
        actor: str,
        evidence: str,
    ) -> Path:

        preflight_errors = self._check_locked()
        if preflight_errors:
            raise ContractError(
                "owner-comment tree is not clean before consume:\n"
                + "\n".join(preflight_errors)
            )

        source = self.comments / repository / f"{comment_id}.json"
        destination = self.comments / repository / "consumed" / f"{comment_id}.json"
        self._assert_safe_target(source)
        self._assert_safe_target(destination)
        if not source.is_file():
            if destination.is_file():
                raise ContractError(f"{comment_id!r} is already consumed")
            raise ContractError(f"unconsumed comment does not exist: {source}")
        if destination.exists():
            raise ContractError(f"consumed destination already exists: {destination}")

        try:
            data, _ = _load_json(source)
        except Exception as exc:
            raise ContractError(f"invalid source record JSON: {exc}") from exc
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

        transaction_paths = (
            source,
            destination,
            self.comments / repository / "README.md",
            self.comments / "index.json",
        )
        with self.rollback_snapshot(transaction_paths):
            source.replace(destination)  # the lifecycle transition is a real move
            _fsync_directory(source.parent)
            _fsync_directory(destination.parent)
            _atomic_write(destination, _json_bytes(updated))
            self._reindex_locked()
            postflight_errors = self._check_locked()
            if postflight_errors:
                raise ContractError(
                    "consume produced an invalid tree:\n"
                    + "\n".join(postflight_errors)
                )
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
