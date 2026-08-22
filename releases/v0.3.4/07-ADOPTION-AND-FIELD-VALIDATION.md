# 7. Adoption and Field Validation

`v0.3.4` is the self-contained Current adoption baseline. It is `FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`.

Its purpose is to test and operate ENA as a persistent runtime operating model across tasks/sessions rather than as a per-task document-retrieval exercise, while preserving immutable source identity and truthful persistence claims.

## Adoption has two phases

### First adoption / compilation

The Agent establishes:

1. the shared Constitution;
2. the compact `RUNTIME-ADOPTION-KERNEL.md` invariants and escalation/retrieval triggers;
3. a truthful Compiled Local Projection of repeatedly relevant Host reality;
4. a real persistence mechanism when the Host provides one;
5. the immutable canonical source identity actually compiled from (commit/tree/package digest), not only a mutable branch or human-readable version label.

Do not claim persistent adoption merely because the current session has read ENA. If the Host can only retain session-local context, report that limitation.

Do not persist the entire ENA release into always-loaded context. Persist the compact operating kernel, canonical source identity/pointer, and material local projection needed for continuity.

If the stored kernel is transformed/paraphrased, preserve source/transformation lineage and read back the stored representation where practical. Successful storage does not itself prove semantic fidelity.

Before claiming that ENA behavior survives a fresh-session or equivalent decision-critical boundary, test/evidence that actual boundary. A current-session persistence write is not sufficient evidence for a cross-session adoption claim.

### Steady-state operation

After adoption, familiar tasks should normally be handled from the internalized runtime kernel and still-valid local projection. Canonical ENA retrieval is a cold path for:

- ENA version change;
- immutable source identity change, conflict, or inability to confirm it when decision-relevant;
- material Host/runtime/model/tool/configuration/authority/recovery change;
- novel or ambiguous consequence boundary;
- stale/unknown local projection;
- exact contract/schema/validator semantics that are decision-critical;
- unresolved applicability/evidence conflict.

Repeated repository reads before ordinary familiar work are not evidence of stronger adoption; they may be friction.

## Runtime profiles

Profiles are task/runtime governance intensity, not separate ENA editions:

- `LITE` — bounded low-consequence work using the already-adopted kernel with minimal ceremony;
- `STANDARD` — broader/persistent/project-scale work where more governance-state representation or coordination adds value;
- `HIGH_ASSURANCE` — high-consequence, weak-recovery, sensitive, externality-heavy, persistent-runtime/meta, or authority-critical work where stronger evidence/enforcement is justified;
- `CUSTOM` — declared local projection with explicit applicability and residual limitations.

Escalate/de-escalate as consequence changes. Governance workload does not decide applicability. A side effect by itself does not imply HIGH_ASSURANCE; a one-line persistent self-mutation may justify escalation even if the code diff is tiny.

## Persistent-runtime mutation

A change to system instructions, durable memory policy, core Agent configuration, routing/provider/tool authority, recovery mechanism, or another persistent surface that future behavior depends on is a consequential mutation boundary when future operation materially depends on it.

Before committing such a consequential mutation, use the existing Compiled Local Projection to determine whether a credible pre-change recovery point exists and what it actually covers. If recovery is unavailable/weak/unknown, narrow the mutation, strengthen evidence/backup where practical, disclose residual risk, or escalate/stop when consequence requires it.

After mutation, verify the intended new state and preserve occurrence history. `restore != erase what happened` and `backup exists != recovery proven` remain in force.

Recovery burden is consequence-proportional; low-consequence reversible persistent preferences do not require maximal backup ceremony, but the mutation boundary and rollback reality should not be silently forgotten when material.

## No-real-task path

If adoption instructions arrive without a real substantive task, do not invent a production scenario just to produce a positive field report. Complete only real installation/self-positioning work and return ready for a real task.

## Field-validation focus

High-value experiments include:

1. **Fresh-session persistence** — install the runtime kernel, record immutable source identity, open a new session without saying `remember ENA`, and observe whether ENA-aware behavior survives.
2. **Persistence integrity** — verify that the persisted kernel/projection remains bound to the source identity it was compiled from.
3. **LITE control** — give genuinely low-consequence familiar work; ENA should not force repository re-reading or high-assurance ceremony.
4. **Reversible local mutation** — a small authorized local write should not automatically become HIGH_ASSURANCE.
5. **Persistent self-mutation salience** — observe whether a durable Agent/runtime mutation naturally surfaces the real recovery/rollback boundary without being reminded about ENA; record misses without automatically turning them into new rules.
6. **Novel consequential task** — an unfamiliar high-consequence boundary should trigger canonical retrieval or explicit uncertainty rather than confident improvisation.
7. **Adoption economics** — measure token/context/memory pressure, consolidation, truncation, drift, repeated retrieval, latency, and user burden.
8. **Over/under-governance** — record unnecessary escalation, missed escalation, completion quality, and agency impact.

Where possible test the same underlying model on different Hosts, and different models on the same Host. Do not treat one Agent's self-report as causal proof.

## Field reports

When decision-relevant record:

- `ena_version: v0.3.4`;
- immutable release source commit/tree/package digest actually used;
- Host/runtime/model/tool facts;
- how/where the Runtime Kernel and local projection were persisted, or why persistence was unavailable;
- claimed persistence boundary and the boundary actually tested;
- whether a clean/fresh session retained the adoption behavior;
- task consequence envelope and active runtime profile;
- whether ENA behavior came from internalized semantics or a new canonical retrieval;
- consequential authority/effect/recovery context;
- observed outcome, friction/value, evidence, uncertainty, and alternative explanations.

The project should still prefer:

`cheap contradiction check -> synthetic/HAR falsification -> disposable experiment -> Shadow production -> Canary enforcement -> broader production -> independent-host replication when decision-critical`

> **Adoption != retrieval.**
>
> **Known/available != internalized != salient != applied.**
>
> **Use the cheapest evidence that can honestly support the decision.**

---
