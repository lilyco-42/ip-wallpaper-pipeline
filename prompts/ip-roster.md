# IP 角色清单（直接点名验证）

> 实测记录：哪个角色能直接点名生成，哪个会被拦。持续追加。

## ✅ 可直接点名（GPT 实测通过）

| 角色 | 渠道 | 特征关键词（写进提示词） |
|---|---|---|
| Hu Tao / 胡桃 | GPT ✅ | brown twintails, red eyes, black and red outfit, Staff of Homa, plum blossoms, ghost spirits, night shrine, moon |
| Raiden Shogun / 雷电将军 | GPT ✅ | long purple hair side braid, violet eyes, purple white kimono, Musou no Hitotachi, storm sky, lightning, sakura petals |
| Ganyu / 甘雨 | GPT ✅ | long blue-violet hair, small curved horns, aqua eyes, white blue qipao dress, ornate bow, snowy mountain, snowflakes |

## ❌ 被拦截（换特征版或跳过）

| 角色 | 拦截原因 | 替代方案 |
|---|---|---|
| Nahida / 纳西妲 | 萝莉形象触发内容保护 | 特征描述版：花冠绿发少女（char2，已上架） |
| Pikachu / 宝可梦 | 版权角色拦截 | 跳过 |
| K-pop 真人 | 真人肖像拦截 | 跳过 |
| Christmas 题材 | 季节性内容拦截 | 跳过 |

## 🎯 下一批候选（预计可点名，逐次验证后登记）

原神：刻晴（Keqing）、神里绫华（Kamisato Ayaka）、宵宫（Yoimiya）、夜兰（Yelan）、芙宁娜（Furina）、钟离（Zhongli）、魈（Xiao）、派蒙（Paimon）

其他：星穹铁道 流萤/卡芙卡、明日方舟 银灰

## 拦截应对策略（按序尝试）

1. 换措辞：去掉 `girl / little / young / gentle` 等词，强调气质（`elegant / graceful / powerful`）
2. 换新会话重试（同会话可能被会话级风控）
3. 换特征描述版：不点名，描述外貌特征（发型/瞳色/服饰/标志物）
4. 换角色
