# AI Tool Guides Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a navigation-only AI tool guide section with an eight-card catalog and eight source-backed, image-rich installation/use guides while leaving the homepage body unchanged.

**Architecture:** Add a separate Astro `tools` content collection, a static catalog route, and one dynamic static detail route. Content drives metadata, grouped model-directory navigation, SEO, and navigation; shared CSS/JavaScript provide responsive disclosure behavior and code-copy enhancement without introducing a framework or runtime API.

**Tech Stack:** Astro 7, Markdown Content Collections, TypeScript, semantic HTML, existing vanilla CSS/JavaScript, Python `unittest`, GitHub Pages static file-style routes.

**Spec:** `docs/superpowers/specs/2026-08-26-ai-tool-guides-design.md`

> **Implementation update (2026-08-26):** 用户在首版完成后确认将目录改为语言模型、图片模型、AI 编程、视频模型四组，并在左侧直接列出 8 个工具名称。原计划中关于类别 / 平台 / 使用方式组合筛选的任务记录仅保留为实施历史；当前行为与验收标准以设计文档、`brand-spec.md` 和代码为准。

## Global Constraints

- The first release contains exactly Codex, Cursor, Ollama, ComfyUI, TRAE, Cherry Studio, DeepSeek, and 可灵 AI.
- The homepage body receives no tool card, recommendation section, count, or secondary tool entry; only the global navigation changes.
- Routes are `tools.html` and `/tools/<slug>.html`; existing note URLs, RSS entries, learning routes, and homepage learning entries remain unchanged.
- Each guide contains 4–6 local visuals: one original 16:9 cover, one original flow diagram, and at least two current official-page or locally verified screenshots.
- Screenshots never expose account identifiers, phone numbers, local private paths, API keys, billing details, or private project names.
- Product UI is never fabricated; original diagrams are labeled as diagrams and official-page captures cite their source in the adjacent caption.
- Official docs/product pages and official GitHub repositories are the only installation/download sources.
- Every guide records the checked release/channel and `verifiedAt: 2026-08-26`; unsupported or untested platforms are described as documentation-only, not first-hand testing.
- No Starlight, Docusaurus, Pagefind, database, server API, analytics SDK, login, comment system, or additional front-end dependency is added.
- RSS remains a 17-item notes-only feed; sitemap gains `tools.html` plus eight detail URLs.
- Use test-first steps, `apply_patch` for text edits, focused commits, and `git diff --check` before completion.

## File Map

**Create**

- `src/content/tools/codex.md` — Codex installation and first-task guide.
- `src/content/tools/cursor.md` — Cursor installation and first edit guide.
- `src/content/tools/ollama.md` — Ollama installation, model pull, and storage guide.
- `src/content/tools/comfyui.md` — Comfy Desktop/ComfyUI installation and first workflow guide.
- `src/content/tools/trae.md` — TRAE CN installation and first project guide.
- `src/content/tools/cherry-studio.md` — Cherry Studio installation and provider setup guide.
- `src/content/tools/deepseek.md` — DeepSeek web/app access and first conversation guide.
- `src/content/tools/kling-ai.md` — 可灵 AI web/app access and first video guide.
- `src/components/ToolCard.astro` — catalog card and filter data attributes.
- `src/layouts/ToolGuideLayout.astro` — detail metadata, quick judgment, TOC, body, SEO, and adjacent-guide navigation.
- `src/pages/tools.astro` — catalog, filter controls, count, and CollectionPage structured data.
- `src/pages/tools/[...slug].astro` — eight static file-style detail routes.
- `tests/test_tool_guides.py` — schema, content, asset, page, interaction, sitemap, RSS, and homepage contracts.
- `public/assets/tools/<slug>/cover.svg` — eight original 16:9 title cards.
- `public/assets/tools/<slug>/install-flow.svg` — eight original setup/access diagrams.
- `public/assets/tools/<slug>/step-01.webp` — first source-backed screenshot per guide.
- `public/assets/tools/<slug>/step-02.webp` — second source-backed screenshot per guide.

**Modify**

