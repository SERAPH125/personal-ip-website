import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
TOOL_CONTENT = ROOT / "src" / "content" / "tools"
INTERNATIONAL_GUIDES = {
    "codex": 1,
    "cursor": 2,
    "ollama": 3,
    "comfyui": 4,
    "chatgpt-desktop": 9,
    "claude-desktop": 10,
    "invokeai": 12,
    "stable-diffusion-webui": 13,
    "krita-ai-diffusion": 14,
    "github-copilot": 15,
    "claude-code": 16,
    "cline": 17,
    "framepack": 20,
}
CHINA_GUIDES = {
    "trae": 5,
    "cherry-studio": 6,
    "deepseek": 7,
    "kling-ai": 8,
    "kimi-work": 11,
    "jianying-pro": 18,
    "filmora": 19,
}
SECOND_BATCH_GUIDES = {
    "chatgpt-desktop",
    "claude-desktop",
    "kimi-work",
    "invokeai",
    "stable-diffusion-webui",
    "krita-ai-diffusion",
    "github-copilot",
    "claude-code",
    "cline",
    "jianying-pro",
    "filmora",
    "framepack",
}
OFFICIAL_SCREENSHOT_GUIDES = ("codex", "cursor", "ollama", "comfyui")
REQUIRED_GUIDE_HEADINGS = (
    "快速判断",
    "安装前检查",
    "图解安装",
    "第一次使用",
    "常见问题",
    "更新与卸载",
    "费用、隐私与开源信息",
    "官方资料与核验日期",
)
REQUIRED_TOOL_FRONTMATTER = {
    "title",
    "toolName",
    "description",
    "audience",
    "setupSummary",
    "privacySummary",
    "origin",
    "category",
    "accessTypes",
    "platforms",
    "pricing",
    "openSource",
    "license",
    "officialUrl",
    "versionChecked",
    "verifiedAt",
    "cover",
    "coverAlt",
    "sequence",
    "draft",
}
EXPECTED_CATEGORIES = {
    "codex": "ai-coding",
    "cursor": "ai-coding",
    "ollama": "language-model",
    "comfyui": "image-model",
    "trae": "ai-coding",
    "cherry-studio": "language-model",
    "deepseek": "language-model",
    "kling-ai": "video-model",
    "chatgpt-desktop": "language-model",
    "claude-desktop": "language-model",
    "kimi-work": "language-model",
    "invokeai": "image-model",
    "stable-diffusion-webui": "image-model",
    "krita-ai-diffusion": "image-model",
    "github-copilot": "ai-coding",
    "claude-code": "ai-coding",
    "cline": "ai-coding",
    "jianying-pro": "video-model",
    "filmora": "video-model",
    "framepack": "video-model",
}
EXPECTED_DIRECTORY_GROUPS = {
    "language-model": (
        "ollama", "cherry-studio", "deepseek", "chatgpt-desktop",
        "claude-desktop", "kimi-work",
    ),
    "image-model": (
        "comfyui", "invokeai", "stable-diffusion-webui", "krita-ai-diffusion",
    ),
    "ai-coding": (
        "codex", "cursor", "trae", "github-copilot", "claude-code", "cline",
    ),
    "video-model": ("kling-ai", "jianying-pro", "filmora", "framepack"),
}
EXPECTED_TOOL_NAMES = {
    "codex": "Codex",
    "cursor": "Cursor",
    "ollama": "Ollama",
    "comfyui": "ComfyUI",
    "trae": "TRAE",
    "cherry-studio": "Cherry Studio",
    "deepseek": "DeepSeek",
    "kling-ai": "可灵 AI",
    "chatgpt-desktop": "ChatGPT Desktop",
    "claude-desktop": "Claude Desktop",
    "kimi-work": "Kimi Work",
    "invokeai": "InvokeAI",
    "stable-diffusion-webui": "Stable Diffusion WebUI",
    "krita-ai-diffusion": "Krita AI Diffusion",
    "github-copilot": "GitHub Copilot",
    "claude-code": "Claude Code",
    "cline": "Cline",
    "jianying-pro": "剪映专业版",
    "filmora": "Filmora",
    "framepack": "FramePack",
}
EXPECTED_POLICY_LINKS = {
    "codex": "https://github.com/openai/codex/security",
    "cursor": "https://cursor.com/privacy",
    "ollama": "https://docs.ollama.com/faq",
    "comfyui": "https://github.com/Comfy-Org/ComfyUI/security",
    "trae": "https://www.trae.cn/privacy-policy",
    "cherry-studio": "https://github.com/CherryHQ/cherry-studio/blob/main/PRIVACY.md",
    "deepseek": "https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html",
    "kling-ai": "https://kling.ai/docs/privacy-policy",
    "chatgpt-desktop": "https://openai.com/policies/privacy-policy/",
    "claude-desktop": "https://www.anthropic.com/legal/privacy",
    "kimi-work": "https://www.kimi.com/user/agreement/userPrivacy?version=v2",
    "invokeai": "https://github.com/invoke-ai/InvokeAI/security",
    "stable-diffusion-webui": "https://github.com/AUTOMATIC1111/stable-diffusion-webui/security",
    "krita-ai-diffusion": "https://github.com/Acly/krita-ai-diffusion/security",
    "github-copilot": "https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement",
    "claude-code": "https://www.anthropic.com/legal/privacy",
    "cline": "https://github.com/cline/cline/security",
    "jianying-pro": "https://www.capcut.com/clause/privacy",
    "filmora": "https://www.wondershare.com/privacy.html",
    "framepack": "https://github.com/lllyasviel/FramePack/security",
}


