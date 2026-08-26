---
title: "Cline 安装与入门：在 VS Code 中控制模型与工具权限"
toolName: "Cline"
description: "安装开源 Cline 扩展，配置模型服务、控制文件与终端审批，并完成第一次小型代码任务。"
audience: "希望在 VS Code 中使用开源编程代理，并愿意自行选择模型服务与管理 API 费用的开发者。"
setupSummary: "扩展安装约 5 分钟；还需配置受支持的模型服务或本地模型，费用与隐私取决于所选提供方。"
privacySummary: "Cline 在本地协调工具，但代码与提示可能发往你选择的模型服务；自动批准会扩大文件和命令风险。"
origin: international
category: ai-coding
toolType: plugin
difficulty: beginner
accessTypes: [desktop]
platforms: [windows, macos, linux]
pricing: usage-based
pricingNote: "扩展免费，模型费用依提供方；使用自带 API、订阅或本地模型时，实际成本分别由对应服务决定。"
openSource: true
license: "Apache-2.0"
officialUrl: "https://docs.cline.bot/getting-started/installing-cline"
downloadUrl: "https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev"
repositoryUrl: "https://github.com/cline/cline"
versionChecked: "Cline VS Code extension stable channel"
verifiedAt: 2026-08-26
cover: "/assets/tools/cline/cover.svg"
coverAlt: "Cline 电脑端安装和首次使用流程示意图"
sequence: 17
draft: false
---

## 快速判断

Cline 是安装在 VS Code 中的开源编程代理，可以连接多种模型服务并使用文件、浏览器与终端工具。它给用户更多选择，也把模型配置和费用管理交给用户。

扩展开源不代表所选模型服务开源，也不代表请求留在本机。配置前先画清数据路径：VS Code、Cline、模型提供方和可能调用的外部工具。

## 安装前检查

1. 安装最新版 VS Code。
2. 从官方市场安装 Cline。
3. 准备受支持的模型来源。
4. 为练习项目创建 Git 分支。

## 图解安装

![Cline 从检查到首次使用的六步安装流程](/personal-ip-website/assets/tools/cline/install-flow.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev">官方安装资料</a> 整理 · 核验于 2026-08-26</p>

从 VS Code 官方市场安装 Cline，并核对扩展标识与官方仓库。配置模型时只使用提供方官方创建的密钥。

![Cline 安装时需要确认的三个关键点](/personal-ip-website/assets/tools/cline/setup-screen.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://docs.cline.bot/getting-started/installing-cline">官方产品或项目说明</a> 整理 · 核验于 2026-08-26</p>

保持自动批准关闭，先逐条了解读取文件、编辑、命令和浏览器动作。密钥放在扩展安全设置，不写进代码或截图。

![Cline 第一次使用的目标与验收标准](/personal-ip-website/assets/tools/cline/first-use.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://docs.cline.bot/getting-started/installing-cline">官方使用资料</a> 整理 · 核验于 2026-08-26</p>

在小仓库里让 Cline 解释一个函数，再批准一次单文件修改。记录模型调用成本并运行测试。

## 第一次使用

1. 安装并打开 Cline 面板。
2. 选择模型提供方。
3. 安全填写凭据。
4. 打开练习仓库。
5. 逐条批准小任务并测试。

可以从这个低风险任务开始：

> 只读取当前文件和对应测试；说明修改计划后等待我确认，不运行安装或发布命令。

这次代理任务通过的标准是：密钥没有进入仓库、每个工具动作都经过审批，而且模型成本与 Git diff 都能检查。

## 常见问题

**模型连接失败**：检查提供方 API 地址、密钥、模型名称和账户额度，不公开完整密钥。

**费用上升过快**：缩小上下文和任务，选择合适模型，并关闭不必要的自动循环。

**自动批准风险过高**：关闭自动批准，重启任务并逐条确认文件和命令操作。

**扩展更新后行为变化**：查看官方 changelog 与权限设置，在练习仓库重新验收。

## 更新与卸载

通过 VS Code 扩展管理器更新，并阅读官方发布说明。更新后复查模型、密钥和自动批准设置。

先从模型提供方撤销不再使用的密钥，再卸载扩展。项目改动仍通过 Git 处理。

## 费用、隐私与开源信息

- **费用**：Cline 扩展免费开源，模型 API、云服务或订阅按所选提供方收费，本地模型也有硬件成本。
- **隐私**：数据去向由模型提供方和启用的工具共同决定；敏感代码只在明确协议、权限和保留政策下使用。请复查官方 [隐私或安全说明](https://github.com/cline/cline/security)。
- **开源状态**：Cline 官方仓库采用 Apache-2.0 且维护活跃；本网站只引用安装设计，不复制代码或引入依赖。
- **安全边界**：API 密钥最小权限、自动批准默认关闭、所有命令和 Git diff 人工审查。

## 官方资料与核验日期

- [Cline 安装文档](https://docs.cline.bot/getting-started/installing-cline)
- [Cline 官方仓库](https://github.com/cline/cline)
- [Cline 安全策略](https://github.com/cline/cline/security)

本文最后核验：**2026-08-26**。安装入口、系统要求、模型能力、价格与隐私规则会变化，实际操作时请再次查看官方页面。
