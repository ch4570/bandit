// One-off macOS/Node-22 integration evidence harness. Not an end-user installer.
// Every project, cache, downloaded archive, and log is retained under a fresh
// caller-provided scratch directory. No real home/project setting is overridden.
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { gunzipSync } from 'node:zlib';
import { spawn } from 'node:child_process';

const [scratch, candidateFile, npmBinDirectory] = process.argv.slice(2);
assert.equal(Number(process.versions.node.split('.')[0]), 22);
assert.ok(scratch?.startsWith('/TEMP/bandit-round9-'));
assert.equal(fs.realpathSync(scratch), scratch);
assert.deepEqual(fs.readdirSync(scratch), [], 'scratch must start empty');
assert.ok(path.isAbsolute(candidateFile) && path.isAbsolute(npmBinDirectory));
const hash = bytes => createHash('sha256').update(bytes).digest('hex');
const save = (name, value) => fs.writeFileSync(path.join(scratch, name),
  typeof value === 'string' || Buffer.isBuffer(value) ? value : JSON.stringify(value, null, 2) + '\n', { flag: 'wx' });
const active = ['bandit', 'bandit-research', 'bandit-scope', 'bandit-specify', 'bandit-review'];
const retired = ['bandit-decide', 'bandit-update'];
const marker = '.bandit-install.json';
const urls = Object.fromEntries(['0.4.0', '0.3.0'].map(v => [v,
  `https://github.com/ch4570/bandit/releases/download/v${v}/bandit.tgz`]));
const runs = [];
let serial = 0;
for (const dir of ['bin', 'logs', 'snapshots', 'downloads', 'tmp', 'projects', 'cache-public', 'cache-candidate', 'cache-old'])
  fs.mkdirSync(path.join(scratch, dir));
for (const [name, target] of [['node', process.execPath], ['npm', path.join(npmBinDirectory, 'npm-cli.js')],
  ['npx', path.join(npmBinDirectory, 'npx-cli.js')], ['sh', '/bin/sh']])
  fs.symlinkSync(target, path.join(scratch, 'bin', name));
save('empty-user.npmrc', '');
save('empty-global.npmrc', '');
const environment = cache => ({
  PATH: path.join(scratch, 'bin'), TMPDIR: path.join(scratch, 'tmp'),
  npm_config_cache: path.join(scratch, cache),
  npm_config_userconfig: path.join(scratch, 'empty-user.npmrc'),
  npm_config_globalconfig: path.join(scratch, 'empty-global.npmrc'),
  npm_config_audit: 'false', npm_config_fund: 'false', npm_config_progress: 'false',
  npm_config_update_notifier: 'false', npm_config_fetch_retries: '0',
  npm_config_fetch_timeout: '30000', npm_config_script_shell: '/bin/sh',
});

async function command(label, executable, args, cwd, cache, expected = 0) {
  const index = String(++serial).padStart(2, '0');
  const record = { label, executable, args, cwd, cache, started_at: new Date().toISOString(), stdin: 'closed' };
  process.stdout.write(`START ${index} ${label}\n`);
  const result = await new Promise(resolve => {
    const child = spawn(executable, args, { cwd, env: environment(cache), stdio: ['ignore', 'pipe', 'pipe'] });
    let stdout = '', stderr = '', launchError = null;
    child.stdout.on('data', data => { stdout += data; });
    child.stderr.on('data', data => { stderr += data; });
    child.on('error', error => { launchError = error.message; });
    const deadline = setTimeout(() => child.kill('SIGTERM'), 45000);
    child.on('close', (exit_code, signal) => {
      clearTimeout(deadline); resolve({ stdout, stderr, exit_code, signal, launchError });
    });
  });
  Object.assign(record, result, { finished_at: new Date().toISOString() });
  save(`logs/${index}-${label}.json`, record);
  runs.push(record);
  process.stdout.write(`END ${index} ${label}: ${result.exit_code}\n`);
  assert.equal(result.launchError, null, `${label}: launch error`);
  assert.equal(result.signal, null, `${label}: terminated`);
  assert.equal(result.exit_code, expected, `${label}: ${result.stderr || result.stdout}`);
  return result;
}
const npx = (label, spec, options, project, cache, expected) =>
  command(label, path.join(scratch, 'bin/npx'), ['--yes', spec, ...options], project, cache, expected);

