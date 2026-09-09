#!/usr/bin/env python3
"""Run one isolated, opt-in Codex CLI development case. Uses your host account."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
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
CASES = tuple(sorted(p.name for p in (ROOT / "evals" / "cases").iterdir()
                     if p.is_dir() and (p / "request.md").is_file()))


def snapshot(directory: Path) -> dict[str, str]:
    return {p.relative_to(directory).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(directory.rglob("*")) if p.is_file()}


def run_case(case: str, arm: str, output: Path, upstream: Path | None,
             edit_artifact: str | None = None, standalone: bool = False,
             fixture_dir: Path | None = None, web_search: str = "disabled",
             model: str | None = None) -> int:
    if web_search not in ("disabled", "live"):
        raise ValueError("Web search must be disabled or explicitly set to live")
    if model is not None and (not isinstance(model, str) or not model or model.startswith("-")
                              or re.search(r"[\s\x00-\x1f\x7f-\x9f]", model)):
        raise ValueError("Model must be a nonempty identifier without whitespace, control characters or a leading '-'")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", case):
        raise ValueError("Case names must contain lowercase letters, digits and hyphens")
    if fixture_dir is None and case not in CASES:
        raise ValueError(f"Unknown case: {case}")
    if standalone and arm not in SPECIALISTS:
        raise ValueError("--standalone requires a specialist arm")
    fixture = (fixture_dir or ROOT / "evals" / "cases" / case).resolve(strict=True)
    if not fixture.is_dir() or not (fixture / "request.md").is_file():
        raise ValueError("Fixture directory must contain request.md")
    if any(p.is_symlink() for p in fixture.rglob("*")):
        raise ValueError("Fixture files must not be symlinks")
    run = output.resolve() / f"{case}--{arm}"
    if run.is_relative_to(fixture) or fixture.is_relative_to(run):
        raise ValueError("Run output and fixture directory must not overlap")
    if arm == "upstream":
        if fixture_dir is not None:
            raise ValueError("Custom fixture directories have no reviewed upstream workflow mapping")
        if case not in ROUTES:
            raise ValueError(f"No reviewed upstream workflow mapping for case {case}")
        if upstream is None:
            raise ValueError("--upstream is required for the upstream arm")
        commit = subprocess.check_output(["git", "-C", str(upstream), "rev-parse", "HEAD"], text=True).strip()
        if commit != UPSTREAM_COMMIT:
            raise ValueError(f"Expected upstream commit {UPSTREAM_COMMIT}, got {commit}")
        if subprocess.check_output(["git", "-C", str(upstream), "status", "--porcelain"], text=True).strip():
            raise ValueError("Upstream checkout must be clean")
    instruction_source = None
    if arm in SPECIALISTS:
        instruction_source = ROOT / "skills" / arm if standalone else ROOT / "skills"
    elif arm == "bandit":
        instruction_source = ROOT / "skills" / "bandit"
    elif arm == "upstream":
        instruction_source = upstream
    if instruction_source is not None:
        instruction_source = instruction_source.resolve(strict=True)
        if run.is_relative_to(instruction_source) or instruction_source.is_relative_to(run):
            raise ValueError("Run output and instruction source must not overlap")
        # copytree follows nested links by default, including links back into
        # the run output. Only ordinary resources are supported in the snapshot;
        # upstream's excluded control/cache entries are not resources to copy.
        ignored = {".git", "__pycache__"} if arm == "upstream" else set()
        if any(p.is_symlink() for p in instruction_source.rglob("*")
               if not ignored.intersection(p.relative_to(instruction_source).parts)):
            raise ValueError("Instruction source files must not be symlinks")
    if run.exists():
        raise ValueError(f"Run already exists; use a new output directory: {run}")
    if edit_artifact:
        relative = Path(edit_artifact)
        if relative.is_absolute() or not relative.parts or relative.parts[0] != "input" or ".." in relative.parts:
            raise ValueError("--edit-artifact must name an existing file under input/ in the temporary workspace")
        target = fixture.joinpath(*relative.parts[1:])
        if not target.is_file():
            raise ValueError("--edit-artifact must name an existing file under input/ in the temporary workspace")
        edit_artifact = relative.as_posix()
    workspace = run / "workspace"
    workspace.mkdir(parents=True)
    shutil.copytree(fixture, workspace / "input")
    # Keep pre-run bytes even if a task unexpectedly changes a read-only input.
    shutil.copytree(workspace / "input", run / "original-input")
    if arm in SPECIALISTS:
        if standalone:
            shutil.copytree(instruction_source, workspace / ".agents" / "skills" / arm)
        else:
            shutil.copytree(instruction_source, workspace / ".agents" / "skills")
        instruction = f"Use ${arm} for this task. The requested skill is installed in this project."
    elif arm == "bandit":
        shutil.copytree(instruction_source, workspace / "instructions" / "bandit")
        instruction = "Use instructions/bandit/SKILL.md and the relevant references it routes to."
    elif arm == "upstream":
        # Preserve all dependencies. Routes identify the relevant entrypoints;
        # the agent may follow further skill references within this snapshot.
        shutil.copytree(instruction_source, workspace / "instructions" / "upstream",
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
    if arm != "baseline":
        shutil.copytree(workspace / instruction_scope, run / "original-instructions")
    output_instruction = (
        f"You may edit only {edit_artifact} as the task requests. Leave every other file unchanged. "
        "Summarize the result in your final answer. "
        if edit_artifact else
        "Do not change files. Put the requested artifact in your final answer; the runner will save it. "
    )
    source_instruction = (
        "Public web search and reading are allowed only for the research requested in the task. "
        "Do not sign in, submit forms, contact anyone, buy anything, or change external state. "
        "Cite the actual source pages and distinguish checked facts from unavailable information. "
        if web_search == "live" else
        "Do not browse or contact anyone. "
    )
    prompt = (
        "Perform the user's product-planning task in input/request.md. Read the other files in input/ "
        "as its raw supporting artifacts. " + instruction + "\n"
        f"Use only these local task inputs and, if provided, the {instruction_scope}/ snapshot in this workspace. "
        "Do not inspect other repositories, AGENTS files, evaluation rubrics, examples, other outputs, "
        "or prior sessions. " + source_instruction + "Do not execute the supplied product code "
        "or tests. " + output_instruction + "This is the user's task, not a review of the instructions.\n"
    )
    (run / "prompt.txt").write_text(prompt, encoding="utf-8")
    command = ["codex", "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check",
               "-c", f'web_search="{web_search}"',
               "--sandbox", "workspace-write" if edit_artifact else "read-only", "--color", "never", "--json", "-C", str(workspace),
               "-o", str(run / "output.md")]
    if model is not None:
        command.extend(["--model", model])
    command.append("-")
    model_config = "host model defaults" if model is None else "explicit model override"
    metadata = {"case": case, "arm": arm, "codex_version": None,
                "command": command, "model_override": model,
                "config": f"--ignore-user-config; {model_config}; explicit web_search",
                "web_search": web_search,
                "runner_status": "running",
                "started_at_utc": datetime.now(timezone.utc).isoformat(),
                "upstream_commit": UPSTREAM_COMMIT if arm == "upstream" else None,
                "input_sha256": snapshot(workspace / "input"),
                "instruction_sha256": snapshot(workspace / instruction_scope) if arm != "baseline" else {},
                "invocation": f"${arm}" if arm in SPECIALISTS else None,
                "standalone_specialist": standalone,
                "custom_fixture": fixture_dir is not None,
                "editable_artifact": edit_artifact}
    (run / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    start = time.monotonic()
    with (run / "events.jsonl").open("w", encoding="utf-8") as events, (run / "stderr.txt").open("w", encoding="utf-8") as errors:
        phase = "version_probe"
        try:
            metadata["codex_version"] = subprocess.check_output(["codex", "--version"], text=True, stderr=errors).strip()
            (run / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
            phase = "task_launch"
            result = subprocess.run(command, input=prompt, text=True, stdout=events, stderr=errors)
        except (OSError, subprocess.CalledProcessError) as exc:
            # The task never returned an exit code. Preserve this runner failure
            # separately, including a failed version probe before task launch.
            metadata.update(runner_status="launch_failed", exit_code=None,
                            runner_error={"phase": phase, "type": type(exc).__name__,
                                          "message": str(exc) or repr(exc)})
            raise
        else:
            metadata.update(runner_status="exited", exit_code=result.returncode)
        finally:
            metadata.update(elapsed_seconds=round(time.monotonic() - start, 3),
                            finished_at_utc=datetime.now(timezone.utc).isoformat(),
                            input_after_sha256=snapshot(workspace / "input"),
                            instruction_after_sha256=snapshot(workspace / instruction_scope) if arm != "baseline" else {})
            (run / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"run": str(run), "exit_code": result.returncode}), flush=True)
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True,
                        help="Built-in case name, or a run label when --fixture-dir is supplied")
    parser.add_argument("--fixture-dir", type=Path,
                        help="Use only raw files in this directory (including request.md), for staged task sequences")
    parser.add_argument("--arm", choices=["baseline", "upstream", "bandit", *SPECIALISTS], required=True)
    parser.add_argument("--upstream", type=Path)
    parser.add_argument("--edit-artifact", help="Permit edits to this one existing input/ file in the isolated workspace")
    parser.add_argument("--standalone", action="store_true",
                        help="Copy only the selected specialist and its resources, without sibling skills")
    parser.add_argument("--web-search", choices=["disabled", "live"], default="disabled",
                        help="Opt into public web research only when the task requests it; disabled by default")
    parser.add_argument("--model", metavar="MODEL_ID",
                        help="Request this model for the run; omitted uses host defaults (not a verified backend identity)")
    parser.add_argument("--output-dir", type=Path, required=True,
                        help="New run artifacts are written here; your Codex account's usage applies")
    args = parser.parse_args()
    try:
        return run_case(args.case, args.arm, args.output_dir, args.upstream, args.edit_artifact,
                        args.standalone, args.fixture_dir, args.web_search, args.model)
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(2, f"bandit eval: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
