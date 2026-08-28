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

# 1) Exact adopter entrypoints and core traversal.
baseline = yaml.safe_load(read(cand/'CANDIDATE-BASELINE.yaml'))
current = yaml.safe_load(read(cur/'CURRENT-BASELINE.yaml'))
core = baseline.get('core_files', [])
req(len(core) >= 10, 'candidate core_files unexpectedly shallow')
for path in core:
    req((cand/path).is_file(), f'missing candidate core file: {path}')
for keypath in [
    baseline.get('runtime_adoption',{}).get('kernel_entrypoint'),
    baseline.get('evolution',{}).get('metabolism_entrypoint'),
    baseline.get('evolution',{}).get('evolution_record_schema'),
    baseline.get('evolution',{}).get('evolution_record_consistency_validator'),
    baseline.get('lite_entrypoint'),
]:
    if keypath:
        req((cand/keypath).is_file(), f'baseline points to missing adopter/runtime path: {keypath}')

# Validate relative Markdown links across the candidate package.
md_link = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
broken_links=[]
for p in cand.rglob('*.md'):
    txt=read(p)
    for raw in md_link.findall(txt):
        target=raw.strip().split('#',1)[0]
        if not target or target.startswith(('http://','https://','mailto:','#')):
            continue
        target=target.split('?',1)[0]
        if target.startswith('/'):
            continue
        resolved=(p.parent/target).resolve()
        try:
            resolved.relative_to(cand.resolve())
        except ValueError:
            continue
        if not resolved.exists():
            broken_links.append(f'{p.relative_to(cand)} -> {raw}')
req(not broken_links, 'broken relative Markdown links: ' + '; '.join(broken_links[:20]))

# Known operational traversal surfaces.
for path in [
    'operational/OPERATIONAL-ARCHITECTURE.md',
    'operational/CUE-INDEX.md',
    'operational/REFERENCE-INDEX.md',
]:
    req((cand/path).is_file(), f'missing adopter operational traversal surface: {path}')

# 2) v0.3.6 -> v0.3.7 compatibility inventory.
cfiles = relfiles(cur)
nfiles = relfiles(cand)
removed = sorted(cfiles - nfiles)
added = sorted(nfiles - cfiles)
common = sorted(cfiles & nfiles)
identical=[]; modified=[]
for f in common:
    if (cur/f).read_bytes() == (cand/f).read_bytes(): identical.append(f)
    else: modified.append(f)
observations.append(f'compat_files current={len(cfiles)} candidate={len(nfiles)} identical={len(identical)} modified={len(modified)} added={len(added)} removed={len(removed)}')
observations.append('compat_removed=' + json.dumps(removed, ensure_ascii=False))
observations.append('compat_added=' + json.dumps(added, ensure_ascii=False))
# Candidate development packaging is expected to replace CURRENT-BASELINE with CANDIDATE-BASELINE.
allowed_removed={'CURRENT-BASELINE.yaml'}
unexpected_removed=[f for f in removed if f not in allowed_removed]
# Removal isn't automatically a blocker, but core/current contract surfaces must not vanish.
current_core=set(current.get('core_files',[]))
for f in current_core:
    req(f in nfiles, f'v0.3.6 core adopter path removed in candidate.3: {f}')
# v1 compatibility surfaces explicitly claimed by candidate must exist.
for f in [
    baseline.get('evolution',{}).get('inherited_evolution_record_schema'),
    baseline.get('evolution',{}).get('inherited_adaptation_packet_schema'),
    baseline.get('evolution',{}).get('inherited_reference_tool'),
]:
    if f: req((cand/f).is_file(), f'claimed inherited compatibility surface missing: {f}')
if unexpected_removed:
    observations.append('compat_noncore_removed_requires_release_review=' + json.dumps(unexpected_removed, ensure_ascii=False))

# Constitution stable ID compatibility.
ids=lambda text: sorted(set(re.findall(r'ENA-CON-\d{3}', text)))
cur_ids=ids(read(cur/'01-CONSTITUTION.md'))
cand_ids=ids(read(cand/'01-CONSTITUTION.md'))
req(cur_ids == cand_ids, f'Constitution ID set changed current={cur_ids} candidate={cand_ids}')
req(len(cand_ids)==38, f'expected 38 Constitution IDs, observed {len(cand_ids)}')

