---
title: "Krita AI Diffusion 安装与入门：把本地生成接进绘画软件"
toolName: "Krita AI Diffusion"
description: "在 Krita 安装 AI Diffusion 插件，选择本地后端并完成第一次生成、重绘和权限检查。"
audience: "已经使用或愿意学习 Krita，希望把扩散模型用于绘画、局部重绘和扩图的创作者。"
setupSummary: "先安装 Krita 5.2 或更高版本，再导入插件 ZIP；本地托管后端还需下载模型并预留显存和磁盘。"
privacySummary: "本地托管模式可在设备处理图像；在线服务和自定义远程 ComfyUI 会改变数据去向。"
origin: international
category: image-model
toolType: plugin
difficulty: intermediate
accessTypes: [desktop, local-service]
platforms: [windows, macos, linux]
pricing: free
openSource: true
license: "GPL-3.0"
officialUrl: "https://github.com/Acly/krita-ai-diffusion"
downloadUrl: "https://github.com/Acly/krita-ai-diffusion/releases"
repositoryUrl: "https://github.com/Acly/krita-ai-diffusion"
versionChecked: "Krita AI Diffusion latest stable release"
verifiedAt: 2026-08-26
cover: "/assets/tools/krita-ai-diffusion/cover.svg"
coverAlt: "Krita AI Diffusion 电脑端安装和首次使用流程示意图"
sequence: 14
draft: false
---

## 快速判断

Krita AI Diffusion 把生成、扩图和局部重绘带进 Krita 的图层工作流。它适合想在绘画软件中反复修改，而不是只生成一张成品的用户。

插件可以连接本地托管、在线服务或自定义 ComfyUI。三种模式的数据路径不同；本篇优先讲本地托管，并明确硬件不足时不要假装离线。

## 安装前检查

1. 安装 Krita 5.2 或更高版本。
2. 从官方 Releases 下载插件 ZIP。
3. 更新显卡驱动并检查显存。
4. 为模型准备至少数十 GB 弹性空间。

## 图解安装

![Krita AI Diffusion 从检查到首次使用的六步安装流程](/personal-ip-website/assets/tools/krita-ai-diffusion/install-flow.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://github.com/Acly/krita-ai-diffusion/releases">官方安装资料</a> 整理 · 核验于 2026-08-26</p>

在 Krita 的工具菜单中从文件导入 Python 插件，选择官方 Release ZIP，而不是 GitHub 自动生成的源码压缩包。

![Krita AI Diffusion 安装时需要确认的三个关键点](/personal-ip-website/assets/tools/krita-ai-diffusion/setup-screen.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://github.com/Acly/krita-ai-diffusion">官方产品或项目说明</a> 整理 · 核验于 2026-08-26</p>

重启 Krita 后打开 AI Image Generation Docker。选择 Local Managed Server 时，安装器会准备后端和模型；先选最小工作负载。

![Krita AI Diffusion 第一次使用的目标与验收标准](/personal-ip-website/assets/tools/krita-ai-diffusion/first-use.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://github.com/Acly/krita-ai-diffusion">官方使用资料</a> 整理 · 核验于 2026-08-26</p>

创建低分辨率空白文档，用简单提示词生成。之后画一个小选区测试局部重绘，确认蒙版和图层行为。

## 第一次使用

1. 安装并重启 Krita。
2. 打开 AI Image Generation Docker。
3. 配置本地托管后端。
4. 在小画布生成一次。
5. 用选区测试局部重绘。

可以从这个低风险任务开始：

> soft blue ceramic cup on a clean desk, simple illustration, no text

这次插件验收只看三项：Docker 状态正常、本地后端连接成功、生成结果进入新的可编辑图层。

## 常见问题

**插件呈灰色**：确认使用官方 Release ZIP、Krita 版本和正确导入入口，然后重启应用。

**本地后端安装失败**：核对 GPU、驱动、磁盘和安装路径，查看插件日志中的具体包或模型错误。

**模型下载占用过大**：先选择最小工作负载，了解每个模型用途后再补充。

**生成结果不进图层**：检查当前文档、选区、图层锁定和 Docker 状态。

## 更新与卸载

下载新的官方 Release ZIP 按安装流程覆盖插件；保留独立的服务器和模型目录，升级后先验证连接。

删除插件目录前确认服务器、模型和用户数据位置。若本地后端不再使用，再单独清理其目录。

## 费用、隐私与开源信息

- **费用**：插件与本地软件免费；本地硬件和电力有成本，在线后端可能按套餐收费。
- **隐私**：本地托管、在线服务和自定义服务器的数据边界不同。每次切换后端都应重新确认素材发往哪里。请复查官方 [隐私或安全说明](https://github.com/Acly/krita-ai-diffusion/security)。
- **开源状态**：插件采用 GPL-3.0 且维护活跃；底层 Krita、ComfyUI、模型与插件扩展各有许可证。
- **安全边界**：只安装官方 Release；模型和自定义节点也可能包含风险，避免未知整合包。

## 官方资料与核验日期

- [插件官方仓库](https://github.com/Acly/krita-ai-diffusion)
- [官方安装说明](https://github.com/Acly/krita-ai-diffusion/blob/main/docs/src/content/docs/installation.mdx)
- [官方安全页面](https://github.com/Acly/krita-ai-diffusion/security)

本文最后核验：**2026-08-26**。安装入口、系统要求、模型能力、价格与隐私规则会变化，实际操作时请再次查看官方页面。
