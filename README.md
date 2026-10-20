# Interview Master

[English](README.en.md) · [贡献指南](CONTRIBUTING.md) · [版本记录](CHANGELOG.md)

面向求职者的多语言面试准备与训练 Skill：用真实经历和目标岗位，生成可用材料、讲清专业方法，并进行可调整强度的模拟面试。

**开发版本：v4.0.0-rc.1，尚未发布正式版。** 安装与行为验证范围见评测报告；仓库的既有正式发布与本开发分支不同。

## 从你需要的方式开始

| 方式 | 适合什么需求 | 行为 |
|---|---|---|
| 冲刺 | 明天面试、只补重点 | 先给最有用的答案和速记 |
| 完整准备 | 想一次拿到可学习的准备包 | 先出可用初稿，再集中补事实 |
| 教练训练 | 理解方法、边练边改 | 可以先看示范，也可以自己先答 |
| 正式模拟 | 练临场表现或压力面 | 逐题追问，暂停即可切回讲解 |

直接要自我介绍、反问、项目介绍、谈薪或Offer比较也可以，不必走完整流程。输出可选择仅问题、提纲、完整答案或学习包；压力强度单独选择。

## 多语言

支持指定讲解语言、答案语言和模拟语言，保留事实、贡献边界和数字。中英文有明确示例；其他语种按同一机制工作，质量取决于宿主模型，测试覆盖以报告为准。

~~~text
中文讲解，帮我写英文面试答案；不要把“参与”改成“主导”。
Interview me in English. Give feedback in Chinese when we finish.
Prepare everything in English, including headings and model answers.
Responde solo en español. Practiquemos una entrevista de producto.
~~~

招聘市场与语言分开处理；英文面试不等于美国岗位。语言清晰度与专业能力分开反馈。文字输入不能用于判断发音、眼神或实际语速。

## 内容与岗位

保留JD分析、简历优化、公司研究、行为/项目问题、实操、面试当天、复盘、谈薪与Offer比较。
重点模块覆盖产品、运营/增长、数据分析、技术、AI产品和管理。技术细分后端、前端、移动客户端、AI应用工程。每个方向有方法、取舍、失败变化和合成工作样本。

完整准备包包含岗位判断、证据矩阵、自我介绍、项目答案、针对性问题与回答、专业教学、工作样本、反问、速记及集中核对清单。未知数字不会被编造，也不会让所有准备停住。

其他岗位可以按JD适配，但未建立同等深度的专门模块。材料生成、实际练习和模拟观察是不同完成状态，不承诺录用概率。

## 使用与安装

本开发版本可在本地构建：

~~~sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_repository.py
python3 scripts/build_release.py --version 4.0.0-rc.1 --output-dir dist
~~~

ZIP中只有interview-master/SKILL.md和references，包含全部运行时样例。使用支持Skill文件夹的宿主时保留整个结构，不要只复制入口文件。

Claude支持上传含完整Skill文件夹的ZIP；当前入口及前置能力以[官方安装说明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)为准（2026-10-20核对）。这不是本版本已完成Claude界面安装测试的声明。

没有联网能力时基于已提供材料继续，标明研究缺口；没有文件能力时在对话中交付并提供续接摘要。无需账号服务或运行时CLI。

## 项目维护

- [迁移与回退](docs/migration-v4.md)
- [行为评测协议](evals/README.md)
- [实现与测试状态](evals/reports/v4-release-check.md)
- [来源与独立设计](docs/source-notes.md)
- [后续范围](docs/roadmap.md)

候选人事实、简历和会话应放在Skill之外，不会自动上传、提交或发布。反馈请使用合成或脱敏的最小案例。
MIT License。第三方链接的内容不因此获得本项目许可证。
