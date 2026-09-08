#!/usr/bin/env node
/** Validate distributable skill metadata and references using Node alone. */
import { lstat, readFile, readdir, realpath } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const NAME = 'bandit';
export const SKILL_NAMES = [NAME, 'bandit-research', 'bandit-decide', 'bandit-specify', 'bandit-review', 'bandit-update'];
const PACKAGE_NAME = '@ch4570/bandit';
const CHECKS = 'structure and references only; no claim of PM effectiveness';

function scalar(raw) {
  const value = raw.trim();
  if (value.startsWith('"')) return JSON.parse(value);
  if (value.startsWith("'") && value.endsWith("'")) return value.slice(1, -1).replaceAll("''", "'");
  if (value === 'true' || value === 'false') return value === 'true';
  if (!value || /^[\[\{&*!]/u.test(value)) throw new Error('Use plain or quoted scalar metadata');
  return value;
}

/** The mapping/scalar YAML subset used here; reject unsupported syntax explicitly. */
export function yamlMapping(text) {
  const result = Object.create(null);
  const stack = [{ indent: -1, value: result }];
  const lines = text.split(/\r?\n/u);
  for (let index = 0; index < lines.length; index += 1) {
    const line = lines[index];
    if (!line.trim() || line.trimStart().startsWith('#')) continue;
    if (line.includes('\t')) throw new Error('Metadata indentation must use spaces');
    const match = /^( *)([A-Za-z_][\w-]*):(?: +(.*))?$/u.exec(line);
    if (!match) throw new Error(`Unsupported metadata syntax: ${line}`);
    const [, spaces, key, value] = match;
    while (stack.at(-1).indent >= spaces.length) stack.pop();
    const mapping = stack.at(-1).value;
    if (Object.hasOwn(mapping, key)) throw new Error(`Duplicate metadata key: ${key}`);
    if (value === undefined) {
      mapping[key] = Object.create(null);
      stack.push({ indent: spaces.length, value: mapping[key] });
    } else if (['|', '>', '|-', '>-'].includes(value)) {
      const block = [];
      while (index + 1 < lines.length && (!lines[index + 1].trim() || /^ */u.exec(lines[index + 1])[0].length > spaces.length)) {
        block.push(lines[++index].trim());
      }
      mapping[key] = block.join(value.startsWith('>') ? ' ' : '\n').trim();
    } else {
      mapping[key] = scalar(value);
    }
  }
  return result;
}

function frontmatter(text) {
  const lines = text.split(/\r?\n/u);
  if (lines[0] !== '---') throw new Error('SKILL.md must start with YAML frontmatter');
  const end = lines.indexOf('---', 1);
  if (end < 0) throw new Error('Unterminated frontmatter');
  return yamlMapping(lines.slice(1, end).join('\n'));
}

function inside(candidate, boundary) {
  const relative = path.relative(boundary, candidate);
  return relative === '' || (!relative.startsWith(`..${path.sep}`) && relative !== '..' && !path.isAbsolute(relative));
}

async function regularFile(filename) {
  const info = await lstat(filename);
  if (!info.isFile() || info.isSymbolicLink()) throw new Error(`Expected a regular file: ${filename}`);
  return readFile(filename, 'utf8');
}

async function skillFiles(directory, errors) {
  const files = new Map();
  const names = new Set();
  async function visit(current) {
    const info = await lstat(current);
    if (info.isSymbolicLink()) throw new Error(`Skill may not contain a symlink: ${current}`);
    if (!info.isDirectory()) throw new Error(`Expected a skill directory: ${current}`);
    for (const entry of await readdir(current, { withFileTypes: true })) {
      if (['.git', '__pycache__', '.DS_Store'].includes(entry.name)) continue;
      const filename = path.join(current, entry.name);
      const relative = path.relative(directory, filename).split(path.sep).join('/');
      const normalized = relative.normalize('NFC').toLowerCase();
      if (names.has(normalized)) throw new Error(`Case-insensitive path collision: ${relative}`);
      names.add(normalized);
      if (entry.isSymbolicLink()) throw new Error(`Skill may not contain a symlink: ${relative}`);
      if (entry.isDirectory()) await visit(filename);
      else if (entry.isFile()) files.set(relative, filename);
      else throw new Error(`Skill contains a non-regular file: ${relative}`);
    }
  }
  try { await visit(directory); } catch (error) { errors.push(error.message); }
  return files;
}

function withoutFences(text) {
  const result = [];
  let fence = null;
  for (const line of text.split(/\r?\n/u)) {
    const marker = /^\s*(`{3,}|~{3,})/u.exec(line)?.[1];
    if (fence) {
      if (marker?.[0] === fence[0] && marker.length >= fence.length) fence = null;
      continue;
    }
    if (marker) fence = marker;
    else result.push(line);
  }
  return result.join('\n');
}

async function localReferences(filename, text, boundary, errors) {
  const prose = withoutFences(text);
  const links = [...prose.matchAll(/!?\[[^\]\n]*\]\(([^)\n]+)\)/gu)].map((match) => match[1]);
  links.push(...[...prose.matchAll(/`((?:references|assets|agents)\/[^`]+)`/gu)].map((match) => match[1]));
  for (const raw of links) {
    let target = raw.trim();
    target = target.startsWith('<') && target.includes('>') ? target.slice(1, target.indexOf('>')) : target.split(/ ["']/u)[0];
    if (/^[A-Za-z][A-Za-z\d+.-]*:/u.test(target) || target.startsWith('//')) continue;
    try {
      target = decodeURIComponent(target.split(/[?#]/u)[0]);
      if (!target || /[*{}<>]/u.test(target)) continue;
      const resolved = path.resolve(path.dirname(filename), target);
      if (!inside(resolved, boundary)) {
        errors.push(`${path.basename(filename)}: local reference leaves its package: ${target}`);
      } else {
        try {
          if (!inside(await realpath(resolved), boundary)) errors.push(`${path.basename(filename)}: local reference leaves its package: ${target}`);
        } catch (error) {
          if (error.code === 'ENOENT') errors.push(`${path.basename(filename)}: missing local reference: ${target}`);
          else throw error;
        }
      }
    } catch (error) { errors.push(`${path.basename(filename)}: ${error.message}`); }
  }
}

async function validateSkill(root, name) {
  const errors = [];
  const skill = path.join(root, 'skills', name);
  const files = await skillFiles(skill, errors);
  try {
    const metadata = frontmatter(await regularFile(path.join(skill, 'SKILL.md')));
    if (metadata.name !== name) errors.push(`SKILL.md name must match the ${name} directory`);
    if (typeof metadata.description !== 'string' || !metadata.description.trim()) errors.push('SKILL.md needs a nonempty description');
  } catch (error) { errors.push(`SKILL.md: ${error.message}`); }
  try {
    const ui = yamlMapping(await regularFile(path.join(skill, 'agents/openai.yaml')));
    const face = ui.interface ?? {};
    for (const field of ['display_name', 'short_description', 'default_prompt']) {
      if (typeof face[field] !== 'string' || !face[field].trim()) errors.push(`agents/openai.yaml: interface.${field} is required`);
    }
    const displayName = name === NAME ? 'BANDIT' : `BANDIT ${name.slice(7, 8).toUpperCase()}${name.slice(8)}`;
    if (face.display_name !== displayName) errors.push(`agents/openai.yaml: display_name must be ${displayName}`);
    if (typeof face.default_prompt !== 'string' || !face.default_prompt.match(/\$[a-z][a-z0-9-]*/gu)?.includes(`$${name}`)) errors.push(`agents/openai.yaml: default_prompt must mention $${name}`);
    for (const field of ['icon_small', 'icon_large']) {
      if (face[field] !== undefined) {
        const icon = typeof face[field] === 'string' ? path.resolve(skill, face[field]) : '';
        if (!icon || !inside(icon, skill) || !files.has(path.relative(skill, icon).split(path.sep).join('/'))) errors.push(`agents/openai.yaml: ${field} must resolve inside the skill`);
      }
    }
  } catch (error) { errors.push(`agents/openai.yaml: ${error.message}`); }
  for (const [relative, filename] of files) {
    if (relative.endsWith('.md')) {
      try {
        const text = await regularFile(filename);
        if (/\bpm-craft\b|\bPM Craft\b/u.test(text)) errors.push(`${relative}: previous product identity remains in the active skill`);
        await localReferences(filename, text, skill, errors);
      } catch (error) { errors.push(`${relative}: ${error.message}`); }
    }
  }
  return { name, skillFiles: files.size, errors: errors.map((error) => `${name}/${error}`) };
}

export async function validateDistribution(directory = ROOT) {
  const errors = [];
  let root;
  try { root = await realpath(directory); } catch (error) { return { ok: false, errors: [error.message], checks: CHECKS }; }
  let version;
  try {
    version = (await regularFile(path.join(root, 'VERSION'))).trim();
    if (!/^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/u.test(version)) errors.push('VERSION must be a stable semantic version');
  } catch (error) { errors.push(error.message); }
  try {
    const pkg = JSON.parse(await regularFile(path.join(root, 'package.json')));
    if (pkg.name !== PACKAGE_NAME) errors.push(`package.json name must be ${PACKAGE_NAME}`);
    if (pkg.version !== version) errors.push('package.json version must match VERSION');
    if (typeof pkg.bin?.bandit !== 'string') errors.push('package.json must expose the bandit command');
    else {
      const binary = path.resolve(root, pkg.bin.bandit);
      if (!inside(binary, root) || !inside(await realpath(binary), root)) errors.push('bandit binary must resolve inside the package');
      else if (!(await regularFile(binary)).startsWith('#!/usr/bin/env node')) errors.push('bandit binary must use the Node entrypoint');
    }
    for (const hook of ['preinstall', 'install', 'postinstall', 'prepare']) {
      if (pkg.scripts?.[hook]) errors.push(`package.json must not require a ${hook} lifecycle hook`);
    }
  } catch (error) { errors.push(`package.json: ${error.message}`); }
  const skills = [];
  for (const name of SKILL_NAMES) {
    const result = await validateSkill(root, name);
    skills.push({ name, skillFiles: result.skillFiles });
    errors.push(...result.errors);
  }
  return { ok: errors.length === 0, version, skillFiles: skills.reduce((total, skill) => total + skill.skillFiles, 0), skills, errors, checks: CHECKS };
}

async function main() {
  const args = process.argv.slice(2);
  if (args.length && (args.length !== 2 || args[0] !== '--root')) {
    process.stderr.write('Usage: node scripts/validate-node.mjs [--root PATH]\n');
    process.exitCode = 2;
    return;
  }
  const report = await validateDistribution(args[1] ?? ROOT);
  process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
  process.exitCode = report.ok ? 0 : 1;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) await main();
