# kuake_upload.ps1 — 夸克网盘 CLI 一键上传封装
# 依赖：tools/kuake.exe (kuake_sdk v1.5.0)
# 认证：环境变量 KUAKE_COOKIE（登录 pan.quark.cn 后 F12 复制 Cookie 头），或 -Cookie 参数
#
# 用法：
#   $env:KUAKE_COOKIE="__pus=xxx; __puus=xxx; ..."
#   .\tools\kuake_upload.ps1 -Folder "C:\path\to\4k_folder" -RemoteDir "4K高清壁纸粉丝下载"
#   .\tools\kuake_upload.ps1 -Files "a.jpg","b.jpg" -RemoteDir "test"
#   .\tools\kuake_upload.ps1 -Share "/4K高清壁纸粉丝下载"   # 创建永久分享

param(
    [string]$Folder = "",
    [string[]]$Files = @(),
    [string]$RemoteDir = "4K高清壁纸粉丝下载",
    [string]$Share = "",
    [string]$Cookie = "",
    [int]$ShareDays = 0
)

$kuake = Join-Path $PSScriptRoot "kuake.exe"
if (-not (Test-Path $kuake)) {
    Write-Error "kuake.exe not found at $kuake — download from https://github.com/zhangjingwei/kuake_sdk/releases"
    exit 1
}

# auth env
if ($Cookie) {
    $env:KUAKE_COOKIE = $Cookie
}
if (-not $env:KUAKE_COOKIE) {
    Write-Warning "KUAKE_COOKIE not set. Run:  login pan.quark.cn → F12 → copy Cookie header →  \$env:KUAKE_COOKIE='...'"
}

function Run-Kuake([string[]]$ArgsList) {
    $out = & $kuake @ArgsList 2>&1
    $code = $LASTEXITCODE
    if ($code -ne 0) {
        Write-Warning "kuake $($ArgsList[0]) failed (exit $code): $($out -join ' ')"
    } else {
        Write-Host "kuake $($ArgsList[0]) OK"
    }
    return $out
}

# verify login
$userOut = Run-Kuake @("user")
Write-Host ($userOut | Select-Object -First 5)

# create remote dir (idempotent-ish: ignore 'exists' error)
if ($Folder -or $Files.Count -gt 0) {
    Run-Kuake @("create", $RemoteDir, "/") | Out-Null
}

# upload folder (single files)
if ($Folder) {
    Get-ChildItem $Folder -File | ForEach-Object {
        $dest = "/$RemoteDir/$($_.Name)"
        Run-Kuake @("upload", $_.FullName, $dest)
    }
}

# upload explicit files
foreach ($f in $Files) {
    $name = Split-Path $f -Leaf
    $dest = "/$RemoteDir/$name"
    Run-Kuake @("upload", $f, $dest)
}

# create share (permanent by default)
if ($Share) {
    $passcode = "false"
    $out = Run-Kuake @("share", $Share, $ShareDays, $passcode)
    $out | ForEach-Object { Write-Host $_ }
}
