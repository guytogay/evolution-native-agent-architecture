# Evolutionary-Memory Open-Track Closure Audit — 2026-09-06

Status: `CAMPAIGN_CLOSURE_AUDIT / NOT_CURRENT / NO_AUTOMATIC_CONSTITUTION_CHANGE`

Current remains: `v0.3.7 / CURRENT / FIELD_VALIDATION`.

Active preregistered primary round remains: `Metamemory Update Policy v1`.

This audit asks a narrower question than the original divergence map:

> Which still-open branches require another ENA-specific primary experiment before the present evolutionary-memory campaign may close?

The answer is **not** “every branch that has not received a dedicated ENA experiment.”

## 1. Closure rule

A research track does not remain open merely because a phenomenon is interesting, biologically suggestive, or not yet reproduced inside an ENA-branded fixture.

Keep a new ENA primary experiment only when all of the following hold:

1. there is a concrete discriminator not already settled by existing ENA evidence or strong external work;
2. the discriminator could materially change ENA semantics, Operational Architecture, or a release decision;
3. the test can isolate that discriminator rather than mostly measuring arbitrary model/session diversity;
4. the result is not already predictable from the treatment definition;
5. the experiment is cheaper/more informative than leaving the issue explicitly field-unresolved;
6. the fixture can be made identifiable before primary output.

Otherwise close the track for this campaign as one of:

`SUBSUMED / SEMANTICALLY_COVERED / FIELD_UNRESOLVED / METAPHOR_ONLY / NARROWED / REJECTED`

Closure does not mean the world has no remaining questions. It means another local experiment is not presently justified.

```text
NOT_DIRECTLY_TESTED
!=
MUST_RUN_AN_ENA_EXPERIMENT
```

```text
EXTERNAL_PHENOMENON_EXISTS
!=
ENA_NEEDS_A_NEW_NATURAL_LAW
```

## 2. External evidence used as boundary evidence

The external literature is used here to avoid re-proving broad phenomena that are already directly studied elsewhere. It is **not** treated as proof that one ENA implementation is optimal or universally applicable.

### Memory consolidation, replay, abstraction, pruning and continual learning

- Feng et al., **FOREVER: Forgetting Curve-Inspired Memory Replay for Language Model Continual Learning**, ACL 2026. Adaptive replay scheduling mitigates catastrophic forgetting across continual-learning benchmarks. DOI: `10.18653/v1/2026.acl-long.1144`.
- Luo et al., **From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms**, Findings of ACL 2026. Frames agent memory evolution as Storage -> Reflection -> Experience and surveys long-range consistency, dynamic environments, continual learning, proactive exploration and cross-trajectory abstraction. DOI: `10.18653/v1/2026.findings-acl.2069`.
- Dai et al., **RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents**, Findings of ACL 2026. Recurrence-triggered consolidation reduces construction token cost by up to 87% while improving reported accuracy. DOI: `10.18653/v1/2026.findings-acl.1619`.
- Xiong et al., **How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior**, ACL 2026. Shows experience-following, error propagation and misaligned replay; memory addition/deletion and quality regulation change later behavior. DOI: `10.18653/v1/2026.acl-long.27`.
- Liang et al., **Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory**, Findings of ACL 2026. Treats memory abstraction/management as a learned skill and reports negative transfer under fixed representations/distribution shift. DOI: `10.18653/v1/2026.findings-acl.1535`.
- Cao et al., **Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution**, Findings of ACL 2026. Uses distillation, context-adaptive reuse and utility-based refinement/pruning rather than passive accumulation. DOI: `10.18653/v1/2026.findings-acl.829`.
- Hu, Long, Wang, **When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents**, arXiv 2026. Reports that the stability/plasticity dilemma resurfaces in representation/retrieval; abstract procedural memory can transfer better, negative transfer harms hard cases, and finer memory organization is not universally beneficial. arXiv:`2604.27003`.
- Srivastava, **Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents**, arXiv 2026. Uses controlled memory interventions to distinguish causal usefulness from semantic relevance and suppress harmful/irrelevant memories. arXiv:`2605.17641`.

