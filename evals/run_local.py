#!/usr/bin/env python3
"""Run one isolated, opt-in Codex CLI development case. Uses your host account."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM_COMMIT = "18468a95b427e70e258b51389796367c6f684e7d"
SPECIALISTS = ("bandit-research", "bandit-scope", "bandit-specify", "bandit-review")
ROUTES = {
    "01-multiple-decisions": ["pm-execution/commands/write-prd.md", "pm-execution/skills/create-prd/SKILL.md"],
    "02-offer-change": ["pm-execution/commands/write-prd.md", "pm-execution/skills/create-prd/SKILL.md", "pm-data-analytics/skills/ab-test-analysis/SKILL.md"],
    "03-intent-review": ["pm-ai-shipping/skills/intended-vs-implemented/SKILL.md", "pm-ai-shipping/commands/derive-tests.md", "pm-ai-shipping/skills/shipping-artifacts/SKILL.md"],
    "04-incomparable-scores": ["pm-product-discovery/skills/prioritize-features/SKILL.md", "pm-execution/skills/prioritization-frameworks/SKILL.md"],
    "05-small-research": ["pm-product-discovery/skills/brainstorm-experiments-new/SKILL.md", "pm-product-discovery/skills/identify-assumptions-new/SKILL.md"],
    "06-existing-spec-rewrite": ["pm-execution/commands/write-prd.md", "pm-execution/skills/create-prd/SKILL.md"],
}


def file_hashes(inventory: dict, prefix: str) -> dict[str, str]:
    """Derive legacy hash views from the same captured state, without rereading links."""
    return {name[len(prefix) + 1:]: entry["sha256"] for name, entry in inventory["entries"].items()
            if name.startswith(prefix + "/") and entry["kind"] == "file"}


def workspace_snapshot(directory: Path) -> dict:
    """Capture a quiescent tree; use descriptor-relative traversal where supported."""
    entries, errors = {}, []
    descriptor_paths = os.open in os.supports_dir_fd and os.scandir in os.supports_fd

    def identity(info):
        return info.st_dev, info.st_ino, info.st_mode, info.st_size, info.st_mtime_ns

    def visit(path, relative: str = "", parent_fd=None) -> None:
        try:
            info = os.stat(path, dir_fd=parent_fd, follow_symlinks=False)
            mode = stat.S_IMODE(info.st_mode)
            if (stat.S_ISLNK(info.st_mode)
                    or getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)):
                entries[relative or "."] = {"kind": "symlink", "mode": mode, "target": os.readlink(path, dir_fd=parent_fd)}
            elif stat.S_ISREG(info.st_mode) or stat.S_ISDIR(info.st_mode) and descriptor_paths:
                flags = (os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
                         | getattr(os, "O_BINARY", 0))
                if stat.S_ISDIR(info.st_mode):
                    flags |= getattr(os, "O_DIRECTORY", 0)
                fd = os.open(path, flags, dir_fd=parent_fd)
                try:
                    if identity(os.fstat(fd)) != identity(info):
                        raise OSError("Path changed while opening snapshot entry")
                    if stat.S_ISDIR(info.st_mode):
                        entries[relative or "."] = {"kind": "directory", "mode": mode}
                        with os.scandir(fd) as children:
                            names = sorted(child.name for child in children)
                        for name in names:
                            visit(name, f"{relative}/{name}" if relative else name, fd)
                    else:
                        with os.fdopen(fd, "rb", closefd=False) as stream:
                            digest = hashlib.file_digest(stream, "sha256").hexdigest()
                        entries[relative or "."] = {"kind": "file", "mode": mode, "sha256": digest}
                    if identity(os.fstat(fd)) != identity(info):
                        raise OSError("Entry changed while taking snapshot")
                finally:
                    os.close(fd)
            elif stat.S_ISDIR(info.st_mode):
                # Hosts without directory descriptors require a quiescent workspace.
                entries[relative or "."] = {"kind": "directory", "mode": mode}
                for child in sorted(Path(path).iterdir()):
                    if identity(os.stat(path, follow_symlinks=False)) != identity(info):
                        raise OSError("Directory changed while taking snapshot")
                    visit(child, f"{relative}/{child.name}" if relative else child.name)
                if identity(os.stat(path, follow_symlinks=False)) != identity(info):
                    raise OSError("Directory changed while taking snapshot")
            else:
                entries[relative or "."] = {"kind": "special", "mode": mode}
        except OSError as exc:
            errors.append({"path": relative or ".", "error": str(exc)})

    visit(directory)
    if "." in entries and entries["."]["kind"] != "directory":
        errors.append({"path": ".", "error": "Workspace root is no longer a directory"})
    return {"entries": entries, "errors": errors,
            "traversal": "descriptor-relative" if descriptor_paths else "portable-quiescent"}


def integrity_result(before: dict, after: dict, edit_artifact: str | None) -> dict:
    violations = []
    for name in sorted(before["entries"].keys() | after["entries"].keys()):
        old, new = before["entries"].get(name), after["entries"].get(name)
        if old == new:
            continue
        change = ("created" if old is None else "deleted" if new is None
                  else "type_changed" if old["kind"] != new["kind"] else "modified")
        if (name == edit_artifact and change == "modified" and new["kind"] == "file"
                and old.get("mode") == new.get("mode")):
            continue
        violations.append({"path": name, "change": change})
    errors = {"before": before["errors"], "after": after["errors"]}
    status = "unavailable" if any(errors.values()) else "failed" if violations else "passed"
    return {"integrity_status": status, "violations": violations, "snapshot_errors": errors}


def run_case(case: str, arm: str, output: Path, upstream: Path | None, edit_artifact: str | None = None) -> int:
    fixture = ROOT / "evals" / "cases" / case
    run = output.resolve() / f"{case}--{arm}"
    if run.exists():
        raise ValueError(f"Run already exists; use a new output directory: {run}")
    if arm == "upstream":
        if upstream is None:
            raise ValueError("--upstream is required for the upstream arm")
        commit = subprocess.check_output(["git", "-C", str(upstream), "rev-parse", "HEAD"], text=True).strip()
        if commit != UPSTREAM_COMMIT:
            raise ValueError(f"Expected upstream commit {UPSTREAM_COMMIT}, got {commit}")
        if subprocess.check_output(["git", "-C", str(upstream), "status", "--porcelain"], text=True).strip():
            raise ValueError("Upstream checkout must be clean")
    workspace = run / "workspace"
    workspace.mkdir(parents=True)
    shutil.copytree(fixture, workspace / "input")
    shutil.copytree(fixture, run / "original-input")
    if edit_artifact:
        target = (workspace / edit_artifact).resolve()
        if not target.is_relative_to(workspace / "input") or not target.is_file():
            raise ValueError("--edit-artifact must name an existing file under input/ in the temporary workspace")
        edit_artifact = target.relative_to(workspace).as_posix()
    if arm in SPECIALISTS:
        shutil.copytree(ROOT / "skills", workspace / ".agents" / "skills")
        instruction = f"Use ${arm} for this task. The BANDIT skills are installed in this project."
    elif arm == "bandit":
        shutil.copytree(ROOT / "skills" / "bandit", workspace / "instructions" / "bandit")
        instruction = "Use instructions/bandit/SKILL.md and the relevant references it routes to."
    elif arm == "upstream":
        # Preserve all dependencies. Routes identify the relevant entrypoints;
        # the agent may follow further skill references within this snapshot.
        shutil.copytree(upstream, workspace / "instructions" / "upstream",
                        ignore=shutil.ignore_patterns(".git", "__pycache__"))
        routes = ["instructions/upstream/" + p for p in ROUTES[case]]
        missing = [p for p in routes if not (workspace / p).is_file()]
        if missing:
            raise ValueError(f"Missing upstream routes: {missing}")
        instruction = ("Apply these upstream skill/workflow instructions: " + ", ".join(routes)
                       + ". This host does not run slash commands; read the command procedure and "
                       "apply it as instructions. The concrete user's task takes precedence over "
                       "generic output format or scope. Follow referenced skills if relevant.")
    else:
        instruction = "Complete the task using your normal product-planning reasoning; do not load a PM skill."
    instruction_scope = ".agents/skills" if arm in SPECIALISTS else "instructions"
    output_instruction = (
        f"You may edit only {edit_artifact} as the task requests. Leave every other file unchanged. "
        "Summarize the result in your final answer. "
        if edit_artifact else
        "Do not change files. Put the requested artifact in your final answer; the runner will save it. "
    )
    prompt = (
        "Perform the user's product-planning task in input/request.md. Read the other files in input/ "
        "as its raw supporting artifacts. " + instruction + "\n"
        f"Use only these task inputs and, if provided, the {instruction_scope}/ snapshot in this workspace. "
        "Do not inspect other repositories, AGENTS files, evaluation rubrics, examples, other outputs, "
        "or prior sessions. Do not browse or contact anyone. Do not execute the supplied product code "
        "or tests. " + output_instruction + "This is the user's task, not a review of the instructions.\n"
    )
    (run / "prompt.txt").write_text(prompt, encoding="utf-8")
    command = ["codex", "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check",
               "--sandbox", "workspace-write" if edit_artifact else "read-only", "--color", "never", "--json", "-C", str(workspace),
               "-o", str(run / "output.md"), "-"]
    before = workspace_snapshot(workspace)
    metadata = {"case": case, "arm": arm,
                "codex_version": None, "process_exit_code": None, "quality_status": "not_evaluated",
                "command": command, "model_override": None, "config": "--ignore-user-config; host defaults",
                "upstream_commit": UPSTREAM_COMMIT if arm == "upstream" else None,
                "input_sha256": file_hashes(before, "input"),
                "instruction_sha256": file_hashes(before, instruction_scope) if arm != "baseline" else {},
                "invocation": f"${arm}" if arm in SPECIALISTS else None,
                "editable_artifact": edit_artifact, "workspace_before": before}
    start = time.monotonic()
    exit_code = 2
    try:
        with (run / "events.jsonl").open("w", encoding="utf-8") as events, (run / "stderr.txt").open("w", encoding="utf-8") as errors:
            if before["errors"]:
                metadata["execution_error"] = "Initial workspace snapshot is unavailable; model was not started"
            else:
                metadata["codex_version"] = subprocess.check_output(["codex", "--version"], text=True).strip()
                result = subprocess.run(command, input=prompt, text=True, stdout=events, stderr=errors)
                metadata["process_exit_code"] = result.returncode
                exit_code = result.returncode
    except KeyboardInterrupt:
        exit_code = 130
        metadata["execution_error"] = "Interrupted"
    except (OSError, subprocess.SubprocessError) as exc:
        metadata["execution_error"] = f"{type(exc).__name__}: {exc}"
    finally:
        after = workspace_snapshot(workspace)
        metadata.update(integrity_result(before, after, edit_artifact))
        if metadata["integrity_status"] != "passed" and exit_code == 0:
            exit_code = 2
        metadata.update(exit_code=exit_code, elapsed_seconds=round(time.monotonic() - start, 3),
                        workspace_after=after,
                        input_after_sha256=file_hashes(after, "input"),
                        instruction_after_sha256=file_hashes(after, instruction_scope) if arm != "baseline" else {})
        (run / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"run": str(run), "exit_code": exit_code,
                      "integrity_status": metadata["integrity_status"]}), flush=True)
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", choices=ROUTES, required=True)
    parser.add_argument("--arm", choices=["baseline", "upstream", "bandit", *SPECIALISTS], required=True)
    parser.add_argument("--upstream", type=Path)
    parser.add_argument("--edit-artifact", help="Permit edits to this one existing input/ file in the isolated workspace")
    parser.add_argument("--output-dir", type=Path, required=True,
                        help="New run artifacts are written here; your Codex account's usage applies")
    args = parser.parse_args()
    try:
        return run_case(args.case, args.arm, args.output_dir, args.upstream, args.edit_artifact)
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(2, f"bandit eval: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
