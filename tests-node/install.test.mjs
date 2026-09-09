import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { installInto, installBundle, makePlan, runCli, MARKER, SKILL_NAMES, RETIRED_NAMES } from '../lib/installer.mjs';

function fixture(t) {
  const root = fs.mkdtempSync(path.join(fs.realpathSync(os.tmpdir()), 'bandit-test-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  const source = path.join(root, 'package');
  const project = path.join(root, 'project');
  const skill = path.join(source, 'skills', 'bandit');
  const dest = path.join(project, '.agents', 'skills', 'bandit');
  fs.mkdirSync(skill, { recursive: true });
  fs.mkdirSync(project);
  put(source, 'package.json', JSON.stringify({ name: '@ch4570/bandit', version: '0.4.0' }));
  for (const name of SKILL_NAMES) {
    const folder = path.join(source, 'skills', name);
    put(folder, 'SKILL.md', `---\nname: ${name}\ndescription: Make an actionable product plan.\n---\n# BANDIT\n`);
    put(folder, 'references/research.md', 'Follow the evidence.\n');
    put(folder, 'assets/portrait.png', Buffer.from([0, 255, 42, 12]));
  }
  return { root, source, project, skill, dest };
}

function put(root, name, bytes) {
  const target = path.join(root, name);
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.writeFileSync(target, bytes);
}

function snapshot(root) {
  if (!fs.existsSync(root)) return null;
  return Object.fromEntries(fs.readdirSync(root, { recursive: true }).sort().map((name) => {
    const file = path.join(root, name);
    return [name, fs.lstatSync(file).isFile() ? fs.readFileSync(file).toString('base64') : '<directory>'];
  }));
}

// Keep fault-injection boundaries independent of pathname versus descriptor writes.
function afterWrites(callback, run) {
  const open = fs.openSync, write = fs.writeFileSync;
  const descriptors = new Map();
  fs.openSync = (file, ...args) => {
    const descriptor = open(file, ...args);
    descriptors.set(descriptor, file);
    return descriptor;
  };
  fs.writeFileSync = (file, data, ...args) => {
    const result = write(file, data, ...args);
    callback(typeof file === 'number' ? descriptors.get(file) : file, data, write);
    return result;
  };
  try { return run(); }
  finally { fs.openSync = open; fs.writeFileSync = write; }
}

function cli(args, f, options = {}) {
  let stdout = '', stderr = '';
  const code = runCli(args, { packageRoot: f.source, cwd: f.project, env: {}, home: path.join(f.root, 'home'),
    stdout: { write: (text) => { stdout += text; } }, stderr: { write: (text) => { stderr += text; } }, ...options });
  return { code, stdout, stderr };
}

function oldInstallation(f) {
  const oldNames = ['bandit', 'bandit-research', 'bandit-decide', 'bandit-specify', 'bandit-review', 'bandit-update'];
  for (const name of oldNames) {
    const destination = path.join(path.dirname(f.dest), name);
    const files = {
      'SKILL.md': `---\nname: ${name}\ndescription: The original 0.3 skill.\n---\nOriginal instructions.\n`,
      'references/old.md': 'Original reference.\n',
      'agents/openai.yaml': `interface:\n  default_prompt: "Use $${name}."\n`,
    };
    for (const [file, bytes] of Object.entries(files)) put(destination, file, bytes);
    put(destination, MARKER, JSON.stringify({ format: 1, name, version: '0.3.0',
      files: Object.fromEntries(Object.entries(files).map(([file, bytes]) => [file, createHash('sha256').update(bytes).digest('hex')])) }));
  }
}

test('no-argument CLI installs five discoverable skills and preserves project files', (t) => {
  const f = fixture(t);
  const original = '{"name":"users-app","scripts":{"test":"custom"}}\n';
  put(f.project, 'package.json', original);
  const result = cli([], f);
  assert.equal(result.code, 0);
  assert.match(result.stdout, /BANDIT is ready/);
  assert.match(result.stdout, /\$bandit/);
  assert.equal(result.stderr, '');
  assert.deepEqual(fs.readdirSync(path.dirname(f.dest)).sort(), [...SKILL_NAMES].sort());
  for (const name of SKILL_NAMES) {
    const folder = path.join(path.dirname(f.dest), name);
    assert.match(fs.readFileSync(path.join(folder, 'SKILL.md'), 'utf8'), new RegExp(`name: ${name}\\n`));
    assert.equal(JSON.parse(fs.readFileSync(path.join(folder, MARKER))).name, name);
    assert.ok(result.stdout.includes(`$${name}`));
  }
  assert.deepEqual(fs.readFileSync(path.join(f.dest, 'assets/portrait.png')), Buffer.from([0, 255, 42, 12]));
  assert.equal(fs.readFileSync(path.join(f.project, 'package.json'), 'utf8'), original);
  assert.equal(fs.existsSync(path.join(f.project, 'package-lock.json')), false);
  assert.equal(fs.existsSync(path.join(f.project, 'node_modules')), false);
});

test('plan and JSON output leave no installation directories', (t) => {
  const f = fixture(t);
  const result = cli(['install', '--plan', '--json'], f);
  assert.equal(result.code, 0);
  assert.equal(JSON.parse(result.stdout).status, 'plan');
  assert.equal(JSON.parse(result.stdout).changes.length, 15);
  assert.deepEqual(JSON.parse(result.stdout).commands, SKILL_NAMES.map((name) => `$${name}`));
  assert.equal(JSON.parse(result.stdout).skills.length, 5);
  assert.equal(fs.existsSync(path.join(f.project, '.agents')), false);
});

test('repeating installation is a true no-op, including the ownership marker', (t) => {
  const f = fixture(t);
  assert.equal(installInto(f.source, f.dest).status, 'installed');
  const marker = path.join(f.dest, MARKER);
  const before = fs.statSync(marker).mtimeMs;
  const result = installInto(f.source, f.dest);
  assert.equal(result.status, 'unchanged');
  assert.deepEqual(result.changes, []);
  assert.equal(fs.statSync(marker).mtimeMs, before);
});

test('managed update adds, updates and removes only managed files', (t) => {
  const f = fixture(t);
  installInto(f.source, f.dest);
  put(f.dest, 'my-notes.md', 'Keep these notes.');
  put(f.skill, 'SKILL.md', 'Updated entrypoint.');
  put(f.skill, 'references/decide.md', 'A new reference.');
  fs.unlinkSync(path.join(f.skill, 'references/research.md'));
  put(f.source, 'package.json', JSON.stringify({ version: '0.2.1' }));
  const result = installInto(f.source, f.dest);
  assert.equal(result.status, 'updated');
  assert.equal(result.version, '0.2.1');
  assert.deepEqual(new Set(result.changes.map((item) => item.action)), new Set(['add', 'update', 'remove']));
  assert.equal(fs.readFileSync(path.join(f.dest, 'my-notes.md'), 'utf8'), 'Keep these notes.');
  assert.equal(fs.existsSync(path.join(f.dest, 'references/research.md')), false);
});

test('ownership marker key order from the Python helper remains a no-op', (t) => {
  const f = fixture(t);
  installInto(f.source, f.dest);
  const marker = JSON.parse(fs.readFileSync(path.join(f.dest, MARKER)));
  put(f.dest, MARKER, JSON.stringify({ files: marker.files, format: marker.format, name: marker.name, version: marker.version }));
  assert.equal(installInto(f.source, f.dest).status, 'unchanged');
});

test('a local edit blocks the whole operation before any files change', (t) => {
  const f = fixture(t);
  installInto(f.source, f.dest);
  put(f.dest, 'references/research.md', 'My local edits.');
  put(f.skill, 'SKILL.md', 'Upstream changed.');
  put(f.skill, 'aaa-new.md', 'Should never appear.');
  const before = snapshot(f.dest);
  assert.throws(() => installInto(f.source, f.dest), /locally modified/);
  assert.deepEqual(snapshot(f.dest), before);
});

test('a locally deleted managed file blocks replacement', (t) => {
  const f = fixture(t);
  installInto(f.source, f.dest);
  fs.unlinkSync(path.join(f.dest, 'SKILL.md'));
  assert.throws(() => installInto(f.source, f.dest), /locally modified or deleted/);
  assert.equal(fs.existsSync(path.join(f.dest, 'SKILL.md')), false);
});

test('unmanaged collisions are preserved even when their bytes match', (t) => {
  const f = fixture(t);
  put(f.dest, 'SKILL.md', fs.readFileSync(path.join(f.skill, 'SKILL.md')));
  const before = snapshot(f.dest);
  assert.throws(() => installInto(f.source, f.dest), /unmanaged file/);
  assert.deepEqual(snapshot(f.dest), before);
});

test('global, repo, and exact destination options route without modifying cwd', (t) => {
  const f = fixture(t);
  const codexHome = path.join(f.root, 'custom-codex');
  let result = cli(['--global', '--json'], f, { env: { CODEX_HOME: codexHome } });
  assert.equal(JSON.parse(result.stdout).destination, path.join(codexHome, 'skills', 'bandit'));
  assert.equal(JSON.parse(result.stdout).skills.length, 5);
  result = cli(['--repo', f.project, '--json'], f);
  assert.equal(JSON.parse(result.stdout).destination, f.dest);
  result = cli(['--dest', '../exact-skill', '--json'], f);
  assert.equal(JSON.parse(result.stdout).destination, path.join(f.root, 'exact-skill'));
  assert.equal(JSON.parse(result.stdout).skills.find((skill) => skill.name === 'bandit-review').destination, path.join(f.root, 'bandit-review'));
  result = cli(['--global', '--plan', '--json'], f);
  assert.equal(JSON.parse(result.stdout).destination, path.join(f.root, 'home', '.codex', 'skills', 'bandit'));
});

test('argument errors have exit 2 and parseable JSON when requested', (t) => {
  const f = fixture(t);
  for (const args of [['--global', '--repo', f.project], ['--wat'], ['--dest'], ['--repo', 'missing-project']]) {
    const result = cli([...args, '--json'], f);
    assert.equal(result.code, 2);
    assert.equal(JSON.parse(result.stdout).status, 'error');
    assert.equal(result.stderr, '');
  }
  assert.equal(cli(['--version'], f).stdout, '0.4.0\n');
  assert.match(cli(['--help'], f).stdout, /--global/);
});

test('an existing PM Craft installation is reported and left intact', (t) => {
  const f = fixture(t);
  const legacy = path.join(path.dirname(f.dest), 'pm-craft');
  put(legacy, 'SKILL.md', 'Old installation with custom edits.');
  const before = snapshot(legacy);
  const result = cli(['--json'], f);
  assert.equal(result.code, 0);
  assert.match(JSON.parse(result.stdout).notes[0], /pm-craft/);
  assert.deepEqual(snapshot(legacy), before);
});

test('custom PM Craft core destinations do not emit separate legacy installation notes', (t) => {
  const observations = [];
  // Separate parents also exercise the case alias on case-insensitive filesystems.
  for (const coreName of ['pm-craft', 'PM-Craft']) {
    const f = fixture(t);
    const dest = path.join(f.root, 'custom-skills', coreName);
    const parent = path.dirname(dest);
    const before = snapshot(parent);
    const run = (stage, options = []) => {
      const result = cli(['--dest', dest, ...options, '--json'], f);
      assert.equal(result.code, 0, `${coreName} ${stage}: ${result.stderr}`);
      const report = JSON.parse(result.stdout);
      observations.push({ coreName, stage, notes: report.notes ?? [] });
      return report;
    };
    assert.equal(run('plan before', ['--plan']).status, 'plan');
    assert.deepEqual(snapshot(parent), before);
    assert.equal(run('install').status, 'installed');
    assert.equal(JSON.parse(fs.readFileSync(path.join(dest, MARKER), 'utf8')).name, 'bandit');
    const installed = snapshot(parent);
    assert.equal(run('repeat').status, 'unchanged');
    assert.deepEqual(snapshot(parent), installed);
    assert.equal(run('plan after', ['--plan']).status, 'plan');
    assert.deepEqual(snapshot(parent), installed);
    const textRepeat = cli(['--dest', dest], f);
    assert.equal(textRepeat.code, 0);
    observations.push({ coreName, stage: 'text repeat', notes: textRepeat.stdout.match(/A separate pm-craft[^\n]*/g) ?? [] });
    assert.deepEqual(snapshot(parent), installed);
  }
  assert.deepEqual(observations, observations.map((item) => ({ ...item, notes: [] })));
});

test('malformed and escaping ownership entries are rejected', (t) => {
  const f = fixture(t);
  for (const name of ['../outside.md', '/outside.md', 'refs\\escape.md', 'C:escape', 'refs/CON.md', 'refs/trailing.']) {
    put(f.dest, MARKER, JSON.stringify({ format: 1, name: 'bandit', version: '0.2.0', files: { [name]: 'a'.repeat(64) } }));
    assert.throws(() => installInto(f.source, f.dest), /Unsafe relative/);
  }
  put(f.dest, MARKER, '{broken');
  assert.throws(() => installInto(f.source, f.dest), /Invalid ownership/);
  assert.equal(fs.existsSync(path.join(f.root, 'outside.md')), false);
});

test('source and destination overlap is rejected in both directions', (t) => {
  const f = fixture(t);
  assert.throws(() => makePlan(f.source, f.skill), /overlap/);
  assert.throws(() => makePlan(f.source, path.join(f.skill, 'installed')), /overlap/);
  assert.throws(() => makePlan(f.source, f.source), /overlap/);
});

test('symlink and junction ancestors cannot redirect an installation', (t) => {
  const f = fixture(t);
  const outside = path.join(f.root, 'outside');
  fs.mkdirSync(outside);
  const link = path.join(f.project, '.agents');
  try { fs.symlinkSync(outside, link, process.platform === 'win32' ? 'junction' : 'dir'); }
  catch (error) { if (error.code === 'EPERM') return t.skip('Symlink privilege unavailable'); throw error; }
  assert.throws(() => installInto(f.source, f.dest), /Symlink or junction/);
  assert.deepEqual(fs.readdirSync(outside), []);
});

test('source symlinks cannot include files outside the skill', (t) => {
  const f = fixture(t);
  put(f.root, 'private.txt', 'Do not copy.');
  try { fs.symlinkSync(path.join(f.root, 'private.txt'), path.join(f.skill, 'secret.txt'), 'file'); }
  catch (error) { if (error.code === 'EPERM') return t.skip('Symlink privilege unavailable'); throw error; }
  assert.throws(() => installInto(f.source, f.dest), /Symlink or junction/);
  assert.equal(fs.existsSync(f.dest), false);
});

test('case-only managed directory renames stop before removing old files', (t) => {
  const f = fixture(t);
  put(f.skill, 'Notes/a.md', 'A');
  installInto(f.source, f.dest);
  fs.renameSync(path.join(f.skill, 'Notes'), path.join(f.skill, 'temporary-notes'));
  fs.renameSync(path.join(f.skill, 'temporary-notes'), path.join(f.skill, 'notes'));
  const before = snapshot(f.dest);
  assert.throws(() => installInto(f.source, f.dest), /rename needs a fresh destination/);
  assert.deepEqual(snapshot(f.dest), before);
});

test('unmanaged case aliases are not overwritten on any filesystem', (t) => {
  const f = fixture(t);
  put(f.dest, 'skill.md', 'My separate file.');
  const before = snapshot(f.dest);
  assert.throws(() => installInto(f.source, f.dest), /Ambiguous case/);
  assert.deepEqual(snapshot(f.dest), before);
});

test('Unicode aliases are not treated as separate managed paths', (t) => {
  const f = fixture(t);
  put(f.skill, 'references/café.md', 'Original.');
  installInto(f.source, f.dest);
  const marker = JSON.parse(fs.readFileSync(path.join(f.dest, MARKER)));
  const existing = Object.keys(marker.files).find((name) => name.normalize('NFC') === 'references/café.md');
  marker.files[existing.normalize('NFD') === existing ? existing.normalize('NFC') : existing.normalize('NFD')] = marker.files[existing];
  put(f.dest, MARKER, JSON.stringify(marker));
  assert.throws(() => installInto(f.source, f.dest), /Ambiguous managed path/);
});

test('a destination lock prevents concurrent writes', (t) => {
  const f = fixture(t);
  put(path.dirname(f.dest), '.bandit.bandit.lock', 'Existing lock.');
  assert.throws(() => installInto(f.source, f.dest), /Another installation may be running/);
  assert.equal(fs.existsSync(f.dest), false);
});

test('invalid source versions cannot become installed markers', (t) => {
  const f = fixture(t);
  put(f.source, 'package.json', JSON.stringify({ version: 'next' }));
  assert.throws(() => installInto(f.source, f.dest), /stable semantic version/);
  assert.equal(fs.existsSync(f.dest), false);
});

test('an existing 0.2 core upgrades while all four independent specialists are added', (t) => {
  const f = fixture(t);
  put(f.source, 'package.json', JSON.stringify({ version: '0.2.0' }));
  installInto(f.source, f.dest);
  put(f.dest, 'my-notes.md', 'Keep old notes.');
  put(f.source, 'package.json', JSON.stringify({ version: '0.4.0' }));
  put(f.skill, 'SKILL.md', 'The new general planning skill.');
  const report = installBundle(f.source, f.dest);
  assert.equal(report.status, 'updated');
  assert.equal(report.skills[0].status, 'updated');
  assert.equal(report.skills.filter((skill) => skill.status === 'installed').length, 4);
  assert.equal(report.version, '0.4.0');
  assert.equal(fs.readFileSync(path.join(f.dest, 'my-notes.md'), 'utf8'), 'Keep old notes.');
  assert.equal(installBundle(f.source, f.dest).status, 'unchanged');
});

test('an edited 0.2 core prevents adding the four specialist skills', (t) => {
  const f = fixture(t);
  put(f.source, 'package.json', JSON.stringify({ version: '0.2.0' }));
  installInto(f.source, f.dest);
  put(f.dest, 'SKILL.md', 'Local edits to the old installation.');
  put(f.source, 'package.json', JSON.stringify({ version: '0.4.0' }));
  const before = snapshot(path.dirname(f.dest));
  assert.throws(() => installBundle(f.source, f.dest), /locally modified/);
  assert.deepEqual(snapshot(path.dirname(f.dest)), before);
});

test('a conflict in the last skill blocks all five updates before writing', (t) => {
  const f = fixture(t);
  installBundle(f.source, f.dest);
  for (const name of SKILL_NAMES) put(path.join(f.source, 'skills', name), 'SKILL.md', `New ${name}.`);
  put(path.join(path.dirname(f.dest), 'bandit-review'), 'SKILL.md', 'Local edit in the last skill.');
  const before = snapshot(path.dirname(f.dest));
  assert.throws(() => installBundle(f.source, f.dest), /bandit-review/);
  assert.deepEqual(snapshot(path.dirname(f.dest)), before);
});

test('an unmanaged last-skill conflict leaves a fresh core uninstalled', (t) => {
  const f = fixture(t);
  put(path.join(path.dirname(f.dest), 'bandit-review'), 'SKILL.md', 'Independent user file.');
  const before = snapshot(path.dirname(f.dest));
  assert.throws(() => installBundle(f.source, f.dest), /unmanaged file/);
  assert.deepEqual(snapshot(path.dirname(f.dest)), before);
  assert.equal(fs.existsSync(f.dest), false);
});

test('a missing packaged specialist is rejected before creating any destination', (t) => {
  const f = fixture(t);
  fs.rmSync(path.join(f.source, 'skills', 'bandit-review'), { recursive: true });
  assert.throws(() => installBundle(f.source, f.dest), /Missing skill directory/);
  assert.equal(fs.existsSync(path.join(f.project, '.agents')), false);
});

test('custom --dest cannot collide with another installed skill or any package source', (t) => {
  const f = fixture(t);
  assert.throws(() => installBundle(f.source, path.join(f.root, 'bandit-review')), /--dest overlaps/);
  assert.throws(() => installBundle(f.source, path.join(f.source, 'skills', 'custom-core')), /Source and destination/);
  assert.equal(fs.existsSync(path.join(f.root, 'bandit-review')), false);
});

test('a lock on any specialist prevents the entire package installation', (t) => {
  const f = fixture(t);
  put(path.dirname(f.dest), '.bandit-review.bandit.lock', 'Another installer owns this lock.');
  const before = snapshot(path.dirname(f.dest));
  assert.throws(() => installBundle(f.source, f.dest), /Another installation/);
  assert.deepEqual(snapshot(path.dirname(f.dest)), before);
});

test('an I/O failure in the last skill rolls back updates across earlier skills', (t) => {
  const f = fixture(t);
  installBundle(f.source, f.dest);
  for (const name of SKILL_NAMES) put(path.join(f.source, 'skills', name), 'SKILL.md', `Changed ${name}.`);
  const before = snapshot(path.dirname(f.dest));
  const rename = fs.renameSync;
  let failed = false;
  fs.renameSync = (from, to) => {
    if (!failed && to === path.join(path.dirname(f.dest), 'bandit-review', 'SKILL.md')) {
      failed = true;
      throw Object.assign(new Error('Simulated disk failure'), { code: 'EIO' });
    }
    return rename(from, to);
  };
  try { assert.throws(() => installBundle(f.source, f.dest), /Simulated disk failure/); }
  finally { fs.renameSync = rename; }
  assert.equal(failed, true);
  assert.deepEqual(snapshot(path.dirname(f.dest)), before);
});

test('a failed fresh package install removes only directories and files it created', (t) => {
  const f = fixture(t);
  put(f.project, 'notes.txt', 'Do not touch.');
  const before = snapshot(f.project);
  const rename = fs.renameSync;
  let failed = false;
  fs.renameSync = (from, to) => {
    if (!failed && to === path.join(path.dirname(f.dest), 'bandit-review', 'SKILL.md')) {
      failed = true;
      throw Object.assign(new Error('Simulated disk failure'), { code: 'EIO' });
    }
    return rename(from, to);
  };
  try { assert.throws(() => installBundle(f.source, f.dest), /Simulated disk failure/); }
  finally { fs.renameSync = rename; }
  assert.equal(failed, true);
  assert.deepEqual(snapshot(f.project), before);
});

test('cross-skill recovery preserves an editor change made during the failed update', (t) => {
  const f = fixture(t);
  installBundle(f.source, f.dest);
  for (const name of SKILL_NAMES) put(path.join(f.source, 'skills', name), 'SKILL.md', `Changed ${name}.`);
  const before = snapshot(path.dirname(f.dest));
  const edited = 'User edit while installation was running.';
  const rename = fs.renameSync;
  let failed = false;
  fs.renameSync = (from, to) => {
    if (!failed && to === path.join(path.dirname(f.dest), 'bandit-review', 'SKILL.md')) {
      failed = true;
      put(f.dest, 'SKILL.md', edited);
      throw Object.assign(new Error('Simulated disk failure'), { code: 'EIO' });
    }
    return rename(from, to);
  };
  try { assert.throws(() => installBundle(f.source, f.dest), /Simulated disk failure/); }
  finally { fs.renameSync = rename; }
  const expected = { ...before, [path.join('bandit', 'SKILL.md')]: Buffer.from(edited).toString('base64') };
  assert.deepEqual(snapshot(path.dirname(f.dest)), expected);
});

test('an edit made while later skills are being preflighted cannot become an overwrite baseline', (t) => {
  const f = fixture(t);
  installBundle(f.source, f.dest);
  for (const name of SKILL_NAMES) put(path.join(f.source, 'skills', name), 'SKILL.md', `Changed ${name}.`);
  const before = snapshot(path.dirname(f.dest));
  const edited = 'User edit while the final specialist is being checked.';
  const read = fs.readFileSync;
  const laterSource = path.join(f.source, 'skills', 'bandit-review', 'SKILL.md');
  let reads = 0;
  fs.readFileSync = (file, ...args) => {
    const bytes = read(file, ...args);
    if (file === laterSource && ++reads === 2) put(f.dest, 'SKILL.md', edited);
    return bytes;
  };
  try { assert.throws(() => installBundle(f.source, f.dest), /Destination changed during installation/); }
  finally { fs.readFileSync = read; }
  assert.equal(reads, 2);
  const expected = { ...before, [path.join('bandit', 'SKILL.md')]: Buffer.from(edited).toString('base64') };
  assert.deepEqual(snapshot(path.dirname(f.dest)), expected);
});

test('an edit made while a replacement is being staged is preserved with earlier writes rolled back', (t) => {
  const f = fixture(t);
  installBundle(f.source, f.dest);
  for (const name of SKILL_NAMES) put(path.join(f.source, 'skills', name), 'SKILL.md', `Changed ${name}.`);
  const before = snapshot(path.dirname(f.dest));
  const target = path.join(path.dirname(f.dest), 'bandit-review', 'SKILL.md');
  const edited = 'User edit while the installer stages a replacement.';
  let injected = false;
  afterWrites((file, data, write) => {
    if (!injected && path.dirname(file) === path.dirname(target) && path.basename(file).endsWith('.tmp')) {
      injected = true;
      write(target, edited);
    }
  }, () => assert.throws(() => installBundle(f.source, f.dest), /Destination changed during installation/));
  assert.equal(injected, true);
  const expected = { ...before, [path.join('bandit-review', 'SKILL.md')]: Buffer.from(edited).toString('base64') };
  assert.deepEqual(snapshot(path.dirname(f.dest)), expected);
});

test('0.3 migration installs scope and retires both old commands without aliases', (t) => {
  const f = fixture(t);
  oldInstallation(f);
  const result = cli(['--json'], f);
  assert.equal(result.code, 0);
  const report = JSON.parse(result.stdout);
  assert.equal(report.status, 'updated');
  assert.deepEqual(report.skills.map((skill) => skill.name), SKILL_NAMES);
  assert.deepEqual(report.commands, SKILL_NAMES.map((name) => `$${name}`));
  assert.deepEqual(report.retirements.map((skill) => [skill.name, skill.status]), RETIRED_NAMES.map((name) => [name, 'retired']));
  assert.deepEqual(report.migrations, [
    { from: 'bandit-decide', to: 'bandit-scope', status: 'retired' },
    { from: 'bandit-update', to: 'bandit-specify', status: 'retired' },
  ]);
  assert.deepEqual(fs.readdirSync(path.dirname(f.dest)).sort(), [...SKILL_NAMES].sort());
  assert.ok(report.changes.some((change) => change.skill === 'bandit-decide' && change.action === 'remove'));
  assert.equal(installBundle(f.source, f.dest).status, 'unchanged');
});

test('retirement keeps unrelated notes while removing old entrypoints and ownership', (t) => {
  const f = fixture(t);
  oldInstallation(f);
  const retired = path.join(path.dirname(f.dest), 'bandit-decide');
  put(retired, 'personal/notes.md', 'My local planning notes.');
  const report = installBundle(f.source, f.dest);
  assert.equal(report.retirements[0].status, 'retired');
  assert.equal(fs.readFileSync(path.join(retired, 'personal/notes.md'), 'utf8'), 'My local planning notes.');
  assert.equal(fs.existsSync(path.join(retired, 'SKILL.md')), false);
  assert.equal(fs.existsSync(path.join(retired, MARKER)), false);
  assert.equal(fs.existsSync(path.join(retired, 'references')), false);
  const again = installBundle(f.source, f.dest);
  assert.equal(again.status, 'unchanged');
  assert.equal(again.retirements[0].status, 'preserved');
});

test('already deleted managed files do not block retiring their old skill', (t) => {
  const f = fixture(t);
  oldInstallation(f);
  const retired = path.join(path.dirname(f.dest), 'bandit-update');
  fs.unlinkSync(path.join(retired, 'SKILL.md'));
  fs.unlinkSync(path.join(retired, 'references/old.md'));
  assert.equal(installBundle(f.source, f.dest).status, 'updated');
  assert.equal(fs.existsSync(retired), false);
});

test('a modified retired reference blocks all active updates and both retirements', (t) => {
  const f = fixture(t);
  oldInstallation(f);
  put(path.join(path.dirname(f.dest), 'bandit-update'), 'references/old.md', 'User customization.');
  const before = snapshot(path.dirname(f.dest));
  assert.throws(() => installBundle(f.source, f.dest), /modified files in retired skill bandit-update/);
  assert.deepEqual(snapshot(path.dirname(f.dest)), before);
});

test('an unmanaged retired entrypoint blocks migration even when other notes are safe', (t) => {
  const f = fixture(t);
  const retired = path.join(path.dirname(f.dest), 'bandit-decide');
  put(retired, 'SKILL.md', 'An independent skill with the old name.');
  put(retired, 'notes.md', 'Leave everything alone.');
  const before = snapshot(f.project);
  assert.throws(() => installBundle(f.source, f.dest), /unmanaged retired skill/);
  assert.deepEqual(snapshot(f.project), before);
});

test('a marker cannot authorize removing an unlisted retired entrypoint', (t) => {
  const f = fixture(t);
  oldInstallation(f);
  const retired = path.join(path.dirname(f.dest), 'bandit-decide');
  const marker = JSON.parse(fs.readFileSync(path.join(retired, MARKER)));
  delete marker.files['SKILL.md'];
  put(retired, MARKER, JSON.stringify(marker));
  const before = snapshot(f.project);
  assert.throws(() => installBundle(f.source, f.dest), /unmanaged retired skill/);
  assert.deepEqual(snapshot(f.project), before);
});

test('unmanaged retired folders without an entrypoint are preserved', (t) => {
  const f = fixture(t);
  const retired = path.join(path.dirname(f.dest), 'bandit-update');
  put(retired, 'notes.md', 'These are notes, not an installed command.');
  const report = installBundle(f.source, f.dest);
  assert.equal(report.status, 'installed');
  assert.equal(report.retirements.find((skill) => skill.name === 'bandit-update').status, 'preserved');
  assert.equal(fs.readFileSync(path.join(retired, 'notes.md'), 'utf8'), 'These are notes, not an installed command.');
});

test('migration preview reports removals without changing any files or directories', (t) => {
  const f = fixture(t);
  oldInstallation(f);
  const before = snapshot(f.project);
  const result = cli(['--plan', '--json'], f);
  assert.equal(result.code, 0);
  const report = JSON.parse(result.stdout);
  assert.equal(report.status, 'plan');
  assert.ok(report.retirements.every((skill) => skill.changes.length === 3 && skill.marker_change));
  assert.deepEqual(snapshot(f.project), before);
});

test('retired target locks serialize migration with the 0.3 installer', (t) => {
  const f = fixture(t);
  oldInstallation(f);
  put(path.dirname(f.dest), '.bandit-update.bandit.lock', 'Old installer lock.');
  const before = snapshot(f.project);
  assert.throws(() => installBundle(f.source, f.dest), /Another installation/);
  assert.deepEqual(snapshot(f.project), before);
});

test('custom core destinations cannot overlap either retired command', (t) => {
  const f = fixture(t);
  for (const name of RETIRED_NAMES) assert.throws(() => installBundle(f.source, path.join(f.root, name)), /--dest overlaps/);
  assert.equal(fs.existsSync(path.join(f.root, 'bandit-decide')), false);
  assert.equal(fs.existsSync(path.join(f.root, 'bandit-update')), false);
});

test('an active write failure restores already retired files and markers', (t) => {
  const f = fixture(t);
  oldInstallation(f);
  const before = snapshot(f.project);
  const rename = fs.renameSync;
  let observedRetirement = false;
  let failed = false;
  fs.renameSync = (from, to) => {
    if (!failed && to === path.join(f.dest, 'SKILL.md')) {
      failed = true;
      observedRetirement = RETIRED_NAMES.every((name) => !fs.existsSync(path.join(path.dirname(f.dest), name, MARKER)));
      throw Object.assign(new Error('Simulated active update failure'), { code: 'EIO' });
    }
    return rename(from, to);
  };
  try { assert.throws(() => installBundle(f.source, f.dest), /Simulated active update failure/); }
  finally { fs.renameSync = rename; }
  assert.equal(observedRetirement, true);
  assert.deepEqual(snapshot(f.project), before);
});

test('retirement recovery preserves an editor replacement of a deleted old file', (t) => {
  const f = fixture(t);
  oldInstallation(f);
  const before = snapshot(f.project);
  const edited = 'A concurrent edit to preserve.';
  const retired = path.join(path.dirname(f.dest), 'bandit-update');
  const rename = fs.renameSync;
  let failed = false;
  fs.renameSync = (from, to) => {
    if (!failed && to === path.join(f.dest, 'SKILL.md')) {
      failed = true;
      put(retired, 'SKILL.md', edited);
      throw Object.assign(new Error('Simulated active update failure'), { code: 'EIO' });
    }
    return rename(from, to);
  };
  try { assert.throws(() => installBundle(f.source, f.dest), /Simulated active update failure/); }
  finally { fs.renameSync = rename; }
  const expected = { ...before, [path.join('.agents', 'skills', 'bandit-update', 'SKILL.md')]: Buffer.from(edited).toString('base64') };
  assert.deepEqual(snapshot(f.project), expected);
});

test('retired file edits after their preflight stop every update and removal', (t) => {
  const f = fixture(t);
  oldInstallation(f);
  const before = snapshot(f.project);
  const edited = 'Edit the retiring skill while the next skill is checked.';
  const retired = path.join(path.dirname(f.dest), 'bandit-decide');
  const laterMarker = path.join(path.dirname(f.dest), 'bandit-update', MARKER);
  const read = fs.readFileSync;
  let reads = 0;
  fs.readFileSync = (file, ...args) => {
    const bytes = read(file, ...args);
    if (file === laterMarker && ++reads === 2) put(retired, 'SKILL.md', edited);
    return bytes;
  };
  try { assert.throws(() => installBundle(f.source, f.dest), /Destination changed during installation/); }
  finally { fs.readFileSync = read; }
  assert.equal(reads, 2);
  const expected = { ...before, [path.join('.agents', 'skills', 'bandit-decide', 'SKILL.md')]: Buffer.from(edited).toString('base64') };
  assert.deepEqual(snapshot(f.project), expected);
});

test('lock cleanup cannot follow a replaced parent into unrelated lock files', (t) => {
  const f = fixture(t);
  const parent = path.dirname(f.dest);
  const moved = path.join(f.root, 'moved-skills');
  const unrelated = path.join(f.root, 'unrelated-lock-owner');
  const alias = path.join(f.root, 'prepared-parent-link');
  const names = [...SKILL_NAMES, ...RETIRED_NAMES].map((name) => `.${name}.bandit.lock`);
  for (const name of names) put(unrelated, name, `Another installation owns ${name}.`);
  try { fs.symlinkSync(unrelated, alias, process.platform === 'win32' ? 'junction' : 'dir'); }
  catch { t.skip('Symlink creation unavailable on this platform.'); return; }
  const before = snapshot(unrelated);
  let injected = false;
  afterWrites((file) => {
    if (!injected && path.dirname(file) === f.dest && path.basename(file).endsWith('.tmp')) {
      injected = true;
      fs.renameSync(parent, moved);
      fs.renameSync(alias, parent);
    }
  }, () => assert.throws(() => installBundle(f.source, f.dest), /Symlink or junction/));
  assert.equal(injected, true);
  assert.deepEqual(snapshot(unrelated), before, 'Cleanup must preserve every unrelated lock byte');
  for (const name of names) assert.equal(fs.readFileSync(path.join(moved, name)).length, 0);
});

test('lock cleanup preserves a replacement empty file with a different identity', (t) => {
  const f = fixture(t);
  const parent = path.dirname(f.dest);
  const lock = path.join(parent, '.bandit-update.bandit.lock');
  const saved = path.join(f.root, 'original-acquired-lock');
  let injected = false, replacement;
  afterWrites((file, data, write) => {
    if (!injected && path.dirname(file) === f.dest && path.basename(file).endsWith('.tmp')) {
      injected = true;
      fs.renameSync(lock, saved);
      write(lock, '', { flag: 'wx' });
      replacement = fs.lstatSync(lock, { bigint: true });
    }
  }, () => installBundle(f.source, f.dest));
  assert.equal(injected, true);
  assert.notEqual(replacement.ino, fs.lstatSync(saved, { bigint: true }).ino);
  assert.ok(fs.existsSync(lock), 'Another owner\'s replacement lock must survive');
  assert.equal(fs.lstatSync(lock, { bigint: true }).ino, replacement.ino);
  assert.equal(fs.readFileSync(lock).length, 0);
  assert.deepEqual(fs.readdirSync(parent).filter((name) => name.endsWith('.bandit.lock')), [path.basename(lock)]);
  assert.equal(fs.readFileSync(saved).length, 0);
});

test('a removed lock does not prevent cleanup of the other acquired locks', (t) => {
  const f = fixture(t);
  const parent = path.dirname(f.dest);
  const lock = path.join(parent, '.bandit-update.bandit.lock');
  let injected = false, error;
  afterWrites((file) => {
    if (!injected && path.dirname(file) === f.dest && path.basename(file).endsWith('.tmp')) {
      injected = true;
      fs.unlinkSync(lock);
    }
  }, () => {
    try { installBundle(f.source, f.dest); }
    catch (caught) { error = caught; }
  });
  assert.equal(injected, true);
  assert.deepEqual(fs.readdirSync(parent).filter((name) => name.endsWith('.bandit.lock')), [],
    `A removed lock must not strand unaffected owned locks: ${error?.message ?? 'no error'}`);
  for (const name of SKILL_NAMES) assert.ok(fs.existsSync(path.join(parent, name, MARKER)));
});
