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

1. Hairline borders only; shadow reserved for dropdowns / modals.
2. Sticky frosted top nav; content-led layouts.
3. At most two visible `--accent` uses per screen; homepage uses accent only on the primary「关注我」CTA（无 eyebrow/kicker）.
4. Prefer series + hook meta on cards; avoid redundant duration badges when all items are short-form.
5. CJK display line-height ≥ 1.3; no negative tracking on Chinese headlines.
6. Home polish: no hero kicker; single outbound chip on cover; no duplicate「全部作品」; video-card hover keeps title/meta contrast.
7. Related resources are optional, compact text-only links: at most one per video, neutral by default, and never nested inside the video link.

## Identity

- Display name: **南吴 NANWU**（顶栏：`南吴` + muted `NANWU`）
- Positioning: AI 科技类创作者 · 抖音主力（B站 / YouTube 有真实链接后再展示）
- About identity: 首版不展示未经确认的人像；favicon / 分享备用图使用 `assets/covers/nanwu-avatar.jpg`
- Content: 4 条抖音真片已写入 `assets/hub.js` + `assets/covers/*`
- About IA (locked): **series_first** — `agent` / `observe` / `aivideo`
- Watch policy (locked): **outbound only** — 无站内播放；`watch.html` = `dead_file`
- Home IA (locked): **latest_first + optional_related_resource** — 精选 Codex 篇；封面 `assets/home-latest-cover.jpg`；当前关联知识文档 `notes/codex-5-levels.html`
- Notes IA (locked): **list_detail** — 顶栏「知识库」；列表 `notes.html` + 详情 `notes/*.html`；文章含 `codex-5-levels`（Agent）与 `ai-refund-fraud-report`（行业观察）；列表支持 `?series=agent|industry` 筛选
- Notes motion: GSAP 入场 + 筛选（`assets/notes-motion.js`）；reduced-motion 关闭；hover 仅背景/字色，不动画 layout
- Home WebGL (locked): **cover_depth** — 仅精选封面背后景深网格（`assets/home-cover-three.js` + 本地 `assets/vendor/three.min.js` r160 UMD）；不做枢纽/星座/全屏粒子；canvas `pointer-events: none`，点击仍外链抖音；**勿用** three@0.161+ 的 `three.min.js` CDN（已删除，404）
- Launch policy: 公开页面不得出现空链接或未确认素材；六个公开页面提供 description、canonical、Open Graph、favicon，并由 `robots.txt` / `sitemap.xml` 索引
- Site ambient (locked): **U1 Linear dots + soft glow** — 四页共用 `assets/hub.css`：`body::before` 多层极淡 cobalt/cool-gray 径向柔光；`body::after` 为 `radial-gradient` 点阵 + `@property` 驱动相位/透明度呼吸；边缘 mask 淡出；`z-index: 0` + `pointer-events: none`，不抢封面网格环带；`prefers-reduced-motion: reduce` → 静帧。手法参考 [Typed Halftone Background Drift](https://animationpatterns.art/animations/typed-halftone-background-drift/) 与 [MDN `@property`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Reference/At-rules/@property)；气质对齐 [Linear](https://linear.app)。**禁止** Vanta / tsParticles / 枢纽星座 / 粒子海
