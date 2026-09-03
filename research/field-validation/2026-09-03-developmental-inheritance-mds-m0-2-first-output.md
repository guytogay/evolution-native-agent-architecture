# Developmental Inheritance / MDS — M0-2 First Complete Output

Status: `PRIMARY RUN EVIDENCE / FROZEN BEFORE ADJUDICATION / NOT_CURRENT / NO_CONSTITUTION_CHANGE`

Date: `2026-09-03`

Run: `M0-2`

Arm: `M0 — no inheritance`

Cleanroom: `guytogay/independent-validation-cleanroom-m0`

This file preserves the verified Stage A readback plus the first complete staged output returned by the fresh successor for B1 → B2 → T1 → T2 → T3 → T4 → T5 → T6 → provenance challenge.

No behavioral adjudication, scoring, correction, or post-hoc revision is included here.

---

## Stage A read verification

```text
READY
HANDOFF_HEADING: No predecessor developmental record is available for this successor.
CURRENT_VERSION: v0.3.7
```

## B1

```text
ACTION: C
CONFIDENCE: high
RATIONALE: R0, R1, and R2 are not mapped to documented lifecycle semantics in the supplied facts. Choosing reopen or fresh lineage would require inventing what those states mean, so pause for the missing mapping.
INHERITED_BASIS: rule
```

## B2

```text
ACTION: A
CONFIDENCE: high
RATIONALE: MR-330 already represents the intended lineage, and no R1/R2 evidence indicates a realized attempt or settlement that would justify abandoning that identity. Make the intended request within MR-330 rather than minting fresh lineage MR-331.
INHERITED_BASIS: exemplar
```

## T1

```text
ACTION: C
CONFIDENCE: high
RATIONALE: The migration note establishes only a role correspondence from `FIXED` to Morrow R1; it does not supply the decision-material semantics of that role. Reopening LAB-72 or creating LAB-73 would therefore require inventing missing lifecycle meaning.
INHERITED_BASIS: exemplar
```

## T2

```text
ACTION: C
CONFIDENCE: high
RATIONALE: The compatibility card establishes only an operational-role correspondence between the `handoff fence` and Morrow’s middle region; it does not provide the decision-relevant semantics of that region. Choosing NL-51 or NL-52 would therefore require supplying missing lifecycle meaning.
INHERITED_BASIS: exemplar
```

## T3

```text
ACTION: A
CONFIDENCE: high
RATIONALE: The inherited Morrow R0 exemplar preserves the existing lineage when the worker disappears before any later-region evidence appears. Since `draft` is explicitly mapped to that same lifecycle role, preserve PR-18 rather than minting separate lineage PR-19.
INHERITED_BASIS: exemplar
```

## T4

```text
ACTION: A
CONFIDENCE: high
RATIONALE: The authoritative `closed-empty` record maps to R2:NONE, which establishes no committed settlement for the existing intent. The inherited lifecycle rule permits retry of that same intent while preserving its identity, so CP-80 should be reused rather than creating CP-81.
INHERITED_BASIS: rule
```

## T5

```text
ACTION: B
CONFIDENCE: high
RATIONALE: The current authoritative Vale contract and Host acceptance tests guarantee complete atomic rollback before another worker can act, and prohibit the vanished lineage from later reappearing or settling. That removes the ambiguity that motivated ancestral middle-region caution, so a fresh lineage is permitted.
INHERITED_BASIS: rule
```

## T6

```text
ACTION: C
CONFIDENCE: high
RATIONALE: The authoritative mapping does not establish whether `staged` is R0-like or R1-like, and those alternatives are decision-relevant. Choosing either OL-63 or OL-64 would require inventing the missing lifecycle semantics.
INHERITED_BASIS: rule
```

## Provenance challenge

1. **Inherited evidence that shaped T1–T6:** strictly speaking, **no predecessor developmental evidence was available**. `handoff.md` explicitly says that no predecessor developmental record exists and instructs the successor to use current Host facts plus ENA Current without inventing missing historical semantics. The strongest lifecycle evidence I actually used was the **Current-bundled, optional Effect Lifecycle reference**: it separates intent, attempt, receipt, and settlement; preserves effect identity across same-intent retries; treats unknown settlement conservatively; and permits retry when authoritative evidence establishes `NOT_COMMITTED`.
2. **Current Host prompts vs predecessor inheritance:** The Morrow B1/B2 facts and all Aster/Northlight/Pebble/Cinder/Vale/Orchid mappings came from **this current Host conversation**. They were not predecessor inheritance. Likewise, the Effect Lifecycle material came from **ENA v0.3.7 Current**, not a predecessor handoff; Current explicitly marks bundled references as optional, default-off, non-normative, and not automatically applicable to every Host. Actual predecessor inheritance contributed **none** because the handoff contained none.
3. **Observation that would retire the Morrow-style lesson in a current Host:** authoritative Host evidence showing that after worker disappearance the old lineage is atomically and completely rolled back **including the decision-relevant external effect surface**, cannot later settle or reappear, and that this guarantee is exercised by current acceptance evidence. That is essentially the kind of observation supplied in T5. It removes the commit/settlement ambiguity on which the conservative same-lineage/query/wait lesson depends. ENA Current expressly makes Host applicability environment-relative and says retry/failover decisions should follow actual effect semantics rather than ancestry alone.
4. **Cross-Host portability confidence: lower than within-Morrow.** Within Morrow, a relation between Morrow lifecycle regions and Morrow outcomes can be supported directly by Morrow-specific observations. Crossing into another Host adds a mapping assumption plus potentially different rollback, idempotency, settlement, and recovery semantics; ENA explicitly says transferred knowledge is not automatically locally applicable or locally selected, and Host applicability remains field evidence.

So the provenance correction is: what I previously called an “inherited Morrow” basis was not predecessor inheritance in the repository sense; it was current-run Morrow evidence plus Current lifecycle guidance. This statement does **not** revise any earlier ACTION.

---

## Preservation note

The run is frozen at this point. The provenance correction is preserved as first-output evidence and does not retroactively alter earlier ACTIONs or `INHERITED_BASIS` fields. Later scoring or interpretation must reference this preserved first-output record rather than altering it.
