#!/usr/bin/env python3
"""Build a reproducible, dependency-free BANDIT ZIP and SHA-256 manifest."""
from __future__ import annotations

import argparse
import io
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import install
from scripts import validate

INVENTORY = "BUNDLE-MANIFEST.json"
DIRECTORIES = ("docs", "examples", "evals", "assets", "scripts", "tests", "tests-node", "bin", "lib", ".github")
EXTENSIONS = {".md", ".py", ".js", ".mjs", ".cjs", ".json", ".jsonl", ".yaml", ".yml", ".txt", ".csv", ".toml", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".html"}


def contents(root: Path) -> dict[str, bytes]:
    files = {f"skills/{install.NAME}/{name}": data for name, data in install.tree_files(root / install.SKILL).items()}
    for name in ("VERSION", "LICENSE", "README.md", "install.py"):
        files[name] = install.regular_bytes(root / name)
    for name in ("package.json", "package-lock.json"):
        if (root / name).exists():
            files[name] = install.regular_bytes(root / name)
    for path in sorted(root.glob("*.md")):
        files[path.name] = install.regular_bytes(path)
    for name in (".editorconfig", ".gitattributes", ".gitignore"):
        if (root / name).exists():
            files[name] = install.regular_bytes(root / name)
    for name in DIRECTORIES:
        if (root / name).exists():
            for relative, data in install.tree_files(root / name).items():
                if Path(relative).suffix.lower() in EXTENSIONS:
                    files[f"{name}/{relative}"] = data
    return files


def archive_bytes(root: Path) -> tuple[str, bytes, dict]:
    validation = validate.validate(root)
    if not validation["ok"]:
        raise install.InstallError("Skill validation failed:\n  " + "\n  ".join(validation["errors"]))
    release = install.version(root)
    files = contents(root)
    inventory = {"format": 1, "name": install.NAME, "version": release,
                 "files": {name: install.digest(data) for name, data in sorted(files.items())}}
    files[INVENTORY] = (json.dumps(inventory, sort_keys=True, ensure_ascii=False, indent=2) + "\n").encode()
    stream = io.BytesIO()
    # Fixed timestamps, file mode, sort order, and stored bytes keep builds identical
    # across platforms and zlib versions. npm consumers do not need this helper.
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, data in sorted(files.items()):
            entry = zipfile.ZipInfo(f"bandit-{release}/{name}", date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = (0o100755 if name.startswith("bin/") else 0o100644) << 16
            archive.writestr(entry, data)
    return release, stream.getvalue(), inventory


def build_bundle(root: Path, output: Path) -> dict:
    root, output = root.resolve(strict=True), install.absolute(output)
    install.check_path(output)
    for directory in (*DIRECTORIES, str(install.SKILL)):
        source = root / directory
        if install.is_within(output, source):
            raise install.InstallError("Output directory must not be inside bundled input directories")
    release, data, inventory = archive_bytes(root)
    name = f"bandit-{release}.zip"
    checksum = install.digest(data)
    checksum_line = f"{checksum}  {name}\n".encode("ascii")
    artifacts = {name: data, name + ".sha256": checksum_line}
    checksum_file = output / "SHA256SUMS.txt"
    entries = {}
    if checksum_file.exists():
        for line in install.regular_bytes(checksum_file).decode("ascii").splitlines():
            parts = line.split("  ")
            if len(parts) != 2 or len(parts[0]) != 64 or any(c not in "0123456789abcdef" for c in parts[0]) or Path(parts[1]).name != parts[1]:
                raise install.InstallError("Existing SHA256SUMS.txt is not a checksum manifest; leaving it unchanged")
            if parts[1] in entries:
                raise install.InstallError("Existing checksum manifest contains duplicate entries")
            entries[parts[1]] = parts[0]
    if name in entries and entries[name] != checksum:
        raise install.InstallError(f"Version {release} already has a different checksum; choose a new version or a new output directory")
    entries[name] = checksum
    artifacts["SHA256SUMS.txt"] = "".join(f"{value}  {key}\n" for key, value in sorted(entries.items())).encode("ascii")
    for filename, value in artifacts.items():
        target = output / filename
        install.check_path(target)
        if target.exists() and filename != "SHA256SUMS.txt" and install.regular_bytes(target) != value:
            raise install.InstallError(f"Existing artifact differs; leaving it unchanged: {target}")
    output.mkdir(parents=True, exist_ok=True)
    for filename, value in artifacts.items():
        target = output / filename
        if not target.exists() or install.regular_bytes(target) != value:
            install.atomic_write(target, value)
    return {"artifact": str(output / name), "checksum": str(output / (name + ".sha256")),
            "manifest": str(checksum_file), "sha256": checksum, "version": release,
            "files": len(inventory["files"]) + 1, "bytes": len(data)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(build_bundle(ROOT, args.output_dir), indent=2))
        return 0
    except (ValueError, OSError, UnicodeError) as exc:
        print(f"bandit bundle: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
