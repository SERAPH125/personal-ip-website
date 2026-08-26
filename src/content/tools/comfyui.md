---
title: "ComfyUI 安装与入门：跑通第一个图像生成工作流"
toolName: "ComfyUI"
description: "用节点工作流理解 AI 图像生成，从桌面版安装、模型管理到保存首张图片。"
audience: "想学习可视化节点工作流、精细控制 AI 图像生成，并愿意管理模型与显卡资源的创作者。"
setupSummary: "Windows 新手优先使用官方 Desktop；安装程序较快，但模型下载和首次环境准备可能需要更久。"
privacySummary: "基础生成可在本机完成，但模型下载、模板、扩展节点和云端功能可能联网；素材与模型许可证需单独核对。"
origin: international
category: image-model
accessTypes: [desktop, local-service]
platforms: [windows, macos, linux]
pricing: free
openSource: true
license: "GPL-3.0"
officialUrl: "https://docs.comfy.org/installation/desktop/windows"
downloadUrl: "https://www.comfy.org/download"
repositoryUrl: "https://github.com/Comfy-Org/ComfyUI"
versionChecked: "ComfyUI Desktop stable channel"
verifiedAt: 2026-08-26
cover: "/assets/tools/comfyui/cover.svg"
coverAlt: "ComfyUI 模型、采样器和保存图像节点连接示意图"
sequence: 4
draft: false
---

## 快速判断

ComfyUI 适合想理解“模型、提示词、采样器、图像输出如何连接”的 AI 图像创作者。它通过节点和连线描述生成流程，可复用、可拆解，也比一键式产品更需要学习成本。

如果你只想偶尔输入一句话生成图片，网页工具通常更省事；如果你希望复现工作流、控制参数、连接不同模型与后处理，ComfyUI 更值得投入。首次安装先跑通官方基础模板，不要一次装大量第三方节点。

## 安装前检查

1. Windows Desktop 当前文档要求 Windows 10 或更高版本，并支持 x64、ARM64；官方建议使用独立显卡。
2. 官方文档提示每个安装环境至少需要约 4.85 GB，实际还要给模型和输出图片预留更多空间。
3. 更新显卡驱动，并记录显卡型号、显存与系统剩余空间，方便排错。
4. 模型、LoRA、工作流和自定义节点来自不同作者，各自有许可证和安全风险。

macOS 与 Linux 用户应进入官方安装文档选择对应方案。本篇的图形化步骤以 Windows Desktop 为主，避免把不同平台命令混在一起。

## 图解安装

![ComfyUI 从硬件检查到保存首张图片的六步流程图](/personal-ip-website/assets/tools/comfyui/install-flow.svg)

打开官方 Windows Desktop 文档，下载当前安装程序。安装时优先选择剩余空间充足的磁盘，并给模型目录留出增长空间。

![ComfyUI 官方 Windows Desktop 安装文档和系统要求](/personal-ip-website/assets/tools/comfyui/step-01.webp)

<p class="tool-image-source">图片来源：<a href="https://docs.comfy.org/installation/desktop/windows">ComfyUI 官方 Windows Desktop 文档</a> · 页面截取于 2026-08-26</p>

首次启动可能需要准备运行环境。保持网络稳定，出现错误时记录页面提示和日志，不要同时改驱动、Python、模型路径和多个设置。

![ComfyUI 官方开源仓库及 GPL-3.0 许可证页面](/personal-ip-website/assets/tools/comfyui/step-02.webp)

<p class="tool-image-source">图片来源：<a href="https://github.com/Comfy-Org/ComfyUI">ComfyUI 官方仓库</a> · 页面截取于 2026-08-26</p>

官方仓库用于核对源码、许可证、Issue 和发布动态。自定义节点不是自动等同于官方代码，安装前要单独检查仓库来源、权限和维护状态。

## 第一次使用

1. 打开 ComfyUI，先加载官方提供的基础文字生成图片工作流或模板。
2. 如果模板提示缺少模型，从可信官方或作者页面下载，并放入界面提示的正确模型目录。
3. 只修改提示词和输出尺寸，保留其他默认参数。
4. 点击 Queue/运行按钮，等待节点依次执行。
5. 在保存图像节点和输出目录中找到结果，记录本次工作流和模型名称。

第一次成功的标准不是“生成完美图片”，而是所有节点无红色错误、图片成功写入输出目录、下次还能加载同一工作流复现。

## 常见问题

**显存不足或生成中断**：先降低图片尺寸、批量数量，关闭其他显卡应用，换更轻量的模型。不要盲目复制启动参数掩盖资源问题。

**节点变红或提示缺失**：查看具体节点名称和错误日志。先确认模型文件路径，再判断是否缺少自定义节点；不要使用来源不明的一键整合包。

**工作流来自别人却打不开**：工作流只是连接和参数，通常不包含所需模型。按缺失清单逐项核对模型、节点及其许可证。

**输出找不到**：检查保存图像节点的文件名前缀和当前安装的输出目录，不要在磁盘上无目的全盘搜索或删除。

## 更新与卸载

更新前备份重要工作流、记录自定义节点和模型目录。Desktop 更新后先跑官方基础模板，再逐个验证第三方节点，便于定位兼容性问题。

官方 Windows 文档说明，卸载 Launcher/Desktop 不会自动删除所有模型、输出和安装数据。当前常见目录包括：

- `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Installs`
- `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Shared`
- `%APPDATA%\Comfy Desktop`

这些路径会随版本变化。删除前先在应用设置或官方文档核对，并备份工作流与输出；不要整目录清理还在使用的模型库。

## 费用、隐私与开源信息

- **费用**：本地 ComfyUI 软件可免费使用；模型下载、硬件、电力和可能接入的云服务可能产生额外成本。
- **隐私**：本地工作流可在设备上处理素材，但扩展节点可能联网。安装任何节点前查看其代码来源、网络行为和权限。
- **开源**：官方 ComfyUI 仓库采用 GPL-3.0 许可证；模型、插件、工作流素材和输出的权利条件彼此独立。
- **安全**：自定义节点本质上可能执行代码。不要运行来源不明的整合包、安装脚本或要求关闭安全软件的教程；官方 [安全策略](https://github.com/Comfy-Org/ComfyUI/security) 说明了本机绑定、第三方节点和漏洞报告边界。

## 官方资料与核验日期

- [ComfyUI Windows Desktop 安装文档](https://docs.comfy.org/installation/desktop/windows)
- [ComfyUI 官方下载](https://www.comfy.org/download)
- [ComfyUI 官方仓库](https://github.com/Comfy-Org/ComfyUI)
- [ComfyUI 官方安全策略](https://github.com/Comfy-Org/ComfyUI/security)

本文最后核验：**2026-08-26**。系统要求、目录、桌面版能力和模型生态变化较快，请在安装当天复查官方文档。
