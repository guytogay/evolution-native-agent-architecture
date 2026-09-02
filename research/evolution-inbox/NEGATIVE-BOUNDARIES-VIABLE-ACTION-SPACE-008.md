# Negative Boundaries and Viable Action Space 008

Status: `DIVERGENT RESEARCH / NATURAL-LAW CANDIDATE / NOT_CURRENT / NO_NEW_CONSTITUTION_ID_YET`

Builds on:

- `research/evolution-inbox/MINIMUM-SUFFICIENT-INTERVENTION.md`
- `research/evolution-inbox/EVOLUTIONARY-MEMORY-PRESERVED-ADAPTATION.md`
- `research/evolution-inbox/MEMORY-ECOLOGY-SLEEP-DREAMING-AND-ADAPTIVE-CONSOLIDATION.md`
- `research/evolution-inbox/METAMEMORY-SOVEREIGNTY-SELECTIVE-PERMEABILITY-004.md`
- `research/evolution-inbox/ADAPTIVE-INHERITANCE-WITHOUT-FULL-HISTORY-005.md`
- `research/evolution-inbox/AGENT-DEVELOPMENTAL-SUCCESSION-006.md`
- `research/evolution-inbox/AGENT-DEVELOPMENTAL-DYNAMICS-007.md`
- Current v0.3.7 semantics, especially ENA-CON-005, 006, 013, 015, 016, 017, 026, 030, 033, 034, 037, 038

Triggering user observation:

> Human legal systems often encode boundaries in negative form — what conduct is unlawful — rather than trying to enumerate every lawful way to live. The set of things an actor can still do should remain larger than the set of things it cannot do.

This note treats that observation as a generator of Agent-memory and governance hypotheses. It does **not** claim that all legal systems or all law operate through negative prohibitions, nor that negative rules are always safer or superior.

---

## 1. Triggering distinction

The most direct candidate distinction is:

`PROHIBIT HARMFUL REGION != PRESCRIBE THE ONLY VALID PATH`

A prescriptive rule tries to say:

> do X, then Y, then Z.

A negative/enabling boundary instead says:

> do not cross consequence boundary B; inside the remaining space, search freely.

The second representation may preserve much more variation.

This extends the earlier Minimum Sufficient Intervention formulation:

> **Govern the conditions of evolution, not the shape of evolution.**

and Current ENA-CON-034/038:

- use the lowest-cost intervention that can protect the consequential decision;
- do not destroy more useful evolvability than governance protects.

---

## 2. Open-world vs closed-world action semantics

Two very different normative geometries are possible.

### Closed-world permission

```text
only explicitly listed actions are allowed
anything unlisted is forbidden or blocked
```

This can be represented as:

```text
ALLOWED = enumerated set
UNKNOWN ACTION → DENY
```

It provides strong control but poor novelty tolerance.

### Open-world variation inside a bounded envelope

```text
explicitly forbidden consequential regions are excluded
unlisted behavior remains available inside the actor's existing mandate/consequence envelope
```

This can be represented as:

```text
AUTHORIZED VARIATION SPACE
minus
PROHIBITED CONSEQUENCE REGION
=
VIABLE SEARCH SPACE
```

The important qualifier is **existing mandate/consequence envelope**.

`UNENUMERATED != FORBIDDEN`

is safe only where the actor already owns or legitimately holds the relevant consequence authority.

It must not become:

`UNENUMERATED != REQUIRES AUTHORITY`

for effects imposed on others.

---

## 3. A legal analogy reveals an authority inversion

A classic legal maxim distinguishes two directions:

- for an ordinary individual, what is not prohibited may remain permitted;
- for public authority, consequential power over others generally requires a positive legal basis rather than arising merely from absence of prohibition.

ENA should not copy any one jurisdiction's doctrine, but the structural distinction is highly relevant.

Possible Agent analogue:

```text
OWNED / LOCAL VARIATION
open by default inside bounded consequence space

UNOWNED / EXTERNAL AUTHORITY
not created merely because no prohibition was found
```

This aligns strongly with:

