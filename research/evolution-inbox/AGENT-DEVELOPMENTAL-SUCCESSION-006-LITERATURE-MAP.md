# Agent Developmental Succession 006 — Literature Map

Status: `RESEARCH CONTACT / EXTERNAL LITERATURE / NOT_CURRENT`

Purpose: prevent ENA from relabeling existing work as novelty, while identifying narrower open questions that remain useful.

Search contact date: 2026-09-02.

---

## 1. ReMe — dynamic procedural memory

**Cao et al. (Findings ACL 2026), _Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution_.**

Source: https://aclanthology.org/2026.findings-acl.829/

Relevant result:

- treats passive append-only procedural memory as insufficient;
- distills successes, failure triggers and comparative insights;
- adapts reuse to context;
- refines/prunes memory by utility;
- reports a memory-scaling effect in which Qwen3-8B + ReMe outperforms a larger memoryless Qwen3-14B on reported tasks.

ENA implication:

Do not claim novelty for dynamic procedural-memory refinement or the general idea that experience-driven memory can improve later Agent performance.

Open ENA pressure remains around causal credit, interaction fitness, authority, inheritance and recipient-side selection.

---

## 2. MCMA — learning how to remember

**Liang et al. (Findings ACL 2026), _Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory_.**

Source: https://aclanthology.org/2026.findings-acl.1535/

Relevant result:

- treats memory abstraction as a learnable cognitive skill rather than a fixed representation;
- separates task execution from a learned memory copilot;
- organizes memories at multiple abstraction levels;
- when a particular memory is not transferable, transfers the ability to manage/abstract memory through the copilot;
- reports gains in OOD generalization and cross-task transfer on ALFWorld, ScienceWorld and BabyAI.

ENA implication:

Do not claim novelty for the generic idea of `learning how to remember` or transferable memory-management policies.

Current ENA-specific questions are narrower:

- who/what may mutate the memory-management policy;
- how such mutation remains reversible;
- how authority differs from mere influence;
- whether a successor should inherit a memory-management policy verbatim or locally redevelop it;
- how to detect self-sealing or hostile metamemory.

---

## 3. AgeMem — memory operations learned as policy

**Yu et al. (ACL 2026), _Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents_.**

Source: https://aclanthology.org/2026.acl-long.981/

Relevant result:

- exposes store/retrieve/update/summarize/discard as memory actions;
- trains the Agent to decide what and when to do with memory;
- jointly manages short- and long-term memory rather than relying only on fixed heuristics.

ENA implication:

Memory policy can itself be an action-selection problem. ENA's additional concern is that memory-write and metamemory-write actions have unusually large future leverage and therefore need authority/provenance/selection analysis, not only performance optimization.

---

## 4. LifelongAgentBench — replay is not enough

**Zheng et al. (2025), _LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners_.**

Source: https://arxiv.org/abs/2505.11942

Relevant result:

- benchmark explicitly targets lifelong learning in LLM Agents;
- reports that conventional experience replay can have limited effectiveness because of irrelevant information and context-length pressure.

ENA implication:

Do not assume full-history replay is a strong inheritance baseline merely because it preserves more raw evidence.

This supports testing:

`MORE HISTORY != MORE EXPERIENCE TRANSFER`

without yet proving the proposed Minimum Developmental Set.

---

## 5. CRPS — curriculum replay

**Zhang & Yang (Findings ACL 2026), _CRPS: Curriculum Replay via Progressive Suffixes from Successful Trajectories for Long-Horizon LLM Agents_.**

Source: https://aclanthology.org/2026.findings-acl.680/

Relevant result:

- turns successful trajectories into a progressive curriculum;
- adapts replay difficulty to current competence;
- reports improvements over full-episode GRPO and naive replay on ALFWorld and WebShop.

ENA implication:

Do not claim novelty for curriculum replay or competence-sensitive staging.

Open question:

> Can a selected curriculum reconstruct an ancestor's **scope-sensitive adaptive phenotype**, rather than only make task training easier?

