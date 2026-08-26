---
title: "InvokeAI 安装与入门：建立本地图像生成工作区"
toolName: "InvokeAI"
description: "安装开源 InvokeAI，完成硬件检查、模型准备、首张图片生成和本地目录管理。"
audience: "希望用较完整的本地创作界面管理扩散模型、画布和生成记录，并愿意准备显卡与磁盘空间的创作者。"
setupSummary: "安装器本身较快，模型下载会占用更多时间和空间；首次运行前先核对 GPU、驱动和安装目录。"
privacySummary: "本地生成可让素材留在设备上，但模型下载、更新和可选服务仍可能联网；模型许可证需单独检查。"
origin: international
category: image-model
toolType: workflow
difficulty: intermediate
accessTypes: [desktop, local-service]
platforms: [windows, macos, linux]
pricing: free
openSource: true
license: "Apache-2.0"
officialUrl: "https://invoke.ai/start-here/installation/"
downloadUrl: "https://github.com/invoke-ai/launcher/releases/latest"
repositoryUrl: "https://github.com/invoke-ai/InvokeAI"
versionChecked: "Invoke Launcher stable release channel"
verifiedAt: 2026-08-26
cover: "/assets/tools/invokeai/cover.svg"
coverAlt: "InvokeAI 电脑端安装和首次使用流程示意图"
sequence: 12
draft: false
---

## 快速判断

InvokeAI 是面向本地扩散模型创作的开源应用，提供生成、画布、图库和模型管理等界面。它比纯命令行友好，但仍需要理解显存、磁盘和模型来源。

软件开源不等于模型和输出自动拥有相同权利。每个模型、LoRA、素材与扩展都可能有独立许可证；开始商用前要分别核对。

## 安装前检查

1. 记录显卡型号和可用显存。
2. 预留安装、模型与输出空间。
3. 从 InvokeAI 安装页进入 Invoke Launcher，并从独立的 Launcher Releases 下载对应平台安装包。
4. 决定一个固定的模型目录。

## 图解安装

![InvokeAI 从检查到首次使用的六步安装流程](/personal-ip-website/assets/tools/invokeai/install-flow.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://invoke.ai/start-here/installation/">官方安装资料</a> 整理 · 核验于 2026-08-26</p>

从官方安装页下载 Invoke Launcher。Launcher 支持 Windows、Apple Silicon macOS 与 Linux，会管理所需 Python、安装、更新和启动；不要把主项目 Releases 误当成桌面安装器。首次只安装一个基础模型，最容易排错。

![InvokeAI 安装时需要确认的三个关键点](/personal-ip-website/assets/tools/invokeai/setup-screen.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://github.com/invoke-ai/launcher/releases/latest">Invoke Launcher 官方发布页</a> 整理 · 核验于 2026-08-26</p>

安装目录、模型目录和输出目录尽量分清。空间不足时先迁移模型库，不要直接删除不认识的缓存或环境文件。

![InvokeAI 第一次使用的目标与验收标准](/personal-ip-website/assets/tools/invokeai/first-use.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://invoke.ai/start-here/installation/">官方使用资料</a> 整理 · 核验于 2026-08-26</p>

新建低分辨率任务，保持采样与批量参数为默认值，只修改提示词。先确认能稳定生成和保存，再进入画布、ControlNet 或批处理。

## 第一次使用

1. 启动 InvokeAI 并打开本地界面。
2. 确认基础模型可选。
3. 使用较小输出尺寸。
4. 提交一次单图生成。
5. 在图库与输出目录核对结果。

可以从这个低风险任务开始：

> 一张简洁的蓝白色工作台插画，柔和光线，主体居中，无文字，无品牌标识。

第一次验收只看三件事：任务无报错完成、图片进入图库、模型与输出目录都能找到。

## 常见问题

**显存不足**：降低分辨率和批量，关闭占用 GPU 的程序，并选择更轻量的模型。

**模型未显示**：核对模型格式、目录和导入日志，不反复复制同一大文件。

**服务启动失败**：查看安装日志与端口占用，先排除驱动、权限和磁盘空间。

**输出风格异常**：确认实际选中的模型、VAE 和提示词，不同时更改大量参数。

## 更新与卸载

更新前备份数据库、配置、工作流和模型位置记录。升级后先用原来的基础任务验证，再恢复扩展工作流。

卸载应用前区分程序、模型和个人输出目录。模型体积很大，但删除前仍应确认没有被其他本地工具共用。

## 费用、隐私与开源信息

- **费用**：InvokeAI 软件可免费使用；硬件、电力、模型存储和可能接入的云资源会产生实际成本。
- **隐私**：本地生成可以减少素材上传，但下载安装、遥测设置和外部模型源可能联网；敏感素材仍应放在受控目录。请复查官方 [隐私或安全说明](https://github.com/invoke-ai/InvokeAI/security)。
- **开源状态**：官方仓库采用 Apache-2.0 且保持活跃维护；本指南只引用其安装设计，不复制代码或引入依赖。
- **安全边界**：仅使用官方仓库与文档；模型文件和扩展也可能带来供应链风险，下载后核对来源和许可证。

## 官方资料与核验日期

- [InvokeAI 安装文档](https://invoke.ai/start-here/installation/)
- [Invoke Launcher 官方发布页](https://github.com/invoke-ai/launcher/releases/latest)
- [InvokeAI 官方仓库](https://github.com/invoke-ai/InvokeAI)
- [InvokeAI 安全策略](https://github.com/invoke-ai/InvokeAI/security)

本文最后核验：**2026-08-26**。安装入口、系统要求、模型能力、价格与隐私规则会变化，实际操作时请再次查看官方页面。
