# Operational Architecture — v0.3.8 Current

Status: `CURRENT / COLD_HOW_LIBRARY`

This is the practical cold HOW layer. It helps an adopter move from a real problem to usable implementation branches without reading project research.

```text
ordinary cue
-> CUE-INDEX
-> HOW-MAP
-> REFERENCE-INDEX when exact local path is needed
-> applicability / Host filter
-> procedure / optional reference / Host mechanism
-> action / WAIT / UNKNOWN / REFUSE / NOT_APPLICABLE
```

The full HOW library is not mandatory active context. One semantic property may have several valid Host-specific HOWs.

A bundled reference is optional unless applicability says otherwise; package inclusion does not activate it.

A useful HOW changes what an Agent can actually do and exposes relevant failure/fallback/evidence/non-applicability boundaries.

`WHAT_WHY_SUPPORTED != HOW_A_SUPPORTED != HOW_A_SUPPORTED_ON_HOST_X`

> **Compress the semantic trunk; let concrete HOWs branch.**