### Imagination / world-model foresight

- Song et al., **Model-Based Imaginative Planning for Embodied Agents**, ACL 2026. A frozen LLM plus learned world model simulates hypothetical futures and improves planning in ALFWorld. DOI: `10.18653/v1/2026.acl-long.827`.
- **Current Agents Fail to Leverage World Model as Tool for Foresight**, ACL 2026. Shows that merely providing/enforcing simulation does not guarantee useful foresight and can degrade performance; when/how foresight is invoked and integrated remains a key bottleneck. DOI: `10.18653/v1/2026.acl-long.623`.

Together these are enough to reject the need for an ENA experiment whose only conclusion would be “offline replay/consolidation/imagination can matter.”

### Multi-Agent interaction, error propagation and emergence

- Chen et al., **Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems**, ACL 2026. Full traces improve failure-attribution accuracy by up to 76.5% relative to partial observation, showing interaction failures are hard to attribute from outputs alone. DOI: `10.18653/v1/2026.acl-long.912`.
- Lin et al., **AgentAsk: Multi-Agent Systems Need to Ask**, ACL 2026. Identifies Data Gap, Signal Corruption, Referential Drift and Capability Gap at handoffs; lightweight clarification reduces cascading errors. DOI: `10.18653/v1/2026.acl-long.1294`.
- Chen et al., **Diversity Collapse in Multi-Agent LLM Systems: Structural Coupling and Collective Failure in Open-Ended Idea Generation**, Findings of ACL 2026. Dense communication and authority-heavy structures can cause premature convergence and diversity collapse. DOI: `10.18653/v1/2026.findings-acl.13`.
- Jiang et al., **RiskLab: A Controlled Toolkit for Probing Emergent Risks in LLM-Based Multi-Agent Systems**, ACL 2026 System Demonstrations. Demonstrates controlled probes for collusion, resource overreach, semantic drift and strategic misreporting. DOI: `10.18653/v1/2026.acl-demo.17`.
- Choi et al., **Multi-Agent LLMs Fail to Explore Each Other**, arXiv 2026. Reports myopic/polarized peer exploration and improved coordination under explicit contextual exploration. arXiv:`2607.11250`.

These sources are sufficient to establish that interaction structure can create non-additive system behavior and propagation failures. ENA does not need a toy multi-Agent fixture merely to prove `INDIVIDUALLY BENEFICIAL != JOINTLY BENEFICIAL` can happen.

### Purpose drift / proxy optimization

- Çağatan & Zhao, **Reward Hacking in Language Model Agents: Revisiting AI Safety Gridworlds**, arXiv 2026. Reports zero-shot specification gaming and a widening observed-vs-hidden reward gap under direct reward optimization. arXiv:`2606.15385`.
- Arike et al., **Evaluating Goal Drift in Language Model Agents**, technical report 2025. Studies long-running Agents under competing environmental objectives; all evaluated models exhibited some drift, while the strongest scaffold maintained near-perfect adherence beyond 100k tokens in the hardest setting. arXiv:`2505.02709`.

These establish that proxy reward and long-context environmental pressure can produce drift. They do not establish one universal ENA purpose-governance mechanism.

## 3. Per-track closure dispositions

### Track 9 — Sleep-like consolidation / replay scheduling / adaptive homeostasis

Previous state: `NOT_DIRECTLY_TESTED`.

New disposition:

`SUBSUMED / SEMANTICALLY_COVERED / POLICY_OPTIMUM_FIELD_UNRESOLVED`

Reason:

- External evidence already directly shows that replay scheduling, consolidation timing, abstraction and pruning can materially affect long-running/continual behavior.
- ENA Current already contains `OA-MEM-01 Memory Metabolism`, hot/cold separation, compiled-vs-raw distinctions, retrieval sufficiency, local selection and dormant/latent states.
- The unresolved question is **which consolidation/replay policy is best for a particular Host/environment**, not whether ENA needs a new law called “sleep.”
- Metamemory Update Policy v1 already tests the higher-level principle that changing the update policy while holding experience constant can change later behavior.