---

## 6. TeachCraft — knowing is not teaching

**Wang et al. (ACL 2026), _From Knowing to Teaching: Scaffolding Pedagogical Decisions for LLM Agent_.**

Source: https://aclanthology.org/2026.acl-long.1328/

Relevant result:

- explicitly separates possessing knowledge from transforming it into teachable form;
- highlights content selection, sequencing and synthesis as distinct pedagogical decisions.

ENA implication:

This is a strong neighboring analogy for developmental inheritance:

`KNOWING ANCESTRAL EXPERIENCE != TEACHING A SUCCESSOR`

The inheritance carrier may need pedagogical transformation, not raw memory export.

---

## 7. Developmental robotics — staged skill acquisition and learning progress

### Stefik & Price (2023)

_Bootstrapping Developmental AIs: From Simple Competences to Intelligent Human-Compatible AIs._

Source: https://arxiv.org/abs/2308.04586

Relevant idea:

- developmental AI begins with limited innate competences and acquires further capabilities through interaction;
- emphasizes experiential development and bootstrapping rather than only static pretraining.

### Baranes/Oudeyer-line developmental robotics work

Representative source:

https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00833/full

Relevant results/ideas:

- intrinsic motivation based on learning progress;
- self-generated goals;
- developmental stages;
- continual skill acquisition;
- moving attention toward unknown but learnable regions.

Additional representative source:

https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2013.00011/full

Relevant idea:

- a developmental period can be used to discover reusable skills before a particular external task is imposed;
- intrinsic motivation can decide where learning effort should be allocated.

ENA implication:

Do not claim novelty for developmental stages, intrinsic motivation, curriculum emergence, competence progress or bootstrapping AI development.

The ENA branch specifically asks how those ideas interact with:

- LLM-Agent succession;
- memory ecology;
- inheritance across Hosts/models;
- boundary exemplars;
- provenance;
- local rejection of inherited adaptations;
- authority and viable agency.

---

## 8. Timeline-based dialogue memory — old states can remain useful as history

**Ong et al. (NAACL 2025), _Towards Lifelong Dialogue Agents via Timeline-based Memory Management_.**

Source: https://aclanthology.org/2025.naacl-long.435/

Relevant result:

- argues that outdated memories can still provide useful context about how a user changed;
- links memories temporally/causally rather than simply deleting old states.

ENA implication:

Supports the distinction:

`REMEMBERED PERSON != CURRENT PERSON`

while preserving:

> historical truth about what the person used to prefer or do.

A mature Agent should be able to retain change history without freezing the user into an old state.

---

## 9. Current novelty posture

The literature already gives strong prior art for:

- procedural memory;
- dynamic refinement/pruning;
- memory abstraction;
- learned memory management;
- curriculum replay;
- developmental stages;
- learning-progress-driven exploration;
- lifelong Agent evaluation;
- timeline/causal memory.

Therefore the current ENA research should avoid novelty claims around those generic ideas.

Potentially less-saturated combinations that still deserve investigation include:

1. **Adaptive inheritance without full-history replay**
   - transfer of scoped dispositions + boundary exemplars + cold provenance.

2. **Minimum Developmental Set**
   - optimize for reconstruction of useful future phenotype rather than representation of past history.

3. **Metamemory sovereignty**
   - separate influence, authority and evidence for mutation of learning rules.

4. **Recipient-side selection**
   - ancestral success does not grant descendant obligation.

5. **Adaptive interaction fitness**
   - individually useful memories can combine into a maladaptive whole.

6. **Causal-credit inheritance**
   - preserve uncertainty about why an adaptation worked.

7. **Boundary-centered inheritance**
   - retain counterexamples/generalization width as first-class parts of experience transfer.

8. **Developmental succession**
   - succession quality measured by re-emergent adaptive phenotype and continued plasticity, not artifact equality or ancestor imitation alone.

These are research questions, not novelty claims.
