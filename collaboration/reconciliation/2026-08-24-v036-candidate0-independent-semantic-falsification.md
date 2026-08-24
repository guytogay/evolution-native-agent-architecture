# ENA v0.3.6 candidate.0 independent semantic falsification

Status:

`FRESH_INDEPENDENT_SEMANTIC_FALSIFICATION / NEEDS_REVISION / CANDIDATE.0_FROZEN / CURRENT_UNCHANGED`

This record preserves the handoff from the fresh independent semantic falsifier of frozen ENA v0.3.6 candidate.0. It does not modify candidate.0, promote Current, or constitute release reconciliation.

## Frozen object falsified

- frozen source: `3cb94d98882621acede189d0d47806efae44fb0f`
- frozen candidate tree: `80f2da918811c26381d65eb5afa8e40f8410a32e`
- Current tree: `9c928b4c99ae72e53c89978cf1d10b7ea068c182`
- freeze record commit: `15e513a72d59e28f8d3050ef877746f85ab706ba`
- PR #68 Conversation comment: `issuecomment-5389079667`

The falsifier independently reproduced the machine-green baseline before constructing adversarial probes, and read author/freeze history only after the independent attack inventory and primary probes had been recorded.

## Independent final verdict

`NEEDS_REVISION`

The verdict applies to the frozen candidate.0 artifact, not to the Evolution Ecology semantic core.

The falsifier explicitly supported retaining, rather than weakening during repair:

- the Evolution Ecology semantic core;
- the conceptual necessity of the expression axis;
- schema-level long-lived latent variation;
- Rescue Plane semantics;
- minimal-intervention governance and its anti-externality caveats;
- the inherited 38 Constitution IDs with `NEW_CONSTITUTION_IDS = 0`;
- the truthful staged boundary that full v2 runtime integration is not yet implemented.

## Material release blockers

### F-01 — evolution-record v2 integration-history regression

`schemas/evolution-record.v2.schema.json` weakened `integration_history` items to arbitrary objects with no required keys, silently losing the predecessor v1 representation hooks including `selection_state_at_commit`, `authority_basis`, and `recovery_boundary`.

Reproduction: `INTEGRATED + HARMFUL + integration_history: [{}]` was accepted by the v2 validator.

This violates the author-side principle that the candidate machine record must not silently become weaker than the validated predecessor surface.

Required successor repair: restore the predecessor integration-history contract in v2, with any expression-axis addition kept additive.

### F-02 — array order masquerades as evidence time

`validate_evolution_record_v2.py` used the final array element as the latest expression/evaluation record. v2 time fields were unconstrained non-empty strings.

Reproductions included:

- a chronologically later `HARMFUL` evaluation placed before an older trailing `SUPPORTED` evaluation, while current `SUPPORTED` still validated;
- a chronologically later `LATENT` expression placed before an older trailing `EXPRESSED` expression, while current `EXPRESSED` still validated.

Required successor repair: machine-readable timestamps plus latest-by-time validation, including explicit handling of invalid or tied latest timestamps.

## Material successor repairs

- **F-03** — migration source lineage may be omitted and local/imported evidence provenance lacks a machine representation boundary.
- **F-04** — `adaptation-packet.v1` cannot carry the new expression/dormancy axis; create an additive successor packet format rather than weakening v1 compatibility.
- **F-05** — expression-state consistency exists, but represented harmful/retired/materially consequential expression is not connected to the existing triggered-obligation mechanism. Any repair must be narrow enough not to require Variation Space for every expression.
- **F-06** — mixed `IMPROVED` + `DEGRADED` outcomes can be claimed as `SUPPORTED` without `PARTIAL` or explicit tradeoffs.
- **F-07** — external freeze assignment is defensible and accepted, but the candidate subtree lacks a durable external-freeze pointer protocol; the zh-CN manifest carries an impossible post-freeze rebinding promise; `validate_candidate.py` hard-codes `frozen: false` as the only valid state.
- **F-08** — zh-CN Runtime Kernel omits `ARCHIVED/RETIRED != selection verdict`, with no cold-layer equivalent located.
- **F-09** — full v2 runtime absence is acceptable as staged architecture, but inherited `ena_evolve.py` actively false-BLOCKs legal candidate semantics because `propose` and `import` require `--variation-space`; `validate_candidate.py` also mechanically forbids any expression-field appearance in the tool, creating a repair interlock.

## Nonblocking / research findings

- **F-10** — `ARCHIVED` does not require represented archive metadata while `INTEGRATED` does require integration history; consistency is asymmetric.
- **F-11** — future cue salience/application has no field proof; the candidate already states this honestly. This is research/field evidence, not a semantic defect.
- **F-12** — `experiments` versus broader `reality contact` terminology may underrepresent incidental observation; research wording issue.

## Falsifier self-corrections

Three initial attacks were explicitly withdrawn as false-positive attacks after semantic comparison:

- source-side `UNKNOWN` should not be copied into receiver-local selection;
- ordinary reality contact can be represented in the existing experiment item shape;
- `PROPOSED + EXPRESSED + UNASSESSED` is intentionally representable because expression is not selection.

These withdrawals are preserved because the falsifier's own oracle was also treated as falsifiable.

## Successor discipline

Any material repair must use a new candidate identity.

This branch therefore proceeds as:

`v0.3.6 candidate.1 / successor of frozen candidate.0`

Do not rewrite frozen tree `80f2da918811c26381d65eb5afa8e40f8410a32e` and continue calling it candidate.0.

`releases/current/` remains v0.3.5 until a later governed admission/release decision.
