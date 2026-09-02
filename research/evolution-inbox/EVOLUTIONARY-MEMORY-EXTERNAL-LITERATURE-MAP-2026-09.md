# Evolutionary Memory External Literature Map — 2026-09

Status: `RESEARCH MAP / EXTERNAL PRIOR-ART CHECK / NOT_CURRENT`

Purpose:

- avoid rediscovering existing work under new ENA vocabulary;
- identify which current ENA memory hypotheses already have adjacent evidence;
- isolate gaps that remain decision-relevant;
- prevent novelty claims from outrunning literature contact.

This map is based on public papers/surveys available through 2026-09. It is not a systematic review.

---

## 1. Field-level convergence: memory is already moving from storage toward experience

### Luo et al. 2026 — *From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms*

- Findings of ACL 2026.
- arXiv: `2605.06716`.
- Frames agent-memory evolution as:
  - **Storage** — trajectory preservation;
  - **Reflection** — trajectory refinement;
  - **Experience** — trajectory abstraction.
- Highlights proactive exploration and cross-trajectory abstraction as frontier mechanisms.

Relation to ENA:

- strongly confirms that `memory != simple storage/retrieval` is not a novel ENA claim;
- overlaps with ENA Memory Metabolism and current `preserved adaptation` framing;
- means ENA should not claim ownership of the broad “memory becomes experience” transition.

Remaining ENA emphasis:

- what exactly survives as a behavioral/metamemory change;
- how experience changes **future learning rules**;
- how learned changes are inherited across Agent/Host transitions;
- authority and selective permeability at the write-to-self layer;
- interaction effects among adaptations;
- propagation, recipient-side selection, and retirement.

---

## 2. Reflection without weight updates already demonstrates non-parametric experiential learning

### Shinn et al. 2023 — *Reflexion: Language Agents with Verbal Reinforcement Learning*

- NeurIPS 2023.
- arXiv: `2303.11366`.
- Agent reflects verbally on feedback and stores reflective text in episodic memory.
- Improves later trials without updating model weights.

Relation to ENA:

- validates a key feasibility point: behavior can improve through persistent linguistic memory without parametric retraining;
- still primarily stores/retrieves reflective text;
- does not by itself establish implicit disposition transfer, metamemory regulation, inheritance, or memory ecology.

ENA distinction:

`REFLECTIVE TEXT STORED != ADAPTIVE PHENOTYPE INHERITED`

---

## 3. Experience abstraction into reusable natural-language insight already exists

### Zhao et al. 2024 — *ExpeL: LLM Agents Are Experiential Learners*

- AAAI 2024.
- Agent gathers training-task experiences and extracts natural-language knowledge/insights.
- At inference it recalls both extracted insights and prior experiences.
- Reports transfer-learning potential without parameter access.

Relation to ENA:

- strong prior art for `experience -> abstraction -> reuse`;
- close to the idea that raw trajectories can be compiled into denser durable structures;
- does not settle applicability boundaries, causal credit, interaction debt, or heritability semantics.

ENA research should therefore avoid claiming that “compile experience into reusable lessons without weight updates” is new.

---

## 4. Skills are an existing form of preserved adaptation

### Wang et al. 2024 — *Voyager: An Open-Ended Embodied Agent with Large Language Models*

- TMLR 2024.
- Uses:
  - automatic curriculum;
  - ever-growing executable skill library;
  - iterative prompting with environmental feedback, errors, and self-verification.
- Avoids model parameter fine-tuning.
- Reuses learned skills in new Minecraft worlds.

Relation to ENA:

- executable skills are a clear example of experience becoming durable behavioral capability;
- supports the idea that memory can live in external executable structure, not only narrative records;
- skill reuse across new worlds is adjacent to property transfer/heritable behavior.

Open ENA questions:

- when should a skill stay local vs propagate;
- how should stale skills die;
- how do skills interact;
- can a successor inherit the *selection logic* that produced skills, not only the skills;
- how does recipient-side selection work across Hosts?

---

## 5. Dynamic associative memory networks already challenge flat retrieval

### Xu et al. 2025 — *A-MEM: Agentic Memory for LLM Agents*

- NeurIPS 2025.
- arXiv: `2502.12110`.
- Dynamically organizes memories using Zettelkasten-inspired notes, indexing and links.
- New memories can update contextual representations/attributes of existing memories.
- Explicitly describes this as memory evolution/refinement.

Relation to ENA:

- supports network/associative rather than purely linear memory organization;
- adjacent to the user’s original intuition that human memory is distributed and multi-entry;
- still primarily evolves representations in an external memory network.

