// Run the frozen regression and genuine-sibling control after the narrow source fix.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';

const evidence = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(evidence, '../../../..');
const hashFile = (name) => createHash('sha256').update(fs.readFileSync(path.join(repo, name))).digest('hex');
const source = 'lib/installer.mjs';
const tests = 'tests-node/install.test.mjs';
const before = { [source]: hashFile(source), [tests]: hashFile(tests) };
assert.notEqual(before[source], hashFile(path.relative(repo, path.join(evidence, 'installer-before.mjs'))));
assert.equal(before[tests], '4a2259d68f57107f270efec164304115f226f98a127cc006878d2220cf2f4a46');
assert.equal(process.versions.node, '22.23.2');
const argv = [process.execPath, '--test', '--test-name-pattern=PM Craft', tests];
const started = new Date().toISOString();
const result = spawnSync(argv[0], argv.slice(1), {
  cwd: repo, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'], shell: false,
});
const after = { [source]: hashFile(source), [tests]: hashFile(tests) };
const receipt = { argv, cwd: repo, stdin: 'closed', shell: false, started_at: started,
  ended_at: new Date().toISOString(), runtime: process.version, exit_code: result.status,
  signal: result.signal, error: result.error?.message ?? null, hashes_before: before, hashes_after: after,
  stdout: 'legacy-note-targeted-after.stdout.txt', stderr: 'legacy-note-targeted-after.stderr.txt',
};
for (const stream of ['stdout', 'stderr']) {
  fs.writeFileSync(path.join(evidence, receipt[stream]), result[stream] ?? '', { flag: 'wx' });
}
fs.writeFileSync(path.join(evidence, 'legacy-note-targeted-after-results.json'), `${JSON.stringify(receipt, null, 2)}\n`, { flag: 'wx' });
process.stdout.write(result.stdout ?? '');
process.stderr.write(result.stderr ?? '');
assert.deepEqual(after, before);
assert.equal(result.error, undefined);
assert.equal(result.status, 0, 'The frozen regression must pass against the fixed source.');
process.exitCode = result.status;
