# 每周新闻汇总

自动汇总的 AI 前沿技术新闻索引。

## 最新周报

# AI前沿技术简报

## 2026-03-11

### 论文 / 技术报告

**1. [ReCoSplat: Autoregressive Feed-Forward Gaussian Splatting Using Render-and-Compare](https://arxiv.org/abs/2603.09968)**
- **来源平台**：arXiv
- **子方向**：3D视觉
- **推荐等级**：高
- **摘要**：ReCoSplat 面向在线新视角合成与顺序场景重建，采用自回归前馈式 Gaussian Splatting，在已知或未知相机位姿、内参条件下都能工作。论文引入 Render-and-Compare 模块，用预测视角下的渲染结果和新观测对齐，缓解训练时真值位姿与推理时预测位姿之间的分布偏差，并用混合 KV cache 压缩把长序列缓存成本压低 90% 以上。

**2. [VLM-Loc: Localization in Point Cloud Maps via Vision-Language Models](https://arxiv.org/abs/2603.09826)**
- **来源平台**：arXiv
- **子方向**：3D视觉
- **推荐等级**：高
- **摘要**：VLM-Loc 聚焦“文本描述定位到 3D 点云地图”这一任务，把点云转换成 BEV 图像和场景图后交给视觉语言模型做跨模态空间推理，并通过部分节点分配机制把文本线索和图结构显式绑定。作者同时发布 CityLoc 基准，覆盖多源点云场景。对空间理解、语言导航和机器人场景检索方向都有较强参考价值。

**3. [NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models](https://arxiv.org/abs/2603.09542)**
- **来源平台**：arXiv
- **子方向**：具身智能
- **推荐等级**：高
- **摘要**：NS-VLA 把神经符号方法引入 Vision-Language-Action 模型，试图解决 VLA 对大规模示范数据和复杂网络结构依赖过强的问题。框架通过符号编码器抽取结构化动作原语，再由符号求解器做高效动作编排，并用在线强化学习扩展探索空间。论文在机器人操作基准上强调更好的单次训练表现、零样本泛化和抗数据扰动能力。

**4. [DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation](https://arxiv.org/abs/2603.09121)**
- **来源平台**：arXiv
- **子方向**：具身智能
- **推荐等级**：高
- **摘要**：DexHiL 关注灵巧操作里的 VLA 后训练，把人类在执行过程中的即时纠错纳入臂手协同系统，并设计干预感知的数据采样策略，优先学习真正暴露失败模式的片段。论文给出真实机器人实验结果，平均任务成功率比单纯离线微调高出约 25%，对“如何把通用 VLA 调到具体硬件和复杂接触任务上”很有现实意义。

**5. [How to Think in Latent Space: Structured Cognitive Prompting for World Models](https://arxiv.org/abs/2603.09736)**
- **来源平台**：arXiv
- **子方向**：世界模型
- **推荐等级**：中
- **摘要**：这篇工作把关注点放在世界模型的潜空间推理过程，提出 structured cognitive prompting，希望在不显式展开高成本像素轨迹的前提下，把规划、状态演化和策略选择转化为更结构化的潜变量思考流程。公开信息目前主要来自搜索摘要，但方向上契合“让 world model 更可控、更可解释地服务决策”的近期趋势。（来自搜索摘要）

### 行业新闻 / 产品动态

**1. [Genesis AI Launches With $105 Million To Build A Universal Robotics Foundation Model And Horizontal Robotics Platform](https://www.prnewswire.com/apac/news-releases/genesis-ai-launches-with-105-million-to-build-a-universal-robotics-foundation-model-and-horizontal-robotics-platform-302396516.html)**
- **来源平台**：PR Newswire
- **子方向**：具身智能
- **推荐等级**：中
- **摘要**：Genesis AI 于 2026-03-11 宣布完成 1.05 亿美元融资，定位为通用机器人基础模型与横向机器人平台公司，叙事重点放在以物理引擎、合成数据和基础模型支撑跨机器人形态迁移。虽然目前公开信息偏公司公告口径，但它反映资本市场仍在持续押注 physical AI 与通用机器人软件栈的基础设施机会。

**2. [Luminous Ventures launches $63 million fund to back AI “supercycle” at seed stage](https://tech.eu/2026/03/11/luminous-ventures-launches-63-million-fund-to-back-ai-supercycle-at-seed-stage/)**
- **来源平台**：tech.eu
- **子方向**：AI robotics
- **推荐等级**：低
- **摘要**：tech.eu 报道 Luminous Ventures 推出 6300 万美元新基金，投资方向覆盖 AI、机器人和相关基础设施。它不是直接的产品发布，但能作为行业侧信号，说明早期资本对“AI 与机器人结合”仍保持积极配置意愿。对观察具身智能融资环境、创业窗口和欧洲市场温度有一定辅助价值。

### 一手动态

暂无相关内容。

## 2026-03-10

### 论文 / 技术报告

暂无相关内容。

### 行业新闻 / 产品动态

**1. [Anthropic opens first office in Asia Pacific, boosting AI collaboration and innovation](https://www.anthropic.com/news/anthropic-opens-first-office-in-asia-pacific-boosting-ai-collaboration-and-innovation)**
- **来源平台**：Anthropic
- **子方向**：大模型
- **推荐等级**：中
- **摘要**：Anthropic 于 2026-03-10 宣布在悉尼设立其首个亚太办公室，重点面向本地研究合作、企业采用和政策沟通。虽然这不是新模型发布，但它反映头部大模型公司正加快区域化落地与商业网络建设，侧面说明模型服务和合规支持正在向全球市场进一步延展。

### 一手动态

**1. [Use Gemini in Google Workspace to stay in the flow of work](https://workspace.google.com/blog/product-announcements/use-gemini-in-google-workspace-to-stay-in-the-flow-of-work)**
- **来源平台**：Google Workspace Blog
- **子方向**：大模型
- **推荐等级**：中
- **摘要**：Google Workspace 官方博客在 2026-03-10 更新 Gemini 办公流能力，强调在文档、邮件和协作场景内更连续地调用模型辅助生成、检索与整理功能。它不属于底座模型升级，但反映大模型产品竞争正从参数规模转向工作流渗透、用户留存和实际协同效率。

## 2026-03-09

### 论文 / 技术报告

暂无相关内容。

### 行业新闻 / 产品动态

**1. [Zoox is mapping more cities as it expands robotaxi tests](https://techcrunch.com/2026/03/09/zoox-is-mapping-more-cities-as-it-expands-robotaxi-tests/)**
- **来源平台**：TechCrunch
- **子方向**：自动驾驶
- **推荐等级**：高
- **摘要**：TechCrunch 于 2026-03-09 报道，Zoox 正把机器人出租车测试的测绘和验证工作扩展到更多美国城市，为后续商用部署铺路。相较单次演示，这类“先测绘、再验证、再放量”的城市扩张节奏更能反映自动驾驶公司真实的运营推进情况和监管沟通成熟度。

### 一手动态

**1. [Inside Zoox's Secret Approach to Mapping New Cities](https://zoox.com/journal/inside-zooxs-secret-approach-to-mapping-new-cities)**
- **来源平台**：Zoox
- **子方向**：自动驾驶
- **推荐等级**：高
- **摘要**：Zoox 官网文章披露了其进入新城市前的测绘方法论，核心在于先构建高质量地图和场景先验，再逐步推进真实道路验证。这类一手材料虽然不会给出完整商业指标，但能补足媒体报道没有展开的技术运营细节，对判断自动驾驶扩张路径是否可复制很有帮助。

## 上周周报

# AI前沿技术简报

## 2026-03-08

### 论文 / 技术报告

**1. [ReconDrive: Fast Feed-Forward 4D Gaussian Splatting for Autonomous Driving Scene Reconstruction](https://arxiv.org/abs/2603.07552)**
- **来源平台**：arXiv
- **子方向**：3D视觉
- **推荐等级**：高
- **摘要**：ReconDrive 面向自动驾驶闭环评测中的高保真场景重建，提出基于 VGGT 扩展的前馈式 4D Gaussian Splatting 框架，通过静态-动态 4D 组合与混合高斯预测头，在 nuScenes 上兼顾重建质量、视角合成与推理速度，为大规模城市驾驶仿真提供更可扩展的三维场景表示。

### 行业新闻 / 产品动态

暂无相关内容。

### 一手动态

暂无相关内容。

## 全部周报

- [2026-03-09.md](./每周新闻汇总/2026-03-09.md)：包含 2026-03-09 至 2026-03-11 的内容
- [2026-03-02.md](./每周新闻汇总/2026-03-02.md)：包含 2026-03-08 至 2026-03-08 的内容
