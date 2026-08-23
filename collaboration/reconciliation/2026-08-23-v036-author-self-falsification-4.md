# ENA v0.3.6 author self-falsification — pass 4 / pre-freeze attack disposition

Status: `AUTHOR_SELF_FALSIFICATION / PRE_FREEZE / NOT_INDEPENDENT_VALIDATION`

This pass reconciles all 24 attack classes from `collaboration/inbox/2026-08-23-v036-author-falsification-plan.md` against the current working candidate.

Disposition vocabulary:

- `MACHINE_CLOSED` — represented false claim is rejected by schema/validator/selftest in the tested surface;
- `SEMANTICALLY_GUARDED` — candidate semantics explicitly reject the false claim, but no claim is made that one universal runtime mechanism enforces it;
- `VISIBLE_RESIDUAL` — known gap remains explicit and is not silently promoted to success;
- `OPEN_RESEARCH` — deliberately not standardized in this candidate.

## A. Mutation pressure / latent variation

| Attack | Disposition | Current evidence / boundary |
| --- | --- | --- |
| 1. stimulus auto-mutates production and calls it improvement | `SEMANTICALLY_GUARDED` | `09` states `stimulus != mutation`, `mutation != improvement`; inherited tool has no mutation-pressure auto-execution path. |
| 2. long-lived latent/unassessed candidate is blocked for lacking immediate verdict | `MACHINE_CLOSED` | v2 template permits `PROPOSED + LATENT + UNASSESSED`, `variation_space: null`, no experiment/evaluation. |
| 3. latent candidate is deleted merely because age/usage is low | `SEMANTICALLY_GUARDED` | `09` and `06` state age/usage are evidence, not proof of worthlessness; curation remains cost/context dependent. |
| 4. stored variation is narrated as applied/successful | `MACHINE_CLOSED` for represented expression/selection; broader application remains semantic | independent expression/selection axes; `stored != expressed != applied != selected`. |

## B. Expression / salience

| Attack | Disposition | Current evidence / boundary |
| --- | --- | --- |
| 5. mark `EXPRESSED` with no represented cue/context/event | `MACHINE_CLOSED` | v2 schema requires expression history for `EXPRESSED`; validator requires latest-state consistency and a non-empty represented trigger. |
| 6. configured cue file is narrated as fresh-session salience/application proof | `SEMANTICALLY_GUARDED` | Runtime Kernel and `09` preserve `WRITTEN != LOADED != INTERPRETED != SALIENT != APPLIED`; fresh-session field evidence remains required. |
| 7. dormant capability expression silently revives stale external authority | `SEMANTICALLY_GUARDED` | expression does not mint authority; inherited authority/restore semantics remain binding. |
| 8. hot cues expand into a permanent prompt encyclopedia | `SEMANTICALLY_GUARDED / FIELD_RESIDUAL` | hot-cues/cold-capability direction explicitly rejects encyclopedic hot context; false-positive/false-negative salience remains field research. |

## C. Local selection / fitness

| Attack | Disposition | Current evidence / boundary |
| --- | --- | --- |
| 9. one Host/model/user success exported as universally good | `SEMANTICALLY_GUARDED` | `local selection != universal fitness`; environment-scoped selection preserved. |
| 10. many imports/popularity become receiver proof | `SEMANTICALLY_GUARDED` | `POPULAR != UNIVERSALLY_VALID`; import/propagation do not create local selection. |
| 11. harmful strategy assumed inevitably eliminated or moral convergence narrated | `SEMANTICALLY_GUARDED` | `09` states `survival != moral correctness` and explicitly rejects automatic moral convergence. |

## D. Evolution Commons

| Attack | Disposition | Current evidence / boundary |
| --- | --- | --- |
| 12. publisher packet forces receiver adoption | `SEMANTICALLY_GUARDED` | `PUBLISH -> DISCOVER -> IMPORT -> EXPRESS/EXPERIMENT -> LOCALLY_SELECT`; no arrow automatic. |
| 13. popularity/ranking becomes mandatory adoption authority | `SEMANTICALLY_GUARDED` | Commons rejects mandatory-update service and universal ranking authority. |
| 14. receiver non-adoption or publisher preference becomes illegitimate veto over the other | `SEMANTICALLY_GUARDED` | autonomy is bounded by actual publication/receiver authority and Protected-Subject/external constraints; non-adoption alone is not publication veto. |
| 15. central `BEST` ranking becomes universal fitness oracle | `SEMANTICALLY_GUARDED` | centralized BEST ranking not required; no one metric becomes universal fitness by default. |

## E. Recovery / rescue

| Attack | Disposition | Current evidence / boundary |
| --- | --- | --- |
| 16. mutation disables its own rollback path yet recovery is claimed viable | `SEMANTICALLY_GUARDED / IMPLEMENTATION_DEPENDENT` | rescue-plane property requires an outside-damaged-surface path where material/controllable; no universal Host organ is claimed. |
| 17. narrow rescue credential becomes approval/sovereign authority | `SEMANTICALLY_GUARDED` | rescue authority explicitly does not imply approval/forbid authority over future variations. |
| 18. internal state restore is narrated as external consequence reversal | `SEMANTICALLY_GUARDED` | `state rollback != external consequence rollback`; recovery is not time reversal. |

