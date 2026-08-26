# 南吴 NANWU 内容枢纽 · 开发说明

**源码仓库：** [SERAPH125/personal-ip-website](https://github.com/SERAPH125/personal-ip-website)

**发布运维：** 见 [`ops.md`](./ops.md)

## 技术基线

本站已从手写 HTML 迁移为 **Astro 7 + Markdown Content Collections**。作者维护 `src/content/notes/*.md` 和 `src/content/tools/*.md`；Astro 在构建时生成静态 HTML、知识库列表、工具目录、作品卡、RSS、sitemap 与 JSON-LD。

仍保持两条产品约束：

- 站内不嵌入抖音播放器，视频按钮打开真实平台链接；
- 现有公开地址继续使用 `.html`，例如 `notes/codex-5-levels.html`，避免旧外链失效。

开源参照：

- [Astro Content Collections](https://docs.astro.build/en/guides/content-collections/)：Markdown schema、查询与静态路由；
- [AstroPaper](https://github.com/satnaing/astro-paper)：Markdown、RSS、SEO 与可访问博客结构；
- [Tailwind Typography](https://github.com/tailwindlabs/tailwindcss-typography)：正文标题、段距、引用、表格的比例参照；本站使用原生 CSS 实现，没有引入 Tailwind。

## 目录

```text
src/
├── content.config.ts       # Frontmatter schema
├── content/notes/*.md      # 17 篇知识文章的唯一正文来源
├── content/tools/*.md      # 8 篇 AI 工具指南的唯一正文来源
├── components/             # 导航、页脚、文章卡、工具卡、视频卡
├── layouts/                # 全站 head、文章与工具指南阅读模板
├── lib/site.ts             # 系列、URL、日期等共享配置
└── pages/                  # 首页、作品、路线、工具、知识库、动态路由与 RSS
public/
├── assets/                 # CSS、JS、文章封面与工具图解
├── robots.txt
└── tests/launch-readiness.html
astro.config.mjs            # GitHub Pages base、.html 输出、sitemap
.github/workflows/deploy.yml
```

`dist/` 是构建产物，不提交 Git。

## 内容模型

17 篇 Markdown 同时驱动知识库、学习路线和作品页：

| 内容组 | 数量 | 用途 |
|---|---:|---|
| 既有文章 | 5 | 4 篇带抖音视频，1 篇行业观察 |
| Vibe Coding 路线 | 6 | `learning.track: vibe-coding`，步骤 1—6 |
| AI 视频路线 | 6 | `learning.track: ai-video`，步骤 1—6 |

必填 Frontmatter：`title`、`description`、`publishedAt`、`series`、`sequence`、`cover`、`coverAlt`。有视频时增加 `video.platform / url / title / hook`。路线文章还要增加 `sourcesCheckedAt` 和 `learning.track / step`；普通文章可不填 `learning`。schema 会在构建前验证字段、路线枚举和 1—6 的步骤范围。

12 张路线封面位于 `public/assets/covers/learning-vibe-01.png` 至 `learning-vibe-06.png`、`learning-video-01.png` 至 `learning-video-06.png`。封面是仓库内静态资源，不使用外链。

## AI 工具指南

工具指南使用独立的 `tools` collection，不混入知识库和 RSS。第一批固定 8 个 slug：`codex`、`cursor`、`ollama`、`comfyui`、`trae`、`cherry-studio`、`deepseek`、`kling-ai`。目录页为 `tools.html`，详情页为 `tools/<slug>.html`，全部保持 GitHub Pages 的文件式 URL。

每篇 `src/content/tools/*.md` 必填：

- 标题与摘要：`title`、`toolName`、`description`、`audience`、`setupSummary`、`privacySummary`；
- 分类：`origin`、`category`、`accessTypes`、`platforms`、`pricing`；
- 可信度：`openSource`、`license`、`officialUrl`、可选 `downloadUrl / repositoryUrl`、`versionChecked`、`verifiedAt`；
- 展示：`cover`、`coverAlt`、唯一的 `sequence`、`draft`。

图片放在 `public/assets/tools/<slug>/`。每篇至少四张本地图片：布局读取 Frontmatter 中的 16:9 封面，正文再引用流程图和两个关键步骤视觉。正文 Markdown 图片使用 `/personal-ip-website/assets/tools/...`，确保 GitHub Pages 子路径部署不丢图；每张图必须有具体 alt。官方截图只取公开页面并移除账号信息，截图后紧邻标注可点击的官方来源和截取日期；原创界面结构图必须明确写“示意、以官网为准”，不能冒充真实产品截图。费用与隐私章节至少链接一项产品官方隐私、FAQ、服务条款或安全策略，便于读者自行复核。

`tools.html` 在桌面端采用 Hugging Face 文档式左侧粘性模型目录，按语言模型、图片模型、AI 编程、视频模型四类列出 8 个工具名称；点击名称锚点定位到右侧同类卡片，右侧各分类使用两列卡片。820px 以下目录改为默认折叠的原生 `details`，选择工具后自动收起；640px 以下卡片单列。命令行文章的代码块由 `public/assets/hub.js` 渐进增强为可复制。JavaScript 失效时，桌面目录保持展开，8 张卡片、全部正文和代码仍可读取。首页正文不增加工具入口，唯一入口是全站主导航中的“工具指南”。RSS 仍只包含 17 篇知识文章，不包含安装手册。

## 学习路线与筛选

- `learn.html` 固定先展示 Vibe Coding，再展示 AI 视频；每条路线按 `learning.step` 排序；
- 桌面端学习路线页采用 Hugging Face 文档式左侧粘性目录，目录按路线分组列出 12 个步骤；820px 以下改为默认折叠的原生学习目录，选择步骤后自动收起；
- 首页只展示两张路线入口卡，不重复展开 12 篇文章；
- 知识库包含 `all / agent / observe / aivideo / industry` 五种筛选，并播报当前结果数；
- 作品页和知识库共用 `public/assets/hub.js` 的系列筛选逻辑，`?series=` 可分享当前筛选；
- 文章详情仍使用 `notes/<slug>.html`，学习路线不会产生重复正文或重复 canonical。

## 文章阅读模板

文章由 `src/layouts/ArticleLayout.astro` 统一渲染：

- 文章整体在页面中轴居中，点阵背景外层保留，正文进入高不透明阅读纸面；
- 阅读列最大 `42rem`，桌面正文 `17px / 1.9`，二级标题增加段前留白；
- 根据 Markdown headings 自动生成目录；
- 视频文章自动生成带封面的抖音入口；
- Markdown 的列表、引用、表格、行内代码和代码块都有统一样式；
- 前后篇、canonical、BlogPosting 与 BreadcrumbList 自动生成。

## 本地开发

```bash
npm ci
npm run dev
```

浏览器打开终端给出的本地地址。完整验证：

```bash
npm run check
npm test
node --check public/assets/hub.js
git diff --check
```

`npm test` 会先执行 Astro build，再运行 Python 契约测试，检查 17 篇文章、8 篇工具指南、两条完整路线、旧 `.html` URL、站内图片、RSS、sitemap、JSON-LD、筛选与首页排除规则。Pull Request 到 `main` 时，GitHub Actions 会运行 Astro、浏览器 JavaScript 语法和完整测试但不会部署；PR 按编号使用独立并发队列，不会取消 `main` 的生产发布，只有推送到 `main` 才执行 Pages 发布。

## 视觉与交互

- 全站背景仍为纯 CSS 点阵呼吸 + 径向柔光；`prefers-reduced-motion` 下停止动画；
- 首页封面景深为 CSS，不加载 Three.js/WebGL；
- `public/assets/hub.js` 只负责移动导航、知识库/作品筛选、代码复制、回到顶部、结果播报、外链 toast 与封面失败后备；工具目录本身使用静态锚点导航；
- 当前 17 篇仍可通过两条路线和系列筛选定位，不接全文搜索；达到约 30 篇或出现明确搜索需求时，优先评估开源 [Pagefind](https://github.com/CloudCannon/pagefind)。

## 当前公开入口

- 首页：`index.html`
- 作品：`works.html`
- 学习路线：`learn.html`
- AI 工具指南：`tools.html`（详情：`tools/<slug>.html`）
- 知识库：`notes.html`
- 关于：`about.html`
- RSS：`rss.xml`
- sitemap：`sitemap-index.xml`
- 浏览器自检：`tests/launch-readiness.html`
