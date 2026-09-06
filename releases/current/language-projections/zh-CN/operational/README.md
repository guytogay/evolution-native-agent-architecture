# Operational Architecture（简体中文投影）

状态：`CURRENT / OPERATIONAL_HOW_PROJECTION / VERSION_NEUTRAL`

这是 Current 面向实际运行的 cold HOW 层中文语义投影。它不是 Constitution 的重复翻译，也不是新的规范权威；canonical semantic/machine source 仍在 Current 主路径。

它的目标是让采用者在不阅读 research history 的情况下，从一个真实问题走到可执行机制分支。

```text
默认常驻 Runtime Kernel
-> 真实问题 / 故障 / 决策
-> CUE-INDEX
-> HOW-MAP
-> 需要时 REFERENCE-INDEX / exact reference / Host-native mechanism
-> 行动、WAIT、UNKNOWN、REFUSE 或 NOT_APPLICABLE
```

完整 HOW 库是 cold capability，不应被强制永久塞入 Agent 热上下文。

```text
AVAILABLE_RESOURCE != DEFAULT_HOT_PAYLOAD
HOT_KERNEL != HOW_LIBRARY
HOW_VARIATION != SEMANTIC_DUPLICATION
```

reference 是可复用实现和机器表面，不是 ENA 必须安装的器官清单。Host-native mechanism 只要保留所需 property/boundary，可以是第一等实现。

一个有价值的 HOW 应改变 Agent 实际能做什么：说明适用条件、动作/状态、Host 依赖、effect/authority 边界、失败症状、fallback/WAIT/REFUSE/recovery 与证据边界。若只是把原则换句话说，它仍是 operational debt。

> **压缩热语义面，让具体 HOW 按需分叉。**
