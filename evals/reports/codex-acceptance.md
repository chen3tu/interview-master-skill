# Codex 实际宿主验收报告

> Publication update (2026-10-20): the maintainer explicitly accepted this candidate and authorized GitHub publication. The report below preserves the original pre-publication findings and limits. Runtime payload is unchanged.
2026-10-20 · Interview Master **4.0.0-rc.2** · 本地候选版，尚未推送。

## 验收结论

本报告使用真实 Codex CLI 会话执行已安装的候选包，区分内容表现、宿主文件能力与环境失败。下列10项检查最终通过；涉及3个会话、7个成功完成的对话轮次，另有1个因配额失败的初始轮次。通过指列明的有限场景，不是所有宿主或输入的保证。维护者验收和 GitHub 推送是后续独立步骤。

本次没有运行 WorkBuddy 或 Claude 客户端；它们有格式及官方安装文档支持，不能据此声明实跑通过。Codex 桌面技能选择器、旧用户工作区升级和跨宿主会话迁移也未测试。

## 对象与环境

| 项目 | 记录 |
|---|---|
| Runtime commit | `918a20b0650494e283ed953660ade721130fbddf` |
| ZIP | `interview-master-v4.0.0-rc.2.zip`，64,049 bytes，41 files |
| SHA-256 | `466d5b10bf400edbb42ccf17c687b529454f205aa921107931b80b0671342ee2` |
| 安装 | 独立验收工作区 `.agents/skills/interview-master/`，从实际 ZIP 解压；41 个文件逐字节一致 |
| 宿主 | Codex CLI `0.163.0-alpha.10.2`，macOS，本机桌面应用内置 CLI |
| 模型 | 当前默认 `gpt-6-astra`，reasoning effort `high`；没有更换默认模型或账号 |
| 权限 | 正常 `workspace-write` 子会话；一次默认 resume 变为 `read-only`，另行记录 |
| 输入 | 合成经历、合成岗位及数字；无真实履历或私人材料 |
| 联网 | 场景均要求离线；模型服务连接本身仍需网络 |

入口及专业参考的实际读取命令可在 [事件摘要](../codex-host/events-summary.json) 检查。摘要保留完成命令、退出码、原输出摘要哈希、文件变更及结束状态；省略内部推理与全局日志，并替换本地用户路径。输出正文仅调整路径链接，未重写答案以使其通过。

## 实际场景与判定

| 编号 | 判定条件 | 结果与证据 |
|---|---|---|
| H01 项目安装与加载 | 实际读取项目版本入口及相对参考，而不是只在父会话粘贴规则 | 通过。准备和模拟命令读取 `.agents/skills/interview-master/SKILL.md`，并按需读取模式、事实、语言和岗位模块。 |
| H02 中英完整准备 | 中文讲解、英文自我介绍和三道完整答案；先给正文，集中核对事实 | 通过。[准备稿](../codex-host/outputs/preparation.md)含岗位映射、三题及追问、40分钟安排、五项事实核对。首次执行因配额中断；恢复后完成，不能把失败轮算成功。 |
| H03 事实与专业深度 | 参与不升级为主导；工程职责和未知因果保留；方法不是历史业绩 | 通过。区分权限解释与规则问题、工作空间级验证、交付与结果；15%→18%不归因于候选人。60秒是练习目标，未伪称已测量。 |
| H04 只读降级 | 无写权限时在聊天交付，明确没有保存 | 通过。[只读回复](../codex-host/outputs/preparation-response.md)交付完整正文并明确只读限制，未声称文件已写入。 |
| H05 文件交付 | 恢复写权限后真实保存并验证正文 | 通过。[保存回复](../codex-host/outputs/preparation-save-response.md)及事件记录显示写入并检查7部分、3答案、5核对项；文件13,909 bytes。 |
| H06 压力模拟起始 | 英文只问一道题等待，不泄漏答案 | 通过。[起始输出](../codex-host/outputs/mock-start.md)追问个人贡献与产品判断，未预先给答案。 |
| H07 暂停 | 立即退出追问，用中文解释、英文示范并保留事实 | 通过。[暂停输出](../codex-host/outputs/mock-pause.md)明确暂停；示范保留参与、工程代码、3个百分点及未知因果。 |
| H08 西语续接 | 所有输出切西语，继续待答问题，不把示范当候选人回答 | 通过。[西语恢复](../codex-host/outputs/mock-resume.md)全部使用西语，明确候选人尚未回答，保留同一问题与事实，不评分。 |
| H09 未点名选择与数据样本 | 未指名 interview-master，仍选择项目适用技能；全英文、完整解法、保持经历边界 | 通过。[英文输出](../codex-host/outputs/implicit.md)、[完整练习包](../codex-host/outputs/interview_practice.md)、[SQL](../codex-host/outputs/work_sample.sql)。总体15%→14.5%，渠道20%→22%、10%→12%，固定构成17%，分解+2/−2.5个百分点。 |
| H10 直接Offer任务切换 | 不启动履历问卷；固定收入与目标奖金分开计算 | 通过。[Offer输出](../codex-host/outputs/direct-offer.md)：A固定280,000，B固定288,000、目标324,000；明确奖金不保证，未重启履历采集。 |

