---
title: "Cherry Studio 安装与入门：安全连接第一个 AI 模型"
toolName: "Cherry Studio"
description: "安装开源桌面客户端，理解模型服务商、API 密钥与本地模型的区别，并完成首次对话。"
audience: "希望在一个桌面应用中管理多个模型服务，或连接 Ollama 等本地模型的普通用户与效率工具爱好者。"
setupSummary: "安装客户端后还需配置一个模型来源；客户端约 10 分钟，服务商开通或本地模型准备时间另计。"
privacySummary: "对话数据流向由所选模型服务决定；桌面客户端开源不代表所有请求都只在本机处理。"
origin: china
category: language-model
accessTypes: [desktop]
platforms: [windows, macos, linux]
pricing: free
openSource: true
license: "AGPL-3.0"
officialUrl: "https://www.cherry-ai.com/"
downloadUrl: "https://www.cherry-ai.com/download"
repositoryUrl: "https://github.com/CherryHQ/cherry-studio"
versionChecked: "Cherry Studio stable desktop channel"
verifiedAt: 2026-08-26
cover: "/assets/tools/cherry-studio/cover.svg"
coverAlt: "Cherry Studio 桌面客户端连接云端和本地模型服务示意图"
sequence: 6
draft: false
---

## 快速判断

Cherry Studio 是“模型客户端”，不是一个单独的大模型。它把不同服务商的在线模型、兼容 API 和部分本地模型入口集中到桌面界面中，适合需要切换模型、整理对话和管理多个助手的用户。

最重要的概念是数据流向：你在 Cherry Studio 输入问题，通常仍会发送给当前选择的模型服务商；只有明确连接本机模型并确认无外部调用时，才可能形成完整的本地工作流。

## 安装前检查

1. 确认 Windows、macOS 或 Linux 系统和芯片架构。
2. 决定模型来源：已有云端 API、服务商账户，还是本机 Ollama。
3. 查看所选服务商的计费、隐私、地区与模型使用条款。
4. 为 API 密钥准备安全保存方式；不要把真实密钥放进截图、教程或聊天消息。

## 图解安装

![Cherry Studio 从安装客户端到测试模型连接的六步流程图](/personal-ip-website/assets/tools/cherry-studio/install-flow.svg)

优先从官方网站下载；需要核对源码和许可证时，访问 `CherryHQ/cherry-studio` 官方仓库。普通用户选择稳定版，预发布版更适合愿意排错和反馈问题的人。

![Cherry Studio 添加模型服务商、API 地址和密钥的设置界面示意](/personal-ip-website/assets/tools/cherry-studio/setup-screen.svg)

安装完成后进入模型服务设置。云端服务通常需要 API 地址、API 密钥和模型名称；具体字段以服务商官方文档为准。图中的地址和密钥都是占位示意，不能直接使用。

![Cherry Studio 选择服务商和模型后进行首次安全对话的示意](/personal-ip-website/assets/tools/cherry-studio/first-use.svg)

如果你选择 Ollama，先单独确认 `ollama list` 能看到本机模型，再在 Cherry Studio 中配置本地连接。把“本地模型是否正常”和“客户端能否连接”分两步排查。

## 第一次使用

选择已经配置好的服务商和模型，用不含敏感信息的问题测试：

> 请把下面三条公开信息整理成“事项、日期、来源”表格。没有提供的事实不要补充，并标出不确定项。

发送前再次看一眼当前模型名称，发送后检查回答是否服从格式、是否凭空补充信息。只有连通测试成功且费用可控，再导入更长的普通资料。

## 常见问题

**提示密钥无效**：回到服务商官方控制台确认密钥状态、权限和 API 地址，不要在论坛贴出完整密钥求助。

**模型列表为空**：先确认服务商账户权限和当前 API 文档，再检查客户端字段。模型名称可能更新，不能只照搬旧教程。

**请求失败或超时**：区分网络、服务商额度、本地代理和客户端配置。先用最短问题测试，不要不断重复长请求造成额外费用。

**本地模型连不上**：先在终端验证 Ollama，再检查地址和端口。不要把本地服务直接暴露到公网。

## 更新与卸载

使用应用内更新或官方网站稳定版。更新前备份重要对话和配置，但导出文件可能包含服务地址、对话内容甚至敏感字段，保存和分享前必须检查。

卸载使用系统应用管理器。若要清理配置目录，先在官方文档或仓库 Issue 中核对当前路径并备份；不要误删 Ollama 模型或其他应用共用的数据目录。

## 费用、隐私与开源信息

- **费用**：Cherry Studio 客户端可免费使用；云端模型通常按服务商规则收费，本地模型也会消耗硬件、电力和存储。
- **隐私**：数据处理边界取决于当前模型、服务商、插件和联网功能。每次切换模型都应知道内容发往哪里，并复查官方 [隐私政策](https://github.com/CherryHQ/cherry-studio/blob/main/PRIVACY.md) 与所选模型服务商的规则。
- **开源**：官方仓库采用 AGPL-3.0 许可证；准备分发修改版、提供网络服务或商用集成时，应自行核对许可证义务。
- **密钥安全**：按服务商提供的方式创建最小权限密钥，定期轮换，发现泄露立即撤销，而不是仅从界面删除。

## 官方资料与核验日期

- [Cherry Studio 官方网站](https://www.cherry-ai.com/)
- [Cherry Studio 官方下载](https://www.cherry-ai.com/download)
- [Cherry Studio 官方仓库](https://github.com/CherryHQ/cherry-studio)
- [Cherry Studio 官方隐私政策](https://github.com/CherryHQ/cherry-studio/blob/main/PRIVACY.md)
- [Cherry Studio 官方安全策略](https://github.com/CherryHQ/cherry-studio/security)

本文最后核验：**2026-08-26**。版本、模型服务字段和兼容平台会变化，安装与配置时请复查官方页面和所选服务商文档。