- `src/content.config.ts` — register and validate the `tools` collection.
- `src/lib/site.ts` — tool labels plus `toolPath()` and `toolUrl()`.
- `src/components/SiteNav.astro` — add `tools` active state and navigation item.
- `src/layouts/BaseLayout.astro` — allow `activeNav="tools"`.
- `public/assets/hub.css` — catalog cards, filters, tool metadata, figures, quick judgment, and code-copy styles.
- `public/assets/hub.js` — compound tool filters and progressive code-copy enhancement.
- `docs/README.md` — collection, route, authoring, assets, and validation documentation.
- `docs/ops.md` — publishing, source/image checks, sitemap count, and regression checklist.
- `brand-spec.md` — six-item navigation, tool IA, 31-page launch count, and explicit homepage-body exclusion.
- `docs/superpowers/specs/2026-08-26-ai-tool-guides-design.md` — keep approved status and final field names aligned with code.

## Official Source Set

| Guide | Installation/access source | Usage/privacy/license source |
| --- | --- | --- |
| Codex | `https://learn.chatgpt.com/docs/codex/cli` | `https://github.com/openai/codex` and `https://learn.chatgpt.com/docs/codex/security` |
| Cursor | `https://cursor.com/downloads` and `https://cursor.com/docs/get-started/quickstart` | `https://cursor.com/docs/account/privacy` and `https://cursor.com/docs/account/pricing` |
| Ollama | `https://ollama.com/download` and `https://docs.ollama.com/quickstart` | `https://github.com/ollama/ollama` and `https://ollama.com/privacy` |
| ComfyUI | `https://docs.comfy.org/installation/desktop/windows` and `https://docs.comfy.org/installation/update_comfyui` | `https://github.com/Comfy-Org/ComfyUI` and `https://www.comfy.org/privacy-policy` |
| TRAE | `https://www.trae.cn/ide/download` | `https://forum.trae.cn/t/topic/48` and `https://www.trae.cn/privacy` |
| Cherry Studio | `https://cherry-ai.com/download` | `https://github.com/CherryHQ/cherry-studio`, its `PRIVACY.md`, and official docs linked by the repository |
| DeepSeek | `https://www.deepseek.com/`, `https://chat.deepseek.com/`, and `https://download.deepseek.com/app/` | `https://api-docs.deepseek.com/`, `https://platform.deepseek.com/`, and the privacy link exposed by the official app/site |
| 可灵 AI | `https://kling.ai/cn` and `https://app.klingai.com/cn/quickstart/klingai-video-3-model-user-guide` | the current membership/privacy links exposed by `https://kling.ai/cn`; use `https://ir.kuaishou.com/zh-hans/news-releases/news-release-details/kuaishou-kling-ai-integrates-deepseek-lowering-entry-barrier-ai/` only to verify official web/app entry points |

If a source changes while executing the plan, follow the current official redirect, store the final public URL in the article, and keep `verifiedAt` fixed to the actual re-check date instead of preserving a dead URL.

---

### Task 1: Tool collection schema and shared metadata

**Files:**
- Modify: `tests/test_tool_guides.py`
- Modify: `src/content.config.ts`
- Modify: `src/lib/site.ts`

**Interfaces:**
- Produces: Astro collection name `tools` and `CollectionEntry<"tools">`.
- Produces: `toolCategoryMeta`, `toolOriginMeta`, `toolAccessMeta`, `toolPlatformMeta`, `toolPricingMeta`.
- Produces: `toolPath(slug: string): string` and `toolUrl(slug: string): string`.
- Consumes: existing `withBase()` and `absoluteUrl()` URL helpers.

- [ ] **Step 1: Create the schema contract test**

Create `tests/test_tool_guides.py` with a first test that reads `src/content.config.ts` and `src/lib/site.ts`. Assert that the collection uses `base: "./src/content/tools"`, exports `{ notes, tools }`, contains the exact fields below, exposes the four label maps plus pricing, and creates file-style tool URLs.

```python
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ToolGuideContractTests(unittest.TestCase):
    def test_tools_collection_schema_and_shared_metadata(self):
        config = (ROOT / "src" / "content.config.ts").read_text(encoding="utf-8")
        site = (ROOT / "src" / "lib" / "site.ts").read_text(encoding="utf-8")

        self.assertIn('base: "./src/content/tools"', config)
        for field in (
            "toolName", "description", "audience", "setupSummary", "privacySummary",
            "origin", "category", "accessTypes", "platforms", "pricing", "openSource",
            "license", "officialUrl", "downloadUrl", "repositoryUrl", "versionChecked",
            "verifiedAt", "cover", "coverAlt", "sequence", "draft",
        ):
            self.assertRegex(config, rf"\b{field}\b")
        self.assertRegex(config, r"export const collections = \{ notes, tools \}")

        for symbol in (
            "toolCategoryMeta", "toolOriginMeta", "toolAccessMeta",
            "toolPlatformMeta", "toolPricingMeta", "toolPath", "toolUrl",
        ):
            self.assertIn(symbol, site)
        self.assertIn("tools/${slug}.html", site)
```

