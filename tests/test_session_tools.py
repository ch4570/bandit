"""Structural capture tests use synthetic session rows, never host history."""
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from evals import session_tools


THREAD = "01a089b5-ad9f-7803-8a4c-bdccf12cb79c"
OTHER = "11a089b5-ad9f-7803-8a4c-bdccf12cb79c"
requires_session_traversal = unittest.skipUnless(
    hasattr(os, "O_NOFOLLOW") and hasattr(os, "O_DIRECTORY")
    and os.open in os.supports_dir_fd and os.scandir in os.supports_fd,
    "Safe descriptor-relative session traversal is unavailable on this host")


def row(kind, **payload):
    return {"type": kind, "payload": payload}


def encode(records):
    return b"".join(json.dumps(record, ensure_ascii=False).encode() + b"\n" for record in records)


class SessionToolTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="bandit synthetic sessions ")
        self.addCleanup(temporary.cleanup)
        self.area = Path(temporary.name).resolve()
        self.home = self.area / "codex-home"
        self.directory = self.home / "sessions/2026/09/10"
        self.directory.mkdir(parents=True)
        self.workspace = self.area / "workspace"
        self.workspace.mkdir()
        self.source = self.directory / f"rollout-2026-09-10T14-06-20-{THREAD}.jsonl"
        self.events = self.area / "events.jsonl"
        self.events.write_bytes(encode([{"type": "thread.started", "thread_id": THREAD}]))
        self.export = self.area / "session-tools.jsonl"
        now = datetime.now(timezone.utc)
        self.started_at = (now - timedelta(seconds=1)).isoformat()
        self.records = [
            row("session_meta", id=THREAD, cwd=str(self.workspace), source="exec", timestamp=now.isoformat(),
                base_instructions="SECRET_SYSTEM_INSTRUCTIONS"),
            row("event_msg", type="task_started", turn_id="synthetic-turn"),
            *[row("response_item", type="message", role=role, content=f"SECRET_{role.upper()}_MESSAGE")
              for role in ("system", "developer", "user", "assistant")],
            row("response_item", type="reasoning", summary="SECRET_REASONING"),
            row("response_item", type="custom_tool_call", call_id="call-1", name="exec", input="text(2 + 3);", status="completed"),
            row("response_item", type="custom_tool_call_output", call_id="call-1", output=[{"type": "input_text", "text": "5"}]),
            row("response_item", type="function_call", call_id="call-2", name="exec_command", arguments='{"cmd":"pwd"}'),
            row("response_item", type="function_call_output", call_id="call-2", output="synthetic result"),
            row("event_msg", type="task_complete", turn_id="synthetic-turn", last_agent_message="SECRET_FINAL_MESSAGE"),
        ]
        environment = patch.dict(os.environ, {"CODEX_HOME": str(self.home)})
        environment.start()
        self.addCleanup(environment.stop)

    def capture(self, records=None, *, raw=None):
        self.source.write_bytes(raw if raw is not None else encode(self.records if records is None else records))
        return session_tools.capture_session_tools(self.events, self.workspace, self.export, started_at=self.started_at)

    @requires_session_traversal
    def test_export_preserves_only_exact_tool_rows_and_provenance(self):
        # Deliberate whitespace and CRLF prove that selected rows are not reserialized.
        raw = encode(self.records).replace(b'"input": "text(2 + 3);"', b'"input" : "text(2 + 3);"').replace(b"\n", b"\r\n")
        metadata = self.capture(raw=raw)
        self.assertEqual(metadata["status"], "captured")
        self.assertEqual(metadata["exported_source_lines"], [8, 9, 10, 11])
        self.assertEqual(self.export.read_bytes(), b"".join(raw.splitlines(keepends=True)[7:11]))
        self.assertEqual(metadata["source_sha256"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(metadata["source_line_count"], 12)
        self.assertEqual((metadata["record_count"], metadata["call_count"], metadata["result_count"]), (4, 2, 2))
        self.assertNotIn("SECRET", self.export.read_text())
        self.assertNotIn(str(self.area), json.dumps(metadata))
        self.assertTrue(self.source.exists())
        self.assertNotIn("quality_status", metadata)

    @requires_session_traversal
    def test_default_home_is_used_only_when_codex_home_is_unset(self):
        actual_home = self.area / "fake-user"
        (actual_home / ".codex").parent.mkdir()
        self.home.rename(actual_home / ".codex")
        self.source = actual_home / ".codex/sessions/2026/09/10" / self.source.name
        with patch.dict(os.environ, {}, clear=True), patch.object(Path, "home", return_value=actual_home):
            self.assertEqual(self.capture()["status"], "captured")

    def test_stdout_requires_one_canonical_uuid_before_opening_session_source(self):
        invalid = [[], [{"type": "thread.started", "thread_id": "../../private"}],
                   [{"type": "thread.started", "thread_id": None}],
                   [{"type": "thread.started", "thread_id": THREAD.upper()}],
                   [{"type": "thread.started", "thread_id": THREAD}] * 2]
        for records in invalid:
            with self.subTest(records=records):
                self.events.write_bytes(encode(records))
                with patch.object(session_tools, "_source") as source:
                    metadata = session_tools.capture_session_tools(self.events, self.workspace, self.export, started_at=self.started_at)
                source.assert_not_called()
                self.assertEqual(metadata["status"], "unavailable")
                self.assertTrue(metadata["errors"])
                self.export.unlink()

    def test_malformed_and_truncated_stdout_are_rejected(self):
        for raw in (b"not json\n", b'{"type":"thread.started","thread_id":"' + THREAD.encode() + b'"}',
                    b'{"type":"thread.started","thread_id":"' + THREAD.encode() + b'","thread_id":"' + OTHER.encode() + b'"}\n'):
            with self.subTest(raw=raw), patch.object(session_tools, "_source") as source:
                self.events.write_bytes(raw)
                metadata = session_tools.capture_session_tools(self.events, self.workspace, self.export, started_at=self.started_at)
                source.assert_not_called()
                self.assertEqual(metadata["status"], "unavailable")
                self.export.unlink()

    def test_unsupported_traversal_preserves_failure_evidence_without_opening_host_sources(self):
        self.source.write_bytes(encode(self.records))
        original_events = self.events.read_bytes()
        with patch.object(session_tools.os, "supports_dir_fd", set()), \
                patch.object(session_tools.os, "open") as host_open, \
                patch.object(session_tools.os, "scandir") as host_scan:
            metadata = session_tools.capture_session_tools(self.events, self.workspace, self.export, started_at=self.started_at)
        host_open.assert_not_called()
        host_scan.assert_not_called()
        self.assertEqual(metadata["status"], "unavailable")
        self.assertIn("Safe session traversal is unavailable", metadata["errors"][0])
        self.assertEqual(metadata["thread_id"], THREAD)
        self.assertIsNone(metadata["source_sha256"])
        self.assertEqual(metadata["record_count"], 0)
        self.assertEqual(self.export.read_bytes(), b"")
        self.assertEqual(self.events.read_bytes(), original_events)
        self.assertEqual(self.source.read_bytes(), encode(self.records))

    @requires_session_traversal
    def test_source_id_cwd_origin_and_freshness_must_bind_before_remaining_content_is_read(self):
        mismatches = ({"id": OTHER}, {"cwd": str(self.area / "other-workspace")}, {"source": "vscode"},
                      {"timestamp": "2000-01-01T00:00:00Z"}, {"timestamp": "bad-date"},
                      {"timestamp": "2999-01-01T00:00:00Z"}, {"timestamp": "2026-09-10T12:00:00"})
        for fields in mismatches:
            with self.subTest(fields=fields):
                header = {**self.records[0], "payload": {**self.records[0]["payload"], **fields}}
                self.source.write_bytes(encode([header]) + b"DO_NOT_READ_PRIVATE_BODY\n")
                real_fdopen = session_tools.os.fdopen

                class HeaderOnly:
                    def __enter__(inner):
                        return inner
                    def __exit__(inner, *_):
                        inner.stream.close()
                    def readline(inner):
                        value = inner.stream.readline()
                        self.assertEqual(os.lseek(inner.stream.fileno(), 0, os.SEEK_CUR), len(value),
                                         "Buffered header read prefetched an unbound session body")
                        return value
                    def read(inner):
                        self.fail("Read body before source metadata binding")

                def guarded_stream(*args, **kwargs):
                    result = HeaderOnly()
                    result.stream = real_fdopen(*args, **kwargs)
                    return result

                with patch.object(session_tools.os, "fdopen", side_effect=guarded_stream):
                    metadata = session_tools.capture_session_tools(self.events, self.workspace, self.export, started_at=self.started_at)
                self.assertEqual(metadata["status"], "unavailable")
                self.assertEqual(self.export.read_bytes(), b"")
                self.export.unlink()

    @requires_session_traversal
    def test_missing_ambiguous_and_unsafe_sources_fail_without_opening_session_content(self):
        for kind in ("missing", "ambiguous", "symlink", "directory", "hardlink", "fifo"):
            with self.subTest(kind=kind):
                paths = []
                if kind == "ambiguous":
                    self.source.write_bytes(encode(self.records))
                    duplicate = self.directory / f"rollout-other-{THREAD}.jsonl"
                    duplicate.write_bytes(encode(self.records))
                    paths += [self.source, duplicate]
                elif kind in ("symlink", "hardlink"):
                    external = self.area / "private-session.jsonl"
                    external.write_text("PRIVATE CONTENT")
                    if kind == "symlink":
                        self.source.symlink_to(external)
                    else:
                        os.link(external, self.source)
                    paths += [self.source, external]
                elif kind == "directory":
                    self.source.mkdir()
                elif kind == "fifo":
                    os.mkfifo(self.source)
                    paths += [self.source]
                with patch.object(session_tools.os, "fdopen") as read:
                    metadata = session_tools.capture_session_tools(self.events, self.workspace, self.export, started_at=self.started_at)
                read.assert_not_called()
                self.assertEqual(metadata["status"], "unavailable")
                self.assertTrue(metadata["errors"])
                self.export.unlink()
                for path in paths:
                    path.unlink()
                if kind == "directory":
                    self.source.rmdir()

    @requires_session_traversal
    def test_symlinked_session_directory_is_never_followed(self):
        moved = self.area / "private-tree"
        self.directory.rename(moved)
        self.directory.symlink_to(moved, target_is_directory=True)
        metadata = self.capture()
        self.assertEqual(metadata["status"], "unavailable")
        self.assertEqual(self.export.read_bytes(), b"")

    @requires_session_traversal
    def test_unrelated_sessions_are_not_opened(self):
        unrelated = self.directory / f"rollout-2026-09-10T14-06-20-{OTHER}.jsonl"
        unrelated.write_text("PRIVATE SESSION MUST NOT BE READ")
        confusing = self.directory / f"rollout-extra-{THREAD}.jsonl.backup"
        confusing.write_text("PRIVATE BACKUP MUST NOT BE READ")
        real_open = session_tools.os.open

        def guarded_open(path, *args, **kwargs):
            self.assertNotIn(Path(path).name, (unrelated.name, confusing.name))
            return real_open(path, *args, **kwargs)

        with patch.object(session_tools.os, "open", side_effect=guarded_open) as opened, \
                patch.object(session_tools.os, "supports_dir_fd", {opened}):
            metadata = self.capture()
        self.assertEqual(metadata["status"], "captured")

    @requires_session_traversal
    def test_malformed_truncated_and_nonterminal_sessions_retain_partial_tool_evidence(self):
        variants = [encode(self.records[:-1]), encode(self.records)[:-1],
                    encode(self.records[:-1]) + b"not json\n", encode(self.records) + b"not json\n",
                    encode(self.records + [self.records[-1]]), encode([self.records[0], *self.records]),
                    encode([*self.records[:-1], row("event_msg", type="task_complete", turn_id="wrong-turn")])]
        for raw in variants:
            with self.subTest(raw=raw):
                metadata = self.capture(raw=raw)
                self.assertEqual(metadata["status"], "incomplete")
                self.assertTrue(metadata["errors"])
                self.assertEqual(metadata["source_sha256"], hashlib.sha256(raw).hexdigest())
                self.assertNotIn("SECRET", self.export.read_text())
                self.export.unlink()

    @requires_session_traversal
    def test_inconsistent_call_result_sequences_are_not_accepted(self):
        prefix, call, result, terminal = self.records[:7], self.records[7], self.records[8], self.records[-1]
        variants = [[call], [result], [call, call, result], [call, result, result],
                    [result, call], [call, {**result, "payload": {**result["payload"], "call_id": "unknown"}}],
                    [call, {**result, "payload": {**result["payload"], "type": "function_call_output"}}]]
        for tools in variants:
            with self.subTest(tools=tools):
                metadata = self.capture([*prefix, *tools, terminal])
                self.assertEqual(metadata["status"], "incomplete")
                self.assertTrue(metadata["errors"])
                self.assertGreater(metadata["record_count"], 0)
                self.export.unlink()

    @requires_session_traversal
    def test_completed_self_contained_web_search_is_preserved(self):
        web = row("response_item", type="web_search_call", id="web-1", status="completed", action={"type": "search", "query": "synthetic"})
        metadata = self.capture([*self.records[:-1], web, self.records[-1]])
        self.assertEqual(metadata["status"], "captured")
        self.assertEqual(metadata["self_contained_count"], 1)
        self.assertIn(encode([web]), self.export.read_bytes())

    @requires_session_traversal
    def test_unknown_tool_record_fails_coverage_instead_of_being_silently_ignored(self):
        unknown = row("response_item", type="future_tool_call", call_id="future-1", name="new-tool")
        metadata = self.capture([*self.records[:-1], unknown, self.records[-1]])
        self.assertEqual(metadata["status"], "unavailable")
        self.assertIn("Unsupported tool", metadata["errors"][0])

    @requires_session_traversal
    def test_complete_session_without_tools_has_no_quality_verdict(self):
        metadata = self.capture([*self.records[:7], self.records[-1]])
        self.assertEqual(metadata["status"], "captured")
        self.assertEqual(metadata["record_count"], 0)
        self.assertEqual(self.export.read_bytes(), b"")
        self.assertNotIn("quality_status", metadata)
