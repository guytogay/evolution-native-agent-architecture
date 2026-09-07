# Next-session launch prompt

Use this when handing the project to a new ordinary project-manager session (not a fresh independent validator):

> 请接手 GitHub 仓库 `guytogay/evolution-native-agent-architecture` 的 ENA 项目。先从 `main` 的 `NOW.md` 和 `research/handoffs/CURRENT-HANDOFF.yaml` 开始；当前是一次 DEEP session succession，请按 `CURRENT-HANDOFF.yaml` 指向的 `2026-09-07-v0314-pr224-review` 记录完成接班 readback，并独立核验所有 mutable live facts 后继续其 current next action。不要让我重复上一 session 的背景，也不要做全库审计。当前重点是外部 Agent PR #224：先核对其 live head/state 和 maintainer comments，再继续语义收窄/热负载成本判断；不要把 #224 直接合入已发布 v0.3.14，也不要预设一定要发 v0.3.15。遵守 `same version -> same effective content` 与 `.github/workflows/current-immutability.yml`，保留外部贡献 provenance、负面/收窄结果和已关闭研究的 closure discipline。

This prompt is for project succession only. Do not use it for fresh validation.
