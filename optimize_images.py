#!/usr/bin/env python3
"""Optimize PNG images in static/images/ by converting to WebP and resizing."""

import os
import sys
from pathlib import Path
from PIL import Image

IMAGES_DIR = Path(__file__).parent / "static" / "images"
MAX_WIDTH = 1200  # hero images don't need to be wider than this
WEBP_QUALITY = 82  # good balance of quality vs size


def optimize_image(src: Path, keep_png: bool = False):
    """Convert a PNG to optimized WebP, optionally keeping the original."""
    with Image.open(src) as img:
        orig_size = src.stat().st_size
        w, h = img.size

        # Resize if wider than MAX_WIDTH
        if w > MAX_WIDTH:
            ratio = MAX_WIDTH / w
            new_size = (MAX_WIDTH, int(h * ratio))
            img = img.resize(new_size, Image.LANCZOS)

        # Save as WebP
        webp_path = src.with_suffix(".webp")
        img.save(webp_path, "WEBP", quality=WEBP_QUALITY, method=6)
        new_size_bytes = webp_path.stat().st_size

        # Also save optimized PNG (smaller, resized)
        img.save(src, "PNG", optimize=True)
        png_size = src.stat().st_size

        reduction = (1 - new_size_bytes / orig_size) * 100
        print(f"  {src.name}: {orig_size/1024/1024:.1f}MB -> WebP {new_size_bytes/1024:.0f}KB / PNG {png_size/1024:.0f}KB ({reduction:.0f}% WebP reduction)")

        if not keep_png:
            src.unlink()

        return orig_size, new_size_bytes


def main():
    keep_png = "--keep-png" in sys.argv

    if not IMAGES_DIR.is_dir():
        print(f"Error: {IMAGES_DIR} not found")
        sys.exit(1)

    pngs = sorted(IMAGES_DIR.rglob("*.png"))
    if not pngs:
        print("No PNG files found.")
        return

    print(f"Optimizing {len(pngs)} PNG images (max width: {MAX_WIDTH}px, WebP quality: {WEBP_QUALITY})...")
    if keep_png:
        print("  (keeping optimized PNGs alongside WebP)")
    print()

    total_orig = 0
    total_new = 0

    for png in pngs:
        orig, new = optimize_image(png, keep_png=keep_png)
        total_orig += orig
        total_new += new

    print(f"\nTotal: {total_orig/1024/1024:.1f}MB -> {total_new/1024/1024:.1f}MB ({(1-total_new/total_orig)*100:.0f}% reduction)")


if __name__ == "__main__":
    main()
