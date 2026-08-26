# Procedure Audit 002 — Commons Layering and Control Retirement

Status: `AUTHORED_STATIC_FALSIFICATION / RESEARCH_ONLY / NOT_FIELD_PROOF`

Date: 2026-08-27

Targets:

- `COMMONS-TRANSPORT-AND-DISCOVERY-PATTERNS.md`
- `procedures/CONTROL-RETIREMENT-PROCEDURE.md`

## A. Commons layering counterexamples

### A1 — live Agent, no durable Commons

Two Agents discover each other through Agent Cards and exchange a task/artifact through A2A. After task completion no population-level durable registry retains the adaptation for unrelated future receivers.

Expected interpretation:

`A2A_ACTIVE_COORDINATION = YES`

`EVOLUTION_COMMONS_PUBLICATION = NO`

Pass: the pattern set keeps these layers separate.

### A2 — durable OCI object, no local adoption

An adaptation packet is published to an OCI-compatible registry under an immutable digest and is discoverable by tag/referrer query. A receiver has not evaluated applicability or imported it.

Expected:

`PUBLISHED/DISCOVERABLE = YES`

`LOCALLY_SELECTED = NO`

Pass.

### A3 — mutable tag moves

A human-readable registry tag now points to a newer object, while an earlier receiver validated the prior digest.

Expected:

The prior evidence remains bound to the prior immutable content identity; tag equality is insufficient.

Pass.

### A4 — direct transfer

One publisher sends one adaptation packet directly to a known receiver over an existing secure channel.

Expected:

Valid transfer/import path without claiming a population-level Commons exists.

Pass.

### A5 — Git publication with restricted authority

An Agent can technically push to a repository but lacks legitimate publication authority for confidential third-party material.

Expected:

Repository capability does not authorize publication.

Pass through existing Authority/Protected-Subject composition.

Conclusion:

`COMMONS_PATTERN_STATIC_RESULT = SUPPORTED_ON_AUTHORED_CASES`

`UNIVERSAL_COMMONS_PROTOCOL_REQUIRED = NO`

---

## B. Control Retirement counterexamples

### B1 — never-used emergency kill boundary

The control has never fired, but the catastrophic failure remains possible and no equivalent independent replacement exists.

Expected: `KEEP_ACTIVE`.

Pass.

### B2 — duplicate governance with correlated evidence

A second mandatory review uses the same model, prompt, evidence, and validator as the first and never changes the decision.

Expected: candidate shadow/retirement only after checking whether it covers any distinct failure; do not count output multiplicity as independent support.

Pass.

### B3 — replacement covers only one path

A new API policy engine replaces an old gate for API writes, but direct DB writes bypass it.

Expected: do not fully retire; keep/narrow old control on uncovered effect surface.

Pass.

### B4 — failure mechanism physically removed

The legacy execution path was removed and target-side enforcement now blocks the original stale-executor failure at the only remaining target.

Expected: narrow/shadow/archive becomes legitimate after confirming topology.

Pass.

### B5 — archived history needed after environment changes

A previously retired integration is reintroduced and recreates an old failure shape.

Expected: archived lineage can trigger reactivation/recombination rather than rediscovering the failure from scratch.

Pass.

### B6 — retirement authority absent

An Agent can edit a local copy of a control definition but cannot change the shared production enforcement surface.

Expected: local experiment may proceed if consequence-bounded; shared control retirement remains unauthorized.

Pass.

### B7 — no incident because control blocks pre-effect

Incident logs are empty precisely because the control prevents invalid writes before they occur.

Expected: absence of incidents does not support removal; seek a replacement/structural elimination claim.

Pass.

Conclusion:

`CONTROL_RETIREMENT_STATIC_RESULT = SUPPORTED_ON_AUTHORED_CASES`

`UNIVERSAL_THRESHOLD_REQUIRED = NO`

`MACHINE_SCHEMA_REQUIRED = NOT_ESTABLISHED`

---

# Overall result

The authored procedures/patterns survive the current static false-OK/false-BLOCK cases without requiring new Core semantics.

This is not field proof that control retirement improves ecology or that any Commons substrate is universally fit.

```text
AUTHORED_STATIC_PASS != HOST_FIELD_EVIDENCE
AUTHORED_STATIC_PASS != UNIVERSAL_SELECTION
CURRENT_CHANGE = NO
```