ENA extension:

`MEMORY NETWORK EVOLVES != AGENT LEARNING POLICY EVOLVES`

---

## 6. Procedural memory is now an explicit agent-memory research target

### Fang et al. 2025 — *Memp: Exploring Agent Procedural Memory*

- arXiv: `2508.06433`.
- Distills prior trajectories into:
  - fine-grained step instructions;
  - higher-level script-like abstractions.
- Studies Build / Retrieval / Update strategies.
- Memory is continuously corrected and deprecated.
- Reports that procedural memory built by a stronger model can improve a weaker model after migration.

Relation to ENA:

This is one of the closest pieces of prior work to current ENA adaptive-inheritance research.

It provides adjacent empirical support for:

- `trajectory != best transfer unit`;
- procedural abstraction can migrate across model capability levels;
- memory needs update/deprecation rather than append-only accumulation.

Still-open ENA distinctions:

- procedural transfer vs inheritance of learned salience/metamemory;
- trigger/applicability preservation;
- causal-credit uncertainty;
- interaction fitness among multiple procedures;
- recipient-side selection;
- local vs germline eligibility;
- semantic inheritance without source vocabulary.

---

## 7. Dynamic procedural memory refinement already addresses passive accumulation

### Cao et al. 2025 — *Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution (ReMe)*

- arXiv: `2512.10696`.
- Multi-faceted distillation of successes, failure triggers and comparative insights.
- Context-adaptive reuse.
- Utility-based refinement that adds valid memories and prunes outdated ones.

Relation to ENA:

- strong prior art for `memory must be prunable / refinable / utility-sensitive`;
- close to Memory Metabolism’s supersession/retirement spirit;
- shows that “append-only memory is bad” is not new.

ENA’s additional concern:

> utility of an individual memory is insufficient if combinations create interaction debt or if high-propagation memories reduce Host fitness.

---

## 8. 2026 evidence directly supports abstract procedural memory over detailed trajectory in some settings

### Hu, Long, Wang 2026 — *When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents*

- arXiv: `2604.27003`.
- Argues that external memory does not remove the stability–plasticity problem; it moves the bottleneck to representation/retrieval.
- Sequential ALFWorld/BabyAI experiments report:
  - abstract procedural memories transfer more reliably than detailed trajectories;
  - negative transfer particularly harms difficult cases;
  - finer-grained organization is not universally better;
  - strong forward transfer can coexist with severe forgetting.

Relation to ENA:

This is especially important for current hypotheses.

It provides direct adjacent empirical evidence for:

`MORE DETAILED HISTORY != BETTER ADAPTIVE TRANSFER`

`FORWARD TRANSFER != NO FORGETTING`

`FINER MEMORY ORGANIZATION != UNIVERSALLY BETTER`

`TRANSFER BENEFIT != NO NEGATIVE TRANSFER`

This aligns strongly with:

- adaptive inheritance rather than full-history replay;
- portability as a distinct dimension;
- recipient/context fitness;
- representation compression with bounded decision distortion.

It does **not** yet validate ENA’s full adaptation-capsule or metamemory-sovereignty model.

---

## 9. Reflective retrieval management shows retrieval policy itself can learn

### Tan et al. 2025 — *In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents*

- ACL 2025.
- Prospective reflection summarizes at multiple granularities.
- Retrospective reflection refines retrieval using online reinforcement learning based on cited evidence.
- Reports improvements on LongMemEval.

Relation to ENA:

- retrieval policy need not remain fixed;
- close to a limited form of “memory management learns from use.”

Boundary:

This is still primarily a learned **retrieval manager**, not the broader ENA sense of metamemory as durable regulation of:

- source trust;
- consolidation eligibility;
- learning rate;
- generalization width;
- inheritance;
- propagation;
- forgetting.

---

## 10. Titans provides a neural test-time memory rather than archive retrieval

### Behrouz, Zhong, Mirrokni 2025 — *Titans: Learning to Memorize at Test Time*

- NeurIPS 2025.
- Introduces a neural long-term memory module updated while processing context.
- Uses a surprise-oriented learning signal to prioritize what the neural memory learns.
- Treats attention as precise short-term memory and neural memory as persistent long-term memory.

Relation to ENA:

- important evidence that memory can be a changing internal learned state at inference time rather than only retrieved external records;
- adjacent to `memory = preserved change` at the neural architecture level;
- surprise as a write signal is adjacent to ENA’s salience/prediction-error discussion.

Boundary:

