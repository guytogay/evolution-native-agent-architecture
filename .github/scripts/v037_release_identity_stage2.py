#!/usr/bin/env python3
from pathlib import Path
import re, yaml

ROOT=Path('releases/current')
assert (ROOT/'CURRENT-BASELINE.yaml').is_file()
assert not (ROOT/'CANDIDATE-BASELINE.yaml').exists()

# Files where candidate.3 language is active package self-description, not lineage.
active_docs = [
 '00-READ-ME-FIRST.md','05-CORE-OPERATIONAL-CONTRACTS.md',
 '06-EVOLUTION-KNOWLEDGE-AND-OPEN-PARTICIPATION.md','07-ADOPTION-AND-FIELD-VALIDATION.md',
 '09-EVOLUTION-METABOLISM.md','10-LANGUAGE-PORTABILITY.md','AGENT-ADOPTION-INSTRUCTION.md',
 'LITE-ADOPTION-INSTRUCTION.md','README.md','RUNTIME-ADOPTION-KERNEL.md',
 'language-projections/zh-CN/00-READ-ME-FIRST.md','language-projections/zh-CN/09-EVOLUTION-METABOLISM.md',
 'language-projections/zh-CN/REFERENCE-GUIDE.md','language-projections/zh-CN/RUNTIME-ADOPTION-KERNEL.md',
]
active_docs += [p.relative_to(ROOT).as_posix() for p in (ROOT/'operational').rglob('*.md')]
active_docs += [p.relative_to(ROOT).as_posix() for p in (ROOT/'language-projections/zh-CN/operational').rglob('*.md')]
active_docs += [p.relative_to(ROOT).as_posix() for p in (ROOT/'references').rglob('README.md')]

for rel in sorted(set(active_docs)):
    p=ROOT/rel
    text=p.read_text(encoding='utf-8')
    text=text.replace('v0.3.7 candidate.3','v0.3.7 Current')
    text=text.replace('v0.3.7-candidate.3','v0.3.7')
    text=text.replace('Candidate.3','v0.3.7 Current')
    text=text.replace('candidate.3','v0.3.7 Current')
    text=text.replace('candidate-local','Current-local')
    text=text.replace('Candidate-local','Current-local')
    text=text.replace('CANDIDATE-BASELINE.yaml','CURRENT-BASELINE.yaml')
    text=text.replace('candidate review','Current adoption')
    text=text.replace('Candidate review','Current adoption')
    text=text.replace('candidate package','Current package')
    text=text.replace('Candidate package','Current package')
    # Remove stale working-candidate status tokens only on prose wrappers.
    lines=text.splitlines()
    for i,line in enumerate(lines):
        if line.startswith('Status:') or line.startswith('状态：'):
            line=line.replace('WORKING_CANDIDATE','CURRENT')
            line=line.replace('WORKING_OPERATIONAL_REFERENCE_INDEX','CURRENT_OPERATIONAL_REFERENCE_INDEX')
            line=re.sub(r'\s*/\s*NOT_CURRENT','',line)
            line=re.sub(r'\s*/\s*NOT_FROZEN','',line)
            line=re.sub(r'\s*/\s*NOT_RELEASED','',line)
            lines[i]=line
    p.write_text('\n'.join(lines)+('\n' if text.endswith('\n') else ''),encoding='utf-8')

# v0.3.7 Current field-validation narrative: replace obsolete pre-promotion tail only.
p=ROOT/'07-ADOPTION-AND-FIELD-VALIDATION.md'
text=p.read_text(encoding='utf-8')
text=text.replace('## Candidate-specific high-value tests','## v0.3.7 high-value field tests')
text=text.replace('candidate-specific author machine checks','release-source machine checks')
marker='## Before field validation can begin as a release claim'
if marker in text:
    before=text.split(marker,1)[0].rstrip()
    tail='''## Field-validation boundary\n\nv0.3.7 Current is intentionally `FIELD_VALIDATION`, not universal proof. Release validation establishes package identity, represented consistency, regression preservation, and deterministic distribution parity; it does not establish natural future-session salience, external-world authority/receipt truth, universal Host fitness, or bilingual behavioral equivalence.\n\nField findings must bind to the exact v0.3.7 Current identity and actual Host/model/language/configuration. Do not relabel predecessor v0.3.6 observations as v0.3.7 evidence without explicit applicability.\n\n> **Field validation asks whether the HOWs earn their cost in reality, not whether the release story sounds coherent.**\n'''
    text=before+'\n\n'+tail
p.write_text(text,encoding='utf-8')

# Release discipline: preserve candidate lineage but remove stale claims that Current is still v0.3.6.
p=ROOT/'08-RELEASE-DISCIPLINE.md'
text=p.read_text(encoding='utf-8')
text=text.replace('A deployable ENA adoption version must be self-contained and immutably identifiable. Candidate.3 is not Current and must not acquire release status by self-description.',
                  'A deployable ENA adoption version must be self-contained and immutably identifiable. v0.3.7 Current derives from governed release promotion of the exact frozen candidate.3 source; self-description alone never created that authority.')
