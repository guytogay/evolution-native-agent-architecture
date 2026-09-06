# ENA Current — 请先阅读

状态：**CURRENT / FIELD_VALIDATION**

当前唯一面向采用者的数值版本身份由 `../../CURRENT-BASELINE.yaml` 定义。本目录是 Current 的简体中文语义/运行投影。

## 默认 Agent 热负载

普通 Agent 默认只需常驻：

`RUNTIME-ADOPTION-KERNEL.md`

这不是“必须先读完一张清单”。以下内容按真实问题需要再检索：

- `operational/CUE-INDEX.md`；
- `operational/HOW-MAP.md`；
- `REFERENCE-GUIDE.md` 与 canonical references；
- `../../ENFORCEMENT-MAP.yaml`；
- semantic fixtures / validators；
- Constitution、concept map、glossary 与研究谱系。

```text
AVAILABLE_RESOURCE != DEFAULT_HOT_PAYLOAD
HOT_KERNEL != FULL_HOW_LIBRARY
```

## 采用路径

```text
常驻 Runtime Kernel
-> 真实问题触发 cue
-> 按需检索对应 HOW / Host-native mechanism
-> 必要时检查 enforcement/evidence boundary
-> act / WAIT / UNKNOWN / REFUSE / NOT_APPLICABLE
-> 观察现实
```

采用后，以及 Host/runtime 发生**实质变化**后，做一次有边界的本地 operationalization pass。只有当某个边界的缺失、不确定或失效可能改变当前/反复出现的决策，或 authority/effect/recovery/evidence/长期进化边界时，才把它视为本地适用；否则可以明确 `NOT_REQUIRED` / `NOT_APPLICABLE`。Host/runtime 变化只有在它可能让已有本地投影失效或改变决策边界时才算“实质变化”；无关的环境抖动不要求重跑。

不要把模型提示当成硬控制，也不要把 machine PASS 当成外部世界事实。

```text
MODEL_CUE != HARD_CONTROL
MACHINE_GUARD != EXTERNAL_TRUTH
TRANSLATED != BEHAVIORALLY_EQUIVALENT
LOCAL_OPERATIONALIZATION != INSTALL_EVERY_CONTROL
```

稳定语义面默认不复制可变的 Current 数值版本。需要确认当前版本时，以 `../../CURRENT-BASELINE.yaml` 与本目录 `projection-manifest.yaml` 为准；真实历史 provenance 仍可保留其来源版本。

```text
COLD_SEMANTIC_SURFACE != RELEASE_ID_LABEL_MAINTENANCE_BURDEN
HISTORICAL_PROVENANCE != ACTIVE_RELEASE_IDENTITY
```

> **常驻一个核心；需要时再长出 HOW；只在真实本地缺口值得时落地；版本身份只放在真正需要版本身份的表面。**
