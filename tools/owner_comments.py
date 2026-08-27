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
import errno
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from contextvars import ContextVar
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
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ESTATE_ROW_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|")
MAX_COMMENT_CHARS = 20_000
MAX_CONTEXT_CHARS = 1_000
WINDOWS_RESERVED = {
    "con", "prn", "aux", "nul",
    *(f"com{number}" for number in range(1, 10)),
    *(f"lpt{number}" for number in range(1, 10)),
}
ROOT_RESERVED = {"readme.md", "index.json", "record.schema.json"}
DETACHED_HEAD_REF = "DETACHED"
_ACTIVE_ATOMIC_TEMPORARIES: ContextVar[dict[Path, Path] | None] = ContextVar(
    "owner_comment_atomic_temporaries", default=None
)
_UNSUPPORTED_DIRECTORY_FSYNC_ERRNOS = frozenset(
    {
        errno.EINVAL,
        errno.ENOSYS,
        getattr(errno, "ENOTSUP", errno.EINVAL),
        getattr(errno, "EOPNOTSUPP", errno.EINVAL),
    }
)


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


def _content_state(content: bytes | None) -> dict[str, Any]:
    if content is None:
        return {"exists": False}
    return {
        "exists": True,
        "sha256": hashlib.sha256(content).hexdigest(),
        "size": len(content),
    }


def _path_state(path: Path, *, boundary: Path) -> dict[str, Any] | None:
    """lstat a bounded path without accepting symlinked parent traversal."""
    try:
        relative = path.relative_to(boundary)
    except ValueError:
        return None
    try:
        boundary_metadata = os.lstat(boundary)
    except OSError:
        return None
    if not stat.S_ISDIR(boundary_metadata.st_mode):
        return None
    current = boundary
    components = relative.parts
    for index, component in enumerate(components):
        current /= component
        try:
            metadata = os.lstat(current)
        except FileNotFoundError:
            return _content_state(None)
        except OSError:
            return None
        final = index == len(components) - 1
        if not final:
            if not stat.S_ISDIR(metadata.st_mode):
                return None
            continue
        if not stat.S_ISREG(metadata.st_mode):
            return None
        try:
            return _content_state(current.read_bytes())
        except OSError:
            return None
    return None


def _expected_state_key(state: Any) -> tuple[bool, str, int] | None:
    """Validate and normalize one manifest file-state descriptor."""
    if not isinstance(state, dict) or type(state.get("exists")) is not bool:
        return None
    if state["exists"] is False:
        return (False, "", 0) if set(state) == {"exists"} else None
    if set(state) != {"exists", "sha256", "size"}:
        return None
    sha256 = state.get("sha256")
    size = state.get("size")
    if (
        not isinstance(sha256, str)
        or not SHA256_RE.fullmatch(sha256)
        or type(size) is not int
        or size < 0
    ):
        return None
    return (True, sha256, size)


def _set_file_mode(path: Path, descriptor: int, mode: int) -> None:
    """Set replacement permissions with a Windows-compatible path fallback."""
    fchmod = getattr(os, "fchmod", None)
    if callable(fchmod):
        try:
            fchmod(descriptor, mode)
        except (AttributeError, NotImplementedError):
            pass
        except OSError as exc:
            if exc.errno not in {
                errno.ENOSYS,
                getattr(errno, "ENOTSUP", errno.ENOSYS),
                getattr(errno, "EOPNOTSUPP", errno.ENOSYS),
            }:
                raise
        else:
            return
    os.chmod(path, mode)


def _is_windows() -> bool:
    """Return the platform decision through a small testable seam."""
    return os.name == "nt"


def _windows_readonly_mode(mode: int) -> bool:
    return _is_windows() and not bool(mode & stat.S_IWRITE)


def _clear_windows_readonly(
    path: Path, *, missing_ok: bool = False
) -> int | None:
    """Make one regular Windows path writable and return its prior mode."""
    if not _is_windows():
        return None
    try:
        metadata = os.lstat(path)
    except FileNotFoundError:
        if missing_ok:
            return None
        raise
    if not stat.S_ISREG(metadata.st_mode):
        return None
    mode = stat.S_IMODE(metadata.st_mode)
    if mode & stat.S_IWRITE:
        return None
    os.chmod(path, mode | stat.S_IWRITE)
    return mode


def _restore_mode_without_masking(path: Path, mode: int | None) -> None:
    """Best-effort mode restoration while another exception is active."""
    if mode is None:
        return
    try:
        metadata = os.lstat(path)
        if stat.S_ISREG(metadata.st_mode):
            os.chmod(path, mode)
    except OSError:
        pass


def _unlink_windows_compatible(path: Path, *, missing_ok: bool = False) -> None:
    """Unlink a path after clearing the Windows read-only attribute."""
    prior_mode = _clear_windows_readonly(path, missing_ok=missing_ok)
    try:
        path.unlink()
    except FileNotFoundError:
        if missing_ok:
            return
        raise
    except BaseException:
        _restore_mode_without_masking(path, prior_mode)
        raise