text=text.replace('### v0.3.7 candidate.3 current state','### v0.3.7 frozen release-source lineage')
text=text.replace('`releases/current/` is still v0.3.6 and must not be edited as a side effect of candidate assembly.\n\nA material Current change requires a new release identity and explicit release decision.\n\nCandidate validation therefore checks Current isolation against the exact release-scope checkpoint.',
                  '`releases/current/` is the singular v0.3.7 adopter-facing surface after governed release promotion.\n\nA material Current change requires a new release identity and explicit release decision. Candidate validation preserved predecessor v0.3.6 Current isolation until release packaging began; that historical isolation evidence remains in candidate/reconciliation lineage.')
text=text.replace('Candidate.3 retains the zh-CN operational decision surfaces and v3 paired route fixtures.',
                  'v0.3.7 Current retains the zh-CN operational decision surfaces and v3 paired route fixtures.')
text=text.replace('Candidate.3 exposes one primary practical v2 path:', 'v0.3.7 Current exposes one primary practical v2 path:')
p.write_text(text,encoding='utf-8')

# Inherited active projection bindings that intentionally keep v0.3.6 semantics but now belong to v0.3.7 Current.
p=ROOT/'CONTRIBUTION-PROTOCOL.md'
text=p.read_text(encoding='utf-8').replace('# Contribution Protocol — v0.3.6 Current','# Contribution Protocol — v0.3.7 Current')
text=text.replace('A field finding that exposes a material defect in v0.3.6 may justify a future candidate/version;',
                  'A field finding that exposes a material defect in v0.3.7 may justify a future candidate/version;')
p.write_text(text,encoding='utf-8')

p=ROOT/'CONSTITUTION-CONCEPT-MAP.yaml'
text=p.read_text(encoding='utf-8')
text=text.replace('Cognitive/retrieval map for the inherited 38-ID ENA Constitution. v0.3.6\n  adds cue/index refinements without creating new Constitution rules.',
                  'Cognitive/retrieval map for the inherited 38-ID ENA Constitution. v0.3.7\n  retains all 38 IDs and adds Operational Architecture routing without creating new Constitution rules.')
p.write_text(text,encoding='utf-8')

p=ROOT/'SEMANTIC-GLOSSARY.yaml'
text=p.read_text(encoding='utf-8').replace('multilingual ENA v0.3.6 Current projections','multilingual ENA v0.3.7 Current projections')
p.write_text(text,encoding='utf-8')

p=ROOT/'language-projections/semantic-fixtures.v2.yaml'
text=p.read_text(encoding='utf-8').replace('Paired English/zh-CN decision-semantic scenarios for v0.3.6 Current ecology\n  semantics.',
                                             'Paired English/zh-CN decision-semantic scenarios for inherited ecology\n  semantics retained by v0.3.7 Current.')
p.write_text(text,encoding='utf-8')

p=ROOT/'templates/field-experience.v2.yaml'
text=p.read_text(encoding='utf-8').replace('ena_semantic_identity: "v0.3.6"','ena_semantic_identity: "v0.3.7"')
p.write_text(text,encoding='utf-8')

# zh-CN inherited semantic projection bindings.
p=ROOT/'language-projections/zh-CN/01-CONSTITUTION.md'
text=p.read_text(encoding='utf-8')
old='本文件是 v0.3.6 Current 对既有 38 条宪法的简体中文语义投影；这 38 条规则继承自 v0.3.5 Current，v0.3.6 没有新增 Constitution ID。'
new='本文件是 v0.3.7 Current 对既有 38 条宪法的简体中文语义投影；v0.3.7 继承 v0.3.6 的 38 条稳定规则，没有新增 Constitution ID。'
if old not in text: raise SystemExit('zh constitution release-binding sentence not found')
p.write_text(text.replace(old,new),encoding='utf-8')

for rel in ['language-projections/zh-CN/CONSTITUTION-CONCEPT-MAP.md','language-projections/zh-CN/SEMANTIC-GLOSSARY.zh-CN.yaml']:
    p=ROOT/rel
    text=p.read_text(encoding='utf-8').replace('v0.3.6 Current','v0.3.7 Current')
    p.write_text(text,encoding='utf-8')

# Projection manifest: frozen candidate binding is lineage, but active validation state is now release-facing.
p=ROOT/'language-projections/zh-CN/projection-manifest.yaml'
doc=yaml.safe_load(p.read_text(encoding='utf-8'))
doc['validation']['structural_parity']='CURRENT_DECISION_SURFACE_CHECKABLE'
p.write_text(yaml.safe_dump(doc,sort_keys=False,allow_unicode=True,width=110),encoding='utf-8')

print('V037_RELEASE_IDENTITY_STAGE2=PASS')
