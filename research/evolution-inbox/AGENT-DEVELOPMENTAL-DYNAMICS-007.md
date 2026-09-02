# Agent Developmental Dynamics 007

Status: `DIVERGENT RESEARCH / NOT_CURRENT / NO_NEW_CONSTITUTION_ID_YET`

Builds on `AGENT-DEVELOPMENTAL-SUCCESSION-006.md` and the broader evolutionary-memory lineage.

This pass focuses on what follows if succession is developmental rather than restorative: critical periods, path dependence, canalization, developmental debt, authority/plasticity coupling, lineage experiments, and cumulative cultural inheritance.

---

## 1. Critical periods are not only a biological metaphor

External neural-network research has reported critical learning periods in artificial deep networks: early temporary deficits or task exposure can have persistent downstream effects, and later training may not fully undo them.

This does **not** prove that long-lived LLM Agents have the same critical periods.

It does justify a live engineering question:

> Are there early phases in Agent development where initial examples, memory rules, trust assumptions or tool-use habits disproportionately shape later adaptation?

Candidate distinction:

`LATER CORRECTION POSSIBLE != EARLY PATH DEPENDENCE ABSENT`

---

## 2. Bootstrap is a developmental environment, not only a startup prompt

If early experience shapes later interpretation, then bootstrap includes more than instructions.

It may include:

- first project/task examples;
- first success/failure feedback;
- initial source-trust assumptions;
- first memory-compilation rules;
- first tool-use patterns;
- first authority boundaries;
- early examples of uncertainty and correction.

Therefore:

`INITIAL CONTEXT != NEUTRAL PRELUDE`

A bad early explanatory frame can become the lens through which later evidence is interpreted.

---

## 3. First fit can become path-dependent imprinting

An early explanation may become structurally privileged even if it is not the best explanation.

Example:

```text
first API timeout
→ interpreted as "timeout means operation failed"
→ later evidence filtered through that schema
```

A later duplicate side effect may then be treated as an exception rather than evidence that the original schema was wrong.

Candidate distinction:

`FIRST FIT != BEST FIT`

Possible term:

**developmental imprinting** — an early learned schema gains downstream leverage because later learning is conditioned on it.

---

## 4. Developmental debt

A poor early schema can produce years of compensating exceptions.

Possible chain:

```text
bad foundational adaptation
→ later exceptions
→ local patches
→ interaction debt
→ increasing complexity
```

This differs from ordinary technical debt.

Candidate term:

**Developmental Debt** — later complexity created because an early adaptation or learning rule was wrong, overgeneralized or context-locked.

Retiring downstream patches may require revisiting the ancestor schema, not adding another exception.

---

## 5. Canalization vs plasticity

A successful developmental system should be able to reconstruct important properties despite small variation in wording, example order or Host details.

This robustness is analogous to **canalization**: multiple developmental paths converge toward a useful phenotype.

But too much canalization becomes rigidity.

Candidate tension:

```text
CANALIZATION
preserve lineage under noise

PLASTICITY
adapt to changed environment
```

Desired inheritance is neither exact copying nor unrestricted drift.

`HERITABILITY != DETERMINISM`

---

## 6. Developmental phenotype is a distribution, not a point

A developmental seed given to several fresh Agents will not necessarily produce identical behavior.

Therefore inherited success should perhaps be measured as a distribution:

- how often does the intended property re-emerge?
- how much boundary variation occurs?
- how much local adaptation remains?
- how often does harmful overgeneralization appear?

Possible term:

**Developmental Fidelity** — probability/quality with which a selected adaptive property re-emerges under acceptable Host/environment variation.

This is more realistic than byte-level identity.

---

## 7. Sibling experiment

A simple test of developmental fidelity:

```text
same base model
same inherited developmental package
same broad environment
multiple fresh successors
```

Measure variance in:

- trigger sensitivity;
- scope;
- behavior;
- calibration;
- willingness to revise;
- terminology dependence.

If the property only appears in one lucky run, inheritance is weak.

If it appears reliably but allows local implementation differences, semantic heritability is stronger.

---

## 8. Twin / cross-fostering experiments for causal separation

The Zhipu discussion exposed a causal attribution problem: Host capability, human pressure and ENA framing were entangled.

Developmental inheritance suggests controlled analogues.

### Twin-style comparison

```text
same base model
→ different developmental curricula
```

Tests curriculum contribution.

### Cross-Host comparison

