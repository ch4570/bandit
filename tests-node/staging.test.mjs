import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { installInto, InstallError } from '../lib/installer.mjs';

// Synthetic two-file installation: the second write can fail after the first
// has committed, so preservation includes the existing rollback boundary.
function fixture(t) {
  const root = fs.mkdtempSync(path.join(fs.realpathSync(os.tmpdir()), 'bandit-staging-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  const source = path.join(root, 'package');
  const skill = path.join(source, 'skills', 'bandit');
  const destination = path.join(root, 'project', 'bandit');
  fs.mkdirSync(path.join(skill, 'references'), { recursive: true });
  fs.writeFileSync(path.join(source, 'package.json'), JSON.stringify({ version: '0.4.0' }));
  fs.writeFileSync(path.join(skill, 'SKILL.md'), 'Original synthetic instructions.\n');
  fs.writeFileSync(path.join(skill, 'references', 'rules.md'), 'Original synthetic rules.\n');
  installInto(source, destination);
  const before = snapshot(destination);
  fs.writeFileSync(path.join(skill, 'SKILL.md'), 'Updated synthetic instructions.\n');
  fs.writeFileSync(path.join(skill, 'references', 'rules.md'), 'Updated synthetic rules.\n');
  return { root, source, destination, before };
}

function snapshot(root) {
  const result = {};
  for (const name of fs.readdirSync(root, { recursive: true }).sort()) {
    const file = path.join(root, name);
    if (fs.lstatSync(file).isFile()) result[name] = fs.readFileSync(file).toString('base64');
  }
  return result;
}

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

function updateWithInjection(f, mutate) {
  let staged, error;
  afterWrites((file, data, write) => {
    if (!staged && typeof file === 'string' && path.dirname(file) === path.join(f.destination, 'references')
      && path.basename(file).endsWith('.tmp')) {
      staged = file;
      mutate(file, data, write);
    }
  }, () => {
    try { installInto(f.source, f.destination); }
    catch (caught) { error = caught; }
  });
  assert.ok(staged, 'The injection must run after a real second-file staging write');
  return { staged, error };
}

test('changed staged bytes are neither promoted nor deleted, and earlier writes roll back', (t) => {
  const f = fixture(t);
  const edited = 'Concurrent work in the staged file.\n';
  const { staged, error } = updateWithInjection(f, (file, data, write) => write(file, edited));
  assert.ok(fs.existsSync(staged), 'The changed staging file must remain at its own path');
  assert.equal(fs.readFileSync(staged, 'utf8'), edited);
  assert.ok(error instanceof InstallError, 'The changed staging source must reject the update');
  assert.deepEqual(snapshot(f.destination), {
    ...f.before, [path.relative(f.destination, staged)]: Buffer.from(edited).toString('base64'),
  });
});

test('a different staged file with identical bytes is preserved rather than promoted', (t) => {
  const f = fixture(t);
  const saved = path.join(f.root, 'moved-owned-staging-file');
  let replacement;
  const { staged, error } = updateWithInjection(f, (file, data, write) => {
    fs.renameSync(file, saved);
    write(file, data, { flag: 'wx' });
    replacement = fs.lstatSync(file, { bigint: true });
  });
  assert.notEqual(replacement.ino, fs.lstatSync(saved, { bigint: true }).ino);
  assert.ok(fs.existsSync(staged), 'A replacement staging file must remain at its own path');
  assert.equal(fs.lstatSync(staged, { bigint: true }).ino, replacement.ino);
  assert.ok(error instanceof InstallError, 'A different staging object must reject the update');
  assert.deepEqual(fs.readFileSync(staged), fs.readFileSync(saved));
  assert.deepEqual(snapshot(f.destination), {
    ...f.before, [path.relative(f.destination, staged)]: fs.readFileSync(staged).toString('base64'),
  });
});