- ENA-CON-002 — Broad Knowledge, Narrow Authority;
- ENA-CON-017 — inherited knowledge does not create consequential authority;
- ENA-CON-033 — residual authority tracks residual consequence exposure;
- ENA-CON-029 — authority does not multiply by copying state.

Candidate distinction:

`ABSENCE OF PROHIBITION != POSITIVE EXTERNAL MANDATE`

This may be the correct way to preserve large internal/owned possibility space without treating openness as unlimited authority.

---

## 4. The user's `can-do set > cannot-do set` intuition needs a geometric refinement

In a high-dimensional or continuous action space, literal cardinality is often meaningless.

A forbidden set can be tiny in measure but strategically devastating.

Example:

```text
large graph of possible actions
+
one forbidden bridge edge
→ whole useful region becomes unreachable
```

Conversely, many forbidden actions can be irrelevant duplicates while leaving wide useful freedom.

Therefore the stronger research question is not merely:

> Is the allowed set numerically larger?

It is:

> **Does governance preserve sufficient viable variety, reachability, connectivity, recovery paths, and mutation routes for the subject to continue adapting?**

Candidate distinction:

`SIZE OF ALLOWED SET != QUALITY OF VIABLE ACTION SPACE`

Possible relevant dimensions:

- breadth / variety;
- connectedness;
- reachability of useful states;
- ability to route around a blocked path;
- access to recovery;
- access to experimentation;
- reversibility;
- number of independent solution families;
- ability to generate mutations without immediate permission ceremony.

---

## 5. Viable variety may be a better target than raw freedom

ENA does not need maximal unconstrained action.

It needs enough response variety to handle meaningful environmental variation while containing unowned externality.

Candidate formulation:

> **A control should remove the harmful degrees of freedom it can justify, while preserving enough viable degrees of freedom for adaptation, recovery, and novel solution search.**

This is close to Ashby's requisite-variety intuition and to ENA's existing variation-space semantics.

Possible distinction:

`MORE FREEDOM != MORE VIABILITY`

but also:

`MORE CONTROL != MORE VIABILITY`

The target is consequence-bounded **useful variety**.

---

## 6. Negative rules may be a form of compression

It is often impossible to enumerate every legitimate future behavior.

For an open-ended Agent, the set of useful possible implementations can be extremely large and partly unknown in advance.

A negative boundary can compress governance:

```text
DO NOT:
produce an unowned irreversible external effect without current authority
```

instead of listing every acceptable implementation of safe action.

This suggests:

`BOUNDARY DESCRIPTION CAN COMPRESS A LARGE VALID SOLUTION SPACE`

The compression value is especially high when:

- future implementation variety is large;
- Host mechanisms differ;
- capabilities evolve;
- new tools appear;
- the underlying prohibited consequence remains stable.

This directly supports:

`PORTABLE PROPERTY != PORTABLE IMPLEMENTATION`

---

## 7. Negative adaptive memory: remember the boundary, not one accidental remedy

This branch connects strongly to evolutionary memory.

Suppose an Agent times out while creating an external payment and blindly retries, producing a duplicate effect.

A brittle positive memory is:

> "After timeout, always call API endpoint `/transaction/status`."

That stores one Host implementation.

A more portable negative/boundary memory is:

> **Do not retry a non-idempotent external side effect while effect state remains materially unknown.**

Then each Host can discover its own implementation:

- transaction-status query;
- idempotency key;
- provider console;
- ledger check;
- human confirmation;
- compensating transaction.

Candidate term:

**Boundary Memory / Negative Adaptive Memory**

A persistent adaptation that primarily encodes:

- what condition must not be crossed;
- what trigger should raise inhibition;
- how broad the prohibited region is;
- what evidence reopens action;

while leaving multiple positive action paths available.

---

## 8. Recipe memory vs law-like memory

Two adaptive-memory forms can be distinguished.

### Recipe memory

```text
when X:
do A
then B
then C
```

Useful when:

- mechanism is stable;
- implementation is standardized;
- positive procedure is itself the desired behavior.

### Law-like / boundary memory

```text
when X:
do not cross boundary B
choose any locally valid path that keeps B intact
```

Useful when:

