#!/usr/bin/env python3
from pathlib import Path
import re
import yaml

ROOT = Path('releases/current')
CANDIDATE = ROOT / 'CANDIDATE-BASELINE.yaml'
CURRENT = ROOT / 'CURRENT-BASELINE.yaml'
FROZEN_SOURCE = 'b7e88d7adb70396bd671ca97066daf2c120e0adc'
FROZEN_TREE = 'e3a9a20d16cecd78df7f32f19fca56e21159e810'
PREDECESSOR_CURRENT_TREE = '7dcbb3934883ffa6cc5292a662588cafc1533cff'

if not CANDIDATE.is_file():
    raise SystemExit('expected transplanted CANDIDATE-BASELINE.yaml')
if CURRENT.exists():
    raise SystemExit('CURRENT-BASELINE.yaml already exists; stage1 is one-time')

cand = yaml.safe_load(CANDIDATE.read_text(encoding='utf-8'))

# Build a release-facing machine pointer from validated candidate metadata without
# pretending candidate self-description itself was the freeze/release authority.
current = {
    'schema_version': '3.1',
    'ena_version': 'v0.3.7',
    'adoption_status': 'CURRENT',
    'maturity': 'FIELD_VALIDATION',
    'current': True,
    'complete_adoption_baseline': True,
    'requires_older_release_composition': False,
    'active_mainline_axis': False,
    'version_identity_includes_maturity_status': False,
    'package_scope': 'ALL_FILES_UNDER_RELEASES_CURRENT',
    'lineage': {
        'predecessor_current_version': 'v0.3.6',
        'predecessor_current_tree': PREDECESSOR_CURRENT_TREE,
        'frozen_candidate3_identity': 'v0.3.7-candidate.3',
        'frozen_candidate3_source_commit': FROZEN_SOURCE,
        'frozen_candidate3_tree': FROZEN_TREE,
        'candidate3_exact_prefreeze_run': 33150269264,
        'candidate3_targeted_postfreeze_run': 33150553992,
        'candidate3_release_hardening_run': 33152201566,
        'candidate3_release_preparation_decision': 'RELEASE_PREPARATION_SUPPORTED',
        'candidate_succession_stop': True,
        'candidate4_required_by_current_evidence': False,
        'candidate2_fresh_a_s_sha256': '0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f',
        'candidate2_fresh_a_p_sha256': '80987d24a80c2aff90fddd96bc1891ee03c6ac02b25381d8af2a22418ebbe1db',
        'candidate2_phase_b_verdict': 'NEEDS_REVISION / CANDIDATE_3_REQUIRED',
    },
    'release_identity': {
        'immutable_effective_content_required': True,
        'validated_source_commit_or_tree_evidence_required': True,
        'package_digest_required': True,
        'exact_file_set_and_hash_parity_required': True,
        'published_readback_required': True,
        'bundled_manifest_alone_is_canonical_authority': False,
        'ordinary_adopter_must_repeat_release_author_ceremony': False,
        'frozen_source_is_release_semantic_source': True,
        'release_projection_may_change_identity_status_only_without_semantic_drift': True,
    },
    'release_thesis': cand.get('release_thesis', {}),
    'constitution': cand.get('constitution', {}),
    'semantic_trunk': cand.get('semantic_trunk', {}),
    'evolution': cand.get('evolution', {}),
    'operational_architecture': cand.get('operational_architecture', {}),
    'references': cand.get('references', {}),
    'tooling': cand.get('tooling', {}),
    'language': cand.get('language', {}),
    'accepted_residuals': cand.get('accepted_working_residuals', []),
    'evidence_boundaries': [
        'attack_cardinality = OPEN; observed corpora are not completeness proofs',
        'external mandate and credential authenticity are not established by represented Authority fields',
        'external Effect receipt authenticity and exactly-once execution are not established by reference validation',
        'imported source consistency does not authenticate source evidence or create receiver-local proof',
        'cross-environment candidate_id uniqueness is not universalized absent a governing contract',
        'natural fresh-session cue salience and Host application remain field evidence',
        'paired/structural zh-CN fixtures do not prove universal behavioral equivalence',
        'Host applicability and operational fitness remain environment-relative field evidence',
    ],
    'invariants': [
        'CURRENT_V037_IS_SINGULAR_ADOPTION_SURFACE',
        'FROZEN_CANDIDATE3_BYTES_REMAIN_OCCURRENCE_TRUTH',
        'BUNDLED_REFERENCE_NE_REQUIRED_RUNTIME_ORGAN',
        'REFERENCE_SCHEMA_NE_NORMATIVE_ENA_ONTOLOGY',
        'HOST_PATTERN_NE_UNIVERSAL_IMPLEMENTATION',
        'HOT_KERNEL_NE_FULL_HOW_LIBRARY',
        'SEMANTIC_TRUNK_STABILITY_NE_NO_RELEASE_VALUE',
        'IDENTITY_PROJECTION_NE_SEMANTIC_DRIFT',
        'MACHINE_PASS_NE_EXTERNAL_TRUTH',
        'TRANSLATED_NE_BEHAVIORALLY_EQUIVALENT',
    ],
    'profiles': ['LITE', 'STANDARD', 'HIGH_ASSURANCE', 'CUSTOM'],
    'lite_entrypoint': 'LITE-ADOPTION-INSTRUCTION.md',
    'runtime_adoption': {
        'kernel_entrypoint': 'RUNTIME-ADOPTION-KERNEL.md',
        'cue_index': 'operational/CUE-INDEX.md',
        'how_map': 'operational/HOW-MAP.md',
        'hot_kernel_should_load_full_how_library': False,
    },
    'field_validation': {
        'field_use_intended': True,
        'fresh_session_salience_application_proven': False,
        'universal_host_applicability_proven': False,
        'universal_bilingual_behavioral_equivalence_proven': False,
    },
    'core_files': [
        'README.md', '00-READ-ME-FIRST.md', 'CONSTITUTION-CONCEPT-MAP.yaml',
        '01-CONSTITUTION.md', '02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md',
        'RUNTIME-ADOPTION-KERNEL.md', '03-ROLES-AND-DEVELOPMENTAL-STAGES.md',
        '04-CAPABILITY-MAP.md', '05-CORE-OPERATIONAL-CONTRACTS.md',
        '06-EVOLUTION-KNOWLEDGE-AND-OPEN-PARTICIPATION.md',
        '07-ADOPTION-AND-FIELD-VALIDATION.md', '08-RELEASE-DISCIPLINE.md',
        '09-EVOLUTION-METABOLISM.md', '10-LANGUAGE-PORTABILITY.md',
        'SEMANTIC-GLOSSARY.yaml',
    ],
}

