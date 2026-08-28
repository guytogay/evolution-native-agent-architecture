# Independent Validation Capsule Carrier

Status: `CANONICAL_FOCUSED_METHOD_COMPANION / VALIDATION_INTERFACE / NON_NORMATIVE_TO_CURRENT`

Purpose: provide a physically isolated carrier for fresh A-S when repository UI, candidate self-description, implementation commentary, or search/navigation surfaces can leak author-shaped priors.

This companion refines `INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md` after the candidate.2 natural-navigation incident. The information-boundary method decides **which information role belongs before/after A-S**; this method decides **how the carrier enforces that boundary**.

## 1. Carrier problem

A blind validation branch can still fail as an information boundary when the same repository exposes:

- automatic README rendering;
- repository-wide search;
- `.github/` author harnesses;
- `research/` handoffs/reconciliation;
- other branches/tags/releases;
- candidate-local mixed-role files containing repair/search-map commentary.

Therefore:

```text
PROCEDURAL_RANGED_READ != INFORMATION_BOUNDARY
PROCEDURAL_PATH_AVOIDANCE != INFORMATION_BOUNDARY
DECLARED_WITHHOLDING != PHYSICAL_WITHHOLDING
CLEAN_BRANCH != PHYSICALLY_ISOLATED_REVIEW_SURFACE
```

When normal navigation/search can reach withheld material, do not claim branch-level search-space blindness. Repair the carrier rather than asking the reviewer to exercise perfect self-denial.

## 2. A-S capsule

Build a deterministic archive containing only the A-S review surface.

The capsule should include behavior-bearing contract/schema/implementation/operational semantics while physically excluding:

- project-manager context;
- Current and historical release trees not needed for the target;
- author reconciliation/attack harnesses;
- predecessor findings;
- expected fixtures/oracles when history-bearing;
- candidate-local status/history surfaces whose primary information role is author confidence/repair narrative.

The capsule itself is validation-interface material, not a candidate identity.

```text
CAPSULE_PROJECTION != CANDIDATE_MUTATION
WITHHELD_FROM_A-S != REMOVED_FROM_RELEASE
```

## 3. Mixed-role executable files

Exact-byte retention is preferred when a file is blind-safe.

When an executable file mixes real implementation semantics with author search-map comments/docstrings or embedded selftest corpora, A-S may use a declared semantic-preserving projection if all of the following hold:

1. the exact frozen source and source range are bound;
2. executable AST equivalence is mechanically verified for the retained executable surface;
3. docstring/comment removal cannot alter behavior relied upon by the candidate;
4. any source truncation is explicitly declared and excludes only non-A-S test/oracle regions;
5. the projection is listed in the capsule manifest;
6. the exact original file remains available later in A-P.

This is an exception to byte-preserving branch projection, justified only when exact bytes are themselves a priming channel.

```text
SEMANTIC_PROJECTION MUST_NOT_BECOME UNDECLARED_REIMPLEMENTATION
```

## 4. Mixed-role prose/schema metadata

A-S may use narrowly declared projection where non-behavioral annotation embeds predecessor identity or author history, for example:

- exact source slices that remove a status/confidence header;
- removal of one explicitly bound author-history paragraph;
- annotation-only schema-title redaction where validation-bearing JSON is proven unchanged.

Do not silently rewrite substantive contract language.

## 5. Semantic vocabulary is not an author attack map

Blindness must not erase the object being tested.

A contract may legitimately contain terms such as false block, false confidence, refusal, failure, uncertainty, or overclaim. Those terms can be part of the semantics a fresh reviewer must inspect.

Author attack maps are different: predecessor defect identifiers, repair narratives, probe names, expected outcomes, PR/falsifier lineage, specific green-run claims, or other material that tells the reviewer where the author already searched.

```text
SEMANTIC_FAILURE_VOCABULARY != AUTHOR_ATTACK_MAP
```

A priming detector that removes ordinary semantic failure vocabulary can itself compress the independent attack space and create false confidence in the blindness mechanism.

## 6. A-P supplement

A-P receives the exact frozen candidate package, not the A-S projection.

It is physically delivered only after the A-S report is sealed.

A-P audits:

- self-description/status;
- full lineage;
- fixtures/selftests/regression oracles;
- package claims;
- historical narrative versus actual frozen bytes.

It must not rewrite the already sealed A-S attack tree.

A-P remains role/oracle independent, but is not claimed search-space blind after package history opens.

## 7. Content-hash seal when reviewer cannot write GitHub

