# Memory Metabolism iteration 0.4 — reconciliation after fresh independent review

Status: `RESEARCH_PROTOTYPE / DRAFT / NOT_CURRENT_BASELINE / NOT_RELEASE_CANDIDATE`

Reviewed predecessor:
- branch: `research/memory-metabolism-prototype`
- reviewed commit: `a9d7f4c7b9f2de285f7f938250be66090a92a3f0`
- independent verdict: `NEEDS_REVISION_BEFORE_FURTHER_REVIEW`

Iteration 0.4 preserves the reviewed 0.3 artifacts unchanged and adds a new versioned iteration so the failure evidence is not erased by repair.

## Reconciliation rule

Do not convert reviewer findings into new ENA Constitution rules merely because they are real bugs in the prototype.

The independent review itself concluded that Current v0.3.6 already carries the relevant higher-level semantics; the new findings are mostly places where this reference contract encoded those semantics incorrectly or too narrowly.

## Findings accepted as prototype changes

### F1 — current use / historical use overlap

0.3 allowed one superseded record to appear in both `used_record_ids` and `historical_use_record_ids`, defeating the intended `Revalidation != resurrection` property.

0.4:
- requires the two sets to be disjoint;
- rejects any superseded record in current `used_record_ids`;
- preserves legitimate superseded historical use.

### F2 — silent access-scope relaxation through derivation

The review showed a public compiled record could derive from restricted evidence while only the public record's scope was checked.

A naive fix ("secret scope contaminates all descendants forever") would false-block legitimate sanitization, anonymization, aggregation, or authorized declassification.

0.4 therefore standardizes the property rather than one information-flow organ:

> **Derived memory may not silently relax represented source access scope.**

Default:
- derived cognitive records inherit the union of represented source access requirements.

Escape path:
- scope may be deliberately relaxed only through an explicit `access_scope_reconciliation`;
- reconciliation must state `EXPLICIT_DECLASSIFICATION` or `SANITIZED_DERIVATION`;
- its basis must be external to memory records.

A PASS still does not authenticate that external basis.

### F3 — historical context bypassed access control

Historical context is still a read.

0.4:
- applies retrieval and access-scope checks to both current-use and historical-use records;
- does not treat superseded historical use as current state.

### F5 — contradiction visibility only applied to COMPILED

0.3 let KNOWLEDGE derived from explicitly contradictory sources bypass conflict handling.

0.4 applies direct explicit-contradiction visibility to derived cognitive layers:
- `KNOWLEDGE`
- `COMPILED`
- `IDENTITY`

This still does not claim semantic contradiction detection.

### FB-1 — higher-order compiled learning was false-blocked

0.3 required a decision-material compiled record to directly cite EVIDENCE/ARCHIVE.

That makes hierarchical compilation progressively expensive and works against bounded active memory.

0.4:
- permits transitive finite lineage;
- a decision-material compiled record must be able to reach EVIDENCE/ARCHIVE through represented derivation/evidence links;
- it need not re-inline or re-cite raw evidence at every compilation generation.

## Known target also sharpened: lawful redaction / tombstones

The independent reviewer pinned a concrete path where a tombstone or lawfully redacted record could satisfy the decision-material evidence anchor while the compiled record still appeared fully challengeable.

0.4 introduces an explicit `challengeability` classification for decision-material compiled memory:

`FULL | DEGRADED | UNAVAILABLE | UNKNOWN`

The validator rejects `FULL` when no reachable evidence/archive record remains `PRESENT`.

This preserves a durable learned lesson after lawful evidence loss without pretending its future challenge path is unchanged.

## Findings deliberately NOT "solved"

### Real source independence

Distinct represented source roots are still not external proof of independence.

This remains a claim-boundary / Host-evidence problem, not something a JSON validator can manufacture.

### External authority validity

A string naming an external mandate is still not authenticated by schema acceptance.

The prototype only prevents a memory record from serving as executable authority.

### Unknown-known / truthful omission

The memory-set validator still cannot prove that all decision-material memory that should have been retrieved actually entered a projection.

That belongs to the retrieval reflex / meta-memory problem.

### Entity-level contradictory current facts

Without an entity ontology, the validator cannot know that two unlabeled current-state records refer to the same real-world property.

Do not add a universal entity ontology merely to make this validator omniscient.

### Cross-Host/model/environment applicability

Current ENA already separates transfer from local selection. Iteration 0.4 does not duplicate a universal applicability model into every memory record.

## Evidence added

`review1_regression.py` preserves the first review's strongest concrete traces as regression fixtures:

- F1 used+historical supersession bypass -> now rejected;
- F2 silent restricted-to-public derivation -> now rejected;
- F2 explicit sanitized derivation -> representable;
- F3 historical access bypass -> now rejected;
- F5 KNOWLEDGE contradiction bypass -> now rejected;
- FB-1 second-order compilation -> now accepted;
- F6 redacted evidence + FULL challengeability -> now rejected;
- F6 degraded challengeability -> representable.

The iteration-0.4 validator also contains its own deterministic selftests.

## Epistemic boundary

A 0.4 PASS means only:

> the represented Memory Metabolism structure satisfies this research iteration's internal contract.

It does **not** prove:
- truth;
- source authenticity;
- real independence;
- semantic quality of a learned heuristic;
- confidentiality of arbitrary natural-language transformations;
- validity of external authority/declassification;
- retrieval completeness;
- future salience;
- behavioral improvement;
- Host portability.

## Next question

After regression closure, the next valuable review is not another generic architecture vote.

The most differentiated reviewer would be an **information-flow / access-control security reviewer** focused on whether the 0.4 access-scope reconciliation property is:
- too weak (still leaks through derivation);
- too strong (blocks legitimate information release);
- incorrectly modeled as access control when the actual property is information-flow/declassification provenance.

Only after that should a Host integration experiment be considered.
