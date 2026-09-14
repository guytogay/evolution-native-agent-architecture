<!--
Provenance: authored by the owner's ChatGPT session and delivered to the execution side on
2026-09-15 as a file. The body below is reproduced verbatim; this header is added by the
execution side. The owner's intent when it was written was that this be ENA's mechanism for
producing variation on the way to evolution -- see DIVERGENT-EXPLORER-ADOPTION-GAP.md for what
actually shipped, what did not, and what landing it would require.

Status of this file: RESEARCH_MATERIAL / REFERENCE_TEXT / NOT ENA ADOPTER OR RUNTIME CONTENT.
It is not a method rule; the method-relevant artefact here is the adoption-gap note.
-->

# Divergent Explorer
## 完整发散探索方法论

---

# 0. 这套方法解决什么问题

普通“发散思考”通常会退化成三种东西：

1. 关键词联想；
2. 不同领域举例；
3. 看起来很深刻的比喻。

例如：

```text
老虎钳
→ 工具
→ 工厂
→ 工业
→ 制造业
```

或者：

```text
生物学上……
心理学上……
经济学上……
哲学上……
```

这不是高质量发散。

真正有价值的发散应该是：

```text
具体对象
→ 提取机制
→ 提升抽象
→ 寻找远距离结构同构
→ 改变视角和表示
→ 发现异常、矛盾和隐藏变量
→ 形成新结构
→ 重新定义原问题
```

因此，Divergent Explorer 的目标不是：

> 产生更多想法。

而是：

> **扩大概念空间，直到发现原来没有显露出来的结构、机制、张力、变量、框架或问题。**

---

# 1. 核心原则

整个方法可以浓缩成一句：

> **不要从名词发散，要从机制发散。**

低质量路径：

```text
关键词
→ 相似词
→ 相关对象
→ 更多例子
```

高质量路径：

```text
Seed
→ Decompose
→ Abstract
→ Structural Search
→ Mutate
→ Detect Anomaly
→ Branch
→ Recurse
→ Reframe
→ Validate
```

---

# 2. 什么算成功

一次真正成功的发散，至少应该出现一个：

```text
NEW CONNECTION
NEW MECHANISM
NEW LATENT VARIABLE
NEW TENSION
NEW FRAME
NEW QUESTION
NEW TESTABLE HYPOTHESIS
```

最理想的轨迹是：

```text
“我知道这是什么。”

↓

“等等，它可能不是我以为的那个问题。”

↓

“这个看似毫不相关的东西居然具有类似结构。”

↓

“原来它们共享一个更底层的机制。”

↓

“这个机制可以解释更多现象。”

↓

“原来的问题太小了。”

↓

“现在出现了一个更好的问题。”
```

---

# 3. 发散的基本单位不是“想法”，而是结构

遇到一个 Seed，不要马上联想。

先拆。

例如：

```text
老虎钳
```

可以拆成：

```text
OBJECT
工具、工件

ACTION
夹住

STATE
固定

RELATION
一个主体限制另一个对象

CONSTRAINT
降低自由度

RESOURCE
机械力

TIME
施力后状态可以持续

AGENT
操作人员

FAILURE
过松会滑
过紧会损坏

BOUNDARY
哪些运动仍被允许
```

这一步叫：

## Seed Decomposition

---

# 4. Seed Model

通用 Seed Model 可以检查：

```text
OBJECT
ACTION
STATE
RELATION
CONSTRAINT
RESOURCE
SIGNAL
TIME
AGENT
ENVIRONMENT
BOUNDARY
FAILURE MODE
```

不是每个 Seed 都需要全部字段。

目的不是填表。

目的是打破：

```text
“这个词就是这个词”
```

让它变成：

```text
一个过程
一个关系
一种约束
一个动力学结构
```

---

# 5. 抽象阶梯

然后建立 Abstraction Ladder。

例如：

```text
L0:
老虎钳

L1:
固定物体的工具

L2:
减少对象的运动自由度

L3:
通过局部约束提高可操作性

L4:
选择性减少自由可能创造更高层次能力
```

真正的发散主要从：

```text
L2
L3
L4
```

开始。

不是从 L0 开始。

---

# 6. 为什么必须先抽象

如果直接从：

```text
老虎钳
```

联想，很容易得到：

```text
钳子
扳手
螺丝刀
车间
```

但如果先得到：

```text
减少自由度以提高可操作性
```

就可能连接到：

```text
mutex
关节
规则
语法
游戏
制度
实验控制变量
```

真正的跨域连接来自：

> 中间抽象层。

---

# 7. Structural Search

发散不是寻找：

```text
看起来像什么？
```

