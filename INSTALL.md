# Install BANDIT

[Overview](README.md) · [한국어](README.ko.md) · [Usage](docs/usage.md)

## One command

Open your project folder and run:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.4.0/bandit.tgz
```

Requires **Node.js 22+ and npm**. This installs all five skills into the current project's `.agents/skills/`. Git, cloning, Python, package configuration, and API keys are unnecessary.

Then ask your agent:

```text
$bandit-scope Set the MVP scope for this idea. We have one developer and
two weeks. Recommend what to include, defer, and handle manually.
```

| Command | Task | Installed folder |
| --- | --- | --- |
| `$bandit-research` | Research evidence and experiments | `.agents/skills/bandit-research/` |
| `$bandit-scope` | Set MVP scope and priorities | `.agents/skills/bandit-scope/` |
| `$bandit-specify` | Create or rewrite a product spec | `.agents/skills/bandit-specify/` |
| `$bandit-review` | Review an existing plan | `.agents/skills/bandit-review/` |
| `$bandit` | Combine planning tasks | `.agents/skills/bandit/` |

[Commands and examples](README.md#skill-commands-and-usage) explain each task. **The npm registry package is not published yet.** Use the GitHub archive command above; `npx @ch4570/bandit` is reserved for a future registry release.

## Choose where to install

The default is your current project. Append an option to the same install command:

| Option | Destination |
| --- | --- |
| None | All five folders under the current project's `.agents/skills/` |
| `--global` | All five under `$CODEX_HOME/skills/`, or `~/.codex/skills/` when `CODEX_HOME` is unset |
| `--repo /path/to/project` | All five under that project's `.agents/skills/` |
| `--dest /path/to/skills/bandit` | General `bandit` skill at this exact path; the four specialists beside it |

Choose one destination option. Quote paths containing spaces. `--dest` names the exact general-skill directory, including its final folder. A custom name is allowed, but it cannot match an active or retired specialist's name. The other four folders use their standard names in the same parent directory.

For personal Codex use across projects:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.4.0/bandit.tgz --global
```

To preview the installation and any migration without changing the skill folders:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.4.0/bandit.tgz --plan
```

Add `--json` for machine-readable results, including errors, on stdout. Normal errors use stderr; errors exit with status 2. `--help` lists options and `--version` shows the installer version. The explicit `install` subcommand is optional.

## Upgrade from 0.2 or 0.3

Run the **0.4.0 command above** against the same project. Include the same `--global` or custom destination option if applicable, then start a new agent session.

- **From 0.2:** the installer updates the general skill and adds the four current specialists.
- **From 0.3:** use `$bandit-scope` for the work previously handled by `$bandit-decide`. Use `$bandit-specify` for both new specs and the changes previously handled by `$bandit-update`.

The installer automatically removes unchanged, managed files and ownership records from the retired `bandit-decide` and `bandit-update` installations. Unrelated notes remain; a folder containing those notes can remain after its skill is retired. Files you already deleted from a retired installation are not restored.

If a retired skill has modified managed files, an invalid ownership record, or an unmanaged `SKILL.md`, the whole upgrade stops before changing the skills. Preserve your customizations and move the conflicting old skill outside the host's discovery directory, then rerun the command. A folder containing only unrelated notes does not block migration.

The old installer stays on its old version. Repeating a 0.2 or 0.3 command cannot install the current command set.

## Updates and local changes

For a future version, copy the install command from the [current README](https://github.com/ch4570/bandit#saddle-up) and use the same destination. Then refresh skill discovery or start a new agent session so the host loads the updated skills. The versioned URL ensures npm can distinguish the new release from an earlier cached package.

The installer checks the current and retired skill destinations before applying changes. Identical managed files stay untouched. Conflicting edits are reported and preserved; there is no force-overwrite option. To compare versions, choose a `--dest` under a separate parent directory so all specialist folders are separate too.

The optional `releases/latest/download/bandit.tgz` URL can work for a first installation, but npm may keep executing its earlier cached package when that URL changes. `--prefer-online` did not resolve this in our check. Use a versioned release URL for updates.

An older **PM Craft 0.1.0** folder is reported and left untouched. Preserve any customizations before removing that old folder yourself.

## If the agent cannot find a command

Start a new agent session or refresh its skill discovery. In hosts supporting named skills, use a command such as `$bandit-specify`. Otherwise point to that skill's installed `SKILL.md`. For the default project installation:

```text
Read .agents/skills/bandit-specify/SKILL.md and use it to rewrite our PRD
for the new direction described below.
```

For `--global`, `--repo`, or `--dest`, use `bandit-specify/SKILL.md` under the skills directory printed by the installer instead of assuming the current project's `.agents/skills/`.

Each skill includes its own Markdown instructions, references, and Codex metadata. Your host supplies the model, file access, and research tools under its existing permissions and usage costs. [Validation](VALIDATION.md) records what has actually been checked.

## Release archives and other install methods

The command above pins the installer and all five skills to **0.4.0**. [Release v0.4.0](https://github.com/ch4570/bandit/releases/tag/v0.4.0) provides `bandit.tgz`, the identical `ch4570-bandit-0.4.0.tgz`, and checksums.

If Git is installed, the shorter command follows the repository's default branch:

```sh
npx --yes github:ch4570/bandit
```

That branch can differ from the current release. To keep the installer on your PATH instead, use `npm install -g github:ch4570/bandit`, then run `bandit` in your project. Installing the global CLI and installing the skills with `bandit --global` are separate choices.

For manual or offline installation, copy the complete skill folders from `skills/` into the discovery directory supported by your host. Each folder is self-contained; keep its instructions, references, assets, and metadata together. Manual copies do not automatically migrate old installations.

## Remove

Preserve your customizations, then delete only the five installed folders named in the command table. With a custom `--dest`, use the exact general-skill folder you chose. Keep any retained notes from retired skills. Planning documents remain in your project.

If you also installed the optional global CLI, remove it with `npm uninstall -g @ch4570/bandit`.

## Troubleshooting

| Symptom | Try this |
| --- | --- |
| `npx` is unavailable or Node is too old | Install Node.js 22 or newer, which includes npm |
| GitHub shorthand cannot find Git | Use the versioned archive command at the top |
| Registry package cannot be found | Use the GitHub archive command; registry publication is deferred |
| Old commands still appear | Run the 0.4.0 installer, then refresh or restart your agent session |
| Upgrade reports a retired-skill conflict | Preserve the old customized skill and move it outside discovery before retrying |
| Installer rejects a linked path | Use the real directory path |
| A reference cannot be loaded | Check that the complete skill folder was copied |
| Installation works but the plan is poor | Share a sanitized task and actual output through [Support](SUPPORT.md) |
