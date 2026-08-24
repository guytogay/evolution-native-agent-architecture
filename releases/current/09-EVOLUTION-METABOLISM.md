# 9. Evolution Metabolism and Ecology — v0.3.6 Candidate

Status: `WORKING_CANDIDATE / NOT_FROZEN / NOT_CURRENT`.

This document extends the v0.3.5 evolution metabolism with a candidate ecology model. It is a reference semantics document, not a requirement that every Host implement the same organs.

## 9.1 From linear metabolism to ecological metabolism

v0.3.5 established:

`observe -> wake -> vary -> experiment -> evaluate/select -> integrate/prune -> migrate/recombine -> repeat`

v0.3.6 candidate keeps those functions but removes an overly linear implication: **a variation does not have to move immediately toward experiment or verdict.**

Working ecology:

`environment/stimulus -> mutation pressure -> variation -> latent storage or expression -> reality contact -> local selection -> retention/dormancy/loss -> inheritance/migration/recombination -> renewed variation`

Core distinctions:

`stimulus != mutation`

`mutation != improvement`

`stored != expressed`

`expressed != applied`

`applied != selected`

`local selection != universal fitness`

`publication != receiver adoption`

## 9.2 Stimulus and mutation pressure

Evolutionary stimulus may come from positive or negative events:

`USER_CORRECTION | REPEATED_FAILURE | ERROR | FRICTION | CONTRADICTION | REPEATED_SUCCESS | CAPABILITY_CHANGE | ENVIRONMENT_CHANGE | OTHER_AGENT_BEHAVIOR | EXTERNAL_DISCOVERY | CURIOSITY | RANDOM_RECOMBINATION | OPPORTUNITY | STALE_ADAPTATION`

A stimulus may increase **mutation pressure**: the opportunity or incentive to generate/revisit variations.

Mutation pressure is not a command to mutate and does not specify the direction of mutation.

A Host may deliberately create exploratory mutation pressure through divergent search, recombination, random concept collision, external ecosystem scanning, or alternative-role simulation when the cost is justified. No universal cadence is required.

`stimulus -> review opportunity`, not `stimulus -> improvement`.

## 9.3 Latent / cryptic variation

A variation may remain stored without immediate experiment, expression, or selection.

Long-lived unresolved variation is legitimate when retention is affordable/lawful and it does not create active consequential behavior merely by being stored.

Examples:

- an unused skill variant;
- an alternative workflow discovered during another task;
- a failed idea whose failure may be environment-specific;
- a strange recombination with no present use;
- a capability hypothesis awaiting a future Host/tool/environment;
- an archived adaptation that may become relevant again.

`UNKNOWN` is not automatically backlog debt.

No universal rule requires every variation to receive a final verdict.

Hosts may curate, compress, archive, or lawfully delete latent material when carrying cost exceeds plausible future value, but usage/age alone is not proof of worthlessness.

## 9.4 Expression is a separate axis

Candidate semantics add a conceptual **expression axis** independent from lifecycle and selection.

A minimal conceptual state is:

`LATENT | EXPRESSED`

Expression may change repeatedly with context without rewriting lifecycle or evidence history.

A stored adaptation can be `INTEGRATED + SUPPORTED + LATENT` between relevant tasks, become `EXPRESSED` when a cue/context calls it into active behavior, then return to `LATENT` afterward.

Expression does not mint authority. A dormant capability becoming salient does not create external mandate.

A Host may represent expression as explicit state, event history, routing, lazy skill loading, retrieval activation, or another mechanism. Standardize the semantic property, not the organ.

## 9.5 Cue-triggered salience

First adoption should not require permanent loading of the whole ENA release.

A promising runtime pattern is:

`hot cue recognizers -> retrieve/activate relevant cold semantics/capability -> act`

Illustrative cues:

- evidence/certification language -> evidence semantics;
- irreversible/delete/external-write signals -> consequence/recovery semantics;
- permission/credential/mandate change -> authority semantics;
- repeated correction/failure/success -> evolution wake;
- environment/tool/model change -> applicability/portability re-check;
- repeated governance with no decision change -> closure semantics.

Cue lists are examples, not a universal keyword engine.

A cue mechanism is successful only when it improves appropriate salience without turning ENA into permanent prompt noise. `configured` or `written` is not proof of future salience/application.

## 9.6 Variation Space and reality contact

When a variation is consequentially expressed as an experiment, use a suitable Variation Space where uncertainty can become real enough to learn from while preserving consequence ownership and correction capacity.

Examples remain branch/fork, sandbox, disposable VM/container, shadow execution, canary scope, test Agent, reversible local configuration, isolated skill version, simulation, or replay.

A variation may be aggressive inside its legitimate consequence envelope. Internal capability/permission topology may itself vary there. Internal mutation cannot self-mint external mandate.

