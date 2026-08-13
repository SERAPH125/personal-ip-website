# 发布与运维 · 南吴 NANWU

本站是 **Astro 构建的静态站**：没有数据库、CMS 或站内播放器。日常更新只改 Markdown 和本地封面；列表、作品卡、RSS、sitemap、JSON-LD 与前后篇由构建自动同步。

## 1. 日常发文

1. 在 `src/content/notes/` 新建 `slug.md`，复制任一现有 Frontmatter；`sequence` 使用当前最大值 + 1。
2. 正文直接写标准 Markdown：`##` 标题、列表、引用、表格、代码块都由文章模板统一排版。
3. 封面放到 `public/assets/covers/`，Frontmatter 写 `cover: "assets/covers/文件.jpg"`；禁止热链带签名的抖音 CDN。
4. 有视频就填写 `video`；没有视频则完全删除该对象，页面不会渲染空入口。
5. 运行 `npm run check && npm test`；通过后提交并推送 `main`。

最小模板：

```md
---
title: "文章标题"
description: "用于列表、SEO 与文章导语的完整摘要"
publishedAt: 2026-08-13
series: agent
sequence: 6
cover: "assets/covers/example.jpg"
coverAlt: "封面内容说明"
featured: false
tags: ["标签"]
draft: false
video:
  platform: douyin
  url: "https://v.douyin.com/.../"
  title: "视频标题"
  hook: "卡片的一句话看点"
---

## 第一节

正文。
```

系列只能是 `agent / observe / aivideo / industry`。需要新系列时，先同时更新 `src/content.config.ts`、`src/lib/site.ts` 和作品页筛选。

## 2. 首页精选与作品流

- `featured: true` 决定首页主推；只能保留一篇，避免选择顺序不明确。
- 带 `video` 的文章自动进入作品页；没有视频的长文只进入知识库。
- 作品标题、封面、系列、视频链接和「读文字版」都来自同一 Markdown 条目，不再手改多个 HTML。
- 首页「接着看」自动排除精选后取 3 条视频。

## 3. 本地预览与验收

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
- `dist/rss.xml` 有全部 5 篇；`dist/sitemap-index.xml` 指向 `sitemap-0.xml`；
- `dist/tests/launch-readiness.html` 在本地服务器中显示 `PASS`；
- 390px 下文章纸面左右留白、目录、表格横向滚动正常。

## 4. GitHub Pages 发布

部署工作流：`.github/workflows/deploy.yml`。

流程是 `npm ci → astro check → build + Python tests → 上传 dist → deploy-pages`。Astro 配置已经锁定：

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

## 5. 发布后两分钟检查

1. Actions 的 `Deploy to GitHub Pages` 运行必须成功。
2. 打开线上 `tests/launch-readiness.html`，标题应为 `PASS · Launch readiness`。
3. 打开旧地址 `notes/codex-5-levels.html`，确认仍可访问并显示新版目录/阅读纸面。
4. 打开 `rss.xml` 与 `sitemap-index.xml`，确认均为 200。
5. 手机宽度下测试导航、作品筛选和一篇长表格文章。

## 6. 回滚

- 优先 `git revert <坏提交>` 后推送，让 Actions 重新发布上一版源码构建结果；
- 不要 force-push 或手工改 `dist`；`dist` 不进 Git；
- 封面和 Markdown 都在仓库内，远端 Git 是主备份。

## 7. 刻意不做

- 不引入 WordPress、Ghost 或后端 CMS；
- 不嵌抖音播放器，不热链抖音封面；
- 不为少于约 12 篇内容接全文搜索；
- 不恢复 Three.js 首屏或全屏粒子库；
- 不手工维护生成后的 HTML、RSS、sitemap 或 JSON-LD。
