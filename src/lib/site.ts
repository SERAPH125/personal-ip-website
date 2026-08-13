export const SITE_ORIGIN = "https://seraph125.github.io";
export const SITE_NAME = "南吴 NANWU";
export const DOUYIN_PROFILE =
  "https://www.douyin.com/user/MS4wLjABAAAAwwu7aqbhsXBribQpl5JPNTqXz-9ZRfmL2uZ8c70_l5JnwQsaYZJzGpk3ERvhzrA8";

export const seriesMeta = {
  agent: { label: "Agent 实战", description: "把工具变成生产系统" },
  observe: { label: "模型观察", description: "新模型与能力边界" },
  aivideo: { label: "AI 视频", description: "分镜、生成与提示词" },
  industry: { label: "行业观察", description: "现象、证据与应对" },
} as const;

export type SeriesKey = keyof typeof seriesMeta;

export function withBase(path = "") {
  const base = `${import.meta.env.BASE_URL.replace(/\/+$/, "")}/`;
  return `${base}${path.replace(/^\/+/, "")}`;
}

export function absoluteUrl(path = "") {
  return new URL(withBase(path), SITE_ORIGIN).toString();
}

export function articlePath(slug: string) {
  return withBase(`notes/${slug}.html`);
}

export function articleUrl(slug: string) {
  return absoluteUrl(`notes/${slug}.html`);
}

export function formatDate(date: Date) {
  return new Intl.DateTimeFormat("zh-CN", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  })
    .format(date)
    .replaceAll("/", "-");
}
