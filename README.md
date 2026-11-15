# ai-reviewer-eval

软件工程课程大作业 · 选题 4 · 智能代码审查评测

本仓库用于演示 AI 代码审查工具在 Pull Request 上的实际表现。
每个 PR 只包含一个已注入的缺陷，便于对照 reviewer 能否定位到具体代码行。

| PR | 改动 | 注入的缺陷 |
|---|---|---|
| PR-1 | app/db/users.py | f-string 拼接 SQL（CWE-89） |
| PR-2 | app/stats/score.py | 空列表除零（CWE-369） |
| PR-3 | app/orders/classify.py | 五层 if 嵌套（风格） |

> 仓库中的密钥均为演示用假值，不含任何真实凭据。
