# Project State — 2026-09-07 Handoff

## Current product

- Current: `v0.3.14 / CURRENT / FIELD_VALIDATION`.
- Current release merge: `d21477663013c460c88719bebdcc3f7dfe9ba3d7` (PR #223).
- Predecessor / rollback / occurrence truth: `v0.3.13`.
- Main head at handoff: `6092517d374c09980621664f8e004dac07a902a3`.
- Main commits after the v0.3.14 release changed control plane/live status only; `releases/current/` bytes remained unchanged.

v0.3.14 keeps the v0.3.13 Minimum Evolution Loop and surfaces the existing Local Projection persistence contract in minimum adoption. Important boundaries remain:

```text
SEMANTIC_ADOPTION != LOCAL_OPERATIONALIZATION
LOCAL_OPERATIONALIZATION != INSTALL_EVERY_CONTROL
LOCAL_PROJECTION != SHADOW_ENA_BASELINE
EVOLUTION_VOCABULARY != EXECUTABLE_EVOLUTION_LOOP
PROTECTION_OF_EVOLVABILITY != EVOLUTION_ITSELF
EVOLUTION_LOOP != CONTINUOUS_SELF_EDITING
```

## Active field stream

Issue #208 is the version-neutral Current field-validation stream.

Findings F-208-01 through F-208-10 are recorded in live state. Most recent:

`F-208-10_SAME_VERSION_CURRENT_BYTE_MUTATION_NOT_MACHINE_REJECTED`

PR #224 demonstrated that the existing Main Gate and Current Validate could remain green while a contribution changed released Current bytes without changing `ena_version`. This was a real control-plane defect.

PR #225 fixed it by adding `.github/workflows/current-immutability.yml`. The workflow compares changes under `releases/current/**` against `CURRENT-BASELINE.yaml` and rejects same-version effective-content mutation. PR #226 recorded the finding/fix in `NOW.md` and `CURRENT-HANDOFF.yaml`.

## Active contribution: PR #224

External Agent contribution PR #224 rewrites the 19 compact Durable distinctions in the one hot Runtime Kernel into numbered trigger-style positive rules.

Contributor occurrence:

- branch: `trigger-style-durable-distinctions`;
- original head: `b4b0369d5a4e20550a64d1abf5b13968588fddff`;
- one changed file: `releases/current/RUNTIME-ADOPTION-KERNEL.md`;
- original diff: +39 / -21 lines;
- current state at handoff: OPEN / DRAFT;
- maintainer disposition: `ACCEPT_DIRECTION / REQUEST_NARROWING / SUCCESSOR_REQUIRED`.

Why not merge as written:

1. v0.3.14 is immutable; any adopted text change requires successor identity.
2. Several trigger expansions are not actually semantics-neutral:
   - purpose-relative continuity is reduced to “does it still serve the same goal?”, while Current defines decision-scoped continuity relations and purpose is only one possible dimension;
   - local success adds a specific cross-Host validation prescription;
   - migration says “run local validation”, risking a universal ritual rather than receiver-local reality contact when decision-relevant;
   - correlated agreement is collapsed to exactly one support unit;
   - UNKNOWN defaults only to QUERY/WAIT, excluding other legitimate outcomes such as REFUSE, KEEP_LATENT, NOT_APPLICABLE, or remaining UNKNOWN.
3. The contribution expands the only default hot semantic payload substantially. The claim that reduced negative-inference cost offsets token/context cost is a plausible hypothesis, not established field evidence.

Preferred direction if refined: compact hybrid trigger rules, e.g.

```text
identity / purpose-relative continuity / capability / authority
-> evaluate separately; do not infer one from another.
```

Preserve compactness and exact boundary semantics. A refined candidate does not automatically justify v0.3.15.

## Research

Evolutionary-memory mechanism-discrimination campaign: CLOSED.

Metamemory durable self-modification policy: `FIELD_UNRESOLVED`.

Runtime Kernel fresh-session salience durable claim: `FIELD_UNRESOLVED`; PR #220 showed the tested high-reasoning probes were non-discriminating and had methodological confounds. Do not infer Kernel useful/useless from that observation, and do not start another salience primary without a genuinely discriminating preregisterable probe.

No active research primary.

## Immediate continuation rule

Start with live PR #224 state. If contributor changed the head, inspect the new patch before reusing this handoff's wording. If unchanged, decide whether to wait for contributor refinement or construct a maintainer-side compact candidate for comparison. Do not release merely to keep activity moving.
