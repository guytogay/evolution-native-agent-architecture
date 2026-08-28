# Independent Validation Isolated Carrier

Status: `CANONICAL_FOCUSED_METHOD_COMPANION / VALIDATION_INTERFACE / NON_NORMATIVE_TO_CURRENT`

Compatibility note: this file retains its historical `...CAPSULE-CARRIER.md` path so existing project pointers do not churn. **A ZIP/capsule is only one implementation HOW.** The governing concept is a physically isolated review carrier.

Purpose: preserve fresh A-S search-space independence when the source project, candidate package, repository UI, implementation commentary, or navigation/search surfaces can expose author-shaped priors.

This companion refines `INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`. That method decides **which information roles belong before and after A-S**. This method decides **how the review environment enforces the boundary**.

## 1. Govern the environment, not reviewer self-denial

The candidate.2 Issue #137 occurrence showed that a reviewer can obey written instructions and still cross the information boundary because normal GitHub navigation automatically exposes material.

```text
PROCEDURAL_RANGED_READ != INFORMATION_BOUNDARY
PROCEDURAL_PATH_AVOIDANCE != INFORMATION_BOUNDARY
DECLARED_WITHHOLDING != PHYSICAL_WITHHOLDING
CLEAN_BRANCH != PHYSICALLY_ISOLATED_REVIEW_SURFACE
```

When ordinary browsing/search can reach withheld author/history/oracle material, repair the carrier instead of adding more instructions telling the reviewer what not to click.

## 2. The invariant is physical isolation, not archive format

The required property is:

```text
A-S SEAL NOT YET CREATED
-> REVIEWER CAN REACH A-S MATERIAL
-> REVIEWER CANNOT REACH WITHHELD A-P / AUTHOR-HISTORY MATERIAL THROUGH THE REVIEW SURFACE
```

Possible HOWs include:

- a dedicated clean-room repository;
- an isolated directory or sandbox filesystem;
- a deterministic ZIP/archive;
- an isolated artifact or file set;
- another carrier that demonstrably enforces the same information boundary.

Therefore:

```text
PHYSICALLY_ISOLATED_CARRIER != ZIP
TRANSPORT_FORMAT != METHOD
```

Do not converge on one carrier technology unless behavioral equivalence has been established and the chosen HOW still pays epistemic/operational rent.

## 3. Reusable clean-room repositories

A dedicated repository may be reused across validation occurrences when its identity is treated as infrastructure and its **contents are disposable stage state**.

```text
CLEAN_ROOM_REPOSITORY_IDENTITY = REUSABLE_VALIDATION_INFRASTRUCTURE
CLEAN_ROOM_CONTENT = CURRENT_STAGE_EPHEMERAL_REVIEW_SURFACE
```

Recommended lifecycle:

```text
SOURCE PROJECT
-> BUILD / PROJECT AUTHORIZED REVIEW SURFACE
-> RESET CLEAN ROOM TO A SINGLE STAGE-SCOPED STATE
-> FRESH REVIEW
-> SEAL RESULT
-> PERSIST OCCURRENCE TRUTH BACK TO SOURCE PROJECT
-> RESET / REPLACE CLEAN ROOM FOR THE NEXT OCCURRENCE
```

Historical project context should not accumulate in the clean room by default. Long-lived history belongs in the source project's reconciliation/handoff/evidence surfaces.

When practical, reset the clean-room default branch to a parentless commit for each fresh occurrence so ordinary branch history does not expose the bootstrap/import process or previous projects.

## 4. What belongs in A-S

A-S should contain behavior-bearing contract/schema/implementation/operational semantics needed for independent falsification while physically excluding information whose primary role is author history, search map, confidence, expected oracle, or project-manager continuity.

Blindness must not erase the object being tested.

```text
SEMANTIC_FAILURE_VOCABULARY != AUTHOR_ATTACK_MAP
```

Terms such as false block, false confidence, refusal, failure, uncertainty, and overclaim may be legitimate candidate semantics. Predecessor defect IDs, repair narratives, expected outcomes, PR/falsifier lineage, author green-run claims, and prior findings are different information roles.

## 5. Mixed-role files may use declared projections

Exact bytes are preferred when blind-safe. If a file mixes real semantics with author-shaped priors, the A-S carrier may contain a declared semantic-preserving projection when mechanically justified.

Examples:

- exact source slice that removes a status/confidence header;
- one precisely bound author-history paragraph removal;
- annotation-only schema-title redaction where validation-bearing JSON remains identical;
- Python executable-AST-equivalent projection with comments/docstrings removed;
- whole-file withholding when the file is primarily history/oracle/status material.

```text
CARRIER_PROJECTION != CANDIDATE_MUTATION
WITHHELD_FROM_A-S != REMOVED_FROM_RELEASE
SEMANTIC_PROJECTION MUST_NOT_BECOME UNDECLARED_REIMPLEMENTATION
```

The exact frozen package remains available later for A-P.

## 6. A-S -> seal -> A-P is the real stage boundary

For a self-describing candidate:

```text
A-S CARRIER ONLY
-> INDEPENDENT A-S REPORT
-> CONTENT SEAL
-> ONLY THEN MAKE A-P MATERIAL REACHABLE
-> SAME REVIEWER PERFORMS A-P
-> STOP BEFORE PROJECT-MANAGER PHASE B
```

