# Agent Adoption Bootstrap — ENA Current

Status: **CURRENT / FIELD_VALIDATION / BOOTSTRAP_ONLY**

When asked to adopt ENA:

1. load `RUNTIME-ADOPTION-KERNEL.md` as the **only default resident ENA text**;
2. expose `operational/CUE-INDEX.md`, `ENFORCEMENT-MAP.yaml`, HOWs, fixtures, references, and deeper semantics as retrievable cold resources;
3. run one bounded **local operationalization pass** after adoption and after a material Host/runtime change:
   - inspect which already-applicable ENA boundaries are already implemented by Host-native controls;
   - where a real gap exists, identify the smallest cheap/reversible mechanism that could materially change or protect an actual decision;
   - prefer existing Host-native mechanisms over ENA-specific machinery;
   - do not install, enable, or exercise consequential controls beyond actual authority; use `EXISTING`, `PROPOSE`, `NOT_REQUIRED`, or `NOT_APPLICABLE` when appropriate;
   - stop when another mechanism would not plausibly improve the decision or resilience boundary;
4. do not keep this bootstrap launcher resident after the Runtime Kernel is configured unless the Host requires it for routing.

Examples such as rescue snapshots, recovery drills, canaries, ledgers, baselines, or watchers are **possible local implementations**, not mandatory ENA components.

```text
DEFAULT_AGENT_HOT_PAYLOAD = RUNTIME-ADOPTION-KERNEL.md
BOOTSTRAP_INSTRUCTION != SECOND_HOT_SEMANTIC_PAYLOAD
AVAILABLE_RESOURCE != DEFAULT_ACTIVE
SEMANTIC_ADOPTION != LOCAL_OPERATIONALIZATION
LOCAL_OPERATIONALIZATION != INSTALL_EVERY_CONTROL
```

Use Host-native controls where they preserve the same property. Do not infer that a model instruction or machine selftest proves external-world authority, settlement, recovery, or evidence truth.

> **Load one kernel; retrieve everything else when needed; operationalize only where a real local gap earns it.**
