#!/usr/bin/env python3
import ast, json, re, sys
from pathlib import Path
import yaml

repo = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
cand = repo / 'releases/v0.3.7-candidate'
cur = repo / 'releases/current'
failures=[]; observations=[]

def req(cond,msg):
    if not cond: failures.append(msg)
def relfiles(root): return {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
def read(p): return p.read_text(encoding='utf-8')

def normalized_relocation_ast(path):
    tree=ast.parse(read(path))
    # Module docstrings are allowed to become truthful legacy/release-boundary narration.
    if tree.body and isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant) and isinstance(tree.body[0].value.value,str):
        tree.body=tree.body[1:]
    class N(ast.NodeTransformer):
        def visit_Constant(self,node):
            if isinstance(node.value,str):
                s=node.value
                s=s.replace('ena_evolve_v1_2.py','ena_evolve.py')
                s=s.replace('ena_evolve_candidate1_v1_2','ena_evolve_candidate1')
                s=s.replace('ena_evolve_candidate2_v1_2','ena_evolve_candidate2')
                return ast.copy_location(ast.Constant(value=s),node)
            return node
    tree=N().visit(tree); ast.fix_missing_locations(tree)
    return ast.dump(tree,annotate_fields=True,include_attributes=False)

baseline=yaml.safe_load(read(cand/'CANDIDATE-BASELINE.yaml'))
current=yaml.safe_load(read(cur/'CURRENT-BASELINE.yaml'))

# 1) Adopter traversal / discoverability.
for path in [
 'README.md','00-READ-ME-FIRST.md','RUNTIME-ADOPTION-KERNEL.md','01-CONSTITUTION.md',
 '02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md','03-ROLES-AND-DEVELOPMENTAL-STAGES.md',
 '04-CAPABILITY-MAP.md','05-CORE-OPERATIONAL-CONTRACTS.md','06-EVOLUTION-KNOWLEDGE-AND-OPEN-PARTICIPATION.md',
 '07-ADOPTION-AND-FIELD-VALIDATION.md','08-RELEASE-DISCIPLINE.md','09-EVOLUTION-METABOLISM.md','10-LANGUAGE-PORTABILITY.md']:
    req((cand/path).is_file(),f'missing adopter/core traversal surface: {path}')
op=baseline.get('operational_architecture',{})
for key in ['entrypoint','cue_index','how_map','reference_index']:
    path=op.get(key); req(bool(path) and (cand/path).is_file(),f'operational_architecture.{key} missing or unresolved: {path}')
for path in op.get('selected_procedures',[])+op.get('selected_patterns',[]): req((cand/path).is_file(),f'selected operational path missing: {path}')
evo=baseline.get('evolution',{}); tooling=baseline.get('tooling',{})
for path in [evo.get('metabolism_entrypoint'),evo.get('evolution_record_schema'),evo.get('evolution_record_consistency_validator'),tooling.get('primary_v2_tool'),tooling.get('helper_selftest'),tooling.get('legacy_tool_target')]:
    if path: req((cand/path).is_file(),f'baseline-bound runtime/tool path missing: {path}')
md_link=re.compile(r'\[[^\]]*\]\(([^)]+)\)'); broken_links=[]
for p in cand.rglob('*.md'):
    for raw in md_link.findall(read(p)):
        target=raw.strip().split('#',1)[0]
        if not target or target.startswith(('http://','https://','mailto:','#')): continue
        target=target.split('?',1)[0]
        if target.startswith('/'): continue
        resolved=(p.parent/target).resolve()
        try: resolved.relative_to(cand.resolve())
        except ValueError: continue
        if not resolved.exists(): broken_links.append(f'{p.relative_to(cand)} -> {raw}')
req(not broken_links,'broken relative Markdown links: '+'; '.join(broken_links[:20]))

# 2) v0.3.6 -> v0.3.7 compatibility inventory.
cfiles=relfiles(cur); nfiles=relfiles(cand); removed=sorted(cfiles-nfiles); added=sorted(nfiles-cfiles); common=sorted(cfiles & nfiles)
identical=[]; modified=[]
for f in common: (identical if (cur/f).read_bytes()==(cand/f).read_bytes() else modified).append(f)
observations += [f'compat_files current={len(cfiles)} candidate={len(nfiles)} identical={len(identical)} modified={len(modified)} added={len(added)} removed={len(removed)}','compat_removed='+json.dumps(removed,ensure_ascii=False),'compat_added='+json.dumps(added,ensure_ascii=False)]
for f in current.get('core_files',[]): req(f in nfiles,f'v0.3.6 core adopter path removed in candidate.3: {f}')
relocations={
 'tools/ena_evolve.py':'tools/legacy/ena_evolve_v1_2.py',
 'tools/candidate1_adversarial.py':'tools/legacy/candidate1_adversarial_v1_2.py',
 'tools/candidate2_adversarial.py':'tools/legacy/candidate2_adversarial_v1_2.py'}
