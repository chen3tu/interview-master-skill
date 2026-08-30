# Interview Master 🎯

**全流程面试准备与求职决策系统** — 一个面向 Claude AI 的 Skill，帮助求职者从岗位分析到拿下 Offer 的每一步。

[![Release](https://img.shields.io/github/v/release/chen3tu/interview-master-skill?display_name=tag)](https://github.com/chen3tu/interview-master-skill/releases/latest)
[![Validate](https://github.com/chen3tu/interview-master-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/chen3tu/interview-master-skill/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/chen3tu/interview-master-skill)](LICENSE)
[![Stars](https://img.shields.io/github/stars/chen3tu/interview-master-skill?style=flat)](https://github.com/chen3tu/interview-master-skill/stargazers)
[![Forks](https://img.shields.io/github/forks/chen3tu/interview-master-skill?style=flat)](https://github.com/chen3tu/interview-master-skill/forks)

## 这是什么？

Interview Master 是一个基于 [Claude](https://claude.ai) 的 AI Skill（技能插件），它让 Claude 变成你的**私人面试顾问**——不是给你一堆通用模板，而是基于你的真实背景、目标岗位和具体情况，提供个性化的面试准备指导。

## 能帮你做什么？

| 阶段 | 功能 | 适用场景 |
|------|------|---------|
| **岗位分析 + 公司调研** | 解读 JD、七维度公司全景调研、评估匹配度、预判面试流程 | 刚看到岗位，想知道值不值得投 |
| **简历优化** | 诊断 + 逐条改写 + STAR-R 原则 | 简历投出去没反应 |
| **问题准备** 🔥 | 面经真题采集 + 能力域拆解 + 匹配矩阵 + 故事弹药库 + 深度答案稿 + 遗漏项审查 | 面试前不知道怎么准备 |
| **能力关实操** | Case Study / 做题 / System Design 模拟 | 有实操考核不知道怎么练 |
| **面试复盘** | 三层诊断 + 改进建议 | 面完了想知道问题在哪 |
| **薪资谈判 & Offer 决策** | 谈薪策略 + 多 Offer 对比框架 | 拿到 Offer 不知道怎么谈/怎么选 |
| **模拟面试** 🆕 | Claude 扮演面试官完整模拟 + 教练复盘 | 准备差不多了想试试手感 |
| **面试当天** 🆕 | 临场四大场景应对（不会的题/压力面/时间失控/冷场） | 明天就面试了 |
| **AI 面试** | 专项准备策略 | 遇到 AI 面试不知道怎么应对 |

### v3.0 核心升级

| 机制 | 功能 | 触发方式 |
|------|------|---------|
| **📊 公司全景调研** | 七维度调研（基本面→战略→部门→产品→竞争→文化→动态），输出结构化报告 | 阶段一自动触发，跳阶段提供精简版 |
| **📰 面经搜索** | 搜索小红书/牛客/脉脉/知乎真实面经，真题标注"真题"纳入题库 | 阶段三自动触发 |
| **🎯 能力域映射** | 基于 JD 动态识别 4-6 个能力域，每题标注考察能力+匹配经历+准备盲区 | 阶段三自动触发 |
| **📦 故事弹药库** | 3-5 个核心故事多面体拆解 + 故事-问题映射 + 多轮面试分配 | 阶段三引导建设 |
| **📝 深度答案稿** | 完整答案含时间标注 + 话术 + 数据点 + 决策逻辑 + 追问预判 | 每题自动输出 |
| **🔍 遗漏项审查** | 五维压力测试：数据口径/业务逻辑/指标计算/角色边界/业务细节 | 每题答案后自动触发 |

## 快速开始

### 方式一：上传 Skill ZIP（推荐）

1. 从 [最新 Release](https://github.com/chen3tu/interview-master-skill/releases/latest) 下载 `interview-master-v3.0.0.zip`
2. 确认 Claude 已启用“代码执行和文件创建”能力
3. 进入 `自定义 > Skills`，点击 `+ > 创建技能 > 上传技能`
4. 选择下载的 ZIP，安装后启用 Interview Master

Claude 当前要求上传包含完整 Skill 文件夹的 ZIP；具体入口以 [Anthropic 官方说明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)为准。

### 方式二：在 Claude.ai 中使用

1. 将 `SKILL.md` 和 `references/` 文件夹上传到你的 Claude Project 中
2. 在对话中直接说"帮我准备面试"或任何面试相关的请求
3. Claude 会自动识别你的阶段并给出针对性指导

### 方式三：作为 System Prompt 使用

将 `SKILL.md` 的内容作为 System Prompt 的一部分传入 Claude API。Reference 文件按需引用。

## 文件结构

```
interview-master/
├── SKILL.md                              # 核心 Skill 文件（主逻辑）
├── README.md                             # 你正在看的这个
├── CONTRIBUTING.md                       # 贡献指南
├── CHANGELOG.md                          # 版本记录
└── references/                           # 参考资源（按需读取，19个文件）
    │
    │── 公司调研与能力映射（v3.0新增）
    ├── company_research_guide.md          # 公司全景调研七维度指南
    ├── competency_answer_template.md      # 能力域拆解 + 匹配矩阵 + 答案稿模板
    ├── interview_advanced_guide.md        # 面经搜索 + 遗漏项审查 + 故事弹药库 + 实战指南
    │
    │── 岗位分化
    ├── role_product_operations.md         # 产品/运营岗考察全景
    ├── role_ai_product.md                # AI产品经理专项
    ├── role_technical.md                  # 技术/研发岗考察全景
    ├── role_management.md                 # 管理/管培/校招考察全景
    │
    │── 流程资源
    ├── job_analysis_template.md           # 岗位分析模板
    ├── resume_analysis_checklist.md       # 简历检查清单
    ├── behavioral_question_bank.md        # 行为面试题库
    ├── case_study_guide.md               # 实操考核准备指南
    ├── interview_evaluation_criteria.md   # 面试评分维度
    ├── interaction_guide.md              # 互动话术模板
    │
    │── 谈判与决策
    ├── salary_negotiation.md             # 薪资谈判策略
    ├── offer_evaluation.md               # Offer 评估框架
    │
    │── 专项准备
    ├── reverse_questions_bank.md         # 反向提问指南
    ├── ai_interview_prep.md             # AI 面试准备
    ├── multi_round_strategy.md          # 多轮面试策略
    └── deliverable_templates.md         # 文档沉淀模板
```

## 设计理念

1. **四重视角** — HR筛选视角 + 业务面试官视角 + 面试教练视角 + 职场导师视角
2. **公司级深度** — 不只准备通用题，而是基于公司调研和真实面经定制准备策略
3. **能力域映射** — 从岗位能力域出发出题，每题标注考察能力和匹配经历，识别盲区
4. **深度答案** — 不只给框架，输出完整答案稿含时间控制、话术、数据点和追问预判
5. **遗漏项审查** — 面试官视角压力测试，提前暴露数据口径、业务逻辑、指标计算漏洞
6. **教练式互动** — 不给通用答案，基于你的真实经历进行个性化训练
7. **全链路覆盖** — 从看 JD 到拿 Offer 谈薪，含模拟面试和面试当天实战指南

## 适合谁用？

- 🎓 应届毕业生 / 校招 / 管培生
- 💼 1-5 年经验的跳槽者
- 🧑‍💼 中高级管理岗求职者
- 🌍 海归求职 / 留学生回国找工作
- 🤖 即将参加 AI 面试的候选人

## 贡献

欢迎提 Issue 和 PR！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

特别欢迎：
- 添加新的岗位方向（如销售、设计、财务等）
- 补充特定行业的面试经验
- 分享真实的面试问题和复盘
- 改进话术和框架

## 项目入口

- [提交问题或功能建议](https://github.com/chen3tu/interview-master-skill/issues/new/choose)
- [交流使用经验](https://github.com/chen3tu/interview-master-skill/discussions)
- [查看版本记录](CHANGELOG.md)
- [阅读贡献指南](CONTRIBUTING.md)
- [私密报告安全问题](SECURITY.md)

> **隐私提示：** 简历、薪酬和面试记录可能包含敏感信息。公开提交 Issue、Discussion 或 PR 前，请删除个人信息、公司机密和未公开面试内容。

## 版本

当前版本：**v3.0.0**（2026-04-06 公司调研 + 面经搜索 + 遗漏项审查 + 深度答案 + 模拟面试）

详见 [CHANGELOG.md](CHANGELOG.md)

## License

MIT License — 自由使用、修改和分发。

---

> 💡 **提示**：这个 Skill 的价值在于"个性化"——它不会给你一套通用答案，而是通过和你的对话，基于你的真实情况帮你准备。所以使用时，尽可能详细地描述你的背景和目标。
