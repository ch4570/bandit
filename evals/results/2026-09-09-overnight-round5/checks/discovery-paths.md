# Installed-file fallback paths

A read-only onboarding review found that the fallback instructions always
named the current project's `.agents/skills/` path, even after directing users
to global or custom installation options. That path need not exist after a
successful nondefault installation.

English and Korean onboarding now qualify the project-default example and
direct other installations to the skills directory printed by the installer.
The versioned public command and host-discovery refresh advice are unchanged.

## Synthetic route smoke

An in-process `runCli` smoke used the local package, Node 26.8.1, and separate
temporary projects. Its `cwd`, `home`, and `env` arguments were synthetic; no
real host skill directory was targeted or actual environment variable changed.
The smoke parsed the skills-directory line from normal stdout and checked
both `bandit-scope/SKILL.md` and `bandit-specify/SKILL.md` below that directory.
It also checked the exact five installed folder names, including a custom
general-skill name. All four calls exited 0 without stderr.

The temporary root was `/TEMP/bandit-round5-discovery-x3sg50`; paths below
are relative to that root:

| Mode | Printed skills directory | Both fallback files exist | Current project's default exists |
| --- | --- | --- | --- |
| No option | `project/current-project/.agents/skills` | Yes | Yes |
| `--global` with synthetic `CODEX_HOME` argument | `global/personal-codex/skills` | Yes | No |
| `--repo` pointing to another synthetic project | `repo/another-project/.agents/skills` | Yes | No |
| `--dest` ending in `custom-skills/my-planning` | `dest/custom-skills` | Yes | No |

This checks actual destination output and file presence, not named-command
discovery in every host. It invokes the local CLI function, not GitHub/npx
network retrieval. The route smoke preceded the lock-cleanup fix; destination
selection and printed-root code were unchanged by that fix. The full post-fix
installer and package-consumption suites separately pass.
