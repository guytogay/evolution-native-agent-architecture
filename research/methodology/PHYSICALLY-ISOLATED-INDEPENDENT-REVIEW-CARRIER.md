# Physically Isolated Independent Review Carrier

Status: `CANONICAL_FOCUSED_METHOD_CANDIDATE / VALIDATION_INTERFACE / OPEN_CARDINALITY / NON_NORMATIVE_TO_CURRENT`

Purpose: preserve fresh A-S search-space independence when the project repository, candidate package, or review UI can expose author-shaped history even if the reviewer follows the declared path.

This file complements `INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`. That method decides **what information role belongs before or after A-S**. This method decides **how the carrier enforces that boundary**.

## 1. Procedural restraint is not a strong information boundary

The candidate.2 Issue #137 occurrence demonstrated that a reviewer can obey the written instructions and still cross the boundary because GitHub automatically renders or cross-navigates content.

```text
PROCEDURAL_RANGED_READ != INFORMATION_BOUNDARY
PROCEDURAL_PATH_AVOIDANCE != INFORMATION_BOUNDARY
DECLARED_WITHHOLDING != PHYSICAL_WITHHOLDING
```

A branch inside the same repository can also expose `.github/`, `research/`, old reconciliation, other branches, repository search results, and candidate-local history through ordinary navigation.

Therefore a same-repository blind branch is only sufficient when the actual UI/search/navigation surface has been shown not to reveal withheld material.

## 2. Prefer physical absence over reviewer self-denial

When natural navigation can cross the boundary, build a carrier in which pre-A-S withheld material is absent.

```text
FROZEN_TARGET
-> REPRODUCIBLE_ROLE_PROJECTION
-> PHYSICALLY_ISOLATED_A-S_CARRIER
```

The carrier is a validation interface, not a successor candidate.

It may contain declared derived projections where exact frozen files are mixed-role and cannot be exposed without leaking author history. Such projections require mechanical equivalence evidence appropriate to the transformation.

Examples:

- exact line slice for a semantic file with a history/status header;
- annotation-only redaction where validation-bearing JSON is unchanged;
- executable Python AST equivalence after comments/docstrings are removed;
- whole-file withholding when the file's primary information role is history/oracle/status rather than independent semantic inspection.

```text
PROJECTION_FOR_INFORMATION_ROLE != CANDIDATE_MUTATION
WITHHELD_FROM_A-S != REMOVED_FROM_RELEASE
```

## 3. Separate semantic vocabulary from author attack maps

Blindness must not erase the object being tested.

A contract may legitimately contain terms such as false block, false confidence, refusal, failure, or uncertainty. These are semantic vocabulary.

Author attack maps are different: predecessor defect identifiers, repair narratives, probe names, expected outcomes, PR/falsifier lineage, specific green-run claims, or other material that tells the reviewer where the author already searched.

```text
SEMANTIC_FAILURE_VOCABULARY != AUTHOR_ATTACK_MAP
```

A priming detector that removes ordinary semantic failure vocabulary can itself compress the independent attack space and create a false sense of blindness.

## 4. A-S and A-P use different physical carriers when needed

For a self-describing candidate, a robust sequence is:

```text
A-S CARRIER
  behavior-bearing semantic/implementation surface
  project-manager context absent
  author oracle/history absent

-> A-S REPORT
-> A-S CONTENT SEAL

A-P SUPPLEMENT
  exact frozen candidate package
  no external project-manager repair map required

-> A-P REPORT
-> STOP BEFORE PHASE B
```

A-P may open the exact frozen package after A-S is sealed. A-P is role/oracle independent but is not claimed to remain search-space blind after history becomes visible.

Do not hand the A-P supplement to the fresh reviewer before the A-S seal merely because the reviewer promises not to open it.

## 5. The A-S seal may be a commit or a content digest

An immutable Git commit is a useful seal when the fresh environment has an authenticated write channel.

When it does not, a cryptographic content digest is sufficient to freeze the A-S occurrence **if and only if** it is computed and recorded before A-P material is supplied.

```text
A-S_REPORT_BYTES
-> SHA-256
-> RECORDED_SEAL
-> ONLY_THEN_SUPPLY_A-P
```

Later project-manager persistence must verify the exact report bytes against the recorded digest before Phase B.

This is not weaker merely because GitHub was unavailable; the evidence property is immutability of the observed A-S bytes across the information-boundary transition.

## 6. Carrier integrity is layered

A deterministic capsule should expose distinct integrity layers:

1. exact frozen target source/subtree identity;
2. reproducible projection rules;
3. per-payload file SHA-256 inventory;
4. explicit transformation/exclusion manifest;
5. outer capsule SHA-256;
6. repeated build determinism where practical.

A manifest must not pretend to contain a stable hash of its own final bytes.

```text
MANIFEST_SELF_HASH = EXCLUDED_BY_DEFINITION
PAYLOAD_FILE_HASHES = VERIFIED
OUTER_CAPSULE_HASH = VERIFIED
```

Self-reference cannot be made trustworthy by writing the pre-final manifest hash into the final manifest.

## 7. Mechanical audit requirements

Before a carrier becomes the fresh-review entry surface, verify at minimum:

- exact frozen source/subtree binding;
- all declared A-S exclusions are physically absent;
- no project-manager/research/control-plane directories are packaged into A-S;
- derived executable projections satisfy their declared equivalence check;
- history-specific priming sweep has no unexplained hits;
- semantic failure vocabulary is not removed merely because it resembles an attack word;
- A-P contains the exact frozen candidate package byte-for-byte;
- every listed payload hash matches;
- repeated builds produce the same outer capsule hashes;
- Current and frozen candidate bytes remain unchanged.

Passing these checks proves the **represented carrier construction**, not that the A-S attack space is complete.

```text
CARRIER_AUDIT_PASS != CANDIDATE_PASS
ATTACK_CARDINALITY = OPEN
```

## 8. Fresh-review operational discipline

A genuinely fresh reviewer should receive only the A-S carrier and minimal instruction needed to open its intake document.

Before A-S seal, do not additionally provide:

- project repository URL when repository browsing would re-open withheld context;
- project issue or validation branch as the review surface;
- A-P supplement;
- project-manager handoff;
- repair/reconciliation summaries;
- predecessor review findings.

After the reviewer returns the A-S report and recorded digest, the same reviewer state may receive the A-P supplement and continue to package audit.

The reviewer must stop before project-manager Phase B.

## 9. Trigger occurrence and candidate.2 implementation

Trigger occurrence:

`research/methodology/incidents/2026-08-28-CANDIDATE2-BLIND-CARRIER-LEAK-INCIDENT.md`

Candidate.2 r3 reconciliation:

`collaboration/reconciliation/2026-08-28-v037-candidate2-isolated-review-capsule-r3.md`

The candidate.2 carrier construction is reproducible from frozen source:

- source: `bda470e0a6b170cec61225a905957a501454a2fe`
- candidate subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- audit run: `33131773164`
- final A-S ZIP SHA-256: `dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`
- final A-P ZIP SHA-256: `427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649`

No candidate or Current bytes were changed by this method repair.
