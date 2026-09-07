#!/usr/bin/env python3
"""Check BANDIT packaging, metadata, and local references; not PM effectiveness."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import install


def scalar(value: str):
    value = value.strip()
    if value.startswith('"'):
        return json.loads(value)
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    if value in {"true", "false"}:
        return value == "true"
    if not value or value.startswith(("[", "{", "&", "*", "!")):
        raise ValueError("Use plain or quoted scalar values and nested mappings in metadata")
    return value


def yaml_mapping(text: str) -> dict:
    """Parse the small mapping/scalar YAML subset used by this skill's metadata."""
    result: dict = {}
    stack = [(-1, result)]
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        index += 1
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if "\t" in line:
            raise ValueError("Metadata indentation must use spaces")
        match = re.fullmatch(r"( *)([A-Za-z_][\w-]*):(?: +(.*))?", line)
        if not match:
            raise ValueError(f"Unsupported metadata syntax: {line}")
        indent, key, value = len(match[1]), match[2], match[3]
        while stack[-1][0] >= indent:
            stack.pop()
        mapping = stack[-1][1]
        if key in mapping:
            raise ValueError(f"Duplicate metadata key: {key}")
        if value is None:
            nested: dict = {}
            mapping[key] = nested
            stack.append((indent, nested))
        elif value in {"|", ">", "|-", ">-"}:
            block = []
            while index < len(lines) and (not lines[index].strip() or len(lines[index]) - len(lines[index].lstrip()) > indent):
                block.append(lines[index].strip())
                index += 1
            mapping[key] = (" " if value.startswith(">") else "\n").join(block).strip()
        else:
            mapping[key] = scalar(value)
    return result


def frontmatter(text: str) -> dict:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("Unterminated frontmatter") from exc
    return yaml_mapping("\n".join(lines[1:end]))


def without_code(text: str) -> str:
    return re.sub(r"^\s*(`{3,}|~{3,}).*?^\s*\1\s*$", "", text, flags=re.M | re.S)


def local_references(path: Path, text: str, boundary: Path) -> list[str]:
    errors = []
    prose = without_code(text)
    links = re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", prose)
    # Bare code spans are used for required skill assets/references, not arbitrary code examples.
    links += re.findall(r"`((?:references|assets|agents)/[^`]+)`", prose)
    for raw in links:
        target = raw.strip()
        if target.startswith("<") and ">" in target:
            target = target[1:target.index(">")]
        else:
            target = target.split(' "', 1)[0].split(" '", 1)[0]
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        decoded = unquote(parsed.path)
        if any(char in decoded for char in "*{}<>"):
            continue
        resolved = (path.parent / decoded).resolve()
        if resolved != boundary and boundary not in resolved.parents:
            errors.append(f"{path.name}: local reference leaves its package: {target}")
        elif not resolved.exists():
            errors.append(f"{path.name}: missing local reference: {target}")
    return errors


def validate(root: Path) -> dict:
    root = root.resolve(strict=True)
    errors: list[str] = []
    skill = root / install.SKILL
    try:
        version = install.version(root)
        payload = install.tree_files(skill)
    except (ValueError, OSError, UnicodeError) as exc:
        return {"ok": False, "errors": [str(exc)], "checks": "structure and references only"}
    package = root / "package.json"
    if package.exists():
        try:
            data = json.loads(install.regular_bytes(package))
            if data.get("name") != "@ch4570/bandit" or data.get("version") != version:
                errors.append("package.json: name/version must match @ch4570/bandit and VERSION")
        except (ValueError, AttributeError, OSError) as exc:
            errors.append(f"package.json: {exc}")
    try:
        metadata = frontmatter(payload.get("SKILL.md", b"").decode("utf-8"))
        if metadata.get("name") != install.NAME:
            errors.append("SKILL.md name must match the bandit directory")
        if not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
            errors.append("SKILL.md needs a nonempty description")
    except (ValueError, UnicodeError) as exc:
        errors.append(f"SKILL.md: {exc}")
    try:
        ui = yaml_mapping(payload.get("agents/openai.yaml", b"").decode("utf-8"))
        interface = ui.get("interface", {})
        for field in ("display_name", "short_description", "default_prompt"):
            if not isinstance(interface.get(field), str) or not interface[field].strip():
                errors.append(f"agents/openai.yaml: interface.{field} is required")
        if "$bandit" not in interface.get("default_prompt", ""):
            errors.append("agents/openai.yaml: default_prompt must mention $bandit")
        for field in ("icon_small", "icon_large"):
            if field in interface:
                icon = skill / interface[field]
                if not icon.is_file() or skill.resolve() not in icon.resolve().parents:
                    errors.append(f"agents/openai.yaml: {field} must resolve inside the skill")
    except (ValueError, TypeError, AttributeError, UnicodeError) as exc:
        errors.append(f"agents/openai.yaml: {exc}")
    for name, content in payload.items():
        if name.endswith(".md"):
            try:
                errors.extend(local_references(skill / name, content.decode("utf-8"), skill.resolve()))
            except (UnicodeError, ValueError) as exc:
                errors.append(f"{name}: {exc}")
    # A plugin manifest is optional: native skills do not need one.
    for manifest in (root / ".codex-plugin/plugin.json", root / ".claude-plugin/plugin.json"):
        if manifest.exists():
            try:
                data = json.loads(install.regular_bytes(manifest))
                if data.get("name") != install.NAME or data.get("version") != version:
                    errors.append(f"{manifest.relative_to(root)}: name/version must match bandit and VERSION")
            except (ValueError, AttributeError, OSError) as exc:
                errors.append(f"{manifest}: {exc}")
    return {"ok": not errors, "version": version, "skill_files": len(payload),
            "errors": errors, "checks": "structure and references only; no claim of PM effectiveness"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Distribution root to validate")
    args = parser.parse_args(argv)
    try:
        report = validate(args.root)
    except (ValueError, OSError) as exc:
        report = {"ok": False, "errors": [str(exc)]}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