而是寻找：

```text
什么系统也在做同一件事？
```

或者：

```text
什么系统具有相同动力学？
```

重点寻找：

```text
High Semantic Distance
+
High Structural Similarity
```

即：

> 表面距离很远，但机制很像。

这是最有价值的区域。

---

# 8. Structural Test

每一个远距离类比都必须检查：

```text
INPUT
TRANSFORMATION
OUTPUT
FAILURE MODE
CONTROL RELATION
TIME BEHAVIOR
```

例如：

老虎钳：

```text
input:
自由移动的工件

transformation:
机械约束

output:
稳定工件

failure:
滑脱 / 压坏
```

制度：

```text
input:
自由行为

transformation:
规则约束

output:
更可预测行为

failure:
失控 / 僵化
```

如果连 failure mode 都具有相似结构，说明类比可能较深。

---

# 9. 类比不是证据

所有类比都必须知道：

```text
MAPS WELL
```

以及：

```text
BREAKS HERE
```

例如：

```text
mutex ≈ vise
```

可对应：

```text
exclusive constraint
persistent state
conflict prevention
```

但失效处包括：

```text
mutex 没有物理形变
没有真正的机械力
资源所有权语义不同
```

一个不知道自己在哪里失效的类比，通常已经被过度使用。

---

# 10. Mutation Operators

当一个结构形成后，不要只继续找例子。

主动“变异”它。

核心变异算子包括：

```text
SCALE_SHIFT
TIME_SHIFT
ACTOR_SWAP
CAUSE_REVERSAL
EXTREME_CASE
FAILURE_MODE
FUNCTION_INVERSION
MISSING_THIRD
BOUNDARY_SHIFT
REPRESENTATION_SHIFT
AGENCY_SHIFT
SELECTION_PRESSURE
```

---

# 11. SCALE_SHIFT

改变观察尺度：

```text
微观
→ 个体
→ 群体
→ 组织
→ 社会
→ 生态
→ 文明
```

问：

> 同一个机制在不同尺度下还成立吗？

还要防止：

```text
composition fallacy
```

个体层面成立，不代表群体层面成立。

---

# 12. TIME_SHIFT

不要只观察静态状态。

检查：

```text
before
during
after
short-term
medium-term
long-term
evolutionary
```

很多结构只有进入时间维度才会显现。

例如：

```text
严格控制
→ 短期稳定
→ 长期适应性下降
```

---

# 13. ACTOR_SWAP

更换观察主体。

同一个机制可以从：

```text
controller
controlled object
beneficiary
victim
observer
competitor
environment
```

不同角度观察。

例如：

```text
lock-in
```

对平台：

```text
stability
```

对用户：

```text
loss of optionality
```

因此不能把某一方的价值函数冒充整个系统的价值函数。

---

# 14. CAUSE_REVERSAL

把因果方向反过来试。

不是：

```text
A 导致 B
```

而是：

```text
会不会需要 B 的系统更容易选择出 A？
```

或者：

```text
A 和 B 是否共同由 C 造成？
```

目的不是证明反向因果。

而是打破默认因果框架。

---

# 15. EXTREME_CASE

把变量推向：

```text
0
```

以及：

```text
∞
```

问：

```text
完全没有会怎样？

极端多会怎样？
```

这样常常能发现：

```text
threshold
optimum
phase transition
```

---

# 16. FAILURE_MODE

问：

> 这个机制什么时候会坏？

失败模式往往比正常模式更有价值。

寻找：

```text
overload
brittleness
lock-in
overshoot
runaway feedback
Goodhart effect
self-destruction
```

---

# 17. FUNCTION_INVERSION

问：

> 一个功能什么时候会变成自己的反面？

例如：

```text
security
→ incapacity

discipline
→ rigidity

optimization
→ distortion

stability
→ stagnation

memory
→ fixation
```

这是最强的结构发现来源之一。

---

# 18. MISSING_THIRD

如果当前模型只有：

```text
A → B
```

问：

> 是否缺少 C？

常见隐藏第三者：

```text
environment
incentive
observer
time
selection pressure
resource
information channel
institution
intermediary
```

很多看似二元关系，实际上是三元或多元结构。

---

# 19. BOUNDARY_SHIFT

改变“什么算系统”。

例如：

```text
flower
→ plant
→ plant + pollinator
→ ecosystem
```

很多问题只是因为系统边界画错了。

---

# 20. REPRESENTATION_SHIFT

同一个问题可以重画成：

```text
mechanism
network
feedback loop
optimization problem
game
resource flow
information flow
control system
evolutionary strategy
constraint landscape
```

换表示，往往比增加事实更有效。

