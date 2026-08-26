import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const notes = defineCollection({
  loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/notes" }),
  schema: z.object({
    title: z.string(),
    cardTitle: z.string().optional(),
    description: z.string(),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    sourcesCheckedAt: z.coerce.date().optional(),
    series: z.enum(["agent", "observe", "aivideo", "industry"]),
    sequence: z.number().int().positive(),
    cover: z.string(),
    coverAlt: z.string(),
    featured: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    learning: z
      .object({
        track: z.enum(["vibe-coding", "ai-video"]),
        step: z.number().int().min(1).max(6),
      })
      .optional(),
    video: z
      .object({
        platform: z.enum(["douyin"]),
        url: z.url(),
        title: z.string(),
        hook: z.string(),
      })
      .optional(),
  }),
});

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
      category: z.enum(["language-model", "image-model", "ai-coding", "video-model"]),
      accessTypes: z.array(z.enum(["cli", "desktop", "local-service", "web"])).min(1),
      platforms: z
        .array(z.enum(["windows", "macos", "linux", "web", "android", "ios"]))
        .min(1),
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
