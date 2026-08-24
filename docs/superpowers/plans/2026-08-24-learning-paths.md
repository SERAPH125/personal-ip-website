# Learning Paths Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish 12 source-backed learning articles in two ordered tracks, add a Learning Paths hub, preserve the existing content system, and validate feature branches before GitHub Pages deployment.

**Architecture:** Keep every article in the existing `notes` Astro Content Collection. Add an optional `learning` object to article metadata, query it in a new static `learn.html` hub, and keep article canonical URLs under `/notes/`. Reuse existing cards, navigation, static RSS/sitemap generation, and client-side filtering rather than creating a second collection or runtime API.

**Tech Stack:** Astro 7.2.1, TypeScript 6, Markdown Content Collections, static CSS/JavaScript, Python `unittest`, GitHub Actions/Pages.

**Spec:** `docs/superpowers/specs/2026-08-24-learning-paths-design.md`

## Global Constraints

- Keep `site: "https://seraph125.github.io"`, `base: "/personal-ip-website"`, `output: "static"`, and file-style `.html` URLs.
- Existing five article URLs and four Douyin video cards must remain unchanged.
- New article details use `/notes/{slug}.html`; do not create `/learn/{slug}.html` duplicates.
- Do not add Pagefind in this change; reconsider search at about 30 articles or demonstrated demand.
- Do not fabricate personal tests, audience results, or first-hand experience in the 12 research syntheses.
- New covers must be local 1600×900 PNG files with no third-party portraits, logos, or screenshots.
- A pull request may run checks, but only `main` may deploy GitHub Pages.
- Use the verified drafts at `C:\Users\11960\Documents\公众号企微运营\personal-ip-website\docs\content-drafts\01-*.md` through `12-*.md` as the article body sources.

## File Map

- `src/content.config.ts`: validates `sourcesCheckedAt` and the optional learning track/step.
- `src/lib/site.ts`: owns labels and descriptions for `vibe-coding` and `ai-video` tracks.
- `src/content/notes/*.md`: remains the only source of article body content.
- `src/pages/learn.astro`: owns the learning hub query, grouping, ordering, metadata, and markup.
- `src/components/SiteNav.astro` and `src/layouts/BaseLayout.astro`: expose the new navigation destination and active state.
- `src/pages/index.astro`: adds two compact track entry cards, not a 12-article list.
- `src/pages/notes.astro` and `public/assets/hub.js`: add and operate accessible knowledge-base series filters.
- `public/assets/hub.css`: styles the hub, homepage entry cards, knowledge filters, and responsive states.
- `public/assets/covers/learning-*.png`: contains 12 deterministic title-card covers.
- `tests/test_astro_migration_contract.py`: validates all 17 Markdown entries, learning metadata, and cover existence.
- `tests/test_content_hub_upgrade.py`: validates built routes, hub structure, filters, RSS, sitemap, JSON-LD, and links.
- `.github/workflows/deploy.yml`: runs build checks on pull requests and deploys only from `main`.
- `docs/README.md`, `docs/ops.md`, and `brand-spec.md`: document the new content count, IA, workflow, and search decision.

---

### Task 1: Extend the Content Contract

**Files:**
- Modify: `tests/test_astro_migration_contract.py`
- Modify: `src/content.config.ts`
- Modify: `src/lib/site.ts`

**Interfaces:**
- Produces: `data.learning?: { track: "vibe-coding" | "ai-video"; step: number }`
- Produces: `data.sourcesCheckedAt?: Date`
- Produces: `learningTrackMeta` keyed by `vibe-coding` and `ai-video`

- [ ] **Step 1: Write the failing metadata tests**

Add the exact learning map and assertions:

```python
LEARNING_ARTICLES = {
    "vibe-coding-roadmap": ("vibe-coding", 1),
    "writing-agent-tasks": ("vibe-coding", 2),
    "git-for-vibe-coding": ("vibe-coding", 3),
    "ai-code-acceptance-checklist": ("vibe-coding", 4),
    "agent-task-boundaries": ("vibe-coding", 5),
    "ai-coding-productivity": ("vibe-coding", 6),
    "ai-video-roadmap": ("ai-video", 1),
    "ai-video-prompt-formula": ("ai-video", 2),
    "character-consistency": ("ai-video", 3),
    "ai-video-production-workflow": ("ai-video", 4),
    "cloud-vs-local-ai-video": ("ai-video", 5),
    "ai-video-rights-checklist": ("ai-video", 6),
}
```

