# 05 · 夸克网盘上传分享 SOP

## 两种通道

### A. 网页版（免 CLI，适合一次性）

1. 打开 `https://pan.quark.cn/` → 扫码登录（夸克 App）
2. 点「新建文件夹」→ 右键文件夹 → 重命名（如「4K高清壁纸粉丝下载」）
3. 进入文件夹 → `upload_file("input[type='file']", 路径)` 逐张上传 4K 原图
4. 回上级 → 右键文件夹 → 分享 → **永久有效 + 不需要提取码** → 创建分享
5. 复制链接：`https://pan.quark.cn/s/<code>`

### B. kuake CLI（推荐，可脚本化）

```powershell
# 1. 下载（已放 tools/）
#    https://github.com/zhangjingwei/kuake_sdk/releases/latest/download/kuake-v1.5.0-windows-amd64.exe
# 2. 配置 cookie（登录 pan.quark.cn 后，F12 → Network → 任意请求 Cookie 头，完整复制）
$env:KUAKE_COOKIE="__pus=xxx; __puus=xxx; ..."   # 或 --cookies 参数（自动加 __pus= 前缀）

# 3. 验证
.\tools\kuake.exe user

# 4. 创建文件夹
.\tools\kuake.exe create "4K高清壁纸粉丝下载" "/"

# 5. 上传（注意：只能单文件，文件夹先压缩或用脚本循环）
.\tools\kuake.exe upload "out/hutao_wall_4k.jpg" "/4K高清壁纸粉丝下载/hutao_wall_4k.jpg"

# 6. 永久分享（0 天 = 永久）
.\tools\kuake.exe share "/4K高清壁纸粉丝下载" 0 "false"
```

一键上传封装见 `tools/kuake_upload.ps1`。

## 命名规范

夸克文件夹建议按「角色」归档，每角色 2 张 4K 原图：
```
4K高清壁纸粉丝下载/
├── hutao_wall_4k.jpg / hutao_sq_4k.jpg
├── raiden_wall_4k.jpg / raiden_sq_4k.jpg
└── ganyu_wall_4k.jpg / ganyu_sq_4k.jpg
```

## 已生成分享（持续更新）

| 时间 | 文件夹 | 链接 |
|---|---|---|
| 2026-10-17 | 4K高清壁纸粉丝下载（12张） | https://pan.quark.cn/s/f9e8e8b9ddf5 |

## 踩坑

- CLI 命令参数必须加引号（`upload "file" "dest"`）
- CLI 只能上传单文件；文件夹需 zip 或循环
- 网页重命名：右键菜单（JS hover 不触发，必须真实右键 `right_single`）
- 分享链接永久有效需手动选「永久有效」（默认 30 天）
