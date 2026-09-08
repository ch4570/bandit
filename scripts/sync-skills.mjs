#!/usr/bin/env node
/** Copy the reference closure so every specialist is independently usable. */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const canonical = path.join(root, 'skills', 'bandit');
const specialists = ['research', 'scope', 'specify', 'review'];
const check = process.argv.slice(2).includes('--check');
if (process.argv.slice(2).some((arg) => arg !== '--check')) {
  throw new Error('Usage: node scripts/sync-skills.mjs [--check]');
}

function references(text, relative) {
  return [...text.matchAll(/!?\[[^\]\n]*\]\(([^)\n]+)\)/gu)].flatMap(([, target]) => {
    if (/^[a-z][a-z\d+.-]*:/iu.test(target) || target.startsWith('#')) return [];
    const resolved = path.posix.normalize(path.posix.join(path.posix.dirname(relative), target.split('#')[0]));
    if (!/^(references|assets)\//u.test(resolved)) throw new Error(`Unexpected resource link: ${relative} -> ${target}`);
    return [resolved];
  });
}

let count = 0;
const failures = [];
for (const suffix of specialists) {
  const skill = path.join(root, 'skills', `bandit-${suffix}`);
  const queue = references(fs.readFileSync(path.join(skill, 'SKILL.md'), 'utf8'), 'SKILL.md');
  const seen = new Set();
  while (queue.length) {
    const relative = queue.shift();
    if (seen.has(relative)) continue;
    seen.add(relative);
    const source = path.join(canonical, relative);
    const destination = path.join(skill, relative);
    const bytes = fs.readFileSync(source);
    if (relative.endsWith('.md')) queue.push(...references(bytes.toString('utf8'), relative));
    if (!fs.existsSync(destination) || !fs.readFileSync(destination).equals(bytes)) {
      if (check) failures.push(path.relative(root, destination));
      else {
        fs.mkdirSync(path.dirname(destination), { recursive: true });
        fs.writeFileSync(destination, bytes);
      }
    }
    count += 1;
  }
}
if (failures.length) {
  process.stderr.write(`Specialist resources need synchronization:\n${failures.join('\n')}\nRun node scripts/sync-skills.mjs.\n`);
  process.exitCode = 1;
} else {
  process.stdout.write(`${check ? 'Verified' : 'Synchronized'} ${count} specialist resources from skills/bandit.\n`);
}
