# 发布与运维 · 南吴 NANWU

本站是 **Astro 构建的静态站**：没有数据库、CMS 或站内播放器。日常更新只改 Markdown 和本地封面；列表、作品卡、RSS、sitemap、JSON-LD 与前后篇由构建自动同步。

## 1. 日常发文

1. 在 `src/content/notes/` 新建 `slug.md`，复制任一现有 Frontmatter；`sequence` 使用当前最大值 + 1。
2. 正文直接写标准 Markdown：`##` 标题、列表、引用、表格、代码块都由文章模板统一排版。
3. 封面放到 `public/assets/covers/`，Frontmatter 写 `cover: "assets/covers/文件.jpg"`；禁止热链带签名的抖音 CDN。
4. 有视频就填写 `video`；没有视频则完全删除该对象，页面不会渲染空入口。
5. 路线文章填写 `sourcesCheckedAt` 与 `learning.track / step`；普通文章不需要 `learning`。
6. 运行 `npm run check && npm test`；通过后提交。功能分支可先推送并通过 Pull Request 检查，合并 `main` 后才会部署。

最小模板：

```md
---
title: "文章标题"
description: "用于列表、SEO 与文章导语的完整摘要"
publishedAt: 2026-08-13
sourcesCheckedAt: 2026-08-12
series: agent
sequence: 6
cover: "assets/covers/example.jpg"
coverAlt: "封面内容说明"
featured: false
tags: ["标签"]
draft: false
learning:
  track: vibe-coding
  step: 1
video:
  platform: douyin
  url: "https://v.douyin.com/.../"
  title: "视频标题"
  hook: "卡片的一句话看点"
---

## 第一节

正文。
```

系列只能是 `agent / observe / aivideo / industry`。学习路线只能是 `vibe-coding / ai-video`，同一路线的步骤必须完整且不重复。每条路线在 `src/pages/learn.astro` 的 `learningToolkits` 中维护 6 个工具 slug；增删工具或改 slug 时要同步核对这两个数组和学习页契约测试。需要新系列或路线时，先同时更新 `src/content.config.ts`、`src/lib/site.ts`、页面入口和契约测试。

## 2. 工具指南发布清单

工具指南是独立内容集合，不进入知识库或 RSS。新增或更新 `src/content/tools/<slug>.md` 时逐项完成：

1. 只从产品官网、官方文档或官方 GitHub 仓库确认安装与下载入口，重新核对 `officialUrl`、`versionChecked` 和当天 `verifiedAt`。
2. 至少完整核对一个主要平台的安装/访问路径；未在本机验证的平台明确写“参考官方文档”，不伪装亲测。
3. 在 `public/assets/tools/<slug>/` 准备四张本地图片：16:9 封面、流程图和两个关键步骤视觉；截图去除账号、手机号、本机路径、API Key 与账单信息，并在每张官方截图后紧邻标注官方来源链接和截取日期。
4. 开源工具核对官方仓库、许可证和维护状态；闭源产品明确写“非开源”。模型开放不等于在线产品开源。
5. 云端工具说明素材和代码可能离开本机；本地工具说明硬件、磁盘、模型许可证与可能联网的环节。每篇至少提供一个官方隐私、FAQ、服务条款或安全策略链接。
6. 正文图片地址必须带 `/personal-ip-website/assets/tools/` 前缀，并有非空替代文本。官方页面不可访问时只使用明确标注的原创结构示意，不用第三方镜像冒充证据。
7. 运行 `npm run check`、`npm test`、`node --check public/assets/hub.js` 和 `git diff --check`。
8. 检查 sitemap 中 `tools.html` 与 20 个详情地址；确认 RSS 保持 17 篇，且没有 `/tools/` 条目。

首页正文不增加工具卡片、数量或推荐入口；只允许全局导航出现“工具指南”。

## 3. 首页精选与作品流

- `featured: true` 决定首页主推；只能保留一篇，避免选择顺序不明确。
- 带 `video` 的文章自动进入作品页；没有视频的长文只进入知识库。
- 作品标题、封面、系列、视频链接和「读文字版」都来自同一 Markdown 条目，不再手改多个 HTML。
- 首页「接着看」自动排除精选后取 3 条视频。
- 首页「按路线学」自动展示 Vibe Coding 与 AI 视频入口；`learn.html` 按 `learning.step` 组织各 6 篇，并从工具集合生成各 6 款配套工具入口。
- 知识库按四个系列筛选全部 17 篇；作品页仍只展示带 `video` 的 4 篇。