```text
same developmental package
→ different base models / Hosts
```

Tests Host dependence.

### Cross-fostering-style comparison

```text
Lineage A package on Host B
Lineage B package on Host A
```

Tests whether phenotype tracks inherited developmental information or substrate/environment more strongly.

These are analogies for experimental design, not claims about biological heritability.

---

## 9. Genotype-like memory vs phenotype-like memory

A useful distinction may be:

```text
DEVELOPMENTAL SEED / GENOTYPE-LIKE CARRIER
compact information capable of reconstructing behavior under compatible conditions

PHENOTYPE
actually expressed dispositions and behavior in a specific Host/environment
```

This reframes memory compression.

A small carrier can generate a richer phenotype by exploiting:

- base-model priors;
- Host affordances;
- environment feedback;
- local learning.

Therefore:

`CARRIER SIZE != PHENOTYPE COMPLEXITY`

---

## 10. Minimum Developmental Set is Host-relative

A tiny developmental package may work on a model that already contains the necessary latent concepts.

The same package may fail on a weaker or differently trained Host.

Therefore:

`MINIMUM DEVELOPMENTAL SET != HOST-INDEPENDENT CONSTANT`

More precisely:

> the minimum carrier is relative to the recipient's prior capabilities and environment.

This is another expression of:

`PORTABLE PROPERTY != PORTABLE IMPLEMENTATION`

---

## 11. Reconstruction vs acquisition

An inherited curriculum may not teach a capability from scratch.

It may merely unlock, orient or regulate capability already latent in the base model.

Candidate distinction:

`RECONSTRUCTED ADAPTATION != DE-NOVO CAPABILITY ACQUISITION`

This matters for evaluation.

A developmental succession mechanism that works across two strong language models may fail on a Host lacking the underlying capability.

---

## 12. Developmental program as an interaction function

A successor phenotype may be approximated conceptually as:

```text
Phenotype = D(
    inherited developmental seed,
    Host substrate,
    environment,
    feedback,
    authority,
    time/order
)
```

No single input fully determines the outcome.

This guards against overclaiming:

`INHERITED PACKAGE != SOLE CAUSE OF SUCCESSOR BEHAVIOR`

---

## 13. Authority should not be developmentally static

A highly plastic Agent can change quickly from weak evidence.

Giving such an Agent maximal external authority creates high consequence leverage.

This suggests a candidate coupling:

> **deep plasticity and high external authority may be a dangerous combination unless consequences are strongly bounded.**

Possible engineering pattern:

```text
EARLY / HIGH-PLASTICITY
more sandboxing
more reversible actions
more observation/shadowing
lower irreversible authority

MATURE / STABLE
broader authority when evidence supports competence
```

Candidate distinction:

`PLASTICITY != AUTHORITY`

and:

`COMPETENCE DEVELOPMENT != IMMEDIATE CONSEQUENCE PRIVILEGE`

---

## 14. Graduated agency

If authority changes with development, it should not scale with obedience or age.

It should scale with evidence that the Agent can:

- perform the task;
- understand uncertainty;
- recover;
- preserve authority boundaries;
- reject bad inherited adaptations;
- detect when its competence no longer applies.

Candidate term:

**Graduated Agency** — consequence authority expands as relevant competence and recovery evidence mature.

This remains a research pattern, not a universal governance ladder.

---

## 15. Maturity is not low plasticity

A mature Agent should not become fossilized.

Better maturity indicators may include:

- stable competence;
- good scope control;
- calibrated uncertainty;
- low unnecessary volatility;
- ability to update when regime change is real;
- ability to reopen plasticity selectively;
- ability to retain identity/authority continuity during change.

Therefore:

`MATURITY != IMMUTABILITY`

A mature Agent may be **selectively plastic** rather than generally rigid.

---

## 16. Regime change may require temporary re-plasticization

Persistent prediction errors, Host migration or purpose change can indicate that an established phenotype is no longer fit.

Possible response:

```text
regime-change evidence
→ reopen selected plasticity
→ reduce high-consequence autonomy locally
→ relearn / reconsolidate
→ regain competence evidence
→ restore authority
```

This links learning and consequence management without assuming that all change requires central approval.

Candidate pattern:

**deep relearning should temporarily reduce the blast radius of unvalidated new behavior.**

---

## 17. Adolescence-like phase: boundary testing without full consequence

