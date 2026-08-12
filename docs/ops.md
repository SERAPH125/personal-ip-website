# 发布与运维 · 南吴 NANWU

本站是**纯静态 HTML**（无构建、无 CMS、无站内播放）。更新 = 改文件 → Git 推送 → 托管自动上线。

**源码仓库：** [SERAPH125/personal-ip-website](https://github.com/SERAPH125/personal-ip-website)（项目名：个人ip网站）

**日常真相：** 改 `assets/hub.js` + 封面图 / 手写 `notes/*.html`，推仓库即可。

---

## 1. 托管选型（一步到位）

本站无 build，输出目录 = **仓库根**（含 `index.html`）。GitHub Pages 直接发布 `main` 分支 `/`；若改用 Cloudflare Pages，静态站 Build command 使用 `exit 0`。

| 平台 | 免费要点 | 适合你如果… | 首次上手 |
|---|---|---|---|
| **Cloudflare Pages**（推荐） | 免费档带宽/请求很慷慨；全球 CDN；自定义域名 + 自动 HTTPS | 要稳、要快、以后可能绑自己的域名 | Git 连仓库 → 无构建 → Deploy |
| **GitHub Pages** | 与仓库一体；`username.github.io` 或自定义域名 | 仓库已在 GitHub、只要最简单静态托管 | Settings → Pages → Deploy from branch `/` |
| **Netlify** | Deploy Preview（PR 预览）；拖拽/CLI 也可 | 想每次改动能先看预览站再合并 | 连 Git → Publish directory = `.` |

**当前发布目标：GitHub Pages。** 来源为 `main` 分支根目录，目标地址：`https://seraph125.github.io/personal-ip-website/`。需要 PR 预览时再评估 Netlify。

开源/官方依据：

- [Cloudflare Pages · Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/)（无构建可留空 build command）
- [GitHub Pages](https://docs.github.com/pages)（分支根目录发布）
- [Netlify · Deploy](https://docs.netlify.com/site-deploys/overview/)（Git 连续部署 + Preview）
- 对比综述：[HostDuel · Static Site Hosting](https://hostduel.com/blog/static-site-hosting-comparison)、[TechStackVS 2026 对比](https://techstackvs.com/compare/vercel-vs-netlify-vs-cloudflare-pages-vs-github-pages)

内容工作流：**继续手改 HTML/JS**，不要上博客 CMS。极简长文可参考 [HermanMartinus/bearblog](https://github.com/HermanMartinus/bearblog)；文档列表结构可参考 [withastro/starlight](https://github.com/withastro/starlight)——本站已手写对齐，无需迁框架。

---

## 2. 首次发布 Checklist（约 15–25 分钟）

1. 把项目放进 **Git 仓库**（GitHub / GitLab）；**不要**提交 `.file-versions/`、`.od-skills/`、Open Design 内部产物（若暂存一并忽略）。
2. 本地打开 `index.html`：点阵背景、精选封面、外链抖音正常。
3. GitHub 仓库 Settings → Pages → Deploy from a branch → `main` + `/ (root)`。
4. 等部署完成 → 打开 `*.pages.dev` / `*.netlify.app` / `*.github.io` 验收四页：`index` / `works` / `notes` / `about`。
5. （可选）绑自定义域名 → 按面板改 DNS（CNAME/A）→ 等 HTTPS 变绿。
6. 记一条「回滚」：托管面板 Rollback 上一版，或 `git revert` 再推。

**可发布文件：** `*.html`、`notes/`、`assets/`、`docs/`、`brand-spec.md`。  
**不必上线：** `preview-bg-effects.html`（可选保留）、`.file-versions/`、`*.artifact.json`、草稿 Markdown。

---

## 3. 日常更新剧本

每次做完：**本地预览 → `git add` 相关文件 → commit → push**。托管约 1–3 分钟刷新。

### 推荐入口：把内容单交给 Codex

日常不必亲自查找并同步多个 HTML/JS 文件。把以下内容单发给 Codex，由 Codex 按本章 A–D 的规则完成修改、验证和文档同步：

```text
新增视频
标题：
平台链接：
系列：Agent 实战 / 模型观察 / AI 视频
封面：（附件）
首页位置：精选 / 接着看 / 仅作品页
关联资源：无 / 知识文档链接 / 产品链接
```

约束：`关联资源` 为可选项；只有提供真实对应资源时才展示，每条视频最多 1 条。提交前至少运行相关结构测试与 `git diff --check`，发布后执行第 8 节自检。

### A. 加一条抖音作品（约 10–20 分钟）

1. 准备短链 `https://v.douyin.com/...`；用浏览器/技能抓简介与封面（见 `README.md`「如何爬取封面」）。
2. 封面下载到 `assets/covers/某名.jpg`（**禁止热链抖音 CDN**）。
3. 打开 `assets/hub.js` → `videos[]` **数组最前面**插入一条（新片优先）：

```js
{
  id: "v5",  // 新 id，勿重复
  title: "标题",
  platform: "douyin",
  platformLabel: "抖音",
  duration: "短视频",
  series: "Agent 实战",       // 或 模型观察 / AI 视频
  seriesSlug: "agent",        // agent | observe | aivideo
  cover: "assets/covers/某名.jpg",
  url: "https://v.douyin.com/xxxx/",
  hook: "一句话钩子",
  desc: "简介"
}
```

4. 若要当**首页精选**：改 `index.html` 里 hero 标题、lede、封面 `img`、`href` 短链（精选是手写的，不自动读 `videos[0]`）。
5. 「接着看」三卡若要换片：改 `index.html` 对应卡片的封面/标题/链接。
6. （建议）`docs/README.md` 抖音表格加一行。
7. Push → 线上 `works.html` 应出现新卡。

### B. 加一篇知识库（约 15–30 分钟）

1. 复制一篇已有文：`notes/codex-5-levels.html` → `notes/你的 slug.html`。
2. 改标题、正文、系列文案；资源路径用 `../assets/...`。
3. 在 `notes.html` 的 `<ul class="note-list">` **顶部**加一张卡片：`href="notes/你的 slug.html"`，`data-note-series="agent|industry"`。
4. 更新 `notes.html` 里「共 **N** 篇」的数字。
5. Push → 打开线上知识库列表与详情。

### C. 改关于页 / 关注链接（约 5 分钟）

1. 抖音主页同时维护 `about-link-douyin` 与各页 `follow-douyin`。
2. B站/YouTube 目前不公开；拿到真实主页后再新增入口，禁止使用 `href="#"`。
3. 所有外部主页链接加 `target="_blank" rel="noopener noreferrer"` 与准确的 `data-platform-out`。
4. 全站搜索平台名，确认面板、弹层与说明文档同步。

### D. 换封面图（约 5–10 分钟）

1. 新图放入 `assets/covers/`（建议新文件名，避免强缓存旧图）。
2. `assets/hub.js` 对应条目的 `cover` 字段。
3. 若是首页精选或「接着看」手写卡：同步改 `index.html` 的 `src`。
4. Push。

### E. 改样式 / Three 景深（少见）

| 改什么 | 文件 |
|---|---|
| 全站样式、U1 背景 | `assets/hub.css` |
| 首页封面景深逻辑 | `assets/home-cover-three.js` |
| Three 库（勿乱升） | `assets/vendor/three.min.js`（锁 **r160** UMD） |
| 知识库列表动效 | `assets/notes-motion.js` |

改完 CSS 后做第 4 节缓存戳。

---

## 4. 缓存与 CDN

| 资源 | 现状 | 注意 |
|---|---|---|
| `hub.css` | 全站 `?v=20260812launch1` | **改 CSS 后 bump 所有页的 `?v=`**（根目录 HTML + `notes/*.html`）。 |
| `hub.js` | 全站 `?v=20260812launch1` | 改作品数据或交互后 bump 查询戳并全站统一。 |
| `three.min.js` | 本地 vendor，无 CDN | **勿**换成 three@0.161+ CDN（`three.min.js` 已删会 404）。升级须整包替换并自测首页景深。 |
| 封面 JPG | 路径固定易被 CDN 缓存 | 换图优先**新文件名**，或改查询串。 |

Cloudflare / Netlify 默认边缘缓存静态资源；回滚部署后用户仍可能看到旧 CSS——靠 `?v=` 戳解决，不必清全球缓存。

---

## 5. 域名与 HTTPS

1. 托管面板 → Custom domains → 填 `nanwu.example.com`（示例）。
2. DNS：按面板提示加 **CNAME**（指向 `*.pages.dev` / Netlify 域）或 GitHub Pages 的 A/CNAME。
3. 等证书签发（常几分钟到几小时）；全站自动 HTTPS。
4. 可选：强制 HTTPS、开启托管自带解析/代理（Cloudflare 橙云）。

本站无后端、无 Cookie 会话；HTTPS 主要防劫持与浏览器安全提示。

---

## 6. 备份与回滚

| 手段 | 做法 |
|---|---|
| **主备份** | Git 远程仓库（每次更新都 commit） |
| **一键回滚** | Cloudflare / Netlify 控制台 → Deployments → Rollback |
| **Git 回滚** | `git revert <坏提交>` → push（比 force-push 安全） |
| **封面/文稿** | `assets/covers/` 与 `notes/` 随仓库；重要稿可另存 Markdown 源 |

不要只靠本机文件夹；发布前确认 remote 已 push。

---

## 7. 不要做的事

- **不要**上 WordPress / Ghost / 重型 CMS「图省事」（本站刻意无 CMS）。
- **不要**为发文引入 Forest Admin、Headless CMS，除非你**明确**要非技术编辑后台。
- **不要**站内嵌抖音播放器；继续外链。
- **不要**热链抖音封面 CDN。
- **不要**为背景换 Vanta / tsParticles / 全屏粒子。
- **不要**把 Open Design 的 `.file-versions/`、内部 skill 缓存当生产依赖发布。
- **不要**无必要升级 `three.min.js` 到删了 UMD 构建的大版本。

以后若真要非技术同学改文：再评估「手写 HTML + PR」是否够用；不够再谈轻量 Git 编辑器（如 Front Matter CMS 一类），而非先上整站 CMS。

---

## 8. 两分钟自检（每次发布后）

1. 打开 `tests/launch-readiness.html`，确认标题为 `PASS · Launch readiness`。
2. 首页精选封面可点，作品系列筛选只显示匹配卡片。
3. 知识库在 GSAP 失败时仍可见，列表可进入详情。
4. 关于页抖音主页可开，公开页无空链接。
5. 390px 宽度下导航可开合，按钮名称随状态更新。

---

## 9. 单数据源升级预案（已记录，暂不实施）

**当前状态：** 仅记录方案；网站仍按第 3 节的现有手写流程运行，不改变部署方式。

当作品超过约 20 条、每周更新多次，或出现多人编辑需求时，再把视频和关联资源收口到一个内容表。建议字段：

```js
{
  id: "v5",
  title: "标题",
  url: "https://v.douyin.com/...",
  cover: "assets/covers/example.jpg",
  seriesSlug: "agent",
  related: null
  // 或：{ type: "知识文档", title: "标题", href: "notes/example.html" }
}
```

升级目标：一条数据生成首页、作品页和关联资源卡；`related: null` 时不渲染占位。优先保持静态 HTML 输出，避免把核心内容进一步变成仅靠浏览器 JS 注入。

完成单数据源后，若需要网页编辑后台，再评估开源 [Pages CMS](https://github.com/pagescms/pagescms)（直接管理 GitHub 仓库内容）或 [Decap CMS](https://github.com/decaporg/decap-cms)（Git-based `/admin` 编辑界面）；当前不安装 CMS。

下一步：选好托管 → 按 §2 连 Git 打出第一版预览 URL。