function unpack(bytes) {
  const tar = gunzipSync(bytes), files = new Map();
  for (let offset = 0; offset + 512 <= tar.length;) {
    const header = tar.subarray(offset, offset + 512);
    if (header.every(x => x === 0)) break;
    const text = (start, length) => header.subarray(start, start + length).toString('utf8').split('\0')[0];
    const name = [text(345, 155), text(0, 100)].filter(Boolean).join('/');
    const size = parseInt(text(124, 12).trim(), 8) || 0;
    const type = text(156, 1);
    assert.ok(name.startsWith('package/') && !name.split('/').includes('..'), name);
    assert.ok(['', '0', '5'].includes(type), `unsupported archive type: ${type} ${name}`);
    assert.ok(offset + 512 + size <= tar.length, 'truncated archive');
    if (type !== '5') {
      const relative = name.slice('package/'.length);
      assert.ok(!files.has(relative), 'duplicate archive member');
      files.set(relative, tar.subarray(offset + 512, offset + 512 + size));
    }
    offset += 512 + Math.ceil(size / 512) * 512;
  }
  const manifest = JSON.parse(files.get('package.json'));
  assert.equal(manifest.name, '@ch4570/bandit');
  assert.equal(manifest.bin.bandit, 'bin/bandit.mjs');
  assert.equal(Object.keys(manifest.dependencies ?? {}).length, 0);
  for (const hook of ['preinstall', 'install', 'postinstall', 'prepare', 'prepublish', 'prepublishOnly'])
    assert.equal(manifest.scripts?.[hook], undefined, `unexpected lifecycle hook: ${hook}`);
  return { bytes, files, manifest, sha256: hash(bytes) };
}
async function download(version) {
  const response = await fetch(urls[version], { signal: AbortSignal.timeout(30000) });
  assert.equal(response.status, 200, `download ${version}`);
  const bytes = Buffer.from(await response.arrayBuffer());
  save(`downloads/public-${version}.tgz`, bytes);
  const archive = unpack(bytes);
  assert.equal(archive.manifest.version, version);
  return archive;
}
function inventory(root) {
  const entries = {};
  function walk(dir) {
    for (const name of fs.readdirSync(dir).sort()) {
      const file = path.join(dir, name), st = fs.lstatSync(file, { bigint: true }), rel = path.relative(root, file);
      assert.ok(st.isFile() || st.isDirectory(), `unexpected file type ${file}`);
      entries[rel] = { type: st.isDirectory() ? 'directory' : 'file', mode: Number(st.mode),
        inode: String(st.ino), mtime_ns: String(st.mtimeNs) };
      if (st.isDirectory()) walk(file);
      else Object.assign(entries[rel], { bytes: Number(st.size), sha256: hash(fs.readFileSync(file)) });
    }
  }
  walk(root);
  return entries;
}
function snapshot(label, root) {
  const value = inventory(root); save(`snapshots/${label}.json`, value); return value;
}
function project(name) {
  const dir = path.join(scratch, 'projects', name); fs.mkdirSync(dir);
  fs.writeFileSync(path.join(dir, 'project-note.md'), '# Synthetic integration project\nPreserve this note.\n');
  return dir;
}
function validateInstall(projectRoot, archive, expectedNames = active) {
  const root = path.join(projectRoot, '.agents/skills');
  let count = 0;
  for (const name of expectedNames) {
    const prefix = `skills/${name}/`, folder = path.join(root, name);
    const payload = [...archive.files].filter(([p]) => p.startsWith(prefix));
    const expected = Object.fromEntries(payload.map(([p, bytes]) => [p.slice(prefix.length), hash(bytes)]).sort());
    const ownership = JSON.parse(fs.readFileSync(path.join(folder, marker)));
    assert.deepEqual(ownership, { format: 1, name, version: archive.manifest.version, files: expected });
    for (const [p, bytes] of payload) assert.deepEqual(fs.readFileSync(path.join(root, p.slice('skills/'.length))), bytes, p);
    assert.match(fs.readFileSync(path.join(folder, 'SKILL.md'), 'utf8'), new RegExp(`name: ${name}\\r?\\n`));
    assert.ok(fs.readFileSync(path.join(folder, 'agents/openai.yaml'), 'utf8').includes(`$${name}`));
    count += payload.length;
  }
  for (const name of ['package.json', 'package-lock.json', 'node_modules'])
    assert.equal(fs.existsSync(path.join(projectRoot, name)), false, `unexpected project ${name}`);
  assert.equal(fs.readFileSync(path.join(projectRoot, 'project-note.md'), 'utf8'), '# Synthetic integration project\nPreserve this note.\n');
  for (const name of Object.keys(inventory(projectRoot))) assert.ok(!/\.bandit.*(?:lock|tmp)/.test(name), name);
  return count;
}
function verifyCache(cacheName, archive) {
  const packages = path.join(scratch, cacheName, '_npx');
  const candidates = fs.readdirSync(packages).map(name => path.join(packages, name, 'node_modules/@ch4570/bandit'))
    .filter(file => fs.existsSync(file));
  assert.equal(candidates.length, 1, `${cacheName}: unexpected cache package count`);
  const root = candidates[0];
  for (const [name, bytes] of archive.files) assert.deepEqual(fs.readFileSync(path.join(root, name)), bytes, `${cacheName}: ${name}`);
  return { root, files_checked: archive.files.size, archive_sha256: archive.sha256 };
}
async function unchanged(label, projectRoot, spec, cache, archive) {
  const before = snapshot(label + '-before', projectRoot);
  const result = JSON.parse((await npx(label, spec, ['--json'], projectRoot, cache)).stdout);
  assert.equal(result.status, 'unchanged');
  assert.deepEqual(snapshot(label + '-after', projectRoot), before, `${label}: repeat modified project or mtimes`);
  validateInstall(projectRoot, archive);
}