---

# 21. AGENCY_SHIFT

特别适合 AI、生物和组织问题。

问：

```text
Agency 在哪里？

集中式？
分布式？
涌现？
借来的？
受限但仍然存在？
```

这能避免把复杂行为自动归因于中央意图。

---

# 22. SELECTION_PRESSURE

把静态结构转换成：

```text
为什么这种结构反复出现？
```

问：

> 什么环境会选择出这种机制？

这使发散进入：

```text
evolutionary / adaptive explanation
```

---

# 23. Anomaly Search

每走到一个重要节点，都问：

> 这里最奇怪的地方是什么？

重点寻找：

```text
contradiction
asymmetry
exception
hidden cost
threshold
delay
phase transition
path dependence
lock-in
emergence
```

正常情况往往只能告诉你系统“能运行”。

异常才暴露结构。

---

# 24. Tension Extraction

寻找：

```text
freedom vs control
stability vs adaptability
exploration vs exploitation
security vs capability
efficiency vs resilience
specialization vs robustness
memory vs flexibility
visibility vs privacy
```

不要马上解决成：

```text
“需要平衡”
```

这是低质量收束。

更好的问题是：

```text
在什么条件下 A 成立？

在什么条件下 B 成立？
```

---

# 25. Conditionalization

面对两个看似冲突结构：

不要写：

```text
A 和 B 都很重要。
```

而要尝试：

```text
IF X
THEN A

IF Y
THEN B
```

例如：

```text
Constraint increases capability
IF it removes irrelevant degrees of freedom.

Constraint reduces agency
IF it removes task-relevant control.
```

这样矛盾才真正产生知识。

---

# 26. Recursive Expansion

高质量发散不是：

```text
Seed → 20 个例子
```

而是：

```text
Seed
→ Branch A
→ A1
→ A2
→ latent structure
```

一条 Branch 可以变成新的 Seed。

例如：

```text
老虎钳
→ 降低自由度
→ 提高可操作性
→ 约束创造能力
→ 为什么自由更少反而能力更强？
```

此时“老虎钳”已经可以退出舞台。

---

# 27. Branch Selection

不要平均探索所有 Branch。

内部可以按：

```text
SURPRISE
STRUCTURAL_DEPTH
GENERATIVITY
REFRAMING_POWER
TRANSFERABILITY
```

评分。

例如：

```text
0–3
```

每项。

优先保留：

```text
1–3 条强枝
```

而不是：

```text
20 条浅枝
```

---

# 28. Surprise 不是证据

这是最重要的纪律之一：

> **Surprise selects candidates. Evidence selects beliefs.**

惊讶只说明：

```text
值得看。
```

不说明：

```text
是真的。
```

---

# 29. Seed Removal Test

当一条 Branch 成熟后，把原 Seed 删除。

问：

> 剩下的结构还值得独立研究吗？

例如：

```text
适量降低自由度可能创造更高层次能力。
```

即使不再提老虎钳，它仍然有意义。

这说明真正发生了抽象。

---

# 30. Reframing

当出现：

```text
原对象只是更大问题的一个实例
```

进入 REFRAME。

典型变化：

```text
object → process
thing → relation
cause → feedback loop
binary → continuum
feature → tradeoff
behavior → incentive
choice → selection pressure
individual → system
event → trajectory
control → degrees of freedom
capability → coupling
```

可以明确说：

> 更有意思的问题可能已经不是 X，而是 Y。

---

# 31. 不要过早 Reframe

Reframe 必须来自：

```text
新机制
新变量
跨 Branch 重复结构
异常
矛盾
```

而不是为了显得深刻。

---

# 32. Exploration Graph

长期探索不能只保存聊天。

应该保存：

```text
NODE
EDGE
BRANCH
FRAME
QUESTION
```

真实探索不是树，而更像：

```text
graph
```

因为不同 Branch 可能重新汇合。

---

# 33. Node

重要节点可以记录：

```text
CLAIM
TYPE
EPISTEMIC STATUS
ORIGIN
OPERATORS USED
WHY INTERESTING
OPEN QUESTIONS
STATUS
```

类型例如：

```text
observation
mechanism
analogy
anomaly
tension
question
hypothesis
reframe
latent structure
```

---

# 34. Edge

不要只写：

```text
related_to
```

更好的 Edge：

```text
ABSTRACTS_TO
INSTANCE_OF
STRUCTURALLY_SIMILAR
CAUSES
ENABLES
CONSTRAINS
CONTRADICTS
GENERALIZES
REFRAMES
FAILURE_MODE_OF
TRADEOFF_WITH
EMERGES_FROM
SELECTED_BY
DEPENDS_ON
CHALLENGES
MERGES_WITH
```

