// One-off bounded offline integration receipt, adapted from round9 npx-flow-v2.mjs.
// Local archives only. Retain scratch originals and mirrored evidence; never delete them.
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { gunzipSync } from 'node:zlib';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const harness = fileURLToPath(import.meta.url), checks = path.dirname(harness);
const freeze = JSON.parse(fs.readFileSync(path.join(checks, 'before-run.json')));
const hash = bytes => createHash('sha256').update(bytes).digest('hex');
assert.equal(process.version, freeze.node_version);
for (const [name, digest] of Object.entries(freeze.source_files_sha256))
  assert.equal(hash(fs.readFileSync(path.join(freeze.repo, name))), digest, `source changed before run: ${name}`);
const candidateFile = freeze.archives[0].file, oldFile = freeze.archives[1].file;
const archiveDirectory = path.join(checks, 'attempt1');
assert.equal(fs.existsSync(archiveDirectory), false, 'Do not overwrite an earlier attempt');
const scratch = fs.mkdtempSync('/TEMP/bandit-round14-');
assert.equal(fs.realpathSync(scratch), scratch);
const active = ['bandit', 'bandit-research', 'bandit-scope', 'bandit-specify', 'bandit-review'];
const oldNames = ['bandit', 'bandit-research', 'bandit-decide', 'bandit-specify', 'bandit-review', 'bandit-update'];
const marker = '.bandit-install.json', note = '# Synthetic integration project\nPreserve this note.\n';
const runs = [];
const space = () => { const st = fs.statfsSync(scratch); return Number(st.bavail) * Number(st.bsize); };
const save = (name, value) => {
  const bytes = typeof value === 'string' || Buffer.isBuffer(value) ? value : JSON.stringify(value, null, 2) + '\n';
  for (const root of [scratch, archiveDirectory]) {
    fs.mkdirSync(path.dirname(path.join(root, name)), { recursive: true });
    fs.writeFileSync(path.join(root, name), bytes, { flag: 'wx' });
  }
};
for (const dir of ['bin', 'tmp', 'projects', 'cache-candidate', 'cache-old']) fs.mkdirSync(path.join(scratch, dir));
for (const [name, target] of [['node', process.execPath], ['npm', path.join(freeze.npm_bin_directory, 'npm-cli.js')],
  ['npx', path.join(freeze.npm_bin_directory, 'npx-cli.js')], ['sh', '/bin/sh']]) fs.symlinkSync(target, path.join(scratch, 'bin', name));
for (const name of ['empty-user.npmrc', 'empty-global.npmrc']) fs.writeFileSync(path.join(scratch, name), '', { flag: 'wx' });
const environment = cache => ({
  PATH: path.join(scratch, 'bin'), TMPDIR: path.join(scratch, 'tmp'),
  npm_config_cache: path.join(scratch, cache), npm_config_offline: 'true',
  npm_config_userconfig: path.join(scratch, 'empty-user.npmrc'),
  npm_config_globalconfig: path.join(scratch, 'empty-global.npmrc'),
  npm_config_audit: 'false', npm_config_fund: 'false', npm_config_progress: 'false',
  npm_config_update_notifier: 'false', npm_config_fetch_retries: '0', npm_config_script_shell: '/bin/sh',
});

async function command(label, executable, args, cwd, cache, expected = 0) {
  assert.ok(space() >= 80 * 1024 * 1024, 'Stop before another command: less than 80 MiB available');
  const index = String(runs.length + 1).padStart(2, '0');
  const record = { label, executable, args, cwd, cache, started_at_utc: new Date().toISOString(),
    stdin: 'closed', shell: false, available_bytes_before: space() };
  process.stdout.write(`START ${index} ${label}\n`);
  const result = await new Promise(resolve => {
    const child = spawn(executable, args, { cwd, env: environment(cache), stdio: ['ignore', 'pipe', 'pipe'] });
    let stdout = '', stderr = '', launch_error = null;
    child.stdout.on('data', bytes => { stdout += bytes; });
    child.stderr.on('data', bytes => { stderr += bytes; });
    child.on('error', error => { launch_error = error.message; });
    const deadline = setTimeout(() => child.kill('SIGTERM'), 45000);
    child.on('close', (exit_code, signal) => {
      clearTimeout(deadline); resolve({ stdout, stderr, exit_code, signal, launch_error });
    });
  });
  Object.assign(record, result, { finished_at_utc: new Date().toISOString(), available_bytes_after: space() });
  save(`logs/${index}-${label}.json`, record); runs.push(record);
  process.stdout.write(`END ${index} ${label}: ${result.exit_code}\n`);
  assert.equal(result.launch_error, null, `${label}: launch error`);
  assert.equal(result.signal, null, `${label}: terminated`);
  assert.equal(result.exit_code, expected, `${label}: ${result.stderr || result.stdout}`);
  return result;
}
const npx = (label, file, options, project, expected = 0) => command(label, path.join(scratch, 'bin/npx'),
  ['--yes', '--offline', '--cache=' + path.join(scratch, file === oldFile ? 'cache-old' : 'cache-candidate'),
    '--package=' + file, '--', 'bandit', ...options], project, file === oldFile ? 'cache-old' : 'cache-candidate', expected);