class PageProbe(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags: list[tuple[str, dict[str, str]]] = []
        self.text_parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, {key: value or "" for key, value in attrs}))

    def handle_data(self, data):
        if data.strip():
            self.text_parts.append(data.strip())

    @property
    def text(self):
        return " ".join(self.text_parts)


def parse_page(path: Path) -> tuple[str, PageProbe]:
    html = path.read_text(encoding="utf-8")
    probe = PageProbe()
    probe.feed(html)
    return html, probe


def frontmatter(markdown: str) -> str:
    match = re.match(r"^---\n(?P<body>.*?)\n---\n", markdown, re.S)
    return match.group("body") if match else ""


def frontmatter_keys(markdown: str) -> set[str]:
    return {
        line.split(":", 1)[0].strip()
        for line in frontmatter(markdown).splitlines()
        if line and not line.startswith((" ", "\t", "#")) and ":" in line
    }


class ToolGuideContractTests(unittest.TestCase):
    def test_tools_collection_schema_and_shared_metadata(self):
        config = (ROOT / "src" / "content.config.ts").read_text(encoding="utf-8")
        site = (ROOT / "src" / "lib" / "site.ts").read_text(encoding="utf-8")

        self.assertIn('base: "./src/content/tools"', config)
        for field in (
            "toolName",
            "description",
            "audience",
            "setupSummary",
            "privacySummary",
            "origin",
            "category",
            "accessTypes",
            "platforms",
            "pricing",
            "openSource",
            "license",
            "officialUrl",
            "downloadUrl",
            "repositoryUrl",
            "versionChecked",
            "verifiedAt",
            "cover",
            "coverAlt",
            "sequence",
            "draft",
        ):
            self.assertRegex(config, rf"\b{field}\b")
        self.assertRegex(config, r"export const collections = \{ notes, tools \}")
        self.assertRegex(
            config,
            r'category:\s*z\.enum\(\[\s*"language-model",\s*"image-model",\s*"ai-coding",\s*"video-model"',
        )

        for symbol in (
            "toolCategoryMeta",
            "toolOriginMeta",
            "toolAccessMeta",
            "toolPlatformMeta",
            "toolPricingMeta",
            "toolPath",
            "toolUrl",
        ):
            self.assertIn(symbol, site)
        self.assertIn("tools/${slug}.html", site)

    def assert_guide(self, slug: str, expected_origin: str, expected_sequence: int):
        guide_path = TOOL_CONTENT / f"{slug}.md"
        self.assertTrue(guide_path.is_file(), f"{slug} 指南不存在")
        markdown = guide_path.read_text(encoding="utf-8")
        block = frontmatter(markdown)

        self.assertTrue(
            REQUIRED_TOOL_FRONTMATTER.issubset(frontmatter_keys(markdown)),
            f"{slug} 缺少必填 frontmatter",
        )
        self.assertRegex(block, rf"(?m)^origin:\s*{re.escape(expected_origin)}$")
        self.assertRegex(block, rf"(?m)^sequence:\s*{expected_sequence}$")
        self.assertRegex(block, r"(?m)^verifiedAt:\s*2026-08-26$")
        self.assertRegex(block, r'(?m)^license:\s*["\']?\S.+$')

        for heading in REQUIRED_GUIDE_HEADINGS:
            self.assertIn(f"\n## {heading}\n", markdown, f"{slug} 缺少 {heading}")

        cover_match = re.search(r'(?m)^cover:\s*["\']?([^"\'\n]+)', block)
        self.assertIsNotNone(cover_match, f"{slug} 缺少布局封面")
        self.assertTrue(
            (ROOT / "public" / cover_match.group(1).lstrip("/")).is_file(),
            f"{slug} 布局封面不存在",
        )
        images = re.findall(r"!\[([^\]]+)\]\((/personal-ip-website/assets/tools/[^)]+\.(?:svg|webp))\)", markdown)
        self.assertGreaterEqual(len(images), 3, f"{slug} 正文至少需要 3 张本地图片")
        self.assertLessEqual(len(images), 5, f"{slug} 正文核心图片不应超过 5 张")
        for alt, asset_path in images:
            self.assertTrue(alt.strip(), f"{slug} 图片缺少替代文本")
            self.assertTrue(
                (ROOT / "public" / asset_path.removeprefix("/personal-ip-website/")).is_file(),
                f"{slug} 图片不存在：{asset_path}",
            )

    def test_international_guides_are_complete_and_image_rich(self):
        for slug, sequence in INTERNATIONAL_GUIDES.items():
            with self.subTest(slug=slug):
                self.assert_guide(slug, "international", sequence)

    def test_china_guides_are_complete_and_image_rich(self):
        for slug, sequence in CHINA_GUIDES.items():
            with self.subTest(slug=slug):
                self.assert_guide(slug, "china", sequence)

    def test_official_screenshots_have_adjacent_source_and_capture_date(self):
        for slug in OFFICIAL_SCREENSHOT_GUIDES:
            markdown = (TOOL_CONTENT / f"{slug}.md").read_text(encoding="utf-8")
            screenshots = list(
                re.finditer(
                    r"!\[[^\]]+\]\(/personal-ip-website/assets/tools/[^)]+\.webp\)",
                    markdown,
                )
            )
            self.assertEqual(len(screenshots), 2, f"{slug} 应有两张官方页面截图")
            for screenshot in screenshots:
                adjacent = markdown[screenshot.end() : screenshot.end() + 320]
                self.assertIn('class="tool-image-source"', adjacent, slug)
                self.assertIn("https://", adjacent, slug)
                self.assertIn("2026-08-26", adjacent, slug)

    def test_second_batch_always_has_a_computer_install_path(self):
        for slug in SECOND_BATCH_GUIDES:
            guide_path = TOOL_CONTENT / f"{slug}.md"
            self.assertTrue(guide_path.is_file(), f"{slug} 指南不存在")
            markdown = guide_path.read_text(encoding="utf-8")
            block = frontmatter(markdown)
            access_match = re.search(r"(?m)^accessTypes:\s*\[([^\]]+)\]$", block)
            platform_match = re.search(r"(?m)^platforms:\s*\[([^\]]+)\]$", block)
            self.assertIsNotNone(access_match, slug)
            self.assertIsNotNone(platform_match, slug)
            self.assertRegex(access_match.group(1), r"\b(desktop|cli|local-service)\b", slug)
            self.assertRegex(platform_match.group(1), r"\b(windows|macos|linux)\b", slug)

    def test_every_guide_links_an_official_privacy_or_security_source(self):
        for slug, policy_url in EXPECTED_POLICY_LINKS.items():
            markdown = (TOOL_CONTENT / f"{slug}.md").read_text(encoding="utf-8")
            self.assertIn(policy_url, markdown, f"{slug} 缺少官方隐私或安全来源")


