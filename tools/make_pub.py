# -*- coding: utf-8 -*-
"""
Generate upload previews (1080px wide, q90 JPEG) from 4K masters.
Upload previews are used for goofish/xiaohongshu (fast upload),
while 4K originals go to Quark drive for fans.

Usage:
    python make_pub.py <src_dir> <out_dir> [--width 1080] [--quality 90]
Example:
    python make_pub.py out/ out/pub/
"""
import sys, os
from PIL import Image

def make_pub(src, dst, width=1080, quality=90):
    img = Image.open(src).convert("RGB")
    w, h = img.size
    nw = width
    nh = int(h * (nw / w))
    img = img.resize((nw, nh), Image.LANCZOS)
    img.save(dst, "JPEG", quality=quality, subsampling=0)
    print(f"pub: {dst} {img.size}")

if __name__ == "__main__":
    src_dir = sys.argv[1]
    out_dir = sys.argv[2]
    width = 1080
    quality = 90
    for a in sys.argv[3:]:
        if a.startswith("--width"):
            width = int(a.split("=")[1])
        elif a.startswith("--quality"):
            quality = int(a.split("=")[1])
    os.makedirs(out_dir, exist_ok=True)
    for fn in sorted(os.listdir(src_dir)):
        if fn.lower().endswith((".jpg", ".jpeg", ".png")) and "_4k" in fn.lower():
            src = os.path.join(src_dir, fn)
            base = fn.replace("_4k", "_pub")
            dst = os.path.join(out_dir, base)
            make_pub(src, dst, width, quality)
    print("done")