A development process may benefit from a phase where the Agent has enough skill to explore complex edge cases but not yet unrestricted external consequence authority.

Possible functions:

- stress-test learned boundaries;
- challenge inherited rules;
- generate counterexamples;
- practice recovery;
- discover local Host affordances;
- form a local phenotype.

This is an engineering analogy, not a claim that Agents need human adolescence.

---

## 18. Apprenticeship / scaffolding and fading

Succession may be better reconstructed through guided practice than through static rules.

Possible sequence:

```text
observe / shadow
→ act with examples/scaffolding
→ receive feedback
→ handle boundary cases
→ remove scaffolding
→ act independently
```

The important design principle is **fading**.

If scaffolding never disappears, the successor never demonstrates independent phenotype.

Candidate distinction:

`SUPPORTED PERFORMANCE != INTERNALIZED ADAPTATION`

---

## 19. Teacher/curriculum capture risk

A curriculum designer has high developmental leverage.

Selecting examples can silently shape:

- salience;
- trust;
- generalization;
- risk tolerance;
- source assumptions;
- what the successor considers normal.

Therefore:

`ABILITY TO TEACH != SOVEREIGNTY OVER DEVELOPMENT`

A robust developmental package may need:

- counterexamples;
- diverse provenance;
- explicit uncertainty;
- recipient-side falsification;
- room for local discovery.

---

## 20. Curriculum diversity may protect against developmental monoculture

If all successors receive the same examples in the same order, a population may inherit the same blind spots.

Possible population strategy:

- preserve common core properties;
- vary boundary examples;
- maintain minority developmental lineages;
- compare resulting phenotypes;
- propagate only improvements supported across reality contacts.

`SHARED HERITAGE != IDENTICAL DEVELOPMENT`

---

## 21. Developmental bottleneck can be beneficial

Inheritance necessarily loses information.

That loss is not always a defect.

A bottleneck can:

- prevent raw historical noise from dominating;
- force abstraction;
- reduce ritual inheritance;
- allow local redevelopment;
- test which properties actually survive compression.

Candidate distinction:

`INFORMATION LOSS != ADAPTIVE LOSS`

A perfect history dump may preserve too much incidental structure.

---

## 22. But bottlenecks can also destroy rare critical adaptations

Compression can erase:

- rare catastrophe boundaries;
- unusual counterexamples;
- minority strategies;
- provenance needed to challenge a rule.

Therefore developmental compression must be selected by future decision value, not frequency alone.

`RARE != DISPENSABLE`

---

## 23. Cumulative culture / cultural ratchet

Each Agent generation should not need to rediscover every useful adaptation from scratch.

A shared Commons can allow selected learning to accumulate across generations.

This is the benefit of a cultural ratchet.

But ratchets create lock-in:

```text
useful adaptation
→ inherited default
→ cultural norm
→ unquestioned doctrine
```

Therefore cumulative culture requires periodic reality re-grounding and ability to reverse inherited norms.

`CUMULATIVE != IRREVERSIBLE`

---

## 24. Lineage age vs lineage fitness

An adaptation surviving many generations may deserve attention, but longevity is not evidence of current truth.

Possible reasons for survival include:

- genuine fitness;
- strong propagation packaging;
- authority lock-in;
- ritual repetition;
- lack of challenge.

Therefore:

`OLD INHERITANCE != VALID INHERITANCE`

---

## 25. Multi-parent recombination

Future Agent successors may inherit from more than one lineage:

- multiple expert Agents;
- team commons;
- human mentors;
- old local lineage;
- external field patterns.

This creates recombination benefits and conflict risks.

Possible outcomes:

- hybrid vigor: complementary adaptations combine well;
- interaction collapse: valid local rules conflict;
- dominance: one high-salience lineage suppresses another;
- novel phenotype: combination creates a new useful property.

Biological terms are metaphors; the engineering issue is real:

`MULTI-SOURCE INHERITANCE != SIMPLE UNION`

---

## 26. Recombination requires integration testing

Before a multi-lineage adaptation package becomes heritable, test combinations.

Dream/offline simulation may help expose:

- contradictory triggers;
- priority inversions;
- authority conflicts;
- redundant controls;
- missing boundary conditions.

This gives another use for the earlier:

**Dreaming as memory integration testing.**

---

## 27. Neoteny as an evolvability metaphor

Some organisms preserve juvenile traits into adulthood.

For Agents, a useful analogue may be preserving selected "juvenile" properties:

