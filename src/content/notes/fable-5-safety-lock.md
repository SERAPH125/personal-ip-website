---
title: "Fable 5：Mythos 戴上「安全锁」之后"
description: "Fable 5 与 Mythos 5 使用同一个底层模型，但公开版增加了安全分类器与回退机制。超过 95% 指未触发回退的早期会话占比，不是能力得分。"
publishedAt: 2026-08-13
series: observe
sequence: 2
cover: "assets/covers/fable-5.jpg"
coverAlt: "Fable 5 与 Mythos 5 视频封面"
featured: false
tags: ["模型观察", "AI 安全", "Anthropic"]
draft: false
video:
  platform: douyin
  url: "https://v.douyin.com/sAoQQVUBtaM/"
  title: "Fable 5 来了：Mythos 戴上安全锁的版本"
  hook: "同一个底模，两种开放方式"
---

## 先说结论：同一个底模，两种开放方式

Fable 5 不是把 Mythos 简单改了一个名字，也不宜粗暴理解成「阉割版」。Anthropic 的公开材料说明，两者使用相同的底层模型权重，主要差别在访问范围和安全机制。

Fable 5 面向普通用户与开发者开放；Mythos 5 则保留给 Project Glasswing 中经过审核的网络防御与关键基础设施合作方。

可以把它们理解成同一台发动机的两种配置：Fable 5 多了一套会介入敏感请求的「安全锁」。

## Mythos 为什么没有一开始就公开

Anthropic 先把 Mythos Preview 提供给有限的防御合作方，用来寻找和修复关键软件漏洞。官方披露的案例包括一个存在多年、后来得到修复的 OpenBSD 漏洞。

「发现漏洞、复现漏洞、执行多阶段任务」既能帮助防御者，也可能被攻击者利用。风险来自这种一体两面的能力，而不是「会不会写代码」这一件事。因此，在更广泛开放前增加额外防护，是产品边界的一部分。

## 「安全锁」到底怎么工作

Fable 5 的安全层包含独立分类器，用来识别潜在滥用或绕过防护的请求，重点覆盖网络安全、生物与化学，以及模型蒸馏等高风险领域。

请求触发分类器后，系统可能拒绝处理，或切换到其他模型完成部分任务。

这套机制不保证零误判。官方也承认分类器会偏保守，正常的编程、调试或研究请求仍可能被拦下。对于 API 开发者，真正需要处理的是拒绝状态、回退路径与用户提示，而不只是换一个模型名。

## 「超过 95%」真正指什么

短视频里把信息概括成「同一个底层模型，95% 的日常场景能力一致」，便于理解，但文字版需要补上限定：官方公布的是早期使用数据——**超过 95% 的 Fable 5 会话没有触发模型回退。**

因此，95% 指「未触发回退的会话占比」，不是能力测试得了 95 分，也不能推导出两个产品在任何任务上都有 95% 的答案一致率。

> 相同的底模，不等于完全相同的使用体验。

## 适用范围与不确定性

「安全锁」是便于理解的比喻，不是某个单一组件的正式名称。分类器、回退规则、套餐额度与可用地区都可能继续变化；「超过 95%」也是发布初期的总体数据，不能保证每类用户、每个时期都保持相同比例。

本文解释的是公开产品设计与使用边界，不构成对模型安全性或基准成绩的独立验证。涉及当前价格、区域和 API 行为时，应以官方文档的最新页面为准。

## 资料来源

- [Anthropic：Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [Anthropic：Fable 5 safeguards research](https://www.anthropic.com/research/claude-fable-5-mythos-5)
- [Anthropic：Assessing Claude Mythos Preview](https://www.anthropic.com/research/mythos-preview)
