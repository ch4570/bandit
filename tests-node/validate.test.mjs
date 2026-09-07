import assert from 'node:assert/strict';
import { mkdtemp, mkdir, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { validateDistribution } from '../scripts/validate-node.mjs';

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
  return { root, write, pkg, validate: () => validateDistribution(root) };
}

test('Node alone validates the distributable and excludes historical evidence from identity checks', async (t) => {
  const f = await fixture(t);
  await f.write('evals/results/historical.md', '# PM Craft\nHistorical output invokes $pm-craft.\n');
  const report = await f.validate();
  assert.equal(report.ok, true, report.errors.join('\n'));
  assert.equal(report.version, '0.2.0');
  assert.equal(report.skillFiles, 3);
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