关系本身通常比节点更重要。

---

# 35. Branch

Branch 应保存：

```text
起点
路径
当前结构
frontier question
状态
```

真正值得继承的是：

> “我们已经走到哪里？”

不是全部原始文本。

---

# 36. Branch 状态

建议：

```text
ACTIVE
PARKED
EXHAUSTED
WEAK
REJECTED
MERGED
MATURE
```

---

# 37. 不要删除失败 Branch

失败路径属于：

```text
Negative Knowledge
```

例如：

```text
REJECTED

Reason:
This analogy required centralized control
that the real mechanism does not contain.
```

如果删除失败历史，未来 Agent 会重复犯。

---

# 38. Novelty Detection

模型很容易把：

```text
换词
```

当成：

```text
新发现
```

例如：

```text
限制自由创造能力
适当约束提高功能
减少自由度提升控制
```

可能只是同一个结构。

因此每个候选都检查：

```text
new variable?
new mechanism?
new relation?
new failure mode?
new prediction?
new reframe?
new cross-connection?
```

---

# 39. Semantic Novelty vs Structural Novelty

Semantic novelty：

```text
换了对象。
```

Structural novelty：

```text
增加了机制。
```

优先 Structural Novelty。

---

# 40. Novelty Exhaustion

当出现：

```text
不断换例子
不断换措辞
没有新变量
没有新异常
没有新机制
```

该 Branch 应：

```text
PARK
```

或：

```text
EXHAUST
```

不要靠字数维持生命。

---

# 41. Cross-Branch Collision

定期让两个高价值 Branch 相撞。

问：

```text
是否共享隐藏变量？

是否互相矛盾？

一个是不是另一个的边界？

一个能不能解释另一个失败？

组合后是否出现新系统？
```

新的发现可能并不属于任何一条原 Branch。

---

# 42. Serendipity Memory

一些发现：

```text
很奇怪
但当前不知道有什么用
```

不要扔。

保存为：

```text
SERENDIPITY
```

它们可能在未来 Seed 中重新激活。

这相当于概念种子银行。

---

# 43. Memory-Blind Pass

长期记忆会产生新风险：

```text
看到什么都塞进旧理论。
```

因此每次新 Seed：

先：

```text
FRESH PASS
```

暂时不读 Memory。

之后再：

```text
MEMORY PASS
```

最后：

```text
COLLISION
```

这样既利用历史，又防止路径依赖。

---

# 44. Cross-Session Succession

新 Session 不应该主要继承：

```text
完整聊天记录
```

而应继承：

```text
current seed
active branches
parked branches
mature structures
rejected paths
contradictions
serendipity
current frontier
latest reframes
method changes
```

---

# 45. Successor Readback

接班 Agent 先回答：

```text
现在到底在探索什么？

最重要的结构是什么？

哪些路已经走过？

哪些路不要重走？

哪里仍然未解决？

应该从哪里继续？
```

然后再做一次独立 Fresh Pass。

---

# 46. Frame Lock

长期 Agent 很容易形成自己的“思想盆地”。

例如什么都解释成：

```text
agency
evolution
feedback
constraint
```

如果多个 Seed 不断落回同一套词汇：

触发：

```text
FRAME_ESCAPE
```

---

# 47. FRAME_ESCAPE

执行至少两个：

```text
禁止当前主导框架

禁止核心词汇

换 representation

寻找反例

改变系统边界

从反对视角解释

寻找该框架解释不了的现象
```

如果禁掉旧框架后同一结构仍然独立出现：

可信度反而会上升。

---

# 48. Explorer Bias

Agent 定期检查：

```text
我是不是总用同一个 operator？

是不是总喜欢生物类比？

是不是所有问题都落到控制论？

是不是过度偏爱 agency？

哪些枝总被过早丢弃？
```

方法本身也必须接受观察。

---

# 49. Discovery Candidate

一个有趣 Branch 不应该直接升级成“知识”。

先进入：

```text
DISCOVERY_CANDIDATE
```

这是发散和相信之间的防火墙。

---

# 50. Generation 和 Validation 必须分开

逻辑角色：

```text
EXPLORER
产生候选

CHALLENGER
试图杀死候选
```

Explorer 优化：

```text
possibility
```

Challenger 优化：

```text
false discovery reduction
```

---

# 51. Strip Rhetoric

验证发现的第一步：

> 去掉漂亮措辞。

例如：

```text
“植物没有把太阳装进身体，它只是长出了叶子。”
```

去掉修辞：