## 4. 本地预览与验收

```bash
npm ci
npm run dev
```

提交前：

```bash
npm run check
npm test
node --check public/assets/hub.js
git diff --check
```

构建结果在 `dist/`。重点确认：

- `dist/notes/<slug>.html` 存在，且没有生成目录式 `notes/<slug>/index.html`；
- `dist/tools.html` 和 20 个 `dist/tools/<slug>.html` 存在，且没有目录式详情页；
- `dist/rss.xml` 有全部 17 篇；`dist/sitemap-index.xml` 指向 `sitemap-0.xml`，且 sitemap 包含 `learn.html`、`tools.html` 与 20 个工具详情页；
- `dist/tests/launch-readiness.html` 在本地服务器中显示 `PASS`；
- 390px 下导航折叠、学习路线目录与工具模型目录默认收起且可展开、路线工具箱与工具目录卡片均为单列、目录链接、文章纸面左右留白、图片和代码块都无横向溢出；桌面端学习侧栏与工具模型目录滚动时保持粘性可见，两类工具卡均为两列。

项目的 `npm run check` 与 `npm run build` 已内置 `--force`，会重建 Astro Content Layer 缓存。若直接运行 Astro CLI 后出现 `picomatch` 的 `require is not defined`，请改回上述 npm 脚本；这是 Astro 7.2.1 / Vite 8.2.1 在 Windows 缓存复用路径上的兼容性规避，不需要修改文章或 `src/content.config.ts`。

## 5. GitHub Pages 发布

部署工作流：`.github/workflows/deploy.yml`。

流程是 `npm ci → astro check → hub.js 语法检查 → build + Python tests → 上传 dist`。Pull Request 到 `main` 只运行验证，并按 PR 编号进入独立并发队列；只有推送到 `main` 才继续执行 `deploy-pages`，PR 不会取消生产发布。Astro 配置已经锁定：

```js
site: "https://seraph125.github.io"
base: "/personal-ip-website"
build: { format: "file" }
```

仓库 Pages 必须使用 **GitHub Actions**，不能继续使用 `main /` 分支根目录发布；否则 GitHub 会发布源码而不是 `dist`。首次迁移时执行一次：

```bash
gh api --method PUT repos/SERAPH125/personal-ip-website/pages -f build_type=workflow
```

官方依据：[Astro · Deploy to GitHub Pages](https://docs.astro.build/en/guides/deploy/github/) 与 [GitHub · Custom workflows for Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。

## 6. 发布后两分钟检查

1. Actions 的 `Deploy to GitHub Pages` 运行必须成功。
2. 打开线上 `tests/launch-readiness.html`，标题应为 `PASS · Launch readiness`。
3. 打开旧地址 `notes/codex-5-levels.html`，确认仍可访问并显示新版目录/阅读纸面。
4. 打开 `rss.xml` 与 `sitemap-index.xml`，确认均为 200。
5. 打开 `tools.html`，确认桌面端左侧模型目录保持粘性，语言模型、图片模型、AI 编程、视频模型四组共列出 20 个工具名称；点击名称应定位到右侧对应卡片，同类卡片为两列。再打开 ChatGPT Desktop、InvokeAI、Claude Code、剪映专业版和 FramePack，检查电脑端安装方式、代码复制、隐私说明和四张本地图。
6. 手机 390px 宽度下确认工具模型目录默认收起、展开后 20 个名称均可点击、选择工具后目录自动收起且卡片单列，再测试导航、代码复制、学习路线、知识库筛选、作品筛选和一篇长表格文章。

## 7. 回滚

- 优先 `git revert <坏提交>` 后推送，让 Actions 重新发布上一版源码构建结果；
- 不要 force-push 或手工改 `dist`；`dist` 不进 Git；
- 封面和 Markdown 都在仓库内，远端 Git 是主备份。

## 8. 刻意不做

- 不引入 WordPress、Ghost 或后端 CMS；
- 不嵌抖音播放器，不热链抖音封面；
- 17 篇阶段不接全文搜索；约 30 篇或出现明确需求时再评估 Pagefind；
- 不恢复 Three.js 首屏或全屏粒子库；
- 不手工维护生成后的 HTML、RSS、sitemap 或 JSON-LD。
