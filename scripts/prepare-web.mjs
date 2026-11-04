import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const webDir = path.join(root, 'www');

const files = [
  'index.html',
  'manifest.json',
  'sw.js',
  'firebase.json',
  'icon-192.png',
  'icon-512.png'
];

fs.mkdirSync(webDir, { recursive: true });

for (const file of files) {
  const source = path.join(root, file);

  if (!fs.existsSync(source)) {
    throw new Error(`File sumber tidak ditemukan: ${file}`);
  }

  fs.copyFileSync(source, path.join(webDir, file));
  console.log(`Disalin: ${file}`);
}

console.log('Semua file web berhasil disiapkan.');
