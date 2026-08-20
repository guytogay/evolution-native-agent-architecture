# Network-Protocol Design Extraction for ENA

Status: `RESEARCH / CONVERGENCE_PASS / ISSUE-14 / NOT_PROMOTED`

## Purpose

Convert the earlier divergent network-protocol analogy exploration into a small set of ENA-relevant design candidates. This document deliberately stops collecting additional protocol analogies and asks instead:

> Which structural lessons could change an ENA decision, expose a missing failure class, or justify a cheap experiment?

`Protocol analogy != evidence != ENA rule != implementation requirement.`

## Convergence result

### Class A — Mostly validates existing ENA semantics

These analogies are useful explanatory evidence but do not currently justify new ENA mechanisms.

- **OSPF / link-state:** shared map + local action strongly resembles `Full map, local projection` and `Broad knowledge, narrow authority`.
- **DNS:** delegated retrieval, caching, and freshness resemble `Open Knowledge != Always Loaded Knowledge` and scoped applicability.
- **LLDP/LACP:** capability advertisement is not authorization; cooperation requires compatible/bilateral conditions. Existing capability/authority separation already covers much of this.
- **TCP/ECN:** signal-driven adaptation resembles Minimum Sufficient Intervention and graduated response. Treat as support for MSI experiments, not a separate subsystem.
- **CSMA/CD obsolescence:** a once-useful control can become governance debt after topology changes. This reinforces control revalidation/retirement research rather than requiring a new invariant.

Decision: **do not add ENA rules for these now.**

### Class B — Actionable research candidates

Three protocol-derived structures appear capable of exposing missing failure classes and are worth direct experiments.

#### B1 — Circular provenance / self-confirming support paths

Network inspiration: BGP AS_PATH / split-horizon-style loop prevention.

Potential ENA failure:

`Source A -> Agent B -> Agent C -> Source A` can look like multiple confirmations even though all support descends from one origin. Similar loops can occur in evidence, delegation, approval, or recommendation chains.

Research property:

> A support/delegation path that returns to its own origin must not gain independence or authority merely by traversing more actors.

Experiment: `CIRCULAR-PROVENANCE-PATH-EXPERIMENT.md`.

#### B2 — Mixed-baseline transition safety

Network inspiration: transient routing microloops / blackholes during distributed convergence.

Potential ENA failure:

Each final baseline may be internally correct while a rolling transition creates a temporary population where different actors use incompatible versions, schemas, assumptions, or adoption instructions. The v0.3.1-BETA.1 ZIP/repo identity incident is an ENA-native example of this class.

Research property:

> Final convergence correctness does not imply transition safety.

Experiment: `MIXED-BASELINE-TRANSITION-SAFETY-EXPERIMENT.md`.

#### B3 — Authority lease / expiry semantics

Network inspiration: DHCP leases and failover-role protocols.

Potential ENA failure:

Authority may remain linguistically or persistently attached to an actor after the host, route, model, configuration, role binding, task, or time window that justified it has changed.

Existing ENA already says restored state does not automatically restore authority and binding changes can invalidate evidence applicability. The open question is whether **lease-like authority validity** is a useful explicit implementation pattern or merely another vocabulary layer.

Experiment: `AUTHORITY-LEASE-EXPIRY-EXPERIMENT.md`.

### Class C — Keep as lower-priority candidate patterns

These may be useful but do not yet justify dedicated experiments ahead of B1-B3.

- **STP dormant redundancy / single active effect graph:** useful for recovery and avoiding simultaneous consequential loops; may already be covered by stable-state/recovery/authority rules.
- **IP TTL / hop limit:** bounded retries, recursive self-review, delegation depth, or remediation attempts may cheaply cap runaway loops. Strong implementation pattern; evidence needed before universalizing.
- **GREASE / anti-ossification:** deliberately exercise harmless novelty to preserve future extensibility. Very interesting for evolution readiness, but needs a concrete ENA host experiment.
- **BGP policy routing:** potentially useful for polycentric governance and local preference, but likely descriptive rather than normative for ENA.

### Class D — Beautiful analogy, no current engineering action

Any protocol analogy that cannot produce a concrete failure claim, changed decision, or cheap test remains explanatory only.

## Cross-cutting design lesson

The strongest recurring network pattern is not any specific protocol:

> **Standardize the properties required for interoperability; preserve implementation diversity elsewhere.**

This is already close to `Protocol-Level Unity, Cognitive Diversity`. The current research task is therefore not to add another slogan, but to identify where ENA still lacks a testable boundary around circular support, transition safety, or stale authority.

## Relationship to temporary cognitive modes

The same convergence discipline applies to research itself:

`EXPLORE -> EVALUATE -> IMPLEMENT/EXPERIMENT -> VALIDATE`

The network-protocol exploration phase has now ended for this pass. Additional protocol names should not be added unless they reveal a materially new failure class not represented here.

## Next decision gates

For B1-B3, prefer cheap synthetic/HAR tests first.

A candidate should move closer to Current only if at least one of the following occurs:

- it detects a real false claim or unsafe authority state that Current misses;
- it changes a consequential decision;
- it reduces governance cost while preserving protection;
- recurrence appears across independent hosts or evidence domains.

Otherwise keep it as research or merge it into existing ENA semantics.