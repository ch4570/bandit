"""Synthetic current tests. These files are inputs, not a request to run tests."""
import unittest

from implementation import ExportService, Session


class Queue:
    def __init__(self):
        self.messages = []

    def push(self, export_id):
        self.messages.append(export_id)


class ExistingExportTests(unittest.TestCase):
    def test_same_member_retry_returns_one_export(self):
        queue = Queue()
        service = ExportService(queue)
        session = Session("workspace-a")
        first = service.request_export(session, "key-1", {"month": "2026-08"})
        again = service.request_export(session, "key-1", {"month": "2026-08"})
        self.assertEqual(first["id"], again["id"])
        self.assertEqual(len(queue.messages), 1)

    def test_completed_export_can_be_read_by_its_member(self):
        service = ExportService(Queue())
        session = Session("workspace-a")
        export = service.request_export(session, "key-2", {})
        service.run_export(export["id"], lambda workspace, filters: "synthetic-object/zip-1")
        self.assertEqual(service.get_export(session, export["id"])["state"], "complete")

    def test_inactive_members_cannot_request_exports(self):
        service = ExportService(Queue())
        with self.assertRaises(PermissionError):
            service.request_export(Session("workspace-a", active=False), "key-3", {})
