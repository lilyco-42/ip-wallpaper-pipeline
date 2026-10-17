# 04 · 小红书发布 SOP

## 入口

`https://creator.xiaohongshu.com/publish/publish`（账号：Lilyco42）

## 固定配置

| 项 | 值 |
|---|---|
| 形式 | 图文（2 张：`*_wall_pub.jpg` + `*_sq_pub.jpg`） |
| 标题 | ≤20 字（超长会被截断/违规） |
| 正文 | 描述 + 6 个话题标签 |
| 引流 | 正文附夸克永久分享链接 |

## 步骤

1. 打开发布页 → 点「上传图文」tab (590,120)
2. 点上传区 (830,540) → `upload_file` 2 张 pub 图
3. JS 写标题（遍历 placeholder 含「填写标题」的 input，原生 setter + input 事件）
4. JS 写正文（第一个 contenteditable，execCommand insertText）
5. 点 (500,340) 关话题弹窗
6. JS scroll `.publish-page` 到底 → 点发布 (855,940)
7. **成功标志**：跳回「上传视频」页

## 标题模板（≤20字）

```
4K壁纸 <角色特征词>
4K壁纸 <角色>风格
```

例：`4K壁纸 双马尾红瞳少女` / `4K壁纸 雷电将军风格`

## 正文模板

见 templates/xhs_body.txt。核心话题：#原神 #壁纸 #手机壁纸 #4k壁纸 #手机壳 #二次元

## 踩坑

- 发布按钮在编辑页右下角；顶部导航「发布笔记」是切类型菜单，不是发布
- 标题 20 字限制硬性
- 正文带链接时确保换行清晰，避免被当广告折叠

## 数据复盘（每 3 天）

笔记管理页 `creator.xiaohongshu.com/new/note-manager` 看浏览/赞/藏/评：
- 赞>20 → 加产同风格
- 评>3 → 评论区置顶夸克链接
- 48h 浏览<30 → 换角色方向