# Reconcile a few candidate-stage state labels inside retained metadata while
# leaving evidence/run lineage intact.
if isinstance(current['operational_architecture'], dict):
    current['operational_architecture']['state'] = 'CURRENT_MACHINE_CHECKED'
if isinstance(current['references'], dict):
    current['references']['state'] = 'CURRENT_BUNDLED_OPTIONAL_DEFAULT_OFF'
if isinstance(current['tooling'], dict):
    current['tooling']['state'] = 'CURRENT_FIELD_VALIDATION'
if isinstance(current['language'], dict):
    current['language']['state'] = 'CURRENT_OPERATIONAL_PROJECTION_FIELD_VALIDATION'

CURRENT.write_text(yaml.safe_dump(current, sort_keys=False, allow_unicode=True, width=110), encoding='utf-8')
CANDIDATE.unlink()

status_lines = {
    '00-READ-ME-FIRST.md': 'Status: **CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE**',
    '05-CORE-OPERATIONAL-CONTRACTS.md': 'Status: `CURRENT / FIELD_VALIDATION / CORE_OPERATIONAL_CONTRACT`.',
    '06-EVOLUTION-KNOWLEDGE-AND-OPEN-PARTICIPATION.md': 'Status: `CURRENT / FIELD_VALIDATION`.',
    '07-ADOPTION-AND-FIELD-VALIDATION.md': 'Status: `CURRENT / FIELD_VALIDATION`.',
    '08-RELEASE-DISCIPLINE.md': 'Status: `CURRENT / FIELD_VALIDATION / RELEASED`.',
    '09-EVOLUTION-METABOLISM.md': 'Status: `CURRENT / FIELD_VALIDATION`.',
    '10-LANGUAGE-PORTABILITY.md': 'Status: `CURRENT / FIELD_VALIDATION / OPERATIONAL_LANGUAGE_PROJECTION`.',
    'AGENT-ADOPTION-INSTRUCTION.md': 'Status: **CURRENT ADOPTION / FIELD_VALIDATION**.',
    'LITE-ADOPTION-INSTRUCTION.md': 'Status: `CURRENT / FIELD_VALIDATION / LITE PROFILE`.',
    'README.md': 'Status: **CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE**',
    'RUNTIME-ADOPTION-KERNEL.md': 'Status: `CURRENT / FIELD_VALIDATION / HOT_SEMANTIC_CUE_SURFACE`.',
    'CONTRIBUTION-PROTOCOL.md': 'Status: `CURRENT / FIELD_VALIDATION`.',
    'language-projections/zh-CN/00-READ-ME-FIRST.md': '状态：**CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE**',
    'language-projections/zh-CN/09-EVOLUTION-METABOLISM.md': '状态：`CURRENT / FIELD_VALIDATION`。',
    'language-projections/zh-CN/RUNTIME-ADOPTION-KERNEL.md': '状态：`CURRENT / FIELD_VALIDATION / HOT_SEMANTIC_CUE_SURFACE`。',
}

