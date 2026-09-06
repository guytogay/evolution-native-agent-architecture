from __future__ import annotations

from pathlib import Path
import json
import re
import subprocess
import yaml

ROOT = Path('.')
CUR = ROOT / 'releases/current'
OLD_VERSION = 'v0.3.9'
NEW_VERSION = 'v0.3.10'
PREDECESSOR_TREE = 'b2dfbe1c62a49a84696f01c4f4cb9b124094bad5'


def read(path: str | Path) -> str:
    return Path(path).read_text(encoding='utf-8')


def write(path: str | Path, text: str) -> None:
    Path(path).write_text(text, encoding='utf-8')


def replace_exact(path: str | Path, old: str, new: str, min_count: int = 1) -> int:
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    count = text.count(old)
    assert count >= min_count, f'{p}: expected at least {min_count} occurrences of {old!r}, got {count}'
    p.write_text(text.replace(old, new), encoding='utf-8')
    return count


# 1) Repair the full F-208-03 exact-phrase census by making stable cold surfaces version-neutral.
version_neutral_cold = [
    'releases/current/CONTRIBUTION-PROTOCOL.md',
    'releases/current/references/general/wait-state/README.md',
    'releases/current/references/general/authority-lease/README.md',
    'releases/current/references/general/effect-lifecycle/README.md',
    'releases/current/references/general/recovery-adapter/README.md',
    'releases/current/references/advanced/evidence-envelope/README.md',
    'releases/current/references/general/retrieval-obligation/README.md',
    'releases/current/references/advanced/contested-authorship/README.md',
    'releases/current/references/advanced/evidence-dependency-map/README.md',
    'releases/current/operational/procedures/STANDING-INPUT.md',
    'releases/current/05-CORE-OPERATIONAL-CONTRACTS.md',
    'releases/current/operational/patterns/HOST-MAPPINGS.md',
    'releases/current/operational/patterns/EVOLUTION-COMMONS.md',
    'releases/current/operational/procedures/CONTROL-RETIREMENT.md',
    'releases/current/operational/procedures/PURPOSE-RELATIVE-CONTINUITY.md',
    'releases/current/SEMANTIC-GLOSSARY.yaml',
    'releases/current/references/REFERENCE-MANIFEST.yaml',
    'releases/current/schemas/evolution-record.v2.schema.json',
    'releases/current/language-projections/semantic-fixtures.v2.yaml',
]

for rel in version_neutral_cold:
    replace_exact(rel, 'v0.3.7 Current', 'Current')

cap = CUR / '04-CAPABILITY-MAP.md'
cap_text = cap.read_text(encoding='utf-8')
old_cap_line = 'The v0.3.6 candidate inherits the explicit evolutionary-metabolism capabilities released through v0.3.5 Current:'
new_cap_line = 'The Current capability map retains the explicit evolutionary-metabolism capabilities represented in the v0.3.6 line:'
assert cap_text.count(old_cap_line) == 1
cap.write_text(cap_text.replace(old_cap_line, new_cap_line), encoding='utf-8')
version_neutral_cold.append(str(cap))

# 2) Move true release-bound surfaces from v0.3.9 to v0.3.10 without version-binding the stable cold library.
release_bound = [
    'releases/current/00-READ-ME-FIRST.md',
    'releases/current/07-ADOPTION-AND-FIELD-VALIDATION.md',
    'releases/current/08-RELEASE-DISCIPLINE.md',
    'releases/current/09-EVOLUTION-METABOLISM.md',
    'releases/current/10-LANGUAGE-PORTABILITY.md',
    'releases/current/ADOPTER-QUICKSTART.md',
    'releases/current/AGENT-ADOPTION-INSTRUCTION.md',
    'releases/current/LITE-ADOPTION-INSTRUCTION.md',
    'releases/current/RUNTIME-ADOPTION-KERNEL.md',
    'releases/current/language-projections/zh-CN/00-READ-ME-FIRST.md',
    'releases/current/language-projections/zh-CN/RUNTIME-ADOPTION-KERNEL.md',
]
for rel in release_bound:
    replace_exact(rel, OLD_VERSION, NEW_VERSION)