# 3) Release packaging transform readiness.
req(baseline.get('identity') == 'v0.3.7-candidate.3' or baseline.get('candidate_identity') == 'v0.3.7-candidate.3' or 'v0.3.7-candidate.3' in read(cand/'CANDIDATE-BASELINE.yaml'), 'candidate.3 identity not explicit in baseline')
req((cand/'CANDIDATE-BASELINE.yaml').exists(), 'candidate baseline missing')
req(not (cand/'CURRENT-BASELINE.yaml').exists(), 'candidate unexpectedly already contains CURRENT-BASELINE')
active_candidate_mentions=[]
for p in cand.rglob('*'):
    if not p.is_file() or p.suffix not in {'.md','.yaml','.yml','.json','.py'}: continue
    txt=read(p)
    if 'v0.3.7-candidate.3' in txt:
        active_candidate_mentions.append(p.relative_to(cand).as_posix())
observations.append('candidate3_identity_surface_count=' + str(len(active_candidate_mentions)))
observations.append('candidate3_identity_surfaces=' + json.dumps(sorted(active_candidate_mentions), ensure_ascii=False))
req(len(active_candidate_mentions) >= 5, 'too few explicit candidate.3 identity surfaces for auditable release projection')
# No candidate.2 identity should remain on active adopter-facing surfaces, excluding explicit history/lineage/changelog/legacy/probe fixtures.
stale=[]
for p in cand.rglob('*'):
    if not p.is_file() or p.suffix not in {'.md','.yaml','.yml','.json','.py'}: continue
    rel=p.relative_to(cand).as_posix()
    if any(tok in rel for tok in ['LINEAGE.md','CHANGELOG.md','CANDIDATE-BASELINE.yaml','tools/legacy/','fixtures/','regression','selftest']):
        continue
    txt=read(p)
    if 'v0.3.7-candidate.2' in txt or 'candidate.2' in txt:
        stale.append(rel)
req(not stale, 'stale candidate.2 identity on active non-history surfaces: ' + ', '.join(stale[:30]))

# 4) Residual/evidence-boundary visibility.
alltxt='\n'.join(read(p) for p in cand.rglob('*') if p.is_file() and p.suffix in {'.md','.yaml','.yml','.json','.py'})
visibility = {
    'attack_cardinality_or_completeness_boundary': ('attack_cardinality' in alltxt or 'completeness' in alltxt.lower()),
    'authority_external_authenticity_boundary': ('external_mandate_authenticity' in alltxt or 'external mandate authenticity' in alltxt.lower()),
    'effect_exactly_once_boundary': ('exactly_once' in alltxt or 'exactly-once' in alltxt.lower()),
    'source_receiver_evidence_boundary': ('receiver-local' in alltxt.lower() or 'receiver local' in alltxt.lower()),
    'host_relative_boundary': ('Host' in alltxt and ('environment-relative' in alltxt or 'host-native' in alltxt.lower())),
}
for k,v in visibility.items():
    observations.append(f'residual_visibility {k}={v}')
# attack-cardinality may be control-plane evidence rather than adopter contract, so do not require it in package.
for k in ['authority_external_authenticity_boundary','effect_exactly_once_boundary','source_receiver_evidence_boundary','host_relative_boundary']:
    req(visibility[k], f'material evidence boundary not visible in candidate package: {k}')

# Optional references should remain visibly optional/default-off somewhere in package semantics.
req('optional' in alltxt.lower(), 'candidate package does not visibly express optional reference semantics')
req(('default-off' in alltxt.lower() or 'default off' in alltxt.lower()), 'candidate package does not visibly express default-off semantics')

print('=== RELEASE HARDENING OBSERVATIONS ===')
for x in observations: print(x)
print('broken_relative_links=', len(broken_links))
print('constitution_ids=', len(cand_ids))
print('unexpected_noncore_removed=', len(unexpected_removed))
if failures:
    print('=== RELEASE HARDENING FAILURES ===')
    for f in failures: print('FAIL:', f)
    raise SystemExit(1)
print('CANDIDATE3_RELEASE_HARDENING_MACHINE_AUDIT=PASS')
print('review_mode=PROJECT_MANAGER_RELEASE_HARDENING_NOT_FRESH_INDEPENDENT_REVIEW')
print('release_authority=NOT_ASSIGNED_BY_THIS_SCRIPT')
