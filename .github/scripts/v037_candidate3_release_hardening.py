#!/usr/bin/env python3
import json, re, sys
from pathlib import Path
import yaml

repo = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
cand = repo / 'releases/v0.3.7-candidate'
cur = repo / 'releases/current'

failures = []
observations = []

def req(cond, msg):
    if not cond:
        failures.append(msg)

def relfiles(root):
    return {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}

def read(p):
    return p.read_text(encoding='utf-8')

baseline = yaml.safe_load(read(cand/'CANDIDATE-BASELINE.yaml'))
current = yaml.safe_load(read(cur/'CURRENT-BASELINE.yaml'))

# 1) Adopter traversal / discoverability.
# Candidate baseline 3.1 does not carry a `core_files` list; use the actual adopter
# entry surfaces plus baseline-bound operational/evolution/tool paths instead.
for path in [
    'README.md','00-READ-ME-FIRST.md','RUNTIME-ADOPTION-KERNEL.md',
    '01-CONSTITUTION.md','02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md',
    '03-ROLES-AND-DEVELOPMENTAL-STAGES.md','04-CAPABILITY-MAP.md',
    '05-CORE-OPERATIONAL-CONTRACTS.md','06-EVOLUTION-KNOWLEDGE-AND-OPEN-PARTICIPATION.md',
    '07-ADOPTION-AND-FIELD-VALIDATION.md','08-RELEASE-DISCIPLINE.md',
    '09-EVOLUTION-METABOLISM.md','10-LANGUAGE-PORTABILITY.md',
]:
    req((cand/path).is_file(), f'missing adopter/core traversal surface: {path}')

op=baseline.get('operational_architecture',{})
for key in ['entrypoint','cue_index','how_map','reference_index']:
    path=op.get(key)
    req(bool(path) and (cand/path).is_file(), f'operational_architecture.{key} missing or unresolved: {path}')
for path in op.get('selected_procedures',[]) + op.get('selected_patterns',[]):
    req((cand/path).is_file(), f'selected operational path missing: {path}')

evo=baseline.get('evolution',{})
tooling=baseline.get('tooling',{})
for path in [
    evo.get('metabolism_entrypoint'), evo.get('evolution_record_schema'),
    evo.get('evolution_record_consistency_validator'), tooling.get('primary_v2_tool'),
    tooling.get('helper_selftest'), tooling.get('legacy_tool_target')
]:
    if path: req((cand/path).is_file(), f'baseline-bound runtime/tool path missing: {path}')

# Validate natural relative Markdown navigation inside package.
md_link = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
broken_links=[]
for p in cand.rglob('*.md'):
    for raw in md_link.findall(read(p)):
        target=raw.strip().split('#',1)[0]
        if not target or target.startswith(('http://','https://','mailto:','#')):
            continue
        target=target.split('?',1)[0]
        if target.startswith('/'):
            continue
        resolved=(p.parent/target).resolve()
        try: resolved.relative_to(cand.resolve())
        except ValueError: continue
        if not resolved.exists(): broken_links.append(f'{p.relative_to(cand)} -> {raw}')
req(not broken_links, 'broken relative Markdown links: ' + '; '.join(broken_links[:20]))

# 2) v0.3.6 -> v0.3.7 compatibility inventory.
cfiles=relfiles(cur); nfiles=relfiles(cand)
removed=sorted(cfiles-nfiles); added=sorted(nfiles-cfiles); common=sorted(cfiles & nfiles)
identical=[]; modified=[]
for f in common:
    (identical if (cur/f).read_bytes()==(cand/f).read_bytes() else modified).append(f)
observations.append(f'compat_files current={len(cfiles)} candidate={len(nfiles)} identical={len(identical)} modified={len(modified)} added={len(added)} removed={len(removed)}')
observations.append('compat_removed=' + json.dumps(removed,ensure_ascii=False))
observations.append('compat_added=' + json.dumps(added,ensure_ascii=False))

# Core adopter paths from Current must survive candidate succession.
for f in current.get('core_files',[]):
    req(f in nfiles, f'v0.3.6 core adopter path removed in candidate.3: {f}')

# Development baseline replacement is expected; three v0.3.6 top-level tools are
# deliberately demoted/relocated to compatibility history. Require exact bytes.
relocations={
    'tools/ena_evolve.py':'tools/legacy/ena_evolve_v1_2.py',
    'tools/candidate1_adversarial.py':'tools/legacy/candidate1_adversarial_v1_2.py',
    'tools/candidate2_adversarial.py':'tools/legacy/candidate2_adversarial_v1_2.py',
}
allowed_removed={'CURRENT-BASELINE.yaml',*relocations.keys()}
unexpected_removed=[f for f in removed if f not in allowed_removed]
req(not unexpected_removed, 'unexplained v0.3.6 file removals: ' + ', '.join(unexpected_removed))
for old,new in relocations.items():
    req((cand/new).is_file(), f'relocated compatibility target missing: {old} -> {new}')
    if (cand/new).is_file():
        req((cur/old).read_bytes()==(cand/new).read_bytes(), f'relocated compatibility bytes drifted: {old} -> {new}')
observations.append('compat_relocations_exact=' + json.dumps(relocations,ensure_ascii=False))