# Projection manifest is release-bound; cold zh-CN semantic files remain version-neutral.
manifest_path = CUR / 'language-projections/zh-CN/projection-manifest.yaml'
manifest = yaml.safe_load(manifest_path.read_text(encoding='utf-8'))
manifest['schema_version'] = '2.3'
manifest['projection_version'] = 'v0.3.10.zh-CN.1'
manifest['source_semantic_version'] = NEW_VERSION
manifest['release_identity']['current_version'] = NEW_VERSION
manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding='utf-8')

# 3) Current baseline: R0 identity successor, no semantic-law claim.
baseline_path = CUR / 'CURRENT-BASELINE.yaml'
b = yaml.safe_load(baseline_path.read_text(encoding='utf-8'))
assert b['ena_version'] == OLD_VERSION
b['schema_version'] = '3.5'
b['ena_version'] = NEW_VERSION
b['release_lane'] = 'R0_FIELD_PATCH_PUBLICATION_COHERENCE'
b['release_method'] = 'RAPID_CURRENT_SUCCESSION'
b['lineage']['predecessor_current_version'] = OLD_VERSION
b['lineage']['predecessor_current_tree'] = PREDECESSOR_TREE
b['lineage']['predecessor_role'] = 'ROLLBACK_AND_OCCURRENCE_TRUTH'
b['lineage']['source_release_branch'] = 'release/v0.3.10'
findings = list(b['lineage'].get('field_findings', []))
if 'F-208-03_ENGLISH_COLD_SURFACE_STALE_RELEASE_NARRATION' not in findings:
    findings.append('F-208-03_ENGLISH_COLD_SURFACE_STALE_RELEASE_NARRATION')
b['lineage']['field_findings'] = findings
b['release_thesis']['new_constitution_rule_required'] = '0_DEMONSTRATED'
b['release_thesis']['new_core_semantic_delta_required'] = '0_DEMONSTRATED'
b['release_thesis']['primary_delta'] = 'COLD_SURFACE_RELEASE_IDENTITY_DECOUPLING_AND_RECURRENCE_GATE'
b['release_thesis']['summary'] = (
    'Preserve v0.3.9 semantic and machine behavior while removing stale active release identity '
    'from stable English cold surfaces, retaining historical provenance where it is actually history, '
    'and extending Current validation so this narration defect class cannot silently recur.'
)
b['operational_architecture']['inherited_from'] = OLD_VERSION
b['operational_architecture']['route_structure_materially_rewritten'] = False
b['operational_architecture']['core_machine_behavior_materially_rewritten'] = False
b['release_identity']['cold_semantic_surfaces_version_neutral_by_default'] = True
b['release_identity']['historical_provenance_may_retain_source_version'] = True
b['field_validation']['post_release_findings_create_rapid_successor'] = True
residuals = [x for x in b.get('accepted_residuals', []) if 'Metamemory Update Policy v1 is a separate preregistered research round' not in x]
residuals.append('Metamemory Update Policy v1 completed its frozen primary with no replication trigger; its result is research evidence, not a mandatory Current trust-update threshold.')
residuals.append('Historical provenance may name predecessor versions; version-neutral cold-surface rules apply to active release/adoption narration, not occurrence truth.')
b['accepted_residuals'] = residuals
if 'COLD_SEMANTIC_SURFACE_NE_RELEASE_ID_LABEL_MAINTENANCE_BURDEN' not in b['invariants']:
    b['invariants'].append('COLD_SEMANTIC_SURFACE_NE_RELEASE_ID_LABEL_MAINTENANCE_BURDEN')
baseline_path.write_text(yaml.safe_dump(b, sort_keys=False, allow_unicode=True), encoding='utf-8')

