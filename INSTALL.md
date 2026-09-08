# Install BANDIT

[Overview](README.md) · [한국어](README.ko.md) · [Usage](docs/usage.md)

## One command

Open your project folder and run:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.3.0/bandit.tgz
```

Requires **Node.js 22+ and npm**. The command downloads BANDIT 0.3.0 from GitHub and installs all six skills into the current project's `.agents/skills/`. No Git, clone, Python, package configuration, or API key is needed.

Then ask your agent:

```text
$bandit-decide Turn this idea into a two-week MVP plan. Recommend the scope,
explain the trade-offs, and use our existing planning document.
```

The installation adds these commands:

| Command | Installed folder |
| --- | --- |
| `$bandit-research` | `.agents/skills/bandit-research/` |
| `$bandit-decide` | `.agents/skills/bandit-decide/` |
| `$bandit-specify` | `.agents/skills/bandit-specify/` |
| `$bandit-review` | `.agents/skills/bandit-review/` |
| `$bandit-update` | `.agents/skills/bandit-update/` |
| `$bandit` | `.agents/skills/bandit/` |

The five specialists handle their named tasks directly. Use `$bandit` for a combined planning request. [Commands and examples](README.md#skill-commands-and-usage).

The npm registry package is **not published yet**. Use the GitHub command above; `npx @ch4570/bandit` is reserved for a future registry release.

## Release archives

The command above pins the installer and all six skills to **0.3.0**. Release archives and checksums are available on [v0.3.0](https://github.com/ch4570/bandit/releases/tag/v0.3.0). `bandit.tgz` and `ch4570-bandit-0.3.0.tgz` on that release contain the same package.

A checksum verifies that a downloaded archive matches the published file; it does not assess the quality of the skill's output.

## Short GitHub command

If Git is already installed, the shorter command also works:

```sh
npx --yes github:ch4570/bandit
```

This follows the repository's default branch, which can differ from the latest release. The archive command above is the default route for published releases.

## Choose where to install

The default is your current project. Append an option to the same install command:

| Option | Destination |
| --- | --- |
| None | All six skill folders under the current project's `.agents/skills/` |
| `--global` | All six under `$CODEX_HOME/skills/`, or `~/.codex/skills/` when `CODEX_HOME` is unset |
| `--repo /path/to/project` | All six under that project's `.agents/skills/` |
| `--dest /path/to/skills/bandit` | General `bandit` skill at this exact path; the five specialists beside it |

Choose only one destination option. Quote paths containing spaces. `--dest` is the exact directory for the general `bandit` skill. The installer puts `bandit-research`, `bandit-decide`, `bandit-specify`, `bandit-review`, and `bandit-update` in the same parent directory. A custom name is allowed for the general directory, but it cannot collide with a specialist's name. Use the discovery location supported by your host.

To see the changes before installing:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.3.0/bandit.tgz --plan
```

For script-friendly output, add `--json`; it emits a JSON result on stdout, including errors. Normal errors use stderr. Errors exit with status 2. `--help` lists options and `--version` shows the installer version. The explicit `install` subcommand is optional; the short command already performs installation.

The same npx commands work in a terminal or PowerShell. [Validation](VALIDATION.md) records the platforms and commands actually tested.

## If the agent cannot find BANDIT

Start a new agent session or refresh the host's skill discovery. In hosts that support named skills, use the command for the task, such as `$bandit-review`. Otherwise point to that skill's installed file:

```text
Read .agents/skills/bandit-review/SKILL.md and apply it to review our PRD.
Report the gaps and proposed fixes without editing the original.
```

Each skill includes Codex metadata, Markdown instructions, and its own references. Other agents can read those instructions directly. Discovery, reference loading, and task execution are separate behaviors; check them in the host you use.

BANDIT contains instructions and an installer. The agent supplies its model, filesystem access, and any live research tools under its existing permissions and usage costs.

## Upgrade from 0.2.0

Run the **0.3.0 command above** against the same project. It updates the general `bandit` skill and adds all five specialist folders. Include the same `--global` or custom destination option if that is how you installed before. Start a new agent session so it can discover the new commands.

The old 0.2.0 installer contains only the general skill; repeating its old command cannot add the specialists.

## Updates and local changes

To update, copy the installation command from the [current README](https://github.com/ch4570/bandit#saddle-up), which names the current release version. Run it against the same project, or include the same `--global` or destination option you used before. Repeating a fixed-version command keeps that version.

The installer recognizes its managed files, leaves identical files alone, and checks all six destinations for local conflicts before changing anything. It preserves unrelated files and reports conflicting customizations instead of overwriting them. There is no force-overwrite option.

The optional `releases/latest/download/bandit.tgz` URL can be used for a first installation, but npm may keep executing its earlier cached package when that URL changes. `--prefer-online` did not resolve this in our check. Use a versioned release URL for updates.

If a local edit conflicts, keep a copy of your customized skill. Install the new release with `--dest` under a separate parent directory for comparison, or deliberately remove the old skill folder after preserving your changes. Do not delete other skills or project files.

If you previously installed **PM Craft 0.1.0**, BANDIT uses the six new folders and commands listed above. The installer reports a sibling `pm-craft` folder and leaves it untouched. Keep the old folder while reviewing any customizations; remove only the old `pm-craft` skill folder when you are ready. Renaming the repository does not update an installed copy automatically.

## Optional global command

If you prefer to keep the installer command on your PATH:

```sh
npm install -g github:ch4570/bandit
bandit
```

Run `bandit` in each project that should receive all six skills. `npm install -g` installs the **CLI**; `bandit --global` installs **all six skills for Codex across projects**. These are separate choices. The default npx command requires neither a permanent CLI installation nor global npm write access. This optional GitHub shorthand route requires Git.

## Manual copy and removal

You can also copy any of the six complete skill folders from the repository's `skills/` directory into the discovery directory your agent supports. Each is self-contained. Keep its `SKILL.md`, references, assets, and metadata together. Manual copying can work offline once you have the files; live research still needs the host's tools.

To remove the full set, preserve your customizations and delete only the six installed folders named in the command table above. With a custom `--dest`, use the exact general skill folder you chose. Your planning documents remain in your project. If you also installed the optional global CLI, remove it with `npm uninstall -g @ch4570/bandit`.

## Troubleshooting

| Symptom | Try this |
| --- | --- |
| `npx` is unavailable or Node is too old | Install Node.js 22 or newer, which includes npm |
| GitHub shorthand cannot find Git | Use the [default release archive command](#one-command) |
| `npx @ch4570/bandit` cannot find a package | Use `npx --yes https://github.com/ch4570/bandit/releases/download/v0.3.0/bandit.tgz`; registry publication is deferred |
| Rerunning an old command keeps an old version | Copy the versioned command from the current README |
| Installer reports a conflicting file | Preserve the customization and compare in a separate destination |
| Installer rejects a linked path | Use the real directory path shown by your filesystem |
| Only `$bandit` appears after a 0.2.0 installation | Run the 0.3.0 command, then refresh or restart the agent session |
| Agent cannot load a reference | Check that the entire skill folder was copied |
| Installation works but the plan is poor | Share a small sanitized task and actual output through [Support](SUPPORT.md) |
