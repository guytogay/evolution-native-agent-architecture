# Finite-Context Adoption — deployment recipes

Status: `RESEARCH_DEPLOYMENT_RECIPES / NOT_CURRENT`

This directory intentionally contains **separate deployment tools** for materially different HOW lineages.

It is not one adapter framework, does not define a mandatory Host profile, and does not define a fixed number of adoption HOW slots.

Currently implemented deployment surfaces:

```text
HOW-A File/Git tiny+cold
  -> install_file_git_adoption.py

HOW-B tool-native retrieval
  -> gate_native_retrieval_result.py

HOW-C monolithic-hot
  -> inspect_monolithic_hot_projection.py

HOW-D compiled Local Projection
  -> compile_local_projection.py

HOW-E native Host organ rebind
  -> validate_native_host_rebind.py
```

`CURRENTLY_IMPLEMENTED_COUNT != ARCHITECTURAL_CARDINALITY`

The scripts do not share one required runtime object model because the underlying Host mechanisms are materially different.

HOW-E is intentionally not implemented as a subclass of HOW-D. A mature Host may already possess the needed transaction/recovery/wake/evidence/governance organs and require semantic rebinding plus gap validation rather than compilation or mechanism migration.

## Degradation alarm

If future work tries to replace these with one universal class such as:

```python
class AdoptionAdapter:
    resident_kernel
    resolver
    cold_store
    refresh_hook
```

stop and ask whether the interface is silently assuming HOW-A/B/D architecture and thereby degrading HOW-C, HOW-E, or another future native Host mechanism.

Also stop if:

- an exact current tool count becomes a validator invariant;
- a new deployment phenotype is rejected primarily because it would add another tool/HOW;
- weak deployment variants are invented merely to satisfy a requested count;
- existing distinct deployment behavior is merged merely to produce a shorter list.

Shared utilities may emerge later only for genuinely identical operations such as digest calculation or Current identity comparison. Shared utilities must not become a reason to erase deployment behavior.

See `research/reconstruction/CARDINALITY-DISCOVERY-GUARD.md`.

`HOW_CARDINALITY = OPEN`

`CURRENT_CHANGE = NO`
