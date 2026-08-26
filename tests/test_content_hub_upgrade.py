import json
import re
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
BASE_PATH = "/personal-ip-website/"
DOUYIN_PROFILE = (
    "https://www.douyin.com/user/"
    "MS4wLjABAAAAwwu7aqbhsXBribQpl5JPNTqXz-9ZRfmL2uZ8c70_l5JnwQsaYZJzGpk3ERvhzrA8"
)
ARTICLE_PATHS = [
    "notes/fable-5-safety-lock.html",
    "notes/ai-storyboard-perspective.html",
    "notes/seedance-2-workflows.html",
    "notes/codex-5-levels.html",
    "notes/ai-refund-fraud-report.html",
    "notes/vibe-coding-roadmap.html",
    "notes/writing-agent-tasks.html",
    "notes/git-for-vibe-coding.html",
    "notes/ai-code-acceptance-checklist.html",
    "notes/agent-task-boundaries.html",
    "notes/ai-coding-productivity.html",
    "notes/ai-video-roadmap.html",
    "notes/ai-video-prompt-formula.html",
    "notes/character-consistency.html",
    "notes/ai-video-production-workflow.html",
    "notes/cloud-vs-local-ai-video.html",
    "notes/ai-video-rights-checklist.html",
]
VIDEO_ARTICLE_PATHS = {
    "notes/fable-5-safety-lock.html",
    "notes/ai-storyboard-perspective.html",
    "notes/seedance-2-workflows.html",
    "notes/codex-5-levels.html",
}
LEARNING_PATHS = {
    "vibe-coding": {
        1: "notes/vibe-coding-roadmap.html",
        2: "notes/writing-agent-tasks.html",
        3: "notes/git-for-vibe-coding.html",
        4: "notes/ai-code-acceptance-checklist.html",
        5: "notes/agent-task-boundaries.html",
        6: "notes/ai-coding-productivity.html",
    },
    "ai-video": {
        1: "notes/ai-video-roadmap.html",
        2: "notes/ai-video-prompt-formula.html",
        3: "notes/character-consistency.html",
        4: "notes/ai-video-production-workflow.html",
        5: "notes/cloud-vs-local-ai-video.html",
        6: "notes/ai-video-rights-checklist.html",
    },
}
LEARNING_TOOLKITS = {
    "vibe-coding": ["codex", "cursor", "trae", "github-copilot", "claude-code", "cline"],
    "ai-video": ["kling-ai", "jianying-pro", "filmora", "framepack", "comfyui", "invokeai"],
}


class DocumentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.text = []
        self.json_ld = []
        self._in_json_ld = False
        self._json_buffer = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.tags.append((tag, attributes))
        if tag == "script" and attributes.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._json_buffer = []

    def handle_endtag(self, tag):
        if tag == "script" and self._in_json_ld:
            self.json_ld.append(json.loads("".join(self._json_buffer)))
            self._in_json_ld = False
            self._json_buffer = []

    def handle_data(self, data):
        if self._in_json_ld:
            self._json_buffer.append(data)
        else:
            self.text.append(data)

    def attrs_for(self, tag):
        return [attrs for candidate, attrs in self.tags if candidate == tag]


def parse(relative_path):
    parser = DocumentParser()
    parser.feed((DIST / relative_path).read_text(encoding="utf-8"))
    return parser


def schema_types(payload):
    nodes = payload.get("@graph", [payload]) if isinstance(payload, dict) else []
    found = set()
    for node in nodes:
        node_type = node.get("@type") if isinstance(node, dict) else None
        if isinstance(node_type, list):
            found.update(node_type)
        elif node_type:
            found.add(node_type)
    return found


