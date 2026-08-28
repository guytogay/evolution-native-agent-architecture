#!/usr/bin/env python3
from pathlib import Path
import yaml

# Root metadata projection for the prospective v0.3.7 release payload.
meta_path=Path('PROJECT-METADATA.yaml')
meta=yaml.safe_load(meta_path.read_text(encoding='utf-8'))
entry=meta['entrypoints']
entry['primary_v2_evolution_tool']='releases/current/tools/ena_evolve_v2.py'
entry['inherited_reference_tool']='releases/current/tools/legacy/ena_evolve_v1_2.py'
cv=meta['current_validation']
cv['current_version']='v0.3.7'
cv['field_use_intended']=True
cv['field_participation_open']=True
cv['active_tracker']=None
cv['active_tracker_state']='POST_PROMOTION_BINDING_REQUIRED'
cv['predecessor_tracker']='GitHub Issue #70 (v0.3.6 field scope preserved as predecessor evidence)'
cv['focus']=[
  'Natural hot-cue -> cold-HOW retrieval and application without permanent HOW-library loading',
  'Operational routing economics: usefulness versus maintenance/governance/context burden',
  'False-BLOCK controls: NOT_REQUIRED / NOT_APPLICABLE / WAIT / UNKNOWN remain usable',
  'Optional/default-off reference applicability without normative or universal laundering',
  'Authority / Effect / Recovery composition under real external consequence',
  'Evolution Commons receiver-local reselection without source-proof laundering',
  'Purpose-relative continuity only where it changes a decision',
  'Standing input without sovereignty or authority creep',
  'Host-native mechanism equivalence and Host-relative fitness',
  'Primary v2 helper usefulness versus explicit legacy v1.2 compatibility boundary',
  'English / zh-CN operational route reachability and natural behavioral equivalence',
  'Unexpected counterexamples, new variations, and release residuals',
]
rc=meta['research_checkpoint']
rc['v037_frozen_candidate3_files']=118
rc['v037_inherited_composed_valid_cases']=164
rc['v037_successor_closure_cases']=61
rc['v037_v2_record_selftest_cases']=35
rc['v037_v2_helper_selftest_cases']=13
rc['v037_candidate3_exact_prefreeze_run']=33150269264
rc['v037_candidate3_targeted_postfreeze_run']=33150553992
rc['v037_candidate3_release_hardening_run']=33152201566
rc['counts_are_historical_observations_not_closure_thresholds']=True
meta_path.write_text(yaml.safe_dump(meta,sort_keys=False,allow_unicode=True,width=115),encoding='utf-8')

# v3 bilingual fixture is a release-bound test definition, not a behavior proof.
p=Path('releases/current/language-projections/semantic-fixtures.v3.yaml')
text=p.read_text(encoding='utf-8')
if 'schema_version: "3.0-candidate"' not in text:
    raise SystemExit('expected candidate-bound v3 fixture schema marker')
text=text.replace('schema_version: "3.0-candidate"','schema_version: "3.0"',1)
text=text.replace('Paired English/zh-CN decision-semantic fixtures for the v0.3.7 candidate\n  Operational Architecture.',
                  'Paired English/zh-CN decision-semantic fixtures for the v0.3.7 Current\n  Operational Architecture.',1)
text=text.replace('The candidate package contains Authority Lease and Evidence Envelope references.',
                  'The Current package contains Authority Lease and Evidence Envelope references.')
text=text.replace('candidate 包里带有 Authority Lease 和 Evidence Envelope reference。',
                  'Current 包里带有 Authority Lease 和 Evidence Envelope reference。')
p.write_text(text,encoding='utf-8')

print('V037_RELEASE_ROOT_PROJECTION=PASS')