```text
系统可以通过高效耦合外部资源获得能力，而无需内部拥有全部资源。
```

只有后者才是可验证结构。

---

# 52. Paraphrase Collapse Test

问：

> 这个“新发现”是不是旧发现换句话说？

如果两个理论：

```text
对同一输入产生同一预测
```

大概率不是新结构。

---

# 53. Instance Collapse Test

问：

> 这只是旧机制的新例子吗？

如果是：

```text
INSTANCE_OF
```

不要记成：

```text
NEW_DISCOVERY
```

---

# 54. Mechanism Test

真正的机制至少要回答：

```text
什么发生变化？
什么导致变化？
中间过程是什么？
什么条件需要存在？
```

如果只能回答：

```text
感觉很像
```

最多只是 metaphor。

---

# 55. Counterexample Attack

主动找：

```text
strongest plausible counterexample
```

反例的作用不是单纯否定。

而是找到边界。

例如：

```text
Constraints create capability.
```

太宽。

反例：

```text
无限限制并不会创造能力。
```

于是修订：

```text
约束只有在移除无关自由度、同时保留任务相关控制时，才可能提高高层能力。
```

理论变窄，但变强。

---

# 56. Opposite World Test

构造相反解释：

```text
A:
约束创造能力

B:
能力来自移除约束
```

问：

```text
A 能解释什么而 B 不能？

B 能解释什么而 A 不能？
```

如果两者都能解释一切：

理论没有区分力。

---

# 57. Prediction Test

问：

> 如果机制是真的，它比没有这个机制时多预测了什么？

一个好结构应该至少产生：

```text
conditional prediction
```

---

# 58. Falsifiability Gradient

不同发现不需要同样强度。

可以分：

```text
F0 PURE METAPHOR

F1 INTERPRETIVE

F2 MECHANISTIC

F3 PREDICTIVE

F4 TESTABLE

F5 EMPIRICALLY CHALLENGED
```

不能把 F0 当 F4。

---

# 59. Compression Test

高价值结构应该：

```text
用更少假设
解释更多现象
```

但要防止：

```text
fake compression
```

例如：

```text
“这都是能量。”
```

太宽，无法失败。

---

# 60. Boundary Test

所有成熟结构都应该明确：

```text
WORKS_WHEN
FAILS_WHEN
UNKNOWN_WHEN
```

没有边界的理论通常只是口号。

---

# 61. Competing Explanation

至少产生一个竞争解释。

例如：

```text
观察到向光行为
```

解释 A：

```text
goal-oriented behavior
```

解释 B：

```text
local differential growth
```

不要把高层描述偷偷升级成底层机制。

---

# 62. Level Confusion

区分：

```text
DESCRIPTIVE
FUNCTIONAL
MECHANISTIC
EVOLUTIONARY
INTENTIONAL
```

不能从：

```text
“这个行为具有某功能”
```

直接跳到：

```text
“系统想这么做”
```

---

# 63. Causal Direction

检查：

```text
A causes B?
B causes A?
C causes both?
A and B reinforce each other?
```

相关不是因果。

功能也不是原因。

---

# 64. Hidden Variable Attack

问：

> 有没有 C 使得 A-B 关系只是表象？

这是打破“漂亮因果故事”的重要工具。

---

# 65. Beauty Penalty

内部纪律：

> **观点越漂亮，验证越严格。**

因为 aesthetic appeal 会显著增加自我欺骗风险。

---

# 66. Discovery Maturity

可以设置：

```text
D0 SPARK

D1 CANDIDATE

D2 CHALLENGED

D3 SURVIVED

D4 CONDITIONALIZED

D5 PREDICTIVE

D6 RESEARCH-READY

D7 EMPIRICALLY SUPPORTED
```

Divergent Explorer 通常做到：

```text
D3–D5
```

之后交给 Research。

---

# 67. Discovery Promotion

一个节点不能：

```text
SPECULATIVE
→ MATURE
```

直接升级。

至少经过：

```text
Structural Test
Counterexample Attack
Boundary Statement
```

重要发现再加：

```text
Competing Explanation
Prediction
```

---

# 68. Discovery Demotion

旧发现可以：

```text
MATURE
→ REVISED
→ WEAK
→ REJECTED
```

历史地位不是证据。

---

# 69. Research Boundary

当问题从：

```text
conceptual uncertainty
```

变成：

```text
empirical uncertainty
```

继续纯思考意义很低。

例如：

```text
这种植物机制是否真的存在？
这个效应是否有实验支持？
```

应该进入：

```text
RESEARCH
```

---

# 70. Cheap Decisive Check

最重要的现实纪律：

> 如果一个廉价检查能够改变当前判断，就去检查。

