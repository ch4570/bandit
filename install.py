#!/usr/bin/env python3
"""Install all six BANDIT skills without changing unrelated project files."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
import unicodedata

NAME = "bandit"
MARKER = ".bandit-install.json"
ROOT = Path(__file__).resolve().parent
SKILL = Path("skills") / NAME
SKILL_NAMES = (NAME, "bandit-research", "bandit-decide", "bandit-specify", "bandit-review", "bandit-update")
IGNORED = {".git", "__pycache__", ".DS_Store"}


class InstallError(ValueError):
    """A conflict or unsafe path that must be resolved without overwriting it."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def absolute(path: Path) -> Path:
    return Path(os.path.abspath(path.expanduser()))


def canonical_name(name: str) -> str:
    return unicodedata.normalize("NFC", name).casefold()


def is_within(path: Path, directory: Path) -> bool:
    """Conservatively include case/Unicode aliases and existing filesystem aliases."""
    path, directory = absolute(path), absolute(directory)
    parts = tuple(canonical_name(part) for part in path.parts)
    base = tuple(canonical_name(part) for part in directory.parts)
    if parts[:len(base)] == base:
        return True
    if directory.exists():
        for candidate in (path, *path.parents):
            if candidate.exists() and os.path.samefile(candidate, directory):
                return True
    return False


def check_path(path: Path) -> None:
    """Reject symlinks/junctions in every existing component, including dangling links."""
    path = absolute(path)
    for part in (*reversed(path.parents), path):
        try:
            info = part.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400):
            raise InstallError(f"Symlink or junction is not allowed: {part}")
        if part != path and not stat.S_ISDIR(info.st_mode):
            raise InstallError(f"Parent path is not a directory: {part}")


def regular_bytes(path: Path) -> bytes:
    check_path(path)
    if not path.is_file() or not stat.S_ISREG(path.stat().st_mode):
        raise InstallError(f"Expected a regular file: {path}")
    return path.read_bytes()


def relative_name(name: str) -> str:
    parsed = PurePosixPath(name)
    if (not isinstance(name, str) or not name or "\\" in name or ":" in name
            or parsed.is_absolute() or any(p in {"", ".", ".."} for p in name.split("/"))
            or any(ord(c) < 32 for c in name) or parsed.as_posix() != name):
        raise InstallError(f"Unsafe relative file name: {name!r}")
    return name


def tree_files(directory: Path) -> dict[str, bytes]:
    check_path(directory)
    if not directory.is_dir():
        raise InstallError(f"Missing directory: {directory}")
    result: dict[str, bytes] = {}
    seen: set[str] = set()
    for parent, directories, files in os.walk(directory, followlinks=False):
        directories[:] = sorted(d for d in directories if d not in IGNORED)
        for name in directories:
            check_path(Path(parent) / name)
        for name in sorted(files):
            if name in IGNORED or name.endswith((".pyc", ".pyo")):
                continue
            path = Path(parent) / name
            relative = relative_name(path.relative_to(directory).as_posix())
            if canonical_name(relative) in seen:
                raise InstallError(f"Case-insensitive path collision: {relative}")
            seen.add(canonical_name(relative))
            result[relative] = regular_bytes(path)
    return result


def version(root: Path) -> str:
    value = regular_bytes(root / "VERSION").decode("utf-8").strip()
    if not re.fullmatch(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)", value):
        raise InstallError("VERSION must contain a stable semantic version, e.g. 0.2.0")
    return value


def read_marker(destination: Path, skill_name: str = NAME) -> dict | None:
    path = destination / MARKER
    check_path(path)
    if not path.exists():
        return None
    try:
        value = json.loads(regular_bytes(path))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise InstallError(f"Invalid ownership marker: {path}") from exc
    if not isinstance(value, dict) or value.get("format") != 1 or value.get("name") != skill_name or not isinstance(value.get("files"), dict):
        raise InstallError(f"Unrecognized ownership marker: {path}")
    seen: set[str] = set()
    for name, checksum in value["files"].items():
        relative_name(name)
        if canonical_name(name) == canonical_name(MARKER) or canonical_name(name) in seen or not isinstance(checksum, str) or not re.fullmatch(r"[0-9a-f]{64}", checksum):
            raise InstallError(f"Invalid managed file entry: {name}")
        seen.add(canonical_name(name))
    return value