class ToolGuidePageTests(unittest.TestCase):
    def test_catalog_groups_named_tools_in_sidebar_and_content_sections(self):
        catalog_html, catalog = parse_page(ROOT / "dist" / "tools.html")

        sidebars = [
            attrs
            for tag, attrs in catalog.tags
            if tag == "aside" and "data-tool-sidebar" in attrs
        ]
        disclosures = [
            attrs
            for tag, attrs in catalog.tags
            if tag == "details" and "data-tool-directory-disclosure" in attrs
        ]

        self.assertEqual(len(sidebars), 1, "工具目录需要一个左侧模型目录")
        self.assertEqual(len(disclosures), 1, "移动端需要一个原生模型目录折叠区")
        self.assertIn("open", disclosures[0], "桌面端无 JavaScript 时模型目录也应保持可见")
        self.assertEqual(catalog_html.count("data-tool-directory-nav-group="), 4)
        self.assertEqual(catalog_html.count("data-tool-directory-section="), 4)
        self.assertEqual(catalog_html.count("data-tool-directory-link="), 20)
        self.assertEqual(catalog_html.count("data-tool-item"), 20)
        self.assertIn("模型目录", catalog.text)
        self.assertNotIn("data-tool-filter-group=", catalog_html)

        for category, slugs in EXPECTED_DIRECTORY_GROUPS.items():
            self.assertIn(f'data-tool-directory-nav-group="{category}"', catalog_html)
            self.assertIn(f'data-tool-directory-section="{category}"', catalog_html)
            for slug in slugs:
                self.assertRegex(
                    catalog_html,
                    rf'<a(?=[^>]*data-tool-directory-link="{slug}")(?=[^>]*href="#tool-{slug}")[^>]*>{re.escape(EXPECTED_TOOL_NAMES[slug])}</a>',
                )
                self.assertRegex(
                    catalog_html,
                    rf'<li(?=[^>]*id="tool-{slug}")(?=[^>]*data-category="{category}")[^>]*data-tool-item',
                )
        self.assertLess(
            catalog_html.index("data-tool-sidebar"),
            catalog_html.index('class="tools-content"'),
            "左侧模型目录应先于右侧工具内容渲染",
        )

    def test_catalog_and_twenty_file_style_detail_pages(self):
        dist = ROOT / "dist"
        catalog_path = dist / "tools.html"
        detail_dir = dist / "tools"
        self.assertTrue(catalog_path.is_file(), "缺少 dist/tools.html")
        self.assertTrue(detail_dir.is_dir(), "缺少 dist/tools 详情目录")

        expected_slugs = set(INTERNATIONAL_GUIDES) | set(CHINA_GUIDES)
        detail_files = {path.stem: path for path in detail_dir.glob("*.html")}
        self.assertEqual(set(detail_files), expected_slugs)
        self.assertEqual(list(detail_dir.glob("*/index.html")), [])

        catalog_html, catalog = parse_page(catalog_path)
        self.assertEqual(sum(tag == "h1" for tag, _ in catalog.tags), 1)
        self.assertIn('"@type":"CollectionPage"', catalog_html)
        cards = [attrs for _, attrs in catalog.tags if "data-tool-item" in attrs]
        self.assertEqual(len(cards), 20)
        for card in cards:
            slug = card.get("data-tool-slug")
            self.assertIn(slug, expected_slugs)
            self.assertEqual(card.get("data-category"), EXPECTED_CATEGORIES[slug])
            self.assertTrue(card.get("data-platforms"))
            self.assertTrue(card.get("data-access"))
        catalog_links = [attrs for tag, attrs in catalog.tags if tag == "a"]
        for slug in expected_slugs:
            self.assertTrue(
                any(
                    attrs.get("href", "").endswith(f"/tools/{slug}.html")
                    for attrs in catalog_links
                ),
                f"目录缺少 {slug} 链接",
            )

        for page_path in [catalog_path, *detail_files.values()]:
            _, page = parse_page(page_path)
            current_links = [
                attrs
                for tag, attrs in page.tags
                if tag == "a" and attrs.get("aria-current") == "page"
            ]
            self.assertTrue(
                any(attrs.get("href", "").endswith("/tools.html") for attrs in current_links),
                f"{page_path.name} 的工具导航未激活",
            )

        for slug, page_path in detail_files.items():
            html, page = parse_page(page_path)
            self.assertEqual(sum(tag == "h1" for tag, _ in page.tags), 1, slug)
            self.assertIn('"@type":"TechArticle"', html, slug)
            self.assertIn('"@type":"BreadcrumbList"', html, slug)
            self.assertTrue(
                any("data-tool-quick" in attrs for _, attrs in page.tags),
                f"{slug} 缺少快速判断区",
            )
            for heading in REQUIRED_GUIDE_HEADINGS:
                self.assertIn(heading, page.text, f"{slug} 构建页缺少 {heading}")