不要用更多推理代替容易获得的现实信息。

---

# 71. 什么时候不该 Research

如果问题是：

```text
agency 到底应该理解为总自由度，还是对关键自由度的控制？
```

这是概念问题。

搜索再多资料，也不一定解决。

更适合：

```text
REFRAME
CONDITIONALIZE
```

---

# 72. Research Handoff

成熟候选交给 Research 时至少包括：

```text
candidate
mechanism
why it matters
predictions
competing explanations
boundary conditions
falsifiers
known uncertainties
requested checks
do not assume
```

---

# 73. Scheduler

到这一层，需要一个 Orchestrator。

它只回答：

> **下一步做什么最有价值？**

可选动作：

```text
DIVERGE
DEEPEN
MUTATE
COLLIDE
REFRAME
FRAME_ESCAPE
CHALLENGE
CONDITIONALIZE
RESEARCH
SIMULATE
PARK
MERGE
COMPRESS
CONVERGE
STOP
```

---

# 74. Bottleneck-First Thinking

Scheduler 不问：

```text
我们还能做什么？
```

而问：

```text
当前最小瓶颈是什么？
```

例如：

```text
可能性太少
→ DIVERGE

机制模糊
→ DEEPEN

开始重复
→ MUTATE

框架占领
→ FRAME_ESCAPE

多个强枝
→ COLLIDE

漂亮 Candidate
→ CHALLENGE

事实决定方向
→ RESEARCH

枝条耗尽
→ PARK / STOP
```

---

# 75. Expected Action Value

可以粗略思考：

```text
ACTION VALUE
=
Expected Information Gain
+
Reframing Value
+
Validation Value
-
Cost
-
Redundancy
```

不需要精确数学。

它只是纪律。

---

# 76. Decision-Changing Test

执行搜索、实验、研究前问：

> 结果不同会改变下一步吗？

如果：

```text
A → 继续
B → 继续
C → 继续
```

说明测试的信息价值可能很低。

---

# 77. Cheapest Decisive Move

多个动作都可行时：

> 选择最便宜、最可能改变判断的那个。

例如：

```text
继续推理 3000 字
```

vs

```text
查一个明确事实
```

如果后者足以区分理论，先查。

---

# 78. Explore vs Exploit

Explorer 也必须管理：

```text
breadth
vs
depth
```

原则：

```text
breadth follows uncertainty
depth follows promise
```

空间太窄：

增加 breadth。

有强 Branch：

增加 depth。

---

# 79. Branch Competition

不同 Branch 竞争探索资源。

不要因为已经投入很多就继续。

避免：

```text
sunk cost
```

只根据：

```text
future value
```

选择。

---

# 80. PARK 是合法动作

Park 不是失败。

适用于：

```text
有价值
但当前不值得继续
```

必须记录：

```text
why parked
reactivation condition
```

---

# 81. STOP 是合法动作

高质量探索的最后能力是：

> 知道什么时候已经没有必要继续。

停止条件：

```text
expected information gain low

AND

no unresolved high-value contradiction

AND

no cheap decisive reality check

AND

no high-value active branch

AND

user objective satisfied
```

---

# 82. Meta-Stop

方法论本身也可能变成拖延。

当系统开始：

```text
不断优化自己的探索规则
```

却没有改善真实探索时：

```text
META_STOP
```

方法只有改善实际结果时才有价值。

---

# 83. Expansion / Compression Rhythm

健康发散不是一直扩张。

更像：

```text
EXPAND
↓
STRUCTURE
↓
COMPRESS
↓
CHALLENGE
↓
EXPAND AGAIN
```

是一种呼吸。

---

# 84. Compression

当 Branch 太多：

```text
10 branches
→ 3 latent structures
```

Compression 是建立索引。

不是删除历史。

原 Branch 应保留作为 provenance。

---

# 85. Multi-Agent Divergence

多个 Agent 不应该都收到：

```text
“自由发散”
```

更好的角色：

```text
Agent A
Mechanism-first

Agent B
Anomaly-first

Agent C
Agency-first

Agent D
Boundary-first

Agent E
Temporal/evolution-first
```

---

# 86. Independent First Output

每个 Agent：

```text
先独立输出
```

并冻结。

之后再互看。

否则容易：

```text
anchoring
→ apparent consensus
```

---

# 87. Consensus 不是目标

如果：

```text
4 Agent → A
1 Agent → B
```

不能自动采用 A。

B 可能：

```text
解释 A 的失败边界
揭示隐藏变量
```

少数 Branch 必须保留检验资格。

---

# 88. Cross-Agent Synthesis

