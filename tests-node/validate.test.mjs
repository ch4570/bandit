import assert from 'node:assert/strict';
import { mkdtemp, mkdir, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { SKILL_NAMES, validateDistribution } from '../scripts/validate-node.mjs';

async function fixture(t) {
  const root = await mkdtemp(path.join(os.tmpdir(), 'bandit validation '));
  t.after(() => rm(root, { recursive: true, force: true }));
  async function write(relative, text) {
    const filename = path.join(root, relative);
    await mkdir(path.dirname(filename), { recursive: true });
    await writeFile(filename, text);
  }
  const pkg = { name: '@ch4570/bandit', version: '0.2.0', bin: { bandit: 'bin/bandit.mjs' } };
  await write('VERSION', '0.2.0\n');
  await write('package.json', JSON.stringify(pkg));
  await write('bin/bandit.mjs', '#!/usr/bin/env node\n');
  await write('skills/bandit/SKILL.md', '---\nname: bandit\ndescription: >-\n  Plan useful products\n  with evidence and tradeoffs.\n---\n# BANDIT\n[Rules](references/rules.md)\n');
  await write('skills/bandit/references/rules.md', '# Rules\nUse the product context.\n');
  await write('skills/bandit/agents/openai.yaml', 'interface:\n  display_name: "BANDIT"\n  short_description: "Plan useful products with evidence"\n  default_prompt: "Use $bandit to plan my product."\n');
  for (const name of SKILL_NAMES.slice(1)) {
    const display = `BANDIT ${name.slice(7, 8).toUpperCase()}${name.slice(8)}`;
    await write(`skills/${name}/SKILL.md`, `---\nname: ${name}\ndescription: Product planning specialist\n---\n[Rules](references/rules.md)\n`);
    await write(`skills/${name}/references/rules.md`, '# Rules\nUse the product context.\n');
    await write(`skills/${name}/agents/openai.yaml`, `interface:\n  display_name: "${display}"\n  short_description: "Plan useful products with evidence"\n  default_prompt: "Use $${name} to plan my product."\n`);
  }
  return { root, write, pkg, validate: () => validateDistribution(root) };
}

test('Node alone validates the distributable and excludes historical evidence from identity checks', async (t) => {
  const f = await fixture(t);
  await f.write('evals/results/historical.md', '# PM Craft\nHistorical output invokes $pm-craft.\n');
  const report = await f.validate();
  assert.equal(report.ok, true, report.errors.join('\n'));
  assert.equal(report.version, '0.2.0');
  assert.equal(report.skillFiles, 15);
  assert.deepEqual(report.skills.map((skill) => skill.name), SKILL_NAMES);
  assert.match(report.checks, /no claim/u);
});

test('package version and command metadata must match the shipped skill', async (t) => {
  const f = await fixture(t);
  await f.write('package.json', JSON.stringify({ ...f.pkg, version: '9.0.0', bin: { other: 'bin/bandit.mjs' } }));
  const report = await f.validate();
  assert.equal(report.ok, false);
  assert.ok(report.errors.some((error) => error.includes('match VERSION')));
  assert.ok(report.errors.some((error) => error.includes('bandit command')));
});

test('missing references and references outside the skill fail validation', async (t) => {
  const f = await fixture(t);
  await f.write('README.md', '# Outside\n');
  await f.write('skills/bandit/references/rules.md', '[Missing](missing.md)\n[Outside](../../../README.md)\n');
  const report = await f.validate();
  assert.equal(report.ok, false);
  assert.ok(report.errors.some((error) => error.includes('missing local reference')));
  assert.ok(report.errors.some((error) => error.includes('leaves its package')));
});

test('external links and fenced examples are not required local files', async (t) => {
  const f = await fixture(t);
  await f.write('skills/bandit/references/rules.md', '[External](https://example.com/no-file)\n```markdown\n[Example](missing.md)\n```\n~~~markdown\n[Example](also-missing.md)\n~~~\n');
  const report = await f.validate();
  assert.equal(report.ok, true, report.errors.join('\n'));
});

test('duplicate metadata keys cannot silently override the skill identity', async (t) => {
  const f = await fixture(t);
  await f.write('skills/bandit/SKILL.md', '---\nname: wrong\nname: bandit\ndescription: Planning\n---\n');
  const report = await f.validate();
  assert.equal(report.ok, false);
  assert.ok(report.errors.some((error) => error.includes('Duplicate metadata key')));
});

test('UI prompt and icons must point to the current packaged skill', async (t) => {
  const f = await fixture(t);
  await f.write('skills/bandit/agents/openai.yaml', 'interface:\n  display_name: "BANDIT"\n  short_description: "Plan useful products with evidence"\n  default_prompt: "Use $pm-craft to plan my product."\n  icon_small: "../../private.svg"\n');
  const report = await f.validate();
  assert.equal(report.ok, false);
  assert.ok(report.errors.some((error) => error.includes('$bandit')));
  assert.ok(report.errors.some((error) => error.includes('icon_small')));
});

test('source identity and installation lifecycle hooks cannot drift unnoticed', async (t) => {
  const f = await fixture(t);
  await f.write('skills/bandit/references/rules.md', '# PM Craft\n');
  await f.write('package.json', JSON.stringify({ ...f.pkg, scripts: { prepare: 'python3 setup.py' } }));
  const report = await f.validate();
  assert.equal(report.ok, false);
  assert.ok(report.errors.some((error) => error.includes('previous product identity')));
  assert.ok(report.errors.some((error) => error.includes('prepare lifecycle hook')));
});

test('symlinked skill references are rejected before packaging', async (t) => {
  const f = await fixture(t);
  await f.write('outside.md', 'outside contents');
  try {
    await symlink(path.join(f.root, 'outside.md'), path.join(f.root, 'skills/bandit/references/link.md'));
  } catch (error) {
    if (process.platform === 'win32' && ['EPERM', 'EACCES'].includes(error.code)) return t.skip('Windows runner does not permit symlinks');
    throw error;
  }
  const report = await f.validate();
  assert.equal(report.ok, false);
  assert.ok(report.errors.some((error) => error.includes('symlink')));
});

test('missing distribution root produces a structured failure', async (t) => {
  const f = await fixture(t);
  const report = await validateDistribution(path.join(f.root, 'missing'));
  assert.equal(report.ok, false);
  assert.ok(report.errors.length > 0);
});

test('a valid core cannot hide a missing specialist', async (t) => {
  const f = await fixture(t);
  await rm(path.join(f.root, 'skills/bandit-review'), { recursive: true });
  const report = await f.validate();
  assert.equal(report.ok, false);
  assert.ok(report.errors.some((error) => error.includes('bandit-review')));
});

test('specialists must keep their exact metadata and invocation identity', async (t) => {
  const f = await fixture(t);
  await f.write('skills/bandit-specify/SKILL.md', '---\nname: bandit\ndescription: Planning\n---\n');
  await f.write('skills/bandit-specify/agents/openai.yaml', 'interface:\n  display_name: "BANDIT"\n  short_description: "Plan useful products with evidence"\n  default_prompt: "Use $bandit-specify-extra to plan."\n');
  const report = await f.validate();
  assert.equal(report.ok, false);
  assert.ok(report.errors.some((error) => error.includes('name must match the bandit-specify')));
  assert.ok(report.errors.some((error) => error.includes('display_name must be BANDIT Specify')));
  assert.ok(report.errors.some((error) => error.includes('default_prompt must mention $bandit-specify')));
});

test('core invocation does not accept a specialist as its own default prompt', async (t) => {
  const f = await fixture(t);
  await f.write('skills/bandit/agents/openai.yaml', 'interface:\n  display_name: "BANDIT"\n  short_description: "Plan useful products with evidence"\n  default_prompt: "Use $bandit-research to plan."\n');
  const report = await f.validate();
  assert.equal(report.ok, false);
  assert.ok(report.errors.some((error) => error.includes('default_prompt must mention $bandit')));
});

test('specialists cannot depend on a sibling skill even when that file exists', async (t) => {
  const f = await fixture(t);
  await f.write('skills/bandit-review/references/rules.md', '[Core rules](../../bandit/references/rules.md)\n');
  const report = await f.validate();
  assert.equal(report.ok, false);
  assert.ok(report.errors.some((error) => error.includes('bandit-review') && error.includes('leaves its package')));
});

test('retired commands cannot remain in the packaged skill tree', async (t) => {
  const f = await fixture(t);
  for (const name of ['bandit-decide', 'bandit-update']) await f.write(`skills/${name}/SKILL.md`, '# Obsolete command\n');
  const report = await f.validate();
  assert.equal(report.ok, false);
  assert.ok(report.errors.some((error) => error.includes('Unexpected packaged skill: bandit-decide')));
  assert.ok(report.errors.some((error) => error.includes('Unexpected packaged skill: bandit-update')));
});

test('unknown skills cannot bypass the canonical package inventory', async (t) => {
  const f = await fixture(t);
  await f.write('skills/bandit-unknown/SKILL.md', '# Unexpected command\n');
  const report = await f.validate();
  assert.equal(report.ok, false);
  assert.ok(report.errors.some((error) => error.includes('Unexpected packaged skill: bandit-unknown')));
});
