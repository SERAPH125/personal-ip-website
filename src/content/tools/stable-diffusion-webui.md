---
title: "Stable Diffusion WebUI 安装与入门：跑通本地生成"
toolName: "Stable Diffusion WebUI"
description: "从官方仓库安装 AUTOMATIC1111 Stable Diffusion WebUI，配置模型并生成第一张本地图片。"
audience: "希望学习经典 Stable Diffusion 本地界面、能够管理 Python 环境、模型与显卡资源的进阶用户。"
setupSummary: "Windows 可使用官方仓库提供的批处理流程；macOS 与 Linux 按 Wiki 操作，模型下载和环境创建耗时较长。"
privacySummary: "基础生成在本机运行，但 Git、Python 包、模型和扩展下载会联网；第三方扩展可执行代码。"
origin: international
category: image-model
toolType: workflow
difficulty: intermediate
accessTypes: [local-service]
platforms: [windows, macos, linux]
pricing: free
openSource: true
license: "AGPL-3.0"
officialUrl: "https://github.com/AUTOMATIC1111/stable-diffusion-webui"
downloadUrl: "https://github.com/AUTOMATIC1111/stable-diffusion-webui"
repositoryUrl: "https://github.com/AUTOMATIC1111/stable-diffusion-webui"
versionChecked: "AUTOMATIC1111 v1.10.1 release and master README · checked 2026-08-26"
verifiedAt: 2026-08-26
cover: "/assets/tools/stable-diffusion-webui/cover.svg"
coverAlt: "Stable Diffusion WebUI 电脑端安装和首次使用流程示意图"
sequence: 13
draft: false
---

## 快速判断

Stable Diffusion WebUI（AUTOMATIC1111）是经典的本地图像生成界面，通过本机服务在浏览器中操作。它不是普通在线网页：程序、模型和推理环境都安装在你的电脑上。

它的扩展生态很大，也意味着供应链风险更高。首次安装只使用官方仓库和一个可信模型，不添加整合包、未知扩展或来源不明的启动参数。

## 安装前检查

1. Windows 自动安装流程当前要求 Git 与 Python 3.10.6；Linux/macOS 应按官方对应页面选择版本，不机械套用 Windows 版本。
2. 确认显卡驱动和可用显存。
3. 准备至少一个来源可信的模型。
4. 给代码、模型和输出预留空间。

## 图解安装

![Stable Diffusion WebUI 从检查到首次使用的六步安装流程](/personal-ip-website/assets/tools/stable-diffusion-webui/install-flow.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">官方安装资料</a> 整理 · 核验于 2026-08-26</p>

Windows 10/11 用户可先安装 Git 与 Python 3.10.6，并勾选“Add Python to PATH”，然后在准备好的目录运行：

```bash
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```

进入克隆得到的目录，用普通用户身份双击 `webui-user.bat`。不要以管理员身份启动，也不要从转载站下载所谓整合包。

Linux 用户可按官方 README 安装发行版依赖，克隆仓库后运行 `webui.sh`；macOS 使用官方 Apple Silicon 或 Intel 指南。不同系统的依赖并不相同。

![Stable Diffusion WebUI 安装时需要确认的三个关键点](/personal-ip-website/assets/tools/stable-diffusion-webui/setup-screen.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">官方产品或项目说明</a> 整理 · 核验于 2026-08-26</p>

第一次启动会安装依赖，耐心等待并保留终端日志。看到本地地址后再在浏览器打开，不要把监听地址改成公网可访问。

![Stable Diffusion WebUI 第一次使用的目标与验收标准](/personal-ip-website/assets/tools/stable-diffusion-webui/first-use.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">官方使用资料</a> 整理 · 核验于 2026-08-26</p>

选择一个基础模型，使用默认采样设置和较小尺寸生成单张图片。只有稳定成功后，再学习 LoRA、ControlNet 和扩展。

## 第一次使用

1. 从官方仓库安装并启动。
2. 确认终端没有致命错误。
3. 在模型列表选择基础模型。
4. 以默认参数生成单张图片。
5. 核对 outputs 目录。

可以从这个低风险任务开始：

> minimal blue geometric poster, soft studio lighting, clean background, no text, no logo

第一次验收只看三件事：本地页面可以打开、终端无致命错误、输出文件已写入本机目录。

## 常见问题

**Python 版本不兼容**：按仓库当前文档安装指定版本，不在同一环境反复混装多个 Python。

**模型列表为空**：确认模型文件完整且位于正确 checkpoints 目录，再刷新模型列表。

**CUDA 或显存错误**：更新驱动、降低分辨率与批量，并确认启动时实际使用了正确 GPU。

**扩展导致启动失败**：先禁用最近添加的扩展，用纯净官方环境复现后再逐个恢复。

## 更新与卸载

更新前提交或备份自己的配置、扩展清单和工作流。使用 Git 更新后先以禁用第三方扩展的状态启动。

程序目录、Python 环境、模型库和输出可能分散。按目录逐项确认后删除，不要误删其他工具共用的模型。

## 费用、隐私与开源信息

- **费用**：软件免费；硬件、电力、下载流量与存储是主要成本，模型可能另有商用限制。
- **隐私**：默认本地推理不代表完全离线，依赖、扩展和模型下载会联网；不要把本地端口直接暴露到公网。请复查官方 [隐私或安全说明](https://github.com/AUTOMATIC1111/stable-diffusion-webui/security)。
- **开源状态**：官方仓库采用 AGPL-3.0；扩展与模型各自有许可证，本指南不复用项目代码。
- **安全边界**：避免未知整合包和要求关闭防护的软件。扩展可执行代码，安装前查看仓库、维护状态和权限。

## 官方资料与核验日期

- [Stable Diffusion WebUI 官方仓库](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [Windows 与 Linux 官方安装步骤](https://github.com/AUTOMATIC1111/stable-diffusion-webui#installation-and-running)
- [官方安全页面](https://github.com/AUTOMATIC1111/stable-diffusion-webui/security)

本文最后核验：**2026-08-26**。安装入口、系统要求、模型能力、价格与隐私规则会变化，实际操作时请再次查看官方页面。
