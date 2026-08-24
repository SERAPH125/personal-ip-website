import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUGS = {
    "codex-5-levels",
    "fable-5-safety-lock",
    "ai-storyboard-perspective",
    "seedance-2-workflows",
    "ai-refund-fraud-report",
}
REQUIRED_FRONTMATTER = {
    "title",
    "description",
    "publishedAt",
    "series",
    "cover",
}


def frontmatter_keys(markdown: str) -> set[str]:
    match = re.match(r"^---\n(?P<body>.*?)\n---\n", markdown, re.S)
    if not match:
        return set()
    return {
        line.split(":", 1)[0].strip()
        for line in match.group("body").splitlines()
        if line and not line.startswith((" ", "\t", "#")) and ":" in line
    }


class AstroMigrationContractTests(unittest.TestCase):
    def test_npm_scripts_are_cross_platform_on_windows(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        scripts = package["scripts"]

        for name in ("dev", "build", "check", "preview"):
            self.assertTrue(
                scripts[name].startswith("cross-env ASTRO_TELEMETRY_DISABLED=1 "),
                f"{name} 必须通过 cross-env 设置环境变量",
            )
        self.assertIn("python -m unittest", scripts["test"])
        self.assertNotIn("python3 ", scripts["test"])
        self.assertIn("cross-env", package.get("devDependencies", {}))

    def test_project_builds_with_astro_and_keeps_file_style_urls(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertIn("astro", package.get("dependencies", {}))
        self.assertTrue(package["scripts"]["build"].endswith("astro build"))

        config = (ROOT / "astro.config.mjs").read_text(encoding="utf-8")
        self.assertIn("build:", config)
        self.assertRegex(config, r"format:\s*['\"]file['\"]")
        self.assertIn("base:", config)
        self.assertIn("site:", config)

    def test_five_articles_are_markdown_content_entries(self):
        content_dir = ROOT / "src" / "content" / "notes"
        markdown_files = {path.stem: path for path in content_dir.glob("*.md")}
        self.assertEqual(set(markdown_files), SLUGS)

        for slug, path in markdown_files.items():
            markdown = path.read_text(encoding="utf-8")
            self.assertTrue(
                REQUIRED_FRONTMATTER.issubset(frontmatter_keys(markdown)),
                f"{slug} 缺少必填 frontmatter",
            )
            self.assertGreaterEqual(markdown.count("\n## "), 2, f"{slug} 正文层级不足")

    def test_content_collection_validates_article_metadata(self):
        config = (ROOT / "src" / "content.config.ts").read_text(encoding="utf-8")
        self.assertIn("defineCollection", config)
        self.assertIn("glob", config)
        for field in REQUIRED_FRONTMATTER:
            self.assertRegex(config, rf"\b{field}\b", f"schema 缺少 {field}")

    def test_one_dynamic_route_renders_all_articles_with_shared_reading_ui(self):
        route = ROOT / "src" / "pages" / "notes" / "[...slug].astro"
        source = route.read_text(encoding="utf-8")
        self.assertIn("getStaticPaths", source)
        self.assertIn("render", source)
        self.assertIn("ArticleLayout", source)

        layout = (ROOT / "src" / "layouts" / "ArticleLayout.astro").read_text(
            encoding="utf-8"
        )
        self.assertIn("article__surface", layout)
        self.assertIn("article__toc", layout)
        self.assertIn('"@type": "BlogPosting"', layout)
        self.assertIn('"@type": "BreadcrumbList"', layout)
        base_layout = (ROOT / "src" / "layouts" / "BaseLayout.astro").read_text(
            encoding="utf-8"
        )
        self.assertIn("application/ld+json", base_layout)

    def test_authored_html_articles_are_removed_after_migration(self):
        legacy_dir = ROOT / "notes"
        authored_articles = list(legacy_dir.glob("*.html")) if legacy_dir.exists() else []
        self.assertEqual(authored_articles, [])


if __name__ == "__main__":
    unittest.main()
