# Install PM Craft

[Overview](README.md) · [한국어 소개](README.ko.md) · [Usage](docs/usage.md)

Install the complete `pm-craft` skill folder in a location your agent can read. The supplied installer requires Python 3.11+ and creates a project skill; the target application does not need to use Python.

PM Craft has no planning runtime, package-index dependency, model API client, or MCP server. The host agent provides inference and tools. Check [VALIDATION.md](VALIDATION.md) for the platforms and host behavior actually checked.

## Get version 0.1.0

With Git:

```sh
git clone --branch v0.1.0 https://github.com/ch4570/pm-craft.git
cd pm-craft
```

Or download `pm-craft-0.1.0.zip` and its checksum from [release v0.1.0](https://github.com/ch4570/pm-craft/releases/tag/v0.1.0), extract it, and open `pm-craft-0.1.0/`, which contains `install.py`. The release includes `SHA256SUMS.txt` and a `.zip.sha256` file. Compare the downloaded archive's SHA-256 with the published value before extracting if you need to verify the download.

## Install in a project

Use an existing project path. Quote paths containing spaces.

```sh
python3 install.py --repo /absolute/path/to/project --plan
python3 install.py --repo /absolute/path/to/project
```

`--plan` reports the proposed operation without writing files. Omit it when ready to install. The destination is:

```text
/absolute/path/to/project/.agents/skills/pm-craft/
```

The installer copies the skill and its referenced resources, records managed file hashes, and emits a JSON result on stdout. Errors go to stderr with exit code 2. It does not modify agent instructions, shell configuration, or unrelated skill folders. Installation paths containing symbolic links or junctions are refused; use the real directory path.

On Windows, use a launcher that selects Python 3.11 or newer, for example:

```powershell
py -3 install.py --repo "C:\projects\my-app" --plan
py -3 install.py --repo "C:\projects\my-app"
```

These commands describe the intended installation interface. Executed platform checks are listed in [Validation](VALIDATION.md).

## Choose an exact destination

Use `--dest` instead of `--repo` when the host requires another skill location:

```sh
python3 install.py --dest /absolute/path/to/skills/pm-craft --plan
python3 install.py --dest /absolute/path/to/skills/pm-craft
```

`--dest` is the complete skill directory, including `pm-craft`, not its parent. Choose the discovery path supported by your host. A different destination does not prove that the host has loaded or executed the skill.

## Use it

In hosts that support named skill invocation:

```text
$pm-craft Reduce this plan to a two-week pilot. Keep the core approval
rules, explain what can be handled manually, and preserve the existing PRD.
```

Otherwise provide the path directly:

```text
Read /absolute/path/to/project/.agents/skills/pm-craft/SKILL.md and use it
to review our product plan. Report findings without editing the plan.
```

Start a new agent session or refresh the host's skill discovery when needed. The skill's [openai.yaml](skills/pm-craft/agents/openai.yaml) file supplies Codex-facing metadata; the Markdown instructions remain readable by other agents. Compatibility includes separate questions: can the host discover the folder, load its references, and successfully complete a task? Check each through the host you use.

## Update and keep local changes

Get the new release, then rerun its installer against the same destination. Identical managed files are a no-op; an unedited managed installation can be updated. Conflicting local modifications or different unmanaged files are preserved and reported. Byte-identical files can be adopted into a managed installation. There is no force-overwrite option.

If there is a conflict, review the local and release versions. Preserve your customized folder and install the release into another exact destination for comparison, or back up and remove the old skill folder before installing again. Do not remove other skills or project files to resolve a conflict.

## Copy manually or work offline

You can use a file manager to copy the entire `skills/pm-craft/` directory from the release into your host's skill directory. Keep `SKILL.md`, references, assets, and metadata together; copying only `SKILL.md` leaves its relative references unavailable. Start with an absent destination or merge deliberately to preserve local changes.

The installer and manual copying work from a downloaded bundle without a network connection. Research tasks may still need the host's browsing capability; a skill cannot turn unavailable sources into verified evidence.

Manual copies do not have the installer's ownership record. A later installer can adopt byte-identical files, but a conflicting manual version needs the update procedure above.

## Remove

Delete only the installed `pm-craft` skill directory after preserving any customizations. The installer does not add a runtime, external account, or shell command that needs separate removal. Documents you created using the skill belong to your project and remain there.

## Troubleshooting

| Symptom | Next check |
| --- | --- |
| Python is unavailable | Use Python 3.11+, or copy the complete skill manually |
| Installer rejects a symbolic link or junction | Use the real source and destination directory paths |
| Installer reports a conflict | Inspect the affected local files; use another destination or preserve them before replacing |
| Host cannot find the skill | Check its discovery location and refresh the session, or give it the `SKILL.md` path |
| Reference file cannot be read | Verify the whole folder was copied with relative paths intact |
| Agent cannot research a source | Supply the source or use available host tools; keep the claim unverified until supported |
| Output quality is poor despite installation success | Share a sanitized task and actual output through [Support](SUPPORT.md); installation is not a behavior test |
