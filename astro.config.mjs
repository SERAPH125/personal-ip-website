import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://seraph125.github.io",
  base: "/personal-ip-website",
  output: "static",
  trailingSlash: "never",
  build: {
    format: "file",
  },
  integrations: [
    sitemap({
      serialize(item) {
        const url = new URL(item.url);
        const basePath = "/personal-ip-website";
        const normalizedPath = url.pathname.replace(/\/+$/, "");
        if (normalizedPath !== basePath && !url.pathname.endsWith(".html")) {
          url.pathname += ".html";
        }
        return { ...item, url: url.toString() };
      },
    }),
  ],
  markdown: {
    shikiConfig: {
      theme: "github-light",
    },
  },
});
