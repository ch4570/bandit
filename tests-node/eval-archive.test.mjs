import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { archiveRun } from '../evals/archive_run.mjs';

const hash = (bytes) => createHash('sha256').update(bytes).digest('hex');
function put(root, name, bytes) {
  const full = path.join(root, name);
  fs.mkdirSync(path.dirname(full), { recursive: true });
  fs.writeFileSync(full, bytes);
}
function read(root, name) { return fs.readFileSync(path.join(root, name)); }
function hashes(root) {
  return Object.fromEntries(fs.readdirSync(root, { recursive: true }).sort()
    .filter((name) => fs.lstatSync(path.join(root, name)).isFile())
    .map((name) => [name.split(path.sep).join('/'), hash(read(root, name))]));
}
function fixture(t, { baseline = false, originals = false } = {}) {
  const root = fs.mkdtempSync(path.join(fs.realpathSync(os.tmpdir()), 'bandit-eval-archive-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  const run = path.join(root, '실행 run');
  const destination = path.join(root, 'archives', 'case');
  const input = path.join(run, 'workspace/input');
  const instructions = path.join(run, 'workspace/.agents/skills');
  put(input, 'request.md', 'Review the linked plan.\n');
  put(input, 'docs/PRD.md', `Original plan with literal fixture text: ${run}\n`);
  if (!baseline) {
    put(instructions, 'bandit-review/SKILL.md', '\ufeff---\nname: bandit-review\n---\nRead references/review.md.\n');
    put(instructions, 'bandit-review/references/review.md', 'Review actual consequences.\n');
    put(instructions, 'bandit-review/assets/avatar.png', Buffer.from([137, 80, 78, 71, 255, 0]));
  }
  if (originals) {
    fs.cpSync(input, path.join(run, 'original-input'), { recursive: true });
    if (!baseline) fs.cpSync(instructions, path.join(run, 'original-instructions'), { recursive: true });
  }
  const metadata = {
    case: '09-linked-policy-review', arm: baseline ? 'baseline' : 'bandit-review',
    command: ['codex', 'exec', '-C', path.join(run, 'workspace'), '-o', path.join(run, 'output.md'), '-'],
    input_sha256: hashes(input), input_after_sha256: hashes(input),
    instruction_sha256: baseline ? {} : hashes(instructions),
    instruction_after_sha256: baseline ? {} : hashes(instructions),
    editable_artifact: null, exit_code: 0, elapsed_seconds: 1.25,
  };
  put(run, 'metadata.json', JSON.stringify(metadata, null, 2) + '\n');
  put(run, 'prompt.txt', `Read ${path.join(run, 'workspace/input/request.md')}\n`);
  put(run, 'output.md', `Reviewed ${run}. No material issue.\n`);
  put(run, 'events.jsonl', JSON.stringify({ type: 'turn.started' }) + '\n' + JSON.stringify({ type: 'turn.completed', run }) + '\n');
  put(run, 'stderr.txt', '');
  return { root, run, destination, input, instructions, metadata,
    save() { put(run, 'metadata.json', JSON.stringify(metadata, null, 2) + '\n'); } };
}

function launchFailure(f, phase = 'task_launch') {
  Object.assign(f.metadata, {
    runner_status: 'launch_failed', exit_code: null,
    started_at_utc: '2026-09-08T15:52:07.859429+00:00',
    finished_at_utc: '2026-09-08T15:52:07.860000+00:00',
    runner_error: { phase, type: 'FileNotFoundError', message: 'Synthetic executable unavailable' },
  });
  f.save();
  fs.unlinkSync(path.join(f.run, 'output.md'));
  put(f.run, 'events.jsonl', '');
}

test('archives older read-only runs with exact originals, normalized logs, and PNG hash receipts', (t) => {
  const f = fixture(t);
  const before = hashes(f.run);
  const receipt = archiveRun(f.run, f.destination);
  assert.equal(receipt.run_status, 'completed');
  assert.equal(receipt.original_text_snapshot_complete, true);
  assert.equal(receipt.input_scope_respected, true);
  assert.deepEqual(read(f.destination, 'input/docs/PRD.md'), read(f.input, 'docs/PRD.md'));
  assert.deepEqual(read(f.destination, 'instructions/bandit-review/SKILL.md'), read(f.instructions, 'bandit-review/SKILL.md'));
  assert.equal(fs.existsSync(path.join(f.destination, 'instructions/bandit-review/assets/avatar.png')), false);
  assert.equal(receipt.files['instructions/bandit-review/assets/avatar.png'].original_sha256,
    f.metadata.instruction_sha256['bandit-review/assets/avatar.png']);
  assert.match(read(f.destination, 'prompt.txt').toString(), /<temporary-run-root>/);
  assert.equal(read(f.destination, 'metadata.json').toString().includes(f.run), false);
  for (const [name, record] of Object.entries(receipt.files)) {
    assert.equal(record.original_sha256, hash(read(f.run, record.source)));
    if (record.archived_sha256) assert.equal(record.archived_sha256, hash(read(f.destination, name)));
  }
  assert.deepEqual(hashes(f.run), before);
  assert.equal(fs.existsSync(path.join(f.destination, 'ARCHIVE_INCOMPLETE')), false);
});

test('preserves edited inputs and changed instructions separately using pre-run snapshots', (t) => {
  const f = fixture(t, { originals: true });
  f.metadata.editable_artifact = 'input/docs/PRD.md';
  put(f.input, 'docs/PRD.md', 'Rewritten current plan.\n');
  put(f.instructions, 'bandit-review/references/review.md', 'A changed instruction.\n');
  f.metadata.input_after_sha256 = hashes(f.input);
  f.metadata.instruction_after_sha256 = hashes(f.instructions);
  f.save();
  const receipt = archiveRun(f.run, f.destination);
  assert.deepEqual(read(f.destination, 'input/docs/PRD.md'), read(f.run, 'original-input/docs/PRD.md'));
  assert.equal(read(f.destination, 'after/docs/PRD.md').toString(), 'Rewritten current plan.\n');
  assert.equal(read(f.destination, 'instructions/bandit-review/references/review.md').toString(), 'Review actual consequences.\n');
  assert.equal(read(f.destination, 'instructions-after/bandit-review/references/review.md').toString(), 'A changed instruction.\n');
  assert.deepEqual(receipt.input_changes, ['docs/PRD.md']);
  assert.deepEqual(receipt.instruction_changes, ['bandit-review/references/review.md']);
  assert.equal(receipt.input_scope_respected, true);
  assert.equal(receipt.original_text_snapshot_complete, true);
});

test('keeps completed failures with missing output and corrupt event lines without fabricating success', (t) => {
  const f = fixture(t, { baseline: true, originals: true });
  f.metadata.exit_code = 1;
  f.save();
  fs.unlinkSync(path.join(f.run, 'output.md'));
  put(f.run, 'events.jsonl', '{"type":"turn.failed"}\ntruncated {\n');
  put(f.run, 'stderr.txt', Buffer.concat([Buffer.from(`Failure in ${f.run}\n`), Buffer.from([255, 254])]));
  const receipt = archiveRun(f.run, f.destination);
  assert.equal(receipt.run_status, 'failed');
  assert.equal(receipt.source_exit_code, 1);
  assert.equal(receipt.terminal_event, 'turn.failed');
  assert.equal(receipt.invalid_event_lines, 1);
  assert.equal(receipt.missing_or_empty_output, true);
  assert.equal(fs.existsSync(path.join(f.destination, 'output.md')), false);
  assert.deepEqual(read(f.destination, 'stderr.txt'), Buffer.concat([Buffer.from('Failure in <temporary-run-root>\n'), Buffer.from([255, 254])]));
});

test('archives terminal launch failures separately without inventing a child exit or event', (t) => {
  for (const phase of ['task_launch', 'version_probe']) {
    const f = fixture(t, { originals: true });
    launchFailure(f, phase);
    const before = hashes(f.run);
    const receipt = archiveRun(f.run, f.destination);
    assert.equal(receipt.run_status, 'launch-failed');
    assert.equal(receipt.source_exit_code, null);
    assert.equal(receipt.terminal_event, null);
    assert.equal(receipt.missing_or_empty_output, true);
    assert.equal(receipt.original_text_snapshot_complete, true);
    assert.deepEqual(JSON.parse(read(f.destination, 'metadata.json')).runner_error, f.metadata.runner_error);
    assert.deepEqual(read(f.destination, 'input/docs/PRD.md'), read(f.run, 'original-input/docs/PRD.md'));
    assert.deepEqual(hashes(f.run), before);
  }
});

test('a launch-failure label cannot turn unfinished or contradictory evidence into a terminal archive', (t) => {
  for (const mutation of [
    (f) => { delete f.metadata.runner_error; },
    (f) => { f.metadata.runner_error = {}; },
    (f) => { f.metadata.runner_error.phase = 'unknown'; },
    (f) => { f.metadata.runner_error.type = ''; },
    (f) => { f.metadata.runner_error.message = ''; },
    (f) => { f.metadata.exit_code = 0; },
    (f) => { delete f.metadata.exit_code; },
    (f) => { delete f.metadata.elapsed_seconds; },
    (f) => { delete f.metadata.started_at_utc; },
    (f) => { delete f.metadata.finished_at_utc; },
    (f) => { f.metadata.finished_at_utc = 'not a timestamp'; },
    (f) => { f.metadata.finished_at_utc = '2026-09-07T15:52:07+00:00'; },
    (f) => { f.metadata.runner_status = 'running'; f.metadata.exit_code = 0; },
    (f) => { delete f.metadata.runner_status; f.metadata.exit_code = 0; },
  ]) {
    const f = fixture(t, { originals: true });
    launchFailure(f);
    mutation(f);
    f.save();
    assert.throws(() => archiveRun(f.run, f.destination), /terminal|runner|launch/i);
    assert.equal(fs.existsSync(f.destination), false);
  }
});

test('records lost originals and out-of-scope changes from older runners honestly', (t) => {
  const f = fixture(t);
  put(f.input, 'docs/PRD.md', 'An unauthorized edit.\n');
  put(f.instructions, 'bandit-review/SKILL.md', 'Modified during task.\n');
  f.metadata.input_after_sha256 = hashes(f.input);
  f.metadata.instruction_after_sha256 = hashes(f.instructions);
  f.save();
  const receipt = archiveRun(f.run, f.destination);
  assert.equal(receipt.input_scope_respected, false);
  assert.equal(receipt.original_text_snapshot_complete, false);
  assert.deepEqual(receipt.original_input_missing, ['docs/PRD.md']);
  assert.deepEqual(receipt.original_instruction_missing, ['bandit-review/SKILL.md']);
  assert.equal(fs.existsSync(path.join(f.destination, 'input/docs/PRD.md')), false);
  assert.equal(fs.existsSync(path.join(f.destination, 'instructions/bandit-review/SKILL.md')), false);
  assert.equal(read(f.destination, 'after/docs/PRD.md').toString(), 'An unauthorized edit.\n');
});

test('a zero exit without a completed turn is retained as an incomplete response', (t) => {
  const f = fixture(t);
  put(f.run, 'events.jsonl', '{"type":"turn.started"}\n');
  assert.equal(archiveRun(f.run, f.destination).run_status, 'incomplete-response');
});

test('refuses unfinished or inconsistent metadata before creating an archive', (t) => {
  for (const mutation of [
    (f) => { delete f.metadata.exit_code; f.save(); },
    (f) => { delete f.metadata.input_after_sha256; f.save(); },
    (f) => { put(f.input, 'docs/PRD.md', 'Changed after metadata was recorded.'); },
    (f) => { put(f.input, 'extra.md', 'Unrecorded input.'); },
    (f) => { put(f.instructions, 'bandit-review/SKILL.md', 'Changed after completion.'); },
    (f) => { put(f.run, 'original-input/docs/PRD.md', 'Not the original.'); },
    (f) => { put(f.run, 'original-instructions/bandit-review/SKILL.md', 'Not the original.'); },
    (f) => { f.metadata.input_sha256['../escape'] = 'a'.repeat(64); f.save(); },
  ]) {
    const f = fixture(t, { originals: true });
    mutation(f);
    assert.throws(() => archiveRun(f.run, f.destination), /terminal|invalid|match metadata/i);
    assert.equal(fs.existsSync(f.destination), false);
  }
});

test('refuses existing destinations and source overlap without replacing files', (t) => {
  const f = fixture(t);
  put(f.destination, 'user-note.md', 'Keep this note.');
  assert.throws(() => archiveRun(f.run, f.destination), /already exists/);
  assert.equal(read(f.destination, 'user-note.md').toString(), 'Keep this note.');
  assert.throws(() => archiveRun(f.run, path.join(f.run, 'archive')), /overlap/);
  assert.equal(fs.existsSync(path.join(f.run, 'archive')), false);
});

test('does not follow a linked workspace directory outside the raw run', (t) => {
  const f = fixture(t);
  const moved = path.join(f.root, 'external-workspace');
  fs.renameSync(path.join(f.run, 'workspace'), moved);
  fs.symlinkSync(moved, path.join(f.run, 'workspace'), 'junction');
  const before = hashes(moved);
  assert.throws(() => archiveRun(f.run, f.destination), /symlink/);
  assert.equal(fs.existsSync(f.destination), false);
  assert.deepEqual(hashes(moved), before);
});

test('normalizes Python Unicode-escaped run paths while keeping JSON valid', (t) => {
  const f = fixture(t);
  const asciiJson = JSON.stringify(f.metadata).replace(/[^\x00-\x7f]/g,
    (char) => `\\u${char.charCodeAt(0).toString(16).padStart(4, '0')}`);
  put(f.run, 'metadata.json', asciiJson + '\n');
  archiveRun(f.run, f.destination);
  const archived = JSON.parse(read(f.destination, 'metadata.json').toString());
  assert.equal(archived.command[archived.command.indexOf('-C') + 1], `<temporary-run-root>${path.sep}workspace`);
});

test('CLI reports archive success independently from the source process failure', (t) => {
  const f = fixture(t, { baseline: true });
  f.metadata.exit_code = 2;
  f.save();
  const result = spawnSync(process.execPath, [fileURLToPath(new URL('../evals/archive_run.mjs', import.meta.url)), f.run, f.destination], { encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr);
  assert.equal(JSON.parse(result.stdout).archive_status, 'archived');
  assert.equal(JSON.parse(result.stdout).run_status, 'failed');
  const repeated = spawnSync(process.execPath, [fileURLToPath(new URL('../evals/archive_run.mjs', import.meta.url)), f.run, f.destination], { encoding: 'utf8' });
  assert.equal(repeated.status, 2);
  assert.match(repeated.stderr, /already exists/);
});
