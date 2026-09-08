#!/usr/bin/env python3
"""Run one isolated, opt-in Codex CLI development case. Uses your host account."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
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


def snapshot(directory: Path) -> dict[str, str]:
    return {p.relative_to(directory).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(directory.rglob("*")) if p.is_file()}


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
    if edit_artifact:
        target = (workspace / edit_artifact).resolve()
        if not target.is_relative_to(workspace / "input") or not target.is_file():
            raise ValueError("--edit-artifact must name an existing file under input/ in the temporary workspace")
        edit_artifact = target.relative_to(workspace).as_posix()
        shutil.copytree(workspace / "input", run / "original-input")
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
    metadata = {"case": case, "arm": arm, "codex_version": subprocess.check_output(["codex", "--version"], text=True).strip(),
                "command": command, "model_override": None, "config": "--ignore-user-config; host defaults",
                "upstream_commit": UPSTREAM_COMMIT if arm == "upstream" else None,
                "input_sha256": snapshot(workspace / "input"),
                "instruction_sha256": snapshot(workspace / instruction_scope) if arm != "baseline" else {},
                "invocation": f"${arm}" if arm in SPECIALISTS else None,
                "editable_artifact": edit_artifact}
    start = time.monotonic()
    with (run / "events.jsonl").open("w", encoding="utf-8") as events, (run / "stderr.txt").open("w", encoding="utf-8") as errors:
        result = subprocess.run(command, input=prompt, text=True, stdout=events, stderr=errors)
    metadata.update(exit_code=result.returncode, elapsed_seconds=round(time.monotonic() - start, 3),
                    input_after_sha256=snapshot(workspace / "input"),
                    instruction_after_sha256=snapshot(workspace / instruction_scope) if arm != "baseline" else {})
    (run / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"run": str(run), "exit_code": result.returncode}), flush=True)
    return result.returncode


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