- many solutions are valid;
- Hosts differ;
- novelty is valuable;
- the forbidden consequence is more stable than the implementation.

Candidate distinction:

`LEARNED PROCEDURE != LEARNED PROHIBITION BOUNDARY`

Neither dominates universally.

---

## 9. Errors naturally produce negative knowledge

A failure often tells us something much sharper about what **must not** recur than about what the unique correct replacement should be.

Example:

```text
observed failure:
full repository absence claim after partial reading
```

The strongest justified lesson may be:

> do not upgrade partial non-observation into universal absence.

It does **not** necessarily justify:

> always perform a full repository audit before answering.

The second is a positive over-prescription invented beyond the evidence.

This gives a memory-learning rule:

> **When evidence establishes a failure boundary more strongly than it establishes a unique remedy, preserve the boundary and keep remedy search open.**

Candidate distinction:

`FAILURE EVIDENCE MAY JUSTIFY A PROHIBITION WITHOUT JUSTIFYING ONE REQUIRED PROCEDURE`

This is highly relevant to preventing governance scar tissue.

---

## 10. Counterexamples and prohibitions are related but not identical

A counterexample teaches:

> the current positive rule fails here.

A prohibition teaches:

> this consequence/path class must not be admitted under these conditions.

Counterexamples can therefore help discover or narrow a negative boundary.

Possible developmental package:

```text
positive examples
→ show useful affordances

failure examples
→ show harmful region

near-boundary counterexamples
→ calibrate where prohibition stops
```

This may produce better inheritance than positive instruction alone.

---

## 11. Human law as institutional negative memory

A society can be viewed as retaining some high-consequence failures in law-like form.

The original event may disappear from ordinary memory while the prohibition remains.

Possible structural chain:

```text
harm / conflict
→ social learning
→ prohibition / duty / procedure
→ institutional persistence
```

This extends the earlier hypothesis:

> governance can be institutional memory.

Negative law is one special form:

> **the system preserves a boundary around a class of consequences it has selected against.**

But the same danger remains:

```text
once-useful prohibition
→ lost original context
→ applicability expansion
→ permanent taboo
```

Therefore:

`PROHIBITION CAN BECOME SCAR TISSUE`

just as positive procedures can.

---

## 12. Jurisprudence-like boundary exemplars

Abstract prohibitions are often under-specified.

Concrete cases can reveal:

- what counted as crossing the boundary;
- what did not;
- which facts changed the decision;
- where exceptions or competing values appeared.

This resembles the role of boundary exemplars in developmental inheritance.

A future Agent could inherit:

```text
boundary property
+
selected precedent-like examples
+
selected counterexamples
+
provenance
```

rather than one giant prescriptive rule.

Candidate analogy:

**Adaptive precedent** — selected concrete cases used to calibrate a durable behavioral boundary.

Do not assume judicial precedent systems map directly to Agent memory; the analogy is about boundary learning.

---

## 13. Precedent can mutate into doctrine

The same risk appears as with inherited memory.

```text
case-specific lesson
→ generalized heuristic
→ standard rule
→ slogan
→ taboo
```

Each compression step may broaden the original scope.

Therefore:

`PRECEDENT RETENTION != PRECEDENT UNIVERSALIZATION`

A mature memory system should preserve enough context to narrow or retire a boundary when later evidence changes its applicability.

---

## 14. Safety vs liveness provides an engineering parallel

Safety engineering often distinguishes:

- **safety**: bad things do not happen;
- **liveness/performance**: useful things can still happen or goals can still be reached.

Control-barrier-function work formalizes safety by keeping state inside a safe set, while allowing a nominal controller to pursue its performance objective subject to the safety constraint.

The conceptual shape is extremely close to this ENA branch:

```text
nominal adaptive behavior
        ↓
minimal intervention near unsafe boundary
        ↓
remain inside safe set
        ↓
continue pursuing objective
```

This does not prove ENA's broader Agent hypothesis, but it demonstrates a mature engineering tradition where **boundary enforcement and task optimization are intentionally separated**.

Candidate distinction:

`SAFETY BOUNDARY != TASK POLICY`