allowed_removed={'CURRENT-BASELINE.yaml',*relocations.keys()}; unexpected=[f for f in removed if f not in allowed_removed]
req(not unexpected,'unexplained v0.3.6 file removals: '+', '.join(unexpected))
# Runtime legacy tool is exact-byte preserved.
req((cur/'tools/ena_evolve.py').read_bytes()==(cand/'tools/legacy/ena_evolve_v1_2.py').read_bytes(),'legacy ena_evolve runtime bytes drifted during relocation')
# Adversarial probes may truthfully change their docstring/import target/module name only.
for old,new in [('tools/candidate1_adversarial.py','tools/legacy/candidate1_adversarial_v1_2.py'),('tools/candidate2_adversarial.py','tools/legacy/candidate2_adversarial_v1_2.py')]:
    req((cand/new).is_file(),f'relocated probe missing: {new}')
    if (cand/new).is_file(): req(normalized_relocation_ast(cur/old)==normalized_relocation_ast(cand/new),f'relocated adversarial probe changed beyond explicit legacy path/narration adaptation: {old} -> {new}')
observations.append('compat_relocations=runtime_byte_exact_probes_normalized_ast_equivalent')
for path in ['schemas/evolution-record.v1.schema.json','schemas/adaptation-packet.v1.schema.json']: req((cand/path).is_file(),f'inherited compatibility schema missing: {path}')
ids=lambda text: sorted(set(re.findall(r'ENA-CON-\d{3}',text))); cur_ids=ids(read(cur/'01-CONSTITUTION.md')); cand_ids=ids(read(cand/'01-CONSTITUTION.md'))
req(cur_ids==cand_ids,'Constitution ID set changed between v0.3.6 Current and candidate.3'); req(len(cand_ids)==38,f'expected 38 Constitution IDs, observed {len(cand_ids)}')

# 3) Release packaging transform readiness.
base_text=read(cand/'CANDIDATE-BASELINE.yaml'); req('v0.3.7-candidate.3' in base_text,'candidate.3 identity not explicit in baseline')
req(not (cand/'CURRENT-BASELINE.yaml').exists(),'candidate unexpectedly already contains CURRENT-BASELINE')
identity=[]
for p in cand.rglob('*'):
    if p.is_file() and p.suffix in {'.md','.yaml','.yml','.json','.py'} and 'v0.3.7-candidate.3' in read(p): identity.append(p.relative_to(cand).as_posix())
observations += ['candidate3_identity_surface_count='+str(len(identity)),'candidate3_identity_surfaces='+json.dumps(sorted(identity),ensure_ascii=False)]
req(len(identity)>=5,'too few explicit candidate.3 identity surfaces for auditable release projection')
readme=read(cand/'README.md'); rd=read(cand/'08-RELEASE-DISCIPLINE.md')
req('candidate.3' in '\n'.join(readme.splitlines()[:8]) and 'NOT_CURRENT' in '\n'.join(readme.splitlines()[:8]),'README active candidate identity/status not explicit')
req('candidate.3' in '\n'.join(rd.splitlines()[:8]) and 'NOT_CURRENT' in '\n'.join(rd.splitlines()[:8]),'Release Discipline active candidate identity/status not explicit')
observations += ['release_identity_projection_required=true','candidate2_mentions_in_README='+str(readme.count('candidate.2')),'candidate2_mentions_in_RELEASE_DISCIPLINE='+str(rd.count('candidate.2'))]
req('## Lineage' in readme and 'Predecessor frozen candidate.2 subtree' in readme,'README predecessor references lack lineage framing')
req('Predecessor v0.3.7 candidate.2 preserved state' in rd,'Release Discipline predecessor references lack preserved-state framing')

# 4) Residual/evidence-boundary visibility.
alltxt='\n'.join(read(p) for p in cand.rglob('*') if p.is_file() and p.suffix in {'.md','.yaml','.yml','.json','.py'})
visibility={
 'attack_cardinality_or_completeness_boundary':('attack_cardinality' in alltxt or 'completeness' in alltxt.lower()),
 'authority_external_authenticity_boundary':('external_mandate_authenticity' in alltxt or 'external mandate authenticity' in alltxt.lower()),
 'effect_exactly_once_boundary':('exactly_once' in alltxt or 'exactly-once' in alltxt.lower()),
 'source_receiver_evidence_boundary':('receiver-local' in alltxt.lower() or 'receiver local' in alltxt.lower()),
 'host_relative_boundary':('host-native' in alltxt.lower() or 'universal host applicability' in alltxt.lower())}
for k,v in visibility.items(): observations.append(f'residual_visibility {k}={v}')
for k in ['authority_external_authenticity_boundary','effect_exactly_once_boundary','source_receiver_evidence_boundary','host_relative_boundary']: req(visibility[k],f'material evidence boundary not visible in candidate package: {k}')
req('optional' in alltxt.lower(),'candidate package does not visibly express optional reference semantics'); req(('default-off' in alltxt.lower() or 'default off' in alltxt.lower()),'candidate package does not visibly express default-off semantics')

print('=== RELEASE HARDENING OBSERVATIONS ===')
for x in observations: print(x)
print('broken_relative_links=',len(broken_links)); print('constitution_ids=',len(cand_ids)); print('unexpected_unexplained_removed=',len(unexpected))
if failures:
    print('=== RELEASE HARDENING FAILURES ===')
    for f in failures: print('FAIL:',f)
    raise SystemExit(1)
print('CANDIDATE3_RELEASE_HARDENING_MACHINE_AUDIT=PASS')
print('review_mode=PROJECT_MANAGER_RELEASE_HARDENING_NOT_FRESH_INDEPENDENT_REVIEW')
print('release_authority=NOT_ASSIGNED_BY_THIS_SCRIPT')