- [ ] **Step 2: Run the targeted test and confirm the red state**

Run: `python -m unittest tests.test_tool_guides.ToolGuideContractTests.test_tools_collection_schema_and_shared_metadata -v`

Expected: FAIL because `tests/test_tool_guides.py` or the `tools` collection does not exist.

- [ ] **Step 3: Add the `tools` collection**

In `src/content.config.ts`, add a second `defineCollection()` with these exact enum sets and conditions:

```ts
const tools = defineCollection({
  loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/tools" }),
  schema: z
    .object({
      title: z.string(),
      toolName: z.string(),
      description: z.string(),
      audience: z.string(),
      setupSummary: z.string(),
      privacySummary: z.string(),
      origin: z.enum(["international", "china"]),
      category: z.enum(["ai-coding", "local-model", "desktop-client", "image-video"]),
      accessTypes: z.array(z.enum(["cli", "desktop", "local-service", "web"])).min(1),
      platforms: z.array(z.enum(["windows", "macos", "linux", "web", "android", "ios"])).min(1),
      pricing: z.enum(["free", "freemium", "paid", "usage-based"]),
      openSource: z.boolean(),
      license: z.string(),
      officialUrl: z.url(),
      downloadUrl: z.url().optional(),
      repositoryUrl: z.url().optional(),
      versionChecked: z.string(),
      verifiedAt: z.coerce.date(),
      cover: z.string(),
      coverAlt: z.string(),
      sequence: z.number().int().min(1).max(8),
      draft: z.boolean().default(false),
    })
    .refine((data) => !data.openSource || Boolean(data.repositoryUrl), {
      message: "开源工具必须提供 repositoryUrl",
      path: ["repositoryUrl"],
    }),
});

export const collections = { notes, tools };
```

- [ ] **Step 4: Add shared labels and URL helpers**

In `src/lib/site.ts`, add exact Chinese labels for all enum values and these helpers:

```ts
export function toolPath(slug: string) {
  return withBase(`tools/${slug}.html`);
}

export function toolUrl(slug: string) {
  return absoluteUrl(`tools/${slug}.html`);
}
```

Use these label values: AI 编程、本地模型、桌面客户端、图像/视频；国际、国内；命令行、桌面应用、本地服务、网页；Windows、macOS、Linux、网页、Android、iOS；免费、免费增值、付费、按量计费.

- [ ] **Step 5: Run the targeted test**

Run: `python -m unittest tests.test_tool_guides.ToolGuideContractTests.test_tools_collection_schema_and_shared_metadata -v`

Expected: PASS.

- [ ] **Step 6: Commit the schema unit**

```bash
git add tests/test_tool_guides.py src/content.config.ts src/lib/site.ts
git commit -m "feat: define AI tool guide collection"
```

---

### Task 2: Four international guides and their visual evidence

**Files:**
- Modify: `tests/test_tool_guides.py`
- Create: `src/content/tools/codex.md`
- Create: `src/content/tools/cursor.md`
- Create: `src/content/tools/ollama.md`
- Create: `src/content/tools/comfyui.md`
- Create: `public/assets/tools/{codex,cursor,ollama,comfyui}/{cover.svg,install-flow.svg,step-01.webp,step-02.webp}`

**Interfaces:**
- Consumes: `tools` schema from Task 1.
- Produces: sequences 1–4 with slugs `codex`, `cursor`, `ollama`, `comfyui`.
- Produces: four local visual paths per guide for later page rendering.

- [ ] **Step 1: Add an international-content contract**

Extend `tests/test_tool_guides.py` with constants for the four exact slugs and a test that verifies: required frontmatter keys, sequence 1–4, `origin: international`, a non-empty license, `verifiedAt: 2026-08-26`, all eight required H2 headings, four local image references, non-empty image alt text, and existence of every referenced asset.

The required headings are:

```python
REQUIRED_GUIDE_HEADINGS = (
    "快速判断", "安装前检查", "图解安装", "第一次使用",
    "常见问题", "更新与卸载", "费用、隐私与开源信息", "官方资料与核验日期",
)
```

Use a Markdown image regex that accepts both SVG and WebP and resolves paths under `public/` after removing the leading slash.

- [ ] **Step 2: Run the international test and confirm the red state**

