# Old-line salvage audit: what the theory corpus can still give the clean product

Status: `RESEARCH / NOT_PROMOTED`. Date: 2026-09-14.
Method: four read-only digests run in parallel over the theory corpus, each item judged against the
clean product's four-item contract budget rather than against how complete the theory reads.

## 0. Result in one line

**Zero port candidates.** Four routes — the Current operational architecture, all 20 research
prototypes, the 9 packaged reference mechanisms, and the incident/evidence/field-validation/history
surface — produced **no mechanism that passes the budget**. What the corpus does give the clean
product is the three things a product cannot generate about itself: a **falsified-hypothesis
library**, a **retirement history**, and **evidence that disposes of three pending proposals**.

## 1. What was searched, and what "evidence" means here

```text
releases/current/operational/**            cues, HOW map, procedures, patterns
releases/current/05, 09, ENFORCEMENT-MAP   contracts, metabolism, enforcement classes
releases/current/references/**             authority-lease, effect-lifecycle, recovery-adapter,
                                           retrieval-obligation, wait-state, contested-authorship,
                                           evidence-dependency-map, evidence-envelope, manifest
research/prototypes/** (20)                including v2-machine-contract-hardening v2.1–v2.4.1
research/{incidents,experiments,field-validation,methodology,history,status-notes,reconstruction}/**
evidence/**, HISTORY.md, NOW.md, LINEAGE.md, releases/current/{CHANGELOG,LINEAGE}
```

**A method warning that must travel with every number below**: of the 20 prototypes, **one** keeps a
frozen result JSON family (`v2-machine-contract-hardening`) and **one** keeps execution output
(`evolution-record-progressive-envelope/SELFTEST-RESULTS.md`). The other 18 offer *re-runnable
fixtures plus selftest*, not archived measurements. The corpus's own audit labels this
`STATIC_EXECUTION_DEPTH_AUDIT / NOT_FIELD_EVIDENCE`. **Specification completeness is not field
validation**, and reading a complete-looking spec as mature is the exact mistake the budget exists to
prevent.

## 2. Distribution of the verdicts

| verdict | count | examples |
| --- | --- | --- |
| `ALREADY-IN-PRODUCT` | 8 | authority-lease (boundary form), effect-lifecycle, recovery-adapter (core), contested-authorship (partial), evolution-loop, host-mappings, reference-index anchors, recovery/composition rules of §5.4/§5.7 |
| `RECORD-NOT-PORT` | 12+ | cue-index / how-map routing, **control-retirement procedure**, purpose-relative continuity, standing-input, evolution-commons, enforcement classification, retrieval-obligation, wait-state, evidence-envelope, evidence-dependency-map, reference-manifest, ~14 prototypes |
| `PORT-CANDIDATE` | **0** | — |
| `FALSIFIED` | 4 direct + 2 self-falsifications | see §3 |
| `DONT` | 1 | `SEMANTIC-GLOSSARY.yaml` as a prose glossary |
| `SPECULATION` | 1 | tiny-hot-kernel: 36 blind prompts and an oracle exist, the controlled run was never executed |

## 3. The falsified library — the most reusable output

This is the part worth keeping even though nothing is ported. Each line is a hypothesis the corpus
already killed, with what would break if someone re-proposed it as a feature.

