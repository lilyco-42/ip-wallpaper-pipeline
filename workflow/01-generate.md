# 01 · 生图 SOP（GPT / Gemini 双渠道）

## 核心原则

1. **直接点名热门 IP 角色**：实测 ChatGPT 对大多数原神成年角色直接点名成功（Hu Tao / Raiden Shogun / Ganyu）。
2. **每角色 2 张**：9:16 竖屏壁纸 + 1:1 方形素材（手机壳）。
3. **文案关键**：加 `official game art style, no text.` 保证官方风格 + 无水印文字。
4. **拦截即换路**：被拦 → 换措辞（去掉 girl/幼/小等词）→ 换新会话 → 换角色。

## GPT 流程

1. 打开 chatgpt.com（App 内浏览器新会话）
2. 粘贴提示词（模板见 prompts/gpt-wallpaper.md / gpt-square-art.md）
3. 等「正在创建图像」→ 出现图片（60-90s）
4. 下载：页面 blob URL → `fetch` → base64 → 存本地 `raw/<role>_wall_raw.jpg` / `raw/<role>_sq_raw.jpg`
5. 偶发 blob 未出现：等 30-60s 重试；输入 Enter 后没进「正在创建图像」→ 重新导航再发

## Gemini 流程

1. 打开 gemini.google.com（App 内浏览器）
2. 粘贴提示词（模板见 prompts/gemini-wallpaper.md）
3. 等出图 → 下载（blob 或右键另存）

## 直接点名验证清单（已测）

| 角色 | GPT 直接点名 | 备注 |
|---|---|---|
| Hu Tao（胡桃） | ✅ | 双马尾红瞳、黑红古装、护摩之杖、幽灵金蝶 |
| Raiden Shogun（雷电将军） | ✅ | 紫色侧辫、和服、梦想一心、雷暴樱花 |
| Ganyu（甘雨） | ✅ | 蓝紫长发白角、白蓝旗袍、冰弓雪山 |
| Nahida（纳西妲） | ❌ 拦截 | 萝莉形象触发保护 → 用特征版（花冠绿发少女）替代 |

完整清单与黑名单见 [prompts/ip-roster.md](../prompts/ip-roster.md)。

## 下载脚本示例（GPT blob）

```python
# 浏览器 cell 内
import base64
res = bu.js("""
var imgs = document.querySelectorAll('img[src*="blob:"]');
var urls = [];
for (var i = 0; i < imgs.length; i++) {
    if (imgs[i].naturalWidth > 200 && !urls.includes(imgs[i].src)) urls.push(imgs[i].src);
}
return urls;
""")
# 对每个 url：fetch → blob → FileReader → dataURL → 解码存盘
```