Run: `python -m unittest tests.test_tool_guides.ToolGuideContractTests.test_international_guides_are_complete_and_image_rich -v`

Expected: FAIL because the four Markdown files do not exist.

- [ ] **Step 3: Capture and author Codex evidence**

Create:

- `cover.svg`: original 1600×900 cobalt terminal-and-repository title card labeled “Codex 安装与入门 / CLI · AI 编程”.
- `install-flow.svg`: “系统检查 → 官方安装 → 运行 codex → 登录 → 选择项目目录 → 首个小任务”.
- `step-01.webp`: current official Codex CLI install/quickstart page capture.
- `step-02.webp`: locally verified terminal capture showing only `codex --version`, `codex --help`, or the signed-out start screen; exclude account and private paths.

Write `codex.md` with `sequence: 1`, Apache-2.0, `accessTypes: [cli]`, all three desktop OS labels only if the official page still lists them, official OpenAI documentation citations, the official repository, first task “解释当前项目结构并列出三个最安全的小改动”, permissions guidance, update/uninstall commands, ChatGPT/API cost distinction, and a statement that project context may be sent to a cloud model according to the selected task and account policy.

- [ ] **Step 4: Capture and author Cursor evidence**

Create the same four asset names under `public/assets/tools/cursor/`. The original flow is “下载 → 安装 → 登录 → 导入设置 → 打开文件夹 → 小改动 → 审查 diff”. Capture the official downloads page and official quickstart/onboarding page.

Write `cursor.md` with `sequence: 2`, `license: Proprietary`, `accessTypes: [desktop]`, Windows/macOS/Linux only when confirmed by the current download page, Privacy Mode choices, free-versus-paid usage explanation without copying volatile numeric quotas into frontmatter, and first task “解释一个文件后修改按钮文案并审查 diff”.

- [ ] **Step 5: Capture and author Ollama evidence**

Create the four assets under `public/assets/tools/ollama/`. The original flow is “检查内存/磁盘 → 安装 → `ollama pull` → `ollama run` → 验证本地服务 → 管理模型”. Capture the official download page and official quickstart/model-library page.

Write `ollama.md` with `sequence: 3`, MIT, `accessTypes: [cli, local-service]`, `pricing: free`, a small currently listed model chosen from the official library, commands for `ollama pull`, `ollama run`, `ollama list`, `ollama rm`, model-size caution, default local endpoint explanation, and a clear distinction between local inference and any separately configured cloud model/provider.

- [ ] **Step 6: Capture and author ComfyUI evidence**

Create the four assets under `public/assets/tools/comfyui/`. The original flow is “检查系统/GPU/磁盘 → 选择 Desktop/Portable/Manual → 安装 → 创建实例 → 加载模板 → 首次生成”. Capture the current official Windows Desktop installation page and official first-generation/workflow page.

Write `comfyui.md` with `sequence: 4`, GPL-3.0 for the ComfyUI repository, `accessTypes: [desktop, local-service]`, `pricing: free`, Windows Desktop as the fully walked primary path, documented notes for macOS/Linux without claiming local testing, model licensing caution, output/model storage locations, safe uninstall wording that distinguishes the launcher from retained model/output folders, and one built-in-template first generation.

- [ ] **Step 7: Run schema, content, and asset checks**

Run: `python -m unittest tests.test_tool_guides.ToolGuideContractTests.test_international_guides_are_complete_and_image_rich -v`

Run: `npm run check`

Expected: both PASS.

- [ ] **Step 8: Commit the international guide unit**

```bash
git add tests/test_tool_guides.py src/content/tools public/assets/tools/codex public/assets/tools/cursor public/assets/tools/ollama public/assets/tools/comfyui
git commit -m "content: add four international AI tool guides"
```

---

### Task 3: Four domestic guides and their visual evidence

**Files:**
- Modify: `tests/test_tool_guides.py`
- Create: `src/content/tools/trae.md`
- Create: `src/content/tools/cherry-studio.md`
- Create: `src/content/tools/deepseek.md`
- Create: `src/content/tools/kling-ai.md`
- Create: `public/assets/tools/{trae,cherry-studio,deepseek,kling-ai}/{cover.svg,install-flow.svg,step-01.webp,step-02.webp}`

**Interfaces:**
- Consumes: `tools` schema from Task 1.
- Produces: sequences 5–8 with `origin: china`.
- Produces: a complete eight-entry collection for page generation.

