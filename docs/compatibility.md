# 多 Agent 安装与兼容性

Interview Master 是一个宿主无关的 Agent Skill。运行包只有 `SKILL.md` 和相对引用的 `references/`，没有 Claude 专用 API、固定 MCP 名称、运行时 Python 依赖或模型供应商绑定。

“支持同一格式”与“在某宿主实际验收通过”分开记录。当前验收版本为 **4.0.0-rc.2**；结果见 [Codex 验收报告](../evals/reports/codex-acceptance.md)。

## 一份运行包

```text
interview-master/
├── SKILL.md
└── references/
    ├── language_and_locale.md
    ├── session_modes.md
    ├── role_catalog.md
    └── …专业模块与完整工作样本
```

运行格式遵循 [Agent Skills 规范](https://agentskills.io/specification)。请保留整个文件夹；只粘贴入口会丢失方法、案例及事实规则。支持读取这种目录的 Agent 可复用同一包，但安装路径和触发入口由各宿主决定。

## Codex：项目级安装

把完整文件夹放在准备工作的项目中：

```text
your-interview-workspace/.agents/skills/interview-master/SKILL.md
```

从该项目启动 Codex，并输入：

```text
使用本项目的 interview-master，中文讲解、英文答案。
以下是我的JD和经历，请先给完整准备初稿，再集中核对事实。
```

也可通过技能选择器选中项目版本。全局与项目存在同名技能时，明确选中项目路径，避免误用旧版。安装后未出现时开启新会话或重启。当前本机的实际加载路径与命令已记录在验收报告中；CLI项目安装与10项有限检查通过，桌面技能选择器未测试。

用户级目录按 [Codex 官方说明](https://developers.openai.com/codex/skills) 为 `~/.agents/skills`；已有旧安装路径无需为本次验收迁移。不要将候选人的履历或会话存入 Skill 目录。

## WorkBuddy：导入本地技能包

按 [WorkBuddy 官方技能说明](https://cloud.tencent.com/document/product/1831/134432)，进入技能管理，添加技能并上传本地技能包，然后在对话中启用。选择本项目生成的完整 ZIP，并检查导入后入口旁仍有 `references/`。

示例请求与 Codex 相同，不需要更改面试方法或语言规则。WorkBuddy 的具体版本可能影响导入入口；本项目未在 WorkBuddy 客户端实跑，不能把文档对接视作宿主验收通过。

不要把 CodeBuddy Code/IDE 的 `.codebuddy/skills` 安装路径直接当作 WorkBuddy 桌面版路径；它们的产品文档和安装方式应分别核对。

## Claude 与其他 Agent

Claude 可按 [官方技能上传说明](https://support.claude.com/en/articles/12512180-use-skills-in-claude) 导入 ZIP。Claude 不再是本项目唯一或强制的发布验收宿主；它与 WorkBuddy 的运行验证单独记录。

其他 Agent：在其支持的技能目录或导入界面安装整个文件夹，确认能够加载相对参考文件，再执行下方验收请求。普通聊天模型手动阅读文件可以使用内容，但不等于具备自动技能发现能力。

## 能力降级

| 宿主能力 | 行为 |
|---|---|
| 可读取 Skill 和参考资料 | 按任务加载方法与岗位模块 |
| 无联网工具 | 基于用户提供材料准备，标注公司研究缺口 |
| 无文件写入 | 在聊天交付完整正文和可复制的续接摘要 |
| 可写入工作目录 | 按用户要求保存准备稿与续接记录 |
| 只有文字输入 | 评价内容与表达清晰度，不判断发音、眼神或真实语速 |

## 复用的宿主验收请求

1. **发现与准备**：提供合成JD和经历，要求完整答案，检查实际加载了当前安装路径与岗位参考。
2. **文件交付**：保存准备稿，检查正文完整、未知事实没有被补造。
3. **连续模拟**：英文开始 → 暂停并中文讲解/英文示范 → 西语继续原题。
4. **事实保真**：参与不改成主导；15%到18%保持3个百分点；未知因果继续保留。
5. **模块直达**：仅比较Offer，不要求先做履历问卷。

记录宿主版本、模型（可获得时）、包哈希、实际输入/输出和失败，不以格式校验代替真实运行。升级先保留旧包；回退只替换Skill，保留用户资料。

官方资料核对日期：2026-10-20。安装说明属于宿主文档摘要，未复制其完整操作手册。