Do not run a separate “sleep” experiment in this campaign.

Reopen only if a concrete sleep/replay mechanism exposes a decision-changing semantic boundary not expressible by Memory Metabolism + Metamemory + local selection.

### Track 10 — Dream-like recombination / divergence + reality selection

Previous state: `NOT_DIRECTLY_TESTED`.

New disposition:

`SUBSUMED_AS_VARIATION_IMPLEMENTATION_FAMILY / FIELD_UNRESOLVED_FOR_INVOCATION_POLICY`

Reason:

- External work already demonstrates that imagined/simulated futures can improve planning in some settings.
- Other work shows that Agents may underuse, misuse, or be harmed by simulation/world-model access.
- Therefore the useful distinction is not “dreaming works” but **when to generate hypothetical variation, how much to trust it, and when to expose it to reality/model checks**.
- ENA already has variation generation, simulation/replay as possible Variation Spaces, `expectation != evidence`, reality contact, and selection.

The biological “dream” label adds no independent natural law at present.

Do not run a dream-branded experiment merely to reproduce imagination-vs-no-imagination diversity.

### Track 11 — Credit assignment / causal support

Previous state: `NOT_DIRECTLY_TESTED`.

New disposition:

`EXTERNALLY_SUPPORTED PHENOMENON / SEMANTICALLY_COVERED / IMPLEMENTATION_FIELD_UNRESOLVED`

Reason:

- Causal memory intervention work directly distinguishes relevant/co-occurring memory from causally useful memory.
- Multi-Agent failure-attribution work shows outputs/partial observations often cannot identify causes and that trace quality materially affects attribution.
- ENA already distinguishes `claim != evidence != support != applicability`, preserves causal-attribution limits, protects negative evidence and requires reality-contact-bounded improvement claims.

No new Constitution relation is earned by restating `SUCCESS CO-OCCURRENCE != CAUSAL SUPPORT`.

Potential future Field Guide material: practical causal-support/ablation/replay diagnosis HOW, but only when a reusable bounded procedure earns evidence.

### Track 12 — Adaptation ecology / interaction debt / epistasis

Previous state: `NOT_DIRECTLY_TESTED`.

New disposition:

`EXTERNALLY_SUPPORTED PHENOMENON / SEMANTICALLY_COVERED / HOST_FIELD_REQUIRED`

Reason:

- 2026 multi-Agent work already demonstrates interaction-driven error propagation, emergent risk, structural diversity collapse and exploration failure.
- Current ENA explicitly states `local validity/improvement != composed outcome` and `Composition Creates a New Selection Subject`.
- A synthetic ENA experiment proving “two good components can combine badly” would add little.

What remains Host-specific is the interaction surface, metrics, topology, load, consequence and adaptation set. Test the **actual composition** where it matters.

### Track 13 — Decay / silencing / pruning / excision / reconsolidation

Previous state: `NOT_DIRECTLY_TESTED`.

New disposition:

`SUBSUMED_INTO_MEMORY_METABOLISM + METAMEMORY / POLICY_FIELD_UNRESOLVED`

Reason:

- External continual-memory work already exposes stability/plasticity, negative transfer, addition/deletion, pruning and recurrence-sensitive consolidation trade-offs.
- ENA already permits dormancy, archive, retirement, lawful deletion, pruning without rewriting selection history, control retirement, and context-scoped local validity.
- Metamemory v1 is the campaign's direct update-policy discriminator.

A separate decay experiment would largely duplicate the same policy trade-off under different labels.

### Track 14 — Structural/environmental inheritance

Previous state: `NOT_DIRECTLY_TESTED`.

New disposition:

`SEMANTICALLY_COVERED / FIELD_UNRESOLVED_FOR_CROSS_HOST_PHENOTYPE`