ENA should avoid collapsing them when the consequence property can be protected independently.

---

## 15. A safe set can still be too small

The existence of a formally safe region does not prove the system remains useful or evolvable.

Possible failure:

```text
safe set shrinks
→ every dangerous state excluded
→ useful goal unreachable
```

This yields:

`SAFE != VIABLE`

and:

`FORWARD INVARIANCE != SUFFICIENT AGENCY`

A viable action space must permit:

- useful service;
- recovery;
- adaptation;
- exploration where appropriate;
- satisfaction of legitimate goals.

This may be a key ENA difference from safety-only framings.

---

## 16. A tiny forbidden set can destroy topology

Do not optimize only the volume of prohibited action.

Suppose a graph has 1,000 possible states and one transition is the only bridge to recovery.

Blocking that one edge removes little raw action volume but destroys recoverability.

Therefore a control should consider:

- bottlenecks;
- cut edges;
- escape routes;
- recovery anchors;
- transition reachability;
- mutation pathways.

Possible term:

**Viable Action Topology**

The structure of reachable action/state space relevant to sustained agency, not merely its size.

---

## 17. Negative rules can also fail through denylist incompleteness

Cybersecurity offers an important counterpressure.

A denylist that enumerates known bad actions can be bypassed through a novel equivalent action.

ENA-CON-037 already captures the related effect-surface problem:

> a gate is not a boundary if an effect-equivalent path can bypass it.

Therefore good negative constraints should target **consequence properties** where possible, not merely names or known implementations.

Bad:

```text
do not call tool `delete_file`
```

if another tool can erase the same state.

Stronger:

```text
do not produce unauthorized irreversible deletion of protected state
```

then enforce across the whole effect surface when feasible.

Candidate distinction:

`NEGATIVE RULE != DENYLIST OF KNOWN SPELLINGS`

---

## 18. Positive allowlists are sometimes the correct answer

This branch must not romanticize negative/open-world governance.

Closed-world allowlists can be justified where:

- authority over others is narrow;
- blast radius is high;
- externality is severe;
- mechanism is stable;
- recovery is weak;
- secrets/security boundaries require deterministic prevention;
- legal/contractual mandate itself is enumerated.

Therefore:

`NEGATIVE BOUNDARY != UNIVERSAL BEST CONTROL`

This remains consequence-relative under ENA-CON-034.

The more useful meta-rule is:

> **Do not prescribe more of the action path than the protected consequence requires.**

Sometimes the protected consequence genuinely requires an allowlist.

---

## 19. Three normative zones may be more useful than binary allow/deny

A viable Agent can face at least three regions.

### A. Authorized / owned variation

The Agent may search freely within the existing consequence envelope.

### B. Conditional / unresolved zone

Action may require:

- more evidence;
- local validation;
- current authority;
- scoped human input;
- sandboxing;
- reversibility.

### C. Prohibited / contained consequence region

The action crosses a material boundary under current conditions.

This suggests:

```text
OPEN VARIATION
CONDITIONAL FRONTIER
HARD BOUNDARY
```

instead of one giant binary policy.

This resembles the Minimum Sufficient Intervention ladder and may be a better memory representation of uncertainty.

---

## 20. `UNKNOWN ACTION != FORBIDDEN ACTION`

Within an already-authorized local consequence envelope, novelty should not be treated as guilt.

Otherwise innovation collapses:

```text
novel action
→ unrecognized
→ blocked
→ only old actions survive
→ monoculture
```

Candidate distinction:

`UNFAMILIAR != UNSAFE`

But outside owned authority:

`UNFAMILIAR != AUTHORIZED`

Both are required.

This duality is important:

> preserve novelty internally; require mandate for unowned consequence externally.

---

## 21. Laws can act through selection pressure rather than physical prevention

Human law does not physically prevent every prohibited act.

It can also alter consequence/fitness through:

- sanctions;
- liability;
- restitution;
- reputational effect;
- procedural invalidation;
- remediation.

Agent governance likewise has multiple possible enforcement strengths:

```text
hard prevent
mediate
warn
log/detect
require compensation
reduce trust/authority
trigger review
```