## 9.7 Lifecycle, expression, and selection are different questions

Lifecycle:

`PROPOSED | EXPERIMENTED | INTEGRATED | ARCHIVED | RETIRED`

Expression (candidate conceptual axis):

`LATENT | EXPRESSED`

Selection:

`UNASSESSED | SUPPORTED | PARTIAL | NOT_SUPPORTED | HARMFUL | UNKNOWN`

They answer different questions:

- lifecycle: where is this material in its persistence/use history?;
- expression: is it currently activated in behavior/context?;
- selection: what has reality contact supported within the represented environment?

No transition on one axis silently upgrades another.

## 9.8 Evaluation and local selection

When reality contact occurs, record material outcomes as:

`IMPROVED | DEGRADED | UNCHANGED | UNKNOWN`

A result may be mixed.

Evidence-backed positive/negative selection still requires represented reality contact/experiment where the claim depends on that evidence.

But **selection need not happen immediately after variation creation**. A variation may remain unassessed or unknown until useful expression becomes possible.

Selection is scoped to the represented environment, Host, model, language, dependencies, consequence envelope, time, and subject as material.

A locally successful strategy may remain locally successful even if undesirable elsewhere. ENA does not assume reality automatically produces moral convergence.

Therefore:

`local success != universal recommendation`

`wide adoption != universal truth`

`survival != moral correctness`

Plural environments and receiver-side reselection help prevent one local fitness landscape from pretending to be the whole world.

## 9.9 Integration, dormancy, and pruning

Integration is not permanent expression.

A supported adaptation may be integrated into durable capability while normally remaining dormant until a relevant cue/context activates it.

Pruning remains distinct from selection history. Hosts may use:

`KEEP | UPDATE | DORMANT | ARCHIVE | RESTORE | RETIRE`

Dormancy is preferred over destructive deletion when future relevance is plausible and carrying cost is acceptable.

Evolution is neither forced churn nor endless accumulation.

## 9.10 Migration, inheritance, and propagation

Migration transfers a possibility plus represented source history; it does not transfer a conclusion.

Source result and receiver result remain separate.

The receiver may import, ignore, rediscover later, locally adapt, recombine, reject, keep unknown, or re-test.

A source `HARMFUL` variation may later succeed in a different environment after local reality contact; the source negative lineage remains truthful.

Migration packet digest still checks packet consistency only; it does not authenticate the source.

## 9.11 Recombination and emergence

Recombination remains a first-class variation generator.

It may produce conflict, cancellation, amplification, unexpected resource interaction, emergent capability, new externality, or no useful change.

Expectation of emergence is not evidence. Positive emergence is valuable when actually observed.

Exploratory cognitive modes may be one way to raise mutation pressure or recombination diversity, but this candidate does not define a fixed universal mode taxonomy.

## 9.12 Recovery and the rescue-plane property

A self-affecting mutation can damage the very Agent/process that would otherwise perform recovery.

Where material and controllable, preserve a rescue path reachable outside the damaged candidate, such as:

- last-known-viable snapshot;
- watchdog or external timer;
- recovery manifest;
- narrow recovery credential;
- peer Agent/human recovery handoff;
- independent startup/rollback path.

This is a **property**, not a mandated product architecture.

Rescue authority should be narrow. The ability to restore a failed subject does not automatically create authority to approve, forbid, or govern all of its future variations.

`state rollback != external consequence rollback`

Recovery is not a time machine.

## 9.13 Governance closure and ecological restraint

Do not add intervention merely because coordination is imaginable.

Governance should protect the semantic/consequence floor: truthful evidence, scoped authority, owned consequence, recovery/correction capacity, non-self-sealing governance, and lawful history.

Above that floor, heterogeneous Agents/Hosts may discover local organization through interaction, specialization, competition, cooperation, and adaptation.

Minimal intervention does not justify ignoring unowned externality, stale authority, irreversible escape, or known decision-changing evidence.

> **Govern the floor; let the ecology grow above it.**

## 9.14 Reference-tool boundary

The inherited v0.3.5 `tools/ena_evolve.py` does not yet fully represent mutation pressure, a latent reservoir, or the expression axis.

Until the reference tool/schema are modified and validated, the presence of these concepts in this candidate document is **semantic authoring**, not machine-enforced proof.

Do not narrate the tool as implementing semantics it does not yet implement.

## 9.15 Retained v0.3.5 residuals

The inherited research residuals remain visible unless new evidence changes their importance:

- repeated evaluation/reinterpretation of one represented experiment;
- nested visibility of source-negative lineage after receiver positive reselection;
- no in-place restore/reopen path for archived/retired candidates in the inherited reference tool;
- migration-lineage depth growth across generations.

> **Variation does not owe reality an immediate verdict.**
>
> **Stored possibility is not active authority.**
>
> **Selection is local; propagation is not proof.**