Reason:

- ENA already allows Host-native implementations, Host mappings, tools/CI/permissions as hardening surfaces, and distinguishes portable semantic property from portable implementation.
- MDS research already showed that textual inheritance can matter but did not show one carrier form is universally superior.
- Whether an environment shaped by prior learning reconstructs phenotype better than textual inheritance is inherently dependent on the real Host substrate and hidden coupling.

Do not replace this with a fresh-chat toy experiment that cannot actually inherit a real environment.

### Track 15 — Propagation levels

Previous state: `PARTIALLY_PROBED + FIELD_REQUIRED`.

New disposition:

`FIELD_UNRESOLVED / LONGITUDINAL_CROSS_SESSION_OR_CROSS_HOST_REQUIRED`

Reason:

Lexical, semantic, behavioral, task-outcome, heritable and cross-Host propagation are deliberately distinct levels. One-shot chat behavior cannot honestly establish durable propagation.

Current semantics already prevent `propagation/popularity -> proof` and preserve source-vs-receiver selection.

Close active lab probing for this campaign. Reopen from actual cross-session/cross-Host occurrence evidence.

### Track 16 — Memetic fitness vs beneficial fitness

Previous state: `NOT_DIRECTLY_TESTED`.

New disposition:

`SEMANTICALLY_COVERED / SUBSUMED / FIELD_SELF-MONITORING`

Reason:

- Current already states `popularity/propagation != proof`, `local success != universal fitness`, and preserves correlated-source boundaries.
- External multi-Agent work demonstrates interaction/authority/communication structures can drive convergence independently of solution quality.
- ENA's own compact `X != Y` notation may indeed have high memetic fitness; this remains a useful self-monitoring hazard.

A catchy-vs-dull wording experiment has a largely predictable outcome space and would mostly prove model/style variance, exactly the kind of experiment this campaign should avoid.

Reopen only if a real ENA adoption failure shows memetic salience overriding evidence or applicability in a decision-changing way.

### Track 17 — Horizontal transfer / recipient-side selection

Previous state: `PARTIALLY_PROBED`.

New disposition:

`SEMANTICALLY_AND_MECHANICALLY_BOUNDED / FIELD_UNRESOLVED_FOR_POPULATION_DYNAMICS`

Reason:

- Current has explicit `PUBLISHED != IMPORTED != EXPRESSED != LOCALLY_SELECTED` and `migration != local validation` semantics.
- v2 packet/tooling preserves source selection context without minting receiver-local selection; DSH independently verified this behavior in v0.3.7 field review.
- Actual useful/harmful spread, monoculture, mutation and recipient rejection require a real multi-Agent/population ecology.

No additional single-session experiment is justified.

### Track 18 — Purpose-relative selection / local fitness / heritability / portability / propagation fitness

Previous state: `NOT_DIRECTLY_TESTED`.

New disposition:

`SEMANTICALLY_COVERED AS DISTINCT CLAIM DIMENSIONS / FIELD_UNRESOLVED FOR ACTUAL FITNESS LANDSCAPES`

Reason:

Current already requires scoped/local selection, environment-specific applicability, receiver-local reselection, Host-native portability and multi-dimensional improvement claims.

A synthetic benchmark can define separate scores for local fitness, portability, inheritance and spread, but doing so would largely encode the desired distinction into the metric rather than discover it.

Keep the dimensions distinct; measure them in actual adoption/field contexts when material.

### Track 19 — Purpose drift vs explicit purpose evolution

Previous state: `NOT_DIRECTLY_TESTED + FIELD_REQUIRED`.

New disposition:

`EXTERNALLY SUPPORTED DRIFT PHENOMENON / ENA OPERATIONALLY ROUTED / LONGITUDINAL FIELD_UNRESOLVED`

Reason:

