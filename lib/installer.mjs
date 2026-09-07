import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { createHash, randomBytes } from 'node:crypto';

export const NAME = 'bandit';
export const MARKER = '.bandit-install.json';
const IGNORED = new Set(['.git', '.DS_Store', '__pycache__']);
const SEMVER = /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/;
const checksum = (bytes) => createHash('sha256').update(bytes).digest('hex');
const canonical = (name) => name.normalize('NFC').toUpperCase().toLowerCase().normalize('NFC');
const own = (value, name) => Object.hasOwn(value, name);

export class InstallError extends Error {}

function info(file) {
  try { return fs.lstatSync(file); }
  catch (error) { if (error.code === 'ENOENT') return null; throw error; }
}

function absolute(value) {
  if (value === '~') return os.homedir();
  if (value.startsWith('~/') || value.startsWith('~\\')) return path.resolve(os.homedir(), value.slice(2));
  return path.resolve(value);
}

// Walk existing ancestors too: resolving a link first would hide an escaping path.
function checkPath(file) {
  const full = absolute(file);
  const parsed = path.parse(full);
  let current = parsed.root;
  const parts = full.slice(parsed.root.length).split(path.sep).filter(Boolean);
  for (let i = 0; i < parts.length; i++) {
    const parent = info(current);
    if (parent?.isDirectory()) {
      const aliases = fs.readdirSync(current).filter((entry) => canonical(entry) === canonical(parts[i]));
      if (aliases.some((entry) => entry !== parts[i])) {
        throw new InstallError(`Ambiguous case or Unicode spelling: ${path.join(current, parts[i])}`);
      }
    }
    current = path.join(current, parts[i]);
    const stat = info(current);
    if (stat?.isSymbolicLink()) throw new InstallError(`Symlink or junction is not allowed: ${current}`);
    if (i < parts.length - 1 && stat && !stat.isDirectory()) {
      throw new InstallError(`Parent path is not a directory: ${current}`);
    }
  }
  return full;
}

function regularBytes(file) {
  checkPath(file);
  if (!info(file)?.isFile()) throw new InstallError(`Expected a regular file: ${file}`);
  return fs.readFileSync(file);
}

function relativeName(name) {
  if (typeof name !== 'string' || !name || name.includes('\\') || name.includes(':') || /[\x00-\x1f]/.test(name)
    || name.split('/').some((part) => !part || part === '.' || part === '..' || /[. ]$/.test(part)
      || /^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)/i.test(part))) {
    throw new InstallError(`Unsafe relative file name: ${JSON.stringify(name)}`);
  }
  return name;
}

function treeFiles(directory) {
  checkPath(directory);
  if (!info(directory)?.isDirectory()) throw new InstallError(`Missing skill directory: ${directory}`);
  const files = new Map();
  const visit = (parent, prefix = '') => {
    const seen = new Set();
    for (const entry of fs.readdirSync(parent).sort()) {
      if (IGNORED.has(entry)) continue;
      const name = relativeName(prefix + entry);
      if (seen.has(canonical(entry))) throw new InstallError(`Case or Unicode path collision: ${name}`);
      seen.add(canonical(entry));
      const file = path.join(parent, entry);
      checkPath(file);
      const stat = info(file);
      if (stat?.isDirectory()) visit(file, `${name}/`);
      else if (stat?.isFile()) files.set(name, fs.readFileSync(file));
      else throw new InstallError(`Expected a regular file or directory: ${file}`);
    }
  };
  visit(directory);
  return files;
}

function within(first, second) {
  const a = absolute(first).split(path.sep).map(canonical);
  const b = absolute(second).split(path.sep).map(canonical);
  return b.length <= a.length && b.every((part, i) => part === a[i]);
}

function markerAt(destination) {
  const file = path.join(destination, MARKER);
  checkPath(file);
  if (!info(file)) return null;
  let marker;
  try { marker = JSON.parse(regularBytes(file).toString('utf8')); }
  catch { throw new InstallError(`Invalid ownership marker: ${file}`); }
  if (!marker || marker.format !== 1 || marker.name !== NAME || !SEMVER.test(marker.version)
    || !marker.files || typeof marker.files !== 'object' || Array.isArray(marker.files)) {
    throw new InstallError(`Unrecognized ownership marker: ${file}`);
  }
  const seen = new Map();
  for (const [name, hash] of Object.entries(marker.files)) {
    relativeName(name);
    if (canonical(name) === canonical(MARKER) || typeof hash !== 'string' || !/^[a-f0-9]{64}$/.test(hash)) {
      throw new InstallError(`Invalid managed file entry: ${name}`);
    }
    const parts = name.split('/');
    for (let i = 1; i <= parts.length; i++) {
      const part = parts.slice(0, i).join('/');
      const key = canonical(part);
      if (seen.has(key) && seen.get(key) !== part) throw new InstallError(`Ambiguous managed path: ${part}`);
      seen.set(key, part);
    }
  }
  return marker;
}

