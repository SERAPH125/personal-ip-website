# Brand spec — 南吴 NANWU 内容枢纽

**Direction:** `modern-minimal`（Linear / Vercel）  
**One-liner:** Quiet, precise, software-native chrome; cobalt accent only on the primary follow action and one eyebrow per screen.

## Tokens (`:root`)

```css
--bg: oklch(99% 0.002 240);
--surface: oklch(100% 0 0);
--fg: oklch(18% 0.012 250);
--muted: oklch(54% 0.012 250);
--border: oklch(92% 0.005 250);
--accent: oklch(58% 0.18 255); /* cobalt */
--font-display: -apple-system, BlinkMacSystemFont, "SF Pro Display", "PingFang SC", system-ui, sans-serif;
--font-body: -apple-system, BlinkMacSystemFont, "SF Pro Text", "PingFang SC", system-ui, sans-serif;
```

## Observed rules

1. Hairline borders only; shadow reserved for dropdowns, modals and the long-form reading surface.
2. Sticky frosted top nav; content-led layouts.
3. At most two visible `--accent` uses per screen; homepage uses one identity eyebrow and one primary「去抖音关注」CTA.
4. Prefer series + hook meta on cards; avoid redundant duration badges when all items are short-form.
5. CJK display line-height ≥ 1.22; reading body uses `17px / 1.9`. Article H1 may use restrained `-0.025em` tracking to strengthen hierarchy; navigation and card titles stay neutral.
6. Home hierarchy: creator identity → value proposition → current featured topic; single outbound chip on cover; no duplicate「全部作品」.
7. Related resources are optional, compact text-only links: at most one per video, neutral by default, and never nested inside the video link.

## Identity

- Display name: **南吴 NANWU**（顶栏：`南吴` + muted `NANWU`）
- Positioning: AI 科技类创作者 · 抖音主力（B站 / YouTube 有真实链接后再展示）
- About identity: 首版不展示未经确认的人像；favicon / 分享备用图使用 `assets/covers/nanwu-avatar.jpg`
- Content: `src/content/notes/*.md` 是 17 篇文章与 4 条视频卡的唯一内容源；`src/content/tools/*.md` 是 8 篇工具指南的唯一内容源；其中 12 篇知识文章组成两条学习路线；资源位于 `public/assets/covers/*` 与 `public/assets/tools/*`；Astro 构建静态 HTML，`public/assets/hub.js` 只负责渐进交互
- Primary nav (locked): **home / works / learn / tools / notes / about** — `首页 / 作品 / 学习路线 / 工具指南 / 知识库 / 关于`
- About IA (locked): **series_first** — `agent` / `observe` / `aivideo`
- Watch policy (locked): **outbound only** — 无站内播放；`watch.html` = `dead_file`
- Home IA (locked): **creator_first + current_feature** — H1 先说明南吴提供的价值；`featured: true` 决定当前精选；关联知识文档与视频封面来自同一 Markdown 条目
- Works IA (locked): **series_filter + dual_destination** — `agent / observe / aivideo` 系列筛选；每卡并列提供视频与文字入口；Astro 必须生成可直接读取的静态 HTML
- Learning IA (locked): **sidebar_outline + two_ordered_tracks** — `learn.html` 桌面端使用左侧粘性目录，按 Vibe Coding、AI 视频分组列出各 6 步；移动端目录折叠，右侧/下方正文仍由 `learning.track / step` 驱动，首页只显示两张入口卡，文章继续使用 `notes/<slug>.html`
- Tools IA (locked): **grouped_model_directory + static_guides** — `tools.html` 桌面端使用左侧粘性模型目录，按语言模型 / 图片模型 / AI 编程 / 视频模型分组列出 8 个工具名称，并锚点定位右侧同类卡片；820px 以下目录折叠，640px 以下卡片单列；8 篇详情继续使用 `tools/<slug>.html`，首页正文不提供工具入口，只通过全局导航进入
- Notes IA (locked): **series_filter + list_detail** — `notes.html` + 17 篇详情；五个筛选为 `all / agent / observe / aivideo / industry`；17 篇阶段不显示搜索，约 30 篇或有明确需求时再评估 Pagefind；详情采用居中的 `42rem` 阅读列、白色阅读纸面、自动目录与 Markdown 富文本节奏
- Home depth (locked): **css_cover_depth** — 仅用 CSS gradient 网格与柔光衬精选封面，不加载 Three.js、WebGL 或 RAF；不做枢纽/星座/全屏粒子
- Follow policy (locked): 首页与关于页 CTA 直接打开抖音主页，不使用单平台选择弹层
- Launch policy: 公开页面不得出现空链接或未确认素材；31 个 canonical 公开页面提供 description、canonical、Open Graph、RSS discovery、JSON-LD、favicon，并由 `robots.txt` / `sitemap-index.xml` 索引；既有 `.html` URL 永久保留
- Site ambient (locked): **U1 Linear dots + soft glow** — 全站共用 `public/assets/hub.css`：`body::before` 多层极淡 cobalt/cool-gray 径向柔光；`body::after` 为 `radial-gradient` 点阵 + `@property` 驱动相位/透明度呼吸；文章正文由高不透明阅读纸面隔离点阵噪声；`prefers-reduced-motion: reduce` → 静帧。手法参考 [Typed Halftone Background Drift](https://animationpatterns.art/animations/typed-halftone-background-drift/) 与 [MDN `@property`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Reference/At-rules/@property)；气质对齐 [Linear](https://linear.app)。**禁止** Vanta / tsParticles / 枢纽星座 / 粒子海
