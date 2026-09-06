# 最小进化循环 — Current

状态：`CURRENT / COLD_OPERATIONAL_HOW / HOST_NEUTRAL`

当 Agent/Host 需要把 ENA 的进化语义变成可以反复执行的实际循环时使用本 procedure。

它不是 universal daemon、scheduler、数据库或强制 self-modification engine。Host 可以用 JSONL、Git、数据库、task memory、queue、cron/event、experiment runner 或其他原生机制来实现。

```text
进化词汇 != 可执行进化循环
保护可进化性 != 进化本身
```

## Trigger

出现以下真实 signal 时启动或唤醒：

- correction / repeated failure；
- friction、latency、cost、coordination burden、反复人工 rescue；
- unexpected success / reusable shortcut；
- 新 capability/tool/model/Host/environment；
- external contribution / migrated adaptation；
- latent idea 重新与现实问题相关；
- Host/runtime 实质变化使旧假设失效。

只有当 signal 如果丢失，可能影响后续 selection、recovery、evidence 或反复工作决策时，才值得持久化。**不要因为存在 inbox 就把每个一闪而过的念头都记成进化记录。**

没有 signal 也是信息：不能因为“有进化循环”就强迫自己持续修改。

## 最小循环

### 1. 先把 decision-relevant signal 持久化

在决定改什么以前，把真正可能影响后续判断的 observation 放进 durable inbox / queue。无法合理改变后续决策的 trivial/transient thought 可以直接丢弃，不要把记录本身变成仪式。

最小字段：`time / source-author / subject / signal-observation / why-it-matters / evidence-link / state`。

对 `evolution-record.v2`，可把 occurrence ref 放进 `signal_refs` / `mutation_pressure_refs`。

**边界：** 聊天里出现过 != 已持久捕获；Capability Map 里写着 `Evolution Inbox` != Host 真的有 inbox；持久捕获也 != 每个想法都必须记账。

### 2. 形成 candidate，但默认保持 latent

记录：`hypothesis / proposed change / expected outcomes / environment / unknowns / dependencies / protected subjects / observation plan`。

可使用 `templates/evolution-record.v2.json`、`tools/ena_evolve_v2.py new-latent` 或 Host-native equivalent。

默认：

```text
lifecycle_state = PROPOSED
expression_state = LATENT
selection_state = UNASSESSED
```

好想法不欠现实一个立即执行。

### 3. 判断 trial 值不值得

在 expression 之前问：

- 这个 trial 能改变哪个真实决策？
- 什么结果算 improved / degraded / unchanged / unknown？
- 是否足够便宜、可逆，可以直接本地试？
- 是否需要隔离的 Variation Space？
- 是否可能把 recovery 一起改坏？
- 是否跨 external authority / effect boundary？

合法结果：`KEEP_LATENT | TRIAL_NOW | WAIT_FOR_CONTEXT | REJECT_WITHOUT_TRIAL | NOT_APPLICABLE`。

不要为了证明“模型有多样性”去做结果范围早已可以预判的实验。

### 4. 建立最小 before-state

对可能实质改变 Agent/Host 的 trial，只记录能改变后续 selection 的内容：

- decision-relevant baseline / smoke tasks；
- material cost/latency/resource；
- 与 hypothesis 有关的当前 capability/behavior；
- self-change 可能破坏 recovery 时的 snapshot/rescue；
- external authority/effect boundary；
- stop / rollback condition。

```text
BACKUP_EXISTS != RECOVERY_PROVEN
BASELINE_EXISTS != UNIVERSAL_FITNESS_METRIC
```

baseline 可以只是 1–5 个 smoke probes、真实 task metric、trace 或 bounded qualitative evidence；不要制造 universal scalar。

### 5. 在最轻的真实环境表达 variation

优先选择能产生 decision-changing evidence 的最窄 surface：

- local reversible change；
- branch/worktree/sandbox/canary；
- limited task/traffic subset；
- shadow/observe-only；
- real bounded task with rollback；
- 只有低成本接触现实无法回答时才 full integration。