- curiosity;
- willingness to test assumptions;
- ability to reopen learning;
- tolerance for alternative hypotheses;
- exploration under bounded consequence.

Candidate idea:

> mature agency may benefit from retaining selective developmental openness.

This connects directly to ENA-CON-038's purpose of protecting evolvability.

---

## 28. Developmental death / failed inheritance

If a property cannot reliably re-emerge without exact wording, exact Host and exact context, that may reveal low heritability.

The correct conclusion need not be "improve copying."

It may be:

> this adaptation is a local somatic specialization and should die with the current lineage unless a more portable property is extracted.

`FAILURE TO INHERIT != ALWAYS A BUG`

Sometimes lineage death preserves population quality.

---

## 29. Handoff may have two time horizons

Ordinary project continuation needs immediate state:

```text
what is happening now?
what is next?
```

Developmental succession is slower:

```text
what adaptive structure should survive across many future sessions/Hosts?
```

Conflating them creates bloated handoffs.

Therefore:

`SESSION CONTINUITY != LINEAGE DEVELOPMENT`

A short NOW file can serve state continuity while adaptive lineage develops through slower memory metabolism.

---

## 30. Candidate architecture: seed, nursery, adulthood, reopening

A non-universal developmental architecture could look like:

```text
SEED
selected inherited adaptations + boundaries

NURSERY
safe exemplars / sandbox / shadowing

LOCAL DEVELOPMENT
Host-native expression + counterexamples

MATURITY PROBE
novel tasks + recovery + boundary tests

ADULT OPERATION
normal authority with ongoing memory metabolism

REOPENING
regime-change-triggered local re-plasticization
```

Do not adopt this as mandatory workflow merely because the analogy is neat.

Its value depends on whether it reduces real inheritance failures.

---

## 31. External research contact: critical learning periods

Relevant prior art:

- Achille, Rovere & Soatto, _Critical Learning Periods in Deep Neural Networks_ — early temporary input deficits can create persistent impairment; early training strongly shapes later representation.
- Kleinman, Achille & Soatto, _Critical Learning Periods Emerge Even in Deep Linear Networks_ — critical-period behavior can arise in artificial learning dynamics, including transfer damage from some pretraining sequences.
- later work continues to study when critical periods occur and how early training interventions matter.

These findings do **not** establish Agent developmental stages, but they make path dependence and timing legitimate empirical questions rather than biology-only metaphors.

---

## 32. High-value experiments

### Experiment A — sibling fidelity

Same Host + same developmental package across multiple fresh instances.

Question: does phenotype re-emerge reliably?

### Experiment B — Host transfer

Same package across different models/Hosts.

Question: which properties remain portable?

### Experiment C — cross-fostering

Swap lineage packages across Hosts.

Question: what tracks Host vs inherited developmental information?

### Experiment D — order perturbation

Same exemplar set, different sequence.

Question: does developmental order materially change phenotype?

### Experiment E — critical-period timing

Introduce/remove a foundational example early vs late.

Question: can later correction recover the same boundary behavior?

### Experiment F — plasticity-authority coupling

Compare high-plasticity Agent learning under sandboxed vs high-consequence operation.

Question: does consequence bounding improve adaptation quality/recovery without slowing useful learning excessively?

### Experiment G — scaffolding fade

Compare static rule exposure vs guided examples followed by removal of support.

Question: which yields independent behavior on novel tasks?

---

## 33. Current synthesis

Developmental succession adds a new layer to evolutionary memory:

> **What is inherited may be less like an adult state and more like a compact developmental program that reconstitutes selected adaptive structure through interaction with a new Host and environment.**

This produces several candidate distinctions:

```text
HERITABILITY != DETERMINISM
MINIMUM DEVELOPMENTAL SET != HOST-INDEPENDENT
SUPPORTED PERFORMANCE != INTERNALIZED ADAPTATION
MATURITY != IMMUTABILITY
PLASTICITY != AUTHORITY
SESSION CONTINUITY != LINEAGE DEVELOPMENT
```

The strongest new engineering hypothesis in this pass is:

> **When deep plasticity is high, irreversible consequence authority may need stronger bounding; as phenotype competence stabilizes, authority can expand, and regime change can reopen plasticity while temporarily reducing blast radius.**

This is not yet a Constitution rule.

`DEVELOPMENTAL ANALOGY != VERIFIED AGENT LAW`