- [ ] **Step 1: Add the domestic-content and collection-completeness tests**

Extend `tests/test_tool_guides.py` with the four exact domestic slugs. Reuse the same concrete checks by moving the common assertions into `assert_guide(slug, expected_origin, expected_sequence)`. Add a collection test asserting the directory contains exactly the eight approved `.md` stems and sequences form `set(range(1, 9))`.

- [ ] **Step 2: Run the domestic test and confirm the red state**

Run: `python -m unittest tests.test_tool_guides.ToolGuideContractTests.test_domestic_guides_are_complete_and_image_rich -v`

Expected: FAIL because the four domestic guides do not exist.

- [ ] **Step 3: Capture and author TRAE evidence**

Create `cover.svg`, `install-flow.svg`, and two WebP captures under `public/assets/tools/trae/`. The flow is “进入国内官网 → 选择系统 → 安装 → 登录 → 导入 VS Code 设置 → 打开项目 → 首次协作”. Capture the current `trae.cn` download page and an official Chinese community onboarding/FAQ page.

Write `trae.md` with `sequence: 5`, `license: Proprietary`, `accessTypes: [desktop]`, current Windows/macOS/Linux availability from the official download page, the difference between domestic and international account/model entry points, first task “生成一个单页待办清单并预览”, and conservative privacy wording that asks readers to review the current policy before opening confidential repositories.

- [ ] **Step 4: Capture and author Cherry Studio evidence**

Create the four assets under `public/assets/tools/cherry-studio/`. The flow is “下载安装 → 创建本地配置 → 选择模型服务 → 添加密钥/连接 Ollama → 测试连接 → 首次对话”. Capture the official download page and the official repository/docs provider-configuration screen.

Write `cherry-studio.md` with `sequence: 6`, AGPL-3.0, `accessTypes: [desktop]`, Windows/macOS/Linux, `pricing: free`, explicit notice that model provider/API charges are separate, API key storage and screenshot-redaction guidance, local Ollama as the no-cloud-provider example, and license language limited to factual repository status rather than legal advice.

- [ ] **Step 5: Capture and author DeepSeek evidence**

Create the four assets under `public/assets/tools/deepseek/`. The flow is “选择网页/App → 官方入口 → 登录 → 新建对话 → 开启所需模式 → 核对结果 → 管理历史”. Capture the official product homepage showing web/app entries and the official app/download or chat entry page.

Write `deepseek.md` with `sequence: 7`, `license: Proprietary`, `accessTypes: [web]`, `platforms: [web, android, ios]`, `pricing: freemium`, a first conversation that summarizes a public text rather than private data, a separate short API paragraph linking official docs without turning the guide into an API tutorial, and a precise statement that official web/app use is a cloud service even when some DeepSeek model weights have separate licenses.

- [ ] **Step 6: Capture and author 可灵 AI evidence**

Create the four assets under `public/assets/tools/kling-ai/`. The flow is “进入官方网页/App → 登录 → 选择 AI 视频 → 准备原创素材 → 设置提示词/参数 → 生成 → 审核 → 导出”. Capture the official Chinese homepage and current official quickstart/model guide; never use look-alike navigation sites.

Write `kling-ai.md` with `sequence: 8`, `license: Proprietary`, `accessTypes: [web]`, current web/mobile platforms, `pricing: freemium`, a harmless original 5-second scene example, credit/plan information expressed as “以页面实时显示为准” with the checked model/channel, upload privacy and portrait-rights warnings, watermark/export notes based only on the current official UI, and cleanup/account-data guidance.

- [ ] **Step 7: Run all content checks and Astro schema validation**

Run: `python -m unittest tests.test_tool_guides -v`

Run: `npm run check`

Expected: all current tool tests and Astro checks PASS.

- [ ] **Step 8: Commit the domestic guide unit**

```bash
git add tests/test_tool_guides.py src/content/tools public/assets/tools/trae public/assets/tools/cherry-studio public/assets/tools/deepseek public/assets/tools/kling-ai
git commit -m "content: add four domestic AI tool guides"
```

---

### Task 4: Catalog, navigation, card, and detail rendering

**Files:**
- Modify: `tests/test_tool_guides.py`
- Create: `src/components/ToolCard.astro`
- Create: `src/layouts/ToolGuideLayout.astro`
- Create: `src/pages/tools.astro`
- Create: `src/pages/tools/[...slug].astro`
- Modify: `src/components/SiteNav.astro`
- Modify: `src/layouts/BaseLayout.astro`

