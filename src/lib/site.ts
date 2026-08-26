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

export const toolCategoryMeta = {
  "language-model": { label: "语言模型" },
  "image-model": { label: "图片模型" },
  "ai-coding": { label: "AI 编程" },
  "video-model": { label: "视频模型" },
} as const;

export const toolOriginMeta = {
  international: { label: "国际" },
  china: { label: "国内" },
} as const;

export const toolAccessMeta = {
  cli: { label: "命令行" },
  desktop: { label: "桌面应用" },
  "local-service": { label: "本地服务" },
  web: { label: "网页" },
} as const;

export const toolPlatformMeta = {
  windows: { label: "Windows" },
  macos: { label: "macOS" },
  linux: { label: "Linux" },
  web: { label: "网页" },
  android: { label: "Android" },
  ios: { label: "iOS" },
} as const;

export const toolPricingMeta = {
  free: { label: "免费" },
  freemium: { label: "免费增值" },
  paid: { label: "付费" },
  "usage-based": { label: "按量计费" },
} as const;

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

export function toolPath(slug: string) {
  return withBase(`tools/${slug}.html`);
}

export function toolUrl(slug: string) {
  return absoluteUrl(`tools/${slug}.html`);
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