# 4) Product-facing README surfaces.
write('README.md', '''# Evolution-Native Agent Architecture (ENA)\n\nENA is a design method, operational rule set, and conformance surface for Agents expected to learn, adapt, recover, use tools, affect external systems, and pass adaptations onward.\n\n**ENA exists to make sustained self-evolution viable.**\n\n> Evolution is the purpose. Governance protects evolvability.\n>\n> Governance must pay rent.\n>\n> Variation first; selection by reality.\n\n## Use ENA\n\nCurrent adoption truth is always:\n\n- machine identity: [`releases/current/CURRENT-BASELINE.yaml`](releases/current/CURRENT-BASELINE.yaml)\n- effective package: [`releases/current/`](releases/current/)\n\nCurrent is **v0.3.10 / FIELD_VALIDATION**.\n\n### Human adopter\n\nStart with [`releases/current/ADOPTER-QUICKSTART.md`](releases/current/ADOPTER-QUICKSTART.md).\n\n### Agent runtime\n\nThe **only default resident ENA text** is:\n\n[`releases/current/RUNTIME-ADOPTION-KERNEL.md`](releases/current/RUNTIME-ADOPTION-KERNEL.md)\n\nCue routing, HOWs, enforcement classification, fixtures, references, Constitution detail, and research lineage are retrieved only when the current decision needs them.\n\n```text\nAVAILABLE_RESOURCE != DEFAULT_HOT_PAYLOAD\nDEFAULT_AGENT_HOT_PAYLOAD = RUNTIME-ADOPTION-KERNEL.md\n```\n\nENA is not one giant prompt and does not require every bundled reference or private implementation name.\n\n## Current product direction\n\nv0.3.10 is an R0 publication-coherence successor to v0.3.9. It adds no Constitution IDs and does not rewrite core machine semantics.\n\nIssue #208 finding F-208-03 showed that stable English cold surfaces still carried old active-sounding release labels even after Current had moved. v0.3.10 makes those cold semantics version-neutral by default and extends the Current gate against recurrence, while preserving genuine historical provenance.\n\n```text\nCOLD_SEMANTIC_SURFACE != RELEASE_ID_LABEL_MAINTENANCE_BURDEN\nHISTORICAL_PROVENANCE != ACTIVE_RELEASE_IDENTITY\n```\n\n## Project work\n\nLive project state: [`NOW.md`](NOW.md)\n\nCurrent field stream: GitHub Issue **#208**.\n\nThe current evolutionary-memory mechanism-discrimination campaign is closed after the completed Metamemory Update Policy v1 primary. No mechanism experiment is active by default; new research must earn its own discriminator.\n\nOld plans, handoffs, candidate records, prototype workflows, adjudications, and research artifacts remain cold lineage. Retrieve them only when a concrete question requires them.\n\n## Repository shape\n\n- adoption truth: `releases/current/`\n- live project/research status: `NOW.md`\n- open field work: GitHub Issues\n- change history: Git / Pull Requests\n- detailed evidence/research: relevant `research/` or `evidence/` artifact\n\n```text\nRESEARCH_LINEAGE != ADOPTION_PAYLOAD\nIMMUTABLE_VERSION != IMMOBILE_CURRENT\nSOFT_GUIDANCE != HARD_ENFORCEMENT\n```\n\n## Participate\n\nENA is intended to be questioned, falsified, specialized, partially adopted, and improved. See [`CONTRIBUTING.md`](CONTRIBUTING.md).\n\n## License\n\nApache License 2.0. See [`LICENSE`](LICENSE).\n''')

write(CUR/'README.md', '''# ENA v0.3.10 — Current\n\nStatus: **CURRENT / FIELD_VALIDATION**\n\nv0.3.10 is the current adopter-facing ENA release.\n\nIt is an R0 publication-coherence successor to v0.3.9. The 38-ID Constitution and core behavior remain inherited; the change removes stale active release identity from stable cold surfaces and prevents that defect class from recurring.\n\n## One default hot payload\n\nFor an Agent, the only ENA text that should be resident by default is:\n\n`RUNTIME-ADOPTION-KERNEL.md`\n\nEverything else is cold/on-demand capability.\n\n```text\nDEFAULT_AGENT_HOT_PAYLOAD = RUNTIME-ADOPTION-KERNEL.md\nAVAILABLE_RESOURCE != DEFAULT_HOT_PAYLOAD\n```\n\n- Human integration guidance: `ADOPTER-QUICKSTART.md`\n- Bootstrap launcher: `AGENT-ADOPTION-INSTRUCTION.md`\n- Problem routing: `operational/CUE-INDEX.md`\n- HOW library: `operational/HOW-MAP.md`\n- Enforcement classification: `ENFORCEMENT-MAP.yaml`\n- Conformance evidence: semantic fixtures / executable validators\n- Deep semantics / lineage / research: retrieve only when decision-material\n\n## What changed from v0.3.9\n\nIssue #208 F-208-03 showed that Current still contained stable English cold surfaces labeled as `v0.3.7 Current` and one active-sounding `v0.3.6 candidate` narration.\n\nv0.3.10 therefore:\n\n- makes stable English cold semantics version-neutral by default;\n- preserves source-version text only where it is genuine historical provenance;\n- removes the stale active candidate narration from the Capability Map;\n- extends Current validation to reject old `vX.Y.Z Current` labels on designated version-neutral cold surfaces;\n- refines R0 protected-byte checks so release-label metadata can change without silently changing capability IDs or evolution-record schema behavior.\n\nNo new Constitution IDs are introduced and no Metamemory fixture policy is promoted into doctrine.\n\n## Evidence boundary\n\nMachine PASS proves only the exercised representation and regressions. Natural future-session salience, external authority/effect/recovery truth, universal Host fitness, and bilingual behavioral equivalence remain field evidence.\n\nA new bounded defect should create the smallest justified successor rather than silently rewrite v0.3.10.\n\n> **Version the identity surface; keep stable cold semantics stable.**\n''')