class ToolGuideInteractionTests(unittest.TestCase):
    def test_model_directory_copy_enhancement_and_responsive_styles(self):
        script = (ROOT / "public" / "assets" / "hub.js").read_text(encoding="utf-8")
        css = (ROOT / "public" / "assets" / "hub.css").read_text(encoding="utf-8")
        catalog_html = (ROOT / "dist" / "tools.html").read_text(encoding="utf-8")

        self.assertIn("navigator.clipboard", script)
        self.assertIn("data-copy-code", script)
        self.assertIn("1800", script)

        self.assertNotIn("data-tool-filter-root", catalog_html)
        self.assertNotIn("data-tool-clear", catalog_html)

        for selector in (
            ".page--tools",
            ".tools-shell",
            ".tools-sidebar__sticky",
            ".tool-directory-disclosure",
            ".tool-directory__group",
            ".tool-directory-section",
            ".tool-grid",
            ".tool-card",
            ".page--tool-guide",
            ".tool-guide__quick",
            ".tool-guide__body",
            ".code-copy-button",
        ):
            self.assertIn(selector, css)
        self.assertRegex(css, r"\.tool-grid\s*\{[^}]*grid-template-columns:\s*repeat\(2", re.S)
        self.assertIn("@media (max-width: 820px)", css)
        self.assertIn("@media (max-width: 640px)", css)
        self.assertRegex(css, r"(?s)\.tool-directory__group li a .*min-height:\s*44px")
        self.assertIn("aspect-ratio: 16 / 9", css)
        self.assertRegex(css, r"\.tool-card__cover\s*\{[^}]*height:\s*auto", re.S)
        self.assertRegex(css, r"\.tool-guide__cover\s*\{[^}]*height:\s*auto", re.S)
        self.assertRegex(css, r"\.back-to-top\s*\{[^}]*visibility:\s*hidden", re.S)
        self.assertRegex(css, r"\.back-to-top\.is-visible\s*\{[^}]*visibility:\s*visible", re.S)
        self.assertIn(".tool-image-source", css)
        self.assertIn("@media (prefers-reduced-motion: reduce)", css)