| killed hypothesis | falsified by | what breaks if ported into the clean product |
| --- | --- | --- |
| events → current aggregate → discard history is an adequate storage base | `evolution-record-progressive-envelope`: `NAIVE_SNAPSHOT_ONLY_BRANCH = FALSIFIED_FOR_DECISION-MATERIAL_HISTORY` | negative occurrences, provenance and settlement history become undecidable residue; later reconciliation is impossible |
| a compiled memory record can inline all of its source roots | `memory-metabolism` §0.1: `100,000 experiences -> one compiled heuristic -> 100,000 inline source roots` | compact memory regrows into the unbounded history burden it was built to remove |
| re-validation or restore may resurrect a superseded memory | `memory-metabolism` §0.2: `Revalidation does not resurrect a superseded memory.` | persistence would mint truth: a snapshot rollback could silently promote stale records to current |
| optimistic concurrency (versioned single write) proves the current executor | `execution-surface-fencing`: `SINGLE_VERSIONED_WRITE != CURRENT_EXECUTOR_WON`, `EXTERNAL_EXACTLY_ONCE = NOT_CLAIMED` | a stale executor can win while the artifact looks correct |
| a receiver's validation proves the source's obligations were intact | `migration-settlement-composition`: a receiver seeing only the projected packet *cannot* infer a completely omitted source obligation | omission passes import validation; needs source-side witness, not a stricter receiver |
| "retrieval was used" is sufficient closure evidence | `retrieval-obligation` 0.3 removed `RETRIEVAL_USED` as READY closure | a hit would masquerade as sufficiency |
| the triggering agent already knows which scope to search | `retrieval-obligation` 0.2 overturned 0.1's assumption | scope would be assumed rather than derived |
| per-rule isolation success implies composition success | `v2-machine-contract-hardening` v2.2 F3: a V2.1 protection leaked under cumulative composition | green in isolation is not green composed — the composition must be replayed cumulatively |

## 4. Retirement history — the answer to the open question

The contract-surface note asked for the **retirement rate** and suspected it was zero. The corpus
gives a sharper answer.

**True retirements in the measurable range: one.**

| retired | when | basis recorded | regression |
| --- | --- | --- | --- |
| adopter-facing `MAINLINE / NOT_MAINLINE` status axis | v0.3.5 (2026-08-23) | candidate-freeze record: "proposed retirement … while preserving historical Mainline occurrence records"; executed per `HISTORY.md`: "active … axis retired beginning with this release; historical uses remain unchanged" | none observed through v0.3.14 |

**Demotions, which are not retirements**: `ena_evolve_v1_2.py` → `tools/legacy/` with a named
replacement and byte-preserved evidence; `PROJECT-METADATA.yaml` → cold compatibility pointer; the
`commitment-settlement-recovered` prototype → `NOT_BUNDLED_RESEARCH_PROTOTYPE` with the reason
"bundling requires a current adoption need and evidence".

