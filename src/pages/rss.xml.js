import rss from "@astrojs/rss";
import { getCollection } from "astro:content";

export async function GET(context) {
  const notes = (await getCollection("notes", ({ data }) => !data.draft)).sort(
    (a, b) => b.data.publishedAt.valueOf() - a.data.publishedAt.valueOf(),
  );
  const base = `${import.meta.env.BASE_URL.replace(/\/+$/, "")}/`;
  const site = new URL(base, context.site);

  return rss({
    title: "南吴 NANWU 知识库",
    description: "Agent 实战、模型观察、AI 视频与行业观察的可复用文字经验。",
    site,
    trailingSlash: false,
    items: notes.map((entry) => ({
      title: entry.data.title,
      description: entry.data.description,
      pubDate: entry.data.publishedAt,
      link: `notes/${entry.id}.html`,
    })),
    customData: "<language>zh-CN</language>",
  });
}