Update the expected slug set to the existing five plus `LEARNING_ARTICLES`. Add a test that reads `track` and `step` from each new frontmatter block, asserts steps `{1,2,3,4,5,6}` per track, checks `sourcesCheckedAt`, and verifies each `cover` path exists below `public/`.

- [ ] **Step 2: Run the contract test and verify it fails**

Run: `python -m unittest tests.test_astro_migration_contract -v`  
Expected: FAIL because the 12 entries and learning schema do not exist.

- [ ] **Step 3: Add schema and track metadata**

Add to the notes schema:

```ts
sourcesCheckedAt: z.coerce.date().optional(),
learning: z
  .object({
    track: z.enum(["vibe-coding", "ai-video"]),
    step: z.number().int().min(1).max(6),
  })
  .optional(),
```

Add to `src/lib/site.ts`:

```ts
export const learningTrackMeta = {
  "vibe-coding": {
    label: "Vibe Coding",
    eyebrow: "Build with AI",
    description: "从任务描述、Git、安全边界到真实效率，建立可以反复使用的 AI 编程方法。",
  },
  "ai-video": {
    label: "AI 视频",
    eyebrow: "Create with AI",
    description: "从镜头语言、提示词和角色一致性，走到完整生产与合规发布。",
  },
} as const;

export type LearningTrackKey = keyof typeof learningTrackMeta;
```

- [ ] **Step 4: Run the focused test**

Run: `python -m unittest tests.test_astro_migration_contract -v`  
Expected: metadata/schema assertions pass; entry-count assertions still fail until Task 2.

- [ ] **Step 5: Commit the contract**

```bash
git add tests/test_astro_migration_contract.py src/content.config.ts src/lib/site.ts
git commit -m "test: define learning path content contract"
```

### Task 2: Publish the 12 Learning Articles and Covers

**Files:**
- Create: `src/content/notes/vibe-coding-roadmap.md`
- Create: `src/content/notes/writing-agent-tasks.md`
- Create: `src/content/notes/git-for-vibe-coding.md`
- Create: `src/content/notes/ai-code-acceptance-checklist.md`
- Create: `src/content/notes/agent-task-boundaries.md`
- Create: `src/content/notes/ai-coding-productivity.md`
- Create: `src/content/notes/ai-video-roadmap.md`
- Create: `src/content/notes/ai-video-prompt-formula.md`
- Create: `src/content/notes/character-consistency.md`
- Create: `src/content/notes/ai-video-production-workflow.md`
- Create: `src/content/notes/cloud-vs-local-ai-video.md`
- Create: `src/content/notes/ai-video-rights-checklist.md`
- Create: `public/assets/covers/learning-vibe-01.png` through `learning-vibe-06.png`
- Create: `public/assets/covers/learning-video-01.png` through `learning-video-06.png`

**Interfaces:**
- Consumes: the `learning` schema and `learningTrackMeta` from Task 1
- Produces: 12 published `CollectionEntry<"notes">` values with unique global sequences 6—17

- [ ] **Step 1: Add the 12 normalized Markdown entries**

For each source draft, remove `status`, remove the body H1, preserve every reference URL, and replace frontmatter using this exact mapping:

