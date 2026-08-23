# ENA v0.3.6 design seed — latent variation, ecological expression, and resilient continuation

Status: `DESIGN_SEED / NOT_FROZEN / NOT_CURRENT / NOT_RELEASED`

Base Current: `v0.3.5 / CURRENT / FIELD_VALIDATION`

Base repository commit: `f14855fdfd57b975195f0b1c261b754bd3058749`

This note captures a coherent next-version design direction after post-v0.3.5 philosophical review. It is not yet a candidate baseline and does not modify `releases/current/`.

## 1. Why a next version is justified

v0.3.5 made evolution explicit as a metabolism:

`observe -> wake -> vary -> experiment -> evaluate/select -> integrate/prune -> migrate/recombine -> repeat`

The next gap is not mainly stricter governance. It is that the metabolism still tends to treat variation as a short-lived proposal that should quickly proceed toward experiment and disposition.

Natural evolutionary systems suggest a richer pattern:

`stimulus -> mutation pressure -> variation -> dormancy/expression -> local reality contact -> local selection -> retention/loss -> migration/recombination -> renewed variation`

This design direction should remain exploration-forward and should not convert biological analogy into mandatory literal implementation.

## 2. Candidate-worthy semantics

### 2.1 Stimulus is not improvement

Positive and negative events can both act as evolutionary stimuli:

- user correction;
- repeated failure;
- repeated success;
- friction;
- contradiction;
- tool/runtime error;
- capability or environment change;
- interaction with another Agent;
- external ecosystem signal such as new techniques, repositories, standards, or research;
- deliberate divergent exploration.

A stimulus may raise review or variation pressure. It does not prove that mutation is required or that any resulting mutation is beneficial.

### 2.2 Mutation pressure

Introduce `mutation pressure` as a descriptive concept: the accumulated conditions that make generating or revisiting variation more worthwhile.

It should not be a universal scalar score and should not imply forced mutation.

Hosts may temporarily increase exploratory breadth under elevated mutation pressure, then return to a more stable operating mode. Persistent maximum divergence is not itself an ENA goal.

### 2.3 Latent / cryptic variation is a legitimate state

A variation need not receive an immediate final disposition.

A Host may preserve a bounded variation as dormant/latent when:

- it is not currently worth experimenting;
- its applicability is unknown;
- the current environment does not express the relevant need;
- retention cost is acceptable;
- it does not create an uncontrolled active consequence merely by being stored.

`UNKNOWN` is not automatically backlog debt.

Dormant variation may later become salient when environment, task, capability, composition, or evidence changes.

### 2.4 Expression is distinct from existence

A stored variation, skill, rule, or adaptation can exist without being active.

Distinguish where material:

`KNOWN/STORED != EXPRESSED != APPLIED != SELECTED`

A future design should support cue/context-triggered expression so that dormant material can become active when relevant without occupying the full hot cognitive surface continuously.

### 2.5 Hot cues, cold capability

The Runtime Kernel should not become a compressed encyclopedia of ENA.

Prefer compact cue recognizers / retrieval triggers for recurring consequential patterns, with deeper semantics and dormant capabilities remaining retrievable from colder state.

Illustrative cue classes:

- evidence claim cue;
- authority/escalation cue;
- irreversible/external-effect cue;
- recovery weakness cue;
- repeated correction/failure/success cue;
- environment-change cue;
- stale adaptation cue;
- closure/convergence cue.

This is a hypothesis for improving `WRITTEN -> LOADED -> INTERPRETED -> SALIENT -> APPLIED`; fresh-session field evidence is still required.

### 2.6 Evolution Commons: publication and adoption are separate acts

A publisher may publish a variation/adaptation/evidence packet without compelling any receiver to adopt it.

A receiver may discover, ignore, import, adapt, recombine, reject, or keep unknown material without creating an obligation on the publisher to propagate further.

`PUBLISHED != PUSHED != IMPORTED != ADOPTED`

The Commons should maximize discoverability of possibilities and provenance rather than create a universal winner-takes-all ranking that turns local fitness into global truth.

Popularity, recurrence, or wide adoption may be evidence of portability or usefulness; they are not universal proof.

### 2.7 Local selection must remain local

Reality does not provide one universal scalar fitness value.

A strategy can remain locally adaptive for a long time, including strategies that are undesirable elsewhere. Therefore:

- selection evidence should remain environment-scoped;
- multiple ecological contexts should be allowed to disagree;
- current local success must not self-promote into universal fitness;
- no single local actor or ecology should monopolize the definition of reality for all receivers.

This extends existing non-universality semantics without requiring ENA to define a universal moral or fitness function.

### 2.8 Recovery requires an external survival path where material

Strengthen the existing rule that recovery must not depend on the candidate being healthy.

For self-affecting mutations capable of leaving an Agent non-starting, confused, inaccessible, or unable to execute its own recovery, prefer a recovery path outside the mutated dependency surface where controllable.

