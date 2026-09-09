#!/usr/bin/env node
// Archive run_local.py evidence, not a planning-quality verdict. No model calls.
import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';

const SPECIALISTS = new Set(['bandit-research', 'bandit-scope', 'bandit-specify', 'bandit-review']);
const TOKEN = '<temporary-run-root>';
const digest = (bytes) => createHash('sha256').update(bytes).digest('hex');
const exists = (name) => { try { fs.lstatSync(name); return true; } catch (error) { if (error.code === 'ENOENT') return false; throw error; } };

function readFile(name) {
  if (!fs.lstatSync(name).isFile()) throw new Error(`Expected a regular file: ${name}`);
  return fs.readFileSync(name);
}

function readTree(root) {
  if (!fs.lstatSync(root).isDirectory()) throw new Error(`Expected a directory: ${root}`);
  if (fs.realpathSync(root) !== path.resolve(root)) throw new Error(`Unsupported symlink in directory path: ${root}`);
  const files = new Map();
  function walk(folder, prefix = '') {
    for (const entry of fs.readdirSync(folder, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
      const relative = prefix + entry.name;
      const full = path.join(folder, entry.name);
      if (entry.isDirectory()) walk(full, `${relative}/`);
      else if (entry.isFile()) files.set(relative, readFile(full));
      else throw new Error(`Unsupported symlink or special file: ${full}`);
    }
  }
  walk(root);
  return files;
}

function hashMap(value, label) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) throw new Error(`Missing or invalid ${label}`);
  for (const [name, hash] of Object.entries(value)) {
    if (name.includes('\\') || name.includes('\0') || name.split('/').some((part) => !part || part === '.' || part === '..') ||
        !/^[a-f0-9]{64}$/.test(hash)) throw new Error(`Invalid entry in ${label}: ${name}`);
  }
  return value;
}

function changes(before, after) {
  return [...new Set([...Object.keys(before), ...Object.keys(after)])].sort()
    .filter((name) => before[name] !== after[name]);
}

function verify(files, expected, label) {
  const actual = Object.fromEntries([...files].map(([name, bytes]) => [name, digest(bytes)]));
  const mismatches = changes(expected, actual);
  if (mismatches.length) throw new Error(`${label} hashes do not match metadata: ${mismatches.join(', ')}`);
}

function originalSnapshot(run, folder, before, afterFiles) {
  if (exists(path.join(run, folder))) {
    const files = readTree(path.join(run, folder));
    verify(files, before, folder);
    return { files, missing: [], source: folder };
  }
  // Older runners did not retain originals. Recover only bytes whose hash still
  // matches the recorded before-state; never relabel changed bytes as originals.
  const files = new Map([...afterFiles].filter(([name, bytes]) => before[name] === digest(bytes)));
  return { files, missing: Object.keys(before).filter((name) => !files.has(name)).sort(), source: null };
}

function destinationPath(name) {
  let ancestor = path.resolve(name);
  const tail = [];
  while (!exists(ancestor)) {
    tail.unshift(path.basename(ancestor));
    ancestor = path.dirname(ancestor);
  }
  return path.join(fs.realpathSync(ancestor), ...tail);
}

function contains(parent, child) {
  const relative = path.relative(parent, child);
  return !relative || (!path.isAbsolute(relative) && relative !== '..' && !relative.startsWith(`..${path.sep}`));
}

