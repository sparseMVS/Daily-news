# 每周新闻汇总

自动汇总的 AI 前沿技术新闻索引。

## 最新周报

# AI前沿技术简报

## 2026-03-11

### 论文 / 技术报告

**1. [MXFP4: Micro-Scaling FP4 for Efficiently Serving 8x Larger Models with Minimal Accuracy Loss](https://arxiv.org/abs/2603.08713)**
- **来源平台**：arXiv
- **子方向**：大模型
- **推荐等级**：高
- **摘要**：这篇论文聚焦大模型推理基础设施，提出 MXFP4 微缩放 4-bit 浮点格式，希望在精度损失可控的前提下，把可服务模型规模提升到原来的约 8 倍。若结果稳定，它会直接影响大模型部署成本、显存占用和在线服务吞吐，是近期较有工程价值的系统优化信号。

**2. [Comparative Analysis of Patch Attack on VLM-Based Autonomous Driving Architectures](https://arxiv.org/abs/2603.08897)**
- **来源平台**：arXiv
- **子方向**：自动驾驶
- **推荐等级**：中
- **摘要**：该工作比较了视觉语言模型驱动自动驾驶架构在补丁攻击下的脆弱性差异，重点分析感知输入被局部扰动后，对规划与控制链路造成的连锁影响。它不是直接提升性能的论文，但对端到端自动驾驶系统的安全评测、鲁棒训练和上线门槛有现实参考价值。

**3. [EvoDriveVLA: Evolving Vision-Language-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2603.09465)**
- **来源平台**：arXiv
- **子方向**：自动驾驶
- **推荐等级**：高
- **摘要**：EvoDriveVLA 把 Vision-Language-Action 框架引入端到端自动驾驶，希望统一处理场景理解、驾驶意图表达与控制决策，并通过演化式训练改进复杂路况下的泛化表现。该方向延续了“大模型化驾驶栈”的趋势，值得持续跟踪其数据效率和真实路测表现。

### 行业新闻 / 产品动态

暂无相关内容。

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