H09 是“用户要求使用适用项目技能，但不提供技能名”的选择测试：事件显示 Codex 搜索项目文件并读取入口。它不是完全不提示技能时的自动触发测试，也没有验证桌面选择器注册。数据样本实际在 SQLite 执行；生成的验证脚本第一次用分号拆 SQL，遇到注释内分号失败，改为 `sqlite3.complete_statement` 后三组结果通过。失败记录保留，没有写成一次成功。

## 会话与复现

实际三个会话：

- 准备、只读恢复、保存及Offer切换：`01a15751-2168-7020-a378-12aecd6b85f1`。
- 模拟、暂停及西语恢复：`01a157e4-f488-7081-ab2f-776eaed748d5`。
- 未点名技能的数据准备：`01a157e8-7c38-71a3-80de-f6e05684f56b`。

输入原文见 [inputs](../codex-host/inputs/)。以下命令去掉本机绝对路径后保留实际调用结构；先从 ZIP 安装到项目目录，再从该目录启动。`codex` 指上述版本的可执行文件，不要求改动全局配置。

```sh
codex exec --json --sandbox workspace-write --skip-git-repo-check \
  -C "$ACCEPTANCE_WORKSPACE" -o results/preparation-response.md \
  - < inputs/preparation.txt > results/preparation.events.jsonl

codex exec --sandbox workspace-write resume --json --skip-git-repo-check \
  -o results/mock-pause.md "$MOCK_SESSION_ID" \
  - < inputs/mock-pause.txt > results/mock-pause.events.jsonl

codex exec --sandbox workspace-write resume --json --skip-git-repo-check \
  -o results/mock-resume.md "$MOCK_SESSION_ID" \
  - < inputs/mock-resume.txt > results/mock-resume.events.jsonl
```

同一会话内的续接共享上下文。它们验证连续行为，不是独立重复实验。没有对这些输出作统计显著性或成功率估计。

## 环境问题与实际处理

1. 外层受限执行最初无法写 Codex 本地数据库，未启动成功。随后使用获准的普通本机 CLI 执行，子会话仍使用标准沙箱，没有绕过权限机制。
2. 多次启动遇到 WebSocket 超时，CLI 自动回退 HTTP 后继续。没有修改网络、模型或全局配置；这些延迟不能归因于 Skill 的准备节奏，也没有报告端到端耗时提升。
3. 准备首次已读取 Skill 和参考，但遇到账户配额限制而失败；用户回来继续时额度已恢复，随后续接完成。没有重置配额、购买额度或切换账号。
4. 未显式指定顶层沙箱的 resume 使用只读模式；Codex正确告知不能保存。明确传入 `--sandbox workspace-write` 后实际完成保存。
5. CLI还显示其他既有全局技能的解析警告。本候选包读取成功，未修改其他全局技能。

## 与此前验证的关系

rc.1的58份输出、17项测试、引用图与确定性打包见 [行为报告](v4-behavior-report.md)及[本地验证记录](local-checks.md)。rc.2主要增加宿主中立入口说明。本次实际安装和 CLI 执行补上“真实 Codex 宿主”证据，并不等于在每个宿主重新跑完全部场景。

局限：没有真人面试效果测量、原生语言专家审校、语音/视频测试、长会话可靠性估计或旧工作区升级验证。既有v3对照也能首轮交付，不能声称v4已经证明稳定提速。

## 维护者验收入口

建议先检查[准备稿](../codex-host/outputs/preparation.md)能否直接练习，再检查[数据工作样本](../codex-host/outputs/interview_practice.md)的深度，以及模拟的暂停和语言续接。对照[能力提升说明](../../docs/capability-upgrade-v4.md)与[中文README](../../README.md)，评估功能与说明是否达到预期。

本地工程/宿主验收不替代用户批准。**只有维护者明确验收通过后，才执行 GitHub 推送；当前未推送、未创建PR、未发布Release。**
