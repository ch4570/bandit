#!/usr/bin/env python3
"""Install the PM Craft text skill without changing unrelated project files."""
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

NAME = "pm-craft"
MARKER = ".pm-craft-install.json"
ROOT = Path(__file__).resolve().parent
SKILL = Path("skills") / NAME
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
        raise InstallError("VERSION must contain a stable semantic version, e.g. 0.1.0")
    return value


def read_marker(destination: Path) -> dict | None:
    path = destination / MARKER
    check_path(path)
    if not path.exists():
        return None
    try:
        value = json.loads(regular_bytes(path))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise InstallError(f"Invalid ownership marker: {path}") from exc
    if not isinstance(value, dict) or value.get("format") != 1 or value.get("name") != NAME or not isinstance(value.get("files"), dict):
        raise InstallError(f"Unrecognized ownership marker: {path}")
    seen: set[str] = set()
    for name, checksum in value["files"].items():
        relative_name(name)
        if canonical_name(name) == canonical_name(MARKER) or canonical_name(name) in seen or not isinstance(checksum, str) or not re.fullmatch(r"[0-9a-f]{64}", checksum):
            raise InstallError(f"Invalid managed file entry: {name}")
        seen.add(canonical_name(name))
    return value


def make_plan(source_root: Path, destination: Path) -> tuple[dict, dict[str, bytes], bytes]:
    source_root, destination = absolute(source_root), absolute(destination)
    check_path(destination)
    if destination.exists() and not destination.is_dir():
        raise InstallError(f"Destination is not a directory: {destination}")
    source = source_root / SKILL
    if is_within(destination, source) or is_within(source, destination):
        raise InstallError("Source and installation destination must not overlap")
    payload = tree_files(source)
    if "SKILL.md" not in payload or MARKER in payload:
        raise InstallError("Source must contain SKILL.md and must not contain an installation marker")
    installed = read_marker(destination)
    previous = installed["files"] if installed else {}
    previous_case = {canonical_name(name): name for name in previous}
    for name in payload:
        old_name = previous_case.get(canonical_name(name))
        if old_name is not None and old_name != name:
            raise InstallError(
                f"Case-only managed path rename requires manual migration: {old_name} -> {name}. "
                "Nothing installed; use a fresh destination to preserve the existing installation."
            )
    desired = {"format": 1, "name": NAME, "version": version(source_root),
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
    report = {"status": "plan", "source": str(source), "destination": str(destination),
              "version": desired["version"], "managed": installed is not None,
              "changes": changes, "unchanged_files": unchanged, "marker_change": marker_change}
    return report, payload, marker


def atomic_write(path: Path, data: bytes) -> None:
    check_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    check_path(path.parent)
    descriptor, temporary = tempfile.mkstemp(prefix=".pm-craft-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
        check_path(path)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def install_into(source_root: Path, destination: Path, dry_run: bool = False) -> dict:
    destination = absolute(destination)
    report, payload, marker = make_plan(source_root, destination)
    if dry_run:
        return report
    if not report["changes"] and not report["marker_change"]:
        return {**report, "status": "unchanged"}
    # Serialize installers for this destination; never create this lock for --plan.
    check_path(destination.parent)
    destination.parent.mkdir(parents=True, exist_ok=True)
    lock = destination.parent / ("." + destination.name + ".pm-craft.lock")
    check_path(lock)
    try:
        lock_fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise InstallError(f"Install lock exists: {lock}; retry after the other installer finishes") from exc
    os.close(lock_fd)
    backups: dict[Path, bytes | None] = {}
    try:
        report, payload, marker = make_plan(source_root, destination)
        for item in report["changes"]:
            target = destination / item["path"]
            backups[target] = regular_bytes(target) if target.exists() else None
        marker_path = destination / MARKER
        backups[marker_path] = regular_bytes(marker_path) if marker_path.exists() else None
        applied: list[Path] = []
        installed_bytes: dict[Path, bytes | None] = {}
        try:
            for item in report["changes"]:
                target = destination / item["path"]
                current = regular_bytes(target) if target.exists() else None
                if current != backups[target]:
                    raise InstallError(f"Destination changed during installation; preserving the edit: {target}")
                if item["action"] == "remove":
                    check_path(target)
                    target.unlink()
                    installed_bytes[target] = None
                else:
                    atomic_write(target, payload[item["path"]])
                    installed_bytes[target] = payload[item["path"]]
                applied.append(target)
            current_marker = regular_bytes(marker_path) if marker_path.exists() else None
            if current_marker != backups[marker_path]:
                raise InstallError("Ownership marker changed during installation; preserving it")
            atomic_write(marker_path, marker)
            installed_bytes[marker_path] = marker
            applied.append(marker_path)
        except (OSError, InstallError):
            # Recover touched contents after an ordinary I/O failure. No unrelated files are removed.
            for target in reversed(applied):
                old = backups[target]
                current = regular_bytes(target) if target.exists() else None
                if current != installed_bytes[target]:
                    # An editor changed it after our write: keep that edit, never restore over it.
                    continue
                if old is None:
                    check_path(target)
                    target.unlink(missing_ok=True)
                else:
                    atomic_write(target, old)
            raise
    finally:
        lock.unlink()
    return {**report, "status": "updated" if report["managed"] else "installed"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--repo", type=Path, help="Existing project root; installs to .agents/skills/pm-craft")
    target.add_argument("--dest", type=Path, help="Exact skill directory (not its parent)")
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
        print(json.dumps(install_into(ROOT, destination, args.plan), ensure_ascii=False, indent=2))
        return 0
    except (InstallError, OSError, UnicodeError) as exc:
        print(f"pm-craft install: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
