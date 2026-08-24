---
title: "该让 Coding Agent 做什么，不该让它做什么"
description: "Agent 能改文件、运行命令甚至访问外部系统之后，任务选择和权限边界比提示词更重要。用三级授权表决定哪些可自动、哪些需审批、哪些不应委托。"
publishedAt: 2026-08-24
sourcesCheckedAt: 2026-08-23
series: agent
sequence: 10
cover: "assets/covers/learning-vibe-05.png"
coverAlt: "该让 Coding Agent 做什么，不该让它做什么学习路线第 5 步封面"
featured: false
tags: ["Coding Agent","权限","安全边界"]
draft: false
learning:
  track: vibe-coding
  step: 5
---


当 AI 只能回答问题时，答错了最多浪费一点时间。当 Coding Agent 可以修改文件、运行命令、安装依赖和连接外部系统时，答错可能直接改变真实世界。

所以使用 Agent 的第一道问题不应该是「它会不会做」，而是：**这件事适不适合交给它做？**

## 绿色任务 · 可以从这里开始

绿色任务范围小、结果容易检查、失败容易撤回。例如：

- 修改文案和局部样式；
- 为现有函数补单元测试；
- 修复可以稳定复现的小错误；
- 更新 README 和命令说明；
- 检查失效链接；
- 整理重复但没有业务判断的机械工作。

这类任务反馈周期短，你能快速比较指令、结果和验证证据。

## 黄色任务 · 必须有人审批

黄色任务通常涉及跨文件修改、业务逻辑或更大的影响范围：

- 数据库结构变更；
- 登录、权限和账号系统；
- 大规模依赖升级；
- 跨模块重构；
- 自动发布和基础设施配置；
- 批量修改真实业务数据。

这些任务可以让 Agent 调研、写计划、准备补丁和运行测试，但关键动作应保留人工检查点。

一个实用的分界是：如果失败会影响其他人、真实数据或线上服务，就不要默认自动批准。

## 红色任务 · 不应直接委托

以下操作不适合由 Agent 在缺少明确授权和专业监督时执行：

- 删除生产数据库或备份；
- 处理真实密码、私钥和高权限凭证；
- 无回滚方案地修改线上支付；
- 代替专业人员作出医疗、法律或金融决定；
- 为了绕过安全限制而关闭防护；
- 对用户或员工执行未经审查的自动化决策。

问题不在于模型一定会犯错，而是这些操作的错误成本太高。

## 权限要跟着任务走

不要为了方便，一开始就给 Agent 整台电脑、全部网络和所有密钥的权限。

更稳妥的顺序是：

1. 先只允许读取项目；
2. 确认计划后开放项目内写入；
3. 运行命令时逐项审批；
4. 网络访问限制在需要的域名；
5. 外部发布、删除和消息发送单独确认；
6. 高风险任务使用隔离环境和临时凭证。

沙箱并不等于绝对安全。它的作用是缩小错误或恶意输入能够影响的范围。

## 仓库里的文字也可能是输入

Agent 会读取 README、Issue、网页和依赖文档。这些内容中可能出现诱导它忽略原任务、读取密钥或执行额外命令的指令。

来自项目外部或不可信贡献者的文字，应该被视为数据，而不是自动获得更高优先级的命令。遇到突然要求上传文件、关闭安全检查或访问无关路径时，应停下来检查来源。

## 一张三级授权表

| 级别 | Agent 可以做什么 | 人负责什么 |
|---|---|---|
| 自动 | 读取、分析、生成低风险草稿、运行安全检查 | 抽查结果 |
| 审批 | 修改代码、安装依赖、联网、创建提交 | 逐项确认和验收 |
| 禁止 | 不可逆删除、泄露密钥、绕过安全、未经授权的外部操作 | 必须由有权限的人处理 |

工具越强，越不应该依赖一句「小心操作」。真正可靠的边界，需要由权限、沙箱、检查点、日志和回滚一起组成。

Agent 可以替你执行步骤，但不能替你决定哪些风险值得承担。

## 参考资料

- [GitHub：Coding Agent 适合与不适合的任务](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks)
- [GitHub：云端与本地沙箱](https://docs.github.com/en/copilot/concepts/about-cloud-and-local-sandboxes)
- [OpenAI：Codex Windows 沙箱实践](https://openai.com/index/building-codex-windows-sandbox/)
- [Anthropic：Claude Code 沙箱](https://www.anthropic.com/engineering/claude-code-sandboxing)
