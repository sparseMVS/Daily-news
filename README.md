# 每周新闻汇总

自动汇总的 AI 前沿技术新闻索引。

## 最新周报

### 2026-03-16

#### 论文 / 技术报告

**1. [FLEXEVAL: A Flexible and Configurable Evaluation Framework for Foundation Models](https://arxiv.org/abs/2603.12778)**
- **来源平台**：arXiv
- **子方向**：大模型
- **推荐等级**：高
- **摘要**：FLEXEVAL 试图为 foundation models 提供更灵活、可配置的统一评测框架，把任务、指标和评测协议抽象成可组合模块。它的价值在于降低大模型评测碎片化和结果难复现的问题，让研究者和工程团队更容易建立一致的比较基线。

**2. [A Portable Plug-and-Play Weather Forecasting System Based on Large Language Models and External Weather Models](https://arxiv.org/abs/2603.12695)**
- **来源平台**：arXiv
- **子方向**：天气预测
- **推荐等级**：高
- **摘要**：这篇工作提出可移植、可插拔的天气预测系统，把大语言模型与外部天气模型结合，试图在不同区域、不同数据条件下保持更稳定的预报能力。它的意义不只是把 LLM 接进气象流程，而是探索“通用语言推理 + 专业天气模型”协同工作的实际工程路径。

**3. [DRIVE-EVAL: A Multi-Level Evaluation Suite for Autonomous Driving Foundation Models](https://arxiv.org/abs/2603.12657)**
- **来源平台**：arXiv
- **子方向**：自动驾驶
- **推荐等级**：高
- **摘要**：DRIVE-EVAL 围绕自动驾驶 foundation model 设计多层级评测套件，希望把感知、规划、行为理解和安全性评估纳入统一框架。对端到端驾驶和多模态驾驶模型来说，这类系统化评测基座很重要，因为它能缓解“模型很强但难以横向比较”的现实问题。

**4. [AutoDriveVLM: Robustifying Vision-Language Models for Complex Lane Changes in Autonomous Driving](https://arxiv.org/abs/2603.12542)**
- **来源平台**：arXiv
- **子方向**：自动驾驶
- **推荐等级**：中
- **摘要**：AutoDriveVLM 聚焦自动驾驶中的复杂变道决策，尝试提升视觉语言模型在密集交通、遮挡和多车交互条件下的鲁棒性。虽然它仍偏研究阶段，但方向很明确，就是把 VLM 从“看懂路况”进一步推进到“在高风险动作上做出更稳判断”。

#### 行业新闻 / 产品动态

**1. [Meta Delays New AI Model Again as It Weighs Google Tie-Up, Report Says](https://www.barrons.com/articles/meta-delays-new-ai-model-again-as-it-weighs-google-tie-up-report-says-865247d4)**
- **来源平台**：Barron's
- **子方向**：大模型
- **推荐等级**：中
- **摘要**：Barron's 在 2026-03-14 援引媒体报道，称 Meta 再次推迟新模型 “Avocado”，并在评估是否引入 Google Gemini 作为部分能力支持。即便仍属报道阶段，这条消息也反映出头部模型厂商在发布时间、能力达标和外部能力整合之间的压力正在加大。（来自搜索摘要）

**2. [Cerebras and Perplexity deploy Qwen3-235B, one of the world’s most advanced open-source models, across U.S. data centers](https://www.cerebras.ai/blog/cerebras-and-perplexity-deploy-qwen3-235b-one-of-the-worlds-most-advanced-open-source-models-across-us-data-centers)**
- **来源平台**：Cerebras
- **子方向**：大模型
- **推荐等级**：高
- **摘要**：Cerebras 与 Perplexity 宣布在美国数据中心部署 Qwen3-235B，把高参数开源模型与高速推理基础设施直接绑定。它的信号价值在于，行业竞争点正在从“谁有模型”快速转向“谁能把大模型以更低时延和更稳定成本交付成服务”。

**3. [Waabi announces that Volvo Autonomous Solutions is expanding its commercialization with integrated Waabi Driver to transform the AV trucking industry](https://waabi.ai/waabi-announces-that-volvo-autonomous-solutions-is-expanding-its-commercialization-with-integrated-waabi-driver-to-transform-the-av-trucking-industry/)**
- **来源平台**：Waabi
- **子方向**：自动驾驶
- **推荐等级**：高
- **摘要**：Waabi 宣布 Volvo Autonomous Solutions 将在自动驾驶卡车商业化路径中整合 Waabi Driver，把仿真、驾驶模型和量产卡车平台进一步结合。对自动驾驶行业来说，这类“软件栈进入真实商用车型”的进展，比单纯演示更能反映落地成熟度和量产节奏。

**4. [PowerAI and Midcontinent launch AI-powered load forecasting solution](https://www.poweraitech.com/news/powerai-and-midcontinent-launch-ai-powered-load-forecasting-solution-to-help-electricity-providers-weather-extreme-weather-and-risk/)**
- **来源平台**：PowerAI
- **子方向**：电力预测
- **推荐等级**：中
- **摘要**：PowerAI 与 Midcontinent 推出 AI 负荷预测方案，重点面向极端天气和电网风险场景，帮助电力运营方提升负荷预测、调度准备和韧性响应能力。这类产品化动作说明能源 AI 的价值正在从单点建模扩展到更贴近真实运营决策的工作流里。

**5. [WeatherAI and Howso collaborate to improve weather forecasting with causal AI](https://www.weatheraitech.com/news/weatherai-and-howso-combine-causal-ai-and-advanced-weather-modeling-for-more-accurate-weather-forecasting/)**
- **来源平台**：WeatherAI
- **子方向**：天气预测
- **推荐等级**：中
- **摘要**：WeatherAI 与 Howso 宣布把因果 AI 与天气建模结合，用来提升复杂天气场景下的预报准确率。它值得关注的地方在于，气象 AI 的商业化叙事正在从单纯拟合精度转向“更可解释、更可泛化”的建模能力，这对高风险天气应用很关键。

#### 一手动态

暂无相关内容。

## 上周周报

### 2026-03-14

#### 论文 / 技术报告

暂无相关内容。

#### 行业新闻 / 产品动态

**1. [Meta Delays New AI Model Again as It Weighs Google Tie-Up, Report Says](https://www.barrons.com/articles/meta-delays-new-ai-model-again-as-it-weighs-google-tie-up-report-says-865247d4)**
- **来源平台**：Barron's
- **子方向**：大模型
- **推荐等级**：中
- **摘要**：Barron's 在 2026-03-14 援引媒体报道，称 Meta 再次推迟新模型 “Avocado”，并在评估是否引入 Google Gemini 作为部分能力支持。该消息虽非官方发布，但反映头部厂商在发布时间和能力达标上的现实压力。（来自搜索摘要）

#### 一手动态

暂无相关内容。

### 2026-03-13

#### 论文 / 技术报告

暂无相关内容。

#### 行业新闻 / 产品动态

**1. [Welcome Pollen Robotics to Hugging Face](https://huggingface.co/blog/welcome-pollen-robotics)**
- **来源平台**：Hugging Face
- **子方向**：AI robotics
- **推荐等级**：高
- **摘要**：Hugging Face 在 2026-03-13 宣布收购开源人形机器人公司 Pollen Robotics，并表示将 Reachy 2 与 LeRobot、Hub 分发体系和开源模型生态进一步整合，显示开源模型平台正在向“模型+机器人本体”联动扩展。

**2. [Tesla's Grand Plan for Its Cybercab Sparks Mixed Reactions From Investors](https://www.wsj.com/business/autos/teslas-grand-plan-for-its-cybercab-sparks-mixed-reactions-from-investors-6d67d29a)**
- **来源平台**：The Wall Street Journal
- **子方向**：自动驾驶
- **推荐等级**：中
- **摘要**：华尔街日报在 2026-03-13 报道，特斯拉 Cybercab 商业化计划引发投资者分歧，争论集中于量产节奏、无方向盘方案与 Robotaxi 规模化兑现路径，体现自动驾驶关注点正从演示走向商业可执行性。（来自搜索摘要）

**3. [Travis Kalanick launches a new company called Atoms to build an AI-based operating system for restaurants](https://techcrunch.com/2026/03/13/travis-kalanick-launches-a-new-company-called-atoms-to-build-an-ai-based-operating-system-for-restaurants/)**
- **来源平台**：TechCrunch
- **子方向**：AI robotics
- **推荐等级**：中
- **摘要**：TechCrunch 报道 Travis Kalanick 创立 Atoms，定位面向餐饮场景的 AI 操作系统，强调把软件自动化与门店执行能力结合。该动作代表垂直行业开始把 AI 从“工具层”推进到“运营系统层”。

**4. [Ford’s new AI assistant helps customers find vehicle info](https://techcrunch.com/2026/03/13/fords-new-ai-assistant-helps-customers-find-vehicle-info/)**
- **来源平台**：TechCrunch
- **子方向**：自动驾驶
- **推荐等级**：中
- **摘要**：TechCrunch 报道福特上线面向车主的 AI 助手，用于检索车辆功能和用车信息，说明传统车企在将生成式 AI 融入售后服务和用户交互方面持续提速。

**5. [Zendesk acquires AI-powered quality management startup Klaus](https://techcrunch.com/2026/03/13/zendesk-acquires-ai-powered-quality-management-startup-klaus/)**
- **来源平台**：TechCrunch
- **子方向**：其他
- **推荐等级**：中
- **摘要**：TechCrunch 报道 Zendesk 收购 AI 质检公司 Klaus，以补强客服场景下的自动评估与质量管理。此举反映企业软件厂商通过并购加快 Agent 与自动化能力拼图。

**6. [xAI shifts three top members of technical staff into management roles](https://techcrunch.com/2026/03/13/xai-shifts-three-top-members-of-technical-staff-into-management-roles/)**
- **来源平台**：TechCrunch
- **子方向**：大模型
- **推荐等级**：中
- **摘要**：TechCrunch 报道 xAI 将三名核心技术人员调整至管理岗位，显示公司从技术攻坚向组织扩张与产品化推进并行转变，这通常是头部模型公司进入新阶段的组织信号。

#### 一手动态

暂无相关内容。

### 2026-03-12

#### 论文 / 技术报告

暂无相关内容。

#### 行业新闻 / 产品动态

**1. [SLAMcore secures $17M Series A to scale its spatial intelligence platform, accelerating global growth](https://www.slamcore.com/news/slamcore-secures-17m-series-a-to-scale-its-spatial-intelligence-platform-accelerating-global-growth)**
- **来源平台**：SLAMcore
- **子方向**：3D视觉
- **推荐等级**：高
- **摘要**：SLAMcore 在 2026-03-12 宣布完成 1700 万美元 A 轮融资，表示将继续扩展其 spatial intelligence 平台，把视觉定位、空间理解与机器人和自动化部署结合起来。它的信号价值在于，围绕 SLAM、空间感知与边缘智能的基础能力，仍在持续获得产业资金支持与场景验证。

#### 一手动态

暂无相关内容。

### 2026-03-11

#### 论文 / 技术报告

**1. [ReCoSplat: Autoregressive Feed-Forward Gaussian Splatting Using Render-and-Compare](https://arxiv.org/abs/2603.09968)**
- **来源平台**：arXiv
- **子方向**：3D视觉
- **推荐等级**：高
- **摘要**：ReCoSplat 面向在线新视角合成与顺序场景重建，采用自回归前馈式 Gaussian Splatting，并通过 Render-and-Compare 缓解位姿预测误差带来的训练分布偏差。作者还引入混合 KV cache 压缩机制，降低长序列缓存成本，对实时 3D 场景更新和机器人视觉建图都有较强参考价值。

**2. [VLM-Loc: Localization in Point Cloud Maps via Vision-Language Models](https://arxiv.org/abs/2603.09826)**
- **来源平台**：arXiv
- **子方向**：3D视觉
- **推荐等级**：高
- **摘要**：VLM-Loc 聚焦“自然语言描述定位到 3D 点云地图”任务，把点云转换为 BEV 图像和场景图，再交给视觉语言模型做跨模态空间推理。论文同时发布 CityLoc 基准，把文本空间理解、机器人检索和点云语义定位连接起来，对空间智能和语言导航都很关键。

**3. [RAE-NWM: Navigation World Model in Dense Visual Representation Space](https://arxiv.org/abs/2603.09241)**
- **来源平台**：arXiv
- **子方向**：世界模型
- **推荐等级**：高
- **摘要**：RAE-NWM 试图把 Representation Autoencoder 与神经世界模型结合，在稠密视觉表征空间中统一处理视频预测、奖励建模和导航规划。它的核心价值在于不再只依赖像素级重建，而是直接在更紧凑、更语义化的潜空间里推进预测控制，有望提升世界模型的可用性与规划效率。

**4. [PlayWorld: Exploratory Autoregressive Visual World Models with Playful Interventions](https://arxiv.org/abs/2603.09030)**
- **来源平台**：arXiv
- **子方向**：世界模型
- **推荐等级**：高
- **摘要**：PlayWorld 把“先探索、后建模”作为世界模型训练核心，让智能体通过 playful interventions 主动制造状态变化，再学习自回归视觉世界模型。相比被动视频建模，这种 agent-centric 路线更强调决策相关动态，对后续规划、控制和仿真迁移都更有实际意义。

**5. [NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models](https://arxiv.org/abs/2603.09542)**
- **来源平台**：arXiv
- **子方向**：具身智能
- **推荐等级**：高
- **摘要**：NS-VLA 把神经符号方法引入 Vision-Language-Action 模型，希望缓解 VLA 对大规模示范数据和纯黑盒网络结构的依赖。框架通过符号编码器抽取动作原语，再由符号求解器做动作编排，并结合在线强化学习扩展探索空间，重点强调更好的数据效率与零样本泛化。

**6. [DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation](https://arxiv.org/abs/2603.09121)**
- **来源平台**：arXiv
- **子方向**：具身智能
- **推荐等级**：高
- **摘要**：DexHiL 面向灵巧操作中的 VLA 后训练，把人类执行过程中的即时纠错纳入臂手协同系统，并设计干预感知的数据采样策略，优先学习暴露失败模式的关键片段。真实机器人实验显示，这种“人类轻量介入 + 后训练”路线能更快把通用 VLA 调整到复杂接触任务上。

**7. [TiPToP: Task-Driven Iterative Point Prompting for Robot Object Manipulation](https://arxiv.org/abs/2603.09051)**
- **来源平台**：arXiv
- **子方向**：具身智能
- **推荐等级**：高
- **摘要**：TiPToP 针对机器人操作里的关键接触区域选择问题，提出任务驱动的迭代点提示机制，让模型在点云中逐步聚焦对抓取、接触和位姿调整最有价值的区域。它把三维几何感知与任务目标显式对齐，对减少无效感知计算和提升操作稳定性都很有帮助。

**8. [GST-VLA: Dynamic Gaussian Splatting and Task-Aware Token Pruning in Vision-Language-Action Models](https://arxiv.org/abs/2603.08272)**
- **来源平台**：arXiv
- **子方向**：具身智能
- **推荐等级**：中
- **摘要**：GST-VLA 尝试把动态 Gaussian Splatting 表征接入 Vision-Language-Action 模型，并用任务感知 token pruning 压缩视觉输入计算量。论文关注点不只是提速，而是在保持动作性能的同时增强 VLA 的时空表征效率，对资源受限的具身部署场景有探索价值。

**9. [Emerging Extrinsic Dexterity in Robots via Reinforcement Learning and Morphological Computation](https://arxiv.org/abs/2603.08093)**
- **来源平台**：arXiv
- **子方向**：具身智能
- **推荐等级**：高
- **摘要**：这篇工作研究如何通过强化学习与 morphological computation 共同塑造“外在灵巧性”，即不仅依赖末端执行器本身，还利用本体结构与环境接触来完成复杂操作。它对低成本机器人如何获得更强操作能力给出了一条很有启发性的设计路线。

**10. [APPLV: Adaptive Planning for Embodied Task-Driven Large Vision-Language Models](https://arxiv.org/abs/2603.07931)**
- **来源平台**：arXiv
- **子方向**：具身智能
- **推荐等级**：中
- **摘要**：APPLV 让大型视觉语言模型直接预测经典规划器参数，再与任务驱动控制栈组合完成具身导航和执行。它的价值在于把大模型语义理解能力和传统规划器的可解释性、安全约束结合起来，为“VLM 负责高层决策、规划器负责可执行控制”的路线补了一层自适应桥接。

#### 行业新闻 / 产品动态

**1. [SBVA invests $30 million in Yann LeCun-founded AMI to pioneer the era of world models](https://www.prnewswire.com/news-releases/sbva-invests-30-million-in-yann-lecunfounded-ami-to-pioneer-the-era-of-world-models-302709070.html)**
- **来源平台**：PR Newswire
- **子方向**：世界模型
- **推荐等级**：高
- **摘要**：SBVA 在 2026-03-11 宣布向 Yann LeCun 联合创立的 AMI 投资 3000 万美元，主题直接指向 world models。对行业而言，这条消息的含义不只是融资规模，而是资本开始明确把“环境建模 + agent 基础设施”视为下一轮 AI 平台竞争的重要方向，具备较强信号价值。

**2. [Genesis AI Hires Former Amazon Leader Vivian Sun to Advance Commercialization](https://www.prnewswire.com/news-releases/genesis-ai-hires-former-amazon-leader-vivian-sun-to-advance-commercialization-302709847.html)**
- **来源平台**：PR Newswire
- **子方向**：AI robotics
- **推荐等级**：中
- **摘要**：Genesis AI 宣布引入前亚马逊高管 Vivian Sun 负责商业化推进，重点不在算法细节，而在于它反映了 physical AI 和通用机器人公司正在从技术展示走向客户、渠道和交付能力搭建。对 AI robotics 赛道来说，这类组织动作往往是量产与商业落地前的早期信号。

**3. [Strategic LiDAR Customer Ramps Remote Sensing Production with Sivers Semiconductors Technology](https://www.prnewswire.com/news-releases/strategic-lidar-customer-ramps-remote-sensing-production-with-sivers-semiconductors-technology-302710793.html)**
- **来源平台**：PR Newswire
- **子方向**：3D视觉
- **推荐等级**：低
- **摘要**：Sivers 在 2026-03-11 披露其战略 LiDAR 客户已进入远程感知量产爬坡阶段，虽然公告未公开终端客户名称与整机方案，但这类硬件链条的出货信号仍值得记录。它说明 3D 感知基础设施的需求正在恢复，对空间感知和机器人视觉生态属于补充性行业线索。

**4. [Hoverfly Technologies and Overland AI Expand Collaboration to Deliver Integrated Air-Ground Unmanned Capabilities](https://www.prnewswire.com/news-releases/hoverfly-technologies-and-overland-ai-expand-collaboration-to-deliver-integrated-airground-unmanned-capabilities-302711043.html)**
- **来源平台**：PR Newswire
- **子方向**：AI robotics
- **推荐等级**：低
- **摘要**：Hoverfly 与 Overland AI 扩大合作，把系留无人机感知与地面自主导航能力做系统级联动，面向空地一体化无人系统。它不是通用模型发布，但属于具身智能与自主机器人在特种作业场景中的真实部署信号，适合作为行业跟踪条目保留。

#### 一手动态

暂无相关内容。

### 2026-03-10

#### 论文 / 技术报告

暂无相关内容。

#### 行业新闻 / 产品动态

暂无相关内容。

#### 一手动态

**1. [Automated Vehicle Safety Public Meeting](https://www.nhtsa.gov/event/automated-vehicle-safety-public-meeting)**
- **来源平台**：NHTSA
- **子方向**：自动驾驶
- **推荐等级**：中
- **摘要**：美国国家公路交通安全管理局在 2026-03-10 举办自动驾驶安全公开会议，议题覆盖事故数据、监管证据、部署责任和公众安全沟通。虽然它不是产品发布，但这是判断美国监管层如何审视 robotaxi、干线物流自动驾驶和测试扩张节奏的重要一手信号。

### 2026-03-09

#### 论文 / 技术报告

暂无相关内容。

#### 行业新闻 / 产品动态

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

#### 一手动态

**1. [Inside Zoox's Secret Approach to Mapping New Cities](https://zoox.com/journal/inside-zooxs-secret-approach-to-mapping-new-cities)**
- **来源平台**：Zoox
- **子方向**：自动驾驶
- **推荐等级**：中
- **摘要**：Zoox 官方文章披露了其进入新城市前的地图采集、道路规则建模和验证流程，核心是先建立高质量地图和场景先验，再逐步推进真实道路验证。相比媒体报道，这类一手材料更能补足自动驾驶公司扩城背后的技术运营方法论，对判断其复制能力和落地成本很有参考价值。

## 全部周报

- [2026-03-16.md](./每周新闻汇总/2026-03-16.md)：包含 2026-03-16 至 2026-03-16 的内容
- [2026-03-09.md](./每周新闻汇总/2026-03-09.md)：包含 2026-03-09 至 2026-03-14 的内容
- [2026-03-02.md](./每周新闻汇总/2026-03-02.md)：包含 2026-03-08 至 2026-03-08 的内容
