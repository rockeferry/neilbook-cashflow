import { mkdir, copyFile } from 'node:fs/promises';
import { resolve } from 'node:path';

const root = process.cwd();
const webDir = resolve(root, 'www');
await mkdir(webDir, { recursive: true });

const files = [
  'index.html',
  'manifest.json',
  'sw.js',
  'icon-192.png',
  'icon-512.png'
];

for (const file of files) {
  await copyFile(resolve(root, file), resolve(webDir, file));
}

console.log(`Prepared ${files.length} NeilBook web assets in www/.`);