for rel, status in status_lines.items():
    p = ROOT / rel
    text = p.read_text(encoding='utf-8')
    lines = text.splitlines()
    for i in range(min(24, len(lines))):
        if i == 0:
            lines[i] = lines[i].replace('v0.3.7 candidate.3', 'v0.3.7').replace('v0.3.7-candidate.3', 'v0.3.7')
        if lines[i].startswith('Status:') or lines[i].startswith('状态：'):
            lines[i] = status
        if re.search(r'(active .*Current.*v0\.3\.6|active adopter baseline remains.*v0\.3\.6|current remains.*v0\.3\.6)', lines[i], re.I):
            lines[i] = 'The singular adopter-facing baseline is this `v0.3.7 / CURRENT / FIELD_VALIDATION` release.'
        if re.search(r'当前.*Current.*v0\.3\.6|当前唯一.*Current.*v0\.3\.6', lines[i], re.I):
            lines[i] = '当前唯一面向采用者的基线是本目录中的 `v0.3.7 / CURRENT / FIELD_VALIDATION`。'
    p.write_text('\n'.join(lines) + ('\n' if text.endswith('\n') else ''), encoding='utf-8')

# Machine-readable operational reference index.
p = ROOT / 'operational/REFERENCE-INDEX.yaml'
doc = yaml.safe_load(p.read_text(encoding='utf-8'))
doc['schema_version'] = '1.0'
doc.pop('candidate', None)
doc['release'] = 'v0.3.7'
doc['status'] = 'CURRENT_OPERATIONAL_REFERENCE_INDEX'
if isinstance(doc.get('routes', {}).get('OA-EVO-01'), dict):
    doc['routes']['OA-EVO-01']['tool_state'] = 'CURRENT_MACHINE_CHECKED'
p.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=110), encoding='utf-8')

# Optional reference manifest remains optional/default-off; only package identity changes.
p = ROOT / 'references/REFERENCE-MANIFEST.yaml'
doc = yaml.safe_load(p.read_text(encoding='utf-8'))
doc['schema_version'] = '1.0'
doc['status'] = 'CURRENT_OPTIONAL_REFERENCE_MANIFEST'
doc.pop('candidate', None)
doc['release'] = 'v0.3.7'
doc['assembly_state'] = 'RELEASED_MACHINE_CHECKED'
doc['policy']['normative_semantic_authority'] = 'v0.3.7 Current semantic trunk, not bundled reference schemas'
if 'deferred_not_bundled_first_candidate' in doc:
    doc['deferred_not_bundled'] = doc.pop('deferred_not_bundled_first_candidate')
if isinstance(doc.get('machine_evidence'), dict):
    verified = doc['machine_evidence'].get('verified', [])
    doc['machine_evidence']['verified'] = [x.replace('candidate-local', 'release-local') for x in verified]
p.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=110), encoding='utf-8')

# zh-CN projection identity/status binding.
p = ROOT / 'language-projections/zh-CN/projection-manifest.yaml'
doc = yaml.safe_load(p.read_text(encoding='utf-8'))
doc['schema_version'] = '2.0'
doc['projection_version'] = 'v0.3.7.zh-CN.1'
doc['source_semantic_version'] = 'v0.3.7'
doc['source_identity_binding'] = (
    'Release projection derives from frozen candidate.3 source '
    + FROZEN_SOURCE + ' / subtree ' + FROZEN_TREE
    + '; the promoted Current identity is the governed release effective-content tree, not a mutable branch label.'
)
doc['status'] = 'CURRENT_SEMANTIC_OPERATIONAL_PROJECTION'
doc['not_current'] = False
doc.pop('current_source_remains', None)
coverage = doc.get('coverage', {})
if 'candidate_operational_projection' in coverage:
    coverage['operational_projection'] = coverage.pop('candidate_operational_projection')
val = doc.get('validation', {})
if 'v037_candidate_operational_behavioral_conformance' in val:
    val['v037_operational_behavioral_conformance'] = val.pop('v037_candidate_operational_behavioral_conformance')
