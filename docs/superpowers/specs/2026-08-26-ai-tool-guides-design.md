# AI 工具指南板块设计

日期：2026-08-26

状态：已获用户批准

基线分支：`codex/learning-paths`

建议实施分支：`codex/ai-tool-guides`

## 背景

网站当前使用 Astro 7、静态页面和 Content Collections，已有作品、学习路线、知识库与文章详情。用户希望新增一个独立的「工具指南」板块，用普通读者也能理解的方式讲清 AI 工具的安装、首次使用和常见问题，并要求教程图文并茂。

当前固定为 20 款工具。首批 8 款为 Codex、Cursor、Ollama、ComfyUI、TRAE、Cherry Studio、DeepSeek、可灵 AI；第二批 12 款为 ChatGPT Desktop、Claude Desktop、Kimi Work、InvokeAI、Stable Diffusion WebUI、Krita AI Diffusion、GitHub Copilot、Claude Code、Cline、剪映专业版、Filmora、FramePack。第二批只收录具备桌面应用、IDE 插件、CLI 或本地服务的工具，纯网页工具暂不加入。首页不展示工具入口，新内容只通过主导航进入。

## 目标

1. 维护一个与知识库分离的 AI 工具指南目录和 20 篇独立详情页。
2. 同时覆盖国际与国内工具，目录按语言模型、图片模型、AI 编程、视频模型四类组织。
3. 每篇教程提供真实、可复核的安装或访问步骤、首次实战、排错、更新/卸载、费用、隐私和许可证信息。
4. 每篇使用 4—6 张有说明的真实截图或原创示意图，做到图文并茂而不伪造软件界面。
5. 保持现有 Astro 技术栈、视觉语言和 GitHub Pages 静态部署方式。

## 非目标

- 不在首页增加工具卡片、推荐区或其他入口。
- 不把工具教程混入现有 `notes` collection 或知识库筛选。
- 不在第一版加入全文搜索、评论、登录、收藏、阅读进度或自动版本监控。
- 不引入第二套文档框架、数据库、服务端 API 或运行时内容请求。
- 不使用非官方安装包，不在截图中暴露密钥、账号、手机号或其他个人信息。
- 不把网页服务描述为需要安装；DeepSeek 和可灵 AI 应根据官方入口明确标注「免安装」或实际支持的客户端。

## 开源与公开实现调研

### Astro Starlight

