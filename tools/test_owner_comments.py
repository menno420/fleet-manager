#!/usr/bin/env python3
"""Contract/regression tests for tools/owner_comments.py and its route."""

from __future__ import annotations

import errno
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest import mock

import owner_comments
from owner_comments import ContractError, OwnerCommentsStore


REPO = Path(__file__).resolve().parents[1]


def write_lf(path: Path, content: str) -> None:
    """Write a UTF-8 fixture without host newline translation."""
    path.write_bytes(content.encode("utf-8"))


def record(comment_id: str = "oc-20260827t120000z-a1b2c3d4") -> dict:
    return {
        "schema_version": 1,
        "id": comment_id,
        "repository": "websites",
        "created_at": "2026-08-27T12:00:00Z",
        "state": "unconsumed",
        "source": {"surface": "control-plane", "context": "/repos/websites"},
        "comment": "  Preserve my wording exactly — including this spacing.  ",
    }


class StoreCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "docs").mkdir()
        write_lf(
            self.root / "docs/ESTATE.md",
            "# estate\n\n"
            "| repo | state |\n|---|---|\n"
            "| `fleet-manager` | active |\n"
            "| `websites` | active |\n"
            "| `Substrate-kit-app` | archived |\n",
        )
        comments = self.root / "docs/owner-comments"
        comments.mkdir()
        for name in ("README.md", "record.schema.json"):
            shutil.copy2(REPO / "docs/owner-comments" / name, comments / name)
        self.store = OwnerCommentsStore(self.root)
        self.store.reindex()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_record(self, data: dict | None = None) -> Path:
        payload = data or record()
        path = self.root / "docs/owner-comments/websites" / f"{payload['id']}.json"
        write_lf(
            path,
            json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        )
        return path

    def symlink_or_skip(
        self, link: Path, target: Path, *, target_is_directory: bool
    ) -> None:
        """Create a link or skip when ordinary Windows lacks link privilege."""
        try:
            link.symlink_to(target, target_is_directory=target_is_directory)
        except OSError as exc:
            if os.name == "nt" and getattr(exc, "winerror", None) == 1314:
                self.skipTest(
                    "Windows symlink privilege is unavailable without Developer Mode"
                )
            raise

    def assert_safe_data_file_mode(self, path: Path) -> None:
        """Assert the strongest portable mode promised for new data files."""
        mode = stat.S_IMODE(path.stat().st_mode)
        if os.name == "nt":
            # Windows chmod exposes only the read-only attribute; group/other
            # POSIX bits are ignored and writable files commonly report 0666.
            self.assertTrue(mode & stat.S_IREAD, oct(mode))
            self.assertTrue(mode & stat.S_IWRITE, oct(mode))
        else:
            self.assertEqual(mode, 0o644)

    @contextmanager
    def windows_readonly_semantics(self):
        """Model the Windows read-only checks on the POSIX gate runner."""
        real_chmod = os.chmod
        real_replace = os.replace
        real_unlink = os.unlink
        replacements: list[tuple[int, int | None]] = []

        def windows_chmod(
            path: os.PathLike[str] | str, mode: int, *args, **kwargs
        ) -> None:
            observable = 0o666 if mode & stat.S_IWRITE else 0o444
            real_chmod(path, observable, *args, **kwargs)

        def windows_replace(
            source: os.PathLike[str] | str,
            destination: os.PathLike[str] | str,
        ) -> None:
            source_mode = stat.S_IMODE(os.lstat(source).st_mode)
            try:
                destination_mode = stat.S_IMODE(os.lstat(destination).st_mode)
            except FileNotFoundError:
                destination_mode = None
            if destination_mode is not None and not (
                destination_mode & stat.S_IWRITE
            ):
                raise PermissionError(
                    errno.EACCES, "Windows refuses a read-only destination"
                )
            replacements.append((source_mode, destination_mode))
            real_replace(source, destination)

        def windows_unlink(
            path: os.PathLike[str] | str, *args, **kwargs
        ) -> None:
            if not args and not kwargs:
                try:
                    mode = stat.S_IMODE(os.lstat(path).st_mode)
                except FileNotFoundError:
                    mode = None
                if mode is not None and not (mode & stat.S_IWRITE):
                    raise PermissionError(
                        errno.EACCES, "Windows refuses a read-only unlink"
                    )
            real_unlink(path, *args, **kwargs)

        with mock.patch.object(
            owner_comments, "_is_windows", return_value=True
        ), mock.patch.object(
            owner_comments.os, "chmod", side_effect=windows_chmod
        ), mock.patch.object(
            owner_comments.os, "replace", side_effect=windows_replace
        ), mock.patch.object(
            owner_comments.os, "unlink", side_effect=windows_unlink
        ):
            yield replacements

    @contextmanager
    def windows_reparse_semantics(self, *reparse_paths: Path):
        """Model Windows junction/reparse metadata on the POSIX gate runner."""
        real_lstat = os.lstat
        marked = {Path(path) for path in reparse_paths}

        class ReparseMetadata:
            def __init__(self, metadata):
                self._metadata = metadata

            def __getattr__(self, name):
                if name == "st_file_attributes":
                    return (
                        getattr(self._metadata, name, 0)
                        | owner_comments._WINDOWS_REPARSE_POINT
                    )
                if name == "st_reparse_tag":
                    return 0xA0000003  # IO_REPARSE_TAG_MOUNT_POINT
                return getattr(self._metadata, name)

        def windows_lstat(path, *args, **kwargs):
            metadata = real_lstat(path, *args, **kwargs)
            candidate = Path(path)
            if candidate in marked:
                return ReparseMetadata(metadata)
            return metadata

        with mock.patch.object(
            owner_comments, "_is_windows", return_value=True
        ), mock.patch.object(owner_comments.os, "lstat", side_effect=windows_lstat):
            yield

    def commit_baseline(self, message: str = "baseline") -> None:
        subprocess.run(
            ["git", "init", "-q", "--initial-branch=main"],
            cwd=self.root,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.email", "contract-test@example.invalid"],
            cwd=self.root,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.name", "Contract Test"],
            cwd=self.root,
            check=True,
        )
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(
            ["git", "commit", "-q", "-m", message],
            cwd=self.root,
            check=True,
        )

    def publish_test_transaction(
        self,
        phase: dict[Path, owner_comments._FileImage | None],
        *,
        name: str,
    ) -> tuple[Path, dict]:
        """Publish one valid prepared journal for recovery regressions."""
        manifest = self.store._transaction_manifest((phase,))
        transaction_root = self.store._ensure_transaction_root()
        backup_root = transaction_root / f"txn-{name}"
        backup_root.mkdir()
        for number, entry in enumerate(manifest["entries"]):
            if entry["existed"]:
                shutil.copy2(
                    self.root / entry["path"], backup_root / str(number)
                )
        owner_comments._write_transaction_manifest(
            backup_root / "manifest.json", manifest
        )
        return backup_root, manifest

    def test_reindex_builds_all_stable_indexes_and_cheap_root_index(self) -> None:
        root_index = json.loads(
            (self.root / "docs/owner-comments/index.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            [row["repository"] for row in root_index["repositories"]],
            ["fleet-manager", "websites", "Substrate-kit-app"],
        )
        for repository in ("fleet-manager", "websites", "Substrate-kit-app"):
            self.assertTrue(
                (self.root / "docs/owner-comments" / repository / "README.md").is_file()
            )
        self.assertEqual(self.store.check(), [])

    def test_record_text_is_not_normalized_and_active_index_names_record(self) -> None:
        path = self.write_record()
        self.store.reindex()
        self.assertEqual(json.loads(path.read_text())["comment"], record()["comment"])
        index = (path.parent / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Unconsumed (1)", index)
        self.assertIn(record()["id"], index)
        root = json.loads(
            (self.root / "docs/owner-comments/index.json").read_text(encoding="utf-8")
        )
        websites = next(r for r in root["repositories"] if r["repository"] == "websites")
        self.assertEqual(websites["unconsumed_count"], 1)

    def test_consume_moves_preserves_and_excludes_from_unconsumed(self) -> None:
        original = self.write_record()
        self.store.reindex()
        destination = self.store.consume(
            "websites",
            record()["id"],
            consumed_at="2026-08-27T13:00:00Z",
            actor=".sessions/2026-08-27-example.md",
            evidence="https://github.com/menno420/websites/pull/123",
        )
        self.assertFalse(original.exists())
        preserved = self.root / destination
        self.assertTrue(preserved.is_file())
        data = json.loads(preserved.read_text(encoding="utf-8"))
        self.assertEqual(data["comment"], record()["comment"])
        self.assertEqual(data["state"], "consumed")
        self.assertEqual(data["consumption"]["actor"], ".sessions/2026-08-27-example.md")
        index = (original.parent / "README.md").read_text(encoding="utf-8")
        active_section, history = index.split("## Consumed history", 1)
        self.assertIn("## Unconsumed (0)", active_section)
        self.assertNotIn(record()["id"], active_section)
        self.assertIn(record()["id"], history)
        root = json.loads(
            (self.root / "docs/owner-comments/index.json").read_text(encoding="utf-8")
        )
        websites = next(r for r in root["repositories"] if r["repository"] == "websites")
        self.assertEqual(websites["unconsumed_count"], 0)
        self.assertEqual(websites["consumed_count"], 1)
        self.assertEqual(self.store.check(), [])

    def test_consume_rejects_unknown_repository_and_double_consume(self) -> None:
        with self.assertRaises(ContractError):
            self.store.consume(
                "../websites",
                record()["id"],
                consumed_at="2026-08-27T13:00:00Z",
                actor="actor",
                evidence="evidence",
            )
        self.write_record()
        self.store.reindex()
        kwargs = {
            "consumed_at": "2026-08-27T13:00:00Z",
            "actor": "actor",
            "evidence": "evidence",
        }
        self.store.consume("websites", record()["id"], **kwargs)
        with self.assertRaises(ContractError):
            self.store.consume("websites", record()["id"], **kwargs)

    def test_invalid_schema_and_noncanonical_directory_fail(self) -> None:
        bad = record()
        bad["comment"] = "   "
        self.write_record(bad)
        unknown = self.root / "docs/owner-comments/not-indexed"
        unknown.mkdir()
        write_lf(unknown / "README.md", "unexpected\n")
        errors = self.store.check()
        self.assertTrue(any("non-whitespace" in error for error in errors), errors)
        self.assertTrue(any("closed owner-comment" in error for error in errors), errors)

    def test_path_state_and_repository_must_agree(self) -> None:
        bad = record()
        bad["repository"] = "fleet-manager"
        self.write_record(bad)
        errors = self.store.check()
        self.assertTrue(any("does not match path" in error for error in errors), errors)

    def test_source_surface_and_consumption_time_are_bounded(self) -> None:
        bad_source = record()
        bad_source["source"]["surface"] = "[rendered link](https://example.test)"
        self.write_record(bad_source)
        errors = self.store.check()
        self.assertTrue(any("source.surface" in error for error in errors), errors)

        (self.root / "docs/owner-comments/websites" / f"{record()['id']}.json").unlink()
        self.store.reindex()
        self.write_record()
        self.store.reindex()
        with self.assertRaisesRegex(ContractError, "must not precede"):
            self.store.consume(
                "websites",
                record()["id"],
                consumed_at="2026-08-27T11:59:59Z",
                actor="actor",
                evidence="evidence",
            )

    def test_stale_generated_index_fails_check(self) -> None:
        path = self.root / "docs/owner-comments/index.json"
        write_lf(path, "{}\n")
        self.assertTrue(any("stale" in error for error in self.store.check()))

    def test_estate_repository_names_are_safe_path_components(self) -> None:
        with (self.root / "docs/ESTATE.md").open("a", encoding="utf-8") as handle:
            handle.write("| `../../escaped` | invalid |\n")
        with self.assertRaisesRegex(ContractError, "unsafe repository"):
            self.store.reindex()
        self.assertFalse((self.root / "escaped").exists())

    def test_estate_repository_namespace_rejects_reserved_and_casefolded_names(self) -> None:
        for repository in ("README.md", "INDEX.JSON", "record.schema.json"):
            self.assertFalse(owner_comments._valid_repository(repository), repository)

        with (self.root / "docs/ESTATE.md").open("a", encoding="utf-8") as handle:
            handle.write("| `WEBsites` | collision |\n")
        with self.assertRaisesRegex(ContractError, "case-folding"):
            self.store.reindex()

    def test_schema_version_duplicate_keys_and_canonical_json_are_enforced(self) -> None:
        boolean_version = record()
        boolean_version["schema_version"] = True
        path = self.write_record(boolean_version)
        errors = self.store.check()
        self.assertTrue(any("schema_version" in error for error in errors), errors)

        duplicate = json.dumps(record(), sort_keys=True)
        duplicate = duplicate[:-1] + ', "state": "unconsumed"}'
        write_lf(path, duplicate + "\n")
        errors = self.store.check()
        self.assertTrue(any("duplicate JSON key" in error for error in errors), errors)

        write_lf(path, json.dumps(record()) + "\n")
        errors = self.store.check()
        self.assertTrue(any("not canonical" in error for error in errors), errors)

    def test_fractional_timestamps_sort_chronologically(self) -> None:
        first = record("oc-first")
        first["created_at"] = "2026-08-27T12:00:00Z"
        second = record("oc-second")
        second["created_at"] = "2026-08-27T12:00:00.5Z"
        self.write_record(first)
        self.write_record(second)
        self.store.reindex()
        root = json.loads(
            (self.root / "docs/owner-comments/index.json").read_text(encoding="utf-8")
        )
        websites = next(r for r in root["repositories"] if r["repository"] == "websites")
        self.assertEqual(websites["latest_unconsumed_at"], second["created_at"])
        index = (self.root / "docs/owner-comments/websites/README.md").read_text()
        self.assertLess(index.index("oc-first"), index.index("oc-second"))

    def test_mutation_lock_refuses_a_second_consumer_without_changing_tree(self) -> None:
        original = self.write_record()
        self.store.reindex()
        with self.store.mutation_lock():
            with self.assertRaisesRegex(ContractError, "transaction is in progress"):
                self.store.consume(
                    "websites",
                    record()["id"],
                    consumed_at="2026-08-27T13:00:00Z",
                    actor="actor",
                    evidence="evidence",
                )
            with self.assertRaisesRegex(ContractError, "transaction is in progress"):
                self.store.reindex()
        self.assertTrue(original.is_file())
        self.assertFalse(
            (original.parent / "consumed" / original.name).exists()
        )
        self.assertEqual(self.store.check(), [])

    def test_process_lock_is_shared_across_distinct_tmpdirs(self) -> None:
        first_tmp = self.root / "tmp-a"
        second_tmp = self.root / "tmp-b"
        first_tmp.mkdir()
        second_tmp.mkdir()
        holder_code = """
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
from owner_comments import OwnerCommentsStore
with OwnerCommentsStore(Path(sys.argv[2])).mutation_lock():
    print('locked', flush=True)
    sys.stdin.readline()
"""
        contender_code = """
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
from owner_comments import ContractError, OwnerCommentsStore
try:
    with OwnerCommentsStore(Path(sys.argv[2])).mutation_lock():
        raise SystemExit(7)
except ContractError:
    raise SystemExit(0)
"""
        holder = subprocess.Popen(
            [sys.executable, "-c", holder_code, str(REPO / "tools"), str(self.root)],
            cwd=REPO,
            env=dict(os.environ, TMPDIR=str(first_tmp)),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        try:
            self.assertEqual(holder.stdout.readline().strip(), "locked")
            contender = subprocess.run(
                [
                    sys.executable,
                    "-c",
                    contender_code,
                    str(REPO / "tools"),
                    str(self.root),
                ],
                cwd=REPO,
                env=dict(os.environ, TMPDIR=str(second_tmp)),
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
            self.assertEqual(contender.returncode, 0, contender.stderr)
        finally:
            if holder.stdin:
                holder.stdin.write("\n")
                holder.stdin.flush()
            holder.communicate(timeout=5)

    def test_hard_exit_consume_is_recovered_on_next_store_entry(self) -> None:
        original = self.write_record()
        self.store.reindex()
        crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_write = owner_comments._atomic_write
def crash_on_consumed(path, content):
    if path.parent.name == 'consumed':
        os._exit(91)
    real_write(path, content)
owner_comments._atomic_write = crash_on_consumed
store.consume(
    'websites',
    'oc-20260827t120000z-a1b2c3d4',
    consumed_at='2026-08-27T13:00:00Z',
    actor='actor',
    evidence='evidence',
)
"""
        crashed = subprocess.run(
            [sys.executable, "-c", crash_code, str(REPO / "tools"), str(self.root)],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(crashed.returncode, 91, crashed.stderr)
        destination = original.parent / "consumed" / original.name
        self.assertFalse(original.exists())
        self.assertTrue(destination.exists())
        transaction_root = self.store._transaction_root()
        self.assertTrue(list(transaction_root.glob("txn-*")))

        self.assertEqual(self.store.check(), [])
        self.assertTrue(original.exists())
        self.assertFalse(destination.exists())
        self.assertFalse(list(transaction_root.glob("txn-*")))

    def test_hard_exit_atomic_temporary_is_scavenged_before_recovery(self) -> None:
        original = self.write_record()
        self.store.reindex()
        crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_replace = owner_comments.os.replace
def crash_before_atomic_replace(source, destination):
    source = Path(source)
    destination = Path(destination)
    if '.atomic-' in source.name and destination.parent.name == 'consumed':
        os._exit(93)
    real_replace(source, destination)
owner_comments.os.replace = crash_before_atomic_replace
store.consume(
    'websites',
    'oc-20260827t120000z-a1b2c3d4',
    consumed_at='2026-08-27T13:00:00Z',
    actor='actor',
    evidence='evidence',
)
"""
        crashed = subprocess.run(
            [sys.executable, "-c", crash_code, str(REPO / "tools"), str(self.root)],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(crashed.returncode, 93, crashed.stderr)
        temporaries = list(
            (self.root / "docs/owner-comments").rglob(".*.atomic-*")
        )
        self.assertEqual(len(temporaries), 1)

        self.assertEqual(self.store.check(), [])
        self.assertTrue(original.is_file())
        self.assertFalse(
            (original.parent / "consumed" / original.name).exists()
        )
        self.assertFalse(
            list((self.root / "docs/owner-comments").rglob(".*.atomic-*"))
        )
        self.assertFalse(list(self.store._transaction_root().glob("txn-*")))

    def test_changed_atomic_temporary_is_preserved_before_quarantine(self) -> None:
        original = self.write_record()
        self.store.reindex()
        crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_replace = owner_comments.os.replace
def crash_before_atomic_replace(source, destination):
    source = Path(source)
    destination = Path(destination)
    if '.atomic-' in source.name and destination.parent.name == 'consumed':
        os._exit(93)
    real_replace(source, destination)
owner_comments.os.replace = crash_before_atomic_replace
store.consume(
    'websites',
    'oc-20260827t120000z-a1b2c3d4',
    consumed_at='2026-08-27T13:00:00Z',
    actor='actor',
    evidence='evidence',
)
"""
        crashed = subprocess.run(
            [sys.executable, "-c", crash_code, str(REPO / "tools"), str(self.root)],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(crashed.returncode, 93, crashed.stderr)
        temporary = next(
            (self.root / "docs/owner-comments").rglob(".*.atomic-*")
        )
        unexpected = b"post-crash owner bytes must not be deleted\n"
        temporary.write_bytes(unexpected)
        destination = original.parent / "consumed" / original.name
        targets_before = {
            path: path.read_bytes() if path.exists() else None
            for path in (
                original,
                destination,
                original.parent / "README.md",
                self.root / "docs/owner-comments/index.json",
            )
        }

        preserve_crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_replace = owner_comments.os.replace
def preserve_then_crash(source, destination):
    real_replace(source, destination)
    if Path(destination).name.startswith('unexpected-atomic-1'):
        os._exit(94)
owner_comments.os.replace = preserve_then_crash
store.check()
"""
        preserved = subprocess.run(
            [
                sys.executable,
                "-c",
                preserve_crash_code,
                str(REPO / "tools"),
                str(self.root),
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(preserved.returncode, 94, preserved.stderr)
        self.assertFalse(temporary.exists())

        retry_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_fsync_file = owner_comments._fsync_file
real_fsync_directory = owner_comments._fsync_directory
real_rename = owner_comments.os.rename
seen = {'file': False, 'directory': False}
def track_file_fsync(path):
    real_fsync_file(path)
    if Path(path).name.startswith('unexpected-atomic-1'):
        seen['file'] = True
def track_directory_fsync(path):
    real_fsync_directory(path)
    if Path(path).name.startswith('txn-'):
        seen['directory'] = True
def require_durable_preservation(source, destination):
    if Path(destination).name.startswith('quarantine-') and not all(seen.values()):
        os._exit(96)
    real_rename(source, destination)
owner_comments._fsync_file = track_file_fsync
owner_comments._fsync_directory = track_directory_fsync
owner_comments.os.rename = require_durable_preservation
try:
    store.check()
except owner_comments.ContractError as exc:
    if 'temporary mismatch' not in str(exc):
        raise
else:
    raise SystemExit(97)
"""
        retry = subprocess.run(
            [
                sys.executable,
                "-c",
                retry_code,
                str(REPO / "tools"),
                str(self.root),
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(retry.returncode, 0, retry.stderr)
        self.assertEqual(
            {
                path: path.read_bytes() if path.exists() else None
                for path in targets_before
            },
            targets_before,
        )
        transaction_root = self.store._transaction_root()
        self.assertFalse(list(transaction_root.glob("txn-*")))
        quarantine = next(transaction_root.glob("quarantine-*"))
        self.assertEqual(
            (quarantine / "unexpected-atomic-1").read_bytes(), unexpected
        )

    def test_same_filesystem_preservation_fsyncs_before_quarantine(self) -> None:
        self.write_record()
        self.store.reindex()
        crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_replace = owner_comments.os.replace
def crash_before_atomic_replace(source, destination):
    source = Path(source)
    destination = Path(destination)
    if '.atomic-' in source.name and destination.parent.name == 'consumed':
        os._exit(93)
    real_replace(source, destination)
owner_comments.os.replace = crash_before_atomic_replace
store.consume(
    'websites',
    'oc-20260827t120000z-a1b2c3d4',
    consumed_at='2026-08-27T13:00:00Z',
    actor='actor',
    evidence='evidence',
)
"""
        crashed = subprocess.run(
            [sys.executable, "-c", crash_code, str(REPO / "tools"), str(self.root)],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(crashed.returncode, 93, crashed.stderr)
        temporary = next(
            (self.root / "docs/owner-comments").rglob(".*.atomic-*")
        )
        unexpected = b"same-filesystem preserved bytes are durable\n"
        temporary.write_bytes(unexpected)
        real_fsync_file = owner_comments._fsync_file
        real_rename = owner_comments.os.rename
        preserved_fsynced = False

        def track_fsync(path: Path) -> None:
            nonlocal preserved_fsynced
            real_fsync_file(path)
            if Path(path).name.startswith("unexpected-atomic-1"):
                preserved_fsynced = True

        def require_file_fsync(source: Path, destination: Path) -> None:
            if Path(destination).name.startswith("quarantine-"):
                self.assertTrue(preserved_fsynced)
            real_rename(source, destination)

        with mock.patch.object(
            owner_comments, "_fsync_file", side_effect=track_fsync
        ), mock.patch.object(
            owner_comments.os, "rename", side_effect=require_file_fsync
        ):
            with self.assertRaisesRegex(
                ContractError, "temporary mismatch.*preserved.*quarantined"
            ):
                self.store.check()
        self.assertTrue(preserved_fsynced)
        quarantine = next(self.store._transaction_root().glob("quarantine-*"))
        self.assertEqual(
            (quarantine / "unexpected-atomic-1").read_bytes(), unexpected
        )
        self.assertFalse(temporary.exists())

    def test_second_death_after_preserving_temp_still_quarantines_bytes(self) -> None:
        original = self.write_record()
        self.store.reindex()
        atomic_crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_replace = owner_comments.os.replace
def crash_before_atomic_replace(source, destination):
    source = Path(source)
    destination = Path(destination)
    if '.atomic-' in source.name and destination.parent.name == 'consumed':
        os._exit(93)
    real_replace(source, destination)
owner_comments.os.replace = crash_before_atomic_replace
store.consume(
    'websites',
    'oc-20260827t120000z-a1b2c3d4',
    consumed_at='2026-08-27T13:00:00Z',
    actor='actor',
    evidence='evidence',
)
"""
        first = subprocess.run(
            [
                sys.executable,
                "-c",
                atomic_crash_code,
                str(REPO / "tools"),
                str(self.root),
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(first.returncode, 93, first.stderr)
        temporary = next(
            (self.root / "docs/owner-comments").rglob(".*.atomic-*")
        )
        unexpected = b"unique post-crash bytes survive a second death\n"
        temporary.write_bytes(unexpected)

        preservation_crash_code = """
import errno
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_replace = owner_comments.os.replace
real_fsync_file = owner_comments._fsync_file
def force_cross_device(source, destination):
    if Path(destination).name.startswith('unexpected-'):
        raise OSError(errno.EXDEV, 'simulated cross-device journal')
    real_replace(source, destination)
def crash_before_preserved_fsync(path):
    if Path(path).name.startswith('unexpected-atomic-1'):
        os._exit(95)
    real_fsync_file(path)
owner_comments.os.replace = force_cross_device
owner_comments._fsync_file = crash_before_preserved_fsync
store.check()
"""
        second = subprocess.run(
            [
                sys.executable,
                "-c",
                preservation_crash_code,
                str(REPO / "tools"),
                str(self.root),
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(second.returncode, 95, second.stderr)
        transaction_root = self.store._transaction_root()
        transaction = next(transaction_root.glob("txn-*"))
        self.assertEqual(
            (transaction / "unexpected-atomic-1").read_bytes(), unexpected
        )
        self.assertEqual(temporary.read_bytes(), unexpected)

        marker = self.root / "preserved-copy-was-fsynced"
        retry_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
marker = Path(sys.argv[3])
real_fsync_file = owner_comments._fsync_file
real_unlink = Path.unlink
def track_preserved_fsync(path):
    real_fsync_file(path)
    if Path(path).name.startswith('unexpected-atomic-1'):
        marker.write_bytes(b'fsynced before unlink\\n')
def refuse_early_unlink(path, *args, **kwargs):
    if '.atomic-' in path.name and not marker.exists():
        os._exit(96)
    return real_unlink(path, *args, **kwargs)
owner_comments._fsync_file = track_preserved_fsync
Path.unlink = refuse_early_unlink
try:
    store.check()
except owner_comments.ContractError as exc:
    if 'temporary mismatch' not in str(exc):
        raise
else:
    raise SystemExit(97)
"""
        retry = subprocess.run(
            [
                sys.executable,
                "-c",
                retry_code,
                str(REPO / "tools"),
                str(self.root),
                str(marker),
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(retry.returncode, 0, retry.stderr)
        self.assertEqual(marker.read_text(encoding="utf-8"), "fsynced before unlink\n")
        self.assertFalse(list(transaction_root.glob("txn-*")))
        quarantine = next(transaction_root.glob("quarantine-*"))
        self.assertEqual(
            (quarantine / "unexpected-atomic-1").read_bytes(), unexpected
        )
        self.assertFalse(temporary.exists())
        self.assertFalse(original.exists())

    def test_second_hard_exit_recovery_temporary_resumes_cleanly(self) -> None:
        original = self.write_record()
        self.store.reindex()
        consume_crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_write = owner_comments._atomic_write
def crash_on_consumed(path, content):
    if path.parent.name == 'consumed':
        os._exit(91)
    real_write(path, content)
owner_comments._atomic_write = crash_on_consumed
store.consume(
    'websites',
    'oc-20260827t120000z-a1b2c3d4',
    consumed_at='2026-08-27T13:00:00Z',
    actor='actor',
    evidence='evidence',
)
"""
        first = subprocess.run(
            [
                sys.executable,
                "-c",
                consume_crash_code,
                str(REPO / "tools"),
                str(self.root),
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(first.returncode, 91, first.stderr)

        recovery_crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_replace = owner_comments.os.replace
def crash_before_recovery_replace(source, destination):
    if '.recover-' in Path(source).name:
        os._exit(92)
    real_replace(source, destination)
owner_comments.os.replace = crash_before_recovery_replace
store.check()
"""
        second = subprocess.run(
            [
                sys.executable,
                "-c",
                recovery_crash_code,
                str(REPO / "tools"),
                str(self.root),
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(second.returncode, 92, second.stderr)
        self.assertEqual(
            len(list((self.root / "docs/owner-comments").rglob(".*.recover-*"))),
            1,
        )

        self.assertEqual(self.store.check(), [])
        self.assertTrue(original.is_file())
        self.assertFalse(
            (original.parent / "consumed" / original.name).exists()
        )
        self.assertFalse(
            list((self.root / "docs/owner-comments").rglob(".*.recover-*"))
        )
        self.assertFalse(list(self.store._transaction_root().glob("txn-*")))

    def test_same_identity_recovery_quarantines_post_crash_target_edit(self) -> None:
        original = self.write_record()
        self.store.reindex()
        self.commit_baseline("active owner comment")
        prepared_identity = self.store._git_identity()
        crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_write = owner_comments._atomic_write
def crash_on_consumed(path, content):
    if path.parent.name == 'consumed':
        os._exit(91)
    real_write(path, content)
owner_comments._atomic_write = crash_on_consumed
store.consume(
    'websites',
    'oc-20260827t120000z-a1b2c3d4',
    consumed_at='2026-08-27T13:00:00Z',
    actor='actor',
    evidence='evidence',
)
"""
        crashed = subprocess.run(
            [sys.executable, "-c", crash_code, str(REPO / "tools"), str(self.root)],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(crashed.returncode, 91, crashed.stderr)
        destination = original.parent / "consumed" / original.name
        edited = record()
        edited["comment"] = "Canonical owner edit made after the interrupted process."
        destination.write_bytes(owner_comments._json_bytes(edited))
        self.assertEqual(self.store._git_identity(), prepared_identity)
        before = {
            path: path.read_bytes() if path.exists() else None
            for path in (
                original,
                destination,
                original.parent / "README.md",
                self.root / "docs/owner-comments/index.json",
            )
        }
        status_before = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=True,
        ).stdout

        with self.assertRaisesRegex(
            ContractError, "target bytes/state changed.*quarantined"
        ):
            self.store.check()
        self.assertEqual(
            {
                path: path.read_bytes() if path.exists() else None
                for path in before
            },
            before,
        )
        self.assertEqual(
            subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.root,
                capture_output=True,
                text=True,
                check=True,
            ).stdout,
            status_before,
        )
        transaction_root = self.store._transaction_root()
        self.assertFalse(list(transaction_root.glob("txn-*")))
        self.assertEqual(len(list(transaction_root.glob("quarantine-*"))), 1)

    def test_same_identity_recovery_rejects_impossible_deleted_move_vector(self) -> None:
        original = self.write_record()
        self.store.reindex()
        self.commit_baseline("active owner comment")
        prepared_identity = self.store._git_identity()
        crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_write = owner_comments._atomic_write
def crash_on_consumed(path, content):
    if path.parent.name == 'consumed':
        os._exit(91)
    real_write(path, content)
owner_comments._atomic_write = crash_on_consumed
store.consume(
    'websites',
    'oc-20260827t120000z-a1b2c3d4',
    consumed_at='2026-08-27T13:00:00Z',
    actor='actor',
    evidence='evidence',
)
"""
        crashed = subprocess.run(
            [sys.executable, "-c", crash_code, str(REPO / "tools"), str(self.root)],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(crashed.returncode, 91, crashed.stderr)
        destination = original.parent / "consumed" / original.name
        self.assertFalse(original.exists())
        self.assertTrue(destination.exists())
        destination.unlink()
        self.assertEqual(self.store._git_identity(), prepared_identity)
        status_before = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=True,
        ).stdout

        with self.assertRaisesRegex(
            ContractError, "target bytes/state changed.*quarantined"
        ):
            self.store.check()
        self.assertFalse(original.exists())
        self.assertFalse(destination.exists())
        self.assertEqual(
            subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.root,
                capture_output=True,
                text=True,
                check=True,
            ).stdout,
            status_before,
        )
        transaction_root = self.store._transaction_root()
        self.assertFalse(list(transaction_root.glob("txn-*")))
        self.assertEqual(len(list(transaction_root.glob("quarantine-*"))), 1)

    def test_stale_journal_cannot_rewrite_a_switched_branch(self) -> None:
        original = self.write_record()
        self.store.reindex()
        self.commit_baseline("active owner comment")
        subprocess.run(
            ["git", "switch", "-q", "-c", "consumed-state"],
            cwd=self.root,
            check=True,
        )
        destination = self.root / self.store.consume(
            "websites",
            record()["id"],
            consumed_at="2026-08-27T13:00:00Z",
            actor="actor",
            evidence="evidence",
        )
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(
            ["git", "commit", "-q", "-m", "consume owner comment"],
            cwd=self.root,
            check=True,
        )
        subprocess.run(
            ["git", "switch", "-q", "main"], cwd=self.root, check=True
        )

        crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_write = owner_comments._atomic_write
def crash_on_consumed(path, content):
    if path.parent.name == 'consumed':
        os._exit(91)
    real_write(path, content)
owner_comments._atomic_write = crash_on_consumed
store.consume(
    'websites',
    'oc-20260827t120000z-a1b2c3d4',
    consumed_at='2026-08-27T13:00:00Z',
    actor='actor',
    evidence='evidence',
)
"""
        crashed = subprocess.run(
            [sys.executable, "-c", crash_code, str(REPO / "tools"), str(self.root)],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(crashed.returncode, 91, crashed.stderr)
        transaction_root = self.store._transaction_root()
        self.assertEqual(len(list(transaction_root.glob("txn-*"))), 1)

        subprocess.run(
            ["git", "switch", "-q", "-f", "consumed-state"],
            cwd=self.root,
            check=True,
        )
        expected_destination = destination.read_bytes()
        expected_repo_index = (destination.parent.parent / "README.md").read_bytes()
        expected_root_index = (
            self.root / "docs/owner-comments/index.json"
        ).read_bytes()
        self.assertEqual(
            subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.root,
                capture_output=True,
                text=True,
                check=True,
            ).stdout,
            "",
        )

        with self.assertRaisesRegex(
            ContractError, "Git symbolic HEAD/OID/index tree.*quarantined"
        ):
            self.store.check()
        self.assertFalse(original.exists())
        self.assertEqual(destination.read_bytes(), expected_destination)
        self.assertEqual(
            (destination.parent.parent / "README.md").read_bytes(),
            expected_repo_index,
        )
        self.assertEqual(
            (self.root / "docs/owner-comments/index.json").read_bytes(),
            expected_root_index,
        )
        self.assertFalse(list(transaction_root.glob("txn-*")))
        self.assertEqual(len(list(transaction_root.glob("quarantine-*"))), 1)
        self.assertEqual(self.store.check(), [])
        self.assertEqual(
            subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.root,
                capture_output=True,
                text=True,
                check=True,
            ).stdout,
            "",
        )

    def test_same_tree_branch_switch_quarantines_before_unstaged_edit_restore(
        self,
    ) -> None:
        original = self.write_record()
        self.store.reindex()
        self.commit_baseline("active owner comment")
        main_identity = self.store._git_identity()
        subprocess.run(
            ["git", "branch", "other"], cwd=self.root, check=True
        )

        crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_write = owner_comments._atomic_write
def crash_on_consumed(path, content):
    if path.parent.name == 'consumed':
        os._exit(91)
    real_write(path, content)
owner_comments._atomic_write = crash_on_consumed
store.consume(
    'websites',
    'oc-20260827t120000z-a1b2c3d4',
    consumed_at='2026-08-27T13:00:00Z',
    actor='actor',
    evidence='evidence',
)
"""
        crashed = subprocess.run(
            [sys.executable, "-c", crash_code, str(REPO / "tools"), str(self.root)],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(crashed.returncode, 91, crashed.stderr)
        transaction_root = self.store._transaction_root()
        self.assertEqual(len(list(transaction_root.glob("txn-*"))), 1)

        subprocess.run(
            ["git", "switch", "-q", "-f", "other"],
            cwd=self.root,
            check=True,
        )
        other_identity = self.store._git_identity()
        self.assertEqual(main_identity["head"], other_identity["head"])
        self.assertEqual(
            main_identity["index_tree"], other_identity["index_tree"]
        )
        self.assertEqual(main_identity["head_ref"], "refs/heads/main")
        self.assertEqual(other_identity["head_ref"], "refs/heads/other")

        edited = record()
        edited["comment"] = "Different canonical bytes on the switched branch."
        original.write_bytes(owner_comments._json_bytes(edited))
        destination = original.parent / "consumed" / original.name
        source_before = original.read_bytes()
        destination_before = destination.read_bytes() if destination.exists() else None
        status_before = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=True,
        ).stdout

        with self.assertRaisesRegex(
            ContractError, "Git symbolic HEAD/OID/index tree.*quarantined"
        ):
            self.store.check()
        self.assertEqual(original.read_bytes(), source_before)
        if destination_before is None:
            self.assertFalse(destination.exists())
        else:
            self.assertEqual(destination.read_bytes(), destination_before)
        self.assertEqual(
            subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.root,
                capture_output=True,
                text=True,
                check=True,
            ).stdout,
            status_before,
        )
        self.assertFalse(list(transaction_root.glob("txn-*")))
        self.assertEqual(len(list(transaction_root.glob("quarantine-*"))), 1)

    def test_git_identity_marks_detached_head_explicitly(self) -> None:
        self.commit_baseline("baseline")
        symbolic = self.store._git_identity()
        subprocess.run(
            ["git", "switch", "-q", "--detach"], cwd=self.root, check=True
        )
        detached = self.store._git_identity()
        self.assertEqual(detached["head"], symbolic["head"])
        self.assertEqual(detached["index_tree"], symbolic["index_tree"])
        self.assertEqual(detached["head_ref"], owner_comments.DETACHED_HEAD_REF)

    def test_atomic_write_syncs_parent_directory_after_replace(self) -> None:
        path = self.root / "docs/owner-comments/index.json"
        with mock.patch.object(owner_comments, "_fsync_directory") as sync:
            owner_comments._atomic_write(path, b"replacement\n")
        sync.assert_called_once_with(path.parent)

    def test_atomic_replacements_preserve_modes_and_new_outputs_are_readable(
        self,
    ) -> None:
        existing = self.root / "docs/owner-comments/index.json"
        existing.chmod(0o640)
        observable_existing_mode = stat.S_IMODE(existing.stat().st_mode)
        owner_comments._atomic_write(existing, b"replacement\n")
        self.assertEqual(
            stat.S_IMODE(existing.stat().st_mode), observable_existing_mode
        )

        existing.unlink()
        self.store.reindex()
        self.assert_safe_data_file_mode(existing)

        source = self.write_record()
        source.chmod(0o644)
        self.store.reindex()
        consumed_relative = self.store.consume(
            "websites",
            record()["id"],
            consumed_at="2026-08-27T13:00:00Z",
            actor="actor",
            evidence="evidence",
        )
        consumed = self.root / consumed_relative
        self.assert_safe_data_file_mode(consumed)

    def test_transaction_phases_model_reindex_and_consume_modes_exactly(
        self,
    ) -> None:
        root_index = self.root / "docs/owner-comments/index.json"
        repository_index = (
            self.root / "docs/owner-comments/websites/README.md"
        )
        repository_index.chmod(0o604)
        observed_repository_mode = stat.S_IMODE(
            repository_index.stat().st_mode
        )
        root_index.unlink()
        self.write_record()
        manifests: list[dict] = []
        real_manifest = self.store._transaction_manifest

        def capture_manifest(phases):
            manifest = real_manifest(phases)
            manifests.append(manifest)
            return manifest

        with mock.patch.object(
            self.store,
            "_transaction_manifest",
            side_effect=capture_manifest,
        ):
            self.store.reindex()

        reindex_manifest = manifests.pop()
        reindex_paths = {
            entry["path"]: number
            for number, entry in enumerate(reindex_manifest["entries"])
        }
        initial, final = (
            reindex_manifest["expected_phases"][0],
            reindex_manifest["expected_phases"][-1],
        )
        root_number = reindex_paths["docs/owner-comments/index.json"]
        repository_number = reindex_paths[
            "docs/owner-comments/websites/README.md"
        ]
        self.assertEqual(initial[root_number], {"exists": False})
        self.assertEqual(
            final[root_number]["mode"],
            owner_comments._observable_created_mode(
                owner_comments.DEFAULT_FILE_MODE
            ),
        )
        self.assertEqual(
            initial[repository_number]["mode"], observed_repository_mode
        )
        self.assertEqual(
            final[repository_number]["mode"], observed_repository_mode
        )

        source = (
            self.root
            / "docs/owner-comments/websites"
            / f"{record()['id']}.json"
        )
        source.chmod(0o640)
        root_index.chmod(0o660)
        repository_index.chmod(0o604)
        source_mode = stat.S_IMODE(source.stat().st_mode)
        root_mode = stat.S_IMODE(root_index.stat().st_mode)
        repository_mode = stat.S_IMODE(repository_index.stat().st_mode)
        with mock.patch.object(
            self.store,
            "_transaction_manifest",
            side_effect=capture_manifest,
        ):
            destination_relative = self.store.consume(
                "websites",
                record()["id"],
                consumed_at="2026-08-27T13:00:00Z",
                actor="actor",
                evidence="evidence",
            )

        consume_manifest = manifests.pop()
        consume_paths = {
            entry["path"]: number
            for number, entry in enumerate(consume_manifest["entries"])
        }
        destination_number = consume_paths[destination_relative.as_posix()]
        root_number = consume_paths["docs/owner-comments/index.json"]
        repository_number = consume_paths[
            "docs/owner-comments/websites/README.md"
        ]
        for phase in consume_manifest["expected_phases"][1:]:
            if phase[destination_number]["exists"]:
                self.assertEqual(phase[destination_number]["mode"], source_mode)
        self.assertEqual(
            consume_manifest["expected_phases"][-1][root_number]["mode"],
            root_mode,
        )
        self.assertEqual(
            consume_manifest["expected_phases"][-1][repository_number]["mode"],
            repository_mode,
        )
        self.assertEqual(
            stat.S_IMODE((self.root / destination_relative).stat().st_mode),
            source_mode,
        )
        self.assertEqual(stat.S_IMODE(root_index.stat().st_mode), root_mode)
        self.assertEqual(
            stat.S_IMODE(repository_index.stat().st_mode), repository_mode
        )

    def test_same_byte_mode_edit_at_prepared_boundary_is_not_overwritten(
        self,
    ) -> None:
        target = self.root / "docs/owner-comments/index.json"
        target.chmod(0o640)
        initial_mode = stat.S_IMODE(target.stat().st_mode)
        changed = target.read_bytes() + b"\n"
        backup_root, _manifest = self.publish_test_transaction(
            {target: owner_comments._FileImage(changed, initial_mode)},
            name="prepared-mode-edit",
        )
        owner_comments._atomic_write(target, changed)
        requested_mode = 0o444 if os.name == "nt" else (
            0o600 if initial_mode != 0o600 else 0o640
        )
        target.chmod(requested_mode)
        edited_mode = stat.S_IMODE(target.stat().st_mode)
        self.assertNotEqual(edited_mode, initial_mode)

        try:
            with mock.patch.object(
                self.store, "_restore_entry", wraps=self.store._restore_entry
            ) as restore_entry, self.assertRaisesRegex(
                ContractError, "target bytes/state changed.*quarantined"
            ):
                self.store.check()

            restore_entry.assert_not_called()
            self.assertEqual(target.read_bytes(), changed)
            self.assertEqual(stat.S_IMODE(target.stat().st_mode), edited_mode)
            self.assertFalse(backup_root.exists())
            self.assertEqual(
                len(list(self.store._transaction_root().glob("quarantine-*"))), 1
            )
        finally:
            target.chmod(initial_mode)

    def test_same_byte_mode_edit_at_recovering_boundary_is_not_overwritten(
        self,
    ) -> None:
        target = self.root / "docs/owner-comments/index.json"
        target.chmod(0o640)
        initial_mode = stat.S_IMODE(target.stat().st_mode)
        backup_root, manifest = self.publish_test_transaction(
            {
                target: owner_comments._FileImage(
                    target.read_bytes() + b"\n", initial_mode
                )
            },
            name="recovering-mode-edit",
        )
        manifest["state"] = "recovering"
        manifest["recovery"] = {"phase": 1, "cursor": 1}
        owner_comments._write_transaction_manifest(
            backup_root / "manifest.json", manifest
        )
        original_bytes = target.read_bytes()
        requested_mode = 0o444 if os.name == "nt" else (
            0o600 if initial_mode != 0o600 else 0o640
        )
        target.chmod(requested_mode)
        edited_mode = stat.S_IMODE(target.stat().st_mode)
        self.assertNotEqual(edited_mode, initial_mode)

        try:
            with mock.patch.object(
                self.store, "_restore_entry", wraps=self.store._restore_entry
            ) as restore_entry, self.assertRaisesRegex(
                ContractError, "target bytes/state changed.*quarantined"
            ):
                self.store.check()

            restore_entry.assert_not_called()
            self.assertEqual(target.read_bytes(), original_bytes)
            self.assertEqual(stat.S_IMODE(target.stat().st_mode), edited_mode)
            self.assertFalse(backup_root.exists())
        finally:
            target.chmod(initial_mode)

    def test_transaction_manifest_v6_strictly_validates_file_modes(self) -> None:
        valid = owner_comments._content_state(b"content\n", 0o640)
        self.assertEqual(owner_comments._expected_state_key(valid)[3], 0o640)
        for invalid_mode in (True, -1, 0o10000):
            invalid = dict(valid, mode=invalid_mode)
            self.assertIsNone(owner_comments._expected_state_key(invalid))
        missing = dict(valid)
        missing.pop("mode")
        self.assertIsNone(owner_comments._expected_state_key(missing))

        target = self.root / "docs/owner-comments/index.json"
        mode = stat.S_IMODE(target.stat().st_mode)
        backup_root, manifest = self.publish_test_transaction(
            {
                target: owner_comments._FileImage(
                    target.read_bytes() + b"\n", mode
                )
            },
            name="obsolete-schema",
        )
        manifest["schema_version"] = 5
        owner_comments._write_transaction_manifest(
            backup_root / "manifest.json", manifest
        )
        before = target.read_bytes()
        with self.assertRaisesRegex(
            ContractError, "invalid owner-comment recovery journal.*quarantined"
        ):
            self.store.check()
        self.assertEqual(target.read_bytes(), before)
        self.assertFalse(backup_root.exists())

    def test_atomic_mode_fallback_works_without_fchmod(self) -> None:
        existing = self.root / "existing-mode.json"
        existing.write_bytes(b"old\n")
        existing.chmod(0o640)
        observable_existing_mode = stat.S_IMODE(existing.stat().st_mode)
        created = self.root / "new-mode.json"

        with mock.patch.object(
            owner_comments.os, "fchmod", new=None, create=True
        ), mock.patch.object(owner_comments.os, "chmod", wraps=os.chmod) as chmod:
            owner_comments._atomic_write(existing, b"replacement\n")
            owner_comments._atomic_write(created, b"new\n")

        self.assertGreaterEqual(chmod.call_count, 2)
        self.assertEqual(
            stat.S_IMODE(existing.stat().st_mode), observable_existing_mode
        )
        self.assert_safe_data_file_mode(created)

    def test_atomic_mode_fallback_models_windows_observable_permissions(self) -> None:
        existing = self.root / "existing-windows-mode.json"
        existing.write_bytes(b"old\n")
        existing.chmod(0o666)
        created = self.root / "new-windows-mode.json"
        real_chmod = os.chmod

        def windows_chmod(path: os.PathLike[str] | str, mode: int) -> None:
            # Model Windows' documented read-only/writable distinction while
            # running this regression on the POSIX required-gate runner.
            observable = 0o666 if mode & stat.S_IWRITE else 0o444
            real_chmod(path, observable)

        with mock.patch.object(
            owner_comments.os, "fchmod", new=None, create=True
        ), mock.patch.object(
            owner_comments.os, "chmod", side_effect=windows_chmod
        ):
            owner_comments._atomic_write(existing, b"replacement\n")
            owner_comments._atomic_write(created, b"new\n")

        self.assertEqual(stat.S_IMODE(existing.stat().st_mode), 0o666)
        self.assertEqual(stat.S_IMODE(created.stat().st_mode), 0o666)

    def test_windows_readonly_atomic_write_fails_before_temporary_or_mode_change(
        self,
    ) -> None:
        target = self.root / "readonly-index.json"
        target.write_bytes(b"old\n")
        target.chmod(0o444)

        with self.windows_readonly_semantics() as replacements:
            with self.assertRaisesRegex(ContractError, "read-only.*unsupported"):
                owner_comments._atomic_write(target, b"new\n")

        self.assertEqual(target.read_bytes(), b"old\n")
        self.assertEqual(stat.S_IMODE(target.stat().st_mode), 0o444)
        self.assertEqual(replacements, [])
        self.assertEqual(list(self.root.glob(".readonly-index.json.*")), [])

    def test_windows_reparse_classifier_allows_only_nonredirect_regular_files(
        self,
    ) -> None:
        cloud_file = mock.Mock(
            st_mode=stat.S_IFREG | 0o644,
            st_file_attributes=owner_comments._WINDOWS_REPARSE_POINT,
            st_reparse_tag=0x9000001A,
        )
        cloud_directory = mock.Mock(
            st_mode=stat.S_IFDIR | 0o755,
            st_file_attributes=owner_comments._WINDOWS_REPARSE_POINT,
            st_reparse_tag=0x9000001A,
        )
        mount_file = mock.Mock(
            st_mode=stat.S_IFREG | 0o644,
            st_file_attributes=owner_comments._WINDOWS_REPARSE_POINT,
            st_reparse_tag=0xA0000003,
        )
        path = self.root / "modeled-reparse"

        self.assertFalse(owner_comments._is_link_or_reparse(path, cloud_file))
        self.assertTrue(owner_comments._is_link_or_reparse(path, cloud_directory))
        self.assertTrue(owner_comments._is_link_or_reparse(path, mount_file))

    def test_atomic_cleanup_failure_never_masks_original_error(self) -> None:
        target = self.root / "cleanup-mask.json"
        target.write_bytes(b"old\n")
        with mock.patch.object(
            owner_comments.os,
            "replace",
            side_effect=OSError(errno.EIO, "original replacement failure"),
        ), mock.patch.object(
            owner_comments,
            "_unlink_windows_compatible",
            side_effect=PermissionError(errno.EACCES, "cleanup denied"),
        ):
            with self.assertRaisesRegex(OSError, "original replacement failure"):
                owner_comments._atomic_write(target, b"new\n")

    def test_windows_readonly_scratch_cleanup_fails_closed_without_mode_change(self) -> None:
        temporary = self.root / ".readonly-cleanup"
        temporary.write_bytes(b"scratch\n")
        temporary.chmod(0o444)

        with self.windows_readonly_semantics():
            with self.assertRaisesRegex(ContractError, "read-only.*unsupported"):
                owner_comments._unlink_windows_compatible(temporary)

        self.assertTrue(temporary.is_file())
        self.assertEqual(stat.S_IMODE(temporary.stat().st_mode), 0o444)

    def test_windows_readonly_reindex_rejects_before_journal_or_write(self) -> None:
        target = self.root / "docs/owner-comments/index.json"
        peer = self.root / "linked-reindex-index.json"
        os.link(target, peer)
        target.chmod(0o444)
        repository_index = self.root / "docs/owner-comments/websites/README.md"
        before_target = target.read_bytes()
        before_repository_index = repository_index.read_bytes()
        before_mode = stat.S_IMODE(target.stat().st_mode)
        self.write_record()
        transaction_root = self.store._transaction_root()

        with self.windows_readonly_semantics() as replacements:
            with self.assertRaisesRegex(ContractError, "read-only.*unsupported"):
                self.store.reindex()

        self.assertEqual(target.read_bytes(), before_target)
        self.assertEqual(peer.read_bytes(), before_target)
        self.assertEqual(repository_index.read_bytes(), before_repository_index)
        self.assertEqual(stat.S_IMODE(target.stat().st_mode), before_mode)
        self.assertEqual(stat.S_IMODE(peer.stat().st_mode), before_mode)
        self.assertEqual(replacements, [])
        self.assertEqual(list(transaction_root.glob("txn-*")), [])
        self.assertEqual(list(transaction_root.glob("quarantine-*")), [])
        self.assertEqual(
            list((self.root / "docs/owner-comments").rglob(".*.atomic-*")), []
        )

    def test_windows_readonly_linked_source_rejects_consume_without_journal(self) -> None:
        source = self.write_record()
        self.store.reindex()
        peer = self.root / "linked-owner-comment.json"
        os.link(source, peer)
        source.chmod(0o444)
        before_source = source.read_bytes()
        before_root = (self.root / "docs/owner-comments/index.json").read_bytes()
        before_repository = (source.parent / "README.md").read_bytes()
        destination = source.parent / "consumed" / source.name
        transaction_root = self.store._transaction_root()

        with self.windows_readonly_semantics() as replacements:
            with self.assertRaisesRegex(ContractError, "read-only.*unsupported"):
                self.store.consume(
                    "websites",
                    record()["id"],
                    consumed_at="2026-08-27T13:00:00Z",
                    actor="actor",
                    evidence="evidence",
                )

        self.assertEqual(source.read_bytes(), before_source)
        self.assertEqual(peer.read_bytes(), before_source)
        self.assertTrue(os.path.samefile(source, peer))
        self.assertEqual(stat.S_IMODE(source.stat().st_mode), 0o444)
        self.assertFalse(destination.exists())
        self.assertFalse(destination.parent.exists())
        self.assertEqual(
            (self.root / "docs/owner-comments/index.json").read_bytes(), before_root
        )
        self.assertEqual((source.parent / "README.md").read_bytes(), before_repository)
        self.assertEqual(replacements, [])
        self.assertEqual(list(transaction_root.glob("txn-*")), [])
        self.assertEqual(list(transaction_root.glob("quarantine-*")), [])

    def test_windows_writable_consume_remains_supported(self) -> None:
        source = self.write_record()
        source.chmod(0o666)
        self.store.reindex()

        with self.windows_readonly_semantics() as replacements:
            consumed_relative = self.store.consume(
                "websites",
                record()["id"],
                consumed_at="2026-08-27T13:00:00Z",
                actor="actor",
                evidence="evidence",
            )

        destination = self.root / consumed_relative
        self.assertFalse(source.exists())
        self.assertTrue(destination.is_file())
        self.assertEqual(json.loads(destination.read_text())["state"], "consumed")
        self.assertTrue(replacements)
        self.assertEqual(self.store.check(), [])

    def test_identity_quarantine_preserves_matching_target_mode_only_edit(self) -> None:
        original = self.write_record()
        self.store.reindex()
        self.commit_baseline("active owner comment")
        crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_write = owner_comments._atomic_write
def crash_on_consumed(path, content):
    if path.parent.name == 'consumed':
        os._exit(97)
    real_write(path, content)
owner_comments._atomic_write = crash_on_consumed
store.consume(
    'websites',
    'oc-20260827t120000z-a1b2c3d4',
    consumed_at='2026-08-27T13:00:00Z',
    actor='actor',
    evidence='evidence',
)
"""
        crashed = subprocess.run(
            [
                sys.executable,
                "-c",
                crash_code,
                str(REPO / "tools"),
                str(self.root),
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(crashed.returncode, 97, crashed.stderr)
        destination = original.parent / "consumed" / original.name
        self.assertFalse(original.exists())
        self.assertTrue(destination.is_file())
        matching_bytes = destination.read_bytes()
        destination.chmod(0o444)

        estate = self.root / "docs/ESTATE.md"
        write_lf(estate, estate.read_text(encoding="utf-8") + "\n")
        subprocess.run(["git", "add", "docs/ESTATE.md"], cwd=self.root, check=True)

        with mock.patch.object(owner_comments, "_is_windows", return_value=True):
            with self.assertRaisesRegex(
                ContractError, "Git symbolic HEAD/OID/index tree changed"
            ):
                self.store.check()

        self.assertEqual(destination.read_bytes(), matching_bytes)
        self.assertEqual(stat.S_IMODE(destination.stat().st_mode), 0o444)
        transaction_root = self.store._transaction_root()
        self.assertEqual(list(transaction_root.glob("txn-*")), [])
        self.assertEqual(len(list(transaction_root.glob("quarantine-*"))), 1)

    def test_directory_fsync_is_explicitly_unsupported_on_windows(self) -> None:
        directory = self.root / "docs/owner-comments"
        with mock.patch.object(owner_comments, "_is_windows", return_value=True), mock.patch.object(
            owner_comments.os, "open"
        ) as opened, mock.patch.object(owner_comments.os, "fsync") as fsync:
            owner_comments._fsync_directory(directory)

        opened.assert_not_called()
        fsync.assert_not_called()

    def test_directory_fsync_propagates_io_errors_only(self) -> None:
        directory = self.root / "docs/owner-comments"
        with mock.patch.object(
            owner_comments, "_is_windows", return_value=False
        ), mock.patch.object(
            owner_comments.os, "open", return_value=123
        ), mock.patch.object(owner_comments.os, "close"), mock.patch.object(
            owner_comments.os, "fsync",
            side_effect=OSError(errno.EINVAL, "directory fsync unsupported"),
        ):
            owner_comments._fsync_directory(directory)

        with mock.patch.object(
            owner_comments, "_is_windows", return_value=False
        ), mock.patch.object(
            owner_comments.os, "open", return_value=123
        ), mock.patch.object(owner_comments.os, "close"), mock.patch.object(
            owner_comments.os, "fsync",
            side_effect=OSError(errno.EIO, "storage I/O failure"),
        ):
            with self.assertRaisesRegex(OSError, "storage I/O failure"):
                owner_comments._fsync_directory(directory)

        with mock.patch.object(
            owner_comments, "_is_windows", return_value=False
        ), mock.patch.object(
            owner_comments.os,
            "open",
            side_effect=OSError(errno.EIO, "directory open I/O failure"),
        ):
            with self.assertRaisesRegex(OSError, "directory open I/O failure"):
                owner_comments._fsync_directory(directory)

        with mock.patch.object(owner_comments, "_is_windows", return_value=False), mock.patch.object(
            owner_comments.os,
            "open",
            side_effect=PermissionError(errno.EACCES, "directory open denied"),
        ):
            with self.assertRaisesRegex(PermissionError, "directory open denied"):
                owner_comments._fsync_directory(directory)

    def test_file_fsync_uses_a_write_capable_descriptor_on_windows(self) -> None:
        path = self.root / "docs/owner-comments/index.json"
        opened = mock.mock_open()
        with mock.patch.object(
            owner_comments, "_is_windows", return_value=True
        ), mock.patch.object(Path, "open", opened), mock.patch.object(
            owner_comments.os, "fsync"
        ) as fsync:
            owner_comments._fsync_file(path)

        opened.assert_called_once_with("r+b")
        fsync.assert_called_once()

    def test_new_transaction_root_is_durable_before_manifest_publication(self) -> None:
        self.write_record()
        self.store.reindex()
        transaction_root = self.store._transaction_root()
        self.assertEqual(list(transaction_root.iterdir()), [])
        transaction_root.rmdir()
        events: list[tuple[str, object]] = []
        real_sync = owner_comments._fsync_directory
        real_manifest_write = owner_comments._write_transaction_manifest

        def track_sync(path: Path) -> None:
            events.append(("sync", path))
            real_sync(path)

        def track_manifest(path: Path, data: dict) -> None:
            events.append(("manifest", data["state"]))
            real_manifest_write(path, data)

        with mock.patch.object(
            owner_comments, "_fsync_directory", side_effect=track_sync
        ), mock.patch.object(
            owner_comments,
            "_write_transaction_manifest",
            side_effect=track_manifest,
        ):
            self.store.consume(
                "websites",
                record()["id"],
                consumed_at="2026-08-27T13:00:00Z",
                actor="actor",
                evidence="evidence",
            )

        parent_sync = events.index(("sync", transaction_root.parent))
        prepared_manifest = events.index(("manifest", "prepared"))
        self.assertLess(parent_sync, prepared_manifest)

    def test_commit_manifest_sync_failure_uses_prepared_state_to_roll_back(self) -> None:
        generated = (
            self.root / "docs/owner-comments/index.json",
            self.root / "docs/owner-comments/websites/README.md",
        )
        before = {path: path.read_bytes() for path in generated}
        self.write_record()
        real_sync = owner_comments._fsync_directory
        failed = False

        def fail_after_committed_manifest_replace(path: Path) -> None:
            nonlocal failed
            manifest_path = path / "manifest.json"
            if not failed and manifest_path.is_file():
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                if manifest.get("state") == "committed":
                    failed = True
                    raise OSError(
                        errno.EIO,
                        "simulated final manifest directory sync failure",
                    )
            real_sync(path)

        with mock.patch.object(
            owner_comments,
            "_fsync_directory",
            side_effect=fail_after_committed_manifest_replace,
        ):
            with self.assertRaisesRegex(
                OSError, "final manifest directory sync failure"
            ):
                self.store.reindex()

        self.assertTrue(failed)
        self.assertEqual(
            {path: path.read_bytes() for path in generated},
            before,
        )
        self.assertEqual(list(self.store._transaction_root().glob("txn-*")), [])

    def test_manifestless_published_journal_finishes_committed_cleanup(self) -> None:
        transaction_root = self.store._transaction_root()
        residue = transaction_root / "txn-interrupted-cleanup"
        residue.mkdir(parents=True)
        write_lf(residue / "partial-backup", "residue\n")
        self.assertEqual(self.store.check(), [])
        self.assertFalse(residue.exists())

    def test_journal_cleanup_io_failure_is_retryable_not_a_false_mutation_failure(
        self,
    ) -> None:
        transaction_root = self.store._transaction_root()
        residue = transaction_root / "txn-retry-cleanup"
        residue.mkdir(parents=True)
        with mock.patch.object(
            owner_comments.shutil,
            "rmtree",
            side_effect=OSError(errno.EIO, "cleanup unavailable"),
        ):
            self.assertEqual(self.store.check(), [])
        self.assertTrue(residue.is_dir())
        self.assertEqual(self.store.check(), [])
        self.assertFalse(residue.exists())

    def test_baseexception_during_consume_rolls_back_move_and_indexes(self) -> None:
        original = self.write_record()
        self.store.reindex()
        real_write = owner_comments._atomic_write
        calls = 0

        def interrupt_once(path: Path, content: bytes) -> None:
            nonlocal calls
            calls += 1
            if calls == 1:
                raise KeyboardInterrupt
            real_write(path, content)

        with mock.patch.object(
            owner_comments, "_atomic_write", side_effect=interrupt_once
        ):
            with self.assertRaises(KeyboardInterrupt):
                self.store.consume(
                    "websites",
                    record()["id"],
                    consumed_at="2026-08-27T13:00:00Z",
                    actor="actor",
                    evidence="evidence",
                )
        self.assertTrue(original.is_file())
        self.assertFalse(
            (original.parent / "consumed" / original.name).exists()
        )
        self.assertEqual(self.store.check(), [])

    def test_persistent_writer_failure_rolls_back_without_using_writer(self) -> None:
        original = self.write_record()
        self.store.reindex()
        root_before = (self.root / "docs/owner-comments/index.json").read_bytes()
        repo_before = (original.parent / "README.md").read_bytes()
        with mock.patch.object(
            owner_comments, "_atomic_write", side_effect=OSError("disk refused")
        ):
            with self.assertRaisesRegex(OSError, "disk refused"):
                self.store.consume(
                    "websites",
                    record()["id"],
                    consumed_at="2026-08-27T13:00:00Z",
                    actor="actor",
                    evidence="evidence",
                )
        self.assertTrue(original.is_file())
        self.assertFalse((original.parent / "consumed" / original.name).exists())
        self.assertEqual(
            (self.root / "docs/owner-comments/index.json").read_bytes(), root_before
        )
        self.assertEqual((original.parent / "README.md").read_bytes(), repo_before)
        self.assertEqual(self.store.check(), [])

    def test_standalone_reindex_rolls_back_all_projection_writes(self) -> None:
        path = self.root / "docs/owner-comments/websites"
        root_index = self.root / "docs/owner-comments/index.json"
        root_before = root_index.read_bytes()
        repo_before = (path / "README.md").read_bytes()
        self.write_record()
        real_write = owner_comments._atomic_write
        calls = 0

        def fail_second(write_path: Path, content: bytes) -> None:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("second projection write refused")
            real_write(write_path, content)

        with mock.patch.object(owner_comments, "_atomic_write", side_effect=fail_second):
            with self.assertRaisesRegex(OSError, "second projection write refused"):
                self.store.reindex()
        self.assertEqual(root_index.read_bytes(), root_before)
        self.assertEqual((path / "README.md").read_bytes(), repo_before)
        self.assertTrue(any("stale" in error for error in self.store.check()))

    def test_closed_tree_rejects_stray_files_and_uppercase_json_suffix(self) -> None:
        repository = self.root / "docs/owner-comments/websites"
        write_lf(repository / "notes.txt", "not a record\n")
        write_lf(repository / "comment.JSON", "{}\n")
        consumed = repository / "consumed"
        consumed.mkdir()
        write_lf(consumed / "notes.txt", "not a record\n")
        errors = self.store.check()
        self.assertGreaterEqual(
            sum("only" in error and "json" in error for error in errors), 3
        )

    def test_repository_and_consumed_symlinks_are_refused_without_escape(self) -> None:
        outside_repository = self.root / "outside-repository"
        outside_consumed = self.root / "outside-consumed"
        outside_repository.mkdir()
        outside_consumed.mkdir()

        repository = self.root / "docs/owner-comments/websites"
        shutil.rmtree(repository)
        self.symlink_or_skip(
            repository, outside_repository, target_is_directory=True
        )
        consumed = self.root / "docs/owner-comments/fleet-manager/consumed"
        self.symlink_or_skip(consumed, outside_consumed, target_is_directory=True)

        errors = self.store.check()
        self.assertTrue(any("repository path" in error for error in errors), errors)
        self.assertTrue(any("consumed must be a real directory" in error for error in errors), errors)
        with self.assertRaises(ContractError):
            self.store.reindex()
        self.assertEqual(list(outside_repository.iterdir()), [])
        self.assertEqual(list(outside_consumed.iterdir()), [])

    def test_windows_reparse_storage_ancestors_fail_before_mutation(self) -> None:
        self.write_record()
        self.store.reindex()
        transaction_root = self.store._transaction_root()
        root_before = (self.root / "docs/owner-comments/index.json").read_bytes()

        for path in (
            self.root,
            self.root / "docs",
            self.root / "docs/owner-comments",
        ):
            with self.subTest(path=path), self.windows_reparse_semantics(path):
                errors = self.store.check()
                self.assertTrue(
                    any("junction, or reparse point" in error for error in errors),
                    errors,
                )
                with self.assertRaisesRegex(
                    ContractError, "junction, or reparse point"
                ):
                    self.store.reindex()

        self.assertEqual(
            (self.root / "docs/owner-comments/index.json").read_bytes(), root_before
        )
        self.assertEqual(list(transaction_root.glob("txn-*")), [])

    def test_windows_reparse_repository_and_consumed_are_not_traversed(self) -> None:
        repository = self.root / "docs/owner-comments/websites"
        consumed = repository / "consumed"
        consumed.mkdir()
        real_iterdir = Path.iterdir

        for path, expected in (
            (repository, "repository path"),
            (consumed, "consumed must be a real directory"),
        ):
            def guarded_iterdir(candidate, *, forbidden=path):
                if candidate == forbidden:
                    raise AssertionError(f"traversed mocked reparse point {forbidden}")
                return real_iterdir(candidate)

            with self.subTest(path=path), self.windows_reparse_semantics(
                path
            ), mock.patch.object(Path, "iterdir", guarded_iterdir):
                records, errors = self.store.scan()
                self.assertEqual(records, [])
                self.assertTrue(any(expected in error for error in errors), errors)
                with self.assertRaisesRegex(ContractError, "reparse point"):
                    self.store.reindex()

    def test_windows_reparse_target_parent_quarantines_before_recovery(self) -> None:
        original = self.write_record()
        self.store.reindex()
        crash_code = """
import os
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import owner_comments
store = owner_comments.OwnerCommentsStore(Path(sys.argv[2]))
real_write = owner_comments._atomic_write
def crash_on_consumed(path, content):
    if path.parent.name == 'consumed':
        os._exit(99)
    real_write(path, content)
owner_comments._atomic_write = crash_on_consumed
store.consume(
    'websites',
    'oc-20260827t120000z-a1b2c3d4',
    consumed_at='2026-08-27T13:00:00Z',
    actor='actor',
    evidence='evidence',
)
"""
        crashed = subprocess.run(
            [sys.executable, "-c", crash_code, str(REPO / "tools"), str(self.root)],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(crashed.returncode, 99, crashed.stderr)
        destination = original.parent / "consumed" / original.name
        before = destination.read_bytes()
        transaction_root = self.store._transaction_root()
        self.assertEqual(len(list(transaction_root.glob("txn-*"))), 1)

        with self.windows_reparse_semantics(original.parent), mock.patch.object(
            self.store, "_restore_entry", wraps=self.store._restore_entry
        ) as restore_entry:
            with self.assertRaisesRegex(
                ContractError, "invalid owner-comment recovery journal.*quarantined"
            ):
                self.store.check()

        restore_entry.assert_not_called()
        self.assertFalse(original.exists())
        self.assertEqual(destination.read_bytes(), before)
        self.assertEqual(list(transaction_root.glob("txn-*")), [])
        self.assertEqual(len(list(transaction_root.glob("quarantine-*"))), 1)

    def test_windows_reparse_transaction_root_is_not_traversed_or_deleted(
        self,
    ) -> None:
        transaction_root = self.store._transaction_root()
        sentinel = transaction_root / "external-sentinel"
        sentinel.write_bytes(b"external bytes\n")
        real_iterdir = Path.iterdir

        def guarded_iterdir(path):
            if path == transaction_root:
                raise AssertionError("traversed mocked transaction-root junction")
            return real_iterdir(path)

        with self.windows_reparse_semantics(transaction_root), mock.patch.object(
            Path, "iterdir", guarded_iterdir
        ), mock.patch.object(
            owner_comments.shutil, "rmtree"
        ) as remove_tree, self.assertRaisesRegex(
            ContractError, "transaction root.*junction, or reparse point"
        ):
            self.store.check()

        remove_tree.assert_not_called()
        self.assertEqual(sentinel.read_bytes(), b"external bytes\n")

    def test_windows_reparse_transaction_child_is_not_read_or_deleted(
        self,
    ) -> None:
        transaction_root = self.store._transaction_root()
        transaction = transaction_root / "txn-external-target"
        transaction.mkdir()
        sentinel = transaction / "external-sentinel"
        sentinel.write_bytes(b"external bytes\n")

        with self.windows_reparse_semantics(transaction), mock.patch.object(
            self.store, "_read_transaction_manifest"
        ) as read_manifest, mock.patch.object(
            owner_comments.shutil, "rmtree"
        ) as remove_tree, self.assertRaisesRegex(
            ContractError, "transaction directory.*junction, or reparse point"
        ):
            self.store.check()

        read_manifest.assert_not_called()
        remove_tree.assert_not_called()
        self.assertEqual(sentinel.read_bytes(), b"external bytes\n")

    def test_windows_reparse_initializing_and_quarantine_paths_fail_closed(
        self,
    ) -> None:
        transaction_root = self.store._transaction_root()
        initializing = transaction_root / ".initializing-external-target"
        initializing.mkdir()
        initializing_sentinel = initializing / "external-sentinel"
        initializing_sentinel.write_bytes(b"initializing external bytes\n")
        self.write_record()

        with self.windows_reparse_semantics(initializing), mock.patch.object(
            owner_comments.tempfile,
            "mkdtemp",
            return_value=str(initializing),
        ), mock.patch.object(
            owner_comments.shutil, "copy2"
        ) as copy_file, mock.patch.object(
            owner_comments.shutil, "rmtree"
        ) as remove_tree, self.assertRaisesRegex(
            ContractError, "transaction directory.*junction, or reparse point"
        ):
            self.store.reindex()

        copy_file.assert_not_called()
        remove_tree.assert_not_called()
        self.assertEqual(
            initializing_sentinel.read_bytes(), b"initializing external bytes\n"
        )

        # A deterministic quarantine collision must likewise be inspected and
        # left untouched rather than renamed over or traversed.
        target = self.root / "docs/owner-comments/index.json"
        target_mode = stat.S_IMODE(target.stat().st_mode)
        backup_root, _manifest = self.publish_test_transaction(
            {
                target: owner_comments._FileImage(
                    target.read_bytes() + b"\n", target_mode
                )
            },
            name="external-target",
        )
        target.write_bytes(target.read_bytes() + b"owner change\n")
        quarantine = transaction_root / "quarantine-external-target"
        quarantine.mkdir()
        quarantine_sentinel = quarantine / "external-sentinel"
        quarantine_sentinel.write_bytes(b"quarantine external bytes\n")

        with self.windows_reparse_semantics(quarantine), mock.patch.object(
            owner_comments.os, "rename", wraps=os.rename
        ) as rename, self.assertRaisesRegex(
            ContractError, "transaction directory.*junction, or reparse point"
        ):
            self.store.check()

        rename.assert_not_called()
        self.assertTrue(backup_root.is_dir())
        self.assertEqual(
            quarantine_sentinel.read_bytes(), b"quarantine external bytes\n"
        )

    def test_symlinked_docs_ancestor_never_reads_or_writes_external_store(self) -> None:
        self.write_record()
        self.store.reindex()
        with tempfile.TemporaryDirectory() as external_temp:
            external_docs = Path(external_temp) / "docs"
            shutil.copytree(self.root / "docs", external_docs)
            before = {
                path.relative_to(external_docs): path.read_bytes()
                for path in external_docs.rglob("*")
                if path.is_file()
            }
            shutil.rmtree(self.root / "docs")
            self.symlink_or_skip(
                self.root / "docs", external_docs, target_is_directory=True
            )

            errors = self.store.check()
            self.assertTrue(any("storage ancestor" in error for error in errors), errors)
            with self.assertRaisesRegex(ContractError, "storage ancestor"):
                self.store.reindex()
            with self.assertRaisesRegex(ContractError, "storage ancestor"):
                self.store.consume(
                    "websites",
                    record()["id"],
                    consumed_at="2026-08-27T13:00:00Z",
                    actor="actor",
                    evidence="evidence",
                )

            after = {
                path.relative_to(external_docs): path.read_bytes()
                for path in external_docs.rglob("*")
                if path.is_file()
            }
            self.assertEqual(after, before)
            transaction_root = self.store._transaction_root()
            self.assertEqual(list(transaction_root.glob("txn-*")), [])

    def test_symlinked_store_root_is_not_resolved_away(self) -> None:
        alias = self.root.parent / f"{self.root.name}-owner-comments-alias"
        self.symlink_or_skip(alias, self.root, target_is_directory=True)
        try:
            aliased_store = OwnerCommentsStore(alias)
            errors = aliased_store.check()
            self.assertTrue(any("storage ancestor" in error for error in errors), errors)
            with self.assertRaisesRegex(ContractError, "storage ancestor"):
                aliased_store.reindex()
        finally:
            alias.unlink()

    def test_symlinked_parent_aliases_share_store_lock_and_journal_identity(
        self,
    ) -> None:
        alias_parent = self.root.parent / f"{self.root.name}-parent-alias"
        self.symlink_or_skip(
            alias_parent, self.root.parent, target_is_directory=True
        )
        try:
            aliased_store = OwnerCommentsStore(alias_parent / self.root.name)
            self.assertEqual(aliased_store.root, self.store.root)
            self.assertEqual(aliased_store._lock_path(), self.store._lock_path())
            self.assertEqual(
                aliased_store._transaction_root(), self.store._transaction_root()
            )
            target = self.root / "docs/owner-comments/index.json"
            phase = {
                target: owner_comments._FileImage(
                    target.read_bytes(), stat.S_IMODE(target.stat().st_mode)
                )
            }
            manifest = aliased_store._transaction_manifest((phase,))
            self.assertEqual(manifest["root"], str(self.store.root))
            backup_root = aliased_store._transaction_root() / "txn-alias-recovery"
            backup_root.mkdir(parents=True)
            shutil.copy2(target, backup_root / "0")
            owner_comments._write_transaction_manifest(
                backup_root / "manifest.json", manifest
            )
            self.assertEqual(self.store.check(), [])
            self.assertFalse(backup_root.exists())
            self.assertEqual(aliased_store.check(), [])
        finally:
            alias_parent.unlink()

    def test_symlinked_owner_comments_ancestor_never_writes_external_store(
        self,
    ) -> None:
        self.write_record()
        self.store.reindex()
        with tempfile.TemporaryDirectory() as external_temp:
            external_comments = Path(external_temp) / "owner-comments"
            shutil.copytree(self.root / "docs/owner-comments", external_comments)
            before = {
                path.relative_to(external_comments): path.read_bytes()
                for path in external_comments.rglob("*")
                if path.is_file()
            }
            shutil.rmtree(self.root / "docs/owner-comments")
            self.symlink_or_skip(
                self.root / "docs/owner-comments",
                external_comments,
                target_is_directory=True,
            )

            errors = self.store.check()
            self.assertTrue(any("storage ancestor" in error for error in errors), errors)
            with self.assertRaisesRegex(ContractError, "storage ancestor"):
                self.store.reindex()
            with self.assertRaisesRegex(ContractError, "storage ancestor"):
                self.store.consume(
                    "websites",
                    record()["id"],
                    consumed_at="2026-08-27T13:00:00Z",
                    actor="actor",
                    evidence="evidence",
                )

            after = {
                path.relative_to(external_comments): path.read_bytes()
                for path in external_comments.rglob("*")
                if path.is_file()
            }
            self.assertEqual(after, before)
            transaction_root = self.store._transaction_root()
            self.assertEqual(list(transaction_root.glob("txn-*")), [])

    def test_malformed_state_and_unicode_surrogate_fail_without_crashing(self) -> None:
        path = self.write_record()
        for invalid_state in ([], {}):
            payload = record()
            payload["state"] = invalid_state
            write_lf(
                path,
                json.dumps(payload, indent=2, sort_keys=True) + "\n",
            )
            errors = self.store.check()
            self.assertTrue(any("state must be" in error for error in errors), errors)

        payload = record()
        payload["comment"] = "\ud800"
        path.write_bytes(
            (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("ascii")
        )
        errors = self.store.check()
        self.assertTrue(any("invalid Unicode surrogate" in error for error in errors), errors)

    def test_ids_are_portable_path_and_git_ref_components(self) -> None:
        for comment_id in (
            "con",
            "con.note",
            "abc..def",
            "abc.",
            "abc.lock",
            "COM1",
        ):
            payload = record()
            payload["id"] = comment_id
            errors = owner_comments.validate_record(payload)
            self.assertTrue(any("path/ref-safe" in error for error in errors), comment_id)

    def test_schema_artifact_is_required_and_pinned_to_executable_contract(self) -> None:
        schema = self.root / "docs/owner-comments/record.schema.json"
        parsed = json.loads(schema.read_text(encoding="utf-8"))
        repository_pattern = re.compile(parsed["properties"]["repository"]["pattern"])
        comment_pattern = re.compile(parsed["properties"]["comment"]["pattern"])
        self.assertIsNotNone(repository_pattern.fullmatch("Substrate-kit-app"))
        self.assertIsNone(repository_pattern.fullmatch("repo."))
        self.assertIsNone(repository_pattern.fullmatch("CON"))
        self.assertIsNone(repository_pattern.fullmatch("README.md"))
        self.assertIsNotNone(comment_pattern.search("\nowner wording"))
        self.assertIsNone(comment_pattern.search("\x00owner wording"))
        self.assertIsNone(comment_pattern.search("\ud800owner wording"))

        explicit_null = record()
        explicit_null["consumption"] = None
        errors = owner_comments.validate_record(explicit_null)
        self.assertTrue(any("must not have consumption" in error for error in errors))

        write_lf(schema, "{}\n")
        errors = self.store.check()
        self.assertTrue(any("schema artifact differs" in error for error in errors), errors)
        schema.unlink()
        errors = self.store.check()
        self.assertTrue(any("missing required" in error for error in errors), errors)

    def test_git_lifecycle_allows_only_active_to_consumed_transition(self) -> None:
        self.write_record()
        self.store.reindex()
        self.commit_baseline("active owner comment")
        self.store.consume(
            "websites",
            record()["id"],
            consumed_at="2026-08-27T13:00:00Z",
            actor="actor",
            evidence="evidence",
        )
        self.assertEqual(self.store.check(), [])

    def test_git_index_blob_bytes_are_validated_before_eol_checkout_normalization(self) -> None:
        path = self.write_record()
        self.store.reindex()
        self.commit_baseline("active owner comment")
        crlf = path.read_bytes().replace(b"\n", b"\r\n")
        blob = subprocess.run(
            ["git", "hash-object", "-w", "--stdin"],
            cwd=self.root,
            input=crlf,
            capture_output=True,
            check=True,
        ).stdout.decode("ascii").strip()
        relative = path.relative_to(self.root).as_posix()
        subprocess.run(
            ["git", "update-index", "--cacheinfo", "100644", blob, relative],
            cwd=self.root,
            check=True,
        )
        self.assertNotIn(b"\r", path.read_bytes())
        errors = self.store.check()
        self.assertTrue(any("staged blob contains CR" in error for error in errors), errors)

    def test_staged_candidate_validates_schema_and_lifecycle_when_worktree_is_fixed(
        self,
    ) -> None:
        path = self.write_record()
        self.store.reindex()
        self.commit_baseline("active owner comment")
        baseline = path.read_bytes()

        invalid = record()
        invalid["comment"] = "   "
        path.write_bytes(owner_comments._json_bytes(invalid))
        subprocess.run(["git", "add", str(path)], cwd=self.root, check=True)
        path.write_bytes(baseline)
        errors = self.store.check()
        self.assertTrue(
            any(
                "staged candidate:" in error and "non-whitespace" in error
                for error in errors
            ),
            errors,
        )

        rewritten = record()
        rewritten["comment"] = "A schema-valid rewrite that violates append-only history."
        path.write_bytes(owner_comments._json_bytes(rewritten))
        subprocess.run(["git", "add", str(path)], cwd=self.root, check=True)
        path.write_bytes(baseline)
        errors = self.store.check()
        self.assertTrue(
            any(
                "staged candidate:" in error and "active record" in error
                for error in errors
            ),
            errors,
        )

    def test_staged_candidate_requires_matching_generated_indexes(self) -> None:
        self.commit_baseline("empty owner-comment ledger")
        path = self.write_record()
        self.store.reindex()
        subprocess.run(["git", "add", str(path)], cwd=self.root, check=True)

        errors = self.store.check()
        self.assertTrue(
            any(
                "staged candidate: docs/owner-comments/index.json" in error
                and "stale" in error
                for error in errors
            ),
            errors,
        )
        self.assertTrue(
            any(
                "staged candidate: docs/owner-comments/websites/README.md" in error
                and "stale" in error
                for error in errors
            ),
            errors,
        )

        subprocess.run(
            [
                "git",
                "add",
                "docs/owner-comments/index.json",
                "docs/owner-comments/websites/README.md",
            ],
            cwd=self.root,
            check=True,
        )
        self.assertEqual(self.store.check(), [])

    def test_staged_candidate_rejects_cached_deletion_retained_in_worktree(
        self,
    ) -> None:
        path = self.write_record()
        self.store.reindex()
        self.commit_baseline("active owner comment")
        subprocess.run(
            ["git", "rm", "-q", "--cached", str(path)],
            cwd=self.root,
            check=True,
        )
        self.assertTrue(path.is_file())
        errors = self.store.check()
        self.assertTrue(
            any(
                "staged candidate:" in error and "was deleted" in error
                for error in errors
            ),
            errors,
        )

    def test_git_lifecycle_rejects_active_edit_and_delete(self) -> None:
        path = self.write_record()
        self.store.reindex()
        self.commit_baseline("active owner comment")

        edited = record()
        edited["comment"] = "changed after it became durable"
        write_lf(
            path,
            json.dumps(edited, indent=2, sort_keys=True) + "\n",
        )
        self.store.reindex()
        errors = self.store.check()
        self.assertTrue(any("active record" in error for error in errors), errors)

        path.unlink()
        self.store.reindex()
        errors = self.store.check()
        self.assertTrue(any("was deleted" in error for error in errors), errors)

    def test_git_lifecycle_rejects_consumed_edit_delete_and_reopen(self) -> None:
        self.write_record()
        self.store.reindex()
        destination = self.store.consume(
            "websites",
            record()["id"],
            consumed_at="2026-08-27T13:00:00Z",
            actor="actor",
            evidence="evidence",
        )
        consumed = self.root / destination
        baseline_bytes = consumed.read_bytes()
        self.commit_baseline("consumed owner comment")

        payload = json.loads(baseline_bytes)
        payload["comment"] = "history rewritten"
        consumed.write_bytes(owner_comments._json_bytes(payload))
        self.store.reindex()
        errors = self.store.check()
        self.assertTrue(any("consumed record" in error for error in errors), errors)

        consumed.unlink()
        self.store.reindex()
        errors = self.store.check()
        self.assertTrue(any("was deleted" in error for error in errors), errors)

        active = consumed.parent.parent / consumed.name
        reopened = record()
        active.write_bytes(owner_comments._json_bytes(reopened))
        self.store.reindex()
        errors = self.store.check()
        self.assertTrue(any("consumed record" in error for error in errors), errors)

    def test_git_lifecycle_rejects_new_record_created_as_consumed(self) -> None:
        self.commit_baseline("empty owner-comment ledger")
        payload = record()
        payload["state"] = "consumed"
        payload["consumption"] = {
            "at": "2026-08-27T13:00:00Z",
            "actor": "actor",
            "evidence": "evidence",
        }
        path = (
            self.root
            / "docs/owner-comments/websites/consumed"
            / f"{payload['id']}.json"
        )
        path.parent.mkdir()
        path.write_bytes(owner_comments._json_bytes(payload))
        self.store.reindex()
        errors = self.store.check()
        self.assertTrue(any("must be added unconsumed" in error for error in errors), errors)


class RouteCase(unittest.TestCase):
    def route_prompt(
        self, prompt: str, session: str, state: str
    ) -> tuple[str, set[str], set[str]]:
        event = {
            "hook_event_name": "UserPromptSubmit",
            "session_id": session,
            "prompt": prompt,
        }
        result = subprocess.run(
            [sys.executable, ".claude/hooks/route_docs.py"],
            cwd=REPO,
            input=json.dumps(event),
            text=True,
            capture_output=True,
            env=dict(os.environ, TMPDIR=state),
            check=True,
        )
        if not result.stdout.strip():
            return "", set(), set()
        context = json.loads(result.stdout)["hookSpecificOutput"][
            "additionalContext"
        ]
        comments = set(
            re.findall(r"docs/owner-comments/([^/]+)/README\.md", context)
        )
        routed_docs = set(re.findall(r"^· `([^`]+)`", context, re.MULTILINE))
        return context, comments, routed_docs

    def test_repository_prompt_routes_stable_comment_index(self) -> None:
        with tempfile.TemporaryDirectory() as state:
            event = {
                "hook_event_name": "UserPromptSubmit",
                "session_id": "owner-comments-route-test",
                "prompt": "Continue work in menno420/websites",
            }
            environment = dict(os.environ, TMPDIR=state)
            result = subprocess.run(
                [sys.executable, ".claude/hooks/route_docs.py"],
                cwd=REPO,
                input=json.dumps(event),
                text=True,
                capture_output=True,
                env=environment,
                check=True,
            )
            payload = json.loads(result.stdout)
            context = payload["hookSpecificOutput"]["additionalContext"]
            self.assertIn("docs/repos/websites/README.md", context)
            self.assertIn("docs/owner-comments/websites/README.md", context)

    def test_direct_layer2_read_routes_comment_index_with_its_own_message(self) -> None:
        with tempfile.TemporaryDirectory() as state:
            event = {
                "hook_event_name": "PreToolUse",
                "session_id": "owner-comments-read-route-test",
                "tool_name": "Read",
                "tool_input": {"file_path": "docs/repos/websites/README.md"},
            }
            result = subprocess.run(
                [sys.executable, ".claude/hooks/route_docs.py"],
                cwd=REPO,
                input=json.dumps(event),
                text=True,
                capture_output=True,
                env=dict(os.environ, TMPDIR=state),
                check=True,
            )
            context = json.loads(result.stdout)["hookSpecificOutput"][
                "additionalContext"
            ]
            self.assertNotIn("· `docs/repos/websites/README.md`", context)
            self.assertIn("· `docs/owner-comments/websites/README.md`", context)
            self.assertIn("open the Unconsumed section", context)
            self.assertNotIn("Layer 2 entry point", context)

    def test_reading_comment_index_does_not_route_it_onto_itself(self) -> None:
        with tempfile.TemporaryDirectory() as state:
            event = {
                "hook_event_name": "PreToolUse",
                "session_id": "owner-comments-self-read-test",
                "tool_name": "Read",
                "tool_input": {
                    "file_path": "docs/owner-comments/websites/README.md"
                },
            }
            result = subprocess.run(
                [sys.executable, ".claude/hooks/route_docs.py"],
                cwd=REPO,
                input=json.dumps(event),
                text=True,
                capture_output=True,
                env=dict(os.environ, TMPDIR=state),
                check=True,
            )
            self.assertFalse(result.stdout.strip())
            state_path = (
                Path(state)
                / "claude-doc-routes"
                / "owner-comments-self-read-test.json"
            )
            self.assertIn(
                "owner-comments-websites",
                json.loads(state_path.read_text(encoding="utf-8")),
            )

    def test_comment_index_backup_name_is_not_mistaken_for_a_self_read(self) -> None:
        with tempfile.TemporaryDirectory() as state:
            event = {
                "hook_event_name": "PreToolUse",
                "session_id": "owner-comments-backup-read-test",
                "tool_name": "Read",
                "tool_input": {
                    "file_path": "docs\\owner-comments\\websites\\README.md.bak"
                },
            }
            result = subprocess.run(
                [sys.executable, ".claude/hooks/route_docs.py"],
                cwd=REPO,
                input=json.dumps(event),
                text=True,
                capture_output=True,
                env=dict(os.environ, TMPDIR=state),
                check=True,
            )

            context = json.loads(result.stdout)["hookSpecificOutput"][
                "additionalContext"
            ]
            self.assertIn("· `docs/owner-comments/websites/README.md`", context)
            self.assertIn("open the Unconsumed section", context)

    def test_absolute_paths_do_not_treat_checkout_ancestor_as_fleet_target(self) -> None:
        cases = [
            (
                REPO / "docs/owner-comments/websites/README.md",
                set(),
            ),
            (
                REPO / "docs/repos/websites/README.md",
                {"websites"},
            ),
        ]
        with tempfile.TemporaryDirectory() as state:
            for number, (path, expected) in enumerate(cases):
                event = {
                    "hook_event_name": "PreToolUse",
                    "session_id": f"owner-comments-absolute-{number}",
                    "tool_name": "Read",
                    "tool_input": {"file_path": str(path)},
                }
                result = subprocess.run(
                    [sys.executable, ".claude/hooks/route_docs.py"],
                    cwd=REPO,
                    input=json.dumps(event),
                    text=True,
                    capture_output=True,
                    env=dict(os.environ, TMPDIR=state),
                    check=True,
                )
                routed = set(
                    re.findall(
                        r"docs/owner-comments/([^/]+)/README\.md",
                        result.stdout,
                    )
                )
                self.assertEqual(routed, expected, str(path))

    def test_absolute_checkout_selection_is_prompt_content_not_read_plumbing(self) -> None:
        with tempfile.TemporaryDirectory() as state:
            _context, comments, _docs = self.route_prompt(
                f"Start in {REPO}",
                "owner-comments-absolute-prompt",
                state,
            )
            self.assertEqual(comments, {"fleet-manager"})

            _context, comments, _docs = self.route_prompt(
                f"Start in {REPO}-old",
                "owner-comments-absolute-prefix-prompt",
                state,
            )
            self.assertEqual(comments, set())

            event = {
                "hook_event_name": "PreToolUse",
                "session_id": "owner-comments-absolute-read",
                "tool_name": "Read",
                "tool_input": {"file_path": str(REPO / "README.md")},
            }
            result = subprocess.run(
                [sys.executable, ".claude/hooks/route_docs.py"],
                cwd=REPO,
                input=json.dumps(event),
                text=True,
                capture_output=True,
                env=dict(os.environ, TMPDIR=state),
                check=True,
            )
            routed = set(
                re.findall(
                    r"docs/owner-comments/([^/]+)/README\.md",
                    result.stdout,
                )
            )
            self.assertEqual(routed, set())

    def test_canonical_repo_terminal_punctuation_is_a_boundary(self) -> None:
        cases = (
            ("Review creator-kit.", {"creator-kit"}),
            ("Review creator-kit!", {"creator-kit"}),
            ("Review creator-kit.component", set()),
            ("Review creator-kit-more", set()),
            ("Review xcreator-kit", set()),
        )
        with tempfile.TemporaryDirectory() as state:
            for number, (prompt, expected) in enumerate(cases):
                event = {
                    "hook_event_name": "UserPromptSubmit",
                    "session_id": f"owner-comments-punctuation-{number}",
                    "prompt": prompt,
                }
                result = subprocess.run(
                    [sys.executable, ".claude/hooks/route_docs.py"],
                    cwd=REPO,
                    input=json.dumps(event),
                    text=True,
                    capture_output=True,
                    env=dict(os.environ, TMPDIR=state),
                    check=True,
                )
                routed = set(
                    re.findall(
                        r"docs/owner-comments/([^/]+)/README\.md",
                        result.stdout,
                    )
                )
                self.assertEqual(routed, expected, prompt)

    def test_estate_family_aliases_route_each_member_comment_index(self) -> None:
        cases = [
            ("Menno Creator Kit", ("creator-kit",)),
            ("THE CREATOR KIT", ("creator-kit",)),
            ("the FreeCAD thing", ("creator-kit",)),
            ("mdverify", ("codetool-lab-opus4.8",)),
            ("envdrift", ("codetool-lab-fable5",)),
            ("the shift calendar", ("shiftlife",)),
            ("Lumen Drift", ("gba-homebrew",)),
            ("GBA homebrew", ("gba-homebrew",)),
            ("Pokemon mod lab", ("pokemon-mod-lab",)),
            ("Ideas Lab", ("idea-engine", "sim-lab")),
            ("idea engine", ("idea-engine",)),
            ("sim lab", ("sim-lab",)),
            ("trading strategy", ("trading-strategy",)),
            ("trading-lab", ("trading-strategy",)),
            ("curious research", ("curious-research",)),
            ("the kit dashboard", ("Substrate-kit-app",)),
            ("Substrate Kit app", ("Substrate-kit-app",)),
            ("proxybench", ("proxybench",)),
            ("SuperBot Games", ("superbot-games",)),
            ("SuperBot Idle", ("superbot-idle",)),
            ("the idle engine", ("superbot-idle",)),
            ("SuperBot Plugin Hello", ("superbot-plugin-hello",)),
            ("SuperBot 2.0", ("superbot-next",)),
            ("the rebuild", ("superbot-next",)),
            (
                "SuperBot World",
                ("superbot-games", "superbot-idle", "superbot-mineverse", "superbot-plugin-hello"),
            ),
        ]
        with tempfile.TemporaryDirectory() as state:
            environment = dict(os.environ, TMPDIR=state)
            for number, (prompt, repositories) in enumerate(cases):
                event = {
                    "hook_event_name": "UserPromptSubmit",
                    "session_id": f"owner-comments-family-{number}",
                    "prompt": prompt,
                }
                result = subprocess.run(
                    [sys.executable, ".claude/hooks/route_docs.py"],
                    cwd=REPO,
                    input=json.dumps(event),
                    text=True,
                    capture_output=True,
                    env=environment,
                    check=True,
                )
                context = json.loads(result.stdout)["hookSpecificOutput"][
                    "additionalContext"
                ]
                for repository in repositories:
                    self.assertIn(
                        f"docs/owner-comments/{repository}/README.md",
                        context,
                        prompt,
                    )
                routed = set(
                    re.findall(r"docs/owner-comments/([^/]+)/README\.md", context)
                )
                self.assertEqual(routed, set(repositories), prompt)

    def test_documented_owner_vocabulary_routes_stable_indexes(self) -> None:
        cases = (
            ("the community bot", {"spider-bot"}),
            ("Slingy-Spider-server work", {"spider-bot"}),
            ("the kit", {"substrate-kit"}),
            ("the review site", {"websites"}),
            ("the control plane", {"websites"}),
            ("Venture Lab", {"venture-lab"}),
            ("Lull/DREAMLINE", {"venture-lab"}),
            ("DREAMLINE", {"venture-lab"}),
            ("Ultramarine", {"venture-lab"}),
            ("Wickroad", {"gba-homebrew"}),
            ("Brineward", {"gba-homebrew"}),
            ("Underroot", {"gba-homebrew"}),
            (
                "SuperBot-World fleet MASTER",
                {
                    "superbot-games",
                    "superbot-idle",
                    "superbot-mineverse",
                    "superbot-plugin-hello",
                },
            ),
        )
        with tempfile.TemporaryDirectory() as state:
            for number, (prompt, expected) in enumerate(cases):
                _context, comments, _docs = self.route_prompt(
                    prompt, f"owner-comments-vocabulary-{number}", state
                )
                self.assertEqual(comments, expected, prompt)

    def test_generic_venture_does_not_consume_later_venture_lab_route(self) -> None:
        with tempfile.TemporaryDirectory() as state:
            session = "owner-comments-generic-venture"
            context, comments, docs = self.route_prompt(
                "What kind of venture should I start?", session, state
            )
            self.assertNotIn("repo-venture-lab", context)
            self.assertEqual(comments, set())
            self.assertNotIn("docs/repos/venture-lab/README.md", docs)

            _context, comments, docs = self.route_prompt(
                "Now continue Venture Lab", session, state
            )
            self.assertEqual(comments, {"venture-lab"})
            self.assertIn("docs/repos/venture-lab/README.md", docs)
            self.assertIn(
                "docs/owner-comments/venture-lab/README.md", docs
            )

    def test_embedded_product_aliases_shadow_only_the_implicit_route(self) -> None:
        cases = (
            (
                "Substrate Kit Dashboard",
                {"Substrate-kit-app"},
                {
                    "docs/ESTATE.md",
                    "docs/owner-comments/Substrate-kit-app/README.md",
                },
            ),
            (
                "Slingy Spider community bot",
                {"spider-bot"},
                {
                    "docs/repos/spider-bot/README.md",
                    "docs/owner-comments/spider-bot/README.md",
                },
            ),
            (
                "the community bot for Slingy Spider",
                {"spider-bot"},
                {
                    "docs/repos/spider-bot/README.md",
                    "docs/owner-comments/spider-bot/README.md",
                },
            ),
            (
                "the community bot for the Slingy Spider",
                {"spider-bot"},
                {
                    "docs/repos/spider-bot/README.md",
                    "docs/owner-comments/spider-bot/README.md",
                },
            ),
            (
                "the community bot for the Slingy Spider Discord server",
                {"spider-bot"},
                {
                    "docs/repos/spider-bot/README.md",
                    "docs/owner-comments/spider-bot/README.md",
                },
            ),
            (
                "the community bot of the Slingy Spider Discord server",
                {"spider-bot"},
                {
                    "docs/repos/spider-bot/README.md",
                    "docs/owner-comments/spider-bot/README.md",
                },
            ),
            (
                "the community bot in the Slingy Spider Discord server",
                {"spider-bot"},
                {
                    "docs/repos/spider-bot/README.md",
                    "docs/owner-comments/spider-bot/README.md",
                },
            ),
            (
                "the Slingy Spider Discord server",
                {"spider-bot"},
                {
                    "docs/repos/spider-bot/README.md",
                    "docs/owner-comments/spider-bot/README.md",
                },
            ),
            (
                "Slingy Spider's community bot",
                {"spider-bot"},
                {
                    "docs/repos/spider-bot/README.md",
                    "docs/owner-comments/spider-bot/README.md",
                },
            ),
            (
                "Slingy Spider game",
                {"spider-swing"},
                {
                    "docs/repos/spider-swing/README.md",
                    "docs/owner-comments/spider-swing/README.md",
                },
            ),
            (
                "compare Substrate Kit Dashboard and substrate-kit",
                {"Substrate-kit-app", "substrate-kit"},
                {
                    "docs/ESTATE.md",
                    "docs/repos/substrate-kit/README.md",
                    "docs/owner-comments/Substrate-kit-app/README.md",
                    "docs/owner-comments/substrate-kit/README.md",
                },
            ),
            (
                "compare the community bot and spider-swing",
                {"spider-bot", "spider-swing"},
                {
                    "docs/repos/spider-bot/README.md",
                    "docs/repos/spider-swing/README.md",
                    "docs/owner-comments/spider-bot/README.md",
                    "docs/owner-comments/spider-swing/README.md",
                },
            ),
            (
                "Compare the community bot and Slingy Spider.",
                {"spider-bot", "spider-swing"},
                {
                    "docs/repos/spider-bot/README.md",
                    "docs/repos/spider-swing/README.md",
                    "docs/owner-comments/spider-bot/README.md",
                    "docs/owner-comments/spider-swing/README.md",
                },
            ),
            (
                "Compare Substrate Kit Dashboard and kit release.",
                {"Substrate-kit-app", "substrate-kit"},
                {
                    "docs/ESTATE.md",
                    "docs/repos/substrate-kit/README.md",
                    "docs/owner-comments/Substrate-kit-app/README.md",
                    "docs/owner-comments/substrate-kit/README.md",
                },
            ),
        )
        with tempfile.TemporaryDirectory() as state:
            for number, (prompt, expected_comments, expected_docs) in enumerate(cases):
                _context, comments, docs = self.route_prompt(
                    prompt, f"owner-comments-collision-{number}", state
                )
                self.assertEqual(comments, expected_comments, prompt)
                self.assertEqual(docs, expected_docs, prompt)

    def test_repository_aliases_share_canonical_suffix_boundaries(self) -> None:
        root_index = json.loads(
            (REPO / "docs/owner-comments/index.json").read_text(encoding="utf-8")
        )
        negative = [
            f"{row['repository']}.component"
            for row in root_index["repositories"]
        ] + [
            "codetool-lab-opus4.80",
            "superbot-games-extra",
            "trading-lab.py",
            "websites.gitignore",
            "websites.github",
            "websites.git/continuation",
            "websites.py",
            "websites-extra",
            "websites2",
            "DREAMLINER",
        ]
        positive = (
            ("creator-kit.", {"creator-kit"}),
            ("trading-lab.", {"trading-strategy"}),
            ("codetool-lab-opus4.8.", {"codetool-lab-opus4.8"}),
            (
                "git clone https://github.com/menno420/websites.git",
                {"websites"},
            ),
            ("Use menno420/websites.git.", {"websites"}),
            ("the community bot!", {"spider-bot"}),
            ("Substrate Kit Dashboard?", {"Substrate-kit-app"}),
        )
        with tempfile.TemporaryDirectory() as state:
            for number, prompt in enumerate(negative):
                _context, comments, docs = self.route_prompt(
                    prompt, f"owner-comments-suffix-negative-{number}", state
                )
                self.assertEqual(comments, set(), prompt)
                self.assertEqual(docs, set(), prompt)
            for number, (prompt, expected) in enumerate(positive):
                _context, comments, _docs = self.route_prompt(
                    prompt, f"owner-comments-suffix-positive-{number}", state
                )
                self.assertEqual(comments, expected, prompt)

    def test_creator_kit_alias_boundaries_do_not_overroute(self) -> None:
        with tempfile.TemporaryDirectory() as state:
            for number, prompt in enumerate(
                ("the creator kitten", "the FreeCAD thingy", "FreeCAD")
            ):
                event = {
                    "hook_event_name": "UserPromptSubmit",
                    "session_id": f"owner-comments-creator-boundary-{number}",
                    "prompt": prompt,
                }
                result = subprocess.run(
                    [sys.executable, ".claude/hooks/route_docs.py"],
                    cwd=REPO,
                    input=json.dumps(event),
                    text=True,
                    capture_output=True,
                    env=dict(os.environ, TMPDIR=state),
                    check=True,
                )
                self.assertNotIn(
                    "docs/owner-comments/creator-kit/README.md",
                    result.stdout,
                    prompt,
                )

    def test_envdrift_python_module_does_not_route_fable5_feedback(self) -> None:
        with tempfile.TemporaryDirectory() as state:
            event = {
                "hook_event_name": "PreToolUse",
                "session_id": "owner-comments-envdrift-module",
                "tool_name": "Read",
                "tool_input": {"file_path": "app/envdrift.py"},
            }
            result = subprocess.run(
                [sys.executable, ".claude/hooks/route_docs.py"],
                cwd=REPO,
                input=json.dumps(event),
                text=True,
                capture_output=True,
                env=dict(os.environ, TMPDIR=state),
                check=True,
            )
            self.assertNotIn(
                "docs/owner-comments/codetool-lab-fable5/README.md",
                result.stdout,
            )

    def test_every_canonical_repo_slug_routes_its_comment_index(self) -> None:
        root_index = json.loads(
            (REPO / "docs/owner-comments/index.json").read_text(encoding="utf-8")
        )
        with tempfile.TemporaryDirectory() as state:
            environment = dict(os.environ, TMPDIR=state)
            for number, row in enumerate(root_index["repositories"]):
                repository = row["repository"]
                event = {
                    "hook_event_name": "UserPromptSubmit",
                    "session_id": f"owner-comments-all-{number}",
                    "prompt": f"Continue menno420/{repository}",
                }
                result = subprocess.run(
                    [sys.executable, ".claude/hooks/route_docs.py"],
                    cwd=REPO,
                    input=json.dumps(event),
                    text=True,
                    capture_output=True,
                    env=environment,
                    check=True,
                )
                context = json.loads(result.stdout)["hookSpecificOutput"][
                    "additionalContext"
                ]
                routed = set(
                    re.findall(r"docs/owner-comments/([^/]+)/README\.md", context)
                )
                self.assertEqual(routed, {repository}, repository)

    def test_owner_comment_tree_is_forced_to_lf_on_every_git_lane(self) -> None:
        result = subprocess.run(
            [
                "git",
                "check-attr",
                "text",
                "eol",
                "--",
                "docs/owner-comments/record.schema.json",
                "docs/owner-comments/index.json",
                "docs/owner-comments/websites/example.json",
            ],
            cwd=REPO,
            text=True,
            capture_output=True,
            check=True,
        )
        for path in (
            "docs/owner-comments/record.schema.json",
            "docs/owner-comments/index.json",
            "docs/owner-comments/websites/example.json",
        ):
            self.assertIn(f"{path}: text: set", result.stdout)
            self.assertIn(f"{path}: eol: lf", result.stdout)

    def test_codex_prompt_adapter_preserves_owner_comment_route(self) -> None:
        with tempfile.TemporaryDirectory() as state:
            event = {
                "hook_event_name": "UserPromptSubmit",
                "session_id": "owner-comments-codex-route-test",
                "prompt": "Continue menno420/websites",
            }
            result = subprocess.run(
                [sys.executable, ".codex/hooks/route_docs.py"],
                cwd=REPO,
                input=json.dumps(event),
                text=True,
                capture_output=True,
                env=dict(os.environ, TMPDIR=state, TEMP=state, TMP=state),
                check=True,
            )
            payload = json.loads(result.stdout)
            context = payload["hookSpecificOutput"]["additionalContext"]
            self.assertIn("docs/owner-comments/websites/README.md", context)
            self.assertNotIn("suppressOutput", payload)


if __name__ == "__main__":
    unittest.main(verbosity=2)
