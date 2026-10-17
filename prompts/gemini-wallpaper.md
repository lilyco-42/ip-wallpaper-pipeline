# Gemini 生图提示词模板

> Gemini（Google）与 GPT 双渠道并行：同一角色两条渠道各出 1 版，选图质量更高；渠道互备，GPT 被拦时可走 Gemini。

## Gemini 壁纸模板（9:16）

```text
Generate a vertical 9:16 phone wallpaper featuring <ROLE> from <GAME>,
with <LOOK_DETAILS>. She wears <OUTFIT>, holding <WEAPON/ITEM>,
<SCENE>. Style: official game art, anime illustration, highly detailed,
clean composition, no text, no watermark.
```

## Gemini 方形素材模板（1:1）

```text
Generate a square 1:1 image featuring <ROLE> from <GAME>, centered
full-body, <LOOK_DETAILS>, <OUTFIT>, <POSE>. Clean simple background.
Style: official game art, anime illustration, suitable as phone case art,
no text, no watermark.
```

## 建议（Gemini 生图特性）

1. Gemini（Imagen）对 IP 角色点名更宽松，适合 GPT 被拦的角色
2. 输出比例：在提示词中显式指定 `vertical 9:16` / `square 1:1`；如生成非目标比例，由 upscale4k.py 的 wallpaper/square 模式统一裁切
3. 生成后同样走：下载 → 4K → pub → 三平台

## 渠道分工建议

| 情况 | 用谁 |
|---|---|
| 常规角色 | GPT 优先（已验证点名成功） |
| GPT 被拦（萝莉/版权） | Gemini 重试一次 |
| 限流/额度紧张 | 切 Gemini |
| 同一角色要 2 个版本对比 | 双渠道各 1 版 |

## 下载

Gemini 出图后 blob/媒体 URL → 与 GPT 同法下载到 `raw/`（渠道后缀 `_gpt` / `_gem` 区分）。