function unpack(record) {
  const bytes = fs.readFileSync(record.file); assert.equal(hash(bytes), record.sha256);
  const tar = gunzipSync(bytes), files = new Map();
  for (let offset = 0; offset + 512 <= tar.length;) {
    const header = tar.subarray(offset, offset + 512); if (header.every(x => x === 0)) break;
    const text = (start, size) => header.subarray(start, start + size).toString('utf8').split('\0')[0];
    const name = [text(345, 155), text(0, 100)].filter(Boolean).join('/');
    const size = parseInt(text(124, 12).trim(), 8) || 0, type = text(156, 1);
    assert.ok(name.startsWith('package/') && !name.split('/').some(p => ['.', '..', ''].includes(p)), name);
    assert.ok(['', '0'].includes(type), `Unexpected archive type ${type}: ${name}`);
    assert.ok(offset + 512 + size <= tar.length, 'Truncated member');
    const relative = name.slice(8); assert.equal(files.has(relative), false, 'Duplicate member');
    files.set(relative, tar.subarray(offset + 512, offset + 512 + size));
    offset += 512 + Math.ceil(size / 512) * 512;
  }
  assert.deepEqual(Object.fromEntries([...files].map(([name, bytes]) => [name, hash(bytes)])), record.package_files_sha256);
  const manifest = JSON.parse(files.get('package.json'));
  assert.equal(manifest.name, '@ch4570/bandit'); assert.equal(manifest.bin.bandit, 'bin/bandit.mjs');
  assert.equal(Object.keys(manifest.dependencies ?? {}).length, 0);
  for (const hook of ['preinstall', 'install', 'postinstall', 'prepare', 'prepublish', 'prepublishOnly'])
    assert.equal(manifest.scripts?.[hook], undefined, `Lifecycle hook ${hook}`);
  return { ...record, files, manifest };
}
function inventory(root) {
  const result = {};
  const visit = (target, relative) => {
    const st = fs.lstatSync(target, { bigint: true });
    assert.ok(st.isFile() || st.isDirectory(), `Unexpected object ${target}`);
    result[relative] = { type: st.isDirectory() ? 'directory' : 'file', mode: Number(st.mode),
      device: String(st.dev), inode: String(st.ino), mtime_ns: String(st.mtimeNs), ctime_ns: String(st.ctimeNs) };
    if (st.isDirectory()) for (const name of fs.readdirSync(target).sort()) visit(path.join(target, name), relative === '.' ? name : `${relative}/${name}`);
    else Object.assign(result[relative], { bytes: Number(st.size), sha256: hash(fs.readFileSync(target)) });
  };
  visit(root, '.'); return result;
}
const snapshot = (label, root) => { const value = inventory(root); save(`snapshots/${label}.json`, value); return value; };
const project = name => {
  const root = path.join(scratch, 'projects', name); fs.mkdirSync(root);
  fs.writeFileSync(path.join(root, 'project-note.md'), note, { flag: 'wx' }); return root;
};
function validateInstall(root, archive, coreName = 'bandit', extras = {}) {
  const skillRoot = coreName === 'bandit' ? '.agents/skills' : 'custom skills';
  const files = new Map([['project-note.md', Buffer.from(note)]]), markers = new Map(), directories = new Set(['.']);
  for (const name of archive.manifest.version === '0.3.0' ? oldNames : active) {
    const prefix = `skills/${name}/`, dest = `${skillRoot}/${name === 'bandit' ? coreName : name}`;
    const payload = [...archive.files].filter(([p]) => p.startsWith(prefix));
    const owned = Object.fromEntries(payload.map(([p, b]) => [p.slice(prefix.length), hash(b)]).sort());
    for (const [p, bytes] of payload) files.set(`${dest}/${p.slice(prefix.length)}`, bytes);
    markers.set(`${dest}/${marker}`, { format: 1, name, version: archive.manifest.version, files: owned });
  }
  for (const [name, value] of Object.entries(extras)) value === null ? directories.add(name) : files.set(name, Buffer.from(value));
  for (const name of [...files.keys(), ...markers.keys(), ...directories]) {
    let parent = path.posix.dirname(name); while (parent !== '.') { directories.add(parent); parent = path.posix.dirname(parent); }
  }
  const actual = inventory(root);
  assert.deepEqual(Object.keys(actual).sort(), [...files.keys(), ...markers.keys(), ...directories].sort(), 'Complete project path set');
  for (const name of directories) assert.equal(actual[name].type, 'directory', name);
  for (const [name, bytes] of files) {
    assert.equal(actual[name].type, 'file', name); assert.equal(actual[name].sha256, hash(bytes), name);
    assert.equal(actual[name].bytes, bytes.length, name);
  }
  for (const [name, expected] of markers) assert.deepEqual(JSON.parse(fs.readFileSync(path.join(root, name))), expected, name);
  return { root, core_name: coreName, files: files.size + markers.size, directories_including_root: directories.size };
}
async function repeat(label, root, options, text = false) {
  const before = snapshot(label + '-before', root);
  const raw = await npx(label, candidateFile, [...options, ...(text ? [] : ['--json'])], root);
  if (text) { assert.match(raw.stdout, /already up to date/); assert.doesNotMatch(raw.stdout, /separate pm-craft/); }
  else assert.equal(JSON.parse(raw.stdout).status, 'unchanged');
  assert.deepEqual(snapshot(label + '-after', root), before, 'Repeat changed an inventoried field');
}
function verifyCache(cache, archive) {
  const npxRoot = path.join(scratch, cache, '_npx');
  const roots = fs.readdirSync(npxRoot).map(name => path.join(npxRoot, name, 'node_modules/@ch4570/bandit')).filter(p => fs.existsSync(p));
  assert.equal(roots.length, 1); const root = roots[0], actual = inventory(root), dirs = new Set(['.']);
  for (const name of archive.files.keys()) { let dir = path.posix.dirname(name); while (dir !== '.') { dirs.add(dir); dir = path.posix.dirname(dir); } }
  assert.deepEqual(Object.keys(actual).sort(), [...archive.files.keys(), ...dirs].sort(), 'Complete cache package path set');
  for (const [name, bytes] of archive.files) { assert.equal(actual[name].type, 'file'); assert.equal(actual[name].sha256, hash(bytes), name); }
  for (const name of dirs) assert.equal(actual[name].type, 'directory');
  return { cache, root, files: archive.files.size, directories_including_root: dirs.size, archive_sha256: archive.sha256 };
}

