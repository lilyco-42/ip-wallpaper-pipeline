# 02 · 4K 放大 SOP

## 依赖

- Python 3.13 + Pillow（`pip install pillow`）

## 命令

```powershell
# 竖屏壁纸：裁 9:16 → 2160×3840 (q95)
python tools/upscale4k.py raw/hutao_wall_raw.jpg out/hutao_wall_4k.jpg wallpaper

# 方形素材：裁中心方形 → 3840×3840 (q95)
python tools/upscale4k.py raw/hutao_sq_raw.jpg out/hutao_sq_4k.jpg square

# 上传预览版（闲鱼/小红书用，1080px 宽 q90）
python tools/make_pub.py out/ out/pub/
```

## 命名规范

```
<role>_wall_4k.jpg   # 壁纸 2160×3840
<role>_sq_4k.jpg     # 方形 3840×3840
<role>_wall_pub.jpg  # 上传版 1080px
<role>_sq_pub.jpg    # 上传版 1080px
```

## 质量检查

1. 4K 输出 2-6 MB/张（太大→降低 q；太小→检查源图分辨率）
2. Read 回读 1-2 张：锐化不过度、五官不糊、无摩尔纹
3. 源图比例不对时：壁纸模式自动裁 9:16，方形模式自动裁中心

## 已知坑

- 方形素材若源图已是 1:1（如 1254×1254），square 模式直接放大，不裁
- 超大图（>10MB）上传闲鱼/小红书会慢 → 一律用 pub 版上传，4K 原图只进夸克