# 5) Changelog + lineage.
changelog = read(CUR/'CHANGELOG.md')
assert changelog.startswith('# ENA Changelog\n')
changelog = changelog.replace('## v0.3.9 — CURRENT / FIELD_VALIDATION', '## v0.3.9 — PREDECESSOR / RELEASED / FIELD_VALIDATION OCCURRENCE TRUTH', 1)
section = '''# ENA Changelog\n\n## v0.3.10 — CURRENT / FIELD_VALIDATION\n\nR0 publication-coherence successor driven by Current field stream #208.\n\n- closed F-208-03 by removing stale active release labels from stable English cold surfaces;\n- preserved genuine predecessor/source-version provenance instead of globally erasing history;\n- removed stale `v0.3.6 candidate` narration from the Current Capability Map;\n- extended Current validation with an English cold-surface stale-identity recurrence gate;\n- refined protected semantic/machine checks to allow metadata-only release-label repair while preserving capability IDs and evolution-record schema behavior;\n- kept the 38-ID Constitution and core runtime/evolution behavior unchanged.\n\n'''
changelog = section + changelog[len('# ENA Changelog\n\n'):]
write(CUR/'CHANGELOG.md', changelog)

write(CUR/'LINEAGE.md', f'''# ENA v0.3.10 Lineage\n\nStatus: `CURRENT / FIELD_VALIDATION`\n\n- predecessor Current: `v0.3.9`, tree `{PREDECESSOR_TREE}`;\n- source release branch: `release/v0.3.10`;\n- active field stream: Issue `#208`;\n- release lane: `R0_FIELD_PATCH_PUBLICATION_COHERENCE`;\n- primary field finding: `F-208-03` English cold-surface stale release narration.\n\nv0.3.9 remains immutable predecessor occurrence truth and rollback anchor. v0.3.10 does not rewrite it.\n\nThe release changes publication/release-identity narration and recurrence checks without adding Constitution IDs or demonstrating a core-contract semantic delta.\n\nFuture corrections require a successor version identity.\n''')