Git commit is useful but not the only valid independent seal carrier.

For a physically isolated workflow, the reviewer may seal A-S by computing SHA-256 of the exact completed A-S report before any A-P material is opened.

Required sequence:

```text
A-S CAPSULE ONLY
-> COMPLETE REPORT
-> COMPUTE REPORT SHA-256
-> RECORD DIGEST
-> STOP
-> VERIFY/PRESERVE REPORT
-> DELIVER A-P SUPPLEMENT
```

The project manager later verifies the exact report bytes against that digest and persists the occurrence into canonical project history.

This is valid only if the A-P supplement was not available to the reviewer before the content seal.

## 8. Carrier integrity is layered

A deterministic capsule should expose distinct integrity layers:

1. exact frozen target source/subtree identity;
2. reproducible projection rules;
3. per-payload file SHA-256 inventory;
4. explicit transformation/exclusion manifest;
5. outer capsule SHA-256;
6. repeated build determinism where practical.

A manifest cannot truthfully contain a stable digest of its own final bytes. Recording the pre-final manifest digest inside the final manifest is false confidence, not self-verification.

```text
MANIFEST_SELF_HASH = EXCLUDED_BY_DEFINITION
PAYLOAD_FILE_HASHES = SHA256_VERIFIED
OUTER_CAPSULE_HASH = SHA256_VERIFIED
```

The outer capsule digest binds the final manifest bytes themselves.

## 9. Mechanical audit requirements

Before a carrier becomes the fresh-review entry surface, verify at minimum:

- frozen source commit and candidate subtree;
- all declared A-S exclusions are physically absent;
- no project/research/control-plane directories are packaged into A-S;
- declared executable projections satisfy their equivalence checks;
- history-specific priming sweep has no unexplained hits;
- semantic failure vocabulary is not removed merely because it resembles an attack term;
- A-P contains the exact frozen candidate package byte-for-byte;
- every listed non-self payload hash matches;
- repeated builds produce the same outer capsule hashes;
- Current and frozen candidate bytes remain unchanged.

Passing these checks proves represented carrier construction, not candidate correctness or attack-space completeness.

```text
CARRIER_AUDIT_PASS != CANDIDATE_PASS
ATTACK_CARDINALITY = OPEN
```

## 10. Fresh-review intake

Do not use a same-repository GitHub issue as the mandatory A-S entrypoint when that UI itself can navigate to withheld material.

Preferred A-S delivery:

```text
MINIMAL PROMPT
+
ONE A-S CAPSULE FILE
+
EXPECTED CAPSULE SHA-256
```

Before A-S seal, do not additionally provide the project repository URL, project issue/branch, project-manager handoff, or A-P supplement when those surfaces reopen withheld context.

Do not provide the A-P supplement in the same message, attachment set, archive, shared folder, or directly accessible surface before A-S seal.

The same fresh reviewer may continue into A-P after the project manager verifies/records the A-S content seal and separately delivers the A-P supplement.

## 11. Failure rule

If the reviewer discovers that withheld author/history/oracle material was available or exposed before A-S seal:

```text
STOP
-> REPORT VALIDATION-INTERFACE DEFECT
-> DO NOT CLAIM A-S FRESHNESS
-> DO NOT START A-P
```

Repair the carrier, not the reviewer instruction.

## 12. Current candidate.2 carrier evidence

Frozen target:

- source `bda470e0a6b170cec61225a905957a501454a2fe`
- subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

Authoritative final build/audit workflow:

- `.github/workflows/v037-candidate2-r3-capsule-build.yml`
- run `33131773164` — SUCCESS

Observed final checks:

- A-S physical isolation: PASS
- A-S payload inventory: PASS
- A-P exact frozen candidate package: PASS
- A-P payload inventory: PASS
- manifest self-hash policy: `EXCLUDED_BY_DEFINITION`
- deterministic repeated build: PASS
- attack cardinality: OPEN

Final deterministic inner hashes:

- A-S capsule `dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`
- A-P supplement `427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649`

The earlier run `33131665994` and hashes `ee80ac...` / `b3e222...` are superseded carrier-build evidence because final self-audit corrected the manifest inventory representation. They must not be used as fresh-review carrier identity.

Incident:
`research/methodology/incidents/2026-08-28-CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md`

Reconciliation:
`collaboration/reconciliation/2026-08-28-v037-candidate2-isolated-capsule-intake-reconciliation.md`

No candidate.2 or Current bytes were changed by this validation-interface repair.
