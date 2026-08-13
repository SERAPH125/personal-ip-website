from html.parser import HTMLParser
from pathlib import Path
import unittest


class RelatedResourceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchor_stack = []
        self.div_stack = []
        self.hero_copy_depth = 0
        self.related_links = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = set(attributes.get("class", "").split())

        if tag == "div":
            is_hero_copy = "hero-copy" in classes
            self.div_stack.append(is_hero_copy)
            if is_hero_copy:
                self.hero_copy_depth += 1

        if tag != "a":
            return

        for related_index in self.anchor_stack:
            if related_index is not None:
                self.related_links[related_index]["contains_nested"] = True

        related_index = None
        if "related-resource" in classes:
            related_index = len(self.related_links)
            self.related_links.append(
                {
                    "href": attributes.get("href"),
                    "in_hero_copy": self.hero_copy_depth > 0,
                    "nested": bool(self.anchor_stack),
                    "contains_nested": False,
                    "text": [],
                }
            )
        self.anchor_stack.append(related_index)

    def handle_data(self, data):
        for related_index in self.anchor_stack:
            if related_index is not None:
                self.related_links[related_index]["text"].append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.anchor_stack:
            self.anchor_stack.pop()
        if tag == "div" and self.div_stack:
            if self.div_stack.pop():
                self.hero_copy_depth -= 1


class HomeRelatedResourceTest(unittest.TestCase):
    def test_featured_video_exposes_an_independent_knowledge_link(self):
        index_path = Path(__file__).resolve().parents[1] / "dist" / "index.html"
        parser = RelatedResourceParser()
        parser.feed(index_path.read_text(encoding="utf-8"))

        featured_links = [
            link for link in parser.related_links if link["in_hero_copy"]
        ]
        self.assertEqual(len(featured_links), 1)
        link = featured_links[0]
        self.assertFalse(link["nested"])
        self.assertFalse(link["contains_nested"])
        self.assertEqual(
            link["href"],
            "/personal-ip-website/notes/codex-5-levels.html",
        )
        link_text = " ".join("".join(link["text"]).split())
        self.assertIn("知识文档", link_text)
        self.assertIn("Codex 的 5 级用法", link_text)


if __name__ == "__main__":
    unittest.main()
