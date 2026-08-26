---
title: "GitHub Copilot 安装与入门：在编辑器里完成第一次受控修改"
toolName: "GitHub Copilot"
description: "在桌面编辑器安装 GitHub Copilot，登录授权、理解建议与代理模式，并验收第一次代码修改。"
audience: "希望在 VS Code 等受支持桌面编辑器中使用 AI 补全、聊天和代理能力的开发者。"
setupSummary: "安装官方扩展并登录 GitHub 账号约需 10 分钟；具体模型、额度和代理能力取决于套餐与组织策略。"
privacySummary: "代码上下文和提示可能发送到 GitHub Copilot 服务；私有仓库、组织策略和内容排除设置需先核对。"
origin: international
category: ai-coding
toolType: plugin
difficulty: beginner
accessTypes: [desktop]
platforms: [windows, macos, linux]
pricing: freemium
openSource: false
license: "Proprietary"
officialUrl: "https://docs.github.com/en/copilot"
downloadUrl: "https://marketplace.visualstudio.com/items?itemName=GitHub.copilot"
versionChecked: "GitHub Copilot extension stable channel"
verifiedAt: 2026-08-26
cover: "/assets/tools/github-copilot/cover.svg"
coverAlt: "GitHub Copilot 电脑端安装和首次使用流程示意图"
sequence: 15
draft: false
---

## 快速判断

GitHub Copilot 是安装在桌面 IDE 中的 AI 编程助手。它可以补全、解释和修改代码，但不会替代测试、代码审查和版本控制。

代理模式可能读取多个文件、运行命令或创建提交。第一次使用只在可回滚的练习仓库中授权，并明确每一步允许的操作。

## 安装前检查

1. 安装受支持的桌面 IDE。
2. 准备可登录的 GitHub 账号。
3. 使用单独的练习仓库。
4. 确认组织 Copilot 与数据策略。

## 图解安装

![GitHub Copilot 从检查到首次使用的六步安装流程](/personal-ip-website/assets/tools/github-copilot/install-flow.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://marketplace.visualstudio.com/items?itemName=GitHub.copilot">官方安装资料</a> 整理 · 核验于 2026-08-26</p>

从 IDE 官方扩展市场安装 GitHub 发布的 Copilot 扩展，核对发布者和扩展标识。完成浏览器登录后回到编辑器检查状态。

![GitHub Copilot 安装时需要确认的三个关键点](/personal-ip-website/assets/tools/github-copilot/setup-screen.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://docs.github.com/en/copilot">官方产品或项目说明</a> 整理 · 核验于 2026-08-26</p>

先了解补全、Chat、Edit 和 Agent 的权限差异。普通解释任务不需要让代理执行终端命令。

![GitHub Copilot 第一次使用的目标与验收标准](/personal-ip-website/assets/tools/github-copilot/first-use.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://docs.github.com/en/copilot">官方使用资料</a> 整理 · 核验于 2026-08-26</p>

让 Copilot 修改一个有测试的小函数。修改后看差异、运行测试、人工阅读，而不是直接接受所有建议。

## 第一次使用

1. 安装扩展并完成登录。
2. 打开练习项目并新建分支。
3. 提出一个单文件小任务。
4. 逐段审查建议。
5. 运行测试并查看 Git diff。

可以从这个低风险任务开始：

> 请只修改这个函数：为空输入返回空数组，并补充对应测试。不要更改依赖或其他文件。

这次代码任务通过的标准是：变更范围符合任务、测试能捕获目标行为，而且 Git diff 没有无关修改。

## 常见问题

**扩展未激活**：检查登录账号、订阅状态、IDE 版本和组织策略。

**没有补全建议**：确认当前文件类型受支持、扩展已启用且网络正常。

**代理想运行高风险命令**：拒绝并缩小任务，先让它解释命令目的和影响。

**建议代码不正确**：以测试、官方文档和人工审查为准，不把模型输出当事实。

## 更新与卸载

通过 IDE 扩展管理器更新。更新后检查模型选择、代理审批和组织策略是否变化。

先退出 Copilot 与 GitHub 授权，再卸载扩展。项目中生成的代码仍需按项目流程审查和保留。

## 费用、隐私与开源信息

- **费用**：提供有限免费或试用能力，个人与组织套餐的额度、模型和功能不同，以 GitHub 当前价格说明为准。
- **隐私**：提示、代码上下文和遥测可能由服务处理；私有代码使用前查看 GitHub 隐私政策与组织内容排除设置。请复查官方 [隐私或安全说明](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)。
- **开源状态**：Copilot 服务与官方扩展为闭源商业产品，许可证标记为 Proprietary。
- **安全边界**：代理可运行命令和修改多个文件；必须使用版本控制、最小权限和测试作为安全锁。

## 官方资料与核验日期

- [GitHub Copilot 官方文档](https://docs.github.com/en/copilot)
- [GitHub Copilot Quickstart](https://docs.github.com/en/copilot/get-started/quickstart)
- [GitHub 隐私声明](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)

本文最后核验：**2026-08-26**。安装入口、系统要求、模型能力、价格与隐私规则会变化，实际操作时请再次查看官方页面。