def make_plan(source_root: Path, destination: Path, skill_name: str = NAME) -> tuple[dict, dict[str, bytes], bytes]:
    if skill_name not in SKILL_NAMES:
        raise InstallError(f"Unknown BANDIT skill: {skill_name}")
    source_root, destination = absolute(source_root), absolute(destination)
    check_path(destination)
    if destination.exists() and not destination.is_dir():
        raise InstallError(f"Destination is not a directory: {destination}")
    source = source_root / "skills" / skill_name
    if is_within(destination, source) or is_within(source, destination):
        raise InstallError("Source and installation destination must not overlap")
    payload = tree_files(source)
    if "SKILL.md" not in payload or MARKER in payload:
        raise InstallError("Source must contain SKILL.md and must not contain an installation marker")
    installed = read_marker(destination, skill_name)
    previous = installed["files"] if installed else {}
    previous_case = {canonical_name(name): name for name in previous}
    for name in payload:
        old_name = previous_case.get(canonical_name(name))
        if old_name is not None and old_name != name:
            raise InstallError(
                f"Case-only managed path rename requires manual migration: {old_name} -> {name}. "
                "Nothing installed; use a fresh destination to preserve the existing installation."
            )
    desired = {"format": 1, "name": skill_name, "version": version(source_root),
               "files": {name: digest(data) for name, data in sorted(payload.items())}}
    changes, conflicts, unchanged = [], [], 0
    for name in sorted(set(previous) | set(payload)):
        target = destination / name
        check_path(target)
        if target.exists() and not target.is_file():
            conflicts.append(f"not a regular file: {name}")
            continue
        current = digest(regular_bytes(target)) if target.exists() else None
        old, new = previous.get(name), desired["files"].get(name)
        if new is not None and current == new:
            unchanged += 1
        elif new is not None and current is None:
            if old is not None:
                conflicts.append(f"managed file was deleted locally: {name}")
            else:
                changes.append({"action": "add", "path": name})
        elif new is not None and old is not None and current == old:
            changes.append({"action": "update", "path": name})
        elif new is None and current is None:
            continue
        elif new is None and current == old:
            changes.append({"action": "remove", "path": name})
        else:
            conflicts.append(f"local modification or unmanaged conflict: {name}")
    if conflicts:
        raise InstallError("Nothing installed; preserve or move these files before retrying:\n  " + "\n  ".join(conflicts))
    marker = (json.dumps(desired, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()
    marker_change = installed != desired
    report = {"name": skill_name, "status": "plan", "source": str(source), "destination": str(destination),
              "version": desired["version"], "managed": installed is not None,
              "changes": changes, "unchanged_files": unchanged, "marker_change": marker_change}
    return report, payload, marker


def atomic_write(path: Path, data: bytes) -> None:
    check_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    check_path(path.parent)
    descriptor, temporary = tempfile.mkstemp(prefix=".bandit-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
        check_path(path)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def _install_plans(planner, dry_run: bool = False) -> list[dict]:
    """Preflight every destination, then apply one rollback journal under all locks."""
    plans = planner()
    if dry_run:
        return [report for report, _, _ in plans]
    if all(not report["changes"] and not report["marker_change"] for report, _, _ in plans):
        return [{**report, "status": "unchanged"} for report, _, _ in plans]
    locks: list[Path] = []
    try:
        destinations = sorted((Path(report["destination"]) for report, _, _ in plans), key=lambda item: canonical_name(str(item)))
        for destination in destinations:
            check_path(destination.parent)
            destination.parent.mkdir(parents=True, exist_ok=True)
            lock = destination.parent / ("." + destination.name + ".bandit.lock")
            check_path(lock)
            try:
                lock_fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            except FileExistsError as exc:
                raise InstallError(f"Install lock exists: {lock}; retry after the other installer finishes") from exc
            os.close(lock_fd)
            locks.append(lock)
        plans = planner()
        changes: list[tuple[Path, bytes | None]] = []
        for report, payload, marker in plans:
            destination = Path(report["destination"])
            for item in report["changes"]:
                changes.append((destination / item["path"], None if item["action"] == "remove" else payload[item["path"]]))
            if report["marker_change"]:
                changes.append((destination / MARKER, marker))
        backups = {target: regular_bytes(target) if target.exists() else None for target, _ in changes}
        applied: list[tuple[Path, bytes | None]] = []
        try:
            for target, desired in changes:
                current = regular_bytes(target) if target.exists() else None
                if current != backups[target]:
                    raise InstallError(f"Destination changed during installation; preserving the edit: {target}")
                if desired is None:
                    check_path(target)
                    target.unlink()
                else:
                    atomic_write(target, desired)
                applied.append((target, desired))
        except (OSError, InstallError):
            for target, installed in reversed(applied):
                current = regular_bytes(target) if target.exists() else None
                if current != installed:
                    # An editor changed it after our write; retain that edit.
                    continue
                old = backups[target]
                if old is None:
                    check_path(target)
                    target.unlink(missing_ok=True)
                else:
                    atomic_write(target, old)
            raise
    finally:
        for lock in reversed(locks):
            lock.unlink()
    return [{**report, "status": ("updated" if report["managed"] else "installed")
             if report["changes"] or report["marker_change"] else "unchanged"} for report, _, _ in plans]


def install_into(source_root: Path, destination: Path, dry_run: bool = False, skill_name: str = NAME) -> dict:
    """Single-skill API retained for existing callers; the CLI installs the bundle."""
    return _install_plans(lambda: [make_plan(source_root, destination, skill_name)], dry_run)[0]


def install_bundle(source_root: Path, destination: Path, dry_run: bool = False) -> dict:
    source_root, destination = absolute(source_root), absolute(destination)
    destinations = {name: destination if name == NAME else destination.parent / name for name in SKILL_NAMES}
    targets = list(destinations.values())
    for index, target in enumerate(targets):
        if any(is_within(target, other) or is_within(other, target) for other in targets[:index]):
            raise InstallError("The core destination collides with a specialist skill destination")
        for name in SKILL_NAMES:
            source = source_root / "skills" / name
            if is_within(target, source) or is_within(source, target):
                raise InstallError("Source and installation destination must not overlap")

    def planner():
        plans = [make_plan(source_root, destinations[name], name) for name in SKILL_NAMES]
        if len({report["version"] for report, _, _ in plans}) != 1:
            raise InstallError("Source version changed during installation; retry with a stable package")
        return plans

    reports = _install_plans(planner, dry_run)
    managed = any(report["managed"] for report in reports)
    status = "plan" if dry_run else "unchanged" if all(report["status"] == "unchanged" for report in reports) else "updated" if managed else "installed"
    return {"status": status, "source": str(source_root / "skills"), "destination": str(destination),
            "destination_root": str(destination.parent), "version": reports[0]["version"], "managed": managed,
            "commands": ["$" + name for name in SKILL_NAMES], "skills": reports,
            "changes": [{"skill": report["name"], "action": item["action"], "path": report["name"] + "/" + item["path"]}
                        for report in reports for item in report["changes"]],
            "unchanged_files": sum(report["unchanged_files"] for report in reports),
            "marker_change": any(report["marker_change"] for report in reports)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--repo", type=Path, help="Existing project root; installs all six skills to .agents/skills")
    target.add_argument("--dest", type=Path, help="Exact core skill directory; specialists install beside it")
    parser.add_argument("--plan", action="store_true", help="Show changes without creating or modifying files")
    args = parser.parse_args(argv)
    try:
        if sys.version_info < (3, 11):
            raise InstallError("Python 3.11 or newer is required")
        if args.repo is not None:
            root = absolute(args.repo)
            check_path(root)
            if not root.is_dir():
                raise InstallError(f"--repo must be an existing directory: {root}")
            destination = root / ".agents" / "skills" / NAME
        else:
            destination = absolute(args.dest)
        print(json.dumps(install_bundle(ROOT, destination, args.plan), ensure_ascii=False, indent=2))
        return 0
    except (InstallError, OSError, UnicodeError) as exc:
        print(f"bandit install: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