/** Copies one terminal runner directory into a new destination; returns provenance. */
export function archiveRun(source, destination) {
  const suppliedSource = path.resolve(source);
  const run = fs.realpathSync(suppliedSource);
  if (exists(path.resolve(destination))) throw new Error(`Destination already exists: ${destination}`);
  const target = destinationPath(destination);
  if (contains(run, target) || contains(target, run)) throw new Error('Source and destination must not overlap');

  const metadataBytes = readFile(path.join(run, 'metadata.json'));
  const metadata = JSON.parse(metadataBytes.toString('utf8'));
  if (!Number.isFinite(metadata.elapsed_seconds) || metadata.elapsed_seconds < 0) {
    throw new Error('Run is not terminal: elapsed_seconds is required');
  }
  const launchFailed = metadata.runner_status === 'launch_failed';
  if (launchFailed) {
    const error = metadata.runner_error;
    const utcTime = (value) => typeof value === 'string' &&
      /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:\+00:00|Z)$/.test(value) && Number.isFinite(Date.parse(value));
    if (metadata.exit_code !== null || !error || !['version_probe', 'task_launch'].includes(error.phase) ||
        typeof error.type !== 'string' || !error.type.trim() || typeof error.message !== 'string' || !error.message.trim() ||
        !utcTime(metadata.started_at_utc) || !utcTime(metadata.finished_at_utc) ||
        Date.parse(metadata.finished_at_utc) < Date.parse(metadata.started_at_utc)) {
      throw new Error('Invalid terminal launch failure: error, UTC timestamps and null task exit_code are required');
    }
  } else if (!Number.isInteger(metadata.exit_code) || metadata.runner_error !== undefined ||
      (metadata.runner_status !== undefined && metadata.runner_status !== 'exited')) {
    throw new Error('Run is not terminal: a task exit_code or explicit launch failure is required');
  }
  if (!['baseline', 'bandit', 'upstream', ...SPECIALISTS].includes(metadata.arm) ||
      typeof metadata.case !== 'string' || !Array.isArray(metadata.command) || !metadata.command.every((arg) => typeof arg === 'string')) {
    throw new Error('Invalid runner identity or command metadata');
  }
  const beforeInput = hashMap(metadata.input_sha256, 'input_sha256');
  const afterInput = hashMap(metadata.input_after_sha256, 'input_after_sha256');
  const beforeInstructions = hashMap(metadata.instruction_sha256, 'instruction_sha256');
  const afterInstructions = hashMap(metadata.instruction_after_sha256, 'instruction_after_sha256');
  const instructionScope = SPECIALISTS.has(metadata.arm) ? '.agents/skills' : 'instructions';
  const input = readTree(path.join(run, 'workspace/input'));
  verify(input, afterInput, 'Current input');
  const instructions = metadata.arm === 'baseline' ? new Map() : readTree(path.join(run, 'workspace', instructionScope));
  verify(instructions, afterInstructions, 'Current instructions');
  if (metadata.arm === 'baseline' && Object.keys(beforeInstructions).length) throw new Error('Baseline has unexpected instruction hashes');
  const originalInput = originalSnapshot(run, 'original-input', beforeInput, input);
  const originalInstructions = originalSnapshot(run, 'original-instructions', beforeInstructions, instructions);
  const changedInputs = changes(beforeInput, afterInput);
  const changedInstructions = changes(beforeInstructions, afterInstructions);
  const editable = metadata.editable_artifact ?? null;
  if (editable !== null && (typeof editable !== 'string' || !editable.startsWith('input/') ||
      !Object.hasOwn(beforeInput, editable.slice(6)))) throw new Error('Invalid editable_artifact metadata');

  const roots = new Set([suppliedSource, run]);
  const workingArg = metadata.command.indexOf('-C');
  const outputArg = metadata.command.indexOf('-o');
  const recordedWorkspace = metadata.command[workingArg + 1];
  if (workingArg < 0 || outputArg < 0 || !path.isAbsolute(recordedWorkspace ?? '') || path.basename(recordedWorkspace) !== 'workspace' ||
      metadata.command[outputArg + 1] !== path.join(path.dirname(recordedWorkspace), 'output.md')) {
    throw new Error('Command does not identify the expected runner workspace and output');
  }
  roots.add(path.dirname(recordedWorkspace));
  if ([...roots].some((root) => root === path.parse(root).root)) throw new Error('A filesystem root is not a valid run directory');
  // Python metadata escapes Unicode; JSON logs also escape Windows backslashes.
  const replacements = [...new Set([...roots].flatMap((root) => {
    const json = JSON.stringify(root).slice(1, -1);
    return [root, json, json.replace(/[^\x00-\x7f]/g, (char) => `\\u${char.charCodeAt(0).toString(16).padStart(4, '0')}`)];
  }))]
    .sort((a, b) => b.length - a.length);
  const normalize = (bytes) => {
    // Latin-1 makes replacement byte-preserving, including BOMs or malformed
    // UTF-8 in a failed process's stderr. Only the UTF-8 path bytes are changed.
    return Buffer.from(replacements.reduce((value, root) => value.replaceAll(Buffer.from(root).toString('latin1'), TOKEN),
      bytes.toString('latin1')), 'latin1');
  };

  const outputFiles = new Map();
  const records = {};
  const omittedImages = [];
  function add(name, bytes, rawPath, transform = false, omitPng = false) {
    const omitted = omitPng && path.extname(name).toLowerCase() === '.png';
    const archived = omitted ? null : transform ? normalize(bytes) : bytes;
    records[name] = { source: rawPath, original_sha256: digest(bytes),
      archived_sha256: archived ? digest(archived) : null,
      temporary_path_normalized: archived ? !bytes.equals(archived) : false };
    if (omitted) { records[name].omitted = 'PNG retained by hash only'; omittedImages.push(name); }
    else outputFiles.set(name, archived);
  }
  const artifacts = new Map([['metadata.json', metadataBytes]]);
  for (const name of ['prompt.txt', 'events.jsonl', 'stderr.txt']) artifacts.set(name, readFile(path.join(run, name)));
  if (exists(path.join(run, 'output.md'))) artifacts.set('output.md', readFile(path.join(run, 'output.md')));
  for (const [name, bytes] of artifacts) add(name, bytes, name, true);

  let terminalEvent = null;
  let invalidEventLines = 0;
  for (const line of artifacts.get('events.jsonl').toString('utf8').split('\n').filter((line) => line.trim())) {
    try {
      const event = JSON.parse(line);
      if (event?.type === 'turn.started') terminalEvent = null;
      else if (event?.type === 'turn.completed' || event?.type === 'turn.failed') terminalEvent = event.type;
    } catch { invalidEventLines++; }
  }
  const missingOutput = !artifacts.get('output.md')?.toString('utf8').trim();
  const runStatus = launchFailed ? 'launch-failed' : metadata.exit_code !== 0 ? 'failed' :
    terminalEvent === 'turn.completed' && !missingOutput && !invalidEventLines ? 'completed' : 'incomplete-response';

  for (const [name, bytes] of originalInput.files) add(`input/${name}`, bytes, `${originalInput.source ?? 'workspace/input'}/${name}`);
  if (editable || changedInputs.length) for (const [name, bytes] of input) add(`after/${name}`, bytes, `workspace/input/${name}`);
  for (const [name, bytes] of originalInstructions.files) add(`instructions/${name}`, bytes,
    `${originalInstructions.source ?? `workspace/${instructionScope}`}/${name}`, false, true);
  if (changedInstructions.length) for (const [name, bytes] of instructions) add(`instructions-after/${name}`, bytes,
    `workspace/${instructionScope}/${name}`, false, true);

  const provenance = {
    format: 1,
    archive_status: 'archived',
    archived_at: new Date().toISOString(),
    source_format: 'evals/run_local.py',
    run_status: runStatus,
    source_exit_code: metadata.exit_code,
    terminal_event: terminalEvent,
    invalid_event_lines: invalidEventLines,
    missing_or_empty_output: Boolean(missingOutput),
    input_changes: changedInputs,
    input_scope_respected: changedInputs.every((name) => `input/${name}` === editable),
    instruction_changes: changedInstructions,
    original_input_missing: originalInput.missing,
    original_instruction_missing: originalInstructions.missing,
    original_text_snapshot_complete: !originalInput.missing.length && !originalInstructions.missing.length,
    instruction_restore_directory: metadata.arm === 'baseline' ? null : instructionScope,
    omitted_png_files: omittedImages,
    temporary_path_replacement: TOKEN,
    files: records,
    limitations: [
      'Process completion and hash agreement are not planning-quality grades or proof of compliance with every task instruction.',
      'Original inputs and instruction bytes are unchanged; only the five run log/artifact files receive literal run-root path normalization.',
      'PNG files are recorded by SHA256 only and must be restored separately for an identical image-bearing workspace.',
      'Missing originals cannot be reconstructed from hashes. Partial original trees and available after-state are retained explicitly.',
      'Path normalization is not a general secret scrubber. Only supplied run evidence is archived; other workspace files and host state are not retained.',
      'Host-default model configuration and external services are not pinned by this archive; replay is not guaranteed to produce the same response.',
    ],
  };

  // All validation and byte selection precede destination creation. mkdir is
  // exclusive, including against a destination created after the initial check.
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.mkdirSync(target);
  const marker = path.join(target, 'ARCHIVE_INCOMPLETE');
  try {
    fs.writeFileSync(marker, 'Archival did not finish unless archive-provenance.json exists and this marker is absent.\n', { flag: 'wx' });
    for (const [name, bytes] of outputFiles) {
      const full = path.join(target, name);
      fs.mkdirSync(path.dirname(full), { recursive: true });
      fs.writeFileSync(full, bytes, { flag: 'wx' });
    }
    fs.writeFileSync(path.join(target, 'archive-provenance.json'), JSON.stringify(provenance, null, 2) + '\n', { flag: 'wx' });
    fs.unlinkSync(marker);
  } catch (error) {
    throw new Error(`Archive is incomplete at ${target}; preserve or inspect it before retrying: ${error.message}`, { cause: error });
  }
  return provenance;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const args = process.argv.slice(2);
  if (args.length === 1 && args[0] === '--help') {
    console.log('Usage: node evals/archive_run.mjs <completed-run-directory> <new-archive-directory>');
  } else if (args.length !== 2) {
    console.error('Usage: node evals/archive_run.mjs <completed-run-directory> <new-archive-directory>');
    process.exitCode = 2;
  } else {
    try {
      const result = archiveRun(...args);
      console.log(JSON.stringify({ destination: path.resolve(args[1]), archive_status: result.archive_status,
        run_status: result.run_status, source_exit_code: result.source_exit_code,
        input_scope_respected: result.input_scope_respected, original_text_snapshot_complete: result.original_text_snapshot_complete }));
    } catch (error) {
      console.error(`bandit eval archive: ${error.message}`);
      process.exitCode = 2;
    }
  }
}
