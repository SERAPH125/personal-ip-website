# 南吴 NANWU 内容枢纽 · 开发说明

**源码仓库：** [SERAPH125/personal-ip-website](https://github.com/SERAPH125/personal-ip-website)（项目名：个人ip网站）

**发布与运维（日常怎么更新）：** 见 [`ops.md`](./ops.md) — 托管选型、首次发布、加作品/知识库剧本、缓存与回滚。

## 目标

AI 科技创作者的**内容枢纽**响应式 Web 原型：认识创作者 → 浏览作品 → **外链到平台观看** → 在关于页完成「关注」。

**硬约束：** 站内不集成播放；作品点击直达对应平台。

## 信息架构（4 屏 + 退役文件）

| 文件 | 屏 | 说明 |
|---|---|---|
| `index.html` | 首页 | **最新片优先**：Codex 五级用法作精选；「接着看」三卡外链抖音；知识库仅顶栏入口 |
| `works.html` | 作品流 | 4 条抖音真片 + 平台/系列筛选 |
| `notes.html` | 知识库列表 | 文字经验入口；顶栏文案「知识库」 |
| `notes/codex-5-levels.html` | 文章详情 | Codex 5 级用法文字版（自抖音口述扩写） |
| `notes/ai-refund-fraud-report.html` | 文章详情 | AI 生成图片骗售后分析报告（源：`AI生成图片骗售后现象与商家应对分析报告.md`） |
| `about.html` | 关于 | 系列：Agent 实战 / 模型观察 / AI 视频 |
| `watch.html` | **已退役** | 保留文件；无入口 |

共享：`assets/hub.css`、`assets/hub.js`；视觉契约见 `brand-spec.md`。

结构参考：[withastro/starlight](https://github.com/withastro/starlight)（文档列表/阅读）、[HermanMartinus/bearblog](https://github.com/HermanMartinus/bearblog)（极简长文）。

## 已接入的抖音内容（南吴 NANWU）

数据源：`assets/hub.js` → `videos[]`（标题、简介、封面、短链）。

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
- 「关注我」→ 抖音主页已接真链；B站 / YouTube 仍占位（虚线态 + toast）
- 封面加载失败会替换为「封面暂不可用」占位，不显示破图图标

## 首页打磨（impeccable polish）

- 去掉「接着看」旁重复的「全部作品」链接（保留 hero 次级按钮）
- 封面只保留一个外链 chip，去掉第二枚浮层徽章
- 卡片 meta 改为「系列 · hook」；去掉无信息量的「短视频」角标
- 补：跳过链接、弹层焦点返回/Tab 陷阱、`:focus-visible`、`::selection`、窄屏按钮堆叠
- **polish2（本轮）：**
  - 去掉 hero kicker/eyebrow（信息并入 lede「抖音最新一期」）
  - 导航当前页背景态；页脚链接 hover/focus 对比不降
  - 「接着看」卡片：缩略图边框/阴影反馈；标题下划线；meta 不因 hover 变浅
  - 精选封面 `fetchpriority=high`；封面失败态撑满景深框
  - 关注弹层 `aria-describedby`；关闭按钮成对 hover 色
  - 筛选 chip 触控高度 44px；主按钮 reduced-motion 取消按下位移

## 知识库（文字经验）

- IA：`list_detail`（列表 + 详情），导航标签固定为「知识库」
- 已有文章：
  1. `notes/codex-5-levels.html` — Agent 实战 · 与抖音精选同源，文末链回抖音（outbound）
  2. `notes/ai-refund-fraud-report.html` — 行业观察 · 自项目根目录 Markdown 报告入库；含证据表、来源外链
- 新增文章：在 `notes/` 加 HTML，并在 `notes.html` 列表加一条卡片；长文表格用 `.article__table-wrap` 横向滚动
- 列表打磨（impeccable）：去掉双语 eyebrow；系列筛选（`?series=agent|industry`）+ 空态；篇数实时更新；卡片 hover/active/focus；窄屏内边距收紧
- 动效（gsap-performance）：`notes.html` 加载 GSAP 3.13 + `assets/notes-motion.js`
  - 只动 `y` / `autoAlpha`（不动画 height/padding）
  - 入场：标题 → 筛选 → 卡片 stagger；筛选切换 kill 旧 timeline 再淡出/淡入
  - `gsap.matchMedia` 尊重 `prefers-reduced-motion`（即时显示）
  - `will-change` 仅在 `.notes-animating` 期间开启；卡片 hover 去掉按下位移，箭头用 transform
- 首页 WebGL（`cover_depth`）：`assets/home-cover-three.js` + 本地 UMD `assets/vendor/three.min.js`（**three r160**）
  - 仅衬精选封面：双层 `GridHelper` 景深，封面 inset **28px**（窄屏 18px）露出网格环带
  - 网格 opacity near≈0.72 / far≈0.45；相机略俯视，环带可读
  - 指针微倾角；`prefers-reduced-motion` → 静帧；DPR≤1.5；切后台停环
  - 无 WebGL 时加 `.hero-media--no-webgl`，封面恢复满铺
  - **坑：** `three@0.161+` 已删除 `build/three.min.js`；旧 CDN 会 404
  - **坑：** inset 过小（曾 10px）时环带约 6% 面积 + 低对比 → 用户以为「没效果」
  - **不做：** 枢纽星座、全屏 Vanta/粒子墙、知识库 WebGL

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

商务询盘、邮件订阅、博客 CMS、站内播放器、全屏 WebGL 粒子背景、粒子库背景。

## 品牌（已锁）

站内显示名：**南吴 NANWU**（顶栏 `南吴` + `NANWU`）。

## 待你确认

1. B站 / YouTube 主页与对应长视频链接

## 开源参考

- [astro-regulus](https://github.com/Batkixni/astro-regulus)
- [starfolio](https://github.com/webrating/starfolio)
- [withastro/starlight](https://github.com/withastro/starlight)（知识库列表/阅读结构）
- [HermanMartinus/bearblog](https://github.com/HermanMartinus/bearblog)（极简长文）
- [521w/douyin-mcp](https://github.com/521w/douyin-mcp)
- [mrdoob/three.js](https://github.com/mrdoob/three.js)（封面景深网格）
- [animationpatterns · Typed Halftone](https://animationpatterns.art/animations/typed-halftone-background-drift/)（U1 点阵 `@property` 相位）
- [MDN · `@property`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Reference/At-rules/@property)

## 本地预览

1. 打开 `index.html` → 应见全站点阵+柔光；精选封面景深环带仍在；点封面新开抖音  
2. `works.html` / `notes.html` / `about.html` → 同款 `hub.css` 背景  
3. 系统开「减少动态效果」→ 点阵相位停、柔光停，静帧保留  
4. `preview-bg-effects.html` → 历史五套对照 + U1 正式版说明（正式站已启用 U1）  

## 发布与运维

上线后如何更新作品/知识库、选托管、缓存与回滚：见 **[`ops.md`](./ops.md)**。  
