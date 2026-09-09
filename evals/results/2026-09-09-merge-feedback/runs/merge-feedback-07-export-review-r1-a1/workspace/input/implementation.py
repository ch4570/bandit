"""Synthetic ParcelDesk service snapshot; all data and components are invented."""
from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Session:
    workspace_id: str
    active: bool = True


class ExportService:
    def __init__(self, queue):
        self.queue = queue
        self.jobs = {}
        self.request_keys = {}

    def _require_member(self, session):
        if not session.active:
            raise PermissionError("Active membership required")

    def _view(self, job):
        return {
            "id": job["id"],
            "workspace_id": job["workspace_id"],
            "filters": dict(job["filters"]),
            "state": job["state"],
            "download_location": job["download_location"],
        }

    def request_export(self, session, request_key, filters):
        self._require_member(session)
        if request_key in self.request_keys:
            return self._view(self.jobs[self.request_keys[request_key]])
        job = {
            "id": str(uuid4()),
            "workspace_id": session.workspace_id,
            "filters": dict(filters),
            "state": "pending",
            "download_location": None,
        }
        self.jobs[job["id"]] = job
        self.request_keys[request_key] = job["id"]
        self.queue.push(job["id"])
        return self._view(job)

    def get_export(self, session, export_id):
        self._require_member(session)
        return self._view(self.jobs[export_id])

    def run_export(self, export_id, renderer):
        job = self.jobs[export_id]
        if job["state"] == "complete":
            return
        job["state"] = "running"
        try:
            location = renderer(job["workspace_id"], job["filters"])
        except TimeoutError:
            job["state"] = "failed"
            raise
        job["download_location"] = location
        job["state"] = "complete"