**Interfaces:**
- Consumes: `CollectionEntry<"tools">`, label maps, `toolPath()`, `toolUrl()`, `formatDate()`.
- Produces: `ToolCard` props `{ entry: CollectionEntry<"tools"> }`.
- Produces: `ToolGuideLayout` props `{ entry, headings, previous?, next? }`.
- Produces: `tools.html` and `/tools/<slug>.html` with `activeNav="tools"`.

- [ ] **Step 1: Add built-page rendering tests**

Extend `tests/test_tool_guides.py` with an HTML parser and a test that expects:

- `dist/tools.html` and exactly eight `dist/tools/<slug>.html` files.
- no `dist/tools/<slug>/index.html` directories.
- eight catalog cards with `data-tool-item`, exact `data-category`, space-separated platforms/access types, and links under `/personal-ip-website/tools/`.
- one H1 per catalog/detail page.
- one current navigation link to `tools.html` on catalog and detail pages.
- `TechArticle` plus `BreadcrumbList` JSON-LD on details and `CollectionPage` on the catalog.
- the eight required body headings and a quick-judgment block on every detail page.

- [ ] **Step 2: Run the page test and confirm the red state**

Run: `npm run build`

Run: `python -m unittest tests.test_tool_guides.ToolGuidePageTests.test_catalog_and_eight_file_style_detail_pages -v`

Expected: FAIL because `tools.html` and detail routes do not exist.

- [ ] **Step 3: Build `ToolCard.astro`**

Render one `<li data-tool-item>` with category, origin, platforms, and access types on the list item. Render a single full-card link, cover image with width/height and fallback hook, tool name, description, visible origin/category/platform/setup labels, pricing label, and formatted verification date. Use `toolPath(entry.id)` and existing base-path helpers; do not construct root-relative links by hand.

- [ ] **Step 4: Build `tools.astro`**

Query non-draft tools, sort by `sequence`, and render:

- hero “AI 工具指南” and “当前 8 款”.
- three `role="group"` filter rows: category, platform, access type.
- each group starts with an `all` button using `aria-pressed="true"`.
- a polite live result count, eight `ToolCard`s, and a hidden empty-state container with a clear-filters button.
- `CollectionPage` JSON-LD and canonical `tools.html`.

Use data attributes `data-tool-filter-root`, `data-tool-filter-group`, `data-tool-filter`, `data-tool-count`, `data-tool-empty`, and `data-tool-clear` for Task 5.

- [ ] **Step 5: Build `ToolGuideLayout.astro`**

Reuse `BaseLayout`, build `TechArticle` and breadcrumb JSON-LD, and render:

- breadcrumb “工具指南 / 工具名”.
- metadata chips for origin, category, access types, platforms, pricing, open-source status/license, channel, and verification date.
- cover with fixed 16:9 geometry.
- quick-judgment grid with `audience`, `setupSummary`, pricing label, and `privacySummary`.
- TOC from depth-2/depth-3 headings.
- Markdown slot inside `.tool-guide__body`.
- “返回工具指南” plus previous/next guide links by sequence.

Use canonical `tools/${entry.id}.html`, cover Open Graph image, `activeNav="tools"`, and `mainId="tool-guide-page"`.

- [ ] **Step 6: Build the dynamic route**

In `src/pages/tools/[...slug].astro`, query non-draft tools, sort by sequence for adjacent navigation, return one path per `entry.id`, call `render(entry)`, and pass `Content`, headings, previous, and next into `ToolGuideLayout`.

- [ ] **Step 7: Add the global navigation item**

Extend both active-nav unions with `tools`. Insert `{ key: "tools", label: "工具指南", href: "tools.html" }` between learning routes and knowledge base. Do not add any tools markup to `src/pages/index.astro`.

- [ ] **Step 8: Run build and page tests**

Run: `npm run check`

Run: `npm run build`

Run: `python -m unittest tests.test_tool_guides.ToolGuidePageTests -v`

Expected: all PASS.

- [ ] **Step 9: Commit the static page unit**

```bash
git add tests/test_tool_guides.py src/components/ToolCard.astro src/layouts/ToolGuideLayout.astro src/pages/tools.astro src/pages/tools src/components/SiteNav.astro src/layouts/BaseLayout.astro
git commit -m "feat: render AI tool guide catalog and details"
```

---

### Task 5: Compound filters, copy buttons, and responsive styling

