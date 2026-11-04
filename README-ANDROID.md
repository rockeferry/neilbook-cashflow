# NeilBook Cashflow — Android Debug APK

Proyek ini menambahkan target Android menggunakan Capacitor tanpa mengganti aplikasi web/PWA yang sudah ada.

## Isi

- `index.html`, `manifest.json`, `sw.js`, ikon, dan `firebase.json`: aset web yang disalin dari aplikasi yang diberikan.
- `capacitor.config.json`: konfigurasi aplikasi Android.
- `scripts/prepare-web.mjs`: menyalin aset web root ke `www/` sebelum sinkronisasi Capacitor.
- `scripts/apply-android-icons.py`: memasang ikon NeilBook ke resource launcher Android.
- `.github/workflows/android-debug-apk.yml`: membangun Debug APK secara otomatis di GitHub Actions.

## Build APK lewat GitHub Actions

1. Ekstrak seluruh isi paket ini ke root repository `rockeferry/neilbook-cashflow`.
2. Pertahankan file website yang ada; file web di paket ini adalah salinan yang digunakan saat paket dibuat.
3. Commit dan push perubahan ke branch `main`.
4. Buka tab **Actions** di GitHub.
5. Pilih **Build NeilBook Cashflow Debug APK**.
6. Tunggu sampai workflow selesai dengan tanda centang hijau.
7. Buka hasil run, lalu unduh artifact **NeilBook-Cashflow-debug**.
8. Ekstrak artifact ZIP untuk mendapatkan `NeilBook-Cashflow-debug.apk`.

Workflow juga bisa dijalankan manual melalui **Actions → Build NeilBook Cashflow Debug APK → Run workflow**.

## Build lokal (opsional)

Persyaratan: Node.js 22+, Android Studio/Android SDK, dan JDK 21.

```bash
npm install
npm run prepare:web
npx cap add android
python -m pip install pillow
python scripts/apply-android-icons.py
npx cap sync android
cd android
./gradlew assembleDebug
```

APK akan berada di `android/app/build/outputs/apk/debug/app-debug.apk`.

## Catatan kompatibilitas

- Aplikasi web tetap disimpan di root agar GitHub Pages tetap dapat menggunakannya.
- Android memuat salinan lokal `www/` yang dibuat ulang dari file root setiap build.
- Koneksi Firebase Realtime Database dan YouTube Data API di `index.html` tetap memakai konfigurasi yang sudah ada; tidak ada migrasi database atau perubahan rules dalam paket ini.
- Beberapa library dan font pada HTML saat ini dimuat dari CDN, dan data Firebase/YouTube tetap memerlukan internet. Jadi tampilan HTML berada di dalam APK, tetapi aplikasi ini belum sepenuhnya offline.
- `sw.js` tetap dipertahankan untuk PWA web; Capacitor Android tidak membutuhkan registrasi service worker untuk memuat aset lokal.

## Keamanan

Sebelum membagikan APK ke publik, tinjau kembali kredensial/API key yang tertanam di sisi klien dan pastikan API key dibatasi sesuai layanan yang digunakan. PIN/otorisasi yang hanya diperiksa di JavaScript sisi klien bukan mekanisme keamanan yang kuat untuk melindungi data; akses database harus ditegakkan melalui Firebase Security Rules.
