# -*- coding: utf-8 -*-
"""
Upscale GPT-generated images to 4K.
- Wallpaper (portrait): crop to 9:16 then upscale to 2160x3840 (4K portrait)
- Square art (phone case / other): upscale to 3840x3840 (4K square)
Method: Pillow Lanczos + UnsharpMask (safe, no extra deps).
Usage: python upscale4k.py <input> <output> <mode:wallpaper|square> [--crop]
"""
import sys, os
from PIL import Image, ImageFilter, ImageEnhance

def upscale_high(img, target_w, target_h):
    """Lanczos upscale to target, then gentle unsharp mask."""
    img = img.convert("RGB")
    img = img.resize((target_w, target_h), Image.LANCZOS)
    img = img.filter(ImageFilter.UnsharpMask(radius=3, percent=70, threshold=2))
    return img

def to_wallpaper_4k(src, dst, do_crop=True):
    img = Image.open(src).convert("RGB")
    w, h = img.size
    # if landscape or square, crop center to 9:16
    if do_crop and w / h > 9 / 16:
        new_w = int(h * 9 / 16)
        x0 = (w - new_w) // 2
        img = img.crop((x0, 0, x0 + new_w, h))
    elif do_crop and h / w > 16 / 9:
        # taller than 9:16 -> keep, will stretch less; crop sides only
        pass
    out = upscale_high(img, 2160, 3840)
    out.save(dst, "JPEG", quality=95, subsampling=0)
    print(f"wallpaper4k: {dst} {out.size}")

def to_square_4k(src, dst):
    img = Image.open(src).convert("RGB")
    w, h = img.size
    s = min(w, h)
    x0 = (w - s) // 2
    y0 = (h - s) // 2
    img = img.crop((x0, y0, x0 + s, y0 + s))
    out = upscale_high(img, 3840, 3840)
    out.save(dst, "JPEG", quality=95, subsampling=0)
    print(f"square4k: {dst} {out.size}")

def to_4k_keep_ratio(src, dst, max_side=3840):
    """Upscale keeping aspect ratio, longest side = max_side."""
    img = Image.open(src).convert("RGB")
    w, h = img.size
    scale = max_side / max(w, h)
    if scale < 1:
        scale = 1
    nw, nh = int(w * scale), int(h * scale)
    out = upscale_high(img, nw, nh)
    out.save(dst, "JPEG", quality=95, subsampling=0)
    print(f"ratio4k: {dst} {out.size}")

if __name__ == "__main__":
    src = sys.argv[1]
    dst = sys.argv[2]
    mode = sys.argv[3] if len(sys.argv) > 3 else "wallpaper"
    if mode == "wallpaper":
        to_wallpaper_4k(src, dst)
    elif mode == "square":
        to_square_4k(src, dst)
    else:
        to_4k_keep_ratio(src, dst)