def _apply_windows_readonly_after_replace(path: Path, mode: int) -> None:
    """Publish Windows read-only state only after replacement succeeds."""
    if not _windows_readonly_mode(mode):
        return
    _clear_windows_readonly(path)
    # Keep a writable descriptor while applying the attribute so the metadata
    # change itself can be committed before this operation reports success.
    with path.open("r+b") as handle:
        os.chmod(path, mode)
        os.fsync(handle.fileno())


def _remove_tree_best_effort(path: Path) -> None:
    """Remove journal scratch, first clearing Windows read-only artifacts."""
    if _is_windows() and path.is_dir() and not path.is_symlink():
        for candidate in sorted(path.rglob("*"), reverse=True):
            try:
                _clear_windows_readonly(candidate, missing_ok=True)
            except OSError:
                pass
    shutil.rmtree(path, ignore_errors=True)


def _atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        target_metadata = os.lstat(path)
    except FileNotFoundError:
        target_mode = 0o644
    else:
        if not stat.S_ISREG(target_metadata.st_mode):
            raise ContractError(f"atomic-write target must be a regular file: {path}")
        target_mode = stat.S_IMODE(target_metadata.st_mode)
    active_temporaries = _ACTIVE_ATOMIC_TEMPORARIES.get()
    temporary = (
        active_temporaries.get(path.absolute())
        if active_temporaries is not None
        else None
    )
    if temporary is None:
        fd, temporary_name = tempfile.mkstemp(
            prefix=f".{path.name}.", dir=path.parent
        )
        temporary = Path(temporary_name)
    else:
        try:
            fd = os.open(
                temporary,
                os.O_WRONLY | os.O_CREAT | os.O_EXCL,
                0o600,
            )
        except FileExistsError as exc:
            raise ContractError(
                f"transaction atomic temporary already exists: {temporary}"
            ) from exc
    windows_readonly = _windows_readonly_mode(target_mode)
    cleared_target_mode: int | None = None
    replaced = False
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            # POSIX replacement modes remain atomic. Windows read-only state
            # must wait until after MoveFileEx has replaced the old path.
            if not windows_readonly:
                _set_file_mode(temporary, handle.fileno(), target_mode)
            os.fsync(handle.fileno())
        if windows_readonly:
            cleared_target_mode = _clear_windows_readonly(path)
        os.replace(temporary, path)
        replaced = True
        _apply_windows_readonly_after_replace(path, target_mode)
        _fsync_directory(path.parent)
    except BaseException:
        _restore_mode_without_masking(
            path, target_mode if replaced and windows_readonly else cleared_target_mode
        )
        try:
            _unlink_windows_compatible(temporary, missing_ok=True)
        except BaseException:
            # Cleanup must never replace the write/replace/fsync failure that
            # made this rollback path necessary.
            pass
        raise