The A-P material may be introduced by replacing the clean-room state, adding a separately controlled stage after seal, or delivering a separate artifact. The HOW is secondary; **A-P must not be reachable through the A-S review surface before seal**.

A-P opens the exact frozen candidate package and audits self-description, lineage, fixtures, selftests/regression oracles, packaging claims, and package/history consistency. A-P remains role/oracle independent but is not claimed search-space blind after those materials open.

## 7. A-S content seal

A Git commit can be a seal when the reviewer has an authenticated write channel. When it does not, SHA-256 of the exact completed report bytes is sufficient when the digest is recorded **outside the bytes being hashed** before A-P becomes reachable.

```text
A-S_REPORT_BYTES
-> SHA-256
-> RECORDED SEAL
-> ONLY THEN OPEN A-P
```

The project manager later verifies the report bytes against the recorded digest and persists the occurrence into the source project's canonical history.

The seal requirement itself must be satisfiable. Do not require an exact report digest to be embedded inside the same exact bytes it hashes unless an explicit deterministic normalization/exclusion rule is defined. Default to an external sidecar, seal record, or signed envelope.

```text
EXACT_REPORT_SELF_HASH_WITHOUT_NORMALIZATION = SELF_REFERENTIAL
EXACT_REPORT_HASH -> EXTERNAL_DIGEST_BY_DEFAULT
```

Incident: `research/methodology/incidents/2026-08-28-INDEPENDENT-REPORT-SELF-HASH-RECURSION-INCIDENT.md`.

## 8. Carrier integrity

Mechanical evidence should match the chosen HOW rather than forcing every carrier to imitate ZIP semantics.

For any carrier, verify as applicable:

1. exact frozen target identity;
2. explicit inclusion/exclusion/transformation rules;
3. physical absence of withheld project/history/oracle surfaces during A-S;
4. mechanical equivalence evidence for derived executable or semantic projections;
5. stable identity of the actual A-S surface delivered to the reviewer;
6. A-P exact frozen candidate package when A-P opens;
7. Current and frozen candidate bytes unchanged by validation-interface work.

Additional integrity mechanisms may include per-file SHA-256 inventories, Git tree/commit identity, outer archive digest, or deterministic rebuilds.

```text
CARRIER_AUDIT_PASS != CANDIDATE_PASS
ATTACK_CARDINALITY = OPEN
```

## 9. Fresh-review intake

A genuinely fresh reviewer should receive the smallest routing information necessary to enter the isolated A-S carrier.

For a dedicated clean-room repository, a suitable intake is simply:

```text
CLEAN_ROOM URL / PINNED COMMIT
+
INSTRUCTION TO START AT THE ROOT INTAKE
```

Do not additionally provide the source project URL, project-manager handoff, predecessor findings, repair summaries, or separately reachable A-P material before A-S seal.

The clean room itself should be safe for ordinary browsing, repository search, README rendering, and execution. If normal use can escape into withheld material, the interface is not actually clean.

## 10. Failure rule

If withheld author/history/oracle material is available or exposed through the review surface before A-S seal:

```text
STOP
-> REPORT VALIDATION-INTERFACE DEFECT
-> DO NOT CLAIM A-S FRESHNESS
-> DO NOT START A-P
```

Repair the carrier, not the reviewer instruction.

## 11. Candidate.2 occurrence

Frozen target remains:

- source `bda470e0a6b170cec61225a905957a501454a2fe`
- candidate subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- Current subtree at that source `7dcbb3934883ffa6cc5292a662588cafc1533cff`

Issue #137's same-repository branch intake was aborted before A-S seal after normal GitHub navigation exposed withheld content. It remains validation-interface occurrence truth, not a candidate verdict.

The deterministic r3 capsule build remains useful **construction and integrity evidence**:

- workflow run `33131773164` — SUCCESS
- A-S package SHA-256 `dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`
- A-P package SHA-256 `427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649`
- manifest self-hash policy `EXCLUDED_BY_DEFINITION`
- deterministic rebuild PASS

The active A-S review HOW is now the reusable dedicated clean-room repository:

- repository `guytogay/independent-validation-cleanroom`
- A-S stage commit `28dde50c9caaeee3b5c269e28a7be5f07ac29ae5`
- A-S stage tree `42debebed620bd05e6e2635409057f20b57bfa9e`
- commit parents `[]`
- root contains only `README.md`, `INTAKE-A-S.md`, `MANIFEST-A-S.json`, and the projected `releases/` review surface
- `.github/`, `research/`, `collaboration/`, `releases/current/`, source-project history, and A-P material are absent from the current clean-room state

The clean-room A-S surface was reconstructed from the final audited r3 A-S package before the bootstrap/import history was removed by resetting `main` to the parentless A-S commit.

The ZIP is therefore no longer the reviewer-facing requirement. It is one validated construction HOW and occurrence-evidence source.

Incident:
`research/methodology/incidents/2026-08-28-CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md`

Clean-room transition reconciliation:
`collaboration/reconciliation/2026-08-28-v037-candidate2-cleanroom-carrier-transition.md`

No candidate.2 or Current bytes were changed by this validation-interface transition.