# 6) Live state surfaces: field stream active, mechanism-discrimination campaign closed.
write('NOW.md', '''# ENA — NOW\n\nThis is the default live project-status surface.\n\n## Current\n\n- `v0.3.10 / CURRENT / FIELD_VALIDATION`\n- authority: `releases/current/CURRENT-BASELINE.yaml`\n- effective adopter package: `releases/current/`\n- predecessor / rollback / occurrence truth: `v0.3.9`\n- field stream: GitHub Issue `#208` — version-neutral Current field validation\n\nv0.3.10 is an R0 publication-coherence successor. It preserves the 38-ID Constitution and core behavior while closing `F-208-03`: stable English cold surfaces no longer carry stale active release identities. Genuine historical provenance remains allowed.\n\n```text\nCOLD_SEMANTIC_SURFACE != RELEASE_ID_LABEL_MAINTENANCE_BURDEN\nHISTORICAL_PROVENANCE != ACTIVE_RELEASE_IDENTITY\n```\n\n## Adoption contract\n\n```text\nDEFAULT_AGENT_HOT_PAYLOAD = releases/current/RUNTIME-ADOPTION-KERNEL.md\nAVAILABLE_RESOURCE != DEFAULT_HOT_PAYLOAD\nHOT_KERNEL != FULL_HOW_LIBRARY\n```\n\nFor ordinary Agent runtime, only the Runtime Adoption Kernel is resident by default. Cue Index, HOW Map, Enforcement Map, fixtures, references, Constitution detail, and research lineage are cold/on-demand.\n\nHuman adopters start at `releases/current/ADOPTER-QUICKSTART.md`.\n\n## Release posture\n\n```text\nIMMUTABLE_VERSION != IMMOBILE_CURRENT\nPRESERVE_OLD_RELEASES + MOVE_CURRENT_QUICKLY\n```\n\nMethod: `research/methodology/RAPID-CURRENT-RELEASE-DISCIPLINE.md`\n\n- R0 — adoption / projection / bounded tooling or publication-coherence field patch: machine/regression/readback + rollback; fresh independent evidence may be post-release.\n- R1 — operational behavior change: targeted adversarial/independent evidence when decision-material.\n- R2 — core semantic/high-consequence change: heavy freeze/fresh falsification by default.\n\n## Active field stream\n\nIssue `#208` follows Current, not one release number. F-208-01/02/03 have produced rapid R0 successors; new bounded defects should continue to create the smallest justified successor instead of freezing Current.\n\n## Research status\n\nThe evolutionary-memory mechanism-discrimination campaign is **CLOSED**.\n\n- closure dispositions: `research/evolution-inbox/EVOLUTIONARY-MEMORY-CLOSURE-DISPOSITIONS.yaml`\n- broad-track audit: `research/field-validation/2026-09-06-evolutionary-memory-open-track-closure-audit.md`\n- final primary adjudication: `research/field-validation/2026-09-06-metamemory-update-policy-v1-adjudication.md`\n\nMetamemory Update Policy v1 completed four valid initial runs, triggered no preregistered replication condition, and was adjudicated `MECHANISM_ACTIVE_BUT_POLICY_OPTIMUM_UNRESOLVED / FIELD_UNRESOLVED_FOR_DURABLE_SELF_MODIFICATION / NO_CURRENT_SEMANTIC_CHANGE`.\n\nNo active mechanism primary remains. Reopen research only for a concrete decision-changing failure or a genuinely new non-derivable discriminator.\n\n## Open work\n\n- GitHub Issue `#208` — version-neutral Current field validation.\n- Continue reality contact; do not manufacture a new mechanism experiment merely because the previous campaign is closed.\n''')

handoff_path = Path('research/handoffs/CURRENT-HANDOFF.yaml')
h = yaml.safe_load(handoff_path.read_text(encoding='utf-8'))
h['schema_version'] = '5.1'
h['updated_at'] = '2026-09-06'
h['current_adoption']['version'] = NEW_VERSION
h['current_adoption']['predecessor_version'] = OLD_VERSION
h['current_adoption']['release_lane'] = 'R0_FIELD_PATCH_PUBLICATION_COHERENCE'
h['active_field_validation']['current_findings'] = [
    'F-208-01_DEFAULT_HOT_PAYLOAD_LIST_AMBIGUITY',
    'F-208-02_ROOT_AND_ZH_CN_IDENTITY_DRIFT',
    'F-208-03_ENGLISH_COLD_SURFACE_STALE_RELEASE_NARRATION',
]
h['active_field_validation']['next_product_rule'] = (
    'Continue the version-neutral Current field stream. A future bounded defect should create the smallest R0/R1/R2 successor; '
    'stable cold semantic surfaces remain version-neutral unless their meaning truly depends on release identity.'
)
h['open_work'] = {'github_issues': [208], 'product': [], 'research': []}
h['rule'] = (
    'ENA Current is v0.3.10 / FIELD_VALIDATION. Issue #208 is the version-neutral Current field stream. '
    'F-208-03 is closed by version-neutral English cold surfaces plus recurrence checks. '
    'The evolutionary-memory mechanism-discrimination campaign remains closed and no active mechanism primary remains.'
)
handoff_path.write_text(yaml.safe_dump(h, sort_keys=False, allow_unicode=True), encoding='utf-8')

# 7) Extend Current validation and move version assertions to v0.3.10.
cv_path = Path('.github/workflows/current-validate.yml')
cv = cv_path.read_text(encoding='utf-8')
assert cv.count("v0.3.9") >= 4
cv = cv.replace('v0.3.9', 'v0.3.10')