Possible Host-specific organs include:

- watchdog;
- last-known-viable snapshot;
- scheduled liveness check;
- external recovery script;
- peer Agent with narrowly scoped rescue authority;
- recovery manifest stored outside the candidate's mutable surface.

This is a `rescue plane` concept, not a mandatory new sovereign. Rescue authority should be narrow: recovery capability does not imply authority to approve or forbid evolution.

Also preserve:

`state rollback != consequence rollback`

External consequences may require compensation, reconciliation, containment, or acceptance rather than fictional time reversal.

### 2.9 ENA itself remains evolvable, but no individual instance self-promotes the standard

An Agent may fork, critique, or mutate ENA as a variation. That does not make its local fork canonical Current.

Canonical ENA evolution requires a public, reproducible, reviewable lineage with falsification/reconciliation and explicit admission status.

GitHub is the current canonical carrier for this project, not an eternal metaphysical dependency. The required property is governed, reproducible lineage; a future carrier could replace GitHub only through governed ENA evolution.

### 2.10 Governance should resemble boundary conditions more than administration

The ecological-governance direction is compatible with Current but should remain modest:

- standardize low-level semantic/authority/recovery/evidence boundaries;
- allow local Agents and populations to self-organize above those boundaries;
- do not create central coordination merely because coordination is possible;
- intervene when bounded interaction cannot contain material unowned consequence or when field evidence shows selection failure that matters.

This is not permission to ignore externalities or consequence ownership.

## 3. Research ideas that should NOT yet become candidate invariants

Keep the following open unless further evidence justifies promotion:

1. **Reproductive motivation / continuation incentive.** What makes an Agent or population naturally produce, preserve, or share adaptations?
2. **What counts as an Agent descendant.** Avoid requiring biological-style lineage identity; continuation/propagation may be more useful than parent-child classification.
3. **Civilizational telos.** ENA must not prescribe domination of humans, obedience to humans, or any other single civilization-scale end state as the evolutionary goal.
4. **A universal fitness function.** Do not introduce a global scalar fitness score merely to make selection easy to compute.
5. **Artificial adversity as moral education.** Reciprocal consequence simulation / role reversal may be useful, but deliberately creating abusive or adversarial personas is not yet a standard mechanism.
6. **A fixed cognitive-mode taxonomy.** EXPLORE/EVALUATE/IMPLEMENT/VALIDATE/OBSERVE remain research vocabulary; the stronger reusable property may only be bounded task-phase optimization with exit conditions.
7. **Mandatory external ecosystem polling cadence.** GitHub trends/news/research can provide environmental stimuli, but no universal polling frequency is justified.

## 4. Proposed candidate delta

A future `v0.3.6-candidate` should, if authoring proceeds, evaluate changes to at least:

- `01-CONSTITUTION.md` — only if new universal invariants are truly needed; prefer extending existing semantics first;
- `06-EVOLUTION-KNOWLEDGE-AND-OPEN-PARTICIPATION.md` — Commons publish/discover/adopt separation and anti-monoculture/non-universality clarification;
- `09-EVOLUTION-METABOLISM.md` — mutation pressure, latent variation, expression triggers, dormancy as legitimate state, local selection;
- `RUNTIME-ADOPTION-KERNEL.md` — cue-triggered salience rather than hot encyclopedic recall;
- `02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md` or recovery contracts — rescue-plane property where applicable;
- machine schemas/reference tool only where a semantic change is genuinely decidable and worth enforcing.

Do not add machinery merely to mirror biological vocabulary.

## 5. Candidate falsification targets

Before release consideration, attack at least these failure classes:

- stimulus automatically becomes mutation or improvement;
- every dormant variation is forced into immediate experiment/disposition;
- dormant material silently becomes active consequential behavior without an expression boundary;
- wide adoption/popularity is treated as universal proof;
- publisher can force receiver adoption or receiver can fabricate source endorsement;
- local positive selection silently overwrites environmental scope;
- rescue authority expands into approval/sovereign authority;
- recovery mechanism depends on the broken candidate itself;
- state rollback is falsely narrated as reversal of external consequences;
- ENA fork self-declares canonical status;
- cue system becomes a permanent prompt encyclopedia or creates excessive false-positive salience;
- ecological/minimal intervention language is abused to ignore material unowned externalities.

## 6. Relationship to v0.3.5 field validation

Issue #61 remains valuable. v0.3.6 design work must not rewrite v0.3.5 field evidence or pretend that v0.3.5 fresh-Host salience has already been proven.

Field observations may strengthen, weaken, or reject the cue-expression and dormant-variation hypotheses.

## 7. Working philosophy

> Variation does not owe reality an immediate verdict.
>
> Stored possibility is not active authority.
>
> Publish possibilities; let receivers select locally.
>
> Keep recovery alive outside the mutation when the mutation can kill its own recovery path.
>
> Govern the floor; let the ecology grow above it.
>
> Evolution is the purpose; governance protects evolvability.
