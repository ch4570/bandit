// Benign after-fix reproduction in a new scratch directory; retain all output separately.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';

const evidence = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(evidence, '../../../..');
const cli = path.join(repo, 'bin/bandit.mjs');
const hash = (bytes) => createHash('sha256').update(bytes).digest('hex');
const sourceHash = hash(fs.readFileSync(path.join(repo, 'lib/installer.mjs')));
const beforeSourceHash = hash(fs.readFileSync(path.join(evidence, 'installer-before.mjs')));
assert.notEqual(sourceHash, beforeSourceHash);
assert.equal(hash(fs.readFileSync(path.join(repo, 'tests-node/install.test.mjs'))), '4a2259d68f57107f270efec164304115f226f98a127cc006878d2220cf2f4a46');
assert.equal(process.versions.node, '22.23.2');
const scratch = fs.mkdtempSync(path.join(fs.realpathSync(os.tmpdir()), 'bandit-round11-legacy-after-'));
const started = new Date().toISOString();
let serial = 0;
const commands = [];
const observations = [];
const inventory = (root) => {
  if (!fs.existsSync(root)) return null;
  return fs.readdirSync(root, { recursive: true }).sort().map((relative) => {
    const target = path.join(root, relative);
    const stat = fs.lstatSync(target);
    return stat.isDirectory() ? { path: relative, type: 'directory' }
      : { path: relative, type: 'file', bytes: stat.size, sha256: hash(fs.readFileSync(target)) };
  });
};
function run(label, cwd, args) {
  const commandStarted = new Date().toISOString();
  const result = spawnSync(process.execPath, [cli, ...args], {
    cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'], shell: false,
  });
  const stem = `after-${String(++serial).padStart(2, '0')}-${label}`;
  for (const stream of ['stdout', 'stderr']) {
    fs.writeFileSync(path.join(evidence, `${stem}.${stream}.txt`), result[stream] ?? '', { flag: 'wx' });
  }
  commands.push({
    label, argv: [process.execPath, cli, ...args], cwd, stdin: 'closed', shell: false,
    started_at: commandStarted, ended_at: new Date().toISOString(), exit_code: result.status,
    signal: result.signal, error: result.error?.message ?? null,
    stdout: `${stem}.stdout.txt`, stderr: `${stem}.stderr.txt`,
  });
  assert.equal(result.error, undefined);
  assert.equal(result.status, 0);
  assert.equal(result.stderr, '');
  return args.includes('--json') ? JSON.parse(result.stdout) : result.stdout;
}
const fixture = (name) => {
  const project = path.join(scratch, name, 'project');
  const skills = path.join(scratch, name, 'skills');
  fs.mkdirSync(project, { recursive: true });
  return { project, skills };
};
for (const [label, coreName] of [['lowercase', 'pm-craft'], ['mixed-case', 'PM-Craft']]) {
  const { project, skills } = fixture(label);
  const destination = path.join(skills, coreName);
  const before = inventory(skills);
  const previewBefore = run(`${label}-plan-before`, project, ['--dest', destination, '--plan', '--json']);
  assert.deepEqual(inventory(skills), before);
  const installed = run(`${label}-install`, project, ['--dest', destination, '--json']);
  const installedInventory = inventory(skills);
  const repeated = run(`${label}-repeat`, project, ['--dest', destination, '--json']);
  assert.deepEqual(inventory(skills), installedInventory);
  const previewAfter = run(`${label}-plan-after`, project, ['--dest', destination, '--plan', '--json']);
  assert.deepEqual(inventory(skills), installedInventory);
  const textRepeated = run(`${label}-text-repeat`, project, ['--dest', destination]);
  assert.deepEqual(inventory(skills), installedInventory);
  for (const report of [previewBefore, installed, repeated, previewAfter]) assert.equal(report.notes, undefined);
  assert.doesNotMatch(textRepeated, /A separate pm-craft/);
  const marker = JSON.parse(fs.readFileSync(path.join(destination, '.bandit-install.json'), 'utf8'));
  assert.equal(marker.name, 'bandit');
  observations.push({ label, core_name: coreName, destination, before_inventory: before,
    installed_inventory: installedInventory, marker,
    reports: { plan_before: previewBefore, install: installed, repeat: repeated, plan_after: previewAfter },
    normal_repeat_stdout: textRepeated,
    legacy_path_resolves_to_core: fs.realpathSync(path.join(skills, 'pm-craft')) === fs.realpathSync(destination),
  });
}
{
  const { project, skills } = fixture('genuine-sibling');
  const legacy = path.join(skills, 'pm-craft');
  fs.mkdirSync(legacy, { recursive: true });
  fs.writeFileSync(path.join(legacy, 'SKILL.md'), 'Synthetic pre-existing PM Craft note. Preserve these bytes.\n', { flag: 'wx' });
  const before = inventory(legacy);
  const destination = path.join(skills, 'core-planner');
  const preview = run('genuine-sibling-plan', project, ['--dest', destination, '--plan', '--json']);
  const installed = run('genuine-sibling-install', project, ['--dest', destination, '--json']);
  assert.deepEqual(inventory(legacy), before);
  assert.match(preview.notes[0], /separate pm-craft/);
  assert.match(installed.notes[0], /separate pm-craft/);
  observations.push({ label: 'genuine-sibling', destination, legacy_before_inventory: before,
    legacy_after_inventory: inventory(legacy), reports: { plan: preview, install: installed },
    installed_inventory: inventory(skills),
  });
}
assert.equal(hash(fs.readFileSync(path.join(repo, 'lib/installer.mjs'))), sourceHash);
const result = { started_at: started, ended_at: new Date().toISOString(), scratch, repo,
  runtime: { executable: process.execPath, version: process.version, platform: process.platform, arch: process.arch },
  pre_fix_installer_sha256: beforeSourceHash,
  source_installer_sha256_before: sourceHash, source_installer_sha256_after: sourceHash,
  scope: 'Direct local Node CLI only; explicit scratch destinations; closed stdin; no network, host skill writes, fault injection, or cleanup.',
  commands, observations,
};
fs.writeFileSync(path.join(evidence, 'legacy-note-after-results.json'), `${JSON.stringify(result, null, 2)}\n`, { flag: 'wx' });
process.stdout.write(`${JSON.stringify({ scratch, commands: commands.length, exit_codes: commands.map((item) => item.exit_code),
  observed_notes: observations.map((item) => ({ label: item.label, stages: Object.fromEntries(Object.entries(item.reports).map(([stage, report]) => [stage, report.notes ?? null])) })) }, null, 2)}\n`);
