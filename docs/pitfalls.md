# 踩坑记录（避免重复犯错）

## 生图
- ChatGPT 拦宝可梦/Pikachu、K-pop 真人、Christmas、Nahida 等萝莉角色 → 换角色或特征描述
- 直接点名原神成年角色（胡桃/雷电将军/甘雨）成功率高；被拦时去掉 `girl/little/young` 等词
- blob 未出现时等 30-60s 重试；输入 Enter 后没进「正在创建图像」→ 重新导航再发

## 闲鱼
- 实物类目（徽章/钥匙扣/贴纸等）网页版全部「暂不支持发布此分类，请用APP扫码」→ 重载页面 + 描述以「手机壁纸」开头重新映射
- 分类下拉：`#rc_select_0` mousedown → 遍历 `.ant-select-item-option`，文案必须完全匹配 `=== '电子资料'`；不在选项时换「电子壁纸」
- 发布按钮偶尔第一次不生效 → 滚到底后重试 click 或 click_xy(500,930)
- 上传图片：主图位 (145,330)、缩略图位 (235,330)，传完点 (970,50) 关预览
- 发布成功标志 = URL 跳转 `item?id=<ID>`

## 小红书
- 发布按钮在编辑页右下角「发布」；顶部导航「发布笔记」是切类型菜单
- 标题限 20 字
- 上传图文：切 tab (590,120) → 点上传区 (830,540) → upload_file 2 张 → JS 写标题（input setter+事件）→ JS 写正文（contenteditable insertText）→ 点 (500,340) 关话题 → scroll .publish-page 到底 → 发布 (855,940)
- 发布成功标志 = 跳回「上传视频」页

## 夸克
- kuake CLI 只支持单文件上传；文件夹需 zip 或脚本循环（见 tools/kuake_upload.ps1）
- 网页重命名必须真实右键（right_single），JS dispatchEvent hover 不触发
- 分享默认 30 天 → 必须手动选「永久有效」
- CLI v1.5.0：KUAKE_COOKIE 完整 cookie 或 KUAKE_PUS+KUAKE_PUUS split；--cookies 自动加 __pus= 前缀
- Cookie 有效期：__pus/__puus 约 13 天（2026-10-30 到期），过期后需重新导出

## 浏览器自动化
- BU_SESSION_STALE / BU_NO_ACTIVE_PAGE → bu.resync()（有时需重试）
- COMMAND_TIMEOUT 常见 → 重发即可
- ref 随页面重载失效 → 重新 snapshot