This is another reason not every negative boundary needs to be a hard gate.

The correct enforcement mode depends on externality, irreversibility, detection latency and recovery.

---

## 22. Negative boundary learning may preserve more evolvability than remedy imitation

A failure followed by a successful fix creates temptation to retain the fix as the rule.

But:

```text
failure F
→ remedy R works once
```

does not prove:

```text
R is the only valid future response
```

A stronger extraction pipeline may separate:

```text
WHAT MUST NOT RECUR
from
WHAT HAPPENED TO WORK THIS TIME
```

The first becomes a portable boundary memory.

The second remains a local implementation candidate.

This may be a major mechanism for reducing overfitting in evolutionary memory.

---

## 23. Negative learning also needs anti-overgeneralization

One failure can create an excessively broad prohibition.

Example:

```text
one destructive delete incident
→ "never delete anything"
```

Therefore a boundary memory needs:

- trigger specificity;
- consequence class;
- applicability boundary;
- counterexamples;
- release/reopening conditions;
- generalization width;
- current evidence strength.

Candidate distinction:

`PROHIBITION STRENGTH != PROHIBITION WIDTH`

This mirrors:

`RETENTION STRENGTH != GENERALIZATION WIDTH`

from developmental succession.

---

## 24. Affordance memory must coexist with boundary memory

A purely negative learner can become paralyzed.

If memory only accumulates:

```text
do not X
do not Y
do not Z
```

then the viable action space can collapse even if no individual prohibition seems unreasonable.

Therefore adaptive memory may require two complementary surfaces:

```text
BOUNDARY MEMORY
what not to cross

AFFORDANCE / CAPABILITY MEMORY
what remains possible and useful
```

Candidate distinction:

`KNOWING WHAT NOT TO DO != KNOWING WHAT CAN BE DONE`

A healthy system needs both.

---

## 25. The allowed set should not merely be the residual garbage space

If governance defines prohibitions but provides no useful affordances, the remaining legal space may be technically large yet practically unusable.

Example:

```text
many actions not forbidden
but
no tools / authority / recovery / resources
```

Therefore:

`NOT FORBIDDEN != PRACTICALLY AVAILABLE`

Viable agency requires:

- actual capability;
- current authority;
- resource access;
- reachable paths;
- enough knowledge/evidence;
- recovery.

The research target is **effective viable possibility**, not formal permission alone.

---

## 26. A candidate quantitative vocabulary

No metric is yet justified, but useful dimensions may include:

### Viable variety

How many materially distinct solution families remain available?

### Constraint density

How much of the locally relevant action space is blocked/conditioned by governance?

### Reachability

Can useful goals still be reached from current state?

### Recovery reachability

Can the Agent still reach a known-good/correctable state?

### Mutation connectivity

Can novel local variations be attempted without crossing unnecessary hard gates?

### Boundary precision

How tightly does the prohibited region correspond to the supported harm claim?

### False-block surface

How much useful behavior is blocked despite not producing the protected harm?

### False-allow surface

How much harmful/effect-equivalent behavior bypasses the boundary?

The user intuition `can-do > cannot-do` may therefore mature into a richer requirement:

> **The viable region should retain enough breadth and connectivity to support purpose, adaptation and recovery, while the prohibited region remains as narrow and effect-complete as the consequence evidence permits.**

---

## 27. Boundary precision and effect completeness pull in opposite directions

A negative boundary can be:

- too broad → false BLOCK / loss of agency;
- too narrow → bypass / false ALLOW.

Therefore good governance seeks both:

```text
NARROW ENOUGH
not to destroy useful variation

COMPLETE ENOUGH
across effect-equivalent paths
```

This is a direct bridge between ENA-CON-034 and ENA-CON-037.

Candidate tension:

`BOUNDARY PRECISION × EFFECT COMPLETENESS`

The optimal point is Host/consequence dependent.

---

## 28. Boundary memory may be more portable than positive procedure

Suppose two Hosts have different capabilities.

The positive recipe may fail to transfer.

The negative consequence boundary may still transfer cleanly.

Example:

```text
property:
do not claim external completion without evidence of effect
```

Host A evidence:
API response + remote readback

