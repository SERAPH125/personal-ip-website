---
title: "Codex 安装与入门：从命令行完成第一个编程任务"
toolName: "Codex"
description: "面向普通用户的 Codex CLI 安装、登录、首次使用与安全审阅指南。"
audience: "想用自然语言完成代码阅读、修改与验证，并愿意接触命令行的学习者和开发者。"
setupSummary: "先准备 Node.js，再安装官方 npm 包；全程约 10—20 分钟。"
privacySummary: "Codex 会按你的授权读取项目并可能执行命令；不要把密钥、客户数据或无关私人文件放进工作目录。"
origin: international
category: ai-coding
accessTypes: [cli]
platforms: [windows, macos, linux]
pricing: freemium
openSource: true
license: "Apache-2.0"
officialUrl: "https://learn.chatgpt.com/docs/codex/cli"
downloadUrl: "https://github.com/openai/codex/releases"
repositoryUrl: "https://github.com/openai/codex"
versionChecked: "Codex CLI stable channel"
verifiedAt: 2026-08-26
cover: "/assets/tools/codex/cover.svg"
coverAlt: "Codex 命令行窗口与首次使用检查清单示意图"
sequence: 1
draft: false
---

## 快速判断

Codex 适合“项目已经在电脑上，希望 AI 帮你读代码、改代码、跑测试”的场景。它主要在终端里工作，比普通聊天窗口更接近真实开发流程，也因此需要你认真确认当前目录、权限和每次改动。

如果你从未使用过终端，先完成一个很小的任务：让它解释项目结构或找出启动命令，不要一上来就让它重构整个项目。若你更偏好图形界面，可以先看 Cursor 指南。

## 安装前检查

1. 准备一个无敏感数据的练习项目，并确认你知道它的完整路径。
2. 安装当前受支持的 Node.js LTS；在终端运行 `node --version` 和 `npm --version`，两条命令都应返回版本号。
3. 如果项目使用 Git，先运行 `git status`，保存或提交自己的修改，便于随时比较和撤销 AI 产生的变更。
4. 公司电脑、受管设备或代理网络可能限制全局 npm 安装，请先遵守组织的 IT 规则。

Codex 本身开源，但使用的账户、模型和额度规则可能变化。安装前应在官方页面确认当前登录方式和可用计划。

## 图解安装

![Codex 从环境检查到审阅首个任务的六步流程图](/personal-ip-website/assets/tools/codex/install-flow.svg)

通用的 npm 安装方式如下：

```bash
npm install -g @openai/codex
codex --version
```

若第一条命令出现权限错误，不要随意关闭系统安全策略。优先检查 Node.js 的安装方式，或按照 Codex 官方页面中与你系统对应的安装标签操作。

![OpenAI Codex 官方开源仓库及 Apache-2.0 许可证页面](/personal-ip-website/assets/tools/codex/step-01.webp)

<p class="tool-image-source">图片来源：<a href="https://github.com/openai/codex">OpenAI Codex 官方仓库</a> · 页面截取于 2026-08-26</p>

官方仓库可以核对项目归属、许可证、发布记录和安全说明。下载二进制文件时，只使用官方仓库的 Releases 页面，不要从网盘或转载站获取。

![Codex 官方 GitHub Releases 页面，版本列表会持续更新](/personal-ip-website/assets/tools/codex/step-02.webp)

<p class="tool-image-source">图片来源：<a href="https://github.com/openai/codex/releases">Codex 官方 Releases</a> · 页面截取于 2026-08-26</p>

Releases 页面可能同时出现稳定版和预发布版。普通用户优先选择稳定版；截图仅用于识别页面结构，不代表推荐截图中的具体版本。

## 第一次使用

先在终端进入练习项目，再启动 Codex：

```bash
cd 你的项目路径
codex
```

按终端提示完成账户登录。第一次任务建议输入：

> 只读检查这个项目，告诉我它使用什么技术、如何启动、有哪些测试。先不要修改文件，也不要执行安装命令。

阅读回答后，再给一个边界清晰的小任务，例如“修正文档中的一个错字并说明改了哪一行”。每次允许命令或文件写入前，确认三件事：当前目录是否正确、命令影响什么、能否通过 Git 或备份恢复。

## 常见问题

**提示找不到 `codex` 命令**：关闭并重新打开终端，再运行 `npm config get prefix` 检查全局可执行文件目录是否已进入系统 PATH。

**登录页面打不开**：检查系统时间、默认浏览器和网络代理；公司网络环境下请联系管理员，不要复制来历不明的令牌。

**AI 想修改太多文件**：立即暂停，把任务缩小到一个目录或一个文件，并要求它先列计划和验证方法。用 `git diff` 检查真实变更。

**命令执行失败**：把完整错误信息交给 Codex解释，但不要让它通过关闭防火墙、杀毒软件或系统权限控制来“解决”。

## 更新与卸载

使用 npm 安装时，可以通过相同渠道更新：

```bash
npm install -g @openai/codex@latest
codex --version
```

卸载命令：

```bash
npm uninstall -g @openai/codex
```

卸载 CLI 不等于删除你的项目。若还要清理配置或登录状态，应先对照官方文档确认目录，避免误删项目文件。

## 费用、隐私与开源信息

- **费用**：CLI 可以免费安装；实际可用模型、登录计划和用量限制以官方实时说明为准。
- **隐私**：只把任务相关目录置于工作范围，使用 `.gitignore`、环境变量和密钥管理工具隔离敏感信息。任何“本地运行”都不意味着模型请求必然只在本机处理；使用前阅读 [OpenAI 隐私政策](https://openai.com/policies/privacy-policy/)。
- **开源**：官方仓库采用 Apache-2.0 许可证。开源的是客户端代码，不代表所连接模型、在线服务或第三方依赖都采用同一许可证。
- **安全底线**：涉及删除、部署、付款、密钥、生产数据库的操作必须人工复核，并先做可恢复备份。

## 官方资料与核验日期

- [Codex CLI 官方文档](https://learn.chatgpt.com/docs/codex/cli)
- [OpenAI Codex 官方仓库](https://github.com/openai/codex)
- [官方 Releases](https://github.com/openai/codex/releases)
- [Codex 官方安全策略](https://github.com/openai/codex/security)
- [OpenAI 隐私政策](https://openai.com/policies/privacy-policy/)

本文最后核验：**2026-08-26**。命令、登录方式、支持平台与额度会更新；执行安装前请再次查看官方页面。