- 项目：[withastro/starlight](https://github.com/withastro/starlight)，MIT 许可证。
- 解决的问题：在 Astro 中提供文档导航、搜索、侧边栏和内容组织，也支持[手动接入既有 Astro 项目](https://github.com/withastro/starlight/blob/main/docs/src/content/docs/manual-setup.mdx)。
- 可借鉴：独立内容集合、统一详情模板、目录导航和可访问性约定。
- 结论：不作为当前依赖。20 篇指南仍可由现有 Content Collections 和模型名称目录清晰承载；接入 Starlight 会形成与个人网站视觉不同的第二套文档界面。实施时借鉴其「内容与展示分离」设计，不复用代码。

### Docusaurus

- 项目：[facebook/docusaurus](https://github.com/facebook/docusaurus)，MIT 许可证。
- 解决的问题：提供完整的 React 文档站、版本化文档、导航和插件生态。
- 可借鉴：教程的固定章节、版本标记和文档更新机制。
- 结论：不采用。它会在现有 Astro 网站旁引入另一套 React 构建与路由体系，明显超过当前 20 篇静态内容的需要。

### Pagefind

- 项目：[Pagefind](https://github.com/Pagefind/pagefind)，MIT 许可证。
- 解决的问题：为静态网站生成低带宽全文搜索和筛选索引。
- 可借鉴：以后内容量增大时，可按工具类别和平台建立静态筛选索引。
- 结论：当前不安装。20 篇指南仍可通过四类模型名称目录直接定位；达到约 30 篇或读者明确需要关键词搜索时再评估。

### Hugging Face Hub Docs

- 项目：[huggingface/hub-docs](https://github.com/huggingface/hub-docs)，Apache-2.0 许可证，仓库仍持续维护。
- 解决的问题：为大量产品文档提供清晰的左侧分组导航、稳定的阅读主列和小屏目录入口。
- 可借鉴：桌面端粘性侧栏、导航先于正文的 DOM 顺序、移动端原生折叠目录，以及内容区不过度铺满宽屏。
- 结论：不复用其 `doc-builder` 代码或依赖。当前页面是既有 Astro 站中的 20 项静态目录，直接复用其分组信息架构比引入第二套文档工具更兼容；最终采用左侧模型名称目录与右侧分类卡片区。

### 国内工具与后续候选

- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) 是活跃的多模型桌面客户端，采用 AGPL-3.0，适合首批桌面客户端教程。许可证必须在教程中显式说明。
- [Dify](https://github.com/langgenius/dify) 适合自托管 AI 工作流，但其许可证包含 Apache 2.0 之外的附加条件；本批不纳入，后续加入时需单独解释商用边界。
- [Coze Studio](https://github.com/coze-dev/coze-studio) 提供 Apache-2.0 的智能体开发平台实现，适合作为后续进阶部署教程候选。
- [ModelScope](https://github.com/modelscope/modelscope) 提供 Apache-2.0 的模型生态和安装方式，适合作为后续国内模型平台候选。

调研结果使第一版保持 Astro 原生实现，不增加文档框架或搜索依赖；同时把许可证、维护状态、费用和数据去向纳入每篇教程的固定信息区。

### 第二批开源项目核对

- [InvokeAI](https://github.com/invoke-ai/InvokeAI) 解决本地扩散模型生成、画布和模型管理问题，采用 Apache-2.0，仓库未归档且在 2026-08 仍活跃；适合普通读者从完整桌面/本地工作区入门，因此取代维护节奏较慢的 Forge 候选。只引用官方安装流程，不复用代码或增加依赖。
- [AUTOMATIC1111 Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 提供经典本地 WebUI，采用 AGPL-3.0，仓库未归档且 2026 年仍有更新；适合讲解本地服务、模型目录和扩展安全，但教程必须提醒扩展可执行代码。
- [Krita AI Diffusion](https://github.com/Acly/krita-ai-diffusion) 把扩散模型接入 Krita，采用 GPL-3.0，2026-08 仍活跃；适合图像编辑而非只生成成品，教程采用官方 Release ZIP 与本地托管后端。
- [Cline](https://github.com/cline/cline) 是可安装到 VS Code 的开源编程代理，采用 Apache-2.0，2026-08 仍活跃；适合说明自选模型、API 成本和工具审批。只把它作为教程对象，不引入扩展依赖。
- [FramePack](https://github.com/lllyasviel/FramePack) 解决消费级 NVIDIA 显卡上的本地视频扩散，采用 Apache-2.0，仓库未归档；其 README 明确 GitHub 是唯一官网，因此教程把仿冒站识别作为首要安全步骤。

这次调研直接形成两项取舍：第二批不加入 Midjourney、即梦、Runway、海螺或 Vidu 等网页优先候选；视频类用剪映专业版、Filmora 和本地 FramePack 覆盖入门剪辑、桌面 AI 后期与本地生成三种路径。

## 首批内容范围

| 工具 | 地区 | 类别 | 主要教程定位 |
| --- | --- | --- | --- |
| Codex | 国际 | AI 编程 | 官方安装、登录、项目授权和第一个编程任务 |
| Cursor | 国际 | AI 编程 | 编辑器安装、项目导入、模型设置和首次修改 |
| Ollama | 国际 | 语言模型 | 安装、拉取模型、本地对话和存储管理 |
| ComfyUI | 国际 | 图片模型 | 环境选择、安装、模型目录和第一个工作流 |
| TRAE | 国内 | AI 编程 | 官方安装、登录、项目导入和首次协作 |
| Cherry Studio | 国内 | 语言模型 | 安装、模型服务配置、首次对话和数据设置 |
| DeepSeek | 国内 | 语言模型 | 官方入口、免安装使用、API 或客户端能力边界 |
| 可灵 AI | 国内 | 视频模型 | 官方入口、账号准备、首次生成和素材导出 |

第二批电脑端范围：

| 工具 | 地区 | 类别 | 电脑端形态 |
| --- | --- | --- | --- |
| ChatGPT Desktop | 国际 | 语言模型 | Windows / macOS 桌面应用 |
| Claude Desktop | 国际 | 语言模型 | Windows / macOS / Linux 桌面应用 |
| Kimi Work | 国内 | 语言模型 | macOS 桌面应用 |
| InvokeAI | 国际 | 图片模型 | 桌面/本地服务 |
| Stable Diffusion WebUI | 国际 | 图片模型 | Windows / macOS / Linux 本地服务 |
| Krita AI Diffusion | 国际 | 图片模型 | Krita 桌面插件与本地服务 |
| GitHub Copilot | 国际 | AI 编程 | 桌面 IDE 扩展 |
| Claude Code | 国际 | AI 编程 | Windows / macOS / Linux CLI |
| Cline | 国际 | AI 编程 | VS Code 桌面扩展 |
| 剪映专业版 | 国内 | 视频模型 | Windows / macOS 桌面应用 |
| Filmora | 国内 | 视频模型 | Windows / macOS 桌面应用 |
| FramePack | 国际 | 视频模型 | Windows / Linux 本地服务 |

教程只覆盖官方实际支持的平台和入口。具体版本号、系统要求、价格与客户端能力在写作和截图当天从官方文档、官方仓库或产品界面核验，不根据记忆补写。

## 信息架构

### 主导航

主导航调整为：

`首页 / 作品 / 学习路线 / 工具指南 / 知识库 / 关于`

「工具指南」指向 `tools.html`。桌面端继续横向展示；移动端沿用现有菜单并验证 6 个导航项不会溢出。

### 首页

首页主体内容保持现状，不增加工具指南卡片、推荐区或统计数字。全站主导航会出现「工具指南」，除此之外首页不提供额外入口。

### 工具目录页

新增 `src/pages/tools.astro`，构建为 `tools.html`，包含：

1. 页面标题与一句面向普通读者的用途说明。
2. 桌面端左侧粘性模型目录，按语言模型、图片模型、AI 编程、视频模型分组列出工具名称；820px 以下改为默认折叠的原生目录。
3. 右侧按同样四类展示 20 张工具卡片，名称目录使用锚点定位；桌面两列、640px 以下单列，卡片显示名称、简述、地区、类别、平台、安装方式和最后核验日期。

目录使用静态锚点，不建立浏览器筛选状态，也不发送网络请求。原生 `details` 在静态 HTML 中保持 `open`，保证无 JavaScript 的桌面端仍能看见目录；脚本仅在小屏首屏将其收起，并在选择工具后收起目录。第一版不提供搜索框。

### 工具详情页

新增 `src/pages/tools/[...slug].astro`，生成 `/tools/{slug}.html`。详情页按固定顺序呈现：

1. 标题、摘要、工具元数据和最后核验日期。
2. 「快速判断」：适合谁、是否需要安装、费用概况、主要隐私提示。
3. 安装前检查或账号准备。
4. 图解安装；免安装产品改为图解进入与账号准备。
5. 第一次使用与一个可复现的小案例。
6. 常见问题与排错。
7. 更新与卸载；网页服务说明账号、缓存或数据管理方式。
8. 费用、隐私、开源状态与许可证。
9. 官方资料与本篇核验日期。

详情页使用新的工具指南布局，并复用现有 `BaseLayout`、页头、页脚、字体、颜色和响应式规则；不把工具教程塞进现有 `ArticleLayout` 的文章系列语义。

## 内容模型

在 `src/content.config.ts` 中新增独立的 `tools` collection，内容位于 `src/content/tools`。建议的必填和可选字段如下：

```yaml
title: Codex 安装与入门
toolName: Codex
description: 从官方安装到完成第一个编程任务。
audience: 想在本地项目中使用 AI 编程助手的读者。
setupSummary: 需要安装命令行工具并登录账号。
privacySummary: 项目内容可能按任务需要发送给云端模型，敏感仓库先确认权限与数据政策。
origin: international
category: ai-coding
accessTypes: [cli]
platforms: [windows, macos, linux]
pricing: freemium
openSource: true
license: Apache-2.0
officialUrl: https://developers.openai.com/codex/
repositoryUrl: https://github.com/openai/codex
versionChecked: "核验时的版本或发布通道"
verifiedAt: 2026-08-26
cover: /assets/tools/codex/cover.webp
coverAlt: Codex 工具指南封面
sequence: 1
draft: false
```

字段约束：

- `origin`：`international` 或 `china`。
- `audience`、`setupSummary`、`privacySummary`：详情页「快速判断」区的三项必填短文本，避免模板根据类别猜测具体工具的使用边界。
- `category`：`language-model`、`image-model`、`ai-coding`、`video-model`。
- `accessTypes`：从 `cli`、`desktop`、`local-service`、`web` 中选择一个或多个。
- `platforms`：从 `windows`、`macos`、`linux`、`web`、`android`、`ios` 中选择一个或多个，只填写官方实际支持项。
- `pricing`：`free`、`freemium`、`paid` 或 `usage-based`。同时存在多种计费方式时正文解释，列表使用最能帮助入门者判断的主标签。
- `openSource` 必填；开源工具的 `license` 和 `repositoryUrl` 必填，闭源产品明确显示「非开源」，不留空造成误解。
- `officialUrl`、`versionChecked`、`verifiedAt`、封面与排序字段必填；下载地址仅在有官方安装包时填写。
- 文件名作为唯一 slug。当前 `sequence` 为 1—20 且不重复。

20 篇正文使用 Markdown 或 MDX，但图片统一使用可检查的站内绝对路径，不能引用会失效的临时外链。

## 图文规范

每篇教程至少 4 张、最多约 6 张核心视觉：

1. 一张 16:9 原创封面。
2. 一张原创安装或访问流程图。
3. 优先使用两至三张真实关键步骤截图；官方页面在当前网络环境不可稳定访问时，改用明确标注“界面结构示意、以官网为准”的原创图解，并保留官方链接，绝不使用第三方镜像或伪造截图。
4. 一张首次使用结果或常见故障示意图。

图片统一存放在 `public/assets/tools/<slug>/`，真实截图优先使用 WebP，原创图解使用可访问 SVG。Frontmatter 封面通过 `withBase()` 生成地址；Markdown 正文图片使用 `/personal-ip-website/assets/tools/...`，适配当前 GitHub Pages 子路径。每张图片必须有描述画面用途的替代文本；每张官方截图后紧邻标注可点击的官方来源链接与截取日期，避免读者把历史截图误认为当前界面。

实施说明：Codex、Cursor、Ollama、ComfyUI 使用公开官方页面截图；TRAE 官网在实施环境连续超时，国内四篇为保持一致与避免失真，使用带“示意、以官网为准”声明的原创中文操作图解。该调整不改变官方资料优先级，也不把图解称为软件实拍界面。

不得凭空生成产品界面。真实截图在官方当前版本中采集；原创封面和流程图可以使用网站现有品牌元素，但不能冒充软件截图。账号、手机号、文件路径、项目名、API Key 和账单信息必须打码或使用专门的演示账号与演示项目。

## 交互设计

- 模型目录使用真实锚点，类别标题和工具名称均可键盘访问；工具名称指向对应卡片的稳定 `id`。
- 移动模型目录使用原生 `details / summary`；摘要与目录链接点击区域不小于 44px，选择工具后自动收起目录。
- 工具卡片保留完整可见标题和文本标签，不只依赖颜色区分地区、类别或费用。
- 代码块在有命令的教程中增加「复制」按钮；复制成功后提供短暂可见状态和屏幕阅读器提示。
- 没有命令行步骤的网页工具不显示无意义的复制按钮。
- 图片声明宽高或使用稳定宽高比，避免页面加载时大幅跳动；移动端图片保持可读，不横向溢出。
- 页面核心信息不依赖 JavaScript；目录或复制脚本失效时，20 张卡片和全部正文仍然可读。

## 数据流与组件边界

1. Astro 的 `tools` collection 在构建时验证 20 篇 frontmatter；第二批必须至少包含 `desktop`、`cli` 或 `local-service` 之一，并支持 Windows、macOS 或 Linux 至少一个系统。
2. `tools.astro` 使用 `getCollection("tools")` 查询公开条目，按 `sequence` 排序并渲染工具卡片。
3. 目录页不使用客户端筛选状态；内联脚本只控制桌面/移动 `details` 的默认展开状态和移动选择后的收起行为。
4. `[...slug].astro` 为每个公开条目生成静态路径，并交给工具指南布局渲染正文。
5. 复制脚本只增强代码块，不修改教程内容。
6. sitemap 自动收录 `tools.html` 与 20 个详情页；现有 RSS 继续只发布知识库文章，避免把安装手册混入内容文章订阅。

不增加数据库、接口、分析埋点或第三方前端依赖。

## 内容可信度、隐私与失败处理

- 资料优先级：官方文档与产品页面，其次是官方 GitHub 仓库和 Releases；第三方文章只能用于发现问题，不能作为安装包来源。
- 每篇写明软件版本或发布通道及 `verifiedAt`。无法确认的价格、平台能力或系统要求不写成确定事实。
- 下载按钮只指向官方站点或官方仓库。若官方链接不可访问，教程解释限制，不提供镜像站替代品。
- 云端工具说明账号、订阅、素材上传和数据离开本机的情况；本地工具说明硬件、磁盘占用、模型来源和联网行为。
- 每篇费用与隐私章节至少链接一项官方隐私、FAQ、服务条款或安全策略；不存在独立隐私页时使用官方安全策略或 FAQ，并说明其适用范围。
- 开源状态按产品和代码仓库区分。例如「模型开放」不等于「在线产品开源」。
- 某一平台步骤没有完成真实验证时，明确标注「参考官方文档，未在本机实测」，不伪装为亲测。
- 图片缺失、元数据不完整或 slug 重复应让测试或构建失败，避免发布半成品页面。

## 测试与验收

### 内容契约

- `tools` collection 恰好有 20 个公开条目，名称与本设计清单一致；第二批没有纯网页条目。
- `sequence` 为不重复的 1—8，slug 唯一。
- 每篇必填字段完整，开源工具包含许可证与仓库地址。
- 每篇至少包含 4 个站内图片引用，所有文件存在且有非空替代文本。
- 每张官方截图后紧邻官方来源链接与截取日期，每篇至少包含一项官方隐私或安全资料链接。
- 每篇包含安装/访问、首次使用、常见问题、费用与隐私、官方资料等固定章节。
- 教程不包含看起来像真实 API Key 的示例密钥或明显的未打码个人信息。

### 页面契约

- `tools.html` 和 20 个 `/tools/{slug}.html` 均生成成功并各有唯一 H1。
- 主导航包含「工具指南」，详情页与目录页的当前导航状态正确。
- 首页主体不出现工具指南推荐入口或 20 款工具卡片；全站主导航中的「工具指南」正常保留。
- 左侧与右侧均有四个分类分组，20 个模型名称链接准确指向对应卡片，分类和工具数量一致。
- 桌面端左侧模型目录粘性可见、右侧同类卡片两列；390px 下目录默认收起、可展开、选择后收起且工具卡单列，无横向溢出。
- 命令代码块可复制；无 JavaScript 时页面内容仍完整可读。
- sitemap 包含工具目录和 20 个详情地址，RSS 条目数量不因工具指南变化。

### 浏览器与构建验证

```bash
npm ci
npm run check
npm test
git diff --check
```

在约 1280px 桌面宽度和 390px 移动宽度检查目录页、至少一篇 CLI 教程、一篇桌面应用教程、一篇 IDE 扩展教程和一篇本地服务教程。目录页检查桌面粘性侧栏、四类分组、20 个名称锚点、两列卡片、移动折叠目录与单列卡片；同时检查导航、定位高亮、复制按钮、图片清晰度、键盘操作、控制台错误和无效链接。

## 文档同步

代码完成时同步更新：

- `docs/README.md`：新增 `tools` collection、路由、资源目录、内容字段和本地验证方法。
- `docs/ops.md`：同步 20 篇工具页、sitemap 数量、电脑端准入规则、图片与官方链接核验流程。
- 现有品牌或信息架构文档（若仓库中存在）：更新主导航顺序，并明确首页不提供工具入口。
- 本设计文档：实施中若有已确认的结构性调整，更新为最终决策，不留下与代码矛盾的描述。

## 完成标准

独立功能分支包含按四类组织的模型名称目录、20 篇完整图文教程、所需图片、锚点定位与复制增强、内容/页面契约测试以及同步后的开发文档。所有 20 篇都标明真实核验日期、官方资料、费用、隐私和开源状态；第二批全部具备电脑端安装方式，首页保持不变。完整构建、自动化测试和桌面/移动浏览器验收通过后，才建议合并到 `main`。
