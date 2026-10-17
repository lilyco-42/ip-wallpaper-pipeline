# IP 壁纸变现流水线（AIGC → 4K → 多平台分发）

> 一条把「AI 生图」变成「零边际成本数字商品」的完整流水线。
> **GPT + Gemini 双渠道生图 → 本地转 4K → 闲鱼 / 小红书 / 夸克网盘 三平台分发。**
> 商品形态：手机壁纸（9:16 竖屏 4K）+ 手机壳素材（1:1 方形 4K），¥7.7/份。

---

## 为什么是这条路

| 维度 | 结论（实测） |
|---|---|
| 成本 | 生图额度免费，边际成本 ≈ 0 |
| 渠道 | 闲鱼卖货 + 小红书引流 + 夸克网盘供粉丝下载高清原图 |
| 速度 | 单角色全流程 ≈ 15 分钟（生成→4K→三平台） |
| 复利 | 商品/笔记/网盘素材永久积累，一次生成多次曝光 |

---

## 流水线总览（一条命令一份商品）

```
① 生图 (GPT / Gemini)
   └─ 直接点名热门 IP 角色（Hu Tao / Raiden Shogun / Ganyu …）
   └─ 每角色 2 张：9:16 壁纸 + 1:1 方形素材
② 本地 4K 放大 (tools/upscale4k.py)
   └─ 壁纸 → 2160×3840 (q95 JPEG)
   └─ 方形 → 3840×3840 (q95 JPEG)
   └─ 另出 1080px 上传预览版 (tools/make_pub.py)
③ 闲鱼上架 (goofish.com/publish)
   └─ 分类「电子资料」｜价格 ¥7.7 / 原价 12
   └─ 描述含「手机壁纸」关键字（分类映射关键）
④ 小红书发布 (creator.xiaohongshu.com)
   └─ 标题 ≤20 字｜正文带 #原神 #壁纸 #4k壁纸 #手机壳 话题
   └─ 附夸克网盘链接供粉丝下载高清原图
⑤ 夸克网盘归档 (tools/kuake_upload.ps1)
   └─ 上传 4K 原图 → 永久分享链接（无需提取码）
⑥ 台账登记 (data/listings.csv)
   └─ 商品 ID / 角色 / 状态，防止重复铺货
```

---

## 目录结构

```
ip-wallpaper-pipeline/
├── README.md              ← 你在这里
├── workflow/              ← 各环节 SOP（照做即可）
│   ├── 00-overview.md       流水线总览与排期
│   ├── 01-generate.md       GPT/Gemini 生图 SOP
│   ├── 02-upscale4k.md      4K 放大 SOP
│   ├── 03-goofish.md        闲鱼上架 SOP
│   ├── 04-xiaohongshu.md    小红书发布 SOP
│   └── 05-quark.md          夸克网盘上传分享 SOP
├── prompts/               ← 提示词库（实测有效）
│   ├── ip-roster.md         已验证角色清单 + 拦截黑名单
│   ├── gpt-wallpaper.md     GPT 壁纸提示词模板
│   ├── gpt-square-art.md    GPT 方形素材提示词模板
│   └── gemini-wallpaper.md  Gemini 生图提示词模板
├── tools/                 ← 可复现脚本
│   ├── upscale4k.py          4K 放大（Lanczos + 锐化）
│   ├── make_pub.py           生成 1080px 上传预览版
│   └── kuake_upload.ps1      夸克 CLI 上传 + 分享封装
├── templates/             ← 上架文案模板
│   ├── goofish_desc.txt      闲鱼描述模板
│   ├── xhs_title.txt         小红书标题模板（≤20字）
│   └── xhs_body.txt          小红书正文模板
├── data/
│   └── listings.csv          商品台账（持续追加）
└── docs/
    └── pitfalls.md           踩坑记录（避免重复犯错）
```

---

## 快速开始

```powershell
# 1. 4K 放大（壁纸）
python tools/upscale4k.py raw/hutao_wall.jpg out/hutao_wall_4k.jpg wallpaper
# 2. 4K 放大（方形素材）
python tools/upscale4k.py raw/hutao_sq.jpg out/hutao_sq_4k.jpg square
# 3. 上传预览版
python tools/make_pub.py out/ out/pub/
# 4. 夸克上传 + 永久分享（需 KUAKE_COOKIE 环境变量）
$env:KUAKE_COOKIE="__pus=xxxx;"
.\tools\kuake_upload.ps1 -Folder "out/4K高清壁纸粉丝下载"
```

依赖：Python 3.13 + Pillow（`pip install pillow`）；kuake.exe（夸克网盘 CLI，见 workflow/05-quark.md）。

---

## 已验证数据（2026-10-17）

- 直接点名成功：**Hu Tao / Raiden Shogun / Ganyu**（原神）；被拦：Nahida（萝莉触发保护）
- 闲鱼累计 76+ 商品、小红书 300+ 笔记
- 小红书最佳数据：雪山白角 21 赞 / 甘雨 3 评论 14 赞 14 藏
- 夸克网盘永久分享：`https://pan.quark.cn/s/f9e8e8b9ddf5`（12 张 4K 原图）

## License

本仓库脚本与工作流为作者原创，MIT 协议；生成图片的 IP 版权归原 IP 权利人，仅供个人创作参考。