export function makePlan(packageRoot, destination) {
  packageRoot = absolute(packageRoot);
  destination = checkPath(destination);
  if (info(destination) && !info(destination).isDirectory()) throw new InstallError(`Destination is not a directory: ${destination}`);
  const source = path.join(packageRoot, 'skills', NAME);
  if (within(destination, source) || within(source, destination)) throw new InstallError('Source and destination must not overlap.');
  const payload = treeFiles(source);
  if (!payload.has('SKILL.md') || [...payload.keys()].some((name) => canonical(name) === canonical(MARKER))) {
    throw new InstallError('The package must contain SKILL.md and no installation marker.');
  }
  let version;
  try { version = JSON.parse(regularBytes(path.join(packageRoot, 'package.json'))).version; }
  catch { throw new InstallError('Cannot read the package version.'); }
  if (typeof version !== 'string' || !SEMVER.test(version)) throw new InstallError('The package must have a stable semantic version.');
  const previous = markerAt(destination);
  const oldFiles = previous?.files ?? {};
  const previousNames = new Map();
  for (const name of Object.keys(oldFiles)) {
    const parts = name.split('/');
    for (let i = 1; i <= parts.length; i++) {
      const part = parts.slice(0, i).join('/');
      previousNames.set(canonical(part), part);
    }
  }
  for (const name of payload.keys()) {
    const parts = name.split('/');
    for (let i = 1; i <= parts.length; i++) {
      const part = parts.slice(0, i).join('/');
      const old = previousNames.get(canonical(part));
      if (old && old !== part) throw new InstallError(`Case or Unicode rename needs a fresh destination: ${old} -> ${part}`);
    }
  }
  const desired = { format: 1, name: NAME, version, files: Object.fromEntries([...payload].sort(([a], [b]) => a < b ? -1 : a > b ? 1 : 0).map(([name, bytes]) => [name, checksum(bytes)])) };
  const changes = [];
  const conflicts = [];
  let unchanged = 0;
  for (const name of [...new Set([...Object.keys(oldFiles), ...payload.keys()])].sort()) {
    const target = path.join(destination, ...name.split('/'));
    checkPath(target);
    const stat = info(target);
    if (stat && !stat.isFile()) { conflicts.push(`not a regular file: ${name}`); continue; }
    const current = stat ? checksum(regularBytes(target)) : null;
    const old = own(oldFiles, name) ? oldFiles[name] : null;
    const next = own(desired.files, name) ? desired.files[name] : null;
    if (current !== null && old === null) conflicts.push(`unmanaged file: ${name}`);
    else if (next !== null && current === next) unchanged++;
    else if (next !== null && current === null && old === null) changes.push({ action: 'add', path: name });
    else if (next !== null && current === old && current !== null) changes.push({ action: 'update', path: name });
    else if (next === null && current === null) continue;
    else if (next === null && current === old) changes.push({ action: 'remove', path: name });
    else conflicts.push(`locally modified or deleted file: ${name}`);
  }
  if (conflicts.length) throw new InstallError(`Nothing installed. Preserve or move the conflicting files, then retry:\n  ${conflicts.join('\n  ')}`);
  const marker = Buffer.from(`${JSON.stringify(desired, null, 2)}\n`);
  const markerChange = !previous || previous.version !== version
    || Object.keys(previous.files).length !== payload.size
    || Object.entries(desired.files).some(([name, hash]) => previous.files[name] !== hash);
  return { report: { status: 'plan', source, destination, version, managed: previous !== null, changes,
    unchanged_files: unchanged, marker_change: markerChange }, payload, marker };
}

function atomicWrite(file, bytes) {
  checkPath(file);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  checkPath(file);
  const temporary = path.join(path.dirname(file), `.bandit-${randomBytes(12).toString('hex')}.tmp`);
  try {
    fs.writeFileSync(temporary, bytes, { flag: 'wx', mode: 0o644 });
    checkPath(file);
    fs.renameSync(temporary, file);
  } finally { if (info(temporary)) fs.unlinkSync(temporary); }
}

const same = (a, b) => a === null ? b === null : b !== null && a.equals(b);
const existingBytes = (file) => info(file) ? regularBytes(file) : null;