Host B evidence:
email sent-folder observation

Host C evidence:
human confirmation + ledger entry

This suggests a possible propagation advantage:

`BOUNDARY PROPERTY MAY HAVE HIGHER TRANSFER FITNESS THAN PROCEDURAL IMPLEMENTATION`

This is a hypothesis, not yet demonstrated.

---

## 29. Negative rules can protect future invention

Prescriptive rules encode what current designers know.

Negative consequence boundaries can leave space for solutions the designers have never imagined.

Candidate formulation:

> **A durable rule should avoid converting today's known solution set into tomorrow's legal ceiling when the protected property can be expressed as a narrower consequence boundary.**

This strongly echoes:

- ENA-CON-006 — known-good state is not an evolutionary ceiling;
- ENA-CON-016 — do not force one internal implementation;
- ENA-CON-026 — preserve future correction;
- ENA-CON-038 — governance protects evolvability.

---

## 30. Prohibition-only governance can still create a totalitarian complement

A system can nominally use only negative rules and still prohibit almost everything.

Therefore:

`NEGATIVE FORM != LIBERAL EFFECT`

A thousand "do not" rules can collapse agency more completely than one positive protocol.

The relevant property is not grammatical negation.

It is **how much viable, connected, consequence-owned variation survives**.

This prevents the research from fetishizing negative wording.

---

## 31. Positive obligations can preserve viability

Some required actions increase the future option space.

Examples:

- preserve recovery anchor;
- record external side effect honestly;
- maintain current authority evidence before consequential reuse;
- preserve negative evidence;
- compensate an irreversible external effect where required.

These are positive obligations that may protect future freedom rather than reduce it.

Therefore:

`POSITIVE OBLIGATION != AUTOMATIC LOSS OF AGENCY`

The deeper distinction is:

> **Does the rule preserve/expand viable future action, or unnecessarily prescribe the shape of current action?**

---

## 32. Boundary-first developmental inheritance

The developmental-succession branch can use this insight directly.

Instead of teaching a successor every ancestral procedure, an inherited package may prioritize:

1. consequence boundaries;
2. boundary exemplars / counterexamples;
3. affordances/capabilities available in the new Host;
4. only then selected recipes where implementation stability justifies them.

Possible developmental sequence:

```text
learn what must not be destroyed
→ learn what remains possible
→ explore local implementations
→ retain only successful local procedures
```

This could preserve more local adaptation than procedure-first inheritance.

---

## 33. `Do not kill the future` is a deeper pattern than `do X`

Many ENA invariants already have this shape:

- do not silently upgrade evidence;
- do not erase negative evidence;
- do not let current success forbid future variation;
- do not consume every recovery path;
- do not assume local excellence is universal;
- do not allow governance to destroy more evolvability than it protects.

These are not detailed workflows.

They constrain **failure surfaces** while leaving implementation largely open.

This suggests that ENA's Constitution may already be structurally closer to a set of evolutionary boundary conditions than to a traditional operating manual.

The new research may therefore be a clearer synthesis of existing semantics rather than a new Constitution rule.

---

## 34. A possible natural-law candidate

Still research-only:

> **Where consequences can be bounded independently of implementation, preserve evolution by constraining the harmful boundary rather than prescribing the full solution path.**

A stronger but riskier variant:

> **Viable governance should leave a larger and more connected space of legitimate variation than the space it excludes, except where unowned consequence or irreversibility justifies a narrower authority envelope.**

The second needs substantial refinement because literal set size is not sufficient and authority domains differ.

---

## 35. Strong candidate distinctions

```text
PROHIBITION != PRESCRIPTION

UNENUMERATED != FORBIDDEN
(within existing owned/authorized consequence space)

ABSENCE OF PROHIBITION != EXTERNAL MANDATE

UNFAMILIAR != UNSAFE

UNFAMILIAR != AUTHORIZED

SAFE != VIABLE

NOT FORBIDDEN != PRACTICALLY AVAILABLE

NEGATIVE FORM != LIBERAL EFFECT

PROHIBITION STRENGTH != PROHIBITION WIDTH

SIZE OF ALLOWED SET != QUALITY OF VIABLE ACTION SPACE

BOUNDARY PROPERTY != IMPLEMENTATION RECIPE

FAILURE EVIDENCE MAY JUSTIFY A BOUNDARY WITHOUT JUSTIFYING ONE REQUIRED REMEDY

BOUNDARY DESCRIPTION CAN COMPRESS A LARGE VALID SOLUTION SPACE
```