**Files:**
- Modify: `tests/test_tool_guides.py`
- Modify: `public/assets/hub.js`
- Modify: `public/assets/hub.css`

**Interfaces:**
- Consumes: Task 4 data attributes and `.tool-guide__body pre`.
- Produces: one active value per filter group and an updated visible count.
- Produces: `[data-copy-code]` buttons with `aria-label`, success status, and safe failure status.
- Preserves: readable eight-card catalog and code blocks when JavaScript is disabled.

- [ ] **Step 1: Add interaction-source and semantic-state tests**

Add tests that inspect `hub.js`, `hub.css`, and built HTML for the exact hooks from Task 4. Assert `aria-pressed`, `hidden`, `navigator.clipboard`, `[data-copy-code]`, `data-tool-filter-group`, `data-tool-clear`, a 44px minimum filter target, responsive grid rules, stable figure aspect ratio, and `prefers-reduced-motion` coverage.

- [ ] **Step 2: Run the interaction test and confirm the red state**

Run: `python -m unittest tests.test_tool_guides.ToolGuideInteractionTests -v`

Expected: FAIL because tool filtering and copy enhancement do not exist.

- [ ] **Step 3: Add compound tool filtering to `hub.js`**

For each `[data-tool-filter-root]`, store this exact state shape:

```js
const state = { category: "all", platform: "all", access: "all" };
```

An item is visible when every non-`all` state value matches its corresponding data attribute. Split platform/access attributes on spaces. Update `hidden`, count text `当前显示 N 款工具`, empty-state class, and every chip’s `is-active`/`aria-pressed`. The clear button resets all three keys and reapplies filters. Keep all cards visible before JavaScript runs.

- [ ] **Step 4: Add code-copy progressive enhancement**

For every `.tool-guide__body pre`, create a wrapper only when the block contains non-empty `<code>`. Add a real button labeled “复制”, use `navigator.clipboard.writeText(code.textContent)`, show “已复制” on success and “复制失败，请手动选择” on rejection, restore “复制” after 1800ms, and announce status via an existing or newly created polite status node. Do not inject buttons into guides without code blocks.

- [ ] **Step 5: Add catalog and guide CSS**

Add focused sections for:

- `.page--tools`, `.tools-hero`, `.tool-filter-group`, `.tool-grid`, `.tool-card`.
- visible chips for origin/category/platform/setup/pricing without color-only meaning.
- `.page--tool-guide`, `.tool-guide__surface`, metadata, cover, quick-judgment grid, TOC, body, figures/captions, code wrapper, copy button, and pager.
- 3-column catalog at wide widths, 2-column under 960px, 1-column under 640px.
- 44px filter/clear/copy targets, visible focus rings, no horizontal figure overflow, and reduced-motion removal of card/button transitions.

Reuse current tokens and reading widths. Keep cobalt accents to headings/actions; do not introduce gradients or a second design system.

- [ ] **Step 6: Run JavaScript syntax, build, and interaction checks**

Run: `node --check public/assets/hub.js`

Run: `npm run build`

Run: `python -m unittest tests.test_tool_guides.ToolGuideInteractionTests -v`

Expected: all PASS.

- [ ] **Step 7: Commit the interaction and style unit**

```bash
git add tests/test_tool_guides.py public/assets/hub.js public/assets/hub.css
git commit -m "feat: add tool filters and guide reading UI"
```

---

### Task 6: Integration contracts and synchronized documentation

**Files:**
- Modify: `tests/test_tool_guides.py`
- Modify: `docs/README.md`
- Modify: `docs/ops.md`
- Modify: `brand-spec.md`
- Modify: `docs/superpowers/specs/2026-08-26-ai-tool-guides-design.md`

**Interfaces:**
- Consumes: built `dist`, sitemap, RSS, navigation, and all eight tool guides.
- Produces: explicit authoring/runbook documentation and release-level regressions.

- [ ] **Step 1: Add release integration tests**

Add tests that assert:

- all prior 22 canonical HTML pages still exist and all nine new tool pages exist.
- all 31 public HTML pages include `tools.html` in global navigation.
- the homepage body has no `data-tool-item`, `data-tool-entry`, `.tool-grid`, or tool count, while its global nav still has `tools.html`.
- sitemap contains `tools.html` and eight detail URLs.
- RSS still has exactly 17 items and none contains `/tools/`.
- no built tool page contains `pagefind`.
- all external links on tool pages use `https://`; official download links never use URL shorteners, cloud-drive mirrors, or third-party navigation sites.
- all images use the GitHub Pages base path and have non-empty alt text.