policy = doc.get('machine_artifact_policy', {})
if 'canonical_machine_reference_bytes' in policy:
    policy['canonical_machine_reference_bytes'] = 'Current machine paths under references/, schemas/, templates/, tools/'
known = doc.get('known_gaps', [])
doc['known_gaps'] = [
    x.replace('candidate identity/status-bearing zh-CN surfaces are reconciled to candidate.3 before exact pre-freeze validation.',
              'release identity/status-bearing zh-CN surfaces are bound to v0.3.7 Current while preserving frozen candidate lineage.')
    for x in known
]
doc['conflict_policy'] = (
    'A material discrepancy is a projection defect, not permission to choose whichever wording is convenient. '
    'Resolve against the v0.3.7 Current semantic/operational source, stable inherited Constitution IDs, and explicit evidence; '
    'record material reconciliation before any successor release.'
)
doc['evidence_boundary'] = [
    'TRANSLATED != BEHAVIORALLY_EQUIVALENT',
    'FIXTURE_DEFINED != MODEL_PASS',
    'RELEASE_IDENTITY != FIELD_TRUTH',
    'CURRENT_STATUS != UNIVERSAL_HOST_APPLICABILITY',
]
p.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=110), encoding='utf-8')

# Explicit identity-only schema title projection allowed by the candidate baseline.
p = ROOT / 'schemas/evolution-record.v2.schema.json'
text = p.read_text(encoding='utf-8')
old = 'ENA Evolution Candidate Record v2 (v0.3.7 candidate.3)'
new = 'ENA Evolution Record v2 (v0.3.7 Current)'
if text.count(old) != 1:
    raise SystemExit(f'unexpected schema title occurrence count: {text.count(old)}')
p.write_text(text.replace(old, new), encoding='utf-8')

# Preserve candidate.3 occurrence truth in lineage/changelog while making release state first-class.
lineage = ROOT / 'LINEAGE.md'
text = lineage.read_text(encoding='utf-8')
if not text.startswith('# ENA v0.3.7 Lineage'):
    prefix = f'''# ENA v0.3.7 Lineage\n\nStatus: `CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE`.\n\n## Release source and packaging lineage\n\n- predecessor Current: `v0.3.6`, tree `{PREDECESSOR_CURRENT_TREE}`;\n- frozen semantic/operational source: `v0.3.7-candidate.3`;\n- frozen source commit: `{FROZEN_SOURCE}`;\n- frozen subtree: `{FROZEN_TREE}`;\n- exact pre-freeze run: `33150269264` — SUCCESS;\n- targeted post-freeze run: `33150553992` — SUCCESS;\n- release hardening run: `33152201566` — SUCCESS;\n- release-preparation decision: `RELEASE_PREPARATION_SUPPORTED`;\n- candidate succession: `STOP`; candidate.4 not justified by current evidence.\n\nRelease packaging began with a byte-for-byte transplant of the frozen candidate.3 subtree into `releases/current/`. Subsequent differences are restricted to release identity/status/adoption/projection/validation packaging and must not silently change validated material semantics.\n\nThe candidate.3 and predecessor candidate sections below remain occurrence truth; release projection does not rewrite them into historical fiction.\n\n---\n\n'''
    lineage.write_text(prefix + text, encoding='utf-8')

changelog = ROOT / 'CHANGELOG.md'
text = changelog.read_text(encoding='utf-8')
if not text.startswith('# ENA Changelog\n\n## v0.3.7 — CURRENT'):
    prefix = '''# ENA Changelog\n\n## v0.3.7 — CURRENT / FIELD_VALIDATION\n\nPromotes the frozen candidate.3 semantic/operational package into the singular Current adoption surface after candidate succession converged and release preparation was explicitly supported.\n\nRelease value is primarily practical Operational Architecture: consequence-first Cue/HOW routing, selected optional/default-off reference organs, Host mappings, a narrow v2 evolution helper, and zh-CN operational projection while retaining the inherited 38-ID Constitution and semantic trunk.\n\nVisible evidence boundaries remain visible: attack cardinality is open; external mandate/receipt truth, universal Host applicability, natural future-session salience, and universal bilingual behavioral equivalence are not claimed.\n\nThe candidate.3 and predecessor sections below are preserved as development/evidence lineage.\n\n---\n\n'''
    # Avoid duplicating the old standalone '# ENA Changelog' that appears below candidate.1 history.
    changelog.write_text(prefix + text, encoding='utf-8')

print('V037_RELEASE_IDENTITY_STAGE1=PASS')
