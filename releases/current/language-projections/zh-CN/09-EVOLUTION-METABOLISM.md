# 9. 进化代谢与进化生态 — Current

状态：`CURRENT / FIELD_VALIDATION`

生态模型：

`环境/刺激 -> 变异压力 -> 变异 -> 潜伏/表达 -> 接触现实 -> 局部选择 -> 保留/休眠/消失 -> 迁移/重组 -> 再次产生变异`

核心区分：`刺激 != 变异 != 改进`，`保存 != 表达 != 应用 != 选择`，`局部选择 != 普适适应度`。

variation 可以长期 latent；`UNASSESSED` 不等于 backlog debt。有后果实验进入与 consequence 相称的真实 Variation Space。

迁移传递“可能性 + 来源历史”，不传递接收方结论。packet digest 只检查内容一致性，不认证来源。重组/组合可能恶化、抵消、放大或产生涌现，交互会改变决定时应观察组合主体。

self-mutation 可能破坏 recovery 时，在 consequence 值得的情况下保留 damaged variation 之外可达的 rescue path。`restore success != external consequence rollback != authority restoration`。

control retirement 需要 original failure、replacement/coverage、reactivation 和 lineage；`NO_INCIDENT != CONTROL_NOT_NEEDED`。

## 最小可执行进化循环

理解上面的生命周期还不够。一个准备长期自我进化的 Host，至少需要一条可执行循环，即使具体器官完全由 Host-native mechanism 实现：

```text
signal / idea / correction / failure / success
-> durable inbox / candidate queue
-> candidate hypothesis + proposed change
-> 默认 LATENT
-> 判断 trial 是否真的可能改变决策
-> 记录 decision-relevant baseline + 必要的 recovery/authority boundary
-> bounded expression / Variation Space / real task
-> 先观察 outcome，再解释
-> 局部 selection: SUPPORTED | PARTIAL | NOT_SUPPORTED | HARMFUL | UNKNOWN
-> integrate / retain / adapt / dormant / reject / archive
-> 在新 signal 或环境变化时再次 wake
```

规范 HOW：`operational/procedures/EVOLUTION-LOOP.md`。

Host 若声称要长期 self-evolve，应该能识别、实现或明确标记缺失/不适用的功能：

- durable signal/inbox；
- 与 active self 分离的 latent candidate store；
- 真正能接触现实的 bounded trial surface；
- 与 hypothesis 相关的 before/after evidence 或 baseline；
- self-disable 风险实质存在时的 recovery；
- 保存 retain/reject/unknown 原因的 selection record；
- 在相关时重新唤醒 latent material 的 event/schedule/manual review。

这些功能不要求七个独立工具。Git、JSONL、数据库、task memory、cron/event、sandbox/canary、snapshot/watchdog 等都可以一器官多用。

```text
进化词汇 != 可执行进化循环
保护可进化性 != 进化本身
没有新 signal != 没有进化
进化循环 != 连续 self-editing
```

`tools/ena_evolve_v2.py` 仍是窄的 v2 record/packet 实用路径：可以创建/import/export/validate candidate 和 packet，但**不是完整 expression/trial/evaluation/integration lifecycle engine**，也不能证明外部 truth。Host 可以在有用时使用它，并用自己的器官完成其余循环。

> **捕获压力，保存变异，接触现实，局部选择，保留证据，再继续观察。**
