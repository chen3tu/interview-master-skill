# Interview Master 🎯

**全流程面试准备与求职决策系统** — 一个面向 Claude AI 的 Skill，帮助求职者从岗位分析到拿下 Offer 的每一步。

## 这是什么？

Interview Master 是一个基于 [Claude](https://claude.ai) 的 AI Skill（技能插件），它让 Claude 变成你的**私人面试顾问**——不是给你一堆通用模板，而是基于你的真实背景、目标岗位和具体情况，提供个性化的面试准备指导。

## 能帮你做什么？

| 阶段 | 功能 | 适用场景 |
|------|------|---------|
| **岗位分析** | 解读 JD、评估匹配度、预判面试流程 | 刚看到岗位，想知道值不值得投 |
| **简历优化** | 诊断 + 逐条改写 + 教你改写逻辑 | 简历投出去没反应 |
| **问题准备** | 高概率题预测 + 一对一教练式训练 | 面试前不知道怎么准备 |
| **能力关实操** | Case Study / 做题 / System Design 模拟 | 有实操考核不知道怎么练 |
| **面试复盘** | 三层诊断 + 改进建议 | 面完了想知道问题在哪 |
| **薪资谈判 & Offer 决策** | 谈薪策略 + 多 Offer 对比框架 | 拿到 Offer 不知道怎么谈/怎么选 |
| **AI 面试** | 专项准备策略 | 遇到 AI 面试不知道怎么应对 |

## 快速开始

### 方式一：在 Claude.ai 中使用

1. 将 `SKILL.md` 和 `references/` 文件夹上传到你的 Claude Project 中
2. 在对话中直接说"帮我准备面试"或任何面试相关的请求
3. Claude 会自动识别你的阶段并给出针对性指导

### 方式二：作为 System Prompt 使用

将 `SKILL.md` 的内容作为 System Prompt 的一部分传入 Claude API。Reference 文件按需引用。

## 文件结构

```
interview-master/
├── SKILL.md                              # 核心 Skill 文件（主逻辑）
├── README.md                             # 你正在看的这个
├── CONTRIBUTING.md                       # 贡献指南
├── CHANGELOG.md                          # 版本记录
└── references/                           # 参考资源（按需读取）
    ├── role_product_operations.md         # 产品/运营岗考察全景
    ├── role_technical.md                  # 技术/研发岗考察全景
    ├── role_management.md                 # 管理/管培/校招考察全景
    ├── job_analysis_template.md           # 岗位分析模板
    ├── resume_analysis_checklist.md       # 简历检查清单
    ├── behavioral_question_bank.md        # 行为面试题库
    ├── case_study_guide.md               # 实操考核准备指南
    ├── interview_evaluation_criteria.md   # 面试评分维度
    ├── interaction_guide.md              # 互动话术模板
    ├── salary_negotiation.md             # 薪资谈判策略
    ├── offer_evaluation.md               # Offer 评估框架
    ├── reverse_questions.md              # 反向提问指南
    └── ai_interview_prep.md             # AI 面试准备
```

## 设计理念

1. **四重视角** — HR筛选视角 + 业务面试官视角 + 面试教练视角 + 职场导师视角
2. **阶段化准备** — 不是从头到尾走一遍，而是根据你当前的阶段直接进入
3. **教练式互动** — 不给通用答案，基于你的真实经历进行个性化训练
4. **全链路覆盖** — 从看 JD 到拿 Offer 谈薪，不断在"面试答题"这个环节

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

## 版本

当前版本：**v2.0.0**（2025-03 重构版）

详见 [CHANGELOG.md](CHANGELOG.md)

## License

MIT License — 自由使用、修改和分发。

---

> 💡 **提示**：这个 Skill 的价值在于"个性化"——它不会给你一套通用答案，而是通过和你的对话，基于你的真实情况帮你准备。所以使用时，尽可能详细地描述你的背景和目标。