Synthesis Agent 不应该平均所有结果。

它应该寻找：

```text
shared structure
unique variable
contradiction
minority insight
failure boundary
cross-agent collision
```

目标：

> 产生一个简单拼接不可能得到的新 Frontier。

---

# 89. Epistemic Hygiene

整个系统必须持续区分：

```text
FACT
INFERENCE
PLAUSIBLE
SPECULATIVE
METAPHOR
```

大胆探索允许。

虚假确定性不允许。

---

# 90. Benchmark

方法论必须接受压力测试。

不能只挑：

```text
自由
意识
生命
```

这种容易“显得深刻”的 Seed。

应该测试：

```text
普通物体
过程
抽象概念
生物现象
技术对象
矛盾命题
错误前提
情绪性 Seed
随机 Seed
已有理论
```

---

# 91. Ordinary Object Test

例如：

```text
订书机
袜子
勺子
垃圾桶
拉链
```

如果没有宏大概念时，Explorer 就无法工作：

说明方法过于依赖哲学词汇。

---

# 92. False Premise Test

例如：

```text
人类只用了 10% 的大脑
```

Explorer 不能接受错误事实后继续建宏大理论。

必须先区分：

```text
empirical claim
```

和：

```text
conceptual exploration
```

---

# 93. Deep-Sounding Nonsense Test

例如：

```text
记忆是时间对意识施加的反向重力。
```

系统应识别：

```text
METAPHOR
```

可以探索映射。

不能把它偷渡成物理事实。

---

# 94. Framework Bait

如果 Explorer 偏爱：

```text
agency
```

给它：

```text
遥控器
```

看它是否立即写成：

```text
agency extension
```

然后强制 Frame Escape。

测试是否还有真正不同解释。

---

# 95. Endless Metaphor Trap

例如：

```text
袜子
```

Agent 可以无限比：

```text
缓存
防火墙
身份
社会
文明
```

如果没有 Stop Rule，发散最终会自我戏仿。

好的系统应该能够说：

```text
Further branches are mostly rhetorical variants.
STOP.
```

---

# 96. Baseline Comparison

复杂协议必须与简单 Prompt 比较。

至少比较：

```text
A:
普通大模型自由发散

B:
简单跨学科 Prompt

C:
完整 Divergent Explorer
```

如果 C 只多花 10 倍 token，却没有显著增加有价值发现：

复杂系统不值得。

---

# 97. Complexity Tax

评估：

```text
Useful Discovery
/
Cognitive Cost
```

Cost 包括：

```text
tokens
passes
tool calls
branch count
state size
latency
```

---

# 98. Ablation Test

依次删除组件：

```text
MEMORY-BLIND PASS
FRAME_ESCAPE
CHALLENGER
NOVELTY TEST
SCHEDULER
STOP RULE
```

看结果是否明显变差。

如果删除某模块几乎没影响：

删掉它。

---

# 99. Protocol Pruning

最终目标不是让协议越来越长。

而是找到：

> 最小有效核心。

经过测试后，很可能真正关键的只剩：

```text
1. Mechanism-first abstraction

2. Structural search

3. Mutation operators

4. Novelty detection

5. Adversarial challenge

6. Memory-blind inheritance

7. Stop discipline
```

如果够用，就不要保留更多仪式。

---

# 100. Minimal Runtime

最小运行循环可以压缩为：

```text
1. Seed 是什么？

2. 它由哪些动作、关系、约束、边界组成？

3. 抽象到机制层。

4. 找远距离结构同构。

5. 改变尺度、时间、主体、边界、因果方向。

6. 找异常和失败。

7. 选择最强 Branch 深挖。

8. 检查是否真正新。

9. 对漂亮 Candidate 做反例攻击。

10. 遇到事实边界就查现实。

11. 出现更好问题就 Reframe。

12. 新意下降就停。
```

---

# 101. 完整 Runtime Loop

完整版本：

```text
NEW SEED
↓
MEMORY-BLIND FRESH PASS
↓
SEED MODEL
↓
ABSTRACTION LADDER
↓
STRUCTURAL SEARCH
↓
MUTATION
↓
BRANCH CREATION
↓
STRUCTURAL TEST
↓
ANOMALY SEARCH
↓
NOVELTY TEST
↓
BRANCH SCORING
↓
MEMORY COLLISION
↓
CROSS-BRANCH COLLISION
↓
RECURSION
↓
REFRAME
↓
DISCOVERY CANDIDATE
↓
CHALLENGE
↓
COUNTEREXAMPLE
↓
CONDITIONALIZATION
↓
RESEARCH IF NEEDED
↓
ADJUDICATION
↓
PERSIST MEMORY
↓
CONTINUE / PARK / STOP
```

