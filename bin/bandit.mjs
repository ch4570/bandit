#!/usr/bin/env node
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';
import { runCli } from '../lib/installer.mjs';

const packageRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
process.exitCode = runCli(process.argv.slice(2), { packageRoot });
