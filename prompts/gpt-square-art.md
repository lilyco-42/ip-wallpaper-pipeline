# GPT 方形素材提示词模板（1:1 手机壳素材）

## 模板

```text
Create a square 1:1 image of <ROLE> from <GAME>, the <KEYWORD1>, 
<KEYWORD2>, <LOOK_DETAILS>, <POSE>, centered full-body composition, 
<CLEAN_BACKGROUND>, official game art style, no text.
```

## 已实测示例

### Hu Tao 方形 — ✅

```text
Create a square 1:1 image of Hu Tao from Genshin Impact, the cheerful girl with brown twintails, red eyes, black and red outfit, holding her Staff of Homa over her shoulder, playful wink, plum blossoms and ghost spirits around, centered full-body composition, clean night shrine background, official game art style, no text.
```

### Raiden Shogun 方形 — ✅

```text
Create a square 1:1 image of Raiden Shogun from Genshin Impact, the elegant woman with long purple hair in a side braid, calm violet eyes, purple and white kimono, arms crossed holding her sword, centered full-body composition, soft purple storm background with lightning and sakura petals, official game art style, no text.
```

### Ganyu 方形 — ✅

```text
Create a square 1:1 image of Ganyu from Genshin Impact, the graceful woman with long blue-violet hair and small curved horns, calm aqua eyes, white and blue elegant qipao-style dress, drawing her ornate bow with an ice-blue arrow, centered full-body composition, snowy mountain background with gentle snowflakes, soft icy blue glow, official game art style, no text.
```

## 关键规则

1. `square 1:1 image` + `centered full-body composition`（居中全身，裁切安全）
2. `clean ... background`（背景干净，适合手机壳贴图）
3. 手机壳素材用途：主体居中占 60-70%，四周留白
4. 同角色与壁纸提示词保持一致特征（发型/瞳色/服饰）

## 输出

1254×1254（1:1）JPG → 下载为 `raw/<role>_sq_raw.jpg` → 4K 转 `*_sq_4k.jpg`（3840×3840）
