# Install BANDIT

[Overview](README.md) · [한국어](README.ko.md) · [Usage](docs/usage.md)

## One command

Open your project folder and run:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.2.0/bandit.tgz
```

Requires **Node.js 22+ and npm**. The command downloads BANDIT 0.2.0 from GitHub and installs the complete skill into the current project's `.agents/skills/bandit/`. No Git, clone, Python, package configuration, or API key is needed.

Then ask your agent:

```text
$bandit Turn this idea into a two-week MVP plan. Recommend the scope,
explain the trade-offs, and use our existing planning document.
```

The npm registry package is **not published yet**. Use the GitHub command above; `npx @ch4570/bandit` is reserved for a future registry release.

## Release archives

The command above pins both the installer and skill to **0.2.0**. Release archives and checksums are available on [v0.2.0](https://github.com/ch4570/bandit/releases/tag/v0.2.0). `bandit.tgz` and `ch4570-bandit-0.2.0.tgz` on that release contain the same package.

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
| None | Current project: `.agents/skills/bandit/` |
| `--global` | `$CODEX_HOME/skills/bandit/`, or `~/.codex/skills/bandit/` when `CODEX_HOME` is unset |
| `--repo /path/to/project` | Another project's `.agents/skills/bandit/` |
| `--dest /path/to/skills/bandit` | The exact skill directory supplied |

Choose only one destination option. Quote paths containing spaces. `--dest` includes the final `bandit` directory, not just its parent. Use the discovery location supported by your host.

To see the changes before installing:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.2.0/bandit.tgz --plan
```

For script-friendly output, add `--json`; it emits a JSON result on stdout, including errors. Normal errors use stderr. Errors exit with status 2. `--help` lists options and `--version` shows the installer version. The explicit `install` subcommand is optional; the short command already performs installation.

The same npx commands work in a terminal or PowerShell. [Validation](VALIDATION.md) records the platforms and commands actually tested.

## If the agent cannot find BANDIT

Start a new agent session or refresh the host's skill discovery. In hosts that support named skills, use `$bandit`. Otherwise point to the installed file:

```text
Read .agents/skills/bandit/SKILL.md and apply it to review our PRD.
Report the gaps and proposed fixes without editing the original.
```

The [Codex metadata](skills/bandit/agents/openai.yaml) supplies the display name and default prompt. Other agents can read the Markdown skill and its references. Discovery, reference loading, and task execution are separate behaviors; check them in the host you use.

BANDIT contains instructions and an installer. The agent supplies its model, filesystem access, and any live research tools under its existing permissions and usage costs.

## Updates and local changes

To update, copy the installation command from the [current README](https://github.com/ch4570/bandit#saddle-up), which names the current release version. Run it against the same project, or include the same `--global` or destination option you used before. Repeating a fixed-version command keeps that version.

The installer recognizes its managed files, leaves identical files alone, and checks for local conflicts before changing anything. It preserves unrelated files and reports conflicting customizations instead of overwriting them. There is no force-overwrite option.

The optional `releases/latest/download/bandit.tgz` URL can be used for a first installation, but npm may keep executing its earlier cached package when that URL changes. `--prefer-online` did not resolve this in our check. Use a versioned release URL for updates.

If a local edit conflicts, keep a copy of your customized skill. Install the new release into another `--dest` for comparison, or deliberately remove the old skill folder after preserving your changes. Do not delete other skills or project files.

If you previously installed **PM Craft 0.1.0**, BANDIT uses a new folder and invocation: `bandit` and `$bandit`. The installer reports a sibling `pm-craft` folder and leaves it untouched. Keep the old folder while reviewing any customizations; remove only the old `pm-craft` skill folder when you are ready. Renaming the repository does not update an installed copy automatically.

## Optional global command

If you prefer to keep the installer command on your PATH:

```sh
npm install -g github:ch4570/bandit
bandit
```

Run `bandit` in each project that should receive the skill. `npm install -g` installs the **CLI**; `bandit --global` installs the **skill for Codex across projects**. These are separate choices. The default npx command requires neither a permanent CLI installation nor global npm write access. This optional GitHub shorthand route requires Git.

## Manual copy and removal

You can also copy the entire `skills/bandit/` directory from the repository into the discovery directory your agent supports. Keep `SKILL.md`, references, assets, and metadata together. Manual copying can work offline once you have the files; live research still needs the host's tools.

To remove the skill, delete only the installed `bandit` skill directory after preserving any customizations. Your planning documents remain in your project. If you also installed the optional global CLI, remove it with `npm uninstall -g @ch4570/bandit`.

## Troubleshooting

| Symptom | Try this |
| --- | --- |
| `npx` is unavailable or Node is too old | Install Node.js 22 or newer, which includes npm |
| GitHub shorthand cannot find Git | Use the [default release archive command](#one-command) |
| `npx @ch4570/bandit` cannot find a package | Use `npx --yes https://github.com/ch4570/bandit/releases/download/v0.2.0/bandit.tgz`; registry publication is deferred |
| Rerunning an old command keeps an old version | Copy the versioned command from the current README |
| Installer reports a conflicting file | Preserve the customization and compare in a separate destination |
| Installer rejects a linked path | Use the real directory path shown by your filesystem |
| Agent cannot load a reference | Check that the entire skill folder was copied |
| Installation works but the plan is poor | Share a small sanitized task and actual output through [Support](SUPPORT.md) |
