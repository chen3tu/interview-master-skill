# 贡献指南

感谢你对 Interview Master 的关注！我们欢迎任何形式的贡献。

## 如何贡献

### 1. 报告问题 (Issue)

- 面试准备建议不准确或过时
- 某个岗位方向的考察维度缺失
- 话术或框架在实际面试中不好用
- 任何 Bug 或文档错误

### 2. 提交改进 (Pull Request)

**特别欢迎的贡献：**

| 类型 | 说明 |
|------|------|
| 新增岗位方向 | 如销售、设计、财务、法务、市场等 |
| 行业经验补充 | 特定行业（金融/医疗/制造等）的面试特点 |
| 真实面试反馈 | 用了这个 Skill 后的实际效果和改进建议 |
| 框架优化 | 更好的答题框架或教练方法 |
| 国际化 | 英文版、针对海外求职的适配 |

### 3. 分享使用经验

在 Issue 或 Discussion 中分享你使用 Interview Master 准备面试的经历，包括：
- 哪些部分最有帮助
- 哪些建议在实际面试中不管用
- 你自己总结的补充建议

## 贡献规范

### Reference 文件格式

新增 reference 文件请遵循以下结构：

```markdown
# [主题名称]

## 一、概述
[简要说明这个文件的用途]

## 二、核心内容
[按逻辑组织的主要内容]

## 三、实操建议
[可直接使用的建议/框架/模板]
```

### 新增岗位方向

如果要添加新的岗位方向（如 `references/role_sales.md`），请包含：

1. 岗位画像（核心能力、面试官最看重什么、常见淘汰原因）
2. 考察维度表（维度+权重+怎么评）
3. 高概率面试问题（至少5道，配STAR提示）
4. 实操考核类型和准备方法
5. 简历标准（好/差对比示例）
6. 不同层级的考察差异

### Commit 规范

```
feat: 新增销售岗面试指南
fix: 修正薪资谈判话术中的表述错误
docs: 补充 README 使用说明
refactor: 重构行为面试题库分类方式
```

## 本地验证

自动检查需要 Python 3.10 或更高版本。提交前请运行与 GitHub Actions 相同的命令：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_repository.py
```

验证器会检查必需文件、`SKILL.md` frontmatter、Markdown 相对链接和 reference 引用。

如果改动影响 Skill 行为，还需要：

1. 将 Skill 文件夹打包为 ZIP 并上传到 Claude
2. 用与改动相关的最小场景完成一次对话测试
3. 确认对应 reference 能按预期读取，且输出不泄露测试者隐私

## 行为准则

- 保持专业和尊重
- 基于真实经验分享，不造假数据
- 保护隐私：不分享涉及真实公司/个人的敏感信息
- 安全问题请通过[私密漏洞报告](https://github.com/chen3tu/interview-master-skill/security/advisories/new)提交