| Sequence | Slug | Series | Track | Step | Cover |
|---:|---|---|---|---:|---|
| 6 | `vibe-coding-roadmap` | `agent` | `vibe-coding` | 1 | `learning-vibe-01.png` |
| 7 | `writing-agent-tasks` | `agent` | `vibe-coding` | 2 | `learning-vibe-02.png` |
| 8 | `git-for-vibe-coding` | `agent` | `vibe-coding` | 3 | `learning-vibe-03.png` |
| 9 | `ai-code-acceptance-checklist` | `agent` | `vibe-coding` | 4 | `learning-vibe-04.png` |
| 10 | `agent-task-boundaries` | `agent` | `vibe-coding` | 5 | `learning-vibe-05.png` |
| 11 | `ai-coding-productivity` | `observe` | `vibe-coding` | 6 | `learning-vibe-06.png` |
| 12 | `ai-video-roadmap` | `aivideo` | `ai-video` | 1 | `learning-video-01.png` |
| 13 | `ai-video-prompt-formula` | `aivideo` | `ai-video` | 2 | `learning-video-02.png` |
| 14 | `character-consistency` | `aivideo` | `ai-video` | 3 | `learning-video-03.png` |
| 15 | `ai-video-production-workflow` | `aivideo` | `ai-video` | 4 | `learning-video-04.png` |
| 16 | `cloud-vs-local-ai-video` | `aivideo` | `ai-video` | 5 | `learning-video-05.png` |
| 17 | `ai-video-rights-checklist` | `aivideo` | `ai-video` | 6 | `learning-video-06.png` |

Every file uses `publishedAt: 2026-08-24`, `sourcesCheckedAt: 2026-08-23`, `featured: false`, `draft: false`, at least three topic tags, and a Chinese `coverAlt` that names its route and step.

- [ ] **Step 2: Generate deterministic title-card covers**

Render 1600×900 PNGs with system fonts and these fixed visual systems:

- Vibe Coding: `#F7F9FC` background, 48px code grid, cobalt `#2764E7`, dark text `#171B24`, label `VIBE CODING · 0N`.
- AI Video: `#0E1324` background, three 16:9 storyboard frames, blue-violet `#7C6CFF`, light text `#F7F8FF`, label `AI VIDEO · 0N`.
- Put the exact article title in the left safe area with no text closer than 96px to an edge.

Verify all outputs report `Width=1600` and `Height=900` before committing.

- [ ] **Step 3: Run content and Astro validation**

Run: `python -m unittest tests.test_astro_migration_contract -v`  
Expected: PASS with 17 Markdown entries and two complete 1—6 tracks.

Run: `npm ci && npm run check`  
Expected: PASS with no content schema errors.

- [ ] **Step 4: Commit content and assets**

```bash
git add src/content/notes public/assets/covers
git commit -m "content: add vibe coding and ai video learning tracks"
```

### Task 3: Build the Learning Paths Hub and Navigation

**Files:**
- Create: `src/pages/learn.astro`
- Modify: `src/components/SiteNav.astro`
- Modify: `src/layouts/BaseLayout.astro`
- Modify: `tests/test_content_hub_upgrade.py`
- Modify: `public/assets/hub.css`

**Interfaces:**
- Consumes: `learningTrackMeta` and article `data.learning`
- Produces: `/personal-ip-website/learn.html`
- Produces: `activeNav="learn"`

- [ ] **Step 1: Write failing built-page tests**

Extend `ARTICLE_PATHS` with all 12 new routes. Add `LEARNING_PATHS` grouped by track. Assert:

```python
self.assertTrue((DIST / "learn.html").is_file())
self.assertEqual(len(parse("learn.html").attrs_for("h1")), 1)
self.assertEqual(
    {attrs.get("data-learning-track") for _, attrs in parse("learn.html").tags if attrs.get("data-learning-track")},
    {"vibe-coding", "ai-video"},
)
self.assertEqual(
    len([attrs for _, attrs in parse("learn.html").tags if attrs.get("data-learning-step")]),
    12,
)
```

Also assert the primary navigation contains `learn.html` on every public page and exactly one current-page link on the hub.

- [ ] **Step 2: Run the focused test and verify failure**

Run: `npm run build && python -m unittest tests.test_content_hub_upgrade.ContentHubUpgradeTests.test_learning_hub_orders_two_complete_tracks -v`  
Expected: FAIL because `learn.html` and its navigation entry do not exist.

- [ ] **Step 3: Implement `learn.astro` and navigation**

Query and sort with:

