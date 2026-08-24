# 学习路线板块与 12 篇文章接入设计

日期：2026-08-24  
状态：待用户审核  
分支：`codex/learning-paths`

## 背景

网站当前使用 Astro 7、Markdown Content Collections 和静态 GitHub Pages 部署。5 篇公开文章统一存放在 `src/content/notes`，同时驱动知识库、作品页、文章详情、RSS、sitemap 和 JSON-LD。

本次要接入 12 篇已经完成原创整合的文章，其中 6 篇属于 Vibe Coding 学习路线，6 篇属于 AI 视频学习路线。直接把它们加入现有知识库，会让单列列表从 5 篇增至 17 篇，学习顺序也会被发布日期排序打散。

## 目标

1. 新增一个清楚、面向普通读者的「学习路线」板块。
2. 让两条路线各自保持 1—6 的固定学习顺序。
3. 继续复用现有文章详情、RSS、sitemap、SEO 和 Markdown 渲染能力。
4. 保留首页以创作者定位和视频内容为主的层级，只增加紧凑入口。
5. 在功能分支和 Pull Request 阶段运行完整构建检查，合并 `main` 后才发布。

## 非目标

- 不新建第二套文章详情路由或独立 CMS。
- 不改变既有 5 篇文章的 URL。
- 不在本次接入账号系统、阅读进度持久化或全文搜索。
- 不把研究整合内容描述为作者亲测；没有真实经历的数据不补写成第一手结论。
- 不改变抖音视频继续站外打开的现有策略。

## 信息架构

### 主导航

主导航顺序调整为：

`首页 / 作品 / 学习路线 / 知识库 / 关于`

「学习路线」指向 `learn.html`。桌面端保持现有横向导航；移动端沿用当前折叠菜单。

### 首页

在「接着看」之后增加一个紧凑的「系统学习」区域，只显示两张路线入口卡：

- Vibe Coding：从任务描述、Git、安全边界到效率判断。
- AI 视频：从镜头语言、提示词、一致性到发布规范。

首页不展开 12 篇文章列表，避免挤压当前精选和视频卡片。

### 学习路线页

新增 `src/pages/learn.astro`，页面包含：

1. 简短说明：两条路线都可以零基础开始，也可以按需跳读。
2. 两张路线概览卡，显示主题、适合人群和 6 个步骤。
3. 两个路线章节，每章按 `learning.step` 渲染 6 篇文章。
4. 每个步骤显示序号、标题、摘要、系列和阅读入口。

文章详情仍使用 `/notes/{slug}.html`。学习路线页只负责组织顺序，不创建重复详情页或重复 canonical。

### 知识库

知识库继续展示全部 17 篇文章，并补充系列筛选：全部、Agent 实战、模型观察、AI 视频、行业观察。筛选复用现有 `data-series-filter` 和卡片 `data-note-series` 机制。

17 篇仍可通过路线页与筛选快速定位，本次不接 Pagefind。重新评估全文搜索的条件是文章约 30 篇，或出现明确的站内搜索需求。

## 内容模型

继续使用现有 `notes` collection，在 schema 中增加两个可选字段：

```yaml
sourcesCheckedAt: 2026-08-23
learning:
  track: vibe-coding
  step: 1
```

约束如下：

- `sourcesCheckedAt`：可选日期，用于保留资料核验时间。
- `learning.track`：`vibe-coding` 或 `ai-video`。
- `learning.step`：1—6 的正整数。
- 既有 5 篇文章不需要补 `learning`。
- 路线页只查询 `learning` 存在且 `draft` 为 `false` 的文章。

12 篇草稿转换为正式内容时：

- 使用 2026-08-24 作为首次公开发布日期。
- 使用全局唯一 `sequence` 6—17；路线页排序只使用 `learning.step`。
- 前 5 篇 Vibe Coding 归入 `agent`，效率研究归入 `observe`；6 篇 AI 视频归入 `aivideo`。
- 添加 `cover`、`coverAlt`、`tags`、`featured: false` 和 `draft: false`。
- 删除正文中的一级标题，因为 `ArticleLayout` 已根据 frontmatter 输出唯一 H1。
- 保留参考资料章节和原始链接，不保留草稿专用的 `status` 字段。

## 封面策略

新增 12 张 16:9 标题卡封面，统一放在 `public/assets/covers`：

- Vibe Coding 使用同一套冷灰、代码网格和蓝色强调视觉。
- AI 视频使用同一套分镜框、时间轴和紫蓝渐变视觉。
- 每篇使用独立标题与步骤编号，避免社交分享图完全重复。
- 不使用未经授权的人像、品牌素材或第三方作品截图。

封面保持当前页面使用的静态图片方式，不增加运行时图片依赖。

## 组件与数据流

1. Markdown 由 `src/content.config.ts` 验证。
2. `getCollection("notes")` 继续作为唯一内容查询入口。
3. `learn.astro` 按 `learning.track` 分组、按 `learning.step` 排序。
4. 首页从同一集合计算两条路线的文章数与入口，不复制标题数据。
5. 文章详情继续由 `src/pages/notes/[...slug].astro` 和 `ArticleLayout.astro` 渲染。
6. RSS 与 sitemap 自动包含 12 篇新文章和 `learn.html`。

不新增数据库、客户端请求或运行时 API。构建失败就是内容 schema 或链接问题的主要失败信号。

## Git 与持续集成

远端 `main` 当前部署工作流只响应 `push`。本分支会把工作流调整为：

- `pull_request` 到 `main`：运行安装、Astro check、构建和契约测试，但不部署。
- `push` 到 `main`：运行相同检查，通过后部署 GitHub Pages。
- `workflow_dispatch`：保留手动运行能力。

部署 job 增加事件与分支条件，确保功能分支不会覆盖线上站点。

## 测试与验收

### 内容契约

- 12 个新 slug 均存在。
- 总公开文章数为 17，RSS 条目数为 17。
- 两条学习路线各有 6 个不重复步骤，步骤为 1—6。
- 每篇新文章只有一个 H1，至少两个 H2，并有参考资料章节。
- 所有封面文件存在，所有站内链接保留 `/personal-ip-website` base。

### 页面契约

- `learn.html` 存在并有唯一 H1。
- 主导航包含学习路线且当前页状态正确。
- 首页只有两个路线入口，不渲染 12 张长列表。
- 知识库系列筛选支持 `industry`，结果数与空状态可访问。
- 既有 5 个 `.html` 文章地址继续可用。

### 完整验证

```bash
npm ci
npm run check
npm test
node --check public/assets/hub.js
git diff --check
```

最后在 1280px 桌面宽度和约 390px 移动宽度检查首页、学习路线、知识库和任意两篇新文章。

## 文档同步

代码完成时同步更新：

- `docs/README.md`：目录、内容模型、文章数量、学习路线页面和验证方式。
- `docs/ops.md`：17 篇 RSS/sitemap 检查、PR CI 与发布流程。
- `brand-spec.md`：导航顺序、学习路线 IA、首页系统学习入口和 17 篇阶段的搜索决策。
- `docs/content-drafts/README.md` 不进入正式仓库；正式文章以 `src/content/notes` 为唯一来源。

## 完成标准

功能分支包含 12 篇可发布文章、12 张合规封面、学习路线入口、系列筛选、更新后的测试和开发文档。所有本地检查与 Pull Request CI 通过后，才建议合并到 `main`；合并前不改变线上网站。
