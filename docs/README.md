# 南吴 NANWU 内容枢纽 · 开发说明

**源码仓库：** [SERAPH125/personal-ip-website](https://github.com/SERAPH125/personal-ip-website)

**发布运维：** 见 [`ops.md`](./ops.md)

## 技术基线

本站已从手写 HTML 迁移为 **Astro 7 + Markdown Content Collections**。作者维护 `src/content/notes/*.md`；Astro 在构建时生成静态 HTML、知识库列表、作品卡、RSS、sitemap 与 JSON-LD。

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
├── content/notes/*.md      # 5 篇文章的唯一正文来源
├── components/             # 导航、页脚、文章卡、视频卡
├── layouts/                # 全站 head 与文章阅读模板
├── lib/site.ts             # 系列、URL、日期等共享配置
└── pages/                  # 首页、作品、知识库、关于、文章动态路由、RSS
public/
├── assets/                 # CSS、JS 与封面
├── robots.txt
└── tests/launch-readiness.html
astro.config.mjs            # GitHub Pages base、.html 输出、sitemap
.github/workflows/deploy.yml
```

`dist/` 是构建产物，不提交 Git。

## 内容模型

5 篇 Markdown 同时驱动知识库和作品页：

| Markdown | 系列 | 视频 |
|---|---|---|
| `codex-5-levels.md` | `agent` | 抖音 |
| `fable-5-safety-lock.md` | `observe` | 抖音 |
| `ai-storyboard-perspective.md` | `aivideo` | 抖音 |
| `seedance-2-workflows.md` | `aivideo` | 抖音 |
| `ai-refund-fraud-report.md` | `industry` | 无 |

必填 Frontmatter：`title`、`description`、`publishedAt`、`series`、`sequence`、`cover`、`coverAlt`。有视频时增加 `video.platform / url / title / hook`。schema 在构建前验证字段与类型。

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

`npm test` 会先执行 Astro build，再运行 Python 契约测试，检查 5 篇文章、旧 `.html` URL、站内资源、RSS、sitemap、JSON-LD 与视频/文字双入口。

## 视觉与交互

- 全站背景仍为纯 CSS 点阵呼吸 + 径向柔光；`prefers-reduced-motion` 下停止动画；
- 首页封面景深为 CSS，不加载 Three.js/WebGL；
- `public/assets/hub.js` 只负责移动导航、作品筛选、结果播报、外链 toast 与封面失败后备；
- 内容未达到约 12 篇前不接全文搜索，达到阈值后优先评估开源 [Pagefind](https://github.com/CloudCannon/pagefind)。

## 当前公开入口

- 首页：`index.html`
- 作品：`works.html`
- 知识库：`notes.html`
- 关于：`about.html`
- RSS：`rss.xml`
- sitemap：`sitemap-index.xml`
- 浏览器自检：`tests/launch-readiness.html`