def _fsync_directory(path: Path) -> None:
    """Durably sync a directory or ignore an explicitly unsupported platform."""
    if _is_windows():
        # The Windows CRT cannot open a directory with the ordinary os.open
        # flags used here, so there is no descriptor that os.fsync can commit.
        # Keep this platform decision explicit: EACCES and I/O failures on
        # platforms that do support directory descriptors must still surface.
        return
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as exc:
        if exc.errno in _UNSUPPORTED_DIRECTORY_FSYNC_ERRNOS:
            return
        raise
    try:
        os.fsync(descriptor)
    except OSError as exc:
        if exc.errno not in _UNSUPPORTED_DIRECTORY_FSYNC_ERRNOS:
            raise
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
        """Return the exact symbolic HEAD/OID/index rollback identity."""
        inside = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )
        if inside.returncode != 0 or inside.stdout.strip() != "true":
            return {"head": None, "head_ref": None, "index_tree": None}

        head_result = subprocess.run(
            ["git", "rev-parse", "--verify", "HEAD"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )
        head = head_result.stdout.strip() if head_result.returncode == 0 else None
        symbolic_result = subprocess.run(
            ["git", "symbolic-ref", "--quiet", "HEAD"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )
        if symbolic_result.returncode == 0:
            head_ref = symbolic_result.stdout.strip()
            ref_check = subprocess.run(
                ["git", "check-ref-format", head_ref],
                cwd=self.root,
                capture_output=True,
                text=True,
                check=False,
            )
            if not head_ref.startswith("refs/heads/") or ref_check.returncode != 0:
                raise ContractError("Git returned an invalid symbolic HEAD ref")
        elif symbolic_result.returncode == 1 and head is not None:
            head_ref = DETACHED_HEAD_REF
        else:
            detail = symbolic_result.stderr.strip() or "cannot identify symbolic HEAD"
            raise ContractError(
                f"cannot identify owner-comment transaction Git HEAD: {detail}"
            )
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
        return {"head": head, "head_ref": head_ref, "index_tree": index_tree}

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
        self, expected_phases: tuple[dict[Path, bytes | None], ...]
    ) -> dict[str, Any]:
        if not expected_phases or not expected_phases[0]:
            raise ContractError("transaction must declare at least one target phase")
        paths = tuple(expected_phases[0])
        if any(set(phase) != set(paths) for phase in expected_phases):
            raise ContractError("transaction phases must cover the same target paths")

        entries = []
        initial_contents: dict[Path, bytes | None] = {}
        for number, path in enumerate(paths):
            try:
                relative = path.relative_to(self.root)
            except ValueError as exc:
                raise ContractError(
                    f"transaction path is outside repository root: {path}"
                ) from exc
            self._assert_safe_target(path)
            existed = path.exists()
            if existed and not path.is_file():
                raise ContractError(
                    f"transaction target must be a regular file or absent: {path}"
                )
            initial_content = path.read_bytes() if existed else None
            initial_contents[path] = initial_content
            entries.append(
                {
                    "path": relative.as_posix(),
                    "existed": existed,
                    "backup": str(number) if existed else None,
                }
            )

        phase_vectors: list[list[dict[str, Any]]] = []
        seen_vectors: set[tuple[tuple[bool, str, int], ...]] = set()

        def add_phase(contents: dict[Path, bytes | None]) -> None:
            states = [_content_state(contents[path]) for path in paths]
            keys = tuple(_expected_state_key(state) for state in states)
            assert all(key is not None for key in keys)
            normalized = tuple(key for key in keys if key is not None)
            if normalized not in seen_vectors:
                seen_vectors.add(normalized)
                phase_vectors.append(states)

        add_phase(initial_contents)
        for phase in expected_phases:
            add_phase(phase)

        return {
            "schema_version": 5,
            "state": "prepared",
            "root": str(self.root),
            "git_identity": self._git_identity(),
            "entries": entries,
            "expected_phases": phase_vectors,
            "recovery": None,
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
            "expected_phases",
            "recovery",
        }:
            raise ContractError(
                f"owner-comment transaction manifest has unknown fields: {manifest_path}"
            )
        if data.get("schema_version") != 5 or data.get("state") not in {
            "prepared",
            "recovering",
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
        if not isinstance(identity, dict) or set(identity) != {
            "head",
            "head_ref",
            "index_tree",
        }:
            raise ContractError(
                f"owner-comment transaction Git identity is invalid: {manifest_path}"
            )
        oid = re.compile(r"^[0-9a-f]{40,64}$")
        head = identity.get("head")
        head_ref = identity.get("head_ref")
        index_tree = identity.get("index_tree")
        head_valid = head is None or (
            isinstance(head, str) and bool(oid.fullmatch(head))
        )
        tree_valid = index_tree is None or (
            isinstance(index_tree, str) and bool(oid.fullmatch(index_tree))
        )
        symbolic_valid = False
        if isinstance(head_ref, str) and head_ref != DETACHED_HEAD_REF:
            ref_check = subprocess.run(
                ["git", "check-ref-format", head_ref],
                cwd=self.root,
                capture_output=True,
                text=True,
                check=False,
            )
            symbolic_valid = (
                head_ref.startswith("refs/heads/") and ref_check.returncode == 0
            )
        valid_identity = (
            head_valid
            and tree_valid
            and (
                (head is None and head_ref is None and index_tree is None)
                or (index_tree is not None and symbolic_valid)
                or (
                    head is not None
                    and index_tree is not None
                    and head_ref == DETACHED_HEAD_REF
                )
            )
        )
        if not valid_identity:
            raise ContractError(
                f"owner-comment transaction Git identity is invalid: {manifest_path}"
            )
        if not isinstance(data.get("entries"), list):
            raise ContractError(
                f"owner-comment transaction manifest entries are invalid: {manifest_path}"
            )
        expected_phases = data.get("expected_phases")
        if not isinstance(expected_phases, list) or not expected_phases:
            raise ContractError(
                f"owner-comment transaction phases are invalid: {manifest_path}"
            )
        phase_keys: list[tuple[tuple[bool, str, int], ...]] = []
        for phase in expected_phases:
            if not isinstance(phase, list) or len(phase) != len(data["entries"]):
                raise ContractError(
                    f"owner-comment transaction phases are invalid: {manifest_path}"
                )
            keys = tuple(_expected_state_key(state) for state in phase)
            if any(key is None for key in keys):
                raise ContractError(
                    f"owner-comment transaction phases are invalid: {manifest_path}"
                )
            phase_keys.append(tuple(key for key in keys if key is not None))
        if len(phase_keys) != len(set(phase_keys)):
            raise ContractError(
                f"owner-comment transaction phases are duplicated: {manifest_path}"
            )
        recovery = data.get("recovery")
        if data["state"] == "recovering":
            if (
                not isinstance(recovery, dict)
                or set(recovery) != {"phase", "cursor"}
                or type(recovery.get("phase")) is not int
                or type(recovery.get("cursor")) is not int
                or not 0 <= recovery["phase"] < len(phase_keys)
                or not 0 <= recovery["cursor"] <= len(data["entries"])
            ):
                raise ContractError(
                    f"owner-comment transaction recovery cursor is invalid: "
                    f"{manifest_path}"
                )
        elif recovery is not None:
            raise ContractError(
                f"owner-comment transaction recovery cursor is invalid: {manifest_path}"
            )

        seen: set[Path] = set()
        initial_keys: list[tuple[bool, str, int]] = []
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
            if existed:
                if not isinstance(backup_name, str) or not backup_name.isdigit():
                    raise ContractError(
                        f"owner-comment transaction backup is invalid: {manifest_path}"
                    )
                backup = backup_root / backup_name
                if (
                    data["state"] in {"prepared", "recovering"}
                    and (backup.is_symlink() or not backup.is_file())
                ):
                    raise ContractError(
                        f"owner-comment transaction backup is missing: {backup}"
                    )
                if data["state"] in {"prepared", "recovering"}:
                    backup_state = _path_state(backup, boundary=backup_root)
                    backup_key = _expected_state_key(backup_state)
                    if backup_key is None:
                        raise ContractError(
                            f"owner-comment transaction backup is invalid: {backup}"
                        )
                    initial_keys.append(backup_key)
                else:
                    initial_keys.append(phase_keys[0][len(initial_keys)])
            elif backup_name is not None:
                raise ContractError(
                    f"owner-comment transaction has a backup for an absent path: "
                    f"{manifest_path}"
                )
            else:
                initial_keys.append((False, "", 0))
        if data["state"] in {"prepared", "recovering"} and tuple(
            initial_keys
        ) != phase_keys[0]:
            raise ContractError(
                f"owner-comment transaction initial phase is invalid: {manifest_path}"
            )
        return data

    def _current_target_vector(
        self, manifest: dict[str, Any]
    ) -> tuple[tuple[bool, str, int] | None, ...]:
        return tuple(
            _expected_state_key(
                _path_state(
                    self.root / entry["path"], boundary=self.comments
                )
            )
            for entry in manifest["entries"]
        )

    @staticmethod
    def _phase_vectors(
        manifest: dict[str, Any]
    ) -> list[tuple[tuple[bool, str, int] | None, ...]]:
        return [
            tuple(_expected_state_key(state) for state in phase)
            for phase in manifest["expected_phases"]
        ]

    def _prepared_phase_index(self, manifest: dict[str, Any]) -> int | None:
        current = self._current_target_vector(manifest)
        if any(state is None for state in current):
            return None
        try:
            return self._phase_vectors(manifest).index(current)
        except ValueError:
            return None

    def _recovery_vectors(
        self, manifest: dict[str, Any]
    ) -> tuple[
        tuple[tuple[bool, str, int] | None, ...],
        tuple[tuple[bool, str, int] | None, ...],
    ]:
        phases = self._phase_vectors(manifest)
        recovery = manifest["recovery"]
        cursor = recovery["cursor"]
        origin = phases[recovery["phase"]]
        initial = phases[0]
        before = initial[:cursor] + origin[cursor:]
        after_cursor = min(cursor + 1, len(initial))
        after = initial[:after_cursor] + origin[after_cursor:]
        return before, after

    def _recovery_status(self, manifest: dict[str, Any]) -> str | None:
        current = self._current_target_vector(manifest)
        if any(state is None for state in current):
            return None
        before, after = self._recovery_vectors(manifest)
        if current == before:
            return "before"
        if current == after:
            return "after"
        return None

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

    @staticmethod
    def _transaction_id(backup_root: Path) -> str:
        return backup_root.name.removeprefix("txn-")

    def _atomic_temporary_path(
        self, backup_root: Path, entry: dict[str, Any], number: int
    ) -> Path:
        target = self.root / entry["path"]
        return target.with_name(
            f".{target.name}.atomic-{self._transaction_id(backup_root)}-{number}"
        )

    def _recovery_temporary_path(
        self, backup_root: Path, entry: dict[str, Any], number: int
    ) -> Path:
        target = self.root / entry["path"]
        return target.with_name(
            f".{target.name}.recover-{self._transaction_id(backup_root)}-{number}"
        )

    def _atomic_temporaries(
        self, backup_root: Path, manifest: dict[str, Any]
    ) -> dict[Path, Path]:
        """Map atomically-written targets to journal-owned deterministic temps."""
        phases = self._phase_vectors(manifest)
        initial = phases[0]
        final = phases[-1]
        result: dict[Path, Path] = {}
        for number, entry in enumerate(manifest["entries"]):
            if final[number][0] and final[number] != initial[number]:
                target = (self.root / entry["path"]).absolute()
                result[target] = self._atomic_temporary_path(
                    backup_root, entry, number
                )
        return result

    def _temporary_specs(
        self, backup_root: Path, manifest: dict[str, Any]
    ) -> list[tuple[Path, tuple[bool, str, int], str]]:
        """Return every deterministic scratch path and its only valid content."""
        phases = self._phase_vectors(manifest)
        initial = phases[0]
        final = phases[-1]
        specs: list[tuple[Path, tuple[bool, str, int], str]] = []
        for number, entry in enumerate(manifest["entries"]):
            if final[number][0] and final[number] != initial[number]:
                specs.append(
                    (
                        self._atomic_temporary_path(backup_root, entry, number),
                        final[number],
                        f"atomic-{number}",
                    )
                )
            if entry["existed"]:
                specs.append(
                    (
                        self._recovery_temporary_path(backup_root, entry, number),
                        initial[number],
                        f"recovery-{number}",
                    )
                )
        return specs

    def _preserve_unexpected_temporary(
        self, backup_root: Path, temporary: Path, label: str
    ) -> Path:
        """Move unrecognized scratch bytes into the journal before quarantine."""
        preserved = backup_root / f"unexpected-{label}"
        suffix = 0
        while preserved.exists() or preserved.is_symlink():
            suffix += 1
            preserved = backup_root / f"unexpected-{label}-source-{suffix}"
        try:
            os.replace(temporary, preserved)
        except OSError:
            # A linked worktree can put the Git journal on another filesystem.
            # Copy regular bytes durably before removing their checkout name.
            metadata = os.lstat(temporary)
            if not stat.S_ISREG(metadata.st_mode):
                raise ContractError(
                    f"unsafe transaction temporary cannot be preserved: {temporary}"
                )
            shutil.copy2(temporary, preserved)
            with preserved.open("rb") as handle:
                os.fsync(handle.fileno())
            _fsync_directory(preserved.parent)
            _unlink_windows_compatible(temporary)
            _fsync_directory(temporary.parent)
        else:
            metadata = os.lstat(preserved)
            if stat.S_ISREG(metadata.st_mode):
                with preserved.open("rb") as handle:
                    os.fsync(handle.fileno())
            _fsync_directory(preserved.parent)
            _fsync_directory(temporary.parent)
        return preserved

    def _reconcile_preserved_temporaries(
        self, backup_root: Path, manifest: dict[str, Any]
    ) -> list[Path]:
        """Finish an interrupted cross-filesystem preservation idempotently."""
        residues: list[Path] = []
        recognized: set[Path] = set()
        for temporary, _, label in self._temporary_specs(backup_root, manifest):
            base = backup_root / f"unexpected-{label}"
            if not (base.exists() or base.is_symlink()):
                continue
            candidates = [base, *sorted(backup_root.glob(f"{base.name}-source-*"))]
            recognized.update(candidates)
            residues.extend(candidates)
            candidate_states: dict[Path, tuple[bool, str, int] | None] = {}
            for candidate in candidates:
                state = _expected_state_key(
                    _path_state(candidate, boundary=backup_root)
                )
                candidate_states[candidate] = state
                if state is not None and state[0]:
                    # Preservation may have died immediately after rename/copy.
                    # Make every recognized regular artifact durable before an
                    # absent-source fast path or quarantine can proceed.
                    with candidate.open("rb") as handle:
                        os.fsync(handle.fileno())
            _fsync_directory(backup_root)
            actual = _expected_state_key(
                _path_state(temporary, boundary=self.comments)
            )
            if actual == (False, "", 0):
                continue
            matching = [
                path
                for path in candidates
                if actual is not None
                and actual == candidate_states[path]
            ]
            if matching:
                # The journal already owns these exact bytes, but a prior
                # process may have died between copy2 and fsync. Make one
                # matching copy and its directory durable before deleting the
                # deterministic checkout duplicate.
                preserved = matching[0]
                with preserved.open("rb") as handle:
                    os.fsync(handle.fileno())
                _fsync_directory(preserved.parent)
                if actual != _expected_state_key(
                    _path_state(preserved, boundary=backup_root)
                ):
                    raise ContractError(
                        f"preserved transaction temporary changed: {preserved}"
                    )
                _unlink_windows_compatible(temporary)
                _fsync_directory(temporary.parent)
                continue
            # The source changed again (or has an unsafe type). Preserve it as
            # another uniquely named journal artifact before quarantine. If a
            # process dies after a cross-device copy, the next pass recognizes
            # that duplicate by hash and completes the unlink above.
            residues.append(
                self._preserve_unexpected_temporary(
                    backup_root, temporary, label
                )
            )
        unknown = [
            path
            for path in sorted(backup_root.glob("unexpected-*"))
            if path not in recognized and path not in residues
        ]
        for path in unknown:
            try:
                metadata = os.lstat(path)
            except OSError:
                continue
            if stat.S_ISREG(metadata.st_mode):
                with path.open("rb") as handle:
                    os.fsync(handle.fileno())
            elif stat.S_ISDIR(metadata.st_mode):
                _fsync_directory(path)
        if unknown:
            _fsync_directory(backup_root)
        residues.extend(unknown)
        return residues

    def _cleanup_transaction_temporaries(
        self, backup_root: Path, manifest: dict[str, Any]
    ) -> None:
        """Scavenge only exact journal-owned scratch, preserving mismatches."""
        preserved_residue = self._reconcile_preserved_temporaries(
            backup_root, manifest
        )
        if preserved_residue:
            raise ContractError(
                "previous recovery already preserved unexpected transaction "
                "temporary bytes: "
                + ", ".join(path.name for path in preserved_residue)
            )
        unexpected: list[str] = []
        for temporary, expected, label in self._temporary_specs(
            backup_root, manifest
        ):
            state = _path_state(temporary, boundary=self.comments)
            actual = _expected_state_key(state)
            if actual == (False, "", 0):
                continue
            if actual == expected:
                _unlink_windows_compatible(temporary)
                _fsync_directory(temporary.parent)
                continue
            preserved = self._preserve_unexpected_temporary(
                backup_root, temporary, label
            )
            unexpected.append(f"{temporary} -> {preserved.name}")
        if unexpected:
            raise ContractError(
                "transaction temporary bytes/state changed unexpectedly; preserved "
                + ", ".join(unexpected)
            )

    def _begin_recovery(
        self, backup_root: Path, manifest: dict[str, Any]
    ) -> None:
        phase = self._prepared_phase_index(manifest)
        if phase is None:
            raise ContractError("owner-comment transaction target phase is unexpected")
        manifest["state"] = "recovering"
        manifest["recovery"] = {"phase": phase, "cursor": 0}
        _write_transaction_manifest(backup_root / "manifest.json", manifest)

    def _restore_entry(
        self, backup_root: Path, entry: dict[str, Any], number: int
    ) -> None:
        target = self.root / entry["path"]
        if entry["existed"]:
            backup = backup_root / entry["backup"]
            backup_mode = stat.S_IMODE(os.lstat(backup).st_mode)
            windows_readonly = _windows_readonly_mode(backup_mode)
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = self._recovery_temporary_path(
                backup_root, entry, number
            )
            created = False
            cleared_target_mode: int | None = None
            replaced = False
            try:
                if temporary.exists() or temporary.is_symlink():
                    raise ContractError(
                        f"recovery temporary path already exists: {temporary}"
                    )
                descriptor = os.open(
                    temporary,
                    os.O_WRONLY | os.O_CREAT | os.O_EXCL,
                    0o600,
                )
                created = True
                with backup.open("rb") as source, os.fdopen(
                    descriptor, "wb"
                ) as destination:
                    shutil.copyfileobj(source, destination)
                    destination.flush()
                    os.fsync(destination.fileno())
                if not windows_readonly:
                    os.chmod(temporary, backup_mode)
                    with temporary.open("rb") as handle:
                        os.fsync(handle.fileno())
                cleared_target_mode = _clear_windows_readonly(
                    target, missing_ok=True
                )
                os.replace(temporary, target)
                replaced = True
                _apply_windows_readonly_after_replace(target, backup_mode)
                _fsync_directory(target.parent)
            except BaseException:
                _restore_mode_without_masking(
                    target,
                    backup_mode
                    if replaced and windows_readonly
                    else cleared_target_mode,
                )
                try:
                    if created and (
                        temporary.is_symlink() or (
                        temporary.exists() and not temporary.is_dir()
                        )
                    ):
                        _unlink_windows_compatible(temporary, missing_ok=True)
                        _fsync_directory(temporary.parent)
                except BaseException:
                    pass
                raise
        elif target.exists() or target.is_symlink():
            if target.is_dir() and not target.is_symlink():
                raise ContractError(
                    f"transaction recovery refuses to delete directory: {target}"
                )
            _unlink_windows_compatible(target)
            _fsync_directory(target.parent)

    def _finish_windows_recovery_mode(
        self, backup_root: Path, entry: dict[str, Any]
    ) -> None:
        """Close the post-replace mode window after an interrupted recovery."""
        if not _is_windows() or not entry["existed"]:
            return
        backup = backup_root / entry["backup"]
        backup_mode = stat.S_IMODE(os.lstat(backup).st_mode)
        _apply_windows_readonly_after_replace(
            self.root / entry["path"], backup_mode
        )

    def _restore_transaction(
        self, backup_root: Path, manifest: dict[str, Any]
    ) -> None:
        """Resume a cursor-pinned recovery without accepting mixed target states."""
        if manifest["state"] == "prepared":
            self._begin_recovery(backup_root, manifest)
        while manifest["recovery"]["cursor"] < len(manifest["entries"]):
            status = self._recovery_status(manifest)
            if status is None:
                raise ContractError(
                    "owner-comment recovery target phase changed unexpectedly"
                )
            cursor = manifest["recovery"]["cursor"]
            if status == "before":
                self._restore_entry(
                    backup_root, manifest["entries"][cursor], cursor
                )
                if self._current_target_vector(manifest) != self._recovery_vectors(
                    manifest
                )[1]:
                    raise ContractError(
                        "owner-comment recovery could not verify restored target"
                    )
            else:
                self._finish_windows_recovery_mode(
                    backup_root, manifest["entries"][cursor]
                )
            manifest["recovery"]["cursor"] = cursor + 1
            _write_transaction_manifest(backup_root / "manifest.json", manifest)

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
            try:
                manifest = self._read_transaction_manifest(backup_root)
            except ContractError as exc:
                quarantine = self._quarantine_transaction(backup_root)
                raise ContractError(
                    "invalid owner-comment recovery journal was quarantined at "
                    f"{quarantine}: {exc}"
                ) from exc
            if manifest is None:
                # ``txn-*`` is published into this root-digested, non-worktree
                # directory only after a durable manifest exists.  Therefore a
                # manifest-less published directory can only be residue from
                # committed cleanup deleting the manifest before the directory.
                _remove_tree_best_effort(backup_root)
                _fsync_directory(transaction_root)
                continue
            try:
                self._cleanup_transaction_temporaries(backup_root, manifest)
            except ContractError as exc:
                quarantine = self._quarantine_transaction(backup_root)
                raise ContractError(
                    "owner-comment transaction temporary mismatch was preserved "
                    f"and quarantined at {quarantine}: {exc}"
                ) from exc
            transactions.append((backup_root, manifest))

        active = [
            item
            for item in transactions
            if item[1]["state"] in {"prepared", "recovering"}
        ]
        if active:
            current_identity = self._git_identity()
            identity_mismatches = [
                backup_root
                for backup_root, manifest in active
                if manifest["git_identity"] != current_identity
            ]
            target_mismatches = {
                backup_root: [entry["path"] for entry in manifest["entries"]]
                for backup_root, manifest in active
                if (
                    self._prepared_phase_index(manifest) is None
                    if manifest["state"] == "prepared"
                    else self._recovery_status(manifest) is None
                )
            }
            multiple_active = len(active) != 1
            if identity_mismatches or target_mismatches or multiple_active:
                quarantined = [
                    self._quarantine_transaction(backup_root)
                    for backup_root, _ in active
                ]
                reasons = []
                if identity_mismatches:
                    reasons.append("Git symbolic HEAD/OID/index tree changed")
                if multiple_active:
                    reasons.append("multiple overlapping recovery journals exist")
                if target_mismatches:
                    changed = sorted(
                        {
                            path
                            for paths in target_mismatches.values()
                            for path in paths
                        }
                    )
                    reasons.append(
                        "target bytes/state changed at " + ", ".join(changed)
                    )
                raise ContractError(
                    "prepared owner-comment transaction cannot be recovered "
                    "safely (" + "; ".join(reasons) + "); the current checkout "
                    "was not changed and the stale recovery data was quarantined at "
                    + ", ".join(str(path) for path in quarantined)
                )

        for backup_root, manifest in transactions:
            if manifest["state"] in {"prepared", "recovering"}:
                self._restore_transaction(backup_root, manifest)
                manifest["state"] = "committed"
                manifest["recovery"] = None
                _write_transaction_manifest(
                    backup_root / "manifest.json", manifest
                )
            _remove_tree_best_effort(backup_root)
            _fsync_directory(transaction_root)

    @contextmanager
    def rollback_snapshot(
        self, expected_phases: tuple[dict[Path, bytes | None], ...]
    ):
        """Restore files on exceptions and journal recovery across process death.

        Backups are independent files on the repository filesystem, so an
        in-place post-crash target edit cannot mutate the recovery copy and a
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
        manifest = self._transaction_manifest(expected_phases)
        prepared = False
        try:
            for entry in manifest["entries"]:
                if entry["existed"]:
                    path = self.root / entry["path"]
                    backup = backup_root / entry["backup"]
                    shutil.copy2(path, backup)
                    with backup.open("rb") as handle:
                        os.fsync(handle.fileno())
            _write_transaction_manifest(backup_root / "manifest.json", manifest)
            final_root = transaction_root / (
                "txn-" + backup_root.name.removeprefix(".initializing-")
            )
            os.replace(backup_root, final_root)
            _fsync_directory(transaction_root)
            backup_root = final_root
            prepared = True
            atomic_temporaries = self._atomic_temporaries(backup_root, manifest)
            for temporary in atomic_temporaries.values():
                state = _expected_state_key(
                    _path_state(temporary, boundary=self.comments)
                )
                if state != (False, "", 0):
                    raise ContractError(
                        f"transaction atomic temporary is not absent: {temporary}"
                    )
            token = _ACTIVE_ATOMIC_TEMPORARIES.set(atomic_temporaries)
            try:
                yield
            finally:
                _ACTIVE_ATOMIC_TEMPORARIES.reset(token)
            manifest["state"] = "committed"
            manifest["recovery"] = None
            _write_transaction_manifest(backup_root / "manifest.json", manifest)
        except BaseException:
            if prepared:
                self._restore_transaction(backup_root, manifest)
                # Mark the restored state final before cleanup, so a cleanup
                # interruption never retries against partially removed backups.
                manifest["state"] = "committed"
                manifest["recovery"] = None
                _write_transaction_manifest(
                    backup_root / "manifest.json", manifest
                )
                _remove_tree_best_effort(backup_root)
                _fsync_directory(transaction_root)
            else:
                _remove_tree_best_effort(backup_root)
                _fsync_directory(transaction_root)
            raise
        else:
            _remove_tree_best_effort(backup_root)
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
        """Validate the exact candidate index tree, independent of the checkout."""
        if not (self.root / ".git").exists():
            return []
        written = subprocess.run(
            ["git", "write-tree"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )
        if written.returncode != 0 or not written.stdout.strip():
            detail = written.stderr.strip() or "git write-tree failed"
            return [f"staged candidate: cannot write index tree ({detail})"]
        tree = written.stdout.strip()
        listing = subprocess.run(
            [
                "git",
                "ls-tree",
                "-r",
                "-z",
                "--full-tree",
                tree,
                "--",
                ESTATE_REL.as_posix(),
                COMMENTS_REL.as_posix(),
            ],
            cwd=self.root,
            capture_output=True,
            check=False,
        )
        if listing.returncode != 0:
            return ["staged candidate: git ls-tree failed"]

        errors: list[str] = []
        files: dict[Path, bytes] = {}
        for encoded in listing.stdout.split(b"\0"):
            if not encoded:
                continue
            try:
                metadata, encoded_path = encoded.split(b"\t", 1)
                mode, object_type, oid = metadata.decode("ascii").split()
                path_text = encoded_path.decode("utf-8", errors="strict")
            except (ValueError, UnicodeDecodeError):
                errors.append("staged candidate: malformed Git tree entry")
                continue
            relative = Path(path_text)
            if (
                relative.is_absolute()
                or ".." in relative.parts
                or not (
                    relative == ESTATE_REL
                    or relative.parts[:2] == COMMENTS_REL.parts
                )
            ):
                errors.append(f"staged candidate: unsafe path {path_text!r}")
                continue
            if mode != "100644" or object_type != "blob":
                errors.append(
                    f"staged candidate: {path_text} must be a regular 100644 file"
                )
                continue
            shown = subprocess.run(
                ["git", "cat-file", "blob", oid],
                cwd=self.root,
                capture_output=True,
                check=False,
            )
            if shown.returncode != 0:
                errors.append(f"staged candidate: {path_text}: cannot read blob")
                continue
            raw = shown.stdout
            if b"\r" in raw:
                errors.append(
                    f"staged candidate: {path_text}: staged blob contains CR bytes; "
                    "committed "
                    "owner-comment files must use LF"
                )
            files[relative] = raw

        with tempfile.TemporaryDirectory(prefix="owner-comments-candidate-") as temp:
            candidate_root = Path(temp)
            try:
                for relative, raw in files.items():
                    destination = candidate_root / relative
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(raw)
                candidate = OwnerCommentsStore(candidate_root)
                candidate_errors = candidate._check_locked()
                records, scan_errors = candidate.scan()
            except (ContractError, OSError) as exc:
                errors.append(f"staged candidate: cannot validate tree ({exc})")
            else:
                errors.extend(
                    f"staged candidate: {error}" for error in candidate_errors
                )
                if not scan_errors:
                    errors.extend(
                        f"staged candidate: {error}"
                        for error in self.lifecycle_errors(records)
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
        staged_errors = self.staged_blob_errors()
        if errors:
            return errors + staged_errors
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
        errors.extend(staged_errors)
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
        phase = {
            path: path.read_bytes() if path.is_file() else None for path in changes
        }
        expected_phases = []
        for path, content in changes.items():
            phase[path] = content
            expected_phases.append(dict(phase))
        with self.rollback_snapshot(tuple(expected_phases)):
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
            data, source_raw = _load_json(source)
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
        updated_raw = _json_bytes(updated)
        current_records, scan_errors = self.scan()
        if scan_errors:
            raise ContractError("\n".join(scan_errors))
        source_relative = source.relative_to(self.comments)
        destination_relative = destination.relative_to(self.comments)
        planned_records = [
            (
                Record(path=destination_relative, data=updated)
                if current.path == source_relative
                else current
            )
            for current in current_records
        ]
        if sum(current.path == source_relative for current in current_records) != 1:
            raise ContractError("source record is missing from the validated ledger")
        planned_indexes = self.expected_indexes(planned_records)
        repository_index = self.comments / repository / "README.md"
        root_index = self.comments / "index.json"
        destination.parent.mkdir(parents=True, exist_ok=True)

        phase = {
            source: source_raw,
            destination: None,
            repository_index: repository_index.read_bytes(),
            root_index: root_index.read_bytes(),
        }
        expected_phases = []
        # The move first exposes the original bytes at destination.
        phase[source] = None
        phase[destination] = source_raw
        expected_phases.append(dict(phase))
        # The following atomic replace exposes the consumed record bytes.
        phase[destination] = updated_raw
        expected_phases.append(dict(phase))
        # expected_indexes writes the root projection before repository indexes.
        phase[root_index] = planned_indexes[root_index]
        expected_phases.append(dict(phase))
        phase[repository_index] = planned_indexes[repository_index]
        expected_phases.append(dict(phase))
        with self.rollback_snapshot(tuple(expected_phases)):
            source.replace(destination)  # the lifecycle transition is a real move
            _fsync_directory(source.parent)
            _fsync_directory(destination.parent)
            _atomic_write(destination, updated_raw)
            _atomic_write(root_index, planned_indexes[root_index])
            _atomic_write(repository_index, planned_indexes[repository_index])
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
