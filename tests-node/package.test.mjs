import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';
import { SKILL_NAMES, RETIRED_NAMES } from '../lib/installer.mjs';

const repository = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

function npm(args, options) {
  const cli = process.env.npm_execpath;
  if (cli) return execFileSync(process.execPath, [cli, ...args], { encoding: 'utf8', ...options });
  return execFileSync(process.platform === 'win32' ? 'npm.cmd' : 'npm', args,
    { encoding: 'utf8', shell: process.platform === 'win32', ...options });
}

test('the npm artifact is complete and its extracted CLI works without the checkout', { timeout: 60000 }, (t) => {
  const temporary = fs.mkdtempSync(path.join(fs.realpathSync(os.tmpdir()), 'bandit-pack-'));
  t.after(() => fs.rmSync(temporary, { recursive: true, force: true }));
  const packed = JSON.parse(npm(['pack', '--ignore-scripts', '--json', '--pack-destination', temporary], { cwd: repository }))[0];
  assert.equal(packed.filename, 'ch4570-bandit-0.4.0.tgz');
  const entries = new Set(packed.files.map((file) => file.path));
  for (const required of ['package.json', 'bin/bandit.mjs', 'lib/installer.mjs', 'scripts/validate-node.mjs', 'VERSION', 'LICENSE', 'skills/bandit/SKILL.md', 'skills/bandit/agents/openai.yaml']) {
    assert.ok(entries.has(required), `Missing packed file: ${required}`);
  }
  const skillFiles = new Map();
  for (const name of SKILL_NAMES) {
    const skillRoot = path.join(repository, 'skills', name);
    const files = fs.readdirSync(skillRoot, { recursive: true }).filter((file) => fs.statSync(path.join(skillRoot, file)).isFile());
    assert.ok(files.includes('SKILL.md'), `Missing independent skill: ${name}`);
    skillFiles.set(name, files);
    for (const file of files) assert.ok(entries.has(`skills/${name}/${file.split(path.sep).join('/')}`), `Skill asset omitted: ${name}/${file}`);
  }
  for (const name of entries) assert.ok(!/^(?:tests(?:-node)?\/|evals\/|install\.py|\.git\/)/.test(name), `Unneeded payload: ${name}`);
  for (const name of RETIRED_NAMES) assert.ok(![...entries].some((entry) => entry.startsWith(`skills/${name}/`)), `Retired skill must not ship: ${name}`);

  const archive = path.join(temporary, packed.filename);
  const isolated = path.join(temporary, 'isolated');
  fs.mkdirSync(isolated);
  npm(['install', '--offline', '--ignore-scripts', '--no-audit', '--no-fund', '--prefix', isolated, archive], { cwd: isolated });
  const installedPackage = path.join(isolated, 'node_modules', '@ch4570', 'bandit');
  const manifest = JSON.parse(fs.readFileSync(path.join(installedPackage, 'package.json')));
  assert.equal(manifest.engines.node, '>=22');
  assert.equal(manifest.bin.bandit, 'bin/bandit.mjs');
  assert.equal(Object.keys(manifest.dependencies ?? {}).length, 0);
  for (const hook of ['preinstall', 'install', 'postinstall', 'prepare', 'prepublish', 'prepublishOnly']) assert.equal(manifest.scripts?.[hook], undefined);
  assert.equal(fs.existsSync(path.join(isolated, '.agents')), false, 'npm install must not install a skill as a lifecycle side effect');
  const project = path.join(temporary, 'project');
  fs.mkdirSync(project);
  const beforePackageJson = '{"name":"unrelated-project"}\n';
  fs.writeFileSync(path.join(project, 'package.json'), beforePackageJson);
  const report = JSON.parse(execFileSync(process.execPath, [path.join(installedPackage, 'bin', 'bandit.mjs'), '--json'], { cwd: project, encoding: 'utf8' }));
  assert.equal(report.status, 'installed');
  assert.equal(report.destination, path.join(project, '.agents', 'skills', 'bandit'));
  assert.equal(report.skills.length, 5);
  assert.deepEqual(report.commands, SKILL_NAMES.map((name) => `$${name}`));
  assert.deepEqual(fs.readdirSync(report.destination_root).sort(), [...SKILL_NAMES].sort());
  for (const [name, files] of skillFiles) {
    const destination = report.skills.find((skill) => skill.name === name).destination;
    for (const file of files) assert.deepEqual(fs.readFileSync(path.join(destination, file)), fs.readFileSync(path.join(installedPackage, 'skills', name, file)));
    assert.match(fs.readFileSync(path.join(destination, 'SKILL.md'), 'utf8'), new RegExp(`name: ${name}\\r?\\n`));
    assert.ok(fs.readFileSync(path.join(destination, 'agents', 'openai.yaml'), 'utf8').includes(`$${name}`));
  }
  assert.equal(fs.readFileSync(path.join(project, 'package.json'), 'utf8'), beforePackageJson);
  assert.equal(fs.existsSync(path.join(project, 'node_modules')), false);
  assert.equal(fs.existsSync(path.join(project, 'package-lock.json')), false);

  const npxProject = path.join(temporary, 'npx-project');
  fs.mkdirSync(npxProject);
  const npxReport = JSON.parse(npm(['exec', '--offline', '--yes', '--cache', path.join(temporary, 'npm-cache'), `--package=${archive}`, '--', 'bandit', '--json'], { cwd: npxProject }));
  assert.equal(npxReport.status, 'installed');
  assert.equal(npxReport.destination, path.join(npxProject, '.agents', 'skills', 'bandit'));
  assert.equal(npxReport.skills.length, 5);
  for (const name of SKILL_NAMES) assert.equal(fs.existsSync(path.join(npxReport.destination_root, name, 'SKILL.md')), true);
  assert.equal(fs.existsSync(path.join(npxProject, 'package.json')), false);
  assert.equal(fs.existsSync(path.join(npxProject, 'node_modules')), false);
});
