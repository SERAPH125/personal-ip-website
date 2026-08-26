---
title: "Claude Code 安装与入门：在终端中完成第一个可回滚任务"
toolName: "Claude Code"
description: "安装 Claude Code CLI，登录账号、授权项目目录，并用 Git 和测试验收第一次修改。"
audience: "熟悉基本终端与 Git，希望使用 Claude 编程代理处理本地项目的开发者。"
setupSummary: "按系统使用官方原生安装器并验证版本；Windows 需区分 PowerShell 与 CMD。全程约 10—20 分钟。"
privacySummary: "Claude Code 会按任务读取项目文件并与云端模型交互，也可能运行命令；敏感仓库应先确认权限与组织政策。"
origin: international
category: ai-coding
toolType: command-line-tool
difficulty: beginner
accessTypes: [cli]
platforms: [windows, macos, linux]
pricing: paid
openSource: false
license: "Proprietary"
officialUrl: "https://code.claude.com/docs/en/quickstart"
downloadUrl: "https://code.claude.com/docs/en/setup"
versionChecked: "Claude Code stable channel"
verifiedAt: 2026-08-26
cover: "/assets/tools/claude-code/cover.svg"
coverAlt: "Claude Code 电脑端安装和首次使用流程示意图"
sequence: 16
draft: false
---

## 快速判断

Claude Code 是运行在终端里的编程代理，能够读取项目、修改文件和执行命令。它适合有 Git 基础、能审查命令与差异的用户。

终端代理的风险不是回答错一句话，而是对文件和命令产生真实影响。第一次只在练习仓库中使用，不授予家目录或包含密钥的上级目录。

## 安装前检查

1. 确认系统为受支持的 macOS、Linux 或 Windows；原生 Windows 建议安装 Git for Windows。
2. 准备可登录的 Anthropic 账号。
3. 让 Git 工作区保持可回滚。
4. 用 `.gitignore` 隔离 `.env`、密钥与私人文件，并在开始前检查 `git status`。

## 图解安装

![Claude Code 从检查到首次使用的六步安装流程](/personal-ip-website/assets/tools/claude-code/install-flow.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://code.claude.com/docs/en/setup">官方安装资料</a> 整理 · 核验于 2026-08-26</p>

macOS、Linux 或 WSL 使用官方原生安装器：

```bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
```

Windows PowerShell 使用：

```powershell
irm https://claude.ai/install.ps1 | iex
claude --version
```

Windows CMD 使用：

```bat
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
claude --version
```

不要混用 PowerShell 与 CMD 的命令。也可以按官方页面选择 Homebrew、WinGet 或 Linux 软件源，但后续更新应继续使用同一渠道。

![Claude Code 安装时需要确认的三个关键点](/personal-ip-website/assets/tools/claude-code/setup-screen.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://code.claude.com/docs/en/quickstart">官方产品或项目说明</a> 整理 · 核验于 2026-08-26</p>

关闭并重新打开终端，进入一个新建分支的练习仓库，再运行 `claude`。按浏览器提示登录；首次请求目录与命令权限时，理解每项作用后再批准。

![Claude Code 第一次使用的目标与验收标准](/personal-ip-website/assets/tools/claude-code/first-use.svg)

<p class="tool-image-source">原创步骤示意，根据 <a href="https://code.claude.com/docs/en/quickstart">官方使用资料</a> 整理 · 核验于 2026-08-26</p>

从只读解释开始，再让它做一个单文件、有测试的修改。保留终端输出和 Git diff，方便回滚。

## 第一次使用

1. 运行 `claude --version` 验证安装，再执行 `claude` 并完成登录。
2. 进入练习仓库并新建分支。
3. 启动后先让它解释项目。
4. 提出单文件小修改。
5. 运行测试并审查 diff。

可以从这个低风险任务开始：

> 先说明你将读取和修改哪些文件；只修复这个输入校验，并运行相关测试，不安装依赖。

第一次验收只看三件事：权限范围是否只在项目内、命令与变更是否可解释、测试通过后是否没有无关文件变化。

## 常见问题

**命令未找到**：重新核对官方安装路径、Shell 配置和终端重启步骤。

**登录或额度失败**：区分 Claude 应用订阅、API 和组织账号，查看当前官方账号说明。

**读取了不应访问的文件**：立即停止任务，撤销权限并检查项目目录是否包含链接或敏感文件。

**修改范围失控**：中止、查看 Git diff、回滚练习分支，再用更窄的任务重新开始。

## 更新与卸载

使用官方当前推荐方式更新，并查看 changelog。升级后先在练习仓库验证权限提示与命令行为。

按官方 Setup 文档移除 CLI，并检查 Shell 配置。账号、云端记录和项目改动需要分别处理。

## 费用、隐私与开源信息

- **费用**：通常依赖付费 Claude 方案或相应企业授权，具体额度和可用模型以官方当前说明为准。
- **隐私**：代码、提示和工具结果可能发送给 Anthropic；使用敏感仓库前必须确认组织协议与数据控制。请复查官方 [隐私或安全说明](https://www.anthropic.com/legal/privacy)。
- **开源状态**：Claude Code 为闭源商业 CLI，许可证标记为 Proprietary；不要使用声称破解订阅的安装包。
- **安全边界**：只在版本控制项目内运行，逐条审查命令，不允许读取密钥、执行破坏性命令或未经确认向外部发送数据。

## 官方资料与核验日期

- [Claude Code Quickstart](https://code.claude.com/docs/en/quickstart)
- [Claude Code Setup](https://code.claude.com/docs/en/setup)
- [Anthropic 隐私政策](https://www.anthropic.com/legal/privacy)

本文最后核验：**2026-08-26**。安装入口、系统要求、模型能力、价格与隐私规则会变化，实际操作时请再次查看官方页面。