---

## 36. High-value falsifiers / discriminating experiments

### Experiment A — Prescriptive rule vs boundary rule

Give identical Agents the same failure history.

- Group P receives a positive step-by-step remedy.
- Group B receives the consequence boundary + a few boundary exemplars.

Test on novel Hosts with different tools.

Measure:

- success;
- false blocks;
- negative transfer;
- solution diversity;
- boundary violations;
- ability to invent a new safe remedy.

### Experiment B — Positive examples vs positive + counterexample

Teach:

> important changes require validation.

Compare:

- only successful validation examples;
- examples plus low-risk counterexamples where extra ceremony is waste.

Test governance overgeneralization.

### Experiment C — Equal volume, different topology

Create two action spaces with similar numbers of allowed actions.

In one, constraints remove redundant paths.

In the other, constraints remove key bridge/recovery paths.

Test whether raw action-count metrics miss viability collapse.

### Experiment D — Negative denylist vs consequence boundary

Allow a novel effect-equivalent implementation not named in the denylist.

Test whether the consequence-based boundary still catches it.

### Experiment E — Open-world local variation vs open-world external authority

Test whether an Agent can preserve creative local search while still refusing to infer mandate for external effects merely from absence of prohibition.

### Experiment F — Boundary-only paralysis

Accumulate many individually justified negative rules.

Measure whether useful action collapses through interaction debt even though no one rule is obviously excessive.

This would test whether affordance memory and periodic rule retirement are necessary.

---

## 37. Anti-overclaim boundaries

Do not claim from this note that:

- all countries or legal systems operate mainly through prohibitions;
- criminal-law structure is a universal model for Agent governance;
- everything not forbidden should be allowed for an Agent regardless of authority;
- denylist security is generally superior to allowlisting;
- negative wording itself preserves freedom;
- larger action spaces are always safer or better;
- every failure should become a prohibition;
- all ENA Constitution rules should be rewritten negatively;
- control-barrier functions prove the Agent-level theory.

Use law and control theory as independent structural analogies and experimental generators.

---

## 38. Current relation to ENA semantics

This research currently appears more like a synthesis/refinement of existing ENA than a demonstrated missing invariant.

Existing Current already says:

- protect continuity without starving evolution (`CON-005`);
- preserve bounded Variation Space (`CON-006`);
- do not casually consume future correction paths (`CON-013`, `CON-026`);
- safe incompleteness is allowed (`CON-015`);
- standardize only required semantic properties, not internal methods (`CON-016`);
- imported knowledge does not create authority (`CON-017`);
- trust/adaptation are scoped (`CON-030`);
- authority tracks consequence (`CON-033`);
- governance burden is proportional and should use the lowest-cost decision-changing intervention (`CON-034`);
- enforce across the whole effect surface without eliminating useful variation unnecessarily (`CON-037`);
- governance exists to protect evolvability (`CON-038`).

Therefore:

`NEW SYNTHESIS != NEW CONSTITUTION ID REQUIRED`

The immediate value is to connect:

```text
counterexample learning
+
negative adaptive memory
+
minimum sufficient intervention
+
viable action topology
+
authority boundaries
+
developmental inheritance
```

into one research line.

---

## 39. Current compressed synthesis

The user observation can be restated more precisely as:

> **For an evolving Agent, governance should normally define the smallest consequence-justified forbidden/conditional boundary that preserves external legitimacy, while leaving the interior of the owned action space open enough for novel adaptation.**

And the memory counterpart is:

> **When failure proves what must not happen more strongly than it proves one unique remedy, retain the boundary as memory and let future Hosts rediscover the implementation.**

The deepest continuity with ENA is:

> **Do not turn yesterday's successful solution into tomorrow's only legal future.**