export function installInto(packageRoot, destination, dryRun = false) {
  destination = absolute(destination);
  let plan = makePlan(packageRoot, destination);
  if (dryRun) return plan.report;
  if (!plan.report.changes.length && !plan.report.marker_change) return { ...plan.report, status: 'unchanged' };
  checkPath(path.dirname(destination));
  fs.mkdirSync(path.dirname(destination), { recursive: true });
  const lock = path.join(path.dirname(destination), `.${path.basename(destination)}.bandit.lock`);
  checkPath(lock);
  let lockFd;
  try { lockFd = fs.openSync(lock, 'wx', 0o600); }
  catch (error) {
    if (error.code === 'EEXIST') throw new InstallError(`Another installation may be running. Lock: ${lock}`);
    throw error;
  }
  fs.closeSync(lockFd);
  try {
    plan = makePlan(packageRoot, destination);
    const operations = plan.report.changes.map((item) => ({
      file: path.join(destination, ...item.path.split('/')),
      next: item.action === 'remove' ? null : plan.payload.get(item.path),
    }));
    operations.push({ file: path.join(destination, MARKER), next: plan.marker });
    for (const operation of operations) operation.old = existingBytes(operation.file);
    const applied = [];
    try {
      for (const operation of operations) {
        if (!same(existingBytes(operation.file), operation.old)) throw new InstallError(`Destination changed during installation: ${operation.file}`);
        if (operation.next === null) fs.unlinkSync(operation.file);
        else atomicWrite(operation.file, operation.next);
        applied.push(operation);
      }
    } catch (error) {
      // Restore only our own bytes. A concurrent editor's changes take precedence.
      for (const operation of applied.reverse()) {
        try {
          if (!same(existingBytes(operation.file), operation.next)) continue;
          if (operation.old === null) fs.unlinkSync(operation.file);
          else atomicWrite(operation.file, operation.old);
        } catch { /* Keep the original error; do not force overwrites during recovery. */ }
      }
      throw error;
    }
    return { ...plan.report, status: plan.report.managed ? 'updated' : 'installed' };
  } finally { fs.unlinkSync(lock); }
}

const HELP = `BANDIT — an outlaw with a plan.

Usage: bandit [install] [options]

Run in a project to install into .agents/skills/bandit. No questions asked.

  --global       Install for all Codex projects ($CODEX_HOME/skills/bandit,
                 or ~/.codex/skills/bandit when CODEX_HOME is unset)
  --repo PATH    Install into PATH/.agents/skills/bandit
  --dest PATH    Install into this exact skill directory
  --plan         Preview changes without writing files
  --json         Print a machine-readable result
  --help, -h     Show this help
  --version, -v  Show the version

Try: npx --yes https://github.com/ch4570/bandit/releases/download/v0.2.0/bandit.tgz
Then ask your agent: $bandit Turn this app idea into a focused MVP plan.
`;

export function runCli(argv, { packageRoot, cwd = process.cwd(), env = process.env, home = os.homedir(),
  stdout = process.stdout, stderr = process.stderr } = {}) {
  let json = argv.includes('--json');
  try {
    if (Number(process.versions.node.split('.')[0]) < 22) throw new InstallError('BANDIT needs Node.js 22 or newer.');
    const args = [...argv];
    if (args[0] === 'install') args.shift();
    const options = {};
    while (args.length) {
      const flag = args.shift();
      if (['--help', '-h'].includes(flag)) { stdout.write(HELP); return 0; }
      if (['--version', '-v'].includes(flag)) {
        stdout.write(`${JSON.parse(regularBytes(path.join(packageRoot, 'package.json'))).version}\n`); return 0;
      }
      if (['--global', '--plan', '--json'].includes(flag)) options[flag.slice(2)] = true;
      else if (['--repo', '--dest'].includes(flag)) {
        if (!args[0] || args[0].startsWith('--') || own(options, flag.slice(2))) throw new InstallError(`${flag} needs one path.`);
        options[flag.slice(2)] = args.shift();
      } else throw new InstallError(`Unknown argument: ${flag}. Run bandit --help.`);
    }
    json = options.json ?? false;
    if (['global', 'repo', 'dest'].filter((key) => own(options, key)).length > 1) {
      throw new InstallError('Use only one of --global, --repo, or --dest.');
    }
    const fromCwd = (value) => value.startsWith('~') ? absolute(value) : path.resolve(cwd, value);
    let destination;
    if (options.global) destination = path.join(env.CODEX_HOME?.trim() ? fromCwd(env.CODEX_HOME) : path.join(home, '.codex'), 'skills', NAME);
    else if (options.dest) destination = fromCwd(options.dest);
    else {
      const repo = checkPath(options.repo ? fromCwd(options.repo) : cwd);
      if (!info(repo)?.isDirectory()) throw new InstallError(`Project directory does not exist: ${repo}`);
      destination = path.join(repo, '.agents', 'skills', NAME);
    }
    const report = installInto(packageRoot, destination, Boolean(options.plan));
    const legacy = path.join(path.dirname(destination), 'pm-craft');
    if (info(legacy)?.isDirectory()) report.notes = ['A separate pm-craft installation exists. BANDIT leaves it untouched; remove it manually if you no longer need it.'];
    if (json) stdout.write(`${JSON.stringify(report, null, 2)}\n`);
    else {
      const label = { installed: 'BANDIT is ready.', updated: 'BANDIT is updated.', unchanged: 'BANDIT is already up to date.', plan: 'BANDIT installation preview.' }[report.status];
      stdout.write(`${label}\n${report.destination}\n`);
      if (report.status === 'plan') stdout.write(`${report.changes.length} file changes; nothing written.\n`);
      else stdout.write('\nOpen or restart your agent, then try:\n$bandit Turn this app idea into a focused MVP plan.\n');
      for (const note of report.notes ?? []) stdout.write(`\n${note}\n`);
    }
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    if (json) stdout.write(`${JSON.stringify({ status: 'error', error: message })}\n`);
    else stderr.write(`BANDIT: ${message}\n`);
    return 2;
  }
}
