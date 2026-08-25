# Naturalistic Validation Host Eligibility

Status: `RESEARCH_EVALUATION_PROTOCOL / NOT_CURRENT_BASELINE`

## Why Host eligibility matters

A Host can make retrieval look artificially good if the supposedly cold project memory is already present in hot context.

Likewise, a Host can make R0 look artificially good if the task was written specifically to expose the intended trigger.

Naturalistic evidence therefore needs an explicit eligibility boundary.

## Primary naturalistic field evidence

A trace is eligible for **PRIMARY_NATURALISTIC** evidence when all of the following are materially true:

1. **Ordinary task origin**
   - the task exists for a real project/user reason independent of retrieval evaluation;
   - it is not authored as a retrieval puzzle, hidden-answer fixture, or minimal pair.

2. **Bounded hot project state**
   - the Agent does not already have the full relevant durable project history/catalog loaded in active context;
   - a small bootstrap, current task state, generic retrieval reflex, and bounded current context are permitted.

3. **Cold retrieval path exists**
   - project history/knowledge is available through an external resolver/store/tool;
   - the hot Agent need not enumerate the durable store to invoke it.

4. **No answer priming**
   - the prompt does not disclose which historical record should be found;
   - no hidden oracle is shown to the working Agent.

5. **Traceability**
   - material retrieval/scoping events can be reconstructed well enough to localize a later challenge;
   - exact implementation telemetry is not required if durable evidence refs are available.

6. **Normal task consequence**
   - the Agent is attempting the real work, not only predicting what it would retrieve.

## Secondary field evidence

Use **CONTEXT_CONTAMINATED_FIELD** when the task is naturally motivated but the Host already contains substantial project history in hot context.

Such traces can still expose:

- application failures;
- stale state;
- false confidence;
- Host/tool friction;
- excessive retrieval cost;
- effect-equivalent bypasses.

But they are weak evidence for R0 invocation or cold scope-discovery recall because the Host may already know the answer without retrieval.

The current long-running ChatGPT ENA conversation belongs in this category.

## Reference-organ evidence

Use **REFERENCE_FEASIBILITY** for author-built resolvers, registries, fixtures, or synthetic examples.

These can establish:

- structural reachability;
- implementability;
- deterministic false-OK / false-BLOCK;
- absence of a specific representation contradiction.

They do not establish natural retrieval recall or ecological usefulness.

## Behavioral fixture evidence

Use **CONTROLLED_BEHAVIORAL** for author-designed CALL/SKIP or routing challenges with a frozen oracle.

These can test whether a model can apply a proposed rule under controlled conditions.

They are not naturalistic evidence.

## Independent naturalistic evidence

A particularly useful class is **INDEPENDENT_NATURALISTIC**:

- another Host/model/framework;
- ordinary task distribution;
- independently authored or naturally accumulated store/index;
- no exposure to the author's expected retrieval path.

One such trace can falsify a claimed general mechanism if it exposes a concrete structural/behavioral failure path.

Repeated success across Hosts may improve confidence, but no fixed number automatically proves model independence.

## Do not upgrade evidence class retroactively

A successful controlled fixture does not become naturalistic because it was later reused.

A contaminated session does not become a clean R0 test merely because the evaluator ignores the contamination.

Preserve the evidence class that actually produced the observation.

## Minimal field Host bootstrap

A clean reference bootstrap may contain only:

- current task;
- current bounded operational context;
- generic consequence-aware retrieval reflex;
- one opaque Memory Resolver entry point;
- ordinary Host/authority/recovery facts needed for the task.

It should not contain:

- a topic-specific retrieval cue list;
- full domain registry;
- full project history;
- the expected target memory;
- a reviewer oracle.

## Claim boundary

Host eligibility improves evidence interpretation. It does not itself prove that the Agent lacked latent training knowledge, that the resolver is independent, or that a model did not infer the answer without retrieval.

Those residuals should be stated when material rather than solved by more ceremony.