**Zero**: the validation-rule line V2 → V2.2 retired nothing; it *composed*. Additional zero-result
records exist in the corpus (`0 retired` in a v0.3.4 reconciliation summary; an audit stating "no
retirement claim is made"), and one lifecycle term (`RETIRED_REDUNDANT`) is defined but never used
anywhere.

**The most useful single finding**: `procedures/CONTROL-RETIREMENT.md` exists, and **not one
retirement cites it**. The behaviour happened; the documented procedure had zero field use. A
procedure that nobody invokes is itself an instance of the surface the budget is meant to price —
and a warning against answering "the retirement rate is low" with "write a retirement procedure".

**Consequence for the hypothesis**: the ratchet is **not refuted**. The rate is small and non-zero;
the validation-rule line's rate is zero.

## 5. Three pending proposals, disposed by evidence rather than by argument

| pending item | what the corpus shows | disposition |
| --- | --- | --- |
| anchor tri-state (newest anchor takes over / explicit supersede / no-target marking), deferred for "zero product-side failure evidence" | the one **real product-side occurrence** of that class is recorded — a sampling tool exposed its internally sampled anchor through the *same field* used for the explicitly chosen anchor — and the **clean product already carries the fix**: `dream_sample.py` splits `anchor_id` (problem-guided) from `sampled_anchor_id` (free), with two-sided assertions in `self_test.py` | DEFER stands, now on verified ground: the failure class is fixed in the new line, so the residual tri-state mechanism still has **no** product-side occurrence. The documentation-anchor half is covered by the clean product's CI guard. |
| archive coverage ("declared coverage = actual coverage" machine check), refused as costing a legitimate path | **no product-side record in either line**; the closest is a *host-local* snapshot job that silently degraded for nights on partial archives. The old theory itself classes this as external/Host evidence (`EXTERNAL_CONTROL_REQUIRED`), and the recovery mechanism **deliberately does not** compare declared against actual; the retrieval mechanism's selftest explicitly accepts false completeness as an *external residual* | refusal is **doubly supported**: no product-side evidence, and the theory line agrees the property is not the product's to enforce |
| multi-home documentation, "needs one real mistake to qualify" | **no record** of a real multi-home mistake in either line; the only related item is a *moved*-home fails-closed fix (no failure narrative, no consequence) | still unqualified |

Worth recording separately: the closest thing to a real recovery-surface failure — a cross-model
adopter finding that First Use could turn placeholders into machine-readable READY and destroy the
gap evidence — **was already fixed at the gate** (provenance hardening) before this audit. That is
precisely why nothing is mountable on the recovery surface today: the class was closed at the
decision boundary rather than by adding a reference mechanism.

## 6. Sleep/Dream: the corpus has no measured answer, and one tempting sample is a misplant

Searches for sleep, dream, consolidation, pruning, dormancy and decay across the memory-metabolism
line return contract prose and **zero numbers**. The old line's own final wording is
`MECHANISM_VERIFIED / MARGINAL_FIELD_VALUE_NOT_YET_PROVEN`, "Sleep/dreaming has not yet been
validated", and an explicit instruction not to run a separate sleep experiment in that campaign.

The one positive small sample that does exist — retrieval invocation lifting recall from 11.1% to
100% at a 50% call rate — belongs to the **retrieval** line, not to consolidation, and its own author
downgraded it to a proof of concept. **Citing it as Sleep/Dream evidence would be a cross-line
misplant**, which is exactly the kind of borrowed credibility this audit exists to prevent.

## 7. The one rule this audit changed

The budget's fourth item — *which legitimate positive cases does the addition cost* — is not
sufficient as written, and the corpus supplies the measured reason:

```text
v2.2 called its five sacrificed positives "the intended cost of ... not a contract bug".
v2.3 kept `kind: POSITIVE` on those five but re-authored their `expected_verdict` to BLOCK/UNKNOWN,
     and replaced the positive-preservation metric with per-category verdict correctness.
v2.4 reported all five as `preserved: True` - against the RE-AUTHORED expectation.
2026-09-14 reproduction: all five return OK once the artifacts their own references name are
     supplied; the contract never refused those cases.
CORRECTION: the earlier version of this block claimed "v2.4, an INDEPENDENT reproduction, classified
     THREE of those five as CONFIRMED_MATERIAL_DEFECT". That was false. The v2.4 reconciliation
     adjudicated its own independently authored corpus (I01-I16, O01-O04); no independent round ever
     examined P1/P5/P6/P7/P9. The claim misattributed one fixture set's findings to another.
```

Therefore the item-4 answer now carries an **independent-reproduction obligation**:

- the five sacrificed positives are identified concretely (three blocked on an unresolvable support
  reference, two held UNKNOWN for a missing registry) and reconcile exactly with `29/29 + 14/19`;
- **an author's cost claim is a hypothesis, not evidence.** The verifier must reproduce the claimed
  cost before it counts toward item 4 — otherwise the budget can be satisfied by a declaration, and a
  cost can be *encoded* as an expectation that later rounds then report as preservation;
- reproduction of this particular claim
  (`research/prototypes/v2-machine-contract-hardening/positive-recovery-audit/`) showed the cost was
  in the fixtures, not in the contract: five incomplete payloads failed closed, which is the
  documented intent. What remains unmeasured is whether an adopter can always supply the registries.

## 8. What this means for the clean product

Nothing to port; nothing to add. The corpus's value to the clean product is **negative space**: which
shapes have already failed, which controls were already retired and on what evidence, and which of
today's live proposals have no evidence behind them. That is the direction the budget fast-tracks —
removal and refusal — and the only direction that does not grow the surface.

## 9. Provenance

Four read-only digests over the theory repository at `main = 2f91bdf`, judged against the clean
product at `main = d4f3e68`. Records cited by path above; the falsified entries quote the corpus's own
words rather than paraphrase. Nothing in this repository or the product was modified by the audit.
