# ENA v0.3.6 — 请先阅读

状态：**CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE**

本目录是 ENA 唯一面向采用者的 Current 基线。

**ENA 的存在，是为了让持续的自我进化成为一种可行能力。**

v0.3.6 在 v0.3.5“进化代谢”的基础上，正式加入“进化生态”层：

`环境/刺激 -> 变异压力 -> 变异 -> 潜伏保存或表达 -> 接触现实 -> 局部选择 -> 保留/休眠/消失 -> 迁移/重组 -> 再次产生变异`

进化是目的；治理保护可进化性。

## 建议先读

1. `../../CURRENT-BASELINE.yaml` — Current 身份、范围、谱系、机器边界、已接受残差；
2. `RUNTIME-ADOPTION-KERNEL.md` — 中文热路径语义；
3. `01-CONSTITUTION.md` — 38 条稳定普适不变量；
4. `09-EVOLUTION-METABOLISM.md` — 变异压力、潜伏、表达、局部选择、迁移/重组与救援；
5. `CONSTITUTION-CONCEPT-MAP.md` — Constitution 的触发/概念索引；
6. `projection-manifest.yaml` — 本中文投影与 v0.3.6 Current 的绑定及已知缺口。

## 本版关键区分

- `刺激 != 变异 != 改进`；
- 一个变异可以长期潜伏，不欠现实一个立即判决；
- `已保存 != 已表达 != 已应用 != 已选择`；
- 生命周期、表达状态、选择状态是三个不同问题；
- `整合 != 已被证明有益`；
- `归档/退役 != 选择结论`；
- 某个环境里的成功默认只是局部选择，不是普适适应度；
- `已发布 != 已导入 != 已表达 != 已在本地选择`；
- 流行程度和传播次数不能自动变成证据；
- 来源上下文/来源证据不等于接收方本地证明；
- 救援权限不等于对所有变异的审批权；
- 状态回滚不等于外部后果被撤销；
- GitHub 是目前承载规范谱系的工具，不是永久最高主权者；
- 最小干预不代表可以忽略不属于自己的后果。

## Constitution 状态

仍然是 38 个 Constitution ID，v0.3.6 没有新增第 39 条。

`NEW_CONSTITUTION_IDS = 0`

独立反证支持保留进化生态语义内核；被发现的重大机器契约问题已经在 candidate.1 中修复，而不是靠增加宪法条文解决。

## 机器层边界

v0.3.6 Current 正式包含：

- `evolution-record.v2` schema/template；
- v2 consistency validator；
- `adaptation-packet.v2` 表示契约；
- 继承的 v1 schema 和 v0.3.5 `ena_evolve.py` 参考工具。

但继承的 `tools/ena_evolve.py` 仍是 state/schema 1.2，没有完整实现变异压力、潜伏库、表达轴或 packet-v2 runtime。它的 `propose` / `import` 仍强制要求 `--variation-space`，所以它**不是** v0.3.6“先潜伏、以后再决定实验表面”路径的规范实现。

不要因为 schema/文档已经支持，就声称继承工具已经完整执行。

## Field evidence 边界

Current 状态是 `FIELD_VALIDATION`，不是普适证明。

尤其还需要现实证据回答：

- cue 是否会在未来 session 里自然唤醒正确语义；
- 大规模潜伏变异会不会成为垃圾堆；
- 表达状态在多少场景下真正对应行为影响；
- Rescue Plane 在现实部署中是否能保持窄权限；
- EN/zh-CN 的新生态语义是否保持行为级决策等价；
- 继承工具边界是否会给实际使用造成困惑。

## 已接受的可见残差

- 自己写 `provenance: LOCAL` 不是外部认证；
- `triggered_obligation_refs` 结构存在不等于引用真实性已认证；
- 并列“最新”时间戳当前采取保守拒绝；
- 继承工具的 latent propose/import 假阴性仍是明确的非规范实现边界。

这些是 field/research 机会，不是隐藏在发布声明里的“已解决”。

> **变异不欠现实一个立即判决。**
>
> **被保存的可能性，不等于正在生效的权限。**
>
> **治理底层，让生态在其上生长。**