# 04 + evolution-record schema need metadata-only repair, so stop requiring byte identity for those two paths.
cv = cv.replace("              '04-CAPABILITY-MAP.md',\n", '')
cv = cv.replace("              'schemas/evolution-record.v2.schema.json',\n", '')

marker = "          print('ROOT_ZH_RELEASE_IDENTITY_PARITY_PASS')\n"
assert marker in cv
cold_repr = repr(version_neutral_cold)
injected = f'''          import re\n          en_cold = {cold_repr}\n          version_bound_current = re.compile(r'v0\\.3\\.\\d+\\s+Current', re.I)\n          for rel in en_cold:\n              text = Path(rel).read_text(encoding='utf-8')\n              hit = version_bound_current.search(text)\n              assert not hit, (rel, hit.group(0) if hit else None)\n          assert 'v0.3.6 candidate' not in (r/'04-CAPABILITY-MAP.md').read_text(encoding='utf-8')\n          print('ENGLISH_COLD_RELEASE_IDENTITY_PASS', len(en_cold))\n\n'''
cv = cv.replace(marker, injected + marker)

old_protected_print = "          print('R0_PROTECTED_BYTES_PASS', len(protected))\n"
assert old_protected_print in cv
special = '''          # Metadata-only F-208-03 repair must not change capability vocabulary or schema behavior.\n          import json, re\n          cap_now = re.findall(r'ENA-CAP-\\d{3}', (r/'04-CAPABILITY-MAP.md').read_text(encoding='utf-8'))\n          cap_old = re.findall(r'ENA-CAP-\\d{3}', (c/'04-CAPABILITY-MAP.md').read_text(encoding='utf-8'))\n          assert cap_now == cap_old\n          schema_now = json.loads((r/'schemas/evolution-record.v2.schema.json').read_text(encoding='utf-8'))\n          schema_old = json.loads((c/'schemas/evolution-record.v2.schema.json').read_text(encoding='utf-8'))\n          schema_now['title'] = schema_old['title']\n          assert schema_now == schema_old\n          print('R0_METADATA_NORMALIZED_SEMANTIC_PASS', len(cap_now))\n'''
cv = cv.replace(old_protected_print, old_protected_print + special)
cv_path.write_text(cv, encoding='utf-8')

# 8) Pre-commit assertions: no old active Current label remains on designated stable cold surfaces.
pattern = re.compile(r'v0\.3\.\d+\s+Current', re.I)
for rel in version_neutral_cold:
    txt = read(rel)
    assert not pattern.search(txt), (rel, pattern.search(txt).group(0) if pattern.search(txt) else None)
assert 'v0.3.6 candidate' not in read(CUR/'04-CAPABILITY-MAP.md')
assert yaml.safe_load(read(baseline_path))['ena_version'] == NEW_VERSION
assert yaml.safe_load(read(manifest_path))['source_semantic_version'] == NEW_VERSION
assert 'Current is **v0.3.10 / FIELD_VALIDATION**.' in read('README.md')
assert 'active_research:\n  state: NONE' in read(handoff_path)

# Historical provenance is intentionally retained where it is historical.
ref_manifest = yaml.safe_load(read(CUR/'references/REFERENCE-MANIFEST.yaml'))
assert ref_manifest['machine_evidence']['workflow'] == 'ENA v0.3.7 Candidate Assembly Gate'
assert ref_manifest['release'] == 'v0.3.7'

# 9) Restore the normal workflow and remove this branch-only runner before committing product changes.
subprocess.run(['git', 'fetch', 'origin', 'main'], check=True)
subprocess.run(['git', 'checkout', 'origin/main', '--', '.github/workflows/main-gate.yml'], check=True)
Path('research/_tmp_prepare_v0310.py').unlink()

subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'], check=True)
subprocess.run(['git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'], check=True)
subprocess.run(['git', 'add', '-A'], check=True)
status = subprocess.check_output(['git', 'status', '--porcelain'], text=True)
assert status.strip(), 'no staged v0.3.10 changes'
subprocess.run(['git', 'commit', '-m', 'Release ENA v0.3.10 publication-coherence R0 successor'], check=True)
subprocess.run(['git', 'push', 'origin', 'HEAD:release/v0.3.10'], check=True)
print('V0310_BRANCH_PREPARED_AND_PUSHED')