# Explicit inherited schemas remain present.
for path in ['schemas/evolution-record.v1.schema.json','schemas/adaptation-packet.v1.schema.json']:
    req((cand/path).is_file(), f'inherited compatibility schema missing: {path}')

# Constitution IDs are the stable semantic identity boundary.
ids=lambda text: sorted(set(re.findall(r'ENA-CON-\d{3}', text)))
cur_ids=ids(read(cur/'01-CONSTITUTION.md')); cand_ids=ids(read(cand/'01-CONSTITUTION.md'))
req(cur_ids==cand_ids, 'Constitution ID set changed between v0.3.6 Current and candidate.3')
req(len(cand_ids)==38, f'expected 38 Constitution IDs, observed {len(cand_ids)}')

# 3) Release-packaging transform readiness.
base_text=read(cand/'CANDIDATE-BASELINE.yaml')
req('v0.3.7-candidate.3' in base_text, 'candidate.3 identity not explicit in baseline')
req((cand/'CANDIDATE-BASELINE.yaml').exists(), 'candidate baseline missing')
req(not (cand/'CURRENT-BASELINE.yaml').exists(), 'candidate unexpectedly already contains CURRENT-BASELINE')
identity_surfaces=[]
for p in cand.rglob('*'):
    if p.is_file() and p.suffix in {'.md','.yaml','.yml','.json','.py'} and 'v0.3.7-candidate.3' in read(p):
        identity_surfaces.append(p.relative_to(cand).as_posix())
observations.append('candidate3_identity_surface_count=' + str(len(identity_surfaces)))
observations.append('candidate3_identity_surfaces=' + json.dumps(sorted(identity_surfaces),ensure_ascii=False))
req(len(identity_surfaces)>=5, 'too few explicit candidate.3 identity surfaces for auditable release projection')

# Frozen-candidate bytes intentionally retain pre-freeze self-description under the
# external-record freeze model. That is release projection work, not a candidate defect.
readme_head='\n'.join(read(cand/'README.md').splitlines()[:8])
rd_head='\n'.join(read(cand/'08-RELEASE-DISCIPLINE.md').splitlines()[:8])
req('candidate.3' in readme_head and 'NOT_CURRENT' in readme_head, 'README active candidate identity/status is not explicit')
req('candidate.3' in rd_head and 'NOT_CURRENT' in rd_head, 'Release Discipline active candidate identity/status is not explicit')
observations.append('release_identity_projection_required=true')
observations.append('candidate2_mentions_in_README=' + str(read(cand/'README.md').count('candidate.2')))
observations.append('candidate2_mentions_in_RELEASE_DISCIPLINE=' + str(read(cand/'08-RELEASE-DISCIPLINE.md').count('candidate.2')))
# Those predecessor mentions are legitimate only if the package explicitly labels lineage/preserved state.
req('## Lineage' in read(cand/'README.md') and 'Predecessor frozen candidate.2 subtree' in read(cand/'README.md'), 'README candidate.2 references lack explicit lineage framing')
req('Predecessor v0.3.7 candidate.2 preserved state' in read(cand/'08-RELEASE-DISCIPLINE.md'), 'Release Discipline candidate.2 references lack preserved-state framing')

# 4) Residual/evidence-boundary visibility.
alltxt='\n'.join(read(p) for p in cand.rglob('*') if p.is_file() and p.suffix in {'.md','.yaml','.yml','.json','.py'})
visibility={
 'attack_cardinality_or_completeness_boundary': ('attack_cardinality' in alltxt or 'completeness' in alltxt.lower()),
 'authority_external_authenticity_boundary': ('external_mandate_authenticity' in alltxt or 'external mandate authenticity' in alltxt.lower()),
 'effect_exactly_once_boundary': ('exactly_once' in alltxt or 'exactly-once' in alltxt.lower()),
 'source_receiver_evidence_boundary': ('receiver-local' in alltxt.lower() or 'receiver local' in alltxt.lower()),
 'host_relative_boundary': ('host-native' in alltxt.lower() or 'universal host applicability' in alltxt.lower()),
}
for k,v in visibility.items(): observations.append(f'residual_visibility {k}={v}')
for k in ['authority_external_authenticity_boundary','effect_exactly_once_boundary','source_receiver_evidence_boundary','host_relative_boundary']:
    req(visibility[k], f'material evidence boundary not visible in candidate package: {k}')
req('optional' in alltxt.lower(), 'candidate package does not visibly express optional reference semantics')
req(('default-off' in alltxt.lower() or 'default off' in alltxt.lower()), 'candidate package does not visibly express default-off semantics')

print('=== RELEASE HARDENING OBSERVATIONS ===')
for x in observations: print(x)
print('broken_relative_links=',len(broken_links))
print('constitution_ids=',len(cand_ids))
print('unexpected_unexplained_removed=',len(unexpected_removed))
if failures:
    print('=== RELEASE HARDENING FAILURES ===')
    for f in failures: print('FAIL:',f)
    raise SystemExit(1)
print('CANDIDATE3_RELEASE_HARDENING_MACHINE_AUDIT=PASS')
print('review_mode=PROJECT_MANAGER_RELEASE_HARDENING_NOT_FRESH_INDEPENDENT_REVIEW')
print('release_authority=NOT_ASSIGNED_BY_THIS_SCRIPT')