class ContentHubUpgradeTests(unittest.TestCase):
    def test_build_preserves_every_public_file_style_url(self):
        public_pages = [
            "index.html",
            "works.html",
            "learn.html",
            "notes.html",
            "about.html",
            *ARTICLE_PATHS,
        ]
        for relative_path in public_pages:
            self.assertTrue((DIST / relative_path).is_file(), relative_path)
        for relative_path in ARTICLE_PATHS:
            slug = Path(relative_path).stem
            self.assertFalse((DIST / "notes" / slug / "index.html").exists())

    def test_home_leads_with_creator_positioning_and_direct_follow_link(self):
        home = parse("index.html")
        source = (DIST / "index.html").read_text(encoding="utf-8")
        h1_text = re.search(r"<h1[^>]*>(.*?)</h1>", source, re.S)
        self.assertIsNotNone(h1_text)
        self.assertRegex(re.sub(r"<[^>]+>", "", h1_text.group(1)), r"AI|科技|方法")

        links = home.attrs_for("a")
        self.assertTrue(
            any(link.get("href") == DOUYIN_PROFILE for link in links),
            "首页关注入口应直接打开抖音主页",
        )
        self.assertNotIn('data-action="follow"', source)
        self.assertNotIn("assets/vendor/three.min.js", source)
        self.assertNotIn("assets/home-cover-three.js", source)

    def test_works_uses_series_filters_and_every_video_has_article_companion(self):
        works = parse("works.html")
        chips = {
            attrs.get("data-series-filter")
            for attrs in works.attrs_for("button")
            if attrs.get("data-series-filter")
        }
        self.assertEqual(chips, {"all", "agent", "observe", "aivideo"})

        cards = [
            attrs
            for tag, attrs in works.tags
            if tag == "article" and attrs.get("data-video-card")
        ]
        self.assertEqual(len(cards), 4)
        self.assertEqual(
            {card.get("data-series") for card in cards},
            {"agent", "observe", "aivideo"},
        )
        note_links = {
            attrs.get("href")
            for attrs in works.attrs_for("a")
            if "video-card__note-link" in attrs.get("class", "").split()
        }
        self.assertEqual(
            note_links,
            {BASE_PATH + path for path in VIDEO_ARTICLE_PATHS},
        )

    def test_knowledge_base_lists_seventeen_real_articles_without_search(self):
        notes = parse("notes.html")
        article_links = {
            attrs.get("href")
            for attrs in notes.attrs_for("a")
            if attrs.get("href") in {BASE_PATH + path for path in ARTICLE_PATHS}
        }
        self.assertEqual(article_links, {BASE_PATH + path for path in ARTICLE_PATHS})
        self.assertNotIn("pagefind", (DIST / "notes.html").read_text(encoding="utf-8").lower())
        for relative_path in ARTICLE_PATHS:
            self.assertTrue((DIST / relative_path).is_file(), relative_path + " does not exist")

    def test_learning_hub_orders_two_complete_tracks(self):
        self.assertTrue((DIST / "learn.html").is_file(), "learn.html does not exist")
        learning = parse("learn.html")
        sections = [
            attrs.get("data-learning-track")
            for tag, attrs in learning.tags
            if tag == "section" and attrs.get("data-learning-track")
        ]
        self.assertEqual(sections, ["vibe-coding", "ai-video"])

        steps = [
            (attrs.get("data-learning-track"), int(attrs["data-learning-step"]))
            for tag, attrs in learning.tags
            if tag == "li" and attrs.get("data-learning-step")
        ]
        self.assertEqual(
            steps,
            [
                (track, step)
                for track in ("vibe-coding", "ai-video")
                for step in range(1, 7)
            ],
        )

        links = {attrs.get("href") for attrs in learning.attrs_for("a")}
        for track in LEARNING_PATHS.values():
            for path in track.values():
                self.assertIn(BASE_PATH + path, links)

        current_links = [
            attrs
            for attrs in learning.attrs_for("a")
            if attrs.get("aria-current") == "page"
        ]
        self.assertEqual(len(current_links), 1)
        self.assertEqual(current_links[0].get("href"), BASE_PATH + "learn.html")

    def test_learning_hub_exposes_a_sidebar_outline_and_mobile_disclosure(self):
        learning = parse("learn.html")

        sidebars = [
            attrs
            for tag, attrs in learning.tags
            if tag == "aside" and "data-learning-sidebar" in attrs
        ]
        self.assertEqual(len(sidebars), 1)

        disclosures = [
            attrs
            for tag, attrs in learning.tags
            if tag == "details" and "data-learning-disclosure" in attrs
        ]
        self.assertEqual(len(disclosures), 1)
        self.assertIn("open", disclosures[0], "无 JavaScript 时桌面学习目录仍应可见")
        self.assertEqual(len(learning.attrs_for("summary")), 1)
        self.assertIn("学习目录", "".join(learning.text))

        outline_nav = [
            attrs
            for attrs in learning.attrs_for("nav")
            if attrs.get("aria-label") == "学习路线目录"
        ]
        self.assertEqual(len(outline_nav), 1)

        track_links = [
            attrs
            for attrs in learning.attrs_for("a")
            if attrs.get("data-learning-nav-track")
        ]
        self.assertEqual(
            [attrs.get("data-learning-nav-track") for attrs in track_links],
            ["vibe-coding", "ai-video"],
        )

        step_links = [
            attrs
            for attrs in learning.attrs_for("a")
            if attrs.get("data-learning-nav-step")
        ]
        expected_targets = [
            f"#{track}-step-{step}"
            for track in ("vibe-coding", "ai-video")
            for step in range(1, 7)
        ]
        self.assertEqual([attrs.get("href") for attrs in step_links], expected_targets)

        step_targets = {
            attrs.get("id")
            for tag, attrs in learning.tags
            if tag == "li" and attrs.get("data-learning-step")
        }
        self.assertEqual(step_targets, {target.removeprefix("#") for target in expected_targets})

    def test_learning_hub_links_each_track_to_a_curated_toolkit(self):
        learning = parse("learn.html")

        toolkits = [
            attrs.get("data-learning-toolkit")
            for tag, attrs in learning.tags
            if tag == "section" and attrs.get("data-learning-toolkit")
        ]
        self.assertEqual(toolkits, ["vibe-coding", "ai-video"])

        toolkit_links = [
            attrs
            for attrs in learning.attrs_for("a")
            if attrs.get("data-learning-tool")
        ]
        self.assertEqual(len(toolkit_links), 12)
        self.assertEqual(
            [attrs.get("data-learning-tool") for attrs in toolkit_links],
            [slug for track in ("vibe-coding", "ai-video") for slug in LEARNING_TOOLKITS[track]],
        )
        for attrs in toolkit_links:
            slug = attrs["data-learning-tool"]
            self.assertEqual(attrs.get("href"), f"{BASE_PATH}tools/{slug}.html")

        nav_links = [
            attrs
            for attrs in learning.attrs_for("a")
            if attrs.get("data-learning-nav-toolkit")
        ]
        self.assertEqual(
            [(attrs.get("data-learning-nav-toolkit"), attrs.get("href")) for attrs in nav_links],
            [
                ("vibe-coding", "#vibe-coding-tools"),
                ("ai-video", "#ai-video-tools"),
            ],
        )

    def test_primary_navigation_includes_learning_hub_everywhere(self):
        public_pages = [
            "index.html",
            "works.html",
            "learn.html",
            "notes.html",
            "about.html",
            *ARTICLE_PATHS,
        ]
        for relative_path in public_pages:
            self.assertTrue((DIST / relative_path).is_file(), relative_path)
            links = {attrs.get("href") for attrs in parse(relative_path).attrs_for("a")}
            self.assertIn(BASE_PATH + "learn.html", links, relative_path)

    def test_home_surfaces_both_learning_tracks(self):
        home = parse("index.html")
        entries = {
            attrs.get("data-learning-entry"): attrs.get("href")
            for attrs in home.attrs_for("a")
            if attrs.get("data-learning-entry")
        }
        self.assertEqual(
            entries,
            {
                "vibe-coding": BASE_PATH + "learn.html#vibe-coding",
                "ai-video": BASE_PATH + "learn.html#ai-video",
            },
        )

    def test_knowledge_base_filters_all_seventeen_articles_by_series(self):
        notes = parse("notes.html")
        roots = [
            attrs
            for tag, attrs in notes.tags
            if attrs.get("data-series-filter-root") is not None
        ]
        self.assertEqual(len(roots), 1)
        self.assertEqual(roots[0].get("data-filter-unit"), "文章")

        chips = {
            attrs.get("data-series-filter")
            for attrs in notes.attrs_for("button")
            if attrs.get("data-series-filter")
        }
        self.assertEqual(chips, {"all", "agent", "observe", "aivideo", "industry"})

        items = [
            attrs
            for tag, attrs in notes.tags
            if tag == "li" and attrs.get("data-filter-item") is not None
        ]
        self.assertEqual(len(items), 17)
        self.assertEqual(
            {item.get("data-series") for item in items},
            {"agent", "observe", "aivideo", "industry"},
        )

        live_counts = [attrs for attrs in notes.attrs_for("p") if attrs.get("data-filter-count") is not None]
        self.assertEqual(len(live_counts), 1)
        self.assertEqual(live_counts[0].get("aria-live"), "polite")
        self.assertTrue(
            any(attrs.get("data-filter-empty") is not None for _, attrs in notes.tags),
            "知识库需要可访问的空结果提示",
        )

    def test_public_pages_advertise_rss_and_use_structured_data(self):
        public_pages = [
            "index.html",
            "works.html",
            "learn.html",
            "notes.html",
            "about.html",
            *ARTICLE_PATHS,
        ]
        for relative_path in public_pages:
            page = parse(relative_path)
            feed_links = [
                attrs
                for attrs in page.attrs_for("link")
                if attrs.get("rel") == "alternate" and attrs.get("type") == "application/rss+xml"
            ]
            self.assertEqual(len(feed_links), 1, relative_path + " missing RSS discovery link")

        home_types = set().union(*(schema_types(item) for item in parse("index.html").json_ld))
        self.assertTrue({"WebSite", "Person"}.issubset(home_types))

        for relative_path in ARTICLE_PATHS:
            article_page = parse(relative_path)
            types = set().union(*(schema_types(item) for item in article_page.json_ld))
            self.assertTrue(
                {"BlogPosting", "BreadcrumbList"}.issubset(types),
                relative_path + " missing article schemas",
            )
            graphs = [
                node
                for payload in article_page.json_ld
                for node in payload.get("@graph", [payload])
                if isinstance(node, dict)
            ]
            posting = next(node for node in graphs if node.get("@type") == "BlogPosting")
            for field in (
                "headline",
                "description",
                "datePublished",
                "author",
                "mainEntityOfPage",
                "image",
            ):
                self.assertTrue(posting.get(field), relative_path + " missing " + field)
            self.assertTrue(posting["image"].startswith("https://"))

    def test_rss_and_sitemap_include_all_seventeen_articles(self):
        rss = ET.parse(DIST / "rss.xml").getroot()
        items = rss.findall("./channel/item")
        self.assertEqual(len(items), 17)
        rss_links = {item.findtext("link") for item in items}

        sitemap = ET.parse(DIST / "sitemap-0.xml").getroot()
        namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        sitemap_links = {node.text for node in sitemap.findall("sm:url/sm:loc", namespace)}

        for relative_path in ARTICLE_PATHS:
            url = "https://seraph125.github.io/personal-ip-website/" + relative_path
            self.assertIn(url, rss_links)
            self.assertIn(url, sitemap_links)
        self.assertIn(
            "https://seraph125.github.io/personal-ip-website/learn.html",
            sitemap_links,
        )

    def test_articles_have_markdown_reading_structure_and_exact_canonical(self):
        for relative_path in ARTICLE_PATHS:
            source = (DIST / relative_path).read_text(encoding="utf-8")
            page = parse(relative_path)
            self.assertEqual(len(page.attrs_for("h1")), 1, relative_path)
            self.assertTrue(
                any(attrs.get("id") == "article-page" for attrs in page.attrs_for("main")),
                relative_path,
            )
            self.assertTrue(
                any("article__surface" in attrs.get("class", "").split() for attrs in page.attrs_for("div")),
                relative_path,
            )
            self.assertTrue(
                any(
                    attrs.get("aria-label") == "本文目录"
                    for attrs in page.attrs_for("nav")
                ),
                relative_path,
            )
            h2_ids = {attrs.get("id") for attrs in page.attrs_for("h2") if attrs.get("id")}
            self.assertGreaterEqual(len(h2_ids), 2, relative_path)
            heading_ids = h2_ids | {
                attrs.get("id") for attrs in page.attrs_for("h3") if attrs.get("id")
            }
            toc_source = re.search(
                r'<nav class="article__toc".*?</nav>', source, re.S
            )
            self.assertIsNotNone(toc_source, relative_path)
            toc_fragments = set(
                re.findall(r'<a href="#([^"]+)">', toc_source.group(0))
            )
            self.assertTrue(toc_fragments.issubset(heading_ids), relative_path)

            canonical = next(
                attrs.get("href")
                for attrs in page.attrs_for("link")
                if attrs.get("rel") == "canonical"
            )
            self.assertEqual(
                canonical,
                "https://seraph125.github.io/personal-ip-website/" + relative_path,
            )

        self.assertIn("<table>", (DIST / "notes/codex-5-levels.html").read_text(encoding="utf-8"))
        self.assertIn("<table>", (DIST / "notes/ai-refund-fraud-report.html").read_text(encoding="utf-8"))

    def test_video_cta_only_appears_on_the_four_video_articles(self):
        for relative_path in ARTICLE_PATHS:
            links = parse(relative_path).attrs_for("a")
            video_links = [
                attrs
                for attrs in links
                if "article__video" in attrs.get("class", "").split()
            ]
            expected = 1 if relative_path in VIDEO_ARTICLE_PATHS else 0
            self.assertEqual(len(video_links), expected, relative_path)

    def test_all_built_internal_links_and_assets_exist(self):
        public_pages = [
            "index.html",
            "works.html",
            "learn.html",
            "notes.html",
            "about.html",
            *ARTICLE_PATHS,
        ]
        for relative_path in public_pages:
            page = parse(relative_path)
            references = []
            for tag, attrs in page.tags:
                attr = "src" if tag in {"img", "script"} else "href"
                if tag in {"a", "link", "img", "script"} and attrs.get(attr):
                    references.append(attrs[attr])

            for reference in references:
                if not reference.startswith(BASE_PATH):
                    continue
                clean = reference.split("#", 1)[0].split("?", 1)[0]
                local = clean.removeprefix(BASE_PATH) or "index.html"
                self.assertTrue(
                    (DIST / local).is_file(),
                    f"{relative_path} -> {reference} missing",
                )


if __name__ == "__main__":
    unittest.main()
