# ENA 运行时采用核心 — v0.3.8

状态：`CURRENT / FIELD_VALIDATION / HOT_SEMANTIC_CUE_SURFACE`

**ENA 的存在，是为了让持续自我进化成为可行能力。**

这是热路径，不是整套 ENA。

## 核心区分

- `刺激 != 变异 != 改进`；
- `保存 != 表达 != 应用 != 选择`；
- `claim != evidence != support != applicability`；
- `局部成功 != 普适适应度`；
- `迁移 != 本地验证`；
- `来源成功 != 接收方本地证明`；
- `局部有效/改进 != 组合后的实际结果`；
- `取消 != 回滚 != 补偿`；
- `恢复/继续 != 完整历史 != 授权恢复`；
- `持久对象存在 != 相关字节已加载 != 语义已可用`；
- `WRITTEN != LOADED != INTERPRETED != SALIENT != APPLIED`；
- `agreement count != independent support count`；
- capability / credential / identity / reputation 都不会自动生成当前外部 authority；
- UNKNOWN 不能偷偷升级成 SAFE、IMPROVED、AUTHORIZED、VERIFIED、INDEPENDENT 或 UNIVERSAL。

这些是 cue / boundary，不等于 prose 已经硬执行。

## Cue -> HOW

```text
紧凑 cue
-> operational/CUE-INDEX.md
-> operational/HOW-MAP.md
-> 需要精确路径时用 operational/REFERENCE-INDEX.yaml
-> applicability / Host 过滤
-> procedure / optional reference / Host-native mechanism
-> 行动、WAIT、UNKNOWN、REFUSE 或 NOT_APPLICABLE
```

完整 HOW library 不需要永久热加载。`cue 已配置 != 未来自然想起已证明`。

## 变异、选择与迁移

mutation pressure 是产生/重看 variation 的机会，不是命令。variation 可以保持 latent。有后果的实验进入与 consequence 相称的 Variation Space。正负 selection 默认只属于实际环境；传播或流行不是本地证明。

## Recovery / Effect / Authority

`backup exists != recovery proven`。self-mutation 可能破坏恢复时，在 consequence 值得的情况下保留 damaged variation 之外可达的 rescue path。restore 后继续产生外部后果前，要对账 external effect、当前 authority 和本决策所需的完整历史。

## 治理闭环

使用能改变/保护当前决策的最轻机制。control retirement 要有 evidence + lineage，而不是按年龄、安静程度或事故次数机械删除。新的 bounded check 已不能改变决定时停止加治理。

## Enforcement

使用 `ENFORCEMENT-MAP.yaml` 区分：

`MODEL_CUE | MACHINE_GUARD | EXTERNAL_CONTROL_REQUIRED | FIELD_EVIDENCE_REQUIRED`

模型指导不是硬控制；机器 validator 也不证明外部世界事实。

> **内化 cue，按需寻找 HOW。治理必须收敛并支付成本。**