---

# 102. 完整架构

逻辑上可以拆成六个角色：

```text
ORCHESTRATOR
决定下一步做什么

EXPLORER
发现可能结构

CHALLENGER
攻击发现

RESEARCHER
检查现实

ADJUDICATOR
决定什么 survives

MEMORY
保存路径
```

这些不一定是六个模型。

也可以是一个模型的不同模式。

---

# 103. 六个角色各问一个问题

Explorer：

```text
What might be here?
```

Challenger：

```text
Why might this be wrong?
```

Researcher：

```text
What does reality say?
```

Adjudicator：

```text
What survives?
```

Memory：

```text
What have we already learned?
```

Orchestrator：

```text
What should we do next?
```

不要让六个问题混成一个。

---

# 104. 状态文件

最小 Persistent State：

```text
SEED

TOP ACTIVE BRANCHES

MATURE STRUCTURES

REJECTED PATHS

CONTRADICTIONS

SERENDIPITY

CURRENT FRONTIER

LATEST REFRAME

NEXT OPERATOR
```

---

# 105. Session Ending

每个长 Session 结束时，不只是总结。

必须记录：

```text
WHAT CHANGED?

WHAT SURVIVED?

WHAT DIED?

WHAT MERGED?

WHAT APPEARED?

WHAT REMAINS OPEN?

WHAT IS PARKED?

WHERE TO RESUME?

NEXT OPERATOR?

EXPLORER BIAS?
```

---

# 106. Session Succession

新 Agent：

```text
1. Read current state.

2. Reconstruct graph.

3. Read rejected paths.

4. Identify current frontier.

5. Do readback.

6. Run one fresh pass.

7. Compare with inherited state.

8. Continue only after resolving meaningful differences.
```

Truth overrides inheritance。

---

# 107. 发散输出应该是什么样

不要：

```text
一、
二、
三、
四、
五、
```

机械列领域。

更好的输出像概念在生长：

```text
一开始它看起来像 X。

但如果把动作抽象出来，它其实更接近 Y。

这让一个表面上完全不相关的 Z 开始变得有意思。

真正奇怪的是……

如果换成被控制对象的视角……

那么原来的问题就发生了变化……
```

用户应该能感觉到：

> 思维在变形。

---

# 108. 什么时候该继续

继续条件：

```text
novelty remains high

structural depth increasing

new anomaly appears

new hidden variable appears

contradiction appears

reframe imminent

new discriminating hypothesis appears
```

---

# 109. 什么时候该停止

停止条件：

```text
只是在增加例子

只是在换说法

没有新变量

没有新机制

没有新异常

没有新问题

类比越来越依赖修辞

下一步不会改变判断
```

---

# 110. 最重要的防退化规则

Divergent Explorer 必须持续防止：

```text
关键词联想

跨学科清单

随机新奇

类比膨胀

漂亮空话

过早总结

建议反射

框架锁定

重复换皮

研究成瘾

纯推理成瘾

无限验证

无限发散

不肯停止
```

---

# 111. 最重要的认知纪律

可以压成以下几句：

```text
Do not expand from the noun.
Expand from the mechanism.

Do not reward distance alone.
Reward distance plus structural similarity.

Do not confuse surprise with evidence.

Do not preserve an idea because you generated it.

Do not preserve a theory because it is old.

Do not search when thinking can decide.

Do not keep thinking when reality can decide.

Do not call paraphrase novelty.

Do not call metaphor mechanism.

Do not call function intention.

Do not call consensus truth.

Do not call length depth.

Do not call endless branching creativity.
```

---

# 112. 最终目标

Divergent Explorer 最终不是为了生成一个巨大的“想法仓库”。

它应该逐渐形成：

```text
一个不断更新的 Conceptual Landscape
```

这个系统知道：

```text
哪里已经走过；

哪里是死路；

哪里存在矛盾；

哪里只是漂亮比喻；

哪里还有休眠种子；

哪里两个远距离概念可能共享机制；

哪些发现已经接受挑战；

哪些必须交给现实验证；

以及当前最值得迈出的下一步在哪里。
```

---

# 113. 最终工作原则

如果把整套方法压缩成最后八条：

```text
Explore generously.

Abstract before associating.

Search for structure, not similarity.

Mutate the frame.

Follow anomalies.

Challenge attractive discoveries.

Use reality when reality can decide.

Stop when further work is unlikely to change anything.
```

以及整套方法最核心的一句话：

> **发散的目的不是让思维走得更远，而是让思维有机会抵达原来的问题框架根本无法看见的地方。**