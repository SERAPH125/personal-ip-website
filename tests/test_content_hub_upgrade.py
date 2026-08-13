import json
import re
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
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
]


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
    parser.feed((ROOT / relative_path).read_text(encoding="utf-8"))
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
    def test_home_leads_with_creator_positioning_and_direct_follow_link(self):
        home = parse("index.html")
        source = (ROOT / "index.html").read_text(encoding="utf-8")
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
        self.assertEqual(note_links, {path for path in ARTICLE_PATHS if "refund" not in path})

    def test_knowledge_base_lists_five_real_articles_without_premature_search(self):
        notes = parse("notes.html")
        article_links = {
            attrs.get("href")
            for attrs in notes.attrs_for("a")
            if attrs.get("href") in ARTICLE_PATHS
        }
        self.assertEqual(article_links, set(ARTICLE_PATHS))
        self.assertNotIn("pagefind", (ROOT / "notes.html").read_text(encoding="utf-8").lower())
        for relative_path in ARTICLE_PATHS:
            self.assertTrue((ROOT / relative_path).is_file(), relative_path + " does not exist")

    def test_public_pages_advertise_rss_and_use_structured_data(self):
        public_pages = ["index.html", "works.html", "notes.html", "about.html", *ARTICLE_PATHS]
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
            types = set().union(*(schema_types(item) for item in parse(relative_path).json_ld))
            self.assertTrue(
                {"BlogPosting", "BreadcrumbList"}.issubset(types),
                relative_path + " missing article schemas",
            )

    def test_rss_and_sitemap_include_all_five_articles(self):
        rss = ET.parse(ROOT / "rss.xml").getroot()
        items = rss.findall("./channel/item")
        self.assertEqual(len(items), 5)
        rss_links = {item.findtext("link") for item in items}

        sitemap = ET.parse(ROOT / "sitemap.xml").getroot()
        namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        sitemap_links = {node.text for node in sitemap.findall("sm:url/sm:loc", namespace)}

        for relative_path in ARTICLE_PATHS:
            url = "https://seraph125.github.io/personal-ip-website/" + relative_path
            self.assertIn(url, rss_links)
            self.assertIn(url, sitemap_links)


if __name__ == "__main__":
    unittest.main()
