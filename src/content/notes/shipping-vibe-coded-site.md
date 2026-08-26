---
title: "把 AI 做的网站稳定上线：构建、发布、排错与回滚"
description: "本地能打开不等于可以上线。用一次完整演练学会构建、预览、GitHub Pages 发布、404 排查和可恢复回滚。"
publishedAt: 2026-08-26
sourcesCheckedAt: 2026-08-26
series: agent
sequence: 18
cover: "assets/covers/learning-vibe-ship.svg"
coverAlt: "从本地构建到发布和回滚的 Vibe Coding 学习路线第 6 步封面"
featured: false
tags: ["Vibe Coding","部署","GitHub Pages","回滚"]
draft: false
learning:
  track: vibe-coding
  step: 6
---


AI 帮你把页面做出来，只完成了一半。真正的交付还要回答：代码能否从干净环境构建、线上地址能否访问、静态资源会不会 404，以及上线出错后怎样恢复。

这一步不追求复杂运维，而是跑通一条普通人也能重复的安全路径：

> 本地验证 → 测试地址检查 → 合并发布 → 线上冒烟测试 → 回滚演练。

## 发布前先建立一个可重复基线

不要从“我刚才看起来能打开”直接跳到发布。先确认 Git 工作区只包含这次任务的修改：

```bash
git status --short
git diff --cached
```

然后按项目 README 运行完整检查。以本站为例：

```bash
npm ci
npm run check
npm test
node --check public/assets/hub.js
git diff --check
```

`npm ci` 会按锁文件安装依赖，能更接近持续集成环境。如果本地依赖目录已经存在但云端构建失败，重新从干净安装开始，往往比反复修改代码更容易找到真实差异。

## 构建、预览和发布不是一回事

这三个动作解决不同问题：

| 动作 | 回答的问题 | 常见命令 |
|---|---|---|
| 构建 | 源码能否生成可发布文件 | `npm run build` |
| 预览 | 构建产物在本地是否能访问 | `npm run preview` |
| 发布 | 构建产物是否已经部署到线上环境 | GitHub Actions / Pages |

只运行开发服务器不能证明正式构建成功。开发模式可能自动处理路径和错误，而 GitHub Pages 会把项目部署在仓库子路径，例如 `/personal-ip-website/`。Astro 项目必须正确配置 `site` 与 `base`，站内链接和资源路径也要尊重这个前缀。

## 先在测试入口检查，再动生产分支

更稳妥的顺序是：

1. 在功能分支完成修改并推送；
2. 让 Pull Request 的检查完整运行；
3. 查看构建日志，确认没有跳过失败步骤；
4. 在本地预览或测试地址检查页面；
5. 只有检查通过后才合并到触发生产发布的 `main`。

至少检查首页、刚改过的页面和一条深层链接。桌面端之外，再用约 390px 宽度查看一次移动布局。

## 构建失败时从第一条有效错误开始

日志后面常有很多连锁报错，真正根因通常更早。排查时依次做：

1. 记录失败的工作流、提交和第一条有效错误；
2. 在本地运行同一个命令，而不是换一套命令；
3. 核对 Node 版本、锁文件、环境变量和大小写；
4. 修复一个原因后重新运行完整检查；
5. 不通过删除测试、关闭类型检查或忽略退出码来制造“绿色”。

如果错误只发生在云端，下载或搜索 GitHub Actions 日志，比较云端环境与本地环境的差异。

## 页面 404 时先查路径和产物

GitHub Pages 的常见 404 可以按这个顺序检查：

- 发布产物顶层是否真的有 `index.html`；
- Astro 的 `site` 与 `base` 是否对应账号和仓库名；
- 链接与图片是否遗漏仓库子路径；
- 文件名大小写是否与引用完全一致；
- Pages 发布源是否选择 GitHub Actions；
- 最新工作流是否成功部署了当前提交。

首页能打开、二级页面或图片却 404，通常优先检查 `base` 和资源路径，而不是重新设计页面。

## 上线后做五分钟冒烟测试

发布成功提示只说明流程结束，不代表所有页面正确。打开线上地址检查：

1. 首页和本次修改页面返回正常；
2. 导航、站内链接和锚点能跳转；
3. 图片、CSS 与 JavaScript 正常加载；
4. 浏览器控制台没有新的致命错误；
5. 手机宽度下没有横向溢出。

把本次发布提交号和检查结果记录下来。出现问题时，你才知道应该回到哪个版本。

## 用一次可恢复提交练习回滚

共享分支发生问题时，优先创建一个反向提交，而不是强制改写历史：

```bash
git log --oneline -5
git revert 需要撤销的提交号
git push
```

`git revert` 会保留“发生过什么、后来为什么撤销”的记录，并让发布流程重新部署。涉及合并提交时参数不同，不确定就先查看 `git show` 和项目运维文档，不要猜测执行。

不要在共享的 `main` 上直接使用 `git reset --hard` 再强制推送。它可能覆盖别人的工作，也让审计和恢复更困难。

一次合格的回滚演练包括：故意发布一个无害的小变化、确认线上出现、用反向提交撤销、等待重新部署，再确认线上恢复。

## 第 6 步的验收清单

- [ ] 能从干净依赖运行完整检查；
- [ ] 能解释构建、预览和发布的区别；
- [ ] 能找到 GitHub Actions 的第一条有效错误；
- [ ] 能排查仓库子路径导致的 404；
- [ ] 上线后完成桌面与手机冒烟测试；
- [ ] 能用可恢复提交完成一次回滚。

做到这里，“稳定上线”才不再是一句标题，而是一套可以重复执行的动作。

## 参考资料

- [Astro：部署到 GitHub Pages](https://docs.astro.build/en/guides/deploy/github/)
- [GitHub：排查 Pages 404](https://docs.github.com/en/pages/getting-started-with-github-pages/troubleshooting-404-errors-for-github-pages-sites)
- [GitHub：排查工作流](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows)
- [Git：git-revert 官方文档](https://git-scm.com/docs/git-revert)
- [本站发布与回滚说明](https://github.com/SERAPH125/personal-ip-website/blob/main/docs/ops.md)