`SURPRISE != BENEFICIAL ADAPTATION`

High surprise can justify attention/update priority but does not by itself establish purpose-relative fitness, authority, causal credit, or safe inheritance.

---

## 11. MIRAS explicitly separates memory architecture, attentional bias, retention, and learning algorithm

### Behrouz et al. 2025 — *It's All Connected: A Journey Through Test-Time Memorization, Attentional Bias, Retention, and Online Optimization*

- arXiv: `2504.13173`.
- Introduces MIRAS framework.
- Reinterprets sequence models as associative-memory systems with design choices for:
  1. memory architecture;
  2. attentional-bias objective;
  3. retention gate;
  4. memory learning algorithm.

Relation to ENA:

This is strongly adjacent to the idea that memory behavior depends not only on stored content but on:

- what gets attention;
- what gets retained/forgotten;
- what update algorithm changes memory.

It provides architectural prior art for several pieces that ENA calls salience, retention and learning regulation.

Remaining ENA level:

MIRAS operates primarily at sequence-model architecture/optimization level. ENA’s current research asks an Agent-level governance/evolution question:

> who/what has authority to alter those learning/retention rules, how are changes scoped/reversible, and what is inherited across Agents/Hosts?

---

## 12. Nested Learning / HOPE makes multi-timescale learning and learning-rule structure explicit

### Behrouz et al. 2025 — *Nested Learning: The Illusion of Deep Learning Architectures* / Google Research Nested Learning & HOPE

- NeurIPS 2025 / Google Research publication materials.
- Treats architecture and optimization as nested learning problems.
- Each level can have its own update frequency / context flow.
- Introduces continuum memory systems with multiple update timescales.
- HOPE is presented as a self-modifying architecture with nested in-context learning levels.

Relation to ENA:

Very important convergence with current ENA intuitions:

- memory can exist on multiple update timescales;
- what looks like model architecture vs learning algorithm can be viewed as different levels of learning;
- the “how future change happens” layer is itself a computational object.

This is close to the ENA distinction:

```text
memory = past changes future state
metamemory = past changes future change
```

Boundary:

ENA should not claim multi-timescale learning or nested update rules as novel.

ENA’s potential additional contribution is at Agent-level selection/governance:

- selective permeability;
- authority to mutate learning rules;
- recipient-side inheritance;
- causal-credit provenance;
- reversibility;
- propagation fitness;
- agency continuity.

---

## 13. Sleep-like offline replay has direct ANN evidence for continual-learning benefits

### Tadros et al. 2022 — *Sleep-like unsupervised replay reduces catastrophic forgetting in artificial neural networks*

- Nature Communications 2022.
- Adds an offline sleep-like phase with spontaneous replay/local plasticity.
- Reports recovery of old tasks and reduced catastrophic forgetting.

### van de Ven, Siegelmann, Tolias 2020 — *Brain-inspired replay for continual learning with artificial neural networks*

- Nature Communications 2020.
- Brain-inspired replay for continual learning.

Relation to ENA / recovered `ai-dreaming` lineage:

- external evidence exists for **offline replay as useful process** in neural continual learning;
- this supports taking sleep/replay analogy seriously as an engineering inspiration.

Important anti-overclaim:

- these ANN results do not validate ENA’s dream-text isolation, associative-temperature, memory integration-testing, or Agent-level adaptation compiler;
- `sleep-like replay works in ANN continual learning` does not imply `human dreaming mechanism has been reproduced`.

---

## 14. Knowledge distillation is mature prior art for transferring behavior without raw history

Continual-learning literature contains extensive knowledge-distillation approaches where a newer learner preserves prior behavior by matching outputs/representations rather than replaying all original data.

Example survey:

### Li et al. 2025 — *Continual Learning With Knowledge Distillation: A Survey*

- IEEE Transactions on Neural Networks and Learning Systems.
- Reviews distillation as a mechanism to preserve prior-task competence under continual learning.

Relation to ENA adaptive inheritance:

- the general idea `transfer selected behavior without full source dataset` is well established;
- ENA must therefore distinguish its proposed Agent-level carrier from ordinary knowledge distillation.

Potential ENA distinction:

> distillation typically transfers output/representation behavior; adaptive inheritance may also need to transfer **scope, provenance, trigger, causal uncertainty, retirement conditions and learning-policy regulation**.

---

## 15. Distributed/model consolidation also shows successor transfer without original data is possible

### Xue et al. 2026 — *Distillation-Guided Structural Transfer for Continual Learning Beyond Sparse Distributed Memory*