try {
  const runtime = await command('runtime', '/bin/sh', ['-c',
    'set -e; node --version; npm --version; command -v node; command -v npm; command -v npx; if command -v git || command -v python || command -v python3; then exit 9; fi'],
  scratch, 'cache-public');
  const candidate = unpack(fs.readFileSync(candidateFile));
  assert.equal(candidate.sha256, 'a2fb5d29889010c2c0c8d0da3783be052667d6c295ffac72039ac99045655252');
  const published = await download('0.4.0'), old = await download('0.3.0');
  save('sources.json', { candidate: { file: candidateFile, sha256: candidate.sha256 },
    public: { url: urls['0.4.0'], sha256: published.sha256 }, old: { url: urls['0.3.0'], sha256: old.sha256 },
    packages: [candidate, published, old].map(a => ({ version: a.manifest.version, files: a.files.size,
      archive_sha256: a.sha256, package_files: Object.fromEntries([...a.files].map(([p, b]) => [p, hash(b)]).sort()) })) });

  const publicProject = project('public 한글 project');
  const first = await npx('public-install', urls['0.4.0'], [], publicProject, 'cache-public');
  assert.ok(first.stdout.includes(path.join(publicProject, '.agents/skills')));
  assert.ok(first.stdout.includes('Five skills installed:'));
  assert.equal(validateInstall(publicProject, published), 34);
  snapshot('public-installed', publicProject);
  await unchanged('public-repeat', publicProject, urls['0.4.0'], 'cache-public', published);

  const candidateProject = project('candidate 한글 project');
  const candidateBefore = snapshot('candidate-preview-before', candidateProject);
  const preview = JSON.parse((await npx('candidate-preview', candidateFile, ['--plan', '--json'], candidateProject, 'cache-candidate')).stdout);
  assert.equal(preview.status, 'plan');
  assert.equal(preview.skills.length, 5);
  assert.deepEqual(snapshot('candidate-preview-after', candidateProject), candidateBefore);
  const installed = JSON.parse((await npx('candidate-install', candidateFile, ['--json'], candidateProject, 'cache-candidate')).stdout);
  assert.equal(installed.status, 'installed');
  assert.deepEqual(installed.commands, active.map(name => '$' + name));
  assert.equal(validateInstall(candidateProject, candidate), 34);
  await unchanged('candidate-repeat', candidateProject, candidateFile, 'cache-candidate', candidate);

  const migrate = project('migration clean');
  await npx('old-clean-install', urls['0.3.0'], ['--json'], migrate, 'cache-old');
  validateInstall(migrate, old, ['bandit', 'bandit-research', 'bandit-decide', 'bandit-specify', 'bandit-review', 'bandit-update']);
  const legacyRoot = path.join(migrate, '.agents/skills');
  fs.writeFileSync(path.join(legacyRoot, 'bandit-decide/local-note.md'), 'Synthetic unrelated retired note.\n');
  fs.mkdirSync(path.join(legacyRoot, 'bandit-decide/unrelated-empty'));
  fs.writeFileSync(path.join(legacyRoot, 'bandit-research/local-note.md'), 'Synthetic unrelated active note.\n');
  const migrationBefore = snapshot('migration-preview-before', migrate);
  const migrationPlan = JSON.parse((await npx('migration-preview', candidateFile, ['--plan', '--json'], migrate, 'cache-candidate')).stdout);
  assert.equal(migrationPlan.status, 'plan');
  assert.deepEqual(snapshot('migration-preview-after', migrate), migrationBefore);
  const migrated = JSON.parse((await npx('migration-install', candidateFile, ['--json'], migrate, 'cache-candidate')).stdout);
  assert.equal(migrated.status, 'updated');
  assert.deepEqual(migrated.migrations.map(x => x.status), ['retired', 'retired']);
  validateInstall(migrate, candidate);
  for (const name of retired) for (const file of ['SKILL.md', marker]) assert.equal(fs.existsSync(path.join(legacyRoot, name, file)), false);
  assert.equal(fs.existsSync(path.join(legacyRoot, 'bandit-update')), false);
  assert.equal(fs.readFileSync(path.join(legacyRoot, 'bandit-decide/local-note.md'), 'utf8'), 'Synthetic unrelated retired note.\n');
  assert.ok(fs.statSync(path.join(legacyRoot, 'bandit-decide/unrelated-empty')).isDirectory());
  assert.equal(fs.readFileSync(path.join(legacyRoot, 'bandit-research/local-note.md'), 'utf8'), 'Synthetic unrelated active note.\n');
  await unchanged('migration-repeat', migrate, candidateFile, 'cache-candidate', candidate);

  const conflict = project('migration customized');
  await npx('old-customized-install', urls['0.3.0'], ['--json'], conflict, 'cache-old');
  const custom = path.join(conflict, '.agents/skills/bandit-update/SKILL.md');
  fs.appendFileSync(custom, '\nSynthetic preexisting customization: preserve this line.\n');
  const conflictBefore = snapshot('conflict-before', conflict);
  const rejected = await npx('migration-conflict', candidateFile, ['--json'], conflict, 'cache-candidate', 2);
  assert.equal(JSON.parse(rejected.stdout).status, 'error');
  assert.match(JSON.parse(rejected.stdout).error, /retired skill bandit-update/);
  assert.deepEqual(snapshot('conflict-after', conflict), conflictBefore);
  assert.equal(fs.existsSync(path.join(conflict, '.agents/skills/bandit-scope')), false);

  const caches = [verifyCache('cache-public', published), verifyCache('cache-candidate', candidate), verifyCache('cache-old', old)];
  save('result.json', { status: 'pass', finished_at: new Date().toISOString(), runtime: runtime.stdout,
    inherited_environment: false, home_override: false, user_config: 'empty fixture files', stdin: 'closed',
    caches_initially_empty: true, git_and_python_on_path: false, caches, commands: runs.length,
    fixtures: ['public exact command and unchanged repeat', 'candidate preview/install/unchanged repeat',
      'authentic 0.3 migration preserves unrelated files', 'customized retired file refuses entire upgrade unchanged'],
    limitations: 'Fresh macOS Node-22 npx integration, not first-ever public installation proof, cross-platform coverage, named host discovery, product quality, or publication. Downloads are locally hashed; cache package bytes are compared to them. No hidden process syscall audit.' });
  process.stdout.write('PASS: all four integration fixtures\n');
} catch (error) {
  save('failure.json', { status: 'failed', finished_at: new Date().toISOString(), message: error.message, stack: error.stack,
    completed_command_records: runs.length, preserved_root: scratch });
  process.stderr.write(String(error.stack) + '\n');
  process.exitCode = 1;
}