```ts
const entries = (await getCollection("notes", ({ data }) => !data.draft && Boolean(data.learning)))
  .sort((a, b) => a.data.learning!.step - b.data.learning!.step);
const tracks = Object.entries(learningTrackMeta).map(([key, meta]) => ({
  key,
  meta,
  entries: entries.filter((entry) => entry.data.learning?.track === key),
}));
```

Render two `section` elements with `data-learning-track`, six linked steps with `data-learning-step`, a `CollectionPage` JSON-LD object, and base-safe article links from `articlePath(entry.id)`.

Update both active-nav unions to include `"learn"`. Insert the navigation item between works and notes:

```ts
{ key: "learn", label: "学习路线", href: "learn.html" }
```

- [ ] **Step 4: Style desktop, mobile, and focus states**

Add focused classes `.learn-hero`, `.learning-overview`, `.learning-track`, `.learning-step`, and their `:hover`, `:focus-visible`, and `@media (max-width: 720px)` rules. Use existing spacing, borders, type tokens, and at most two accent uses in the initial viewport.

- [ ] **Step 5: Run the hub tests**

Run: `npm run check && npm test`  
Expected: learning hub assertions pass; remaining homepage/filter assertions may still fail until Task 4.

- [ ] **Step 6: Commit the hub**

```bash
git add src/pages/learn.astro src/components/SiteNav.astro src/layouts/BaseLayout.astro public/assets/hub.css tests/test_content_hub_upgrade.py
git commit -m "feat: add ordered learning paths hub"
```

### Task 4: Add Homepage Entrypoints and Knowledge Filters

**Files:**
- Modify: `src/pages/index.astro`
- Modify: `src/pages/notes.astro`
- Modify: `public/assets/hub.js`
- Modify: `public/assets/hub.css`
- Modify: `tests/test_content_hub_upgrade.py`
- Modify: `tests/test_home_related_resource.py`

**Interfaces:**
- Consumes: `learningTrackMeta`, learning entries, and `data-note-series`
- Produces: two `.home-learning-card` links
- Produces: reusable filter root identified by `data-series-filter-root`

- [ ] **Step 1: Write failing homepage and filter tests**

Assert the homepage has exactly two links with `data-learning-entry`, both pointing to `learn.html` with `#vibe-coding` and `#ai-video`. Assert the knowledge page exposes filter values `{all, agent, observe, aivideo, industry}`, 17 note cards, a live result count, and an empty-state element.

- [ ] **Step 2: Run tests and verify failure**

Run: `npm test`  
Expected: FAIL on the new homepage-entry and knowledge-filter assertions.

- [ ] **Step 3: Add compact homepage entry cards**

In `index.astro`, derive track counts from the collection and render a `home-learning` section after `home-recent`. Each card includes the track label, description, `6 篇 · 按顺序学习`, and a base-safe `learn.html#track` link.

- [ ] **Step 4: Generalize filtering and add knowledge controls**

Wrap both works and notes filterable regions with `data-series-filter-root`. Within each root, use `data-filter-item` and `data-series` on items. Update `hub.js` to initialize every root independently:

```js
qsa("[data-series-filter-root]").forEach(function (root) {
  const chips = qsa("[data-series-filter]", root);
  const items = qsa("[data-filter-item]", root);
  // apply the root's series query, hidden state, count, empty state, and pressed state
});
```

Use `data-filter-unit="作品"` or `data-filter-unit="篇文章"` for correct result copy. Keep the shareable `?series=` query and sanitize values through `seriesMeta`.

- [ ] **Step 5: Add responsive and accessible styles**

Style `.home-learning`, `.home-learning-grid`, `.home-learning-card`, and `.notes-filters`. Preserve visible focus, 44px chip targets, reduced-motion behavior, and the existing mobile navigation.

- [ ] **Step 6: Run JavaScript and site tests**

Run: `node --check public/assets/hub.js`  
Expected: PASS.

Run: `npm run check && npm test`  
Expected: PASS with two homepage entries, 17 knowledge cards, and unchanged four-video works behavior.

- [ ] **Step 7: Commit entrypoints and filters**

