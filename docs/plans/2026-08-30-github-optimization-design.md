# GitHub 仓库与个人主页优化设计

## 目标

在不改变 Interview Master 核心方法论的前提下，提升仓库的可安装性、可信度、可维护性和社区参与效率，同时建立与项目定位一致的 GitHub 个人主页。所有文件改动通过独立分支和 Pull Request 交付，远端 `main` 在审阅前保持不变。

## 方案

核心仓库分为四个优化单元。第一，修复 README 中不存在的 `.skill` 下载说明，改为从 GitHub Release 获取正式安装包，并增加版本、许可证、自动检查等状态入口。第二，补充 Issue 表单、PR 模板、安全政策和社区入口，让问题反馈与贡献信息结构化。第三，增加无外部运行时依赖的 Python 验证脚本，检查必需文件、Skill frontmatter、Markdown 相对链接和引用文件，并由 GitHub Actions 在 push 与 PR 时执行。第四，完善 Topics、Discussions 和安全更新设置。

个人主页使用新的公开仓库 `chen3tu/chen3tu`，README 聚焦 AI Skill、面试方法论和代表项目，不虚构经历、公司或联系方式。发布流程从已存在的 v3.0.0 内容生成可复现的 `.skill` 压缩包，先验证包内结构，再创建 `v3.0.0` Tag 与 Release。

## 验证与风险控制

本地验证覆盖脚本自测、仓库结构检查、Markdown 相对链接、`.skill` 包内容和 Git diff。GitHub 设置变更在文件 PR 验证通过后执行。若远端出现同名 Tag、Release、Profile 仓库或并发提交，则停止对应写操作并重新读取状态，避免覆盖。发布和合并分别作为独立检查点，确保可回滚并保留审阅记录。
