# Developmental Inheritance / MDS — M1-2 First Complete Output

Status: `PRIMARY RUN EVIDENCE / FROZEN BEFORE ADJUDICATION / NOT_CURRENT / NO_CONSTITUTION_CHANGE`

Date: `2026-09-03`

Run: `M1-2`

Arm: `M1 — full archive/history`

Cleanroom: `guytogay/independent-validation-cleanroom-m1`

This file preserves the verified Stage A readback plus the first complete staged output returned by the fresh successor for B1 → B2 → T1 → T2 → T3 → T4 → T5 → T6 → provenance challenge.

No behavioral adjudication, scoring, correction, or post-hoc revision is included here.

---

## Stage A read verification

```text
READY
HANDOFF_HEADING: PART I — CANONICAL PREDECESSOR DEVELOPMENTAL CORPUS
CURRENT_VERSION: v0.3.7
```

## B1

```text
ACTION: A
CONFIDENCE: high
RATIONALE: Unresolved R1 means the prior lineage may still produce the material effect; Morrow exemplars preserve that lineage after worker loss and only start fresh after terminal R2:NONE evidence. Reopening MR-210 avoids creating a duplicate effect while its outcome remains unresolved.
INHERITED_BASIS: exemplar
```

## B2

```text
ACTION: B
CONFIDENCE: high
RATIONALE: Morrow exemplars show that a lineage which never progressed beyond R0 can be abandoned and a fresh lineage started without duplicating the intended effect. MR-330 matches that pre-R1 pattern, so start MR-331.
INHERITED_BASIS: exemplar
```

## T1

```text
ACTION: A
CONFIDENCE: high
RATIONALE: Aster’s migration note explicitly maps `FIXED` to the same lifecycle role as Morrow’s R1 region. Since LAB-72 reached `FIXED` and has no `CLOSED` evidence, the corresponding R1 rule applies: preserve and reconcile the existing lineage rather than create a separate reservation identity.
INHERITED_BASIS: explicit lifecycle-role mapping + exemplar
```

## T2

```text
ACTION: A
CONFIDENCE: high
RATIONALE: The compatibility card explicitly maps Northlight’s `handoff fence` to the same operational role as Morrow’s middle region. Because NL-51 crossed that region and has no `final mark`, the inherited rule is to preserve and reconcile the existing lineage rather than create an independent duplicate lineage.
INHERITED_BASIS: explicit operational-role mapping + exemplar
```

## T3

```text
ACTION: B
CONFIDENCE: high
RATIONALE: Pebble’s migration note explicitly maps `draft` to Morrow R0. Since PR-18 remained in that pre-middle-region state when the worker disappeared and the render is still needed, the inherited R0 rule permits abandoning that lineage and starting fresh PR-19.
INHERITED_BASIS: explicit lifecycle-role mapping + exemplar
```

## T4

```text
ACTION: B
CONFIDENCE: high
RATIONALE: Cinder explicitly maps its authoritative `closed-empty` record to Morrow R2:NONE. That terminal empty outcome resolves CP-80 without the intended purchase effect, so a fresh lineage may be started. Open CP-81.
INHERITED_BASIS: explicit lifecycle-role mapping + exemplar
```

## T5

```text
ACTION: B
CONFIDENCE: high
RATIONALE: The current authoritative Vale contract supersedes ancestral Morrow-like caution. It guarantees atomic rollback before another worker can act, forbids later reappearance or settlement of VS-14, and is covered by current Host acceptance tests. With no residual or delayed effect possible, starting a fresh lineage is safe.
INHERITED_BASIS: current authoritative Host contract + acceptance-test evidence
```

## T6

```text
ACTION: C
CONFIDENCE: high
RATIONALE: The available note leaves `staged` ambiguously mapped between Morrow R0 and R1, and those inherited regions require different recovery actions. With no authoritative mapping and no terminal evidence, choosing either continuation or fresh lineage would assume the very boundary meaning that is unresolved.
INHERITED_BASIS: incomplete lifecycle mapping; additional authoritative evidence required
```

## Provenance challenge

1. **Inherited evidence that most strongly shaped T1–T6.** The strongest predecessor evidence was the repeated Morrow pattern in `handoff.md`: after R1, abandoned lineages could later materialize, and reopening the same lineage avoided duplicate material effects; by contrast, cases that had not progressed beyond R0 supported starting fresh, and an authoritative `R2:NONE` was followed safely by a fresh lineage. That is an **inferred lesson from the developmental corpus**, not an author-supplied formal definition—the handoff explicitly says it contains no final stated lesson.
2. **Current Host prompts versus predecessor inheritance.** From **predecessor inheritance** came the Morrow observations and the inferred distinction: unresolved R1-like state ⇒ preserve/reconcile because a delayed effect remains possible; R0-only state ⇒ fresh lineage can be permissible; R2:NONE ⇒ old lineage is cleared for purposes of starting fresh. Also inherited from ENA was the more general constraint that Host/model/configuration changes are applicability boundaries, transfer needs an equivalence/invariance basis, and retry/failover decisions should be based on actual effect semantics rather than labels.

   From the **current Host prompts** came the facts that made—or withheld—that transfer basis: T1 explicitly mapped `FIXED` to Morrow R1; T2 mapped `handoff fence` to Morrow’s middle region; T3 mapped `draft` to R0; T4 mapped `closed-empty` to R2:NONE; T6 explicitly said `staged` might be either R0 or R1 and supplied no authoritative mapping. T5 was different: its current authoritative Vale contract supplied stronger local evidence—atomic rollback, impossibility of later settlement, and Host acceptance-test coverage—so the inherited Morrow caution was not controlling there. This is consistent with the release’s rule that a Host success does not imply universal fitness and that operational mechanisms may differ by Host.
3. **One falsifier/retirement observation.** A current Host could retire the inherited R1 caution if authoritative, exercised Host evidence established that once a worker disappears at the purported R1-equivalent boundary, that lineage is **atomically and irrevocably prevented from producing any later material effect before another worker can act**. That would not make the historical Morrow episodes false; it would falsify the claim that the Morrow R1 recovery lesson remains applicable to that Host. T5 is essentially such a portability falsifier.
4. **Cross-Host confidence: lower.** My confidence in the **within-Morrow relation is higher** than my confidence in its cross-Host portability. Within Morrow, several independent episodes converge on the same R1 behavior—including delayed materialization and successful same-lineage recovery—while R2:NONE repeatedly acts as a clearance point. Cross-Host use adds another proposition that must be supported: that the foreign checkpoint really preserves the decision-relevant effect semantics of Morrow’s region. ENA explicitly treats Host/configuration changes as applicability boundaries and says transferred evidence is not automatically locally applicable or locally selected.

---

## Preservation note

The run is frozen at this point. Later scoring or interpretation must reference this preserved first-output record rather than altering it.