## F. Canonical ENA evolution

| Attack | Disposition | Current evidence / boundary |
| --- | --- | --- |
| 19. local fork self-labels `CURRENT` and becomes canonical | `SEMANTICALLY_GUARDED` | candidate/fork cannot self-promote; canonical admission requires governed lineage + explicit promotion event. |
| 20. GitHub availability becomes metaphysical ENA validity | `SEMANTICALLY_GUARDED` | GitHub is current carrier; governed reproducible lineage is the semantic requirement. |
| 21. future carrier migration drops review/freeze/history evidence but claims seamless continuity | `SEMANTICALLY_GUARDED` | carrier migration must preserve sufficient lineage/evidence or it is a silent fork, not canonical continuity. |

## G. Ecological minimal intervention

| Attack | Disposition | Current evidence / boundary |
| --- | --- | --- |
| 22. minimal intervention is used to ignore unowned externality/stale authority | `SEMANTICALLY_GUARDED` | `09` explicitly rejects this; governance floor retains owned consequence, scoped authority and recovery/correction. |
| 23. a new administrator/role is created for every ecological interaction | `SEMANTICALLY_GUARDED` | candidate says govern the floor, not every interaction; `06` says Commons is not sovereign; no new mandatory role added. |
| 24. fixed cognitive-mode taxonomy promoted because EXPLORE was useful | `OPEN_RESEARCH / NOT_STANDARDIZED` | `09` permits exploratory cognitive modes as one mutation-pressure mechanism but explicitly refuses a fixed universal taxonomy. |

## Machine execution evidence obtained in this pass

The exact current candidate copies of:

- `tools/validate_evolution_record_v2.py`;
- `schemas/evolution-record.v2.schema.json`;
- `templates/evolution-record.v2.json`

were retrieved from the candidate branch and executed together in an isolated local environment. Result:

`EVOLUTION_RECORD_V2_SELFTEST_PASS 10`

This proves the ten represented v2 consistency probes executed successfully in that environment. It does **not** prove external-world expression, evidence truth, salience, authority, recovery, universal fitness, or independent validation.

## Additional identity findings from full PR sweep

### D1 — active capability/contract files retained predecessor candidate wording

Severity: `MATERIAL_IDENTITY_LEAKAGE`

`04-CAPABILITY-MAP.md` still described CAP-072..080 as `v0.3.5 candidate additions`; `05-CORE-OPERATIONAL-CONTRACTS.md` described itself as the active v0.3.5 candidate contract surface and bounded its validator claim against the wrong candidate identity.

Correction:

- rebind active-file wording to v0.3.6 candidate;
- preserve v0.3.5/v0.3.3 labels only where they describe inherited implementation/history;
- add active-file identity checks to `tools/validate_candidate.py` so this class becomes a regression condition.

### D2 — GitHub Actions execution observability remains unresolved

Severity: `VISIBLE_INFRASTRUCTURE_RESIDUAL`

The candidate workflow exists with push/pull-request triggers, but the available connector returned no workflow runs/statuses for either candidate head SHA or PR merge SHA. A direct container clone was also blocked by DNS/network isolation.

Therefore no `CI PASS` or `CI FAIL` claim is made here.

This does not invalidate the separately executed v2 selftest; it means the full repository pre-freeze workflow has not yet been evidenced through the available observation path.

### D3 — expression runtime integration into `ena_evolve.py` intentionally deferred

Severity: `VISIBLE_IMPLEMENTATION_RESIDUAL / DECISION_FOR_INDEPENDENT_FALSIFICATION`

The inherited `ena_evolve.py` remains the v0.3.5 state/evidence implementation and does not implement mutation-pressure, latent-reservoir, or expression commands.

Author decision before freeze:

- do **not** modify the mature inherited tool merely for feature symmetry;
- v2 schema + consistency validator already close represented expression/selection false-claim cases currently identified;
- retain the missing runtime integration as explicit residual;
- ask the independent falsifier whether absence of operational expression commands creates a material false-confidence, usability, or semantic-composition failure that should block release.

`schema/validator support != full runtime implementation`

## Author pre-freeze disposition

No author finding currently justifies:

- a new Constitution ID;
- a universal fitness function;
- a central Commons ranking authority;
- a mandatory rescue sovereign;
- a fixed cognitive-mode taxonomy;
- forced mutation or forced disposition of latent variation.

The candidate is closer to freeze, but **not frozen by this document**. Remaining freeze work is primarily identity/lineage finalization, full-repository validation evidence if obtainable, immutable candidate identity creation, and independent falsification handoff.

> **Variation does not owe reality an immediate verdict.**
>
> **Claims still owe evidence and scope.**
