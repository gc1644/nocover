#!/usr/bin/env python3
from pathlib import Path
import sys

FOLDER = "/run/user/1000/gvfs/mtp:host=Xiaomi_POCO_M3_e9bc7baf1220/Internal shared storage/Music"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".heic", ".avif"}

ASK_CONFIRMATION = True

print(f"Scanning folder: {FOLDER}\n")

root = Path(FOLDER).expanduser().resolve()

if not root.exists():
    print(f"Error: Folder does not exist → {root}", file=sys.stderr)
    sys.exit(1)

found_images = []

# Find all images recursively
for path in root.rglob("*"):
    if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
        found_images.append(path)

if not found_images:
    print("No image files found. Nothing to do.")
    sys.exit(0)

print(f"Found {len(found_images)} image files:")
for img in found_images:
    print(f"  {img}")
print()

if ASK_CONFIRMATION:
    answer = input("Really DELETE all these files? [y/N] ").strip().lower()
    if answer not in ("y", "yes", "ye"):
        print("Cancelled — nothing was deleted.")
        sys.exit(0)

# Delete
deleted_count = 0
for path in found_images:
    try:
        path.unlink()
        print(f"Deleted: {path}")
        deleted_count += 1
    except Exception as e:
        print(f"Error deleting {path}: {e}", file=sys.stderr)

print(f"\nDone! Deleted {deleted_count} of {len(found_images)} files.")