try {
  const candidate = unpack(freeze.archives[0]), old = unpack(freeze.archives[1]);
  save('sources.json', { scratch, candidate: freeze.archives[0], old: freeze.archives[1],
    before_run_sha256: hash(fs.readFileSync(path.join(checks, 'before-run.json'))), harness_sha256: hash(fs.readFileSync(harness)),
    environment: environment('cache-candidate'), environment_inherited: false, home_or_codex_home_override: false,
    initially_empty_caches: ['cache-candidate', 'cache-old'], available_bytes: space() });
  const runtime = await command('runtime', '/bin/sh', ['-c', 'set -e; node --version; npm --version; command -v node; command -v npm; command -v npx; if command -v git || command -v python || command -v python3; then exit 9; fi'], scratch, 'cache-candidate');
  const verified = [];
  const normal = project('default 한글 project'), before = snapshot('default-plan-before', normal);
  assert.equal(JSON.parse((await npx('default-plan', candidateFile, ['--plan', '--json'], normal)).stdout).status, 'plan');
  assert.deepEqual(snapshot('default-plan-after', normal), before);
  const installed = JSON.parse((await npx('default-install', candidateFile, ['--json'], normal)).stdout);
  assert.equal(installed.status, 'installed'); assert.deepEqual(installed.commands, active.map(n => '$' + n));
  verified.push(validateInstall(normal, candidate)); await repeat('default-repeat', normal, []);
  for (const [label, core] of [['lowercase', 'pm-craft'], ['mixed-case', 'PM-Craft']]) {
    const root = project(label), dest = path.join(root, 'custom skills', core);
    const report = JSON.parse((await npx(label + '-install', candidateFile, ['--dest', dest, '--json'], root)).stdout);
    assert.equal(report.status, 'installed'); assert.equal(report.destination, dest); assert.equal(report.notes, undefined);
    verified.push(validateInstall(root, candidate, core)); await repeat(label + '-repeat', root, ['--dest', dest], true);
    const previous = snapshot(label + '-plan-before', root);
    const plan = JSON.parse((await npx(label + '-plan', candidateFile, ['--dest', dest, '--plan', '--json'], root)).stdout);
    assert.equal(plan.status, 'plan'); assert.equal(plan.notes, undefined);
    assert.deepEqual(snapshot(label + '-plan-after', root), previous);
  }
  const sibling = project('genuine sibling'), legacy = path.join(sibling, 'custom skills/pm-craft');
  fs.mkdirSync(legacy, { recursive: true });
  const sentinel = 'Synthetic genuine PM Craft installation. Preserve these bytes.\n';
  fs.writeFileSync(path.join(legacy, 'SKILL.md'), sentinel, { flag: 'wx' });
  const legacyBefore = snapshot('legacy-before', legacy), siblingBefore = snapshot('sibling-plan-before', sibling);
  for (const [label, options] of [['sibling-plan', ['--plan']], ['sibling-install', []]]) {
    const report = JSON.parse((await npx(label, candidateFile, ['--dest', path.join(sibling, 'custom skills/core-planner'), ...options, '--json'], sibling)).stdout);
    assert.match(report.notes[0], /separate pm-craft/);
    if (options.length) assert.deepEqual(snapshot('sibling-plan-after', sibling), siblingBefore);
  }
  assert.deepEqual(snapshot('legacy-after', legacy), legacyBefore);
  verified.push(validateInstall(sibling, candidate, 'core-planner', { 'custom skills/pm-craft/SKILL.md': sentinel }));
  const clean = project('migration clean');
  await npx('old-clean-install', oldFile, ['--json'], clean); validateInstall(clean, old);
  const extras = { '.agents/skills/bandit-decide/local-note.md': 'Synthetic unrelated retired note.\n',
    '.agents/skills/bandit-decide/unrelated-empty': null, '.agents/skills/bandit-research/local-note.md': 'Synthetic unrelated active note.\n' };
  for (const [name, value] of Object.entries(extras)) value === null ? fs.mkdirSync(path.join(clean, name)) : fs.writeFileSync(path.join(clean, name), value, { flag: 'wx' });
  const cleanBefore = snapshot('migration-plan-before', clean);
  assert.equal(JSON.parse((await npx('migration-plan', candidateFile, ['--plan', '--json'], clean)).stdout).status, 'plan');
  assert.deepEqual(snapshot('migration-plan-after', clean), cleanBefore);
  const migrated = JSON.parse((await npx('migration-install', candidateFile, ['--json'], clean)).stdout);
  assert.equal(migrated.status, 'updated'); assert.deepEqual(migrated.migrations.map(x => x.status), ['retired', 'retired']);
  verified.push(validateInstall(clean, candidate, 'bandit', extras)); await repeat('migration-repeat', clean, []);
  const conflict = project('migration customized');
  await npx('old-customized-install', oldFile, ['--json'], conflict); validateInstall(conflict, old);
  fs.appendFileSync(path.join(conflict, '.agents/skills/bandit-update/SKILL.md'), '\nSynthetic preexisting customization: preserve this line.\n');
  const conflictBefore = snapshot('conflict-before', conflict);
  for (const [label, options] of [['conflict-plan', ['--plan']], ['conflict-install', []]]) {
    const rejected = JSON.parse((await npx(label, candidateFile, [...options, '--json'], conflict, 2)).stdout);
    assert.equal(rejected.status, 'error'); assert.match(rejected.error, /retired skill bandit-update/);
    assert.deepEqual(snapshot(label + '-after', conflict), conflictBefore);
  }
  const caches = [verifyCache('cache-candidate', candidate), verifyCache('cache-old', old)];
  const sourceAfter = Object.fromEntries(Object.keys(freeze.source_files_sha256).map(name => [name, hash(fs.readFileSync(path.join(freeze.repo, name)))]));
  assert.deepEqual(sourceAfter, freeze.source_files_sha256, 'Frozen source files changed');
  for (const record of freeze.archives) assert.equal(hash(fs.readFileSync(record.file)), record.sha256);
  save('result.json', { status: 'pass', finished_at_utc: new Date().toISOString(), scratch, runtime: runtime.stdout,
    commands: runs.length, command_exit_codes: runs.map(r => r.exit_code), verified_project_inventories: verified,
    conflict_recorded_paths_including_root: Object.keys(conflictBefore).length, caches, source_after_sha256: sourceAfter,
    available_bytes_at_end: space(), minimum_recorded_available_bytes: Math.min(...runs.flatMap(r => [r.available_bytes_before, r.available_bytes_after])),
    limitations: 'Offline local-tarball macOS integration only; no public/network availability, cross-platform behavior, native skill discovery, PM quality or publication claim. Explicit npm offline/config/PATH settings are not a syscall/network sandbox audit. Tree comparisons include types, bytes/hashes, modes, device/inode, mtime and ctime, but not atime/xattrs.' });
  process.stdout.write(`PASS: six fixtures; ${runs.length} commands; scratch ${scratch}\n`);
} catch (error) {
  save('failure.json', { status: 'failed', finished_at_utc: new Date().toISOString(), message: error.message, stack: error.stack,
    completed_command_records: runs.length, scratch, available_bytes: space() });
  process.stderr.write(String(error.stack) + '\n'); process.exitCode = 1;
}