class ToolGuideReleaseTests(unittest.TestCase):
    def test_release_keeps_home_clean_navigation_global_and_feeds_separate(self):
        dist = ROOT / "dist"
        note_pages = sorted((dist / "notes").glob("*.html"))
        tool_pages = sorted((dist / "tools").glob("*.html"))
        top_pages = [dist / name for name in ("index.html", "works.html", "learn.html", "notes.html", "about.html")]
        canonical_pages = [*top_pages, *note_pages, dist / "tools.html", *tool_pages]

        self.assertEqual(len(note_pages), 17)
        self.assertEqual(len(tool_pages), 20)
        self.assertEqual(len(canonical_pages), 43)
        self.assertTrue(all(path.is_file() for path in canonical_pages))

        for page_path in canonical_pages:
            html = page_path.read_text(encoding="utf-8")
            self.assertIn("/personal-ip-website/tools.html", html, page_path.name)
            self.assertNotIn("pagefind", html.lower(), page_path.name)

        home_html = (dist / "index.html").read_text(encoding="utf-8")
        home_main = re.search(r"<main\b.*?</main>", home_html, re.S)
        self.assertIsNotNone(home_main)
        for forbidden in ("data-tool-item", "data-tool-entry", "tool-grid", "tools-count"):
            self.assertNotIn(forbidden, home_main.group(0))
        self.assertIn("/personal-ip-website/tools.html", home_html)

        sitemap = (dist / "sitemap-0.xml").read_text(encoding="utf-8")
        self.assertIn("/personal-ip-website/tools.html", sitemap)
        for slug in set(INTERNATIONAL_GUIDES) | set(CHINA_GUIDES):
            self.assertIn(f"/personal-ip-website/tools/{slug}.html", sitemap)

        rss = (dist / "rss.xml").read_text(encoding="utf-8")
        self.assertEqual(rss.count("<item>"), 17)
        self.assertNotIn("/tools/", rss)

    def test_tool_links_and_images_are_publishable(self):
        pages = [ROOT / "dist" / "tools.html", *(ROOT / "dist" / "tools").glob("*.html")]
        blocked_hosts = ("bit.ly", "t.cn", "pan.baidu.com", "lanzou", "cloud.189.cn")

        for page_path in pages:
            _, page = parse_page(page_path)
            for tag, attrs in page.tags:
                if tag == "a":
                    href = attrs.get("href", "")
                    if href.startswith("http"):
                        self.assertTrue(href.startswith("https://"), f"非 HTTPS 外链：{href}")
                        hostname = urlparse(href).hostname or ""
                        self.assertFalse(
                            any(hostname == host or hostname.endswith(f".{host}") for host in blocked_hosts),
                            href,
                        )
                if tag == "img":
                    self.assertTrue(attrs.get("alt", "").strip(), f"{page_path.name} 图片缺少 alt")
                    self.assertTrue(
                        attrs.get("src", "").startswith("/personal-ip-website/assets/tools/"),
                        f"{page_path.name} 工具图片未使用站点 base path",
                    )

    def test_development_and_operations_docs_cover_tool_guides(self):
        readme = (ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        ops = (ROOT / "docs" / "ops.md").read_text(encoding="utf-8")
        brand = (ROOT / "brand-spec.md").read_text(encoding="utf-8")
        spec = (ROOT / "docs" / "superpowers" / "specs" / "2026-08-26-ai-tool-guides-design.md").read_text(encoding="utf-8")

        for phrase in (
            "src/content/tools/*.md",
            "public/assets/tools/<slug>/",
            "tools.html",
            "tools/<slug>.html",
            "首页正文不增加工具入口",
            "RSS 仍只包含 17 篇",
        ):
            self.assertIn(phrase, readme)
        for phrase in ("工具指南发布清单", "四张本地图片", "390px", "RSS 保持 17 篇"):
            self.assertIn(phrase, ops)
        self.assertIn("home / works / learn / tools / notes / about", brand)
        self.assertIn("43 个 canonical", brand)
        self.assertIn("grouped_model_directory + static_guides", brand)
        self.assertIn("首页正文不提供工具入口", brand)
        for field in ("audience", "setupSummary", "privacySummary"):
            self.assertIn(field, spec)

    def test_pages_workflow_isolates_pr_runs_and_checks_browser_javascript(self):
        workflow = (ROOT / ".github" / "workflows" / "deploy.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("node --check public/assets/hub.js", workflow)
        self.assertNotRegex(workflow, r"(?m)^\s*group:\s*pages\s*$")
        self.assertIn("github.event_name", workflow)
        self.assertIn("github.event.pull_request.number", workflow)


if __name__ == "__main__":
    unittest.main()
