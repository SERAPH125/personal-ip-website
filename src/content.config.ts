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
    series: z.enum(["agent", "observe", "aivideo", "industry"]),
    sequence: z.number().int().positive(),
    cover: z.string(),
    coverAlt: z.string(),
    featured: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
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

export const collections = { notes };
