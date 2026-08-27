#!/usr/bin/env python3
"""Contract/regression tests for tools/owner_comments.py and its route."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from owner_comments import ContractError, OwnerCommentsStore


REPO = Path(__file__).resolve().parents[1]


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
        (self.root / "docs/ESTATE.md").write_text(
            "# estate\n\n"
            "| repo | state |\n|---|---|\n"
            "| `fleet-manager` | active |\n"
            "| `websites` | active |\n"
            "| `Substrate-kit-app` | archived |\n",
            encoding="utf-8",
        )
        self.store = OwnerCommentsStore(self.root)
        self.store.reindex()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_record(self, data: dict | None = None) -> Path:
        payload = data or record()
        path = self.root / "docs/owner-comments/websites" / f"{payload['id']}.json"
        path.write_text(
            json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        return path

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
        (unknown / "README.md").write_text("unexpected\n", encoding="utf-8")
        errors = self.store.check()
        self.assertTrue(any("non-whitespace" in error for error in errors), errors)
        self.assertTrue(any("not a canonical" in error for error in errors), errors)

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
        path.write_text("{}\n", encoding="utf-8")
        self.assertTrue(any("stale" in error for error in self.store.check()))


class RouteCase(unittest.TestCase):
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

    def test_layer2_probe_still_routes_unopened_comment_companion(self) -> None:
        with tempfile.TemporaryDirectory() as state:
            event = {
                "hook_event_name": "PreToolUse",
                "session_id": "owner-comments-read-route-test",
                "tool_name": "Grep",
                "tool_input": {
                    "pattern": "control-plane",
                    "path": "docs/repos/websites/README.md",
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
            self.assertNotIn("· `docs/repos/websites/README.md`", context)
            self.assertIn("· `docs/owner-comments/websites/README.md`", context)


if __name__ == "__main__":
    unittest.main(verbosity=2)