- [ ] **Step 2: Run the release test and confirm documentation gaps**

Run: `npm test`

Expected before final updates: new code tests pass; documentation-specific assertions fail until Task 6 Step 3.

- [ ] **Step 3: Update `docs/README.md`**

Document the separate `src/content/tools/*.md` collection, exact eight slugs, frontmatter fields, `public/assets/tools/<slug>/` naming, catalog/detail routes, source and screenshot rules, filter/copy behavior, no-homepage-entry rule, and verification commands. State that notes remain 17 items and RSS remains notes-only.

- [ ] **Step 4: Update `docs/ops.md`**

Add a tool-guide publishing checklist: re-check official URL and channel/date, verify the primary OS path, remove secrets from screenshots, ensure four local visuals, verify license/repository, run all checks, inspect the nine sitemap URLs, and confirm RSS stays at 17. Update the two-minute release check to include `tools.html`, one CLI guide, one desktop guide, one web guide, filters, code copy, and 390px layout.

- [ ] **Step 5: Update `brand-spec.md` and the approved spec**

Change the locked navigation to `home / works / learn / tools / notes / about`, add Tool IA as `catalog_filter + static_guides`, state that the homepage body has no tool entry, and update the canonical-page count from 22 to 31. In the design spec, keep status “已获用户批准” and ensure `audience`, `setupSummary`, and `privacySummary` match the implemented schema.

- [ ] **Step 6: Run complete automated verification**

Run: `npm run check`

Run: `npm test`

Run: `node --check public/assets/hub.js`

Run: `git diff --check`

Expected: all checks PASS; RSS count is 17; sitemap contains 31 canonical HTML pages plus existing non-HTML endpoints generated by Astro as applicable.

- [ ] **Step 7: Commit tests and documentation**

```bash
git add tests/test_tool_guides.py docs/README.md docs/ops.md brand-spec.md docs/superpowers/specs/2026-08-26-ai-tool-guides-design.md
git commit -m "docs: document AI tool guide publishing"
```

---

### Task 7: Browser acceptance, final audit, and remote branch

**Files:**
- Modify only files whose browser behavior or content evidence fails the checks below.

**Interfaces:**
- Consumes: local Astro dev/preview server and built pages.
- Produces: verified desktop/mobile catalog and representative CLI, desktop, and web guides.

- [ ] **Step 1: Start the local server and open the catalog**

Run: `npm run dev -- --host 127.0.0.1`

Open: `http://127.0.0.1:4321/personal-ip-website/tools.html`

Verify at approximately 1280px: six-item nav, eight cards, 3-column grid where space permits, complete visible labels, compound filters, live count, empty state, clear button, and no console errors.

- [ ] **Step 2: Verify mobile behavior**

At approximately 390px, verify the collapsed navigation, one-column cards, 44px controls, no horizontal overflow, readable screenshots/captions, and visible focus states using keyboard navigation.

- [ ] **Step 3: Verify representative detail pages**

Open:

- `/personal-ip-website/tools/codex.html` for command copying and OpenAI source links.
- `/personal-ip-website/tools/cherry-studio.html` for installation/provider/privacy/license wording.
- `/personal-ip-website/tools/kling-ai.html` for web access, visual captions, upload/privacy warnings, and no fake install steps.

For each, verify unique H1, quick judgment, TOC, four visuals, no broken image, adjacent navigation, canonical/structured data, and no secrets in text or pixels.

- [ ] **Step 4: Verify homepage exclusion and regression pages**

Open `index.html`, `learn.html`, `notes.html`, and one old note detail. Confirm the homepage body has no tool section, the global nav includes tools, prior learning cards and note filters still work, and the old `.html` note URL remains unchanged.

- [ ] **Step 5: Fix only observed acceptance failures and rerun the full suite**

Use focused patches for any observed issue, then rerun:

```bash
npm run check
npm test
node --check public/assets/hub.js
git diff --check
```

Expected: all PASS and `git status --short` shows only intentional acceptance fixes.

- [ ] **Step 6: Commit acceptance fixes when present**

```bash
git add -u
git commit -m "fix: polish AI tool guide acceptance issues"
```

Skip this commit when the working tree is already clean.

- [ ] **Step 7: Push the feature branch**

Run: `git push -u origin codex/ai-tool-guides`

Expected: remote branch `codex/ai-tool-guides` points to the final verified commit; `main` is untouched.