```bash
git add src/pages/index.astro src/pages/notes.astro public/assets/hub.js public/assets/hub.css tests/test_content_hub_upgrade.py tests/test_home_related_resource.py
git commit -m "feat: surface learning paths across the content hub"
```

### Task 5: Add Pull Request Validation and Synchronize Documentation

**Files:**
- Modify: `.github/workflows/deploy.yml`
- Modify: `docs/README.md`
- Modify: `docs/ops.md`
- Modify: `brand-spec.md`
- Modify: `tests/test_content_hub_upgrade.py`

**Interfaces:**
- Produces: PR-only build validation with no deployment
- Produces: main-only GitHub Pages deployment

- [ ] **Step 1: Add a workflow contract test**

Read `.github/workflows/deploy.yml` and assert it contains `pull_request`, targets `main`, and guards the deploy job with both `github.event_name != 'pull_request'` and `github.ref == 'refs/heads/main'`.

- [ ] **Step 2: Run the workflow test and verify failure**

Run: `python -m unittest tests.test_content_hub_upgrade -v`  
Expected: FAIL because the workflow has no pull-request trigger or deploy guard.

- [ ] **Step 3: Update the GitHub Actions workflow**

Use these triggers and deploy guard:

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

deploy:
  if: github.event_name != 'pull_request' && github.ref == 'refs/heads/main'
```

Keep checkout, Node 22, `npm ci`, `npm run check`, `npm test`, artifact upload, and deploy-pages actions unchanged.

- [ ] **Step 4: Update all affected documentation**

Document 17 articles, `learn.html`, optional learning frontmatter, the 12 learning covers, PR validation, RSS count 17, knowledge filters, and the decision to defer Pagefind until about 30 articles. Remove statements that hardcode five articles or say search is deferred only because content is below 12.

- [ ] **Step 5: Run the documentation and workflow tests**

Run: `python -m unittest tests.test_content_hub_upgrade -v`  
Expected: PASS.

- [ ] **Step 6: Commit workflow and docs**

```bash
git add .github/workflows/deploy.yml docs/README.md docs/ops.md brand-spec.md tests/test_content_hub_upgrade.py
git commit -m "ci: validate learning hub pull requests"
```

### Task 6: Full Verification, Visual Review, and Branch Push

**Files:**
- Verify only: all changed files

**Interfaces:**
- Consumes: all prior task outputs
- Produces: a pushed `codex/learning-paths` branch with no failing checks

- [ ] **Step 1: Run the complete automated suite**

```bash
npm run check
npm test
node --check public/assets/hub.js
git diff --check origin/main...HEAD
```

Expected: all commands exit 0; Python reports zero failures/errors.

- [ ] **Step 2: Inspect generated output contracts**

Confirm `dist/learn.html`, all 17 `dist/notes/*.html` files, `dist/rss.xml`, `dist/sitemap-0.xml`, and all 12 `dist/assets/covers/learning-*.png` files exist. Confirm RSS has 17 items and sitemap includes `learn.html` plus all article canonicals.

- [ ] **Step 3: Review desktop and mobile pages**

Start `npm run preview`. At 1280×720 and 390×844 inspect:

- `index.html`: existing hero and three videos remain primary; two learning cards appear below.
- `learn.html`: two complete tracks, readable step order, no horizontal overflow.
- `notes.html`: 17 cards, five filters, correct count and empty state.
- `notes/vibe-coding-roadmap.html` and `notes/ai-video-roadmap.html`: one H1, working table of contents, correct cover/metadata, readable long-form layout.

Record console errors and broken internal requests; acceptable result is none.

- [ ] **Step 4: Review the final diff and working tree**

Run: `git status --short --branch` and `git diff --stat origin/main...HEAD`.  
Expected: only intentional source, content, assets, tests, workflow, specs, plans, and docs changes; no `dist`, `.astro`, or `node_modules` tracked.

- [ ] **Step 5: Push the feature branch**

Run: `git push origin codex/learning-paths`  
Expected: remote branch advances to the final verified commit. Do not merge `main` or create a pull request unless separately authorized.
