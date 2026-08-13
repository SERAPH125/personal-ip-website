# 南吴 NANWU 内容枢纽 · 开发说明

**源码仓库：** [SERAPH125/personal-ip-website](https://github.com/SERAPH125/personal-ip-website)（项目名：个人ip网站）

**发布与运维（日常怎么更新）：** 见 [`ops.md`](./ops.md) — 托管选型、首次发布、加作品/知识库剧本、缓存与回滚。

## 目标

AI 科技创作者的**内容枢纽**响应式 Web 站点：首页先说明「南吴是谁、做什么」→ 浏览系列作品 → 站内读文字版 / 外链看视频 → 直达抖音关注。

**硬约束：** 站内不集成播放；作品点击直达对应平台。

## 信息架构（4 屏 + 退役文件）

| 文件 | 屏 | 说明 |
|---|---|---|
| `index.html` | 首页 | **创作者定位优先**：南吴定位 + Codex 精选 + 关联知识文档；「接着看」三卡外链抖音 |
| `works.html` | 作品流 | 4 条静态作品卡；按 `agent / observe / aivideo` 系列筛选；每卡有视频与文字双入口 |
| `notes.html` | 知识库列表 | 5 篇文字经验；内容不足 12 篇时不加全文搜索 |
| `notes/codex-5-levels.html` | 文章详情 | Codex 5 级用法文字版（自抖音口述扩写） |
| `notes/fable-5-safety-lock.html` | 文章详情 | Fable 5 / Mythos 5 的安全机制与数字边界 |
| `notes/ai-storyboard-perspective.html` | 文章详情 | AI 短片第一/第三视角与提示词模板 |
| `notes/seedance-2-workflows.html` | 文章详情 | Seedance 2.0 四种工作流与提示词骨架 |
| `notes/ai-refund-fraud-report.html` | 文章详情 | AI 生成图片骗售后分析报告（源：`AI生成图片骗售后现象与商家应对分析报告.md`） |
| `about.html` | 关于 | 系列：Agent 实战 / 模型观察 / AI 视频；抖音入口 |
| `watch.html` | **已退役** | 保留文件；无入口 |

共享：`assets/hub.css`、`assets/hub.js`；视觉契约见 `brand-spec.md`。

结构参考：[withastro/starlight](https://github.com/withastro/starlight)（文档列表/阅读）、[HermanMartinus/bearblog](https://github.com/HermanMartinus/bearblog)（极简长文）。

## 已接入的抖音内容（南吴 NANWU）

生产内容源：`works.html` 的静态卡片（标题、系列、封面、短链、对应文章）。静态输出保证 JavaScript 失败或爬虫不执行脚本时仍能读取核心内容；`assets/hub.js` 只负责筛选、导航、toast 与封面后备。

| id | 标题摘要 | 短链 | 封面 |
|---|---|---|---|
| v1 | Codex 5 级用法 | `https://v.douyin.com/YIaxfdnPQeQ/` | `assets/covers/codex-5levels.jpg` |
| v2 | Fable 5 / Mythos | `https://v.douyin.com/sAoQQVUBtaM/` | `assets/covers/fable-5.jpg` |
| v3 | AI 短片分镜 | `https://v.douyin.com/-Hud8DcvLYs/` | `assets/covers/ai-storyboard.jpg` |
| v4 | Seedance 2.0 | `https://v.douyin.com/zrrR1ARupU4/` | `assets/covers/seedance-2.jpg` |

抖音主页：`https://www.douyin.com/user/MS4wLjABAAAAwwu7aqbhsXBribQpl5JPNTqXz-9ZRfmL2uZ8c70_l5JnwQsaYZJzGpk3ERvhzrA8`

## 如何爬取封面与简介（技能路径）

抖音短链有 WAF，**纯 curl 不稳定**；官方 `iteminfo` 常返回 `encrypt_data_miss`。本项目采用：

1. **skill · ego-browser**（推荐）  
   - 打开 `v.douyin.com/...` → 落页后取 `meta[name=description]` + `img[src*=origin_cover]`  
   - Seedance 等缺 `origin_cover` 时：对 `<video>` 画 canvas 截一帧落盘  
2. **开源备选**：[521w/douyin-mcp](https://github.com/521w/douyin-mcp)（`parse_douyin`）— MCP 当前未启用，需要时再接  
3. **知识库**：[[v2rayn-直连分流简明手册]] — 抖音建议直连，避免代理干扰抓取  

封面必须**下载到 `assets/covers/`** 用相对路径引用（勿热链抖音 CDN，签名会过期）。

## 外链交互

- 作品卡 / 精选：真实 `href` + `target="_blank"`；toast 提示「前往抖音观看」
- 作品卡的「读文字版」为站内链接；视频链接与文章链接并列，禁止嵌套 `<a>`
- 作品卡的两类操作均保持至少 44px 触控高度
- 首页 / 关于页的「去抖音关注」直接打开抖音主页，不再弹二次选择层；B站 / YouTube 在提供真实链接前不展示
- 封面加载失败会显示「封面暂不可用」后备状态，不显示破图图标

## 首页打磨（impeccable polish）

- 精选视频新增轻量 `.related-resource`：当前关联 `notes/codex-5-levels.html`，位于简介与行动按钮之间
- 关联资源规则：仅在确有对应产品/知识文档时显示，每条视频最多 1 条；资源链接与视频外链必须是并列链接，禁止嵌套 `<a>`
- 资源条保持无缩略图、无摘要、无常驻 accent；390px 下隐藏「阅读全文」，保留类型与标题
- 去掉「接着看」旁重复的「全部作品」链接（保留 hero 次级按钮）
- 封面只保留一个外链 chip，去掉第二枚浮层徽章
- 卡片 meta 改为「系列 · hook」；去掉无信息量的「短视频」角标
- 补：跳过链接、`:focus-visible`、`::selection`、窄屏按钮堆叠
- **polish2（本轮）：**
  - 首页首屏恢复创作者身份 eyebrow；H1 固定回答「南吴提供什么价值」，精选视频降为本期内容
  - 导航当前页背景态；页脚链接 hover/focus 对比不降
  - 「接着看」卡片：缩略图边框/阴影反馈；标题下划线；meta 不因 hover 变浅
  - 精选封面 `fetchpriority=high`；封面失败态撑满景深框
  - 关注 CTA 直达抖音主页，删除只包含一个平台的冗余弹层
  - 筛选 chip 触控高度 44px；主按钮 reduced-motion 取消按下位移

## 知识库（文字经验）

- IA：`list_detail`（列表 + 详情），导航标签固定为「知识库」
- 已有文章：
  1. `notes/codex-5-levels.html` — Agent 实战 · 与抖音精选同源，文末链回抖音（outbound）
  2. `notes/fable-5-safety-lock.html` — 模型观察 · 区分发布表述、官方资料与数字边界
  3. `notes/ai-storyboard-perspective.html` — AI 视频 · 两种视角与提示词模板
  4. `notes/seedance-2-workflows.html` — AI 视频 · 四种工作流与素材职责
  5. `notes/ai-refund-fraud-report.html` — 行业观察 · 含证据表、来源外链
- 新增文章：在 `notes/` 加 HTML，在 `notes.html` 加卡片，在对应 `works.html` 卡片加文字版链接，并同步 `rss.xml` / `sitemap.xml` / JSON-LD；长文表格用 `.article__table-wrap` 横向滚动
- 文章详情使用居中的 `42rem` 阅读列；面包屑、标题、正文和文末操作保持同一条左边线
- 5 篇阶段保持一眼能扫完的单列，不显示大号篇数和筛选区；约 12 篇时再接 [Pagefind](https://github.com/CloudCannon/pagefind) 静态全文索引
- 首页封面景深已改为纯 CSS 网格与柔光，不加载 `three.min.js` / WebGL / RAF；保留 28px（窄屏 18px）环带

## 全站背景（U1 · 已落地）

选型锁定：**Linear 点阵呼吸 + 径向柔光**（纯 CSS，无 npm 粒子库）。

| 层 | 选择器 | 作用 |
|---|---|---|
| 柔光 | `body::before` | 多层极淡 cobalt / cool-gray `radial-gradient`；慢漂 `site-glow-drift` |
| 点阵 | `body::after` | `radial-gradient` 点格 + `@property --site-dot-x/y/a` 相位漂移与透明度呼吸；边缘 mask 淡出 |

约束：

- `z-index: 0`、`pointer-events: none`；`.page` / `.site-footer` 抬到 `z-index: 1`，正文可读
- 不与首页 `cover_depth` 抢环带（opacity 克制）
- `prefers-reduced-motion: reduce` → 停相位/柔光动画，保留静帧点阵+柔光
- **禁止** Vanta、tsParticles、枢纽/星座、粒子海

参考（实现前对齐）：

- [Typed Halftone Background Drift](https://animationpatterns.art/animations/typed-halftone-background-drift/)（`@property` + 点阵相位，CC BY 4.0）
- [MDN · `@property`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Reference/At-rules/@property)（CSS Properties and Values / Typed OM）
- [Linear](https://linear.app)（点阵透明度 + 径向柔光气质）

选型对照页 `preview-bg-effects.html` 仍保留五套草稿对比；正式站已启用 U1。

## 刻意不做（首版）

商务询盘、邮件订阅、博客 CMS、站内播放器、全屏 WebGL 粒子背景、粒子库背景、当前阶段的站内搜索与框架迁移。

## 品牌（已锁）

站内显示名：**南吴 NANWU**（顶栏 `南吴` + `NANWU`）。

## 待你确认

1. 提供 B站 / YouTube 真实主页与对应长视频链接后，再公开相应入口

## 开源参考

- [astro-regulus](https://github.com/Batkixni/astro-regulus)
- [starfolio](https://github.com/webrating/starfolio)
- [withastro/starlight](https://github.com/withastro/starlight)（知识库列表/阅读结构）
- [HermanMartinus/bearblog](https://github.com/HermanMartinus/bearblog)（极简长文）
- [521w/douyin-mcp](https://github.com/521w/douyin-mcp)
- [mrdoob/three.js](https://github.com/mrdoob/three.js)（对照后移除首屏完整库，改为 CSS 静态景深）
- [CloudCannon/pagefind](https://github.com/CloudCannon/pagefind)（内容达到约 12 篇后的静态搜索预案）
- [wonderunit/storyboarder](https://github.com/wonderunit/storyboarder)（AI 分镜文章的开源工作流参照）
- [animationpatterns · Typed Halftone](https://animationpatterns.art/animations/typed-halftone-background-drift/)（U1 点阵 `@property` 相位）
- [MDN · `@property`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Reference/At-rules/@property)

## 本地预览

1. 打开 `index.html` → 首屏先见创作者定位；精选封面有 CSS 景深环带；「知识文档」进入 Codex 文章；关注直达抖音
2. `works.html` / `notes.html` / `about.html` → 同款 `hub.css` 背景  
3. 系统开「减少动态效果」→ 点阵相位停、柔光停，静帧保留  
4. `preview-bg-effects.html` → 历史五套对照 + U1 正式版说明（正式站已启用 U1）  

上线回归：

1. 浏览器打开 `tests/launch-readiness.html`，标题应为 `PASS · Launch readiness`
2. 运行 `python3 -m unittest discover -s tests -p 'test_*.py' -v`
3. 运行 `node --check assets/hub.js`（Python 测试缓存由 `.gitignore` 排除）
4. 检查 `robots.txt`、`sitemap.xml`、`rss.xml`、canonical、Open Graph、JSON-LD 与 favicon

## 发布与运维

上线后如何更新作品/知识库、选托管、缓存与回滚：见 **[`ops.md`](./ops.md)**。  