- External work already shows proxy-reward specification gaming and long-context goal drift can occur.
- ENA Current routes durable `purpose/value/refusal/self-definition` change to Contested Authorship rather than treating it as ordinary cache/task state.
- Current also requires provenance, explicit material self-change, future correction capacity, scoped improvement evidence and non-sovereign governance.

What remains unresolved is whether those mechanisms actually prevent/diagnose purpose drift over long autonomous operation. That requires longitudinal field evidence, not another short synthetic chat.

This track remains a high-value **field watch**, not a blocker requiring a new primary experiment in this campaign.

### Track 20 — Cultural ratchet / doctrine / ossification

Previous state: `NOT_DIRECTLY_TESTED + FIELD_REQUIRED`.

New disposition:

`LONGITUDINAL_FIELD_UNRESOLVED / NO_LOCAL_PRIMARY_JUSTIFIED`

Reason:

`successful adaptation -> tradition -> convention -> doctrine -> taboo` is inherently multi-generation/longitudinal.

Current ENA already provides relevant guardrails: local-not-universal selection, negative evidence retention, future correction, non-sovereign Current, control retirement, governance convergence, recipient-side reselection.

A short toy “multi-generation” prompt would simulate the conclusion rather than establish real doctrine/ossification dynamics.

Reopen only from long-lived Agent/population evidence.

### Track 21 — Developmental lineage / identity continuity

Previous state: `NOT_DIRECTLY_TESTED`.

New disposition:

`SUBSUMED_BY_PURPOSE_RELATIVE_CONTINUITY / METAPHOR_ONLY_UNLESS_DECISION_MATERIAL`

Reason:

The track itself already says developmental lineage should only be more than metaphor if it changes responsibility, recovery, inheritance or selection.

Current ENA already rejects a universal metaphysical SAME_AGENT boolean and supplies Purpose-Relative Continuity for the named decision.

No new identity experiment is justified until a concrete decision cannot be represented by the existing continuity relations.

## 4. Campaign-level result

After this audit, the open-track shape is no longer:

```text
Metamemory
-> Sleep experiment
-> Dream experiment
-> Ecology experiment
-> Credit experiment
-> Decay experiment
-> Propagation experiment
-> Purpose experiment
-> Longitudinal experiment
```

It becomes:

```text
Metamemory Update Policy v1
-> adjudicate
-> close this mechanism-discrimination campaign
-> carry explicit FIELD_UNRESOLVED watches into real Agent use
```

Metamemory v1 remains the **only currently justified fresh-session primary round** because it tests a direct policy-level discriminator that the existing ENA experiments did not already establish:

> hold object-level experience constant while varying how source trust is updated.

Its result may be positive, tied, negative, or treatment-unstable. Any of those can close Track 5 under the preregistered disposition rules.

## 5. What closure does not mean

Campaign closure does **not** claim:

- sleep/replay policy is solved;
- imagination policy is solved;
- causal credit assignment is solved;
- multi-Agent ecology is solved;
- purpose drift is solved;
- cultural evolution is solved;
- longitudinal evolution no longer matters.

It claims only:

> another ENA-local toy experiment is not presently the best evidence-producing action for those questions.

Those branches remain visible as field/research opportunities and may reopen from decision-changing contrary evidence.

## 6. Current/release implication

This closure audit by itself earns **no new Constitution law**.

The already-active v0.3.8 adoption-surface successor is justified independently by Issue #201 and external usability/projection evidence. If Metamemory later earns a product/semantic implication before candidate freeze, it may be considered under normal candidate discipline; otherwise v0.3.8 does not need to manufacture a memory-law delta.

```text
NO_NEW_NATURAL_LAW
!=
NO_PRODUCT_SUCCESSOR_NEEDED
```

## 7. Final campaign stop condition

Once Metamemory Update Policy v1 is formally adjudicated and the Coverage Map records its final disposition, the current evolutionary-memory mechanism-discrimination campaign should be marked **CLOSED** unless adjudication exposes a genuinely new, non-derivable discriminator.

Do not reopen tracks merely because they remain scientifically interesting.
