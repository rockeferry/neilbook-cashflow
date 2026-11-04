from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ANDROID_RES = ROOT / "android" / "app" / "src" / "main" / "res"
SOURCE = ROOT / "icon-512.png"

if not SOURCE.exists():
    raise SystemExit("icon-512.png tidak ditemukan")

image = Image.open(SOURCE).convert("RGBA")
sizes = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
}

# Hapus adaptive-icon XML bawaan template agar ikon PNG NeilBook dipakai konsisten.
adaptive = ANDROID_RES / "mipmap-anydpi-v26"
if adaptive.exists():
    for filename in ("ic_launcher.xml", "ic_launcher_round.xml"):
        target = adaptive / filename
        if target.exists():
            target.unlink()

for folder, size in sizes.items():
    target_dir = ANDROID_RES / folder
    target_dir.mkdir(parents=True, exist_ok=True)
    rendered = image.resize((size, size), Image.Resampling.LANCZOS)
    rendered.save(target_dir / "ic_launcher.png", optimize=True)
    rendered.save(target_dir / "ic_launcher_round.png", optimize=True)

print("Ikon launcher NeilBook berhasil dipasang ke resource Android.")