在 `experiments[]` 或 Host 记录中保存 actual change、time、variation space、effect boundary、recovery path、authority basis。

纯概念 variation 保持 `LATENT`，不要伪造 `EXPRESSED` evidence。

### 6. 先观察，再选故事

比较 before-state 和 expected outcomes。按需要记录多个维度：correctness/usefulness、latency/token/compute/human attention、recovery/resilience、新 failure mode、coordination cost、external effect、目标 Host 上的真实 behavior。

保留 negative evidence 与 unknown。

局部 selection：

`SUPPORTED | PARTIAL | NOT_SUPPORTED | HARMFUL | UNKNOWN`。

```text
局部选择 != 普适适应度
一次成功 != 定律
生存/奖励 != 道德正确
```

### 7. 根据 selection 处理 variation

- `SUPPORTED` → 在真实 scope/authority 允许时 integrate，并记录 lineage/residual；
- `PARTIAL` → 缩窄/调整，只保留被支持部分；
- `NOT_SUPPORTED` → 对当前环境拒绝，同时保留 negative evidence；
- `HARMFUL` → stop/rollback（若可能），保留 failure lineage；
- `UNKNOWN` → latent/dormant，或等待真正能改变判断的新 evidence；不要强行 verdict。

可能的 lifecycle：`INTEGRATED | LATENT | DORMANT | ARCHIVED | RETIRED | REJECTED_AS_LOCAL_SELECTION`。

### 8. 让循环活着，但不要变仪式

在 new signal、环境变化、重复 failure/success、migrated candidate 或有理由的 catch-up review 时再次 wake。

periodic scan 可有可无；没有可能改变 selection 的东西时就什么都不做。

```text
没有新 signal != 没有进化
进化循环 != 持续自我修改
```

## 最小 Host 器官

| 功能 | 最小目的 | 可能实现 |
|---|---|---|
| signal/inbox | idea/pressure 跨 session 存活 | JSONL、issue queue、DB、durable memory、Git file |
| candidate store | latent variation 与 active self 分离 | branch、record、DB row、skill draft |
| reality-contact surface | proposal 真正接触现实 | sandbox、canary、task subset、branch、real bounded task |
| before/after evidence | 判断变化有没有买到价值 | smoke task、metric、trace、qualitative evidence |
| recovery（必要时） | 防止 self-disable 无法恢复 | snapshot、Git rollback、watchdog、external rescue |
| selection record | 保存为什么 retain/reject/unknown | evolution record、ledger、PR/issue disposition |
| wake/review | 在相关时重新看 latent material | event、schedule、manual review、task trigger |

不要求七个独立工具；一个 Host organ 可以承担多个功能。

对每个功能可明确标记：`EXISTING | PROPOSE | IMPLEMENTED_AND_DRILLED | NOT_REQUIRED | NOT_APPLICABLE | UNKNOWN`。

## 与 Current machine artifact 的关系

Current 已提供 `evolution-record.v2` template/schema、validator 和窄的 `ena_evolve_v2.py` latent/migration helper。

`ena_evolve_v2.py` **不是完整 lifecycle engine**。Host 可以用它创建/迁移 candidate，但 expression、trial、evaluation、integration、dormancy、wake 可以由 Host-native 机制完成。

## Monitor / Stop

观察：signal 是否还会丢失、latent 是否在相关时被重新看到、trial 是否产生 decision-changing evidence、selected change 是否经得住真实使用、negative result 是否保留、循环本身花掉多少 token/时间/人力。

以下情况重新验证或缩减：Host/model/tooling 实质变化；recovery/authority boundary 改变；inbox/candidate 长期不再被调用；metric 开始被优化而不再代表目标；循环成本高于产生的 useful variation/evidence。

> **捕获有决策价值的压力，保存变异，接触现实，局部选择，保留证据，再继续观察。**
