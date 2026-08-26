---
title: "Ollama 安装与入门：在本地运行第一个 AI 模型"
toolName: "Ollama"
description: "从硬件与磁盘检查，到安装本地服务、下载小模型和完成第一次对话。"
audience: "希望在自己的电脑上试用开源模型、重视本地工作流，并能接受模型下载和硬件门槛的用户。"
setupSummary: "安装 Ollama 后下载一个小模型即可使用；程序安装很快，模型下载时间取决于网络和文件大小。"
privacySummary: "本地模型可在设备上推理，但下载、更新或接入外部应用时仍可能联网；是否离线取决于完整工作流。"
origin: international
category: language-model
accessTypes: [cli, local-service]
platforms: [windows, macos, linux]
pricing: free
openSource: true
license: "MIT"
officialUrl: "https://docs.ollama.com/quickstart"
downloadUrl: "https://ollama.com/download"
repositoryUrl: "https://github.com/ollama/ollama"
versionChecked: "Ollama stable channel"
verifiedAt: 2026-08-26
cover: "/assets/tools/ollama/cover.svg"
coverAlt: "电脑通过 Ollama 命令行加载本地模型的示意图"
sequence: 3
draft: false
---

## 快速判断

Ollama 适合想在本机运行模型、测试本地 API，或给其他桌面 AI 客户端提供模型服务的用户。它把模型下载、启动和管理封装成较简单的命令，不要求你先搭建复杂的 Python 环境。

本地运行不等于“任何电脑都跑得快”。模型越大，对内存、显存和磁盘要求越高。第一次应选择官方模型库里的小参数版本，先确认完整流程可用，再考虑更大的模型。

## 安装前检查

1. 在系统信息中查看内存、显卡和处理器；共享内存或入门显卡优先选择小模型。
2. 检查系统盘和模型存储盘的剩余空间。模型文件常以 GB 计，还会有下载和缓存开销。
3. 公司电脑可能禁止常驻本地服务或模型下载，应先遵守组织网络与数据政策。
4. 明确模型本身也有独立许可证和使用限制，Ollama 的 MIT 许可证并不会覆盖每一个模型。

## 图解安装

![Ollama 从空间检查到本地对话的六步流程图](/personal-ip-website/assets/tools/ollama/install-flow.svg)

进入官方下载页，切换到 Windows、macOS 或 Linux 标签，使用对应的官方安装方式。安装后新开一个终端并运行：

```bash
ollama --version
```

![Ollama 官方下载页的 Windows 安装入口](/personal-ip-website/assets/tools/ollama/step-01.webp)

<p class="tool-image-source">图片来源：<a href="https://ollama.com/download">Ollama 官方下载</a> · 页面截取于 2026-08-26</p>

如果系统提示命令不存在，先退出并重开终端或重启应用，不要重复安装多个来源的版本。

![Ollama 官方 Quickstart 页面，包含平台与语言入口](/personal-ip-website/assets/tools/ollama/step-02.webp)

<p class="tool-image-source">图片来源：<a href="https://docs.ollama.com/quickstart">Ollama 官方 Quickstart</a> · 页面截取于 2026-08-26</p>

官方 Quickstart 是核对当前命令、API 和平台差异的首选资料。第三方客户端接入时，也应先在命令行确认 Ollama 本身运行正常。

## 第一次使用

下面用一个小模型演示。模型名称和可用标签会变化，执行前可在官方模型库确认 `gemma3:1b` 仍存在：

```bash
ollama run gemma3:1b
```

首次运行会先下载模型。完成后输入“请用三句话解释什么是本地大模型”，确认可以生成回答，再输入 `/bye` 退出。随后查看本机已安装模型：

```bash
ollama list
```

回答速度慢时，先换更小的模型，不要同时运行多个高负载任务。模型回答仍可能出错，不能仅因为它在本地运行就降低事实核验要求。

## 常见问题

**下载很慢或中断**：检查磁盘空间和网络稳定性，保留终端中的原始错误。不要从网盘下载同名未知模型文件替代官方来源。

**模型启动后电脑很卡**：退出当前模型，关闭其他占用内存或显存的程序，选择更小量化或更小参数版本。

**第三方客户端连不上**：先用 `ollama list` 验证命令行，再检查 Ollama 服务是否启动、客户端地址是否指向本机。不要为了连接而把本地服务直接暴露到公网。

**回答质量不理想**：先明确任务、补充上下文，再比较不同模型；“更大”通常更耗资源，也不保证在你的任务上一定更好。

## 更新与卸载

优先使用官方应用的更新方式或重新运行官方当前安装流程。更新后执行 `ollama --version`，并用一个小模型验证基本功能。

删除不再需要的模型可以释放大量空间：

```bash
ollama rm gemma3:1b
```

卸载程序请使用系统应用管理器或官方文档。模型目录可能独立保留；彻底删除前先运行 `ollama list` 记录需要的模型，并按官方当前路径说明操作。

## 费用、隐私与开源信息

- **费用**：Ollama 客户端可免费使用；电力、硬件、存储和网络成本由本机承担，第三方模型或云端接口可能另行计费。
- **隐私**：在本机推理可减少把提示词发送给云端的需求，但下载安装、云功能、第三方插件和外部 API 都需要单独核对。官方 [FAQ](https://docs.ollama.com/faq) 说明了本地与云端模式的数据边界及关闭云功能的方法。
- **开源**：Ollama 官方仓库采用 MIT 许可证；每个模型有自己的许可证、训练来源和商用条件，下载前必须分别查看。
- **安全**：不要把本地 API 无认证暴露到公网；模型文件和第三方 Modelfile 也应来自可信来源。

## 官方资料与核验日期

- [Ollama 官方下载](https://ollama.com/download)
- [Ollama 官方 Quickstart](https://docs.ollama.com/quickstart)
- [Ollama 官方模型库](https://ollama.com/search)
- [Ollama 官方仓库](https://github.com/ollama/ollama)
- [Ollama 官方 FAQ：本地与云端数据说明](https://docs.ollama.com/faq)

本文最后核验：**2026-08-26**。平台支持、模型标签、硬件建议和命令可能更新，执行前请再次查看官方资料。
