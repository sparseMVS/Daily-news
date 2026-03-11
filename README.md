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
- **摘要**：ReCoSplat 面向在线新视角合成与顺序场景重建，采用自回归前馈式 Gaussian Splatting，在已知或未知相机位姿条件下都能工作。论文引入 Render-and-Compare 模块，用渲染结果和新观测对齐来减轻位姿预测误差带来的分布偏差，并以混合 KV cache 压缩把长序列缓存成本明显压低。

**2. [VLM-Loc: Localization in Point Cloud Maps via Vision-Language Models](https://arxiv.org/abs/2603.09826)**
- **来源平台**：arXiv
- **子方向**：3D视觉
- **推荐等级**：高
- **摘要**：VLM-Loc 聚焦“文本描述定位到 3D 点云地图”任务，把点云转换为 BEV 图像和场景图后交给视觉语言模型做跨模态空间推理，并通过节点分配机制把文本线索和图结构显式绑定。作者同时发布 CityLoc 基准，对空间理解、语言导航和机器人场景检索都有较强参考价值。

**3. [NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models](https://arxiv.org/abs/2603.09542)**
- **来源平台**：arXiv
- **子方向**：具身智能
- **推荐等级**：高
- **摘要**：NS-VLA 把神经符号方法引入 Vision-Language-Action 模型，试图缓解 VLA 对大规模示范数据和复杂网络结构的依赖。框架通过符号编码器抽取结构化动作原语，再由符号求解器做动作编排，并用在线强化学习扩展探索空间，强调更好的单次训练表现、零样本泛化与抗数据扰动能力。

**4. [DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation](https://arxiv.org/abs/2603.09121)**
- **来源平台**：arXiv
- **子方向**：具身智能
- **推荐等级**：高
- **摘要**：DexHiL 面向灵巧操作里的 VLA 后训练，把人类在执行过程中的即时纠错纳入臂手协同系统，并设计干预感知的数据采样策略，优先学习真正暴露失败模式的片段。论文给出真实机器人实验结果，说明“人类轻量介入 + 后训练”能够更快把通用 VLA 调到复杂接触任务上。

**5. [PlayWorld: Exploratory Autoregressive Visual World Models with Playful Interventions](https://jacobjj.github.io/playworld/)**
- **来源平台**：Project Page
- **子方向**：世界模型
- **推荐等级**：高
- **摘要**：PlayWorld 把“先探索、后建模”作为世界模型训练核心，让智能体在仿真环境中通过 playful interventions 主动制造状态变化，再学习自回归视觉世界模型。项目页强调这种 agent-centric 建模更有利于把决策相关动态与静态背景解耦，对规划、控制和仿真迁移都更有意义。

### 行业新闻 / 产品动态

暂无相关内容。

### 一手动态

暂无相关内容。

## 2026-03-10

### 论文 / 技术报告

暂无相关内容。

### 行业新闻 / 产品动态

暂无相关内容。

### 一手动态

**1. [Automated Vehicle Safety Public Meeting](https://www.nhtsa.gov/event/automated-vehicle-safety-public-meeting)**
- **来源平台**：NHTSA
- **子方向**：自动驾驶
- **推荐等级**：中
- **摘要**：美国国家公路交通安全管理局在 2026-03-10 举办自动驾驶安全公开会议，议题覆盖事故数据、监管证据、部署责任和公众安全沟通。虽然它不是产品发布，但这是判断美国监管层如何审视 robotaxi、干线物流自动驾驶和测试扩张节奏的重要一手信号。

## 2026-03-09

### 论文 / 技术报告

暂无相关内容。

### 行业新闻 / 产品动态

**1. [WeRide and Geely Farizon to Launch World's First Level-4 Autonomous Van](https://www.weride.ai/news/1105)**
- **来源平台**：WeRide
- **子方向**：自动驾驶
- **推荐等级**：高
- **摘要**：文远知行与吉利远程在 2026-03-09 宣布将推出 Level-4 自动驾驶货运车，把自动驾驶能力从 robotaxi 进一步推进到城市物流车型。公开信息给出了合作方、车型方向和落地场景，说明自动驾驶商业化正在从单点示范转向更明确的运营载体与量产协同。

**2. [ABB and NVIDIA to develop AI systems for smart factories](https://global.abb/group/en/media/press-releases/2026/03/abb-and-nvidia-to-develop-ai-systems-for-smart-factories)**
- **来源平台**：ABB
- **子方向**：AI robotics
- **推荐等级**：高
- **摘要**：ABB 与 NVIDIA 于 2026-03-09 宣布扩展合作，把生成式 AI、数字孪生和 Omniverse 接入工业机器人与工厂运维体系。它的价值不在单一模型发布，而在于 physical AI 正通过仿真、视觉感知和制造执行系统的结合，更快进入真实工业流程。

**3. [NEURA Robotics and Qualcomm Technologies, Inc. announce strategic collaboration to power cognitive robots](https://www.qualcomm.com/news/releases/2026/03/neura-robotics-and-qualcomm-technologies--inc--announce-str)**
- **来源平台**：Qualcomm
- **子方向**：具身智能
- **推荐等级**：中
- **摘要**：NEURA Robotics 与高通在 2026-03-09 公布战略合作，计划将 Qualcomm Dragonwing 平台用于认知机器人系统，重点覆盖边缘算力、感知推理和系统级集成。这条消息的重要性在于，它展示了“机器人本体厂商 + 芯片平台”正加速围绕认知机器人构建可量产的软件硬件栈。

### 一手动态

**1. [Inside Zoox's Secret Approach to Mapping New Cities](https://zoox.com/journal/inside-zooxs-secret-approach-to-mapping-new-cities)**
- **来源平台**：Zoox
- **子方向**：自动驾驶
- **推荐等级**：中
- **摘要**：Zoox 官方文章披露了其进入新城市前的地图采集、道路规则建模和验证流程，核心是先建立高质量地图和场景先验，再逐步推进真实道路验证。相比媒体报道，这类一手材料更能补足自动驾驶公司扩城背后的技术运营方法论，对判断其复制能力和落地成本很有参考价值。

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
