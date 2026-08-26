# Finite-Context Adoption — deployment recipes

Status: `RESEARCH_DEPLOYMENT_RECIPES / NOT_CURRENT`

This directory intentionally contains **separate deployment tools** for different HOW lineages.

It is not one adapter framework and does not define a mandatory Host profile.

```text
HOW-A File/Git tiny+cold
  -> install_file_git_adoption.py

HOW-B tool-native retrieval
  -> gate_native_retrieval_result.py

HOW-C monolithic-hot
  -> inspect_monolithic_hot_projection.py

HOW-D compiled Local Projection
  -> compile_local_projection.py
```

The scripts do not share one required runtime object model because the underlying Host mechanisms are materially different.

## Degradation alarm

If future work tries to replace these with one universal class such as:

```python
class AdoptionAdapter:
    resident_kernel
    resolver
    cold_store
    refresh_hook
```

stop and ask whether the interface is silently assuming HOW-A/B/D architecture and thereby degrading HOW-C or a native Host mechanism.

Shared utilities may emerge later only for genuinely identical operations such as digest calculation or Current identity comparison. Shared utilities must not become a reason to erase deployment behavior.

`CURRENT_CHANGE = NO`