and related distributed continual-learning/model-consolidation literature show that useful behavior/representations can sometimes transfer between models without original training data.

Relation to ENA:

- again confirms that “inherit learning without replaying whole original history” is not conceptually unprecedented;
- strengthens the need to define what ENA means specifically by **adaptive lineage** rather than generic model distillation.

---

## 16. What appears well covered by existing work

Do **not** treat the following as novel ENA discoveries in isolation:

- external long-term memory;
- reflective memory;
- experience abstraction;
- skill/procedural memory;
- dynamic memory linking;
- memory updating/deprecation;
- test-time neural memory;
- surprise-driven write signals;
- explicit retention/forget gates;
- multiple memory timescales;
- offline replay for continual learning;
- knowledge distillation / behavior transfer without full raw history;
- “storage -> reflection -> experience” as a field-level framing.

---

## 17. Where the current ENA research may still have a distinctive synthesis

No novelty claim is made yet, but the following combination appears less directly covered by the inspected literature:

### 17.1 Memory as preserved adaptation **plus** explicit causal uncertainty

Not only:

> extract a lesson from a trajectory

but:

> preserve what evidence supports the lesson, what alternative causes remain, and how strong the causal credit is.

### 17.2 Interaction fitness among memories

Not only evaluate each memory's utility, but ask:

> do individually useful adaptations become harmful when co-expressed?

Candidate concept:

**adaptive interaction debt**.

### 17.3 Metamemory sovereignty

Not only learn retrieval/write/retention policy, but ask:

> who or what may legitimately change the rules that govern future learning?

Includes:

- source authority;
- selective permeability;
- reversible plasticity;
- learning-policy poisoning;
- temporal/future-self consequences.

### 17.4 Local / somatic vs heritable / germline adaptation

Explicitly separate:

`LOCAL USEFULNESS != INHERITANCE ELIGIBILITY`

and require recipient-side selection after Host transition.

### 17.5 Adaptive inheritance across Agent/Host changes

Carrier target is not just facts or a model checkpoint, but a package of:

- disposition;
- trigger;
- scope;
- evidence/provenance;
- counterexamples;
- interaction dependencies;
- retirement/revalidation conditions;
- propagation status.

### 17.6 Semantic/behavioral inheritance tests

Transfer success should survive removal of source jargon and be demonstrated on unseen equivalent cases.

`CARRIER COPIED != ADAPTATION INHERITED`

### 17.7 Memory-write authority as high-leverage authority

Persistent self-change can influence thousands of future actions; therefore memory/metamemory mutation authority may deserve different treatment from one-shot tool authority.

### 17.8 Purpose-relative memory fitness

A memory can be memorable, transferable and frequently reused while still reducing Host fitness.

`PROPAGATION FITNESS != BENEFICIAL FITNESS`

### 17.9 Recipient-side inheritance rather than donor sovereignty

A successful donor's adaptation remains a candidate under a new Host.

`DONOR FITNESS != RECIPIENT FITNESS`

### 17.10 Forgetting as preservation of evolvability

Not only solve catastrophic forgetting; also recognize the opposite failure:

> overconsolidation can freeze variation and create ritual/dogma.

---

## 18. Strongest external contact for the current next question

The closest current evidence found is the 2026 study:

> *When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents* (`2604.27003`).

Its reported result that abstract procedural memories can transfer more reliably than detailed trajectories directly motivates the next ENA question:

> **What is the smallest transferable representation that preserves future decision quality, scope and revisability better than either full history or a context-free rule?**

This is exactly where the proposed:

```text
ADAPTATION MAP
+
REPRESENTATIVE / BOUNDARY EXEMPLARS
+
COLD PROVENANCE
```

becomes a testable candidate rather than only a metaphor.

---

## 19. Recommended research posture after this literature contact

Do not rush to create a new memory architecture.

Next steps should be discriminating tests between plausible representations:

1. full-history / trajectory replay;
2. retrieval of episodic memories;
3. static summary;
4. abstract procedural memory;
5. procedural memory + scope/counterexample exemplars;
6. procedural memory + scope + provenance/causal uncertainty;
7. executable skill;
8. optional parametric/distilled carrier.

Measure not only success rate, but:

- transfer;
- negative transfer;
- overgeneralization;
- calibration;
- forgetting;
- interaction with pre-existing adaptations;
- context cost;
- ability to retire/delete source-derived effects;
- portability across Hosts/models;
- semantic retention after vocabulary stripping.

This would test an actual gap rather than merely reproduce the known result that “memory helps agents.”